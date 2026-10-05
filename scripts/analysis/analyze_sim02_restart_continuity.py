#!/usr/bin/env python3
"""Summarize the SIM-02 10 ps NVE restart-continuity preflight.

The script compares the uninterrupted trace against the two-segment trace at
matched 1 ps samples. It reports descriptive statistics only; it does not
assign an acceptance threshold or label statistical equivalence.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import math
import statistics
from pathlib import Path


def thermo_rows(path: Path) -> list[dict[str, float | int]]:
    rows: list[dict[str, float | int]] = []
    for line in path.read_text(encoding="utf-8", errors="replace").splitlines():
        fields = line.split()
        if len(fields) < 16 or fields[2] != "13500" or not fields[0].isdigit():
            continue
        rows.append(
            {
                "step": int(fields[0]),
                "temperature_K": float(fields[3]),
                "potential_energy_kcal_mol": float(fields[5]),
                "kinetic_energy_kcal_mol": float(fields[6]),
                "total_energy_kcal_mol": float(fields[7]),
                "com_speed_A_fs": float(fields[15]),
            }
        )
    return rows


def by_step(rows: list[dict[str, float | int]]) -> dict[int, dict[str, float | int]]:
    # If a run prints the initialization and post-adjustment state at the same
    # step, keep the last record, which is the state that starts integration.
    return {int(row["step"]): row for row in rows}


def mean_slope_and_change(
    samples: list[dict[str, float | int]], field: str
) -> tuple[float, float, float]:
    values = [float(row[field]) for row in samples]
    times_ps = [(int(row["step"]) - int(samples[0]["step"])) / 1000 for row in samples]
    x_bar = statistics.mean(times_ps)
    y_bar = statistics.mean(values)
    denominator = sum((x - x_bar) ** 2 for x in times_ps)
    slope = sum(
        (x - x_bar) * (y - y_bar) for x, y in zip(times_ps, values)
    ) / denominator
    return y_bar, slope, values[-1] - values[0]


def path_summary(samples: list[dict[str, float | int]]) -> dict[str, float | int]:
    mean_energy, energy_slope, endpoint_energy_change = mean_slope_and_change(
        samples, "total_energy_kcal_mol"
    )
    temperatures = [float(row["temperature_K"]) for row in samples]
    com = [float(row["com_speed_A_fs"]) for row in samples]
    return {
        "sample_count_1ps": len(samples),
        "mean_temperature_K": statistics.mean(temperatures),
        "sample_sd_temperature_K": statistics.stdev(temperatures),
        "mean_total_energy_kcal_mol": mean_energy,
        "fitted_total_energy_slope_kcal_mol_ps": energy_slope,
        "sampled_endpoint_total_energy_change_kcal_mol": endpoint_energy_change,
        "mean_com_speed_A_fs": statistics.mean(com),
        "maximum_sampled_com_speed_A_fs": max(com),
    }


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--raw-dir",
        type=Path,
        default=Path("results/raw/SIM-02/preflight-restart-continuity-2026-10-05"),
        help="directory containing continuous.log, split-first.log, and split-second.log",
    )
    parser.add_argument(
        "--csv",
        type=Path,
        default=Path("results/tables/SIM-02-preflight-continuity-2026-10-05.csv"),
    )
    parser.add_argument(
        "--summary",
        type=Path,
        default=Path("results/tables/SIM-02-preflight-continuity-2026-10-05-summary.json"),
    )
    args = parser.parse_args()

    continuous = by_step(thermo_rows(args.raw_dir / "continuous.log"))
    first = by_step(thermo_rows(args.raw_dir / "split-first.log"))
    second = by_step(thermo_rows(args.raw_dir / "split-second.log"))
    steps = list(range(22000, 32001, 1000))
    if any(step not in continuous for step in steps):
        raise SystemExit("Continuous log is missing one or more expected 1 ps samples")
    if any(step not in first for step in range(22000, 27001, 1000)):
        raise SystemExit("First split log is missing one or more expected samples")
    if any(step not in second for step in range(27000, 32001, 1000)):
        raise SystemExit("Second split log is missing one or more expected samples")

    split = {**first, **second}
    paired_rows: list[dict[str, float | int]] = []
    for step in steps:
        continuous_row = continuous[step]
        split_row = split[step]
        paired_rows.append(
            {
                "step": step,
                "elapsed_ps_from_stage_c_start": (step - 22000) / 1000,
                "continuous_temperature_K": continuous_row["temperature_K"],
                "split_temperature_K": split_row["temperature_K"],
                "temperature_difference_split_minus_continuous_K": (
                    float(split_row["temperature_K"])
                    - float(continuous_row["temperature_K"])
                ),
                "continuous_total_energy_kcal_mol": continuous_row[
                    "total_energy_kcal_mol"
                ],
                "split_total_energy_kcal_mol": split_row["total_energy_kcal_mol"],
                "total_energy_difference_split_minus_continuous_kcal_mol": (
                    float(split_row["total_energy_kcal_mol"])
                    - float(continuous_row["total_energy_kcal_mol"])
                ),
                "continuous_com_speed_A_fs": continuous_row["com_speed_A_fs"],
                "split_com_speed_A_fs": split_row["com_speed_A_fs"],
            }
        )

    args.csv.parent.mkdir(parents=True, exist_ok=True)
    with args.csv.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(paired_rows[0]))
        writer.writeheader()
        writer.writerows(paired_rows)

    continuous_samples = [continuous[step] for step in steps]
    split_samples = [split[step] for step in steps]
    boundary_energy_jump = (
        float(second[27000]["total_energy_kcal_mol"])
        - float(first[27000]["total_energy_kcal_mol"])
    )
    boundary_temperature_jump = (
        float(second[27000]["temperature_K"])
        - float(first[27000]["temperature_K"])
    )
    post_restart_energy_differences = [
        float(second[step]["total_energy_kcal_mol"])
        - float(continuous[step]["total_energy_kcal_mol"])
        for step in range(27000, 32001, 1000)
    ]
    summary = {
        "status": "descriptive preflight complete; statistical-equivalence acceptance not adjudicated",
        "reason": "DECISION-014 specifies statistical agreement but freezes no quantitative acceptance threshold for this 10 ps test.",
        "sampling": "paired 1 ps thermo samples; n=11 per path; samples are not independent replicates",
        "continuous": path_summary(continuous_samples),
        "split_restart": path_summary(split_samples),
        "restart_boundary_at_step_27000": {
            "total_energy_jump_kcal_mol_split_minus_first": boundary_energy_jump,
            "temperature_jump_K_split_minus_first": boundary_temperature_jump,
        },
        "paired_energy_difference_after_restart": {
            "maximum_absolute_kcal_mol": max(map(abs, post_restart_energy_differences)),
            "root_mean_square_kcal_mol": math.sqrt(
                statistics.mean(value**2 for value in post_restart_energy_differences)
            ),
            "endpoint_kcal_mol_split_minus_continuous": post_restart_energy_differences[-1],
        },
        "sha256": {
            "source_stage_b_restart": {
                "path": "results/raw/SIM-02/checkpoint-12-four-rank-high-cadence/stage-b-2ps-four-rank.restart",
                "digest": sha256(Path("results/raw/SIM-02/checkpoint-12-four-rank-high-cadence/stage-b-2ps-four-rank.restart")),
            },
            "inputs": {
                path.as_posix(): sha256(path)
                for path in (
                    Path("simulations/SIM-02/lammps/in.preflight-restart-continuity-10ps"),
                    Path("simulations/SIM-02/lammps/in.preflight-restart-continuity-5ps-first"),
                    Path("simulations/SIM-02/lammps/in.preflight-restart-continuity-5ps-second"),
                )
            },
            "raw_artifacts": {
                path.name: sha256(path)
                for path in sorted(args.raw_dir.iterdir())
                if path.is_file() and path.suffix in {".log", ".stdout", ".stderr", ".restart"}
            },
        },
        "outputs": {
            "paired_csv": str(args.csv),
            "summary_json": str(args.summary),
        },
    }
    args.summary.parent.mkdir(parents=True, exist_ok=True)
    args.summary.write_text(json.dumps(summary, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(summary, indent=2))


if __name__ == "__main__":
    main()
