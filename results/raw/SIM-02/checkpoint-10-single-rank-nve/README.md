# SIM-02 checkpoint 10 — single-rank NVE diagnostic

User-approved 2026-10-04. The one-MPI-rank run replayed the 2 ps Stage-B NVT
transition from the same 20 ps Stage-A restart used for checkpoint 09, then ran
2 ps of uncorrected NVE. It used LAMMPS 10 Dec 2025, OPT suffix, one OpenMP
thread, 1 fs steps, and thermo every 100 steps. Only MPI rank count and output
location changed relative to the four-rank continuation input. The rank count
also changes the Stage-B trajectory, so this does not isolate NVE/RATTLE as the
cause of the different COM outcomes.

The run reached final step 24,000; LAMMPS printed its completion marker and
wrote the final restart. Wall time was 32:23 and stderr is empty. The shell
wrapper failed after completion while writing its exit-code record, so the
LAMMPS process exit status itself was not captured. See `run-metadata.json`.

`checkpoint-10-summary.json` contains compact measured results. The raw LAMMPS
log, stdout, Stage-B restart, and final restart are retained locally and covered
by `sha256-manifest.json`; raw trajectories and binary restarts are excluded
from Git. The replay input is also archived here and tracked at
`simulations/SIM-02/lammps/in.checkpoint-10-single-rank-nve`.
