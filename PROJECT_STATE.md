# Project handoff

Tags: `SIM-02` · `graphify` · `token-reduction`
Inspected: 2026-09-30. This is a navigation summary, not simulation evidence.

## Current task
Resume SIM-02 from Claude's drafts. Graphify and the token-efficient project
guidance are established. The method audit found that the drafted static
`Hot/Cold/Rest` GROMACS groups do not implement spatial reservoirs for diffusing
water. On 2026-09-30 the user approved LAMMPS eHEX; detailed design choices
remain open before implementation.

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
| SIM-02 design | `research/designs/SIM-02-LAMMPS-eHEX-design.md` | Temperature sequence approved; heat rate, exact box/count, and replication remain open |
| SIM-02 drafts | `simulations/SIM-02/` | GROMACS files retained as non-runnable historical drafts |
| Literature notes | `research/literature/README.md` | Empty; citations in supplied prompt are leads, not verified literature evidence |

## Historical SIM-02 draft (rejected method, not validated behavior)
The inherited GROMACS draft proposed 500 ps startup, 1500 ps production,
2 fs steps, and fixed Hot/Cold/Rest groups at 320/280/300 K. It saved no
velocities. These values remain part of the chronology but are not the current
LAMMPS design.

## Open items before a runnable experiment
- [DECIDED] Use LAMMPS eHEX; do not run the static GROMACS initial-slab groups.
- [DECIDED] Validate at 400 K, then run the 300 K target only after the pilot
  gates pass (DECISION-006).
- [OPEN] Approve the exact molecule count, box dimensions, reservoir widths,
  profile bin width, seeds, heat rate, run lengths, and replication plan.
- [TO IMPLEMENT] LAMMPS system construction, run workflow, analysis, and raw
  result directory. No SIM-02 run output currently exists.
- [TO TEST] LAMMPS equilibrium bridge, eHEX energy conservation, regional
  membership, heat accounting, and stationary profile/block uncertainty checks.
- Historical SIM-01 report has an empty command section and inconsistent temperature
  summaries; consult raw evidence if that discrepancy affects a decision.

Next scientific step: discuss and approve the design in
`research/designs/SIM-02-LAMMPS-eHEX-design.md`, then implement the equilibrium
bridge and eHEX pilot. No SIM-02 results are claimed here.

## Navigation
Use `scripts/graphify.ps1 query "SIM-02" --budget 1500` once the graph is built.
Graph is a retrieval index; source files remain authoritative. Avoid reading the
full graph JSON, bundled web assets, or trajectories into chat.
