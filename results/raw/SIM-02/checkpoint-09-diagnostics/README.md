# SIM-02 checkpoint 09 bounded diagnostics

These four-rank LAMMPS OPT runs validate the approved checkpoint-09 input
correction. They do not establish equilibrium or release eHEX.

- `zero-step.txt` and `zero-step.log`: full production path, all stage durations
  overridden to zero; PPPM/RATTLE setup and fix ordering passed.
- `stage-a-2ps.txt` and `.log`: 2,000 Stage-A steps, thermo every 100 steps;
  20 integrated samples stayed at 400 K, with maximum sampled COM speed
  `6.5634249714037e-19 Å/fs` against a `1e-6 Å/fs` limit.
- `stage-a-20ps.txt` and `.log`: 20,000-step Stage-A extension, running at the
  last recorded check. See `checkpoint-09-summary.json` for its progress.

The run outputs are excluded from Git. After the 20 ps, Stage-B, and NVE
diagnostics finish, preserve compact measured results and SHA-256 hashes in the
research record.
