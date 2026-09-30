# SIM-02 — thermal-gradient NEMD

Status: **LAMMPS eHEX and the 400 K → 300 K sequence are approved; detailed
input design is in progress.**

The GROMACS NEMD files in this directory remain **non-runnable historical
drafts**. New approved implementation files will live under `lammps/` after the
design parameters and pilot criteria are accepted.

SIM-02 asks whether bulk SPC/E water develops a statistically resolved spatial
polarization under a controlled thermal gradient. Its scope is
`gradient -> heat transport -> polarization`; it does not include electrical
extraction.

## Current finding

The equilibrium preparation files are drafts. The current NEMD files
`nemd-startup.mdp` and `nemd-production.mdp` use `tc-grps = Hot Cold Rest`.
Those names resolve to fixed atom groups when `gmx grompp` builds the run input.
They do not describe spatial reservoirs whose membership follows molecules as
water diffuses. `gmx select` supports dynamic trajectory analysis, but it does
not dynamically redefine `tc-grps` during `mdrun`.

Consequently, an index generated from the initial coordinates would thermostat
the initially selected molecules after they leave the intended slabs. The
result would not implement the literature method and must not be interpreted as
a bulk thermal-gradient experiment.

The draft also sets `nstvout = 0`. Its compressed trajectory contains positions,
not velocities, so it cannot support a kinetic local-temperature profile from
saved frames. The topology still contains `__N_SOL_TBD__`, and the referenced
spatial-group generator does not exist.

See `research/decisions/DECISION-004-SIM-02-method-audit.md` for the audit,
`research/decisions/DECISION-005-SIM-02-LAMMPS-eHEX.md` for the approved engine
choice, and `research/designs/SIM-02-LAMMPS-eHEX-design.md` for the open design.
The condition order is recorded in
`research/decisions/DECISION-006-SIM-02-temperature-path.md`. Exact geometry,
heat rate, sampling, duration, and replication remain gated.

## Preserved draft parameters

These are proposals, not validated settings or measured results:

- rigid SPC/E; 2 fs timestep; PME; 1.0 nm real-space cutoffs;
- fixed-volume NEMD after NPT equilibration;
- 280/320 K nominal cold/hot targets with a 300 K mean;
- 500 ps startup and 1.5 ns production;
- symmetric center/periodic-edge reservoir geometry along z.

No SIM-02 trajectory or result is currently claimed.

## Documentation contract

- This README records exact commands and checkpoint state.
- `notebooks/sim02_research.py` is the executable Marimo analysis record.
- `research/book/SIM-02.md` is the chronological academic narrative.
- `results/reports/SIM-02-report.md` becomes the frozen technical report.
- `research/media/SIM-02-longform-youtube.md` follows the same evidence timeline
  for the long-form documentary.
