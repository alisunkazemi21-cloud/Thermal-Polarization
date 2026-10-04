# DECISION-012 — Four-rank high-cadence SIM-02 NVE diagnostic

- Date: 2026-10-04
- Status: **Approved; diagnostic complete; mechanism review pending**
- Depends on: DECISION-011 and the checkpoint-11 same-restart archive

## Question

Checkpoint 11 established that the one-rank continuation stayed below the
center-of-mass (COM) speed ceiling while the four-rank continuation from the
same Stage-B restart exceeded it at 100 fs. The first four-rank sample does not
show when the excursion began. This bounded replay samples each integration
step to locate the first crossing without changing the physical protocol.

## Approved scope

Use the byte-identical four-rank Stage-B restart archived with checkpoint 11,
SHA-256
`3b43042a7dceb3f774708d54a57d76bc701cff44cfe7231afea299ba8a9494ef`.
Run four MPI ranks and one OpenMP thread on the same Ubuntu-on-WSL LAMMPS
10 Dec 2025 installation with the OPT suffix. Keep the 1 fs timestep, 400 K
velocity scale, exact Stage-C command ordering, RATTLE settings, PPPM accuracy,
and uncorrected NVE policy. Do not remove momentum during NVE and do not alter
any scientific parameter.

Record COM velocity components and temperature at every timestep. Use a
`fix halt` check each timestep against the existing strict `1e-6 Å/fs` COM
ceiling; stop at the first exceedance or after 400 fs, whichever comes first.
The shorter bound covers the prior four-rank failure window. The sole protocol
change is diagnostic sampling/early stopping. Store the run under
`results/raw/SIM-02/checkpoint-12-four-rank-high-cadence/`.

The first-step trajectory shape can establish whether the sampled COM excursion
is gradual or abrupt and when it first crosses the ceiling. It cannot by itself
identify a specific cause (for example RATTLE, velocity cleanup, PPPM/MPI
reductions, or another rank-sensitive operation).

## Measured result (2026-10-04)

The first launcher invocation could not allocate four ranks and exited before
LAMMPS started. No simulation steps ran in that attempt. Retrying with
`mpirun --oversubscribe -np 4` (the launch option used by prior successful
four-rank runs) preserved the approved ranks and simulation protocol.

LAMMPS exited 0 after its per-step `fix halt` stopped NVE at step 22,007, 7 fs
after the post-cleanup start at step 22,000. COM speed was
`6.0282895e-8 Å/fs` at the post-cleanup start, rose at every recorded step, and
first exceeded the frozen `1e-6 Å/fs` ceiling at step 22,007. The first
exceedance was `1.1198276995146967e-6 Å/fs` according to the halt message
(the thermo table rounds this to `1.1198277e-6`). Temperature changed from
400.02681 K to 401.48097 K over the seven NVE steps. The total-energy column
also changed by +2.206 kcal/mol over the same interval; energy drift was not a
frozen acceptance test for this COM-timing diagnostic, so that observation is
recorded as exploratory only.

The per-step trace locates the onset and crossing. It does not establish why
the four-rank COM velocity grows, and it does not justify attributing the
change to RATTLE, velocity cleanup, PPPM/MPI reductions, or another mechanism.
The 400 fs maximum was not reached because the frozen COM ceiling triggered
the early stop. Exit code 0 reflects the configured soft halt and successful
record finalization, not a COM pass.

## Decision boundary

This is an implementation diagnostic. A crossing is a bounded failure; reaching
400 fs without one is only a bounded pass, not equilibrium validation. The full
bridge remains on hold until separate review. No equilibrium, eHEX, stationary
gradient, or polarization result follows from this run.
