# Checkpoint 08 pre-run correction — MPI momentum initialization

- **Date:** 2026-10-01
- **Classification:** measured implementation failure before trajectory step 1
- **LAMMPS:** 10 Dec 2025, four MPI ranks, `-sf opt`

The first approved gate-2 launch reached only the stage-A step-zero diagnostic.
After parallel RATTLE initialization, its center-of-mass velocity was
`(5.7820e-7, 1.1293e-7, -5.9771e-8) Å/fs`, although the earlier
`velocity create ... mom yes rot yes` command had requested momentum removal.
No integration step was completed and this attempt is not gate-2 evidence.

The process was stopped before step 1. Its complete screen output, LAMMPS log,
and step-zero compressed frame are preserved in this directory.

The input correction initializes RATTLE with `run 0`, then explicitly removes
angular and linear momentum before the 20 ps rescaling stage and repeats linear
removal at later constraint-initialization boundaries. Standard and optimized
four-rank kernels reproduced the same stage-start floor: at most
`5.9e-7 Å/fs`, about 0.06 m/s and approximately `1e-8` of the thermal kinetic
energy. Before step 1, checkpoint 08 therefore froze `1e-6 Å/fs` plus no
systematic growth as the operational numerical-noise criterion. No periodic
momentum-removal fix is used.
