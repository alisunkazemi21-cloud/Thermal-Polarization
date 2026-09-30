# SIM-02 checkpoint 08 raw evidence

This directory is reserved for the PPPM equilibrium-bridge run. The large
restart, trajectory, and final-data files are ignored by Git. After execution,
preserve the LAMMPS log, a SHA-256 manifest of every raw artifact, compact CSV
tables, and the gate report in version control.

`dry-run-stdout.txt` and `dry-run-log.lammps` preserve the input validation with
all three stage durations replaced by zero. LAMMPS 10 Dec 2025 parsed every
stage, initialized PPPM and RATTLE, accepted `custom/gz` and RDF output, and
advanced zero steps. This is implementation evidence, not a gate-2 physical
result. At proposal time no trajectory has been run.
