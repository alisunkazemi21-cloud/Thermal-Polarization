# DECISION-014 — Consolidated SIM-02 bridge go/no-go proposal

- Date: 2026-10-04
- Status: **Proposed; no full-bridge run authorized by this document**
- Depends on: DECISION-007 through DECISION-013

## Why consolidate now

Checkpoint 13 closes the matched high-cadence rank comparison. One rank stayed
below the COM ceiling for 400 fs; four ranks crossed it after 7 fs from the
same Stage-B restart. Rank-count-sensitive behavior is supported for this
saved-state sequence, while its mechanism is unresolved. Additional short
mechanism probes would extend the path without producing SIM-02's intended
equilibrium or heat-transport result.

## Proposed decision

Choose one of two endpoints:

1. **One final Gate 2 attempt:** authorize one resource-appropriate execution
   of the already frozen fixed-volume 400 K bridge from DECISION-008, with its
   1.52-million-step protocol and all eight acceptance criteria unchanged.
   Before launch, record and validate the chosen LAMMPS build, execution host,
   rank/thread layout, restart-continuity plan, and expected wall time. The
   measured one-rank CP13 path may inform the layout, but this proposal does
   not assume it will satisfy the 1 ns NVE energy or temperature criteria.
   At CP13's observed 400 steps in 3:57, linear extrapolation gives about 10.4
   days for 1.52 million steps on that local path; this is a rough resource
   estimate, not a measured full-bridge runtime. The execution host therefore
   needs durable restart storage and enough sustained runtime for the frozen
   protocol.
   A failed criterion ends the attempt; no further diagnostic ladder or
   parameter sweep is implied.
2. **Close the current method path:** do not spend more compute on this
   protocol. Publish the rank-count-sensitive COM result and its unresolved
   cause as the current SIM-02 outcome, leaving eHEX, gradient, and
   polarization unmeasured.

## Frozen scientific boundary

For option 1, do not change the force field, box, cutoff, PPPM accuracy,
RATTLE settings, timestep, preparation stages, or DECISION-008 thresholds.
The already approved 400 K bridge remains a method-validation study, not the
300 K target and not an eHEX production result. A new scientific method or
threshold requires a separate decision.

This proposal asks the user to select option 1 or 2. No run is authorized until
that choice is recorded.
