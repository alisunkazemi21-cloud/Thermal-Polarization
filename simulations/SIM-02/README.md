# SIM-02 — thermal-gradient NEMD

Status: **checkpoint 07 gate 1 passed. Checkpoint 08 failed its Stage-A COM
criterion. Checkpoint 09 passed Stage A/B but the four-rank NVE diagnostic
exceeded the frozen COM ceiling at 100 fs. Checkpoint 10's one-rank 2 ps NVE
comparison passed. Checkpoint 11 then used the exact same four-rank Stage-B
restart: one-rank Stage-C/NVE passed 2 ps, while the four-rank path breached at
100 fs. Checkpoint 12 sampled the four-rank path each timestep and halted at
its first COM-ceiling crossing, 7 fs into NVE. Checkpoint 13 used the same
restart at one rank and completed 400 fs with maximum COM `9.65e-19 Å/fs`.
Together the matched high-cadence traces support rank-count-sensitive behavior
for this saved-state sequence; the cause remains unresolved. Checkpoint 13
closes this diagnostic branch. DECISION-014 now authorizes one conditional final-results campaign. The long
bridge awaits host and restart-continuity preflight; no equilibrium or
polarization result exists yet.**

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

## Checkpoint 08 approved protocol

`lammps/in.equilibrium-bridge` defines the approved fixed-volume bridge from the imported
author NEMD state to a 400 K PPPM equilibrium reference. It replaces the source
velocities with deterministic seed `20260930`, runs 20 ps of explicit velocity
rescaling, 500 ps NVT, an exact kinetic-energy adjustment, and 1 ns NVE at 1 fs.

The paper's original 200 ps NpT stage is not copied because its pressure target
is not reported and our starting state is the supplied steady-state snapshot,
not the paper's initial lattice. The exact published box and 0.934 g cm⁻³ density
remain fixed. The proposal, acceptance criteria, restart rules, and bounded
output plan are in
`research/designs/SIM-02-checkpoint-08-equilibrium-bridge.md`.

The first four-rank production-path launch stopped before step 1 when MPI
RATTLE initialization exposed a `5.9e-7 Å/fs` COM-velocity floor. The corrected
input initializes constraints before explicit stage-boundary momentum removal;
the frozen criterion is at most `1e-6 Å/fs` with no systematic growth. Raw
initialization evidence is under
`history/SIM-02-checkpoint-08-mpi-momentum-init/`.

The corrected production run started on 2026-10-03 at 20:22:39 +03:30 with
four MPI ranks and the LAMMPS OPT suffix. Its corrected step-zero COM speed was
`4.3903e-7 Å/fs`, below the frozen ceiling. At steps 1,000 and 2,000 it rose to
`1.02778929e-5` and `1.25105105e-5 Å/fs`. The run was stopped during Stage A.
LAMMPS emitted no warning or error; this is a scientific acceptance failure.
The compact record is `results/raw/SIM-02/checkpoint-08-equilibrium/run-start.json`
and the preserved evidence is under
`history/SIM-02-checkpoint-08-stage-a-com-drift/`.

Checkpoint 09 adds `fix momentum 100 linear 1 1 1 rescale` in Stages A and B,
places RATTLE after velocity-changing fixes, and removes periodic momentum
control before Stage D NVE. The 20 ps Stage-A diagnostic completed 200 samples
at 400 K with maximum sampled COM speed `9.65e-19 Å/fs`. The 2 ps Stage-B
transition ended at 399.81 K with COM below the frozen ceiling. In the
uncorrected NVE check, COM reached `7.14e-6 Å/fs` at 100 fs, above the approved
`1e-6 Å/fs` limit; the partial run was stopped at 400 fs. This is an
implementation failure, not an equilibrium result. See the
[diagnostic report](../../results/reports/SIM-02-checkpoint-09-diagnostics.md),
the completed [checkpoint 10 one-rank report](../../results/reports/SIM-02-checkpoint-10-one-rank-nve.md), the [checkpoint 11 same-restart report](../../results/reports/SIM-02-checkpoint-11-same-restart-one-rank.md), the [checkpoint 12 high-cadence report](../../results/reports/SIM-02-checkpoint-12-four-rank-high-cadence.md), and the [checkpoint 13 matched one-rank report](../../results/reports/SIM-02-checkpoint-13-one-rank-high-cadence.md). DECISION-010 through DECISION-014 record the diagnostics and the approved conditional campaign; its stages stop automatically at the first failed gate.
The reproducible continuation, Stage-C zero-step, checkpoint-10 through checkpoint-13 inputs are tracked as
`in.checkpoint-09-continuation-b-nve` and
`in.checkpoint-09-stage-c-zero-step`, `in.checkpoint-10-single-rank-nve`, and
`in.checkpoint-11-same-restart-one-rank`, and
`in.checkpoint-12-four-rank-high-cadence`, and
`in.checkpoint-13-one-rank-high-cadence` in this directory.

## Documentation contract

- This README records exact commands and checkpoint state.
- `notebooks/sim02_research.py` is the executable Marimo analysis record.
- `research/book/SIM-02.md` is the chronological academic narrative.
- `results/reports/SIM-02-report.md` becomes the frozen technical report.
- `research/media/SIM-02-longform-youtube.md` follows the same evidence timeline
  for the long-form documentary.
