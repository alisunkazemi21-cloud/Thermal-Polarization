# SIM-02 checkpoint 09 — preparation-stage momentum control

## Checkpoint question

Should checkpoint 08 be revised to remove whole-system linear momentum every
100 steps during thermostatted preparation only, with kinetic-energy rescaling,
then disable that operation before the NVE acceptance stage?

Status: **approved by the user on 2026-10-03; Stage-A (2 ps and 20 ps) and
Stage-B (2 ps) diagnostics passed; the uncorrected NVE diagnostic failed the
COM ceiling at 100 fs. See DECISION-010 for the pending follow-up.**

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
velocities. The corrected Stage-A and Stage-B ordering defines RATTLE after
velocity-changing fixes.

## Measured checkpoint-09 outcome

Stage A completed 20,000 steps at 400 K. Its 200 integrated samples had maximum
COM speed `9.654782345768524e-19 Å/fs`. The 2,000-step Stage-B transition
finished at 399.81022 K with maximum sampled COM speed
`8.507873362730173e-19 Å/fs`.

The subsequent NVE check, with periodic momentum control disabled as approved,
first exceeded the `1e-6 Å/fs` ceiling at 100 fs (`7.144552366951081e-6
Å/fs`). It was interrupted after 400 fs; peak sampled speed was
`8.357269209836094e-6 Å/fs`. The Stage-C zero-step replay ended at
`4.8768857346949e-8 Å/fs` after the final velocity cleanup, so the cause of the
later excursion remains unconfirmed. The full equilibrium bridge was not
relaunched. See the [results report](../../results/reports/SIM-02-checkpoint-09-diagnostics.md)
and pending [DECISION-010](../decisions/DECISION-010-SIM-02-NVE-COM-drift-review.md).

Primary sources:

- <https://docs.lammps.org/fix_momentum.html>
- <https://docs.lammps.org/fix_temp_rescale.html>
- <https://docs.lammps.org/fix_shake.html>

## Interpretation

`[MEASURED — CHECKPOINT 08]` Without periodic momentum control, Stage-A COM
speed exceeded the frozen ceiling and rose from the corrected initialization
value. That failure triggered DECISION-009.

`[MEASURED — CHECKPOINT 09]` The approved preparation-only correction passed
both Stage-A durations and the short Stage-B transition. Once the correction
was removed for NVE, COM speed exceeded the same ceiling at 100 fs. A Stage-C
zero-step replay ended below the ceiling after the final velocity cleanup, so
the excursion occurred during integration; its mechanism is unresolved.

`[INFERRED / UNCONFIRMED]` RATTLE and parallel reduction behavior may contribute
to the NVE COM excursion. The current measurements do not establish a cause.

`[APPROVED]` DECISION-009 confines periodic momentum removal to preparation.
No periodic correction is active in NVE, preserving the original momentum
acceptance test. The test failed, so the full bridge remains on hold.

## Follow-up choices

DECISION-010 records the open review. Candidate diagnostics include testing a
short NVE segment with one MPI rank to check rank sensitivity, then isolating
the Stage-C initialization ordering if needed. The frozen COM threshold remains
unchanged unless the user approves a justified revision.

## Verification sequence after approval

1. Parse and initialize the revised production path with zero steps.
2. Run a 2 ps four-rank OPT diagnostic with thermo every 100 steps.
3. If every preparation record is at or below `1e-6 Å/fs`, extend the test to
   the full 20 ps Stage A.
4. Run a short Stage-B transition diagnostic and verify temperature, constraints,
   and COM behavior. **Passed:** 2 ps; final temperature 399.81022 K.
5. Enter an NVE diagnostic with the periodic fix removed. Require the original
   COM ceiling and no-growth condition. **Failed:** first sample at 100 fs was
   `7.144552366951081e-6 Å/fs`; interrupted at 400 fs.
6. A full 1.52 ns bridge relaunch is **not authorized by this failed sequence**;
   DECISION-010 must resolve the next diagnostic first.

## Progress record

- Four-rank OPT production-path zero-step check: **passed**; all stages parsed,
  PPPM and RATTLE initialized, and the input completed at step 0.
- Four-rank OPT Stage-A 2 ps diagnostic: **passed**; all samples every 100
  steps reported 400 K and COM components at approximately `1e-19 Å/fs`.
- Four-rank OPT Stage-A 20 ps diagnostic: **passed**; 200 samples at 400 K,
  maximum COM `9.654782345768524e-19 Å/fs`.
- Four-rank OPT Stage-B 2 ps continuation: **passed**; endpoint 399.81022 K,
  maximum COM `8.507873362730173e-19 Å/fs`.
- Four-rank OPT uncorrected NVE: **failed** at 100 fs; maximum sampled COM
  `8.357269209836094e-6 Å/fs` through 400 fs.
- Full bridge: **on hold** pending DECISION-010.

## Approval boundary

The user approved only the input revision and bounded diagnostic sequence above.
This does not approve eHEX, change the frozen box,
temperature path, timestep, force field, electrostatics, or gate-2 acceptance
tests.
