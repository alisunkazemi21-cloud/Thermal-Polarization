# SIM-02 — thermal-gradient NEMD

Status: **checkpoint 07 is approved and its zero-step gate passed. The
equilibrium bridge is next.**

The GROMACS NEMD files in this directory remain **non-runnable historical
drafts**. The approved implementation and imported reference configuration live
under `lammps/`.

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
choice, and `research/designs/SIM-02-LAMMPS-eHEX-design.md` for the active design.
The condition order is recorded in
`research/decisions/DECISION-006-SIM-02-temperature-path.md`. The exact benchmark
and staged gates are frozen in DECISION-007. Production sampling and allocation
remain gated.

## Preserved draft parameters

These are proposals, not validated settings or measured results:

- rigid SPC/E; 2 fs timestep; PME; 1.0 nm real-space cutoffs;
- fixed-volume NEMD after NPT equilibration;
- 280/320 K nominal cold/hot targets with a 300 K mean;
- 500 ps startup and 1.5 ns production;
- symmetric center/periodic-edge reservoir geometry along z.

The gate 1 audit is a measured implementation result, recorded in
`results/reports/SIM-02-checkpoint-07-zero-step.md`. It advanced zero trajectory
steps and is not evidence of a gradient or polarization.

## Documentation contract

- This README records exact commands and checkpoint state.
- `notebooks/sim02_research.py` is the executable Marimo analysis record.
- `research/book/SIM-02.md` is the chronological academic narrative.
- `results/reports/SIM-02-report.md` becomes the frozen technical report.
- `research/media/SIM-02-longform-youtube.md` follows the same evidence timeline
  for the long-form documentary.
