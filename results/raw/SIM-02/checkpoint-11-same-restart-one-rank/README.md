# SIM-02 checkpoint 11 — same-restart rank diagnostic

Approved 2026-10-04 in DECISION-011. This diagnostic reads the four-rank
checkpoint-09 Stage-B restart and executes Stage-C initialization plus up to
2 ps of uncorrected NVE at one MPI rank. The LAMMPS version, OPT suffix, one
OpenMP thread, 1 fs timestep, sampling cadence, RATTLE settings, velocity
initialization, and `1e-6 Å/fs` COM ceiling are retained. No NVE momentum
correction is active.

The restart was copied byte-for-byte from
`results/raw/SIM-02/checkpoint-09-diagnostics/stage-b-nve/stage-b-2ps.restart`;
its source SHA-256 is recorded in DECISION-011. This is an implementation
diagnostic, not an equilibrium or polarization result. See the report and raw
manifest after execution completes.
