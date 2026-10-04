# SIM-02 checkpoint 12 — four-rank high-cadence diagnostic

**Run date:** 2026-10-04  
**Authorization:** User-approved bounded run recorded in DECISION-012  
**Outcome:** COM ceiling exceeded 7 fs after NVE start; run halted automatically

## Question and protocol

Checkpoint 11 established different COM outcomes for one-rank and four-rank
continuations from the same Stage-B restart, but the four-rank trace sampled
only every 100 fs. Checkpoint 12 replays that same four-rank path and measures
the timing of the COM excursion at every integration step.

The Stage-B restart is byte-identical to the checkpoint-11 restart
(`3b43042a7dceb3f774708d54a57d76bc701cff44cfe7231afea299ba8a9494ef`). The
run used four MPI ranks, one OpenMP thread, LAMMPS 10 Dec 2025 with OPT, 1 fs
steps, the same RATTLE and PPPM settings, and the same Stage-C initialization.
Momentum removal remained disabled during NVE. Only the diagnostic cadence
and bounded stop logic changed: COM was sampled and checked each step, with a
400 fs maximum.

## Measured result

The first MPI launcher attempt failed before LAMMPS initialized because it
could not allocate four ranks. It advanced zero steps. The run then completed
using `mpirun --oversubscribe -np 4`; LAMMPS returned exit code 0 after the
configured soft halt and output finalization.

The post-cleanup state was step 22,000, temperature 400.02681 K, and COM speed
`6.0282895e-8 Å/fs`. COM speed increased at every one of the eight recorded
NVE samples. The first threshold crossing was step 22,007 (7 fs): the halt
message reports `1.1198276995146967e-6 Å/fs`, above the frozen `1e-6 Å/fs`
ceiling. The thermo table displays the same value rounded to
`1.1198277e-6 Å/fs`. Temperature at the crossing was 401.48097 K.

| NVE elapsed time | Step | COM speed (Å/fs) | Temperature (K) |
|---:|---:|---:|---:|
| 0 fs | 22,000 | 6.0282895e-8 | 400.02681 |
| 1 fs | 22,001 | 2.0777868e-7 | 400.17401 |
| 2 fs | 22,002 | 3.5564130e-7 | 400.36692 |
| 3 fs | 22,003 | 5.0377126e-7 | 400.58750 |
| 4 fs | 22,004 | 6.5317399e-7 | 400.81920 |
| 5 fs | 22,005 | 8.0494835e-7 | 401.04907 |
| 6 fs | 22,006 | 9.6016938e-7 | 401.26980 |
| 7 fs | 22,007 | 1.1198277e-6 | 401.48097 |

LAMMPS also reported a +2.206 kcal/mol change in the thermo total-energy column
over those seven steps. No energy-drift criterion was frozen for this
COM-timing diagnostic; treat this as an observed lead for a separately scoped
energy audit, not as a pass/fail result.

## Interpretation and boundary

The trace shows that the four-rank COM excursion begins immediately in this
Stage-C/NVE continuation and crosses the criterion by 7 fs, rather than first
appearing near the earlier 100 fs sample. The sampled trend and energy-column
change do not identify a mechanism. RATTLE, velocity initialization, MPI
reductions, PPPM, and other rank-sensitive operations remain hypotheses until
separately tested.

This is an implementation diagnostic only. It does not establish energy
conservation, equilibrium, eHEX heat transfer, a stationary thermal gradient,
or polarization. The full bridge remains on hold. The input, restart, logs,
exit status, compact summary, and SHA-256 manifest are recorded under
`results/raw/SIM-02/checkpoint-12-four-rank-high-cadence/`.
