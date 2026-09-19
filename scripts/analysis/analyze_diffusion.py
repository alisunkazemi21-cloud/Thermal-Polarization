#!/usr/bin/env python3
"""
analyze_diffusion.py

SIM-01 (SPC/E equilibrium validation): self-diffusion coefficient from
the production trajectory via the Einstein relation

    MSD(t) = 6 D t   (three-dimensional diffusion)

using MDAnalysis.analysis.msd.EinsteinMSD on oxygen-atom positions.

CAVEATS — state these explicitly in the validation report, do not drop them:
  1. Oxygen-atom position is used as a proxy for the molecular center of
     mass. For rigid SPC/E water these are close but not identical.
  2. A 1 ns production trajectory gives limited statistics for a
     diffusive fit. Report the fitted value AND its uncertainty, and
     treat it as provisional, not a converged literature-grade estimate.
  3. If production ran under NPT (Parrinello-Rahman, see md.mdp), volume
     fluctuations can add noise to the MSD. Note this, do not hide it.

All numbers here are [TO MEASURE].

Usage
-----
    python scripts/analysis/analyze_diffusion.py \
        --tpr simulations/SIM-01/md.tpr \
        --xtc simulations/SIM-01/md.xtc
"""

import argparse
import sys
from pathlib import Path

import numpy as np
import MDAnalysis as mda
from MDAnalysis.analysis.msd import EinsteinMSD

try:
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
except ImportError:
    plt = None


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                  formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--tpr", required=True, type=Path)
    ap.add_argument("--xtc", required=True, type=Path)
    ap.add_argument("--fit-start-frac", type=float, default=0.2,
                     help="Start of linear-fit window as a fraction of the MSD curve")
    ap.add_argument("--fit-end-frac", type=float, default=0.8,
                     help="End of linear-fit window as a fraction of the MSD curve")
    ap.add_argument("--out-table", type=Path, default=Path("results/tables/msd_oxygen.csv"))
    ap.add_argument("--out-figure", type=Path, default=Path("results/figures/msd_oxygen.png"))
    args = ap.parse_args()

    if not args.tpr.exists() or not args.xtc.exists():
        print("[ERROR] Missing tpr/xtc input — this script performs no calculation "
              "without a real trajectory.", file=sys.stderr)
        sys.exit(1)

    u = mda.Universe(str(args.tpr), str(args.xtc))
    oxygens = u.select_atoms("name OW")
    if len(oxygens) == 0:
        print("[ERROR] No atoms matched selection 'name OW'.", file=sys.stderr)
        sys.exit(1)

    msd_analysis = EinsteinMSD(oxygens, select="all", msd_type="xyz", fft=True)
    msd_analysis.run()
    msd = msd_analysis.results.timeseries  # Angstrom^2

    dt_ps = u.trajectory.dt
    lagtimes_ps = np.arange(len(msd)) * dt_ps

    n = len(msd)
    i0 = int(args.fit_start_frac * n)
    i1 = int(args.fit_end_frac * n)
    if i1 <= i0 + 1:
        print("[ERROR] Fit window too narrow — check --fit-start-frac/--fit-end-frac "
              "against the actual trajectory length.", file=sys.stderr)
        sys.exit(1)

    coeffs, cov = np.polyfit(lagtimes_ps[i0:i1], msd[i0:i1], 1, cov=True)
    slope_A2_per_ps = coeffs[0]
    slope_err = float(np.sqrt(cov[0, 0]))

    # D = slope / 6 (3D Einstein relation). Convert Angstrom^2/ps -> m^2/s:
    # 1 Angstrom^2 = 1e-20 m^2 ; 1 ps = 1e-12 s -> factor 1e-8
    D_m2_s = (slope_A2_per_ps / 6.0) * 1e-8
    D_err_m2_s = (slope_err / 6.0) * 1e-8

    print("[TO MEASURE] Self-diffusion coefficient (oxygen-atom proxy, real trajectory data):")
    print(f"  Fit window: {lagtimes_ps[i0]:.1f}-{lagtimes_ps[i1-1]:.1f} ps "
          f"(fractions {args.fit_start_frac}-{args.fit_end_frac} of the MSD curve)")
    print(f"  D = {D_m2_s:.3e} +/- {D_err_m2_s:.3e} m^2/s")
    print("  Provisional 1 ns estimate — do not treat as converged without an "
          "independent replicate or a longer run.")

    args.out_table.parent.mkdir(parents=True, exist_ok=True)
    np.savetxt(args.out_table, np.column_stack([lagtimes_ps, msd]),
               header="lag_time_ps,msd_A2", delimiter=",", comments="")
    print(f"Saved: {args.out_table}")

    if plt is not None:
        args.out_figure.parent.mkdir(parents=True, exist_ok=True)
        fig, ax = plt.subplots(figsize=(6, 4.5))
        ax.plot(lagtimes_ps, msd, lw=1.0, label="MSD (oxygen)")
        fit_line = coeffs[0] * lagtimes_ps[i0:i1] + coeffs[1]
        ax.plot(lagtimes_ps[i0:i1], fit_line, "k--", lw=1.2, label="linear fit region")
        ax.set_xlabel("Lag time (ps)")
        ax.set_ylabel(r"MSD ($\mathrm{\AA}^2$)")
        ax.legend()
        fig.tight_layout()
        fig.savefig(args.out_figure, dpi=150)
        print(f"Saved: {args.out_figure}")


if __name__ == "__main__":
    main()
