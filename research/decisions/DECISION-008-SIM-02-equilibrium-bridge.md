# DECISION-008 — approve the PPPM equilibrium bridge

- **Date:** 2026-10-01
- **Status:** Approved
- **Decision source:** user approval of checkpoint 08
- **Depends on:** DECISION-007 and gate 1

## Decision

Approve the fixed-volume 400 K PPPM equilibrium bridge defined in
`research/designs/SIM-02-checkpoint-08-equilibrium-bridge.md` and implemented by
`simulations/SIM-02/lammps/in.equilibrium-bridge`.

The run replaces the imported nonequilibrium velocity field using deterministic
seed `20260930`, performs 20 ps of direct velocity rescaling, 500 ps NVT with a
1 ps Nosé–Hoover damping time, an exact constrained-system kinetic-energy
adjustment to 400 K, and 1 ns NVE at a 1 fs timestep. The exact published box
and density remain fixed.

The paper's 200 ps NpT stage is not copied because its target pressure is not
reported and the project begins from the supplied steady-state configuration,
not the paper's lattice. This boundary must remain explicit in comparisons.

## Pre-execution evidence

LAMMPS 10 Dec 2025 parsed every stage with all run durations replaced by zero.
The final parse had no warning or error, initialized PPPM at the gate-1 force
accuracy, applied RATTLE after each integrator, evaluated the final constrained
temperature as 400 K, and advanced zero trajectory steps.

## Release condition

Execution is released. Gate 2 passes only through the acceptance criteria frozen
in checkpoint 08. Approval does not predetermine its outcome and does not release
eHEX until the equilibrium evidence has been analyzed and documented.

## Pre-run implementation correction

The first four-rank launch stopped before step 1 when parallel RATTLE
initialization left a small COM velocity after the earlier momentum removal.
Standard and optimized kernels reproduced the same `5.9e-7 Å/fs` stage-start
floor, showing that it is associated with MPI constraint decomposition rather
than the optimized pair kernel. This speed is about 0.06 m/s and its COM kinetic
energy is roughly `1e-8` of the thermal kinetic energy.

The input now initializes RATTLE before explicit stage-boundary momentum
removal. Before trajectory execution, the checkpoint's qualitative “numerical
noise” criterion was operationally frozen as COM speed at most `1e-6 Å/fs` with
no systematic growth. No periodic momentum-removal fix is used. This enforces
the approved protocol without changing the ensemble, timestep, seed, force
field, or acceptance intent. The stopped initialization and raw output are
preserved under `history/SIM-02-checkpoint-08-mpi-momentum-init/`.

The user explicitly approved this production-path correction and numerical
threshold on 2026-10-03. Gate-2 relaunch from step zero is authorized.
