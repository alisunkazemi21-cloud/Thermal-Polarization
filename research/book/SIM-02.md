# SIM-02 research book — thermal gradient to polarization

## Scope

SIM-02 asks whether an imposed heat flux in bulk rigid SPC/E water produces a
stationary temperature gradient and a signed molecular polarization profile that
is reproducible across time blocks. It covers
\(\nabla T \rightarrow J_q \rightarrow P\) only.

Status on 2026-09-30: **method and temperature sequence selected; the published
400 K protocol has been recovered and awaits project approval; no SIM-02 run or
result exists.**

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

`[PROPOSED]` Checkpoint 07 adopts that reference through short release gates: a
zero-step audit, an equilibrium bridge, a 100 ps 1 fs smoke test, a matched
1 fs/2 fs comparison, and a 1 ns stationarity pilot. The published 10 ns
transient and 60 ns production remain blocked until these checks justify them.

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
