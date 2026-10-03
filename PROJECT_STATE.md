# Project handoff

Tags: `SIM-02` · `graphify` · `token-reduction`
Inspected: 2026-09-30. This is a navigation summary, not simulation evidence.

## Current task
Resume SIM-02 from Claude's drafts. Graphify and the token-efficient project
guidance are established. The method audit found that the drafted static
`Hot/Cold/Rest` GROMACS groups do not implement spatial reservoirs for diffusing
water. On 2026-09-30 the user approved LAMMPS eHEX. The exact published 400 K
benchmark and staged gates were approved in DECISION-007. Gate 1 passed.
Checkpoint 08 was stopped at 2 ps after its COM criterion failed. The user then
approved DECISION-009: preparation-only momentum control with zero-step, 2 ps,
20 ps, NVT-transition, and uncorrected-NVE checks. The first two checks passed;
the 20 ps Stage-A diagnostic is in progress.

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
| Gate 2 protocol | `research/designs/SIM-02-checkpoint-08-equilibrium-bridge.md` | Fixed-volume bridge approved in DECISION-008; first integrated attempt failed the COM criterion |
| Gate 2 failure | `results/reports/SIM-02-checkpoint-08-stage-a-com-drift.md` | Step 1000: 1.0278e-5 Å/fs; step 2000: 1.2511e-5 Å/fs versus 1e-6 ceiling; stopped |
| Checkpoint 09 decision | `research/decisions/DECISION-009-SIM-02-preparation-momentum-control.md` | User approved preparation-only momentum control and bounded diagnostics |
| Checkpoint 09 diagnostics | `results/raw/SIM-02/checkpoint-09-diagnostics/` | Four-rank zero-step passed; 2 ps Stage-A passed at 400 K with COM removed every 100 steps; 20 ps Stage-A is running |
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
- [MEASURED] The first four-rank launch stopped before step 1 after establishing
  the MPI RATTLE COM-velocity floor. Stage-boundary momentum removal and the
  `1e-6 Å/fs` no-growth criterion were approved on 2026-10-03 before relaunch.
- [FAILED] The corrected four-rank OPT bridge launched at 20:22:39 +03:30 on
  2026-10-03 from commit `a1da7bb`. Initialization passed at `4.3903e-7 Å/fs`,
  but COM speed reached `1.02778929e-5 Å/fs` at step 1000 and
  `1.25105105e-5 Å/fs` at step 2000. Both exceed the `1e-6 Å/fs` ceiling, and
  the increase violates the no-growth condition. The run was stopped during
  Stage A; no LAMMPS warning or error occurred.
- [APPROVED / IN PROGRESS] DECISION-009 applies `fix momentum 100 linear 1 1 1
  rescale` in Stage A and B only, places RATTLE after velocity-changing fixes,
  and removes the momentum fix before NVE. Four-rank zero-step initialization
  passed. A 2 ps Stage-A diagnostic completed at exactly 400 K with all sampled
  COM speeds many orders below `1e-6 Å/fs`; the 20 ps Stage-A check is running.
- [NEXT] Complete 20 ps Stage A, then the short Stage-B transition and uncorrected
  NVE diagnostic. A full bridge relaunch depends on those checks passing.
- [TO TEST] LAMMPS equilibrium bridge, eHEX energy conservation, regional
  membership, heat accounting, and stationary profile/block uncertainty checks.
- Historical SIM-01 report has an empty command section and inconsistent temperature
  summaries; consult raw evidence if that discrepancy affects a decision.

Next scientific step: complete the checkpoint-09 20 ps Stage-A check, then the
short NVT-transition and NVE-without-periodic-momentum diagnostics. A full bridge
relaunch depends on those checks passing. The source paper omits its NpT target
pressure, so the bridge keeps the exact published box rather than inventing
that parameter. No equilibrium, temperature-gradient, or polarization result
is claimed here.

## Navigation
Use `scripts/graphify.ps1 query "SIM-02" --budget 1500` once the graph is built.
Graph is a retrieval index; source files remain authoritative. Avoid reading the
full graph JSON, bundled web assets, or trajectories into chat.
