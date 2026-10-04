# DECISION-013 — Proposed one-rank high-cadence SIM-02 control

- Date: 2026-10-04
- Status: **Proposed for review; not approved; not run**
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

## Proposed scope

If approved, replay the same byte-identical Stage-B restart used by checkpoint
12 (`3b43042a7dceb3f774708d54a57d76bc701cff44cfe7231afea299ba8a9494ef`) at
one MPI rank and one OpenMP thread. Use the same LAMMPS 10 Dec 2025 OPT build,
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

## Interpretation and stopping boundary

- If one rank stays near its post-cleanup COM level while four ranks show the
  checkpoint-12 rise, that supports rank-count-sensitive early-time behavior
  under matched sampling. It still does not identify a specific cause.
- If one rank shows a similar increase, the issue is not unique to the
  four-rank path; compare component and energy traces before proposing a
  mechanism.
- Reaching 400 fs without a crossing is only a bounded implementation pass.
  It does not release the equilibrium bridge or establish energy conservation,
  equilibrium, heat transfer, a stationary gradient, or polarization.
- The total-energy column is exploratory in this proposal; no energy acceptance
  threshold has been preregistered.

No simulation is authorized by this proposal. Execution requires approval of
this exact scope. Any later test that changes code path, force/constraint
handling, or scientific parameters needs its own decision.
