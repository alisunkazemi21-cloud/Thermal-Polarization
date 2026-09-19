# FAILED-001 — GROMACS preprocessing segmentation fault

- Date: 2026-09-18
- Stage: SIM-01 energy-minimization preprocessing
- Status: [ESTABLISHED] blocked before energy minimization

## Observation

[ESTABLISHED] `gmx solvate -cs spc216.gro -box 2.5 2.5 2.5 -o water.gro -p topol.top` completed and wrote a coordinate file containing 510 `SOL` residues.

[ESTABLISHED] The project preprocessing invocation was:

```bash
gmx grompp -f em.mdp -c water.gro -p topol.top -o em.tpr -po em-grompp.mdp -pp em-processed.top -maxwarn 0
```

[ESTABLISHED] The process terminated with `Segmentation fault` before `em.tpr` was produced.

[ESTABLISHED] A control invocation using GROMACS's installed `oplsaa.ff/forcefield.itp` and `oplsaa.ff/spce.itp` also did not produce a `.tpr` file.

[ESTABLISHED] The project inputs were copied to a native WSL `/tmp` control directory and the same project preprocessing command exited with code 1 before producing `em.tpr` there.

[ESTABLISHED] On 2026-09-18, the exact Ubuntu packages `gromacs=2025.4-1` and `gromacs-data=2025.4-1` were reinstalled with user approval.

[ESTABLISHED] `gmx --version` still reported `2025.4-Ubuntu_2025.4_1` after reinstallation.

[ESTABLISHED] The unchanged project preprocessing command then again exited with code 1 before producing `em.tpr`; package reinstallation did not resolve the fault.

## Consequence

[ESTABLISHED] `gmx mdrun -deffnm em` could not begin because `em.tpr` was absent.

[TO MEASURE] No minimization energy, force, temperature, pressure, density, RDF, or diffusion result exists.

## Changes made while diagnosing

[ESTABLISHED] The project `topol.top` was temporarily changed only for the stock-force-field control and was restored to `#include "../../models/SPC-E/spce.itp"` immediately afterward.

[ESTABLISHED] No SPC/E parameter, MDP setting, coordinate, or simulation-result file was modified to work around the fault.

## Next action required

[OPEN] Diagnose or repair the installed GROMACS preprocessing environment, then rerun the unmodified project `gmx grompp` command before attempting energy minimization.
