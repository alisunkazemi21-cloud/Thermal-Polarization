# SIM-02 checkpoint 08 — PPPM equilibrium bridge

- **Prepared:** 2026-09-30
- **Status:** `[APPROVED — DECISION-008; INPUT ZERO-STEP PARSE PASSED]`
- **Depends on:** DECISION-007 and gate 1
- **Execution status:** the 1.52 ns trajectory has not started

## Checkpoint question

Should SIM-02 erase the velocity field in the imported nonequilibrium author
snapshot and build a fixed-volume 400 K PPPM reference before eHEX is applied?

**Decision:** approved by the user on 2026-10-01 and recorded in DECISION-008.

## Why a bridge is required

`[MEASURED]` Gate 1 showed that the imported 4,500-water configuration is
structurally valid and that modern LAMMPS can initialize RATTLE and PPPM. Its
step-zero temperature was 404.21051 K. The author package identifies this file
as a steady-state NEMD configuration, so its velocities cannot be treated as an
equilibrium sample.

`[ESTABLISHED]` The paper prepared its original lattice for 20 ps with velocity
rescaling, 200 ps NpT, a rescaling to the target box, 500 ps NVT, a final
kinetic-energy adjustment, and 1 ns NVE. It reports an NVE mean temperature of
400 ± 0.1 K from block analysis.

`[OPEN SOURCE DETAIL]` The paper does not state the NpT target pressure or the
velocity-rescaling cadence. We also do not start from its lattice; we start from
its published steady-state configuration. A literal reconstruction would
therefore require undocumented choices.

## Proposed bridge

Keep the exact published box and density fixed. Replace every imported velocity
with a deterministic Maxwell distribution at 400 K using seed `20260930` and
remove net linear and angular momentum. Then run:

| Stage | Ensemble/control | Steps at 1 fs | Duration | Purpose |
|---|---:|---:|---:|---|
| A | NVE + direct velocity rescaling every 100 steps | 20,000 | 20 ps | erase the NEMD velocity field and reproduce the documented initial control in an explicit form |
| B | Nosé–Hoover NVT, 400 K, 1 ps damping | 500,000 | 500 ps | relax the PPPM liquid at the exact benchmark volume |
| C | exact velocity scale to 400 K | 0 | instantaneous | reproduce the documented kinetic-energy adjustment before NVE |
| D | NVE | 1,000,000 | 1 ns | measure the equilibrium bridge without a thermostat |

RATTLE tolerance remains `1e-10` with 400 iterations. The Lennard-Jones cutoff,
PPPM accuracy, force field, box, and 1 fs timestep remain those already parsed
in gate 1. No eHEX fix or spatial reservoir is active.

This is a bridge from the supplied author state to the project's modern PPPM
implementation. It is not described as a verbatim reconstruction of the
paper's lattice-to-liquid preparation.

## Frozen evidence and output plan

- Thermodynamic values every 1 ps: step, time, temperature, pressure, potential
  energy, kinetic energy, total energy, volume, box lengths, and COM velocity.
- Alternating binary restarts every 50 ps and explicit stage-boundary restarts.
- A sorted, gzip-compressed coordinate/velocity frame every 10 ps. Roughly 152
  frames are enough for spatial-temperature and geometry
  checks without the hundreds-of-gigabytes output implied by a 50 fs cadence.
- O–O RDF sampled every 1 ps and averaged into non-overlapping 100 ps output
  blocks during NVE. Statistical independence must be assessed, not assumed.
- Full-precision final data and restart files for the next eHEX gate.
- Raw trajectories and binary restarts remain outside Git; manifests, logs,
  compact tables, analysis code, and reports enter the repository.

## Acceptance criteria frozen before execution

Gate 2 passes only if all primary criteria pass:

1. **Integrity:** 4,500 molecules, 13,500 atoms, zero net charge, and the exact
   target box survive the fixed-volume bridge.
2. **Completion:** all 1,520,000 steps finish without a LAMMPS error, lost atom,
   or RATTLE failure.
3. **NVE temperature:** the 1 ns block mean is within 1 K of 400 K and its block
   standard error is at most 0.5 K. The paper's 400 ± 0.1 K remains the reference,
   not a silently relaxed project result.
4. **NVE energy:** the magnitude of the fitted 1 ns total-energy change divided
   by the mean absolute total energy is at most `5e-5` (0.005%). Report the raw
   endpoint change as a sensitivity check, but use the fitted drift for the gate.
5. **Constraints and contacts:** final O–H deviations are at most `1e-5 Å`, final
   H–O–H deviations are at most `1e-3°`, and no O–O separation is below `2.2 Å`.
6. **Erased thermal gradient:** for molecular-COM temperature in ten equal z
   slabs, the block-weighted linear slope has a 95% confidence interval that
   includes zero and no slab mean differs from the global mean by more than two
   of its own block standard errors.
7. **Structural stationarity:** between the first and second 500 ps NVE halves,
   the O–O first-peak position differs by no more than `0.05 Å` and the
   coordination number at the first minimum differs by no more than `0.10`.
8. **Momentum:** the final center-of-mass speed is reported, is at most
   `1e-6 Å/fs`, and shows no systematic growth relative to the stage-start
   four-rank RATTLE floor. No periodic momentum-removal fix may hide a drift.
   This numerical threshold was frozen before step 1 after the MPI execution
   path reproducibly gave `5.9e-7 Å/fs` at constraint initialization; its COM
   kinetic energy is about `1e-8` of the system thermal kinetic energy.

Pressure is reported but is not a pass/fail target because volume is fixed and
the source does not document an NpT pressure. Density is an integrity invariant,
not an independently fitted result.

## Restart and Colab contract

The local 10 ps restart-continuity test must precede a cloud trajectory. Compare
one uninterrupted 10 ps NVE segment with two 5 ps segments restored from a
binary restart. LAMMPS restarts can change neighbor-list timing, so acceptance is
statistical agreement of conserved quantities rather than bitwise coordinates.

For Colab, pin the LAMMPS version and build metadata, copy each 50 ps restart and
log to durable storage, and reissue every fix with the same ID after
`read_restart`. Gate 2 has no eHEX state. Later eHEX runs require the eHEX fix to
be reissued because that fix does not store state in binary restarts.

## Release consequence

Passing gate 2 releases only the 100 ps, 1 fs eHEX smoke test. It does not
establish a thermal gradient, polarization, or agreement between PPPM and the
paper's Ewald trajectory. A failed criterion becomes a measured result and
returns the protocol to review.
