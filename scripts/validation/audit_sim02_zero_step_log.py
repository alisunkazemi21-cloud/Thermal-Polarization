"""Convert the SIM-02 LAMMPS zero-step log into a compact audit record."""

from __future__ import annotations

import argparse
import json
import re
from datetime import date
from pathlib import Path


def required(pattern: str, text: str, label: str):
    match = re.search(pattern, text, re.MULTILINE)
    if not match:
        raise ValueError(f"missing {label}")
    return match


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("log", type=Path)
    parser.add_argument("--json", type=Path, required=True)
    args = parser.parse_args()
    text = args.log.read_text(encoding="utf-8")

    version = required(r"LAMMPS \(([^)]+)\)", text, "LAMMPS version").group(1)
    relative_accuracy = float(required(r"estimated relative force accuracy = ([0-9.eE+-]+)", text, "PPPM accuracy").group(1))
    thermo = required(
        r"^\s*0\s+13500\s+([0-9.eE+-]+)\s+([0-9.eE+-]+)\s+([0-9.eE+-]+)\s+([0-9.eE+-]+)\s+([0-9.eE+-]+)\s+([0-9.eE+-]+)\s+([0-9.eE+-]+)\s+([0-9.eE+-]+)\s+([0-9.eE+-]+)\s*$",
        text,
        "step-zero thermodynamics",
    )
    values = list(map(float, thermo.groups()))
    observations = {
        "lammps_version": version,
        "steps_advanced": 0,
        "atoms": 13500,
        "oxygen_atoms": 4500,
        "hydrogen_atoms": 9000,
        "rattle_frozen_angles": 4500,
        "pppm_relative_force_accuracy": relative_accuracy,
        "temperature_K": values[0],
        "pressure_atm": values[1],
        "potential_energy_kcal_mol": values[2],
        "kinetic_energy_kcal_mol": values[3],
        "total_energy_kcal_mol": values[4],
        "volume_angstrom3": values[5],
        "box_angstrom": {"x": values[6], "y": values[7], "z": values[8]},
    }
    checks = {
        "no_lammps_error": "ERROR" not in text,
        "zero_steps": bool(re.search(r"for 0 steps with 13500 atoms", text)),
        "atom_and_velocity_counts": text.count("13500 atoms") >= 1 and "13500 velocities" in text,
        "topology_counts": "9000 bonds" in text and "4500 angles" in text,
        "element_groups": "4500 atoms in group oxygen" in text and "9000 atoms in group hydrogen" in text,
        "rattle_clusters": "4500 = # of frozen angles" in text,
        "ehex_current_syntax": "region hot constrain com" in text and "region cold constrain com" in text,
        "pppm_accuracy": relative_accuracy <= 1.0e-5,
    }
    result = {
        "evidence_class": "MEASURED_ZERO_STEP_LAMMPS_AUDIT",
        "date": str(date.today()),
        "source_log": str(args.log),
        "passed": all(checks.values()),
        "checks": checks,
        "observations": observations,
        "interpretation": "Parser and force initialization only; no trajectory step was advanced.",
    }
    args.json.parent.mkdir(parents=True, exist_ok=True)
    args.json.write_text(json.dumps(result, indent=2), encoding="utf-8")
    print(json.dumps(result, indent=2))
    raise SystemExit(0 if result["passed"] else 1)


if __name__ == "__main__":
    main()
