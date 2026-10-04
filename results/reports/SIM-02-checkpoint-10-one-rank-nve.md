# SIM-02 checkpoint 10 — one-rank NVE diagnostic

**Run date:** 2026-10-04  
**Authorization:** User-approved diagnostic recorded in DECISION-010  
**Scope:** Matched continuation comparison; no full-bridge release

## Question and protocol

Checkpoint 09's four-rank continuation exceeded the frozen center-of-mass
(COM) speed ceiling at the first 100 fs NVE sample. The approved follow-up
repeated the 2 ps Stage-B NVT transition from the same 20 ps Stage-A restart,
then ran 2 ps of uncorrected NVE with one MPI rank. The 1 fs timestep, 100-step
thermo sampling, 400 K scale, RATTLE settings, OPT suffix, one OpenMP thread, and
`1e-6 Å/fs` COM-speed ceiling were retained. Periodic momentum correction
remained disabled during NVE. The input changed only the output path relative to
the checkpoint-09 continuation input; MPI rank count changed from four to one.

Because Stage B was replayed under each rank count, the phase-space state
entering Stage C was not identical between the two continuations. The experiment
tests rank sensitivity of the Stage-B-to-NVE continuation as a whole; it does
not isolate NVE integration, RATTLE, or a particular MPI reduction as the cause.

## Measured results

| Segment | Samples | Temperature range / endpoint | Maximum sampled COM speed | Ceiling result |
|---|---:|---|---:|---|
| Stage B NVT, 2 ps | 20 (steps 20,100–22,000) | 395.56237–404.86220 K; endpoint 400.55730 K | `2.9949981187046465e-19 Å/fs` at step 21,200 | Passed |
| Uncorrected NVE, 2 ps | 20 (steps 22,100–24,000) | 392.66022–402.37766 K; endpoint 399.69651 K | `1.0435411502651417e-18 Å/fs` at step 23,900 | Passed; zero exceedances |

The first NVE sample at 100 fs measured `2.65403473960656e-19 Å/fs`. All 20
NVE samples remained far below the `1e-6 Å/fs` ceiling. LAMMPS reached step
24,000, printed `SIM02_GATE2 nve_complete=yes`, wrote its final restart, and
reported a wall time of 32:23. Stderr is empty.

For comparison, the prior four-rank check captured four NVE samples through
400 fs. Its first sample at 100 fs was `7.144552366951081e-6 Å/fs`, already
above the same ceiling; its peak was `8.357269209836094e-6 Å/fs`. Thus the
observed COM outcome depends on rank count somewhere in these continuation
runs. This supports further controlled diagnosis, while the Stage-B trajectory
difference prevents attributing the result solely to NVE's MPI/RATTLE behavior.

## Execution-record limitation

After LAMMPS completed, the shell wrapper failed while writing its exit-code
file because its `printf` command was malformed. The LAMMPS process exit status
was therefore not captured. The completion marker, final restart, 32:23 LAMMPS
wall-time record, and empty stderr document successful completion. This is a
wrapper bookkeeping error after the measured run, not a simulation failure.

## Interpretation and boundary

This is a bounded implementation diagnostic, not a 2 ps equilibrium result.
It does not measure energy drift, structural equilibration, stationarity,
eHEX heat transfer, temperature-gradient profiles, or polarization. The full
equilibrium bridge remains on hold. No acceptance threshold or scientific
parameter changed; no NVE momentum correction was introduced.

The user later approved this same-restart diagnostic in DECISION-011. The
checkpoint-11 result is recorded in
`results/reports/SIM-02-checkpoint-11-same-restart-one-rank.md`.

## Reproducibility records

- Tracked input: `simulations/SIM-02/lammps/in.checkpoint-10-single-rank-nve`
- Raw LAMMPS log, stdout, stderr, and restarts: `results/raw/SIM-02/checkpoint-10-single-rank-nve/`
- Compact machine-readable summary: `results/raw/SIM-02/checkpoint-10-single-rank-nve/checkpoint-10-summary.json`
- Raw archive SHA-256 manifest: `results/raw/SIM-02/checkpoint-10-single-rank-nve/sha256-manifest.json`
- Approval and follow-up boundary: `research/decisions/DECISION-010-SIM-02-NVE-COM-drift-review.md`
