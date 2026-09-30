# SIM-02 technical report — pre-execution record

Status: **gate 1 zero-step audit passed; checkpoint 08 equilibrium bridge is
approved in DECISION-008; no gate-2 result or polarization result exists.**
Proposed values belong in the design document until their gate is released.

## 1. Research question

Can bulk rigid SPC/E water under a controlled heat flux develop a stationary,
statistically resolved signed polarization profile?

## 2. Approved method boundary

- Engine/mechanism: LAMMPS eHEX (DECISION-005).
- Scope: gradient, heat transport, orientation, polarization.
- Electrical field, voltage, current, and power are outside SIM-02.

## 3. Configuration

`[MEASURED]` The imported author configuration contains 4,500 neutral SPC/E
molecules in a 36.3534308725 × 36.3534308725 × 109.060578798 Å³ box. The
deterministic structure audit and LAMMPS 10 Dec 2025 `run 0` passed. See
`SIM-02-checkpoint-07-zero-step.md`; no trajectory step was advanced.

## 4. Equilibrium bridge

`[APPROVED; TO TEST]` Checkpoint 08 keeps the exact author box, replaces the imported
steady-state velocities using seed `20260930`, and schedules 20 ps direct
rescaling, 500 ps NVT, and 1 ns NVE at 1 fs. Temperature, O–O RDF, constraint
stability, energy drift, z-temperature flattening, and momentum have frozen
acceptance tests. No checkpoint-08 trajectory has run.

## 5. eHEX pilot

`[TO TEST]` Energy balance, heat-flux conversion, reservoir occupancy,
temperature/density profiles, symmetry, and stability.

## 6. Steady state and production

`[TO TEST]` Stationarity windows and accepted production blocks.

## 7. Results

`[TO MEASURE]` T(z), ρ(z), Jq, Pz(z), <cos θ(z)>, Pz versus ρ, and uncertainty.

## 8. Interpretation and limitations

No interpretation is permitted until the measured profiles and block
uncertainties are available.

## 9. Reproducibility record

The completed report must list the LAMMPS version, installed packages, platform,
commit, SPC/E provenance, exact inputs, seeds, box/count, heat rate, durations,
sampling, analysis version, and every non-automated operation.
