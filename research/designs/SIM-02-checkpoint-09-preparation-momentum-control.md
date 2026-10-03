# SIM-02 checkpoint 09 — preparation-stage momentum control

## Checkpoint question

Should checkpoint 08 be revised to remove whole-system linear momentum every
100 steps during thermostatted preparation only, with kinetic-energy rescaling,
then disable that operation before the NVE acceptance stage?

Status: **proposed for review; not approved; input unchanged.**

## Triggering evidence

The corrected four-rank OPT bridge initialized below the frozen COM-speed
ceiling but failed immediately after integration:

| Step | Stage | Temperature (K) | COM speed (Å/fs) | Criterion |
|---:|---|---:|---:|---|
| 0 | corrected initialization | 411.10151 | 4.3903e-7 | pass |
| 1,000 | A, direct rescaling | 400.0 | 1.02778929e-5 | fail |
| 2,000 | A, direct rescaling | 400.0 | 1.25105105e-5 | fail |

The run stopped at 2 ps. It never reached NVT or NVE. LAMMPS emitted no warning
or error. The measured failure is documented in
`results/reports/SIM-02-checkpoint-08-stage-a-com-drift.md`.

## Source evidence

The LAMMPS `fix momentum` documentation states that linear momentum is zeroed by
subtracting the group COM velocity from each atom, leaving every pairwise
relative velocity unchanged. Its `rescale` keyword restores the group's kinetic
energy after removal. The command is intended to prevent drift caused by
perturbations.

The LAMMPS RATTLE documentation states that `fix rattle` modifies forces and
velocities and should be defined after other fixes that modify forces or
velocities. The current Stage-A order defines RATTLE before `fix temp/rescale`;
that ordering should be corrected in the same bounded test.

Primary sources:

- <https://docs.lammps.org/fix_momentum.html>
- <https://docs.lammps.org/fix_temp_rescale.html>
- <https://docs.lammps.org/fix_shake.html>

## Interpretation

`[MEASURED]` Stage-A COM speed exceeded the frozen ceiling and grew from the
corrected initialization value.

`[INFERRED]` The combination of repeated velocity rescaling, constrained
velocity correction, parallel round-off, and the current fix ordering permits
small global momentum errors to accumulate. The short record does not isolate
one component as the sole cause.

`[DECISION NEEDED]` Periodic momentum removal would be confined to preparation,
where velocities are already deliberately changed by temperature control. It
would be absent from Stage D so the NVE no-growth test remains an unmasked
integrator/constraint diagnostic.

## Options

1. **Recommended — bounded preparation-only correction.** Define
   `fix momentum 100 linear 1 1 1 rescale` before RATTLE in Stages A and B;
   define temperature-control and integration fixes before RATTLE; remove the
   momentum fix before Stage C/D. Keep the one-time Stage-D linear and angular
   removal and the original `1e-6 Å/fs` plus no-growth NVE criterion.
2. Run on one MPI rank. This avoids relying on the observed four-rank path but
   greatly increases wall time and does not establish that integrated COM drift
   will remain below the criterion.
3. Raise the COM threshold. This is rejected as an immediate response because
   it would relax a frozen criterion after seeing a failure without an
   independent physical justification.

## Verification sequence after approval

1. Parse and initialize the revised production path with zero steps.
2. Run a 2 ps four-rank OPT diagnostic with thermo every 100 steps.
3. If every preparation record is at or below `1e-6 Å/fs`, extend the test to
   the full 20 ps Stage A.
4. Run a short Stage-B transition diagnostic and verify temperature, constraints,
   and COM behavior.
5. Enter an NVE diagnostic with the periodic fix removed. Require the original
   COM ceiling and no-growth condition.
6. Only then relaunch the full 1.52 ns bridge from step zero.

## Approval boundary

Approval of this checkpoint would authorize only the input revision and bounded
diagnostic sequence above. It would not approve eHEX, change the frozen box,
temperature path, timestep, force field, electrostatics, or gate-2 acceptance
tests.
