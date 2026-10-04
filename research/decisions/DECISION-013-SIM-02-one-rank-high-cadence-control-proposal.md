# DECISION-013 — One-rank high-cadence SIM-02 control

- Date: 2026-10-04
- Status: **Executed 2026-10-04; bounded COM criterion passed; bridge remains held**
- Depends on: DECISION-011 and DECISION-012

## Question

Does the early COM trajectory seen in checkpoint 12 depend on the four-rank
Stage-C/NVE path, or does the same-restart one-rank path show a similar
first-step excursion when sampled at the same cadence?

## Evidence motivating the proposal

Checkpoint 12 replayed the checkpoint-11 Stage-B restart at four MPI ranks.
After Stage-C velocity scaling and cleanup, the step-22,000 COM speed was
`6.0282895e-8 Å/fs`. During the next seven NVE steps, the z component rose
from `5.7704334e-8` to `1.037034e-6 Å/fs`; the COM-speed ceiling was first
crossed at step 22,007 (`1.1198276995146967e-6 Å/fs`). The other COM components
also increased. This describes the trace but does not identify its cause.

Checkpoint 11 used the same Stage-B restart at one rank and reported no sampled
COM ceiling exceedance over 2 ps. Its 100 fs cadence does not resolve the
first seven steps, so it is not a matched high-cadence early-time comparison.

## Approved scope

Replay the same byte-identical Stage-B restart used by checkpoint 12
(`3b43042a7dceb3f774708d54a57d76bc701cff44cfe7231afea299ba8a9494ef`) at one
MPI rank and one OpenMP thread. Use the same LAMMPS 10 Dec 2025 OPT build,
1 fs timestep, PPPM and RATTLE settings, 400 K velocity scaling, Stage-C command
ordering, uncorrected NVE policy, per-step COM/temperature/energy output, strict
`1e-6 Å/fs` soft-halt ceiling, and 400-step maximum as checkpoint 12. Change
only MPI rank count and the output directory. Do not remove momentum during NVE
or change any scientific parameter.

Store the input at
`simulations/SIM-02/lammps/in.checkpoint-13-one-rank-high-cadence` and the
compact run record under
`results/raw/SIM-02/checkpoint-13-one-rank-high-cadence/`. Preserve the source
restart and record its hash in the same way as checkpoint 12.

## Pre-registered interpretation and stopping boundary

- If one rank stays near its post-cleanup COM level while four ranks show the
  checkpoint-12 rise, that supports rank-count-sensitive early-time behavior
  under matched sampling. It still does not identify a specific cause.
- If one rank shows a similar increase, the issue is not unique to the
  four-rank path; compare component and energy traces before proposing a
  mechanism.
- Reaching 400 fs without a crossing is only a bounded implementation pass.
  It does not release the equilibrium bridge or establish energy conservation,
  equilibrium, heat transfer, a stationary gradient, or polarization.
- The total-energy column is exploratory in this diagnostic; no energy acceptance
  threshold has been preregistered.

The user approved execution of this exact scope on 2026-10-04.

## Measured outcome

The one-rank run completed all 400 NVE steps (401 distinct step states) with no
COM ceiling crossing. Maximum sampled COM speed was `9.6530431e-19 Å/fs`; at
7 fs it was `2.3195258e-19 Å/fs`, while checkpoint 12's four-rank trace crossed
the ceiling at that same elapsed time. The two high-cadence traces therefore
support rank-count-sensitive early-time behavior for this saved-state sequence.
They do not identify the responsible operation.

Temperature ranged from 395.87137 to 407.85020 K and the total-energy column
changed by +0.690 kcal/mol across the 400 fs NVE window. These are exploratory
diagnostic values; DECISION-013 had no short-run thermal or energy acceptance
threshold. They do not pass or fail the frozen 1 ns bridge criteria in
DECISION-008. See `results/reports/SIM-02-checkpoint-13-one-rank-high-cadence.md`
and the hashed execution record under
`results/raw/SIM-02/checkpoint-13-one-rank-high-cadence/`.

## Stopping boundary and streamlined next action

Checkpoint 13 closes the rank-count comparison. Do not add another mechanism
microcheckpoint by default. The next research action is one consolidated
bridge-readiness decision using the existing DECISION-008 acceptance criteria:
either authorize a single, resource-appropriate Gate 2 attempt with those
criteria unchanged, or formally stop SIM-02's current method path and document
the unresolved numerical limitation. A failed acceptance criterion ends that
attempt and is reported as the result; no parameter sweep follows without a
new scientific decision. The bridge is not released by this diagnostic.

Any future test that changes force/constraint handling or scientific parameters
requires its own decision.
