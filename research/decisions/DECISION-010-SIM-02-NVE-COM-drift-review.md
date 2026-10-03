# DECISION-010 — Review of checkpoint-09 NVE COM drift

- Date opened: 2026-10-03
- Status: **Pending user discussion; no corrective action approved**
- Depends on: DECISION-009 and the checkpoint-09 results report

## Measured evidence

The 20 ps Stage-A diagnostic and the 2 ps Stage-B transition passed their
bounded implementation checks. In the 2 ps uncorrected NVE diagnostic, the
first sample at 100 fs had COM speed `7.144552366951081e-6 Å/fs`, above the
frozen `1e-6 Å/fs` ceiling. The run reached 0.4 ps before interruption, with a
maximum sampled speed of `8.357269209836094e-6 Å/fs`. At the Stage-C zero-step
boundary, after temperature scaling and both velocity cleanup commands, COM
speed was `4.8769e-8 Å/fs`. The excursion therefore developed during NVE
integration; its mechanism is not yet established.

This diagnostic failure blocks the full equilibrium bridge. It does not
establish an equilibrium or polarization result. No scientific parameter or
acceptance threshold has been changed.

## Questions for the next checkpoint

1. Should a matched short NVE diagnostic be repeated with one MPI rank to test
   whether the excursion depends on parallel RATTLE/reduction behavior?
2. If the excursion persists, should we compare a carefully isolated Stage-C
   initialization ordering while keeping periodic momentum correction disabled
   during NVE?
3. Should the existing `1e-6 Å/fs` ceiling remain unchanged unless evidence
   demonstrates it is incompatible with the accepted implementation?

## Boundary

Until a follow-up decision is made, do not relaunch the full bridge, add
periodic momentum removal to NVE, or relax the frozen ceiling. The current
proposal is diagnostic only; these questions are not approved decisions.
