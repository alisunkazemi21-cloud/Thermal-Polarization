# SIM-02 research book — thermal gradient to polarization

## Scope

SIM-02 asks whether an imposed heat flux in bulk rigid SPC/E water produces a
stationary temperature gradient and a signed molecular polarization profile that
is reproducible across time blocks. It covers
\(\nabla T \rightarrow J_q \rightarrow P\) only.

Status on 2026-09-30: **method, temperature sequence, and exact 400 K protocol
approved; gate 1 zero-step audit passed; checkpoint 08 equilibrium design is
approved in DECISION-008; no gate-2 result or polarization result exists.**

The approved sequence is a 400 K method-validation condition followed by the
300 K target only after the equilibrium and eHEX pilot gates pass
(DECISION-006).

## Why this experiment follows SIM-01

`[MEASURED]` The SIM-01 report records equilibrium density, temperature, O–O
structure, and diffusion values inside its acceptance ranges for the project's
SPC/E implementation. That establishes an equilibrium baseline. It does not
establish thermopolarization or make 300 K a special transition temperature.

## Chronology

| Date | Event | Evidence class | Consequence |
|---|---|---|---|
| Before 2026-09-30 | GROMACS hot/cold/rest drafts were prepared | Historical draft | Preserved for audit; no result produced |
| 2026-09-30 | Graphify project map and compact handoff created | Repository operation | Future work can recover context with bounded queries |
| 2026-09-30 | GROMACS spatial-group method audited | Established + inferred | Static atom membership rejected for diffusing water |
| 2026-09-30 | LAMMPS eHEX selected | Approved decision | Dynamic spatial reservoirs and known heat rate become the method basis |
| 2026-09-30 | Local LAMMPS capabilities inspected | Established | Installed build exposes eHEX, RIGID, SHAKE/RATTLE, and PPPM |
| 2026-09-30 | 2016 paper and author replication package audited | Established | Exact 4,500-water geometry, reservoirs, exchange rate, and reference run were recovered |
| 2026-09-30 | Checkpoint 07 prepared | Proposed | Staged build, equilibrium, timestep, and stationarity gates await approval |
| 2026-09-30 | DECISION-007 approved | Approved decision | Exact benchmark and staged release gates frozen |
| 2026-09-30 | Gate 1 zero-step audit executed | Measured | Structure and modern LAMMPS parse/force initialization passed; zero steps advanced |
| 2026-09-30 | Checkpoint 08 equilibrium bridge prepared | Proposed | Exact input, acceptance criteria, restart behavior, and bounded outputs are ready for review; trajectory not started |
| 2026-10-01 | DECISION-008 approved | Approved decision | Fixed-volume PPPM bridge released for execution; outcome remains to be measured |
| 2026-10-01 | First four-rank launch stopped at step zero | Measured implementation failure | RATTLE initialization left a resolved COM velocity; input corrected to remove momentum after constraint initialization |
| 2026-10-03 | MPI initialization correction approved | Approved decision | `1e-6 Å/fs` COM-speed ceiling plus no-growth requirement frozen; relaunch authorized from step zero |

The GROMACS draft was useful: it exposed the real methodological question. A
thermal reservoir in a liquid must be defined by current position, not by the
identity of molecules that happened to occupy a slab at time zero.

## Method decision

`[ESTABLISHED]` LAMMPS eHEX transfers kinetic energy between spatial reservoirs
and determines membership from current position. With constrained water,
`constrain com` rescales an entire molecule when its center of mass lies inside
the reservoir. Equal-and-opposite reservoir rates give a directly traceable heat
input, while eHEX corrects much of the long-time drift associated with HEX.

`[DECIDED]` SIM-02 will use LAMMPS eHEX, but switching engines requires an
equilibrium bridge back to SIM-01 before nonequilibrium results are trusted.

## Protocol recovery

`[ESTABLISHED]` The 2016 author package uses 4,500 waters at 400 K in a
36.353 × 36.353 × 109.061 Å³ box. The hot reservoir is split across the
periodic edges, the cold reservoir is central, and both have 8 Å total
thickness. The exchange rate is ±0.1614 kcal mol⁻¹ fs⁻¹, corresponding to
4.243 × 10¹⁰ W m⁻² along each branch. These details correct the approximate
geometry in the first project draft.

`[DECIDED]` Checkpoint 07 adopts that reference through short release gates: a
zero-step audit, an equilibrium bridge, a 100 ps 1 fs smoke test, a matched
1 fs/2 fs comparison, and a 1 ns stationarity pilot. The published 10 ns
transient and 60 ns production remain blocked until these checks justify them.

## Gate 1 result — build and zero-step audit

`[MEASURED]` The imported source configuration contains 13,500 atoms in 4,500
neutral three-site molecules at 933.993861 kg m⁻³. The constrained geometry
matches 1.0 Å O–H bonds and a 109.47° H–O–H angle within numerical precision.
COM accounting placed 282 molecules in the periodic hot reservoir, 369 in the
central cold reservoir, and 3,849 in the bulk.

LAMMPS 10 Dec 2025 read all coordinates and velocities, formed 4,500 RATTLE
clusters, accepted the current eHEX syntax, initialized PPPM to an estimated
relative force accuracy of 9.136047 × 10⁻⁶, and completed `run 0`. The diagnostic
step-zero temperature was 404.21051 K. No trajectory step was advanced, so this
does not test equilibrium, energy conservation, a gradient, or polarization.

## Checkpoint 08 — removing the inherited nonequilibrium state

`[ESTABLISHED]` The author data file is a steady-state NEMD configuration. Its
positions are valuable, but its velocity field carries the experiment we are
trying to reset. The paper began from a lattice and used 20 ps velocity
rescaling, 200 ps NpT, a return to the target box, 500 ps NVT, and 1 ns NVE. It
does not report the NpT pressure target or rescaling cadence.

`[DECIDED]` The bridge keeps the exact published box, replaces all velocities
with a seeded 400 K Maxwell distribution, performs 20 ps direct rescaling and
500 ps NVT, rescales once to 400 K, and measures 1 ns NVE. This preserves the
known density while avoiding an invented pressure parameter. Temperature,
energy drift, constraints, center-of-mass momentum, thermal-gradient removal,
and O–O structural stationarity have thresholds frozen before execution.

`[OPEN]` Until those 1.52 million steps run and the evidence is analyzed, gate 2
has no outcome. Passing it would release only the 100 ps eHEX smoke test.

## Evidence that must exist before a claim

1. equilibrium LAMMPS density, temperature, and O–O structure consistent with
   the chosen condition and the translated SPC/E model;
2. stable RATTLE/SHAKE constraints and quantified energy behavior;
3. equal-and-opposite eHEX energy transfer and a defensible conversion to Jq;
4. stationary unfolded T(z) and ρ(z) profiles;
5. signed Pz(z) and <cos θ(z)> with explicit coordinate and dipole conventions;
6. block uncertainty and agreement of the two symmetric transport branches;
7. an independent seed before calling a positive signal reproducible.

## Current conclusion

`[OPEN]` Whether the project will measure thermal polarization remains unknown.
The methodological pivot improves the experiment's ability to answer that
question. It does not make a positive result more likely, and a resolved null
result remains scientifically valuable.

## Linked records

- DECISION-004: method audit
- DECISION-005: LAMMPS eHEX selection
- `simulations/SIM-02/README.md`: run status
- `notebooks/sim02_research.py`: executable research record
- `results/reports/SIM-02-report.md`: technical report shell
