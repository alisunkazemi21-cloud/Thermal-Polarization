# SIM-02 research book — thermal gradient to polarization

## Scope

SIM-02 asks whether an imposed heat flux in bulk rigid SPC/E water produces a
stationary temperature gradient and a signed molecular polarization profile that
is reproducible across time blocks. It covers
\(\nabla T \rightarrow J_q \rightarrow P\) only.

Status on 2026-10-04: **method, temperature sequence, and exact 400 K protocol
approved; gate 1 passed; checkpoint 08 failed its Stage-A COM criterion;
checkpoint 09 Stage A (2 ps and 20 ps) and Stage B (2 ps) passed their
implementation checks. Its four-rank uncorrected NVE diagnostic exceeded the
COM ceiling at 100 fs; checkpoint 10's one-rank continuation then completed 2 ps
below the ceiling from a separately replayed Stage-B state. Checkpoint 11
repeated Stage C/NVE at one rank from the exact four-rank Stage-B restart and
also completed below the ceiling. The same-restart four-rank path failed at
100 fs. Checkpoint 12 located the first crossing at 7 fs; checkpoint 13's
matched one-rank replay completed 400 fs with maximum COM `9.6530e-19 Å/fs`.
The traces support rank-count-sensitive behavior in this saved-state sequence,
while the mechanism remains unresolved. The full equilibrium bridge is on
hold. No equilibrium or polarization result exists. DECISION-014 proposes one
consolidated Gate 2 go/no-go under the already frozen criteria, or closure of
the current method path.**

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
| 2026-10-03 | Corrected checkpoint 08 bridge launched and stopped | Measured acceptance failure | Initialization passed, but COM speed reached `1.0278e-5 Å/fs` at 1 ps and `1.2511e-5 Å/fs` at 2 ps versus the `1e-6 Å/fs` ceiling |
| 2026-10-03 | DECISION-009 approved | Approved decision | Preparation-only momentum control and bounded revalidation sequence authorized |
| 2026-10-03 | Checkpoint 09 zero-step and 2 ps checks | Measured implementation evidence | Corrected input initialized; the 2 ps Stage-A sample maximum COM speed was `6.5634e-19 Å/fs` |
| 2026-10-03 | Checkpoint 09 20 ps Stage-A check | Measured implementation pass | 200 samples at 400 K; maximum sampled COM speed `9.6548e-19 Å/fs`; completed 20,000 steps |
| 2026-10-03 | Checkpoint 09 Stage-B transition | Measured implementation pass | 2,000 NVT steps; temperature returned to `399.81022 K`; COM remained below `1e-6 Å/fs` |
| 2026-10-03 | Checkpoint 09 uncorrected NVE diagnostic | Measured implementation failure | COM speed was `7.1446e-6 Å/fs` at 100 fs; run was interrupted at 400 fs; full bridge held |
| 2026-10-03 | Stage-C zero-step replay | Measured diagnostic | After the final zero-linear command COM was `4.8769e-8 Å/fs`; the mechanism of subsequent NVE drift remained open |
| 2026-10-04 | DECISION-010 approved | Approved decision | User authorized the matched one-rank Stage-B/NVE comparison; full bridge and threshold changes remained out of scope |
| 2026-10-04 | Checkpoint 10 one-rank continuation | Measured implementation diagnostic | Stage B and 2 ps NVE completed; 20 NVE samples had max COM `1.0435e-18 Å/fs`; four-rank path had exceeded the ceiling at 100 fs; cause not isolated |
| 2026-10-04 | DECISION-011 approved | Approved decision | User authorized a one-rank Stage-C/NVE comparison from the exact four-rank Stage-B restart; local WSL build selected to hold software environment close |
| 2026-10-04 | Checkpoint 11 same-restart comparison | Measured implementation diagnostic | One-rank Stage C/NVE completed 2 ps (exit 0; max COM `1.2638e-18 Å/fs`); four-rank path from the same restart breached at 100 fs; mechanism unresolved |
| 2026-10-04 | Checkpoint 12 four-rank replay | Measured diagnostic | From the shared restart, COM crossed the ceiling at 7 fs; mechanism not identified |
| 2026-10-04 | DECISION-013 approved and executed | Approved bounded diagnostic | Matched one-rank high-cadence control from the same restart completed 400 fs; max COM `9.6530e-19 Å/fs`; at 7 fs COM was `2.3195e-19 Å/fs`; no ceiling crossing |
| 2026-10-04 | Checkpoint 13 comparison closed | Measured trace plus inference | Together with checkpoint 12, supports rank-count-sensitive early COM behavior for this saved-state sequence; cause unresolved. Temperature and total-energy changes remain exploratory because no short-run thresholds were frozen |
| 2026-10-04 | DECISION-014 proposed | Proposed bridge go/no-go | One final Gate 2 attempt using DECISION-008's unchanged 1.52-million-step protocol and acceptance criteria, or close the current method path; no run authorized yet |

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

`[MEASURED FAILURE]` The corrected bridge launched at 20:22:39 +03:30 on
2026-10-03 with four MPI ranks and the LAMMPS OPT suffix. At the corrected
step-zero boundary, the COM velocity was
`(-4.1019714e-7, -1.4053665e-7, 6.9854399e-8) Å/fs`, giving a speed of
`4.3903e-7 Å/fs`. After integration it rose to `1.02778929e-5 Å/fs` at 1 ps
and `1.25105105e-5 Å/fs` at 2 ps. Both exceed the frozen ceiling and the growth
condition failed, so the run was stopped during Stage A. Temperature was 400 K
at both records and LAMMPS reported no warning or error. This short failed run
does not measure equilibrium energy drift, structure, or stationarity. The
compact provenance record is
`results/raw/SIM-02/checkpoint-08-equilibrium/run-start.json`.

`[DECIDED]` Checkpoint 09 confines periodic linear-momentum removal to the
already thermostatted preparation stages, uses kinetic-energy rescaling, and
removes the operation before NVE. This preserves the original NVE no-growth test
rather than hiding drift inside the measured stage. The proposal also corrects
Stage A's fix ordering so RATTLE is defined after velocity-modifying fixes, as
required by the LAMMPS documentation.

## Checkpoint 09 outcome

`[MEASURED PASS]` Four-rank LAMMPS OPT completed 20,000 Stage-A steps in
1:39:34. The 200 unique integrated samples (100–20,000) reported 400 K and had
a maximum COM speed of `9.654782345768524e-19 Å/fs`. Stage B then advanced
2,000 NVT steps from the Stage-A restart. Its 20 samples ranged from 395.59333
to 408.00767 K and ended at 399.81022 K; the maximum sampled COM speed was
`8.507873362730173e-19 Å/fs`.

`[MEASURED FAILURE]` With periodic momentum control removed, NVE exceeded the
preapproved `1e-6 Å/fs` ceiling at the first 100 fs sample (`7.144552366951081e-6
Å/fs`). The interrupted run reached 400 fs and captured four samples; the peak
was `8.357269209836094e-6 Å/fs`. It did not measure equilibrium energy drift,
structure, or stationarity.

`[MEASURED DIAGNOSTIC]` A zero-step replay of the Stage-C adjustments ended at
`4.8768857346949e-8 Å/fs`, below the ceiling. The excursion therefore appeared
during subsequent integration; RATTLE/MPI behavior is a hypothesis to test, not
an established cause. DECISION-010 later authorized a bounded one-rank
comparison; checkpoint 10 records its result. No full bridge relaunch, periodic
NVE momentum correction, or threshold change is approved.

## Checkpoint 10 — one-rank comparison

`[MEASURED PASS, BOUNDED]` On 2026-10-04, the user-approved one-rank OPT run
replayed the 2 ps Stage-B transition from the same 20 ps Stage-A restart, then
completed 2 ps of uncorrected NVE. Stage B's 20 samples ranged from 395.56237 to
404.86220 K and ended at 400.55730 K. NVE's 20 samples ranged from 392.66022 to
402.37766 K and ended at 399.69651 K. Maximum NVE COM speed was
`1.0435411502651417e-18 Å/fs`, with no exceedances of the frozen
`1e-6 Å/fs` ceiling. LAMMPS logged completion at step 24,000 in 32:23.

The contrasting four-rank failure indicates rank-sensitive behavior in this
continuation sequence, but Stage B was replayed under each rank count, so the
phase-space state entering NVE differed. This comparison does not isolate the
cause to NVE, RATTLE, or MPI reduction. The report also records that a wrapper
error after LAMMPS completion prevented capture of the process exit status.
This bounded diagnostic measured no equilibrium energy drift, structure,
eHEX heat transfer, stationary gradient, or polarization. The full bridge stays
on hold. DECISION-011 then authorized a same-Stage-B-restart comparison; see
checkpoint 11 below.

See `results/reports/SIM-02-checkpoint-10-one-rank-nve.md` and DECISION-010.

## Checkpoint 11 — same-restart rank comparison

`[MEASURED PASS, BOUNDED]` On 2026-10-04, the user-approved one-rank OPT run
read the exact Stage-B restart written by the four-rank checkpoint-09
continuation. Stage-C initialization and 2 ps uncorrected NVE completed from
step 22,000 to 24,000 with exit code 0 in 14:02. The 20 samples ranged from
395.91302 to 406.10015 K and ended at 400.10536 K. Maximum sampled COM speed was
`1.2638166834526734e-18 Å/fs` at step 23,600, with no ceiling exceedances.

The four-rank path from the same saved restart crossed `1e-6 Å/fs` at 100 fs
(`7.144552366951081e-6 Å/fs`). Rank count is now the controlled run-level
difference for the Stage-C/NVE sequence. The result does not identify whether
RATTLE, velocity cleanup, PPPM/MPI reductions, or another rank-dependent
operation is responsible. This remains an implementation diagnostic; the full
bridge stays on hold, with no equilibrium or polarization result.

The same-restart test used the existing WSL LAMMPS build to keep the software
environment close to the prior run. Colab is a candidate for longer work, but
its hardware and runtime availability vary and a hosted GPU does not
automatically accelerate this CPU OPT configuration.

See `results/reports/SIM-02-checkpoint-11-same-restart-one-rank.md` and
DECISION-011.

## Checkpoint 12 — four-rank high-cadence replay

`[MEASURED FAILURE, BOUNDED]` On 2026-10-04, the user approved a four-rank
replay from the byte-identical checkpoint-11 Stage-B restart. The 1 fs step,
400 K scale, RATTLE/PPPM settings, OPT suffix, and uncorrected NVE policy were
preserved. COM components and speed were sampled every integration step, with
an automatic halt at the existing `1e-6 Å/fs` ceiling and a 400 fs maximum.

After velocity cleanup, the NVE start at step 22,000 had a COM speed of
`6.0282895e-8 Å/fs` and temperature 400.02681 K. COM speed rose at every
recorded step; the first exceedance occurred at step 22,007, 7 fs into NVE.
The halt message reports `1.1198276995146967e-6 Å/fs`; the thermo row rounds
that to `1.1198277e-6 Å/fs`. Temperature at the halt was 401.48097 K. The
400 fs maximum was not reached because the stop criterion fired. LAMMPS
returned exit code 0 after the configured soft halt and output finalization;
that is not a COM pass.

The thermo total-energy column changed by +2.206 kcal/mol over the seven
steps. No energy-drift threshold was frozen for this COM-timing test, so this
is an exploratory observation for a separately scoped follow-up. The COM and
energy observations do not identify a mechanism. RATTLE, velocity
initialization, PPPM/MPI reductions, and other rank-dependent operations
remain hypotheses. The full bridge remains on hold; no equilibrium, eHEX,
stationary-gradient, or polarization result follows.

The initial `mpiexec -n 4` attempt failed before LAMMPS allocated ranks and
advanced zero steps. The same approved run then completed with
`mpirun --oversubscribe -np 4`; both attempts are noted in the raw provenance.
See `results/reports/SIM-02-checkpoint-12-four-rank-high-cadence.md` and
DECISION-012.

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
- `results/reports/SIM-02-checkpoint-09-diagnostics.md`: four-rank bounded diagnostics
- `results/reports/SIM-02-checkpoint-10-one-rank-nve.md`: one-rank comparison from replayed Stage B
- `results/reports/SIM-02-checkpoint-11-same-restart-one-rank.md`: one-rank comparison from the same four-rank Stage-B restart
- `results/reports/SIM-02-checkpoint-12-four-rank-high-cadence.md`: per-step four-rank replay from that restart
- DECISION-010 through DECISION-014: rank-comparison diagnostics and consolidated bridge go/no-go proposal
- `results/reports/SIM-02-checkpoint-13-one-rank-high-cadence.md`: matched one-rank control result
- `simulations/SIM-02/lammps/in.checkpoint-09-continuation-b-nve`: restart-based NVT/NVE diagnostic input
- `simulations/SIM-02/lammps/in.checkpoint-09-stage-c-zero-step`: COM-transition isolation input
