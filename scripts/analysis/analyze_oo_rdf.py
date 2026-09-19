#!/usr/bin/env python3
"""
analyze_oo_rdf.py

SIM-01 (SPC/E equilibrium validation): oxygen-oxygen radial distribution
function g_OO(r), computed directly from the production trajectory with
MDAnalysis (MDAnalysis.analysis.rdf.InterRDF), selecting oxygen atoms
explicitly by name ("name OW") rather than relying on `gmx rdf`
interactive index-group selection.

[OPEN] API note: this script targets MDAnalysis >= 2.0, where InterRDF
results are exposed via `.results.bins` / `.results.rdf`. If
`python -c "import MDAnalysis; print(MDAnalysis.__version__)"` reports
an older version, the results may instead be at `.bins` / `.rdf`
directly — verify before trusting the output.

All RDF values printed/saved here are [TO MEASURE]. Literature comparison
of the first-peak position/height happens in the validation report, not
in this script.

Usage
-----
    python scripts/analysis/analyze_oo_rdf.py \
        --tpr simulations/SIM-01/md.tpr \
        --xtc simulations/SIM-01/md.xtc \
        --begin-ps 0
"""

import argparse
import sys
from pathlib import Path

import numpy as np
import MDAnalysis as mda
from MDAnalysis.analysis.rdf import InterRDF

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
    ap.add_argument("--begin-ps", type=float, default=0.0,
                     help="Start analysis at this simulation time (ps)")
    ap.add_argument("--nbins", type=int, default=200)
    ap.add_argument("--rmax", type=float, default=1.0, help="nm")
    ap.add_argument("--out-table", type=Path, default=Path("results/tables/oo_rdf.csv"))
    ap.add_argument("--out-figure", type=Path, default=Path("results/figures/oo_rdf.png"))
    args = ap.parse_args()

    if not args.tpr.exists() or not args.xtc.exists():
        print("[ERROR] Missing tpr/xtc input — this script performs no calculation "
              "without a real trajectory.", file=sys.stderr)
        sys.exit(1)

    u = mda.Universe(str(args.tpr), str(args.xtc))

    oxygens = u.select_atoms("name OW")
    if len(oxygens) == 0:
        print("[ERROR] No atoms matched selection 'name OW'. Check atom naming in "
              "models/SPC-E/spce.itp and the generated run topology.", file=sys.stderr)
        sys.exit(1)
    print(f"Selected {len(oxygens)} oxygen atoms via 'name OW'.")

    start_frame = 0
    for i, ts in enumerate(u.trajectory):
        if ts.time >= args.begin_ps:
            start_frame = i
            break

    # MDAnalysis reports distances in Angstrom for GROMACS-derived Universes;
    # convert the nm-specified --rmax to Angstrom for the InterRDF call, and
    # convert results back to nm for output/reporting.
    rmax_A = args.rmax * 10.0
    rdf = InterRDF(oxygens, oxygens, nbins=args.nbins, range=(0.0, rmax_A),
                    exclusion_block=(1, 1))
    rdf.run(start=start_frame)

    r_nm = rdf.results.bins / 10.0
    g_r = rdf.results.rdf

    if g_r.max() <= 0:
        print("[ERROR] Computed RDF is identically zero — check selection and trajectory.",
              file=sys.stderr)
        sys.exit(1)

    peak_idx = int(np.argmax(g_r))
    peak_r = float(r_nm[peak_idx])
    peak_g = float(g_r[peak_idx])

    print("[TO MEASURE] First g_OO(r) peak (from real trajectory data):")
    print(f"  r_peak   = {peak_r:.4f} nm")
    print(f"  g(r_peak) = {peak_g:.4f}")
    print("  This is not yet compared to any literature value — that comparison "
          "belongs in results/reports/SIM-01-validation.md with a citation.")

    args.out_table.parent.mkdir(parents=True, exist_ok=True)
    np.savetxt(args.out_table, np.column_stack([r_nm, g_r]),
               header="r_nm,g_OO_r", delimiter=",", comments="")
    print(f"Saved: {args.out_table}")

    if plt is not None:
        args.out_figure.parent.mkdir(parents=True, exist_ok=True)
        fig, ax = plt.subplots(figsize=(6, 4.5))
        ax.plot(r_nm, g_r, lw=1.2)
        ax.axvline(peak_r, color="k", ls="--", lw=0.8)
        ax.set_xlabel("r (nm)")
        ax.set_ylabel(r"g$_{OO}$(r)")
        ax.set_xlim(0, args.rmax)
        fig.tight_layout()
        fig.savefig(args.out_figure, dpi=150)
        print(f"Saved: {args.out_figure}")


if __name__ == "__main__":
    main()
