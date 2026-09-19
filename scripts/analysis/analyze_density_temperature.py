#!/usr/bin/env python3
"""
analyze_density_temperature.py

SIM-01 (SPC/E equilibrium validation): extract density and temperature
statistics from the production-run GROMACS energy file.

This script does NOT compute density/temperature itself — it parses the
.xvg output produced by `gmx energy` (see results/reports/SIM-01-validation.md
for the exact command and interactive selection order: "Density" then
"Temperature", in that order).

All numbers this script prints or saves are [TO MEASURE]. Nothing here is
a literature value; literature comparison happens in the validation report.

Usage
-----
    gmx energy -f simulations/SIM-01/md.edr \
        -o results/tables/density_temperature.xvg
    (at the interactive prompt: select Density, then Temperature, then Ctrl+D)

    python scripts/analysis/analyze_density_temperature.py \
        --xvg results/tables/density_temperature.xvg \
        --skip-ps 0
"""

import argparse
import sys
from pathlib import Path

import numpy as np
import pandas as pd

try:
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
except ImportError:
    plt = None


def read_xvg(path: Path) -> pd.DataFrame:
    """Read a two-column gmx energy .xvg file (Density, Temperature),
    skipping @/# header lines. Column order must match the order the
    quantities were selected in at the `gmx energy` prompt.
    """
    rows = []
    with open(path, "r") as fh:
        for line in fh:
            line = line.strip()
            if not line or line.startswith(("@", "#")):
                continue
            parts = line.split()
            rows.append([float(x) for x in parts])
    if not rows:
        raise ValueError(f"No data rows found in {path}")
    arr = np.array(rows)
    if arr.shape[1] < 3:
        raise ValueError(
            f"Expected time + Density + Temperature (3 columns), found "
            f"{arr.shape[1]} in {path}. Re-check the gmx energy selection order."
        )
    return pd.DataFrame(arr[:, :3], columns=["time_ps", "density_kg_m3", "temperature_K"])


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                  formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--xvg", required=True, type=Path,
                     help="Path to gmx energy .xvg output (Density, Temperature)")
    ap.add_argument("--skip-ps", type=float, default=0.0,
                     help="Discard samples before this time (ps) as extra equilibration margin")
    ap.add_argument("--out-table", type=Path,
                     default=Path("results/tables/density_temperature_summary.csv"))
    ap.add_argument("--out-figure", type=Path,
                     default=Path("results/figures/density_temperature.png"))
    args = ap.parse_args()

    if not args.xvg.exists():
        print(f"[ERROR] Input file not found: {args.xvg}", file=sys.stderr)
        print("This script performs no calculation without real gmx energy output.",
              file=sys.stderr)
        sys.exit(1)

    df = read_xvg(args.xvg)
    used = df[df["time_ps"] >= args.skip_ps]
    if used.empty:
        print("[ERROR] No samples remain after applying --skip-ps.", file=sys.stderr)
        sys.exit(1)

    summary = {
        "n_samples": int(len(used)),
        "time_start_ps": float(used["time_ps"].min()),
        "time_end_ps": float(used["time_ps"].max()),
        "density_mean_kg_m3": float(used["density_kg_m3"].mean()),
        "density_std_kg_m3": float(used["density_kg_m3"].std(ddof=1)),
        "temperature_mean_K": float(used["temperature_K"].mean()),
        "temperature_std_K": float(used["temperature_K"].std(ddof=1)),
    }

    print("[TO MEASURE] Density and temperature summary (real gmx energy output):")
    for k, v in summary.items():
        print(f"  {k}: {v}")

    args.out_table.parent.mkdir(parents=True, exist_ok=True)
    pd.DataFrame([summary]).to_csv(args.out_table, index=False)
    print(f"Saved: {args.out_table}")

    if plt is not None:
        args.out_figure.parent.mkdir(parents=True, exist_ok=True)
        fig, axes = plt.subplots(2, 1, figsize=(7, 6), sharex=True)
        axes[0].plot(used["time_ps"], used["density_kg_m3"], lw=0.8)
        axes[0].axhline(summary["density_mean_kg_m3"], color="k", ls="--", lw=0.8)
        axes[0].set_ylabel("Density (kg/m$^3$)")
        axes[1].plot(used["time_ps"], used["temperature_K"], lw=0.8, color="tab:orange")
        axes[1].axhline(summary["temperature_mean_K"], color="k", ls="--", lw=0.8)
        axes[1].set_ylabel("Temperature (K)")
        axes[1].set_xlabel("Time (ps)")
        fig.tight_layout()
        fig.savefig(args.out_figure, dpi=150)
        print(f"Saved: {args.out_figure}")
    else:
        print("[WARNING] matplotlib not available in this environment — figure not generated.")


if __name__ == "__main__":
    main()
