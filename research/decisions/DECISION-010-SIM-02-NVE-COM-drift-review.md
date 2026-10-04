# DECISION-010 — Review of checkpoint-09 NVE COM drift

- Date opened: 2026-10-03
- Status: **Checkpoint 10 complete; follow-up recorded in DECISION-011**
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

## Approved diagnostic scope (2026-10-04)

The user approved the recommended matched single-MPI-rank NVE diagnostic. Replay
Stage B from the same completed 20 ps Stage-A restart, then execute the existing
Stage-C initialization and up to 2 ps of uncorrected NVE. Keep the 1 fs timestep,
100-step thermo cadence, 400 K velocity scale, RATTLE settings, OPT suffix, and
one OpenMP thread. Change only the MPI rank count (four to one) and the output
location. Keep periodic momentum correction disabled during NVE and retain the
`1e-6 Å/fs` ceiling. The tracked input is
`simulations/SIM-02/lammps/in.checkpoint-10-single-rank-nve`.

## Measured one-rank result (2026-10-04)

The one-rank OPT run replayed Stage B from the same 20 ps Stage-A restart, then
completed 2 ps of uncorrected NVE. Stage B had 20 samples from 395.56237 to
404.86220 K and ended at 400.55730 K. The NVE segment had 20 samples through
step 24,000 (2 ps); temperature ranged from 392.66022 to 402.37766 K and ended
at 399.69651 K. Maximum sampled COM speed was
`1.0435411502651417e-18 Å/fs` at 1.9 ps, with no ceiling exceedance.

Compared with the four-rank run's first-sample failure at 100 fs, this indicates
rank-sensitive behavior in the Stage-B-to-NVE continuation. Stage B was replayed
under each rank count, so the phase-space state entering Stage C differed. This
does not isolate the cause to the NVE integrator, RATTLE, or an MPI reduction.
The LAMMPS log contains the completion marker and final restart; a shell-wrapper
`printf` error prevented capture of the LAMMPS exit code after completion. See
`results/reports/SIM-02-checkpoint-10-one-rank-nve.md` and the local raw archive.

## Boundary and proposed follow-up

The full bridge remains on hold. No scientific parameter, COM threshold, or
NVE momentum policy changed. The user approved a same-restart rank comparison
on 2026-10-04; its scope and measured outcome are recorded in DECISION-011 and
`results/reports/SIM-02-checkpoint-11-same-restart-one-rank.md`.
