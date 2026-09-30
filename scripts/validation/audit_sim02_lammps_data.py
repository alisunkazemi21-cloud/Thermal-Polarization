"""Audit the imported SIM-02 LAMMPS data without advancing a trajectory."""

from __future__ import annotations

import argparse
import hashlib
import json
import math
from collections import defaultdict
from datetime import date
from pathlib import Path


SECTION_NAMES = {"Masses", "Atoms", "Velocities", "Bonds", "Angles"}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("data", type=Path)
    parser.add_argument("--json", type=Path, required=True)
    parser.add_argument("--report", type=Path, required=True)
    return parser.parse_args()


def minimum_image(delta: float, length: float) -> float:
    return delta - length * round(delta / length)


def parse_data(path: Path) -> dict:
    lines = path.read_text(encoding="utf-8").splitlines()
    counts: dict[str, int] = {}
    bounds: dict[str, tuple[float, float]] = {}
    sections: dict[str, list[str]] = defaultdict(list)
    current: str | None = None

    for raw in lines:
        line = raw.strip()
        base = line.split("#", 1)[0].strip()
        if not base:
            continue
        heading = base.split()[0]
        if heading in SECTION_NAMES:
            current = heading
            continue
        if current is None:
            fields = base.split()
            if len(fields) == 2 and fields[1] in {"atoms", "bonds", "angles"}:
                counts[fields[1]] = int(fields[0])
            elif len(fields) == 4 and fields[2:] in (["xlo", "xhi"], ["ylo", "yhi"], ["zlo", "zhi"]):
                bounds[fields[2][0]] = (float(fields[0]), float(fields[1]))
        else:
            sections[current].append(base)

    masses = {int(row.split()[0]): float(row.split()[1]) for row in sections["Masses"]}
    atoms = {}
    for row in sections["Atoms"]:
        f = row.split()
        atoms[int(f[0])] = {
            "molecule": int(f[1]),
            "type": int(f[2]),
            "charge": float(f[3]),
            "xyz": tuple(map(float, f[4:7])),
            "image": tuple(map(int, f[7:10])),
        }
    velocities = {int(row.split()[0]): tuple(map(float, row.split()[1:4])) for row in sections["Velocities"]}
    bonds = [tuple(map(int, row.split()[:4])) for row in sections["Bonds"]]
    angles = [tuple(map(int, row.split()[:5])) for row in sections["Angles"]]
    return {"counts": counts, "bounds": bounds, "masses": masses, "atoms": atoms, "velocities": velocities, "bonds": bonds, "angles": angles}


def nearest_oxygen_distance(oxygen_xyz: list[tuple[float, float, float]], lengths: tuple[float, float, float]) -> float:
    nx, ny, nz = (max(1, int(length / 3.0)) for length in lengths)
    cells: dict[tuple[int, int, int], list[int]] = defaultdict(list)
    for i, xyz in enumerate(oxygen_xyz):
        key = tuple(int((xyz[d] % lengths[d]) / lengths[d] * (nx, ny, nz)[d]) % (nx, ny, nz)[d] for d in range(3))
        cells[key].append(i)
    minimum = math.inf
    for key, members in cells.items():
        for dx in (-1, 0, 1):
            for dy in (-1, 0, 1):
                for dz in (-1, 0, 1):
                    other_key = ((key[0] + dx) % nx, (key[1] + dy) % ny, (key[2] + dz) % nz)
                    for i in members:
                        for j in cells.get(other_key, []):
                            if j <= i:
                                continue
                            delta = [minimum_image(oxygen_xyz[i][d] - oxygen_xyz[j][d], lengths[d]) for d in range(3)]
                            minimum = min(minimum, math.sqrt(sum(value * value for value in delta)))
    return minimum


def audit(data: dict, source: Path) -> dict:
    atoms = data["atoms"]
    bounds = data["bounds"]
    lengths = tuple(bounds[axis][1] - bounds[axis][0] for axis in "xyz")
    molecules: dict[int, list[int]] = defaultdict(list)
    for atom_id, atom in atoms.items():
        molecules[atom["molecule"]].append(atom_id)

    net_charge = sum(atom["charge"] for atom in atoms.values())
    molecule_charge_errors = []
    oh_distances = []
    hoh_angles = []
    reservoir_counts = {"hot": 0, "cold": 0, "bulk": 0}
    oxygen_wrapped = []

    for molecule_id, atom_ids in molecules.items():
        molecule_atoms = [atoms[atom_id] for atom_id in atom_ids]
        molecule_charge_errors.append(abs(sum(atom["charge"] for atom in molecule_atoms)))
        oxygens = [atom for atom in molecule_atoms if atom["type"] == 2]
        hydrogens = [atom for atom in molecule_atoms if atom["type"] == 1]
        if len(oxygens) != 1 or len(hydrogens) != 2:
            continue
        unwrapped = []
        for atom in molecule_atoms:
            unwrapped.append(tuple(atom["xyz"][d] + atom["image"][d] * lengths[d] for d in range(3)))
        by_type = [(atom, xyz) for atom, xyz in zip(molecule_atoms, unwrapped)]
        oxygen_xyz = next(xyz for atom, xyz in by_type if atom["type"] == 2)
        hydrogen_xyz = [xyz for atom, xyz in by_type if atom["type"] == 1]
        vectors = [tuple(h[d] - oxygen_xyz[d] for d in range(3)) for h in hydrogen_xyz]
        norms = [math.sqrt(sum(value * value for value in vector)) for vector in vectors]
        oh_distances.extend(norms)
        cosine = sum(vectors[0][d] * vectors[1][d] for d in range(3)) / (norms[0] * norms[1])
        hoh_angles.append(math.degrees(math.acos(max(-1.0, min(1.0, cosine)))))
        total_mass = sum(data["masses"][atom["type"]] for atom in molecule_atoms)
        com_z = sum(data["masses"][atom["type"]] * xyz[2] for (atom, xyz) in by_type) / total_mass
        wrapped_z = bounds["z"][0] + ((com_z - bounds["z"][0]) % lengths[2])
        if wrapped_z < bounds["z"][0] + 4.0 or wrapped_z >= bounds["z"][1] - 4.0:
            reservoir_counts["hot"] += 1
        elif -4.0 <= wrapped_z < 4.0:
            reservoir_counts["cold"] += 1
        else:
            reservoir_counts["bulk"] += 1
        oxygen_wrapped.append(tuple(bounds[axis][0] + ((oxygen_xyz[d] - bounds[axis][0]) % lengths[d]) for d, axis in enumerate("xyz")))

    volume_a3 = math.prod(lengths)
    mass_kg = len(molecules) * 18.01528e-3 / 6.02214076e23
    density_kg_m3 = mass_kg / (volume_a3 * 1e-30)
    digest = hashlib.sha256(source.read_bytes()).hexdigest()
    checks = {
        "atom_count": len(atoms) == 13500 == data["counts"].get("atoms"),
        "molecule_count": len(molecules) == 4500,
        "three_sites_per_molecule": all(len(ids) == 3 for ids in molecules.values()),
        "bond_count": len(data["bonds"]) == 9000 == data["counts"].get("bonds"),
        "angle_count": len(data["angles"]) == 4500 == data["counts"].get("angles"),
        "velocity_count": len(data["velocities"]) == 13500,
        "neutral_system": abs(net_charge) < 1e-10,
        "neutral_molecules": max(molecule_charge_errors) < 1e-12,
        "spce_oh_geometry": max(abs(value - 1.0) for value in oh_distances) < 1e-5,
        "spce_angle_geometry": max(abs(value - 109.47) for value in hoh_angles) < 1e-3,
    }
    return {
        "evidence_class": "MEASURED_ZERO_STEP_AUDIT",
        "date": str(date.today()),
        "source": str(source),
        "source_sha256": digest,
        "passed": all(checks.values()),
        "checks": checks,
        "observations": {
            "atoms": len(atoms),
            "molecules": len(molecules),
            "bonds": len(data["bonds"]),
            "angles": len(data["angles"]),
            "velocities": len(data["velocities"]),
            "box_angstrom": dict(zip("xyz", lengths)),
            "volume_angstrom3": volume_a3,
            "density_kg_m3": density_kg_m3,
            "net_charge_e": net_charge,
            "oh_distance_angstrom": {"min": min(oh_distances), "mean": sum(oh_distances) / len(oh_distances), "max": max(oh_distances)},
            "hoh_angle_degree": {"min": min(hoh_angles), "mean": sum(hoh_angles) / len(hoh_angles), "max": max(hoh_angles)},
            "reservoir_molecule_counts_by_com": reservoir_counts,
            "minimum_oxygen_oxygen_distance_angstrom": nearest_oxygen_distance(oxygen_wrapped, lengths),
        },
    }


def write_report(result: dict, path: Path) -> None:
    o = result["observations"]
    rows = "\n".join(f"| {name} | {'PASS' if passed else 'FAIL'} |" for name, passed in result["checks"].items())
    text = f"""# SIM-02 checkpoint 07 — zero-step structural audit

- **Evidence class:** `[MEASURED]` deterministic audit of the imported data file
- **Date:** {result['date']}
- **Overall:** {'PASS' if result['passed'] else 'FAIL'}
- **Trajectory advancement:** zero steps
- **SHA-256:** `{result['source_sha256']}`

## Checks

| Check | Result |
|---|---|
{rows}

## Observations

- Atoms / molecules: {o['atoms']} / {o['molecules']}
- Box: {o['box_angstrom']['x']:.12f} × {o['box_angstrom']['y']:.12f} × {o['box_angstrom']['z']:.12f} Å³
- Density from count and volume: {o['density_kg_m3']:.6f} kg m⁻³
- Net charge: {o['net_charge_e']:.3e} e
- O–H distance, min/mean/max: {o['oh_distance_angstrom']['min']:.9f} / {o['oh_distance_angstrom']['mean']:.9f} / {o['oh_distance_angstrom']['max']:.9f} Å
- H–O–H angle, min/mean/max: {o['hoh_angle_degree']['min']:.9f} / {o['hoh_angle_degree']['mean']:.9f} / {o['hoh_angle_degree']['max']:.9f}°
- Molecules by COM region: hot {o['reservoir_molecule_counts_by_com']['hot']}, cold {o['reservoir_molecule_counts_by_com']['cold']}, bulk {o['reservoir_molecule_counts_by_com']['bulk']}
- Minimum periodic O–O distance: {o['minimum_oxygen_oxygen_distance_angstrom']:.9f} Å

This report validates structure and region accounting only. It does not establish
equilibrium under the translated PPPM model, stationarity, a temperature
gradient, or thermopolarization.
"""
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def main() -> None:
    args = parse_args()
    result = audit(parse_data(args.data), args.data)
    args.json.parent.mkdir(parents=True, exist_ok=True)
    args.json.write_text(json.dumps(result, indent=2), encoding="utf-8")
    write_report(result, args.report)
    print(json.dumps({"passed": result["passed"], **result["observations"]}, indent=2))
    raise SystemExit(0 if result["passed"] else 1)


if __name__ == "__main__":
    main()

