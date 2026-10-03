# SIM-02 checkpoint 08 — Stage-A COM drift

Status: **stopped at the first integrated diagnostic because the frozen COM
criterion failed.** This is a measured implementation result, not equilibrium
or polarization evidence.

## Provenance

- Date: 2026-10-03
- Input commit: `a1da7bb`
- Command: `mpirun --oversubscribe -np 4 lmp -sf opt -in simulations/SIM-02/lammps/in.equilibrium-bridge ...`
- Engine: LAMMPS 10 Dec 2025, four MPI ranks, OPT suffix
- Planned bridge: 1,520,000 steps at 1 fs
- Last recorded step before termination: 2,000
- No scheduled 50,000-step restart was reached

## Measured observation

| Step | Stage | Temperature (K) | COM speed (Å/fs) | Frozen ceiling | Outcome |
|---:|---|---:|---:|---:|---|
| 0 | corrected initialization | 411.10151 | 4.3903e-7 | 1.0e-6 | pass |
| 1,000 | A, direct rescaling | 400.0 | 1.02778929e-5 | 1.0e-6 | fail |
| 2,000 | A, direct rescaling | 400.0 | 1.25105105e-5 | 1.0e-6 | fail |

The step-1,000 speed was 10.28 times the ceiling and the step-2,000 speed was
12.51 times the ceiling. The increase from initialization also violates the
approved no-systematic-growth condition. LAMMPS printed no warning or error;
this is a scientific acceptance failure rather than a program crash.

## Interpretation boundary

The direct rescaling stage held the reported temperature at exactly 400 K, but
the existing stage-boundary-only momentum removal did not keep the constrained
system's COM speed within the frozen bound. The run ended during the 20 ps
preparation stage, before NVT or NVE. It therefore provides no evidence about
equilibrium temperature, NVE energy drift, structure, z-stationarity, eHEX, or
polarization.

Any change to momentum handling must be proposed, justified, and approved as a
new checkpoint before relaunch. The preserved `stdout.txt`, `log.txt`, and
step-zero trajectory are the raw record for this stopped attempt.
