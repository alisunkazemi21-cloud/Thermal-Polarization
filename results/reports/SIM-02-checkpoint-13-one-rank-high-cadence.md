# SIM-02 checkpoint 13 — one-rank high-cadence control

**Run date:** 2026-10-04  
**Authorization:** User approved DECISION-013 on 2026-10-04  
**Outcome:** Completed 400 fs; no COM ceiling crossing

## Question and protocol

Does the early COM excursion from checkpoint 12 recur at one rank when both
paths start from the same Stage-B restart and are sampled every integration
step?

The byte-identical checkpoint-11 Stage-B restart was used
(`3b43042a7dceb3f774708d54a57d76bc701cff44cfe7231afea299ba8a9494ef`). The
run used one MPI rank and one OpenMP thread, LAMMPS 10 Dec 2025 OPT, a 1 fs
timestep, the checkpoint-12 PPPM/RATTLE and Stage-C command ordering, 400 K
velocity scaling, uncorrected NVE, per-step COM/temperature/energy output, a
strict `1e-6 Å/fs` soft-halt ceiling, and a 400-step maximum. The only planned
protocol differences from checkpoint 12 were MPI rank count and output path.

## Measured result

LAMMPS reached step 22,400, printed the expected completion marker, and
recorded a total wall time of 3:57. The saved final restart confirms normal
end-of-input finalization. The launcher exit code was not separately captured.
The four-rank restart was accepted with LAMMPS's expected warning that its
processor count changed from four to one.

During the 400 fs NVE window, all 401 distinct per-step states were below the
frozen COM ceiling. The largest sampled COM speed was
`9.6530431e-19 Å/fs` at step 22,323; the final value was
`5.5176068520554e-19 Å/fs`. At 7 fs, the one-rank COM speed was
`2.3195258e-19 Å/fs`, compared with checkpoint 12's four-rank crossing at
`1.1198277e-6 Å/fs`.

The NVE temperature began at 400.04609 K, ranged from 395.87137 to 407.85020 K,
and ended at 397.39277 K. The total-energy column rose by 0.690 kcal/mol from
the post-cleanup NVE start to the final sample. No short-run energy or
temperature acceptance criterion was preregistered for DECISION-013; these
values are reported as diagnostics and do not pass or fail DECISION-008's
1 ns bridge criteria.

## Interpretation and boundary

Under matched restart and high-cadence sampling, the one-rank and four-rank
early-time COM traces differ sharply. This supports rank-count-sensitive
behavior in this saved-state Stage-C/NVE sequence. It does not identify the
responsible operation or prove that rank count alone is the physical cause.
The short run is not an equilibrium result and does not establish eHEX energy
accounting, a stationary thermal gradient, or polarization. The full bridge
remains held pending a consolidated go/no-go plan that uses the already frozen
DECISION-008 acceptance criteria.

## Provenance

Input: `simulations/SIM-02/lammps/in.checkpoint-13-one-rank-high-cadence`  
Compact execution record and hashes:
`results/raw/SIM-02/checkpoint-13-one-rank-high-cadence/`.
