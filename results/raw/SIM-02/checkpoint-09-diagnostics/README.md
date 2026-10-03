# SIM-02 checkpoint 09 raw diagnostic archive

All LAMMPS runs used four MPI ranks, the OPT suffix, LAMMPS 10 Dec 2025, and a
1 fs timestep. Raw output and binary restarts are excluded from Git; the
committed compact record is `checkpoint-09-summary.json`, with hashes in
`sha256-manifest.json`.

- `zero-step/` plus `zero-step.txt` / `.log`: original production-path input
  initialized with all stages set to zero.
- `stage-a-2ps/` plus `stage-a-2ps.txt` / `.log`: 2,000 Stage-A steps, 20
  integrated samples, 400 K, maximum COM `6.5634249714037e-19 Å/fs`.
- `stage-a-20ps/` plus `stage-a-20ps.txt` / `.log`: completed 20,000 Stage-A
  steps, 200 integrated samples, 400 K, maximum COM
  `9.654782345768524e-19 Å/fs`; wall time 1:39:34. Its saved restart feeds the
  continuation diagnostic.
- `continuation-zero-step/`: restart files written by the follow-on input with
  both durations set to zero. They are setup-validation outputs and are not
  production restart points. `continuation-zero.log` records the successful
  initialization.
- `stage-b-nve/` plus `stage-b-nve.txt`, `.log`, and `-lammps.log`: the 2 ps
  Stage-B continuation passed; the uncorrected NVE portion failed at 100 fs.
  Four NVE samples were captured through step 22,400 before interruption.
- `in.stage-c-zero-step` plus `stage-c-zero.txt`: zero-trajectory-step replay
  measuring COM across each Stage-C velocity adjustment.
- `in.continuation-b-nve` and `in.stage-c-zero-step`: raw copies of the tracked
  inputs at `simulations/SIM-02/lammps/in.checkpoint-09-continuation-b-nve` and
  `simulations/SIM-02/lammps/in.checkpoint-09-stage-c-zero-step`.

Several continuation setup attempts ended before any integrated steps while
the restart input re-enabled PPPM and restored the original neighbor skin and
capacity. Their logs are preserved; they are not treated as scientific run
failures. The NVE COM-ceiling breach is the measured diagnostic failure and is
reported in `results/reports/SIM-02-checkpoint-09-diagnostics.md`.
