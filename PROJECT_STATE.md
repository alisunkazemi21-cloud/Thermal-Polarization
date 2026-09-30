# Project handoff

Tags: `SIM-02` · `graphify` · `token-reduction`
Inspected: 2026-09-30. This is a navigation summary, not simulation evidence.

## Current task
Resume SIM-02 from Claude's drafts. Graphify and the token-efficient project
guidance are established. The method audit found that the drafted static
`Hot/Cold/Rest` GROMACS groups do not implement spatial reservoirs for diffusing
water. On 2026-09-30 the user approved LAMMPS eHEX. The exact published 400 K
benchmark and staged gates were approved in DECISION-007. Gate 1, the build and
zero-step audit, passed. Checkpoint 08 and its frozen equilibrium-bridge
acceptance criteria were approved in DECISION-008; execution is released.

## Evidence and routes
| Topic | Source | Observed status |
|---|---|---|
| SIM-01 validation | `results/reports/SIM-01-validation.md` | Report says five criteria pass; no simulations rerun in this inspection |
| Density and temperature | `results/tables/density_temperature_summary.csv` | 998.553 kg/m³; 300.113 K; 1001 samples over 1 ns; reported standard deviations are not errors of the mean |
| Model | `models/SPC-E/spce.itp` | Rigid SPC/E, SETTLE, O=-0.8476e, H=+0.4238e |
| Equilibrium inputs | `simulations/SIM-01/` | 510 molecules per report; initial 2.5 nm cube; 2 fs; PME; 1 nm cutoffs |
| Analysis | `scripts/analysis/` | Density/temperature, O-O RDF, diffusion; notebook at `notebooks/sim01_analysis.py` |
| Diffusion correction | `research/decisions/DECISION-002-msd-pbc-wrapping-correction.md` | No-jump trajectory required by existing diffusion analysis; fit error is not replication uncertainty |
| SIM-02 design | `research/decisions/DECISION-003-SIM-02-NEMD-design.md` | Historical record says approved; date still placeholder; full prior conversation unavailable |
| SIM-02 method audit | `research/decisions/DECISION-004-SIM-02-method-audit.md` | Stock-GROMACS `tc-grps` approach rejected |
| SIM-02 engine decision | `research/decisions/DECISION-005-SIM-02-LAMMPS-eHEX.md` | LAMMPS eHEX approved; local build has eHEX/RIGID/SHAKE/PPPM |
| SIM-02 temperature path | `research/decisions/DECISION-006-SIM-02-temperature-path.md` | 400 K validation followed by 300 K target approved |
| SIM-02 design | `research/designs/SIM-02-LAMMPS-eHEX-design.md` | Exact published box, reservoirs, and heat rate recovered; staged pilot awaits approval |
| Protocol checkpoint | `research/designs/SIM-02-checkpoint-07-protocol-freeze.md` | Exact 400 K implementation and release gates approved in DECISION-007 |
| Protocol decision | `research/decisions/DECISION-007-SIM-02-protocol-freeze.md` | Exact benchmark and staged gates approved; gate 1 passed |
| Gate 1 evidence | `results/reports/SIM-02-checkpoint-07-zero-step.md` | Structure audit and LAMMPS `run 0` passed; zero trajectory steps |
| Gate 2 protocol | `research/designs/SIM-02-checkpoint-08-equilibrium-bridge.md` | Fixed-volume bridge approved in DECISION-008; zero-step input parse passed; execution released |
| SIM-02 drafts | `simulations/SIM-02/` | GROMACS files retained as non-runnable historical drafts |
| Literature notes | `research/literature/Wirnsberger-2016-reproduction-notes.md` | Primary paper and author package audited; no project result imported |

## Historical SIM-02 draft (rejected method, not validated behavior)
The inherited GROMACS draft proposed 500 ps startup, 1500 ps production,
2 fs steps, and fixed Hot/Cold/Rest groups at 320/280/300 K. It saved no
velocities. These values remain part of the chronology but are not the current
LAMMPS design.

## Open items before a runnable experiment
- [DECIDED] Use LAMMPS eHEX; do not run the static GROMACS initial-slab groups.
- [DECIDED] Validate at 400 K, then run the 300 K target only after the pilot
  gates pass (DECISION-006).
- [DECIDED] Checkpoint 07 exact benchmark and staged plan approved
  (DECISION-007).
- [PASSED] Gate 1: imported-system structure, COM reservoir accounting, current
  eHEX syntax, RATTLE clusters, and PPPM initialization; `run 0` advanced no
  trajectory step.
- [APPROVED] Checkpoint 08: fixed-box 20 ps velocity-rescaling warm-up, 500 ps
  NVT, and 1 ns NVE at 400 K with deterministic seed `20260930`.
- [NEXT] Execute and analyze the equilibrium bridge before any eHEX trajectory.
- [TO TEST] LAMMPS equilibrium bridge, eHEX energy conservation, regional
  membership, heat accounting, and stationary profile/block uncertainty checks.
- Historical SIM-01 report has an empty command section and inconsistent temperature
  summaries; consult raw evidence if that discrepancy affects a decision.

Next scientific step: execute the frozen checkpoint-08 equilibrium input and
evaluate every acceptance criterion. The source paper omits its NpT target
pressure, so this bridge keeps the exact published box rather than inventing
that parameter. No temperature-gradient or polarization result is claimed here.

## Navigation
Use `scripts/graphify.ps1 query "SIM-02" --budget 1500` once the graph is built.
Graph is a retrieval index; source files remain authoritative. Avoid reading the
full graph JSON, bundled web assets, or trajectories into chat.
