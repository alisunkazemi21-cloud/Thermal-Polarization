# SIM-02 checkpoint 11 — same-restart one-rank diagnostic

**Run date:** 2026-10-04  
**Authorization:** User-approved diagnostic recorded in DECISION-011  
**Outcome:** Bounded implementation pass; rank-count-sensitive continuation observed

## Question and protocol

Checkpoint 10 showed different COM behavior between the four-rank and one-rank
continuations, but Stage B had been replayed independently at each rank count.
Checkpoint 11 holds that starting state fixed: it reads the four-rank
checkpoint-09 Stage-B restart and executes only Stage-C initialization plus
2 ps of uncorrected NVE at one MPI rank.

The 1 fs timestep, 100-step sampling, 400 K scale, RATTLE settings, OPT suffix,
one OpenMP thread, `1e-6 Å/fs` COM-speed ceiling, and input ordering were
retained. NVE momentum correction remained disabled. The only run-level change
from the prior four-rank continuation was MPI rank count; the source restart
was copied byte-for-byte and verified by SHA-256.

## Measured results

The one-rank run completed from step 22,000 through step 24,000 (2 ps), with
LAMMPS exit code 0 and wall time 14:02. The 20 sampled NVE rows (steps
22,100–24,000) had temperatures from 395.91302 to 406.10015 K and ended at
400.10536 K. The maximum sampled COM speed was
`1.2638166834526734e-18 Å/fs` at step 23,600; no sample exceeded the frozen
`1e-6 Å/fs` ceiling.

The four-rank run from this same Stage-B restart exceeded the ceiling at its
first 100 fs sample (`7.144552366951081e-6 Å/fs`) and stopped at 400 fs. Thus,
the COM outcome differs by rank count for a common saved starting state and
the same Stage-C/NVE sequence. The observation narrows the problem to
rank-count-sensitive behavior during this sequence, but it does not identify a
specific source such as RATTLE, velocity cleanup, or an MPI reduction.

## Decision boundary

This is an implementation diagnostic, not an equilibrium validation. It does
not establish energy drift, structural stability, eHEX heat transfer, a
stationary thermal gradient, or polarization. The full bridge remains on hold;
the scientific parameters and acceptance ceiling are unchanged.

Google Colab is a candidate for later, longer computation. This checkpoint
used the existing Ubuntu-on-WSL LAMMPS 10 Dec 2025 build to keep the software
environment aligned with the four-rank comparison. The local WSL runtime exposed 4 logical CPUs and 3,949,164 KiB of memory.
See the provenance and artifact hashes in
`results/raw/SIM-02/checkpoint-11-same-restart-one-rank/`.
