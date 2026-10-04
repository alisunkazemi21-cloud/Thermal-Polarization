# SIM-02 checkpoint 12 — four-rank high-cadence diagnostic

Approved 2026-10-04 in DECISION-012. Four-rank, one-thread Stage-C/NVE replay
from the exact checkpoint-11 Stage-B restart. The restart SHA-256 is
`3b43042a7dceb3f774708d54a57d76bc701cff44cfe7231afea299ba8a9494ef`.

The physical protocol is unchanged: LAMMPS 10 Dec 2025 OPT, 1 fs timestep,
400 K velocity scaling, RATTLE, and uncorrected NVE. COM components and speed
are recorded every timestep. The existing strict `1e-6 Å/fs` ceiling is checked
every timestep; the run halts at the first exceedance or after 400 fs.

This is an implementation diagnostic only. It does not release the full bridge
or establish equilibrium, eHEX heat transfer, a stationary gradient, or
polarization. Raw trajectory and restart outputs remain local/ignored; compact
summary, provenance, and hashes are the shareable record.

The initial `mpiexec -n 4` launcher attempt failed during rank allocation before LAMMPS started and advanced zero steps. The same approved simulation then ran with `mpirun --oversubscribe -np 4`; the retry stopped automatically at step 22,007 (7 fs) when COM speed first exceeded the frozen ceiling. The logged NVE trace is monotonic over the eight recorded samples. LAMMPS exit code 0 records the configured soft halt and finalization, not a COM pass.
