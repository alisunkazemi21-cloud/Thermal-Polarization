# Project handoff

Tags: `SIM-02` · `graphify` · `token-reduction`
Inspected: 2026-10-04. This is a navigation summary, not simulation evidence.

## Current task
Resume SIM-02 from Claude's drafts. Graphify and the token-efficient project
guidance are established. The method audit found that the drafted static
`Hot/Cold/Rest` GROMACS groups do not implement spatial reservoirs for diffusing
water. On 2026-09-30 the user approved LAMMPS eHEX. The exact published 400 K
benchmark and staged gates were approved in DECISION-007. Gate 1 passed.
Checkpoint 08 was stopped at 2 ps after its COM criterion failed. The user then
approved DECISION-009: preparation-only momentum control with zero-step, 2 ps,
20 ps, NVT-transition, and uncorrected-NVE checks. Stage A passed at 2 ps and
20 ps; Stage B passed at 2 ps. The uncorrected NVE diagnostic failed the frozen
COM ceiling at 100 fs and stopped at 400 fs. Checkpoint 10's one-rank run passed
2 ps NVE from a separately replayed Stage-B state. In checkpoint 11, one-rank
Stage C/NVE from the exact four-rank Stage-B restart also passed 2 ps, while the
four-rank continuation from that restart breached at 100 fs. Checkpoint 12
replayed the four-rank path with per-step COM sampling and halted at the first
ceiling crossing, 7 fs into NVE. COM rose at every recorded step from
`6.03e-8` to `1.12e-6 Å/fs`. Rank-count-sensitive behavior is confirmed for
this saved-state sequence, but its cause remains unresolved. The full bridge
remains on hold.

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
| Checkpoint 09 results | `results/reports/SIM-02-checkpoint-09-diagnostics.md` | 20 ps Stage A passed (400 K; max COM `9.65e-19 Å/fs`); 2 ps Stage B ended at `399.81 K`; uncorrected NVE exceeded the COM ceiling at 100 fs |
| Checkpoint 10 results | `results/reports/SIM-02-checkpoint-10-one-rank-nve.md` | One-rank 2 ps uncorrected NVE: 20 samples, max COM `1.04e-18 Å/fs`; Stage B was replayed, so its comparison alone did not isolate the cause |
| Checkpoint 11 results | `results/reports/SIM-02-checkpoint-11-same-restart-one-rank.md` | From the same four-rank Stage-B restart, one-rank 2 ps Stage-C/NVE passed: max COM `1.264e-18 Å/fs`; four-rank path failed at 100 fs; rank-sensitive sequence, mechanism unresolved |
| Checkpoint 12 results | `results/reports/SIM-02-checkpoint-12-four-rank-high-cadence.md` | Four-rank replay from the same restart, per-step COM; first exceedance at 7 fs (`1.1198277e-6 Å/fs`); monotonic increase across eight samples; cause unresolved |
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
- [PASSED] DECISION-009 Stage A: 20 ps; 200 samples at 400 K; max sampled COM
  speed `9.654782345768524e-19 Å/fs`; 4-rank OPT, 1:39:34.
- [PASSED] DECISION-009 Stage B: 2 ps from the saved Stage-A restart; endpoint
  temperature `399.81022 K`; max sampled COM `8.507873362730173e-19 Å/fs`.
- [FAILED] Uncorrected NVE exceeded the frozen `1e-6 Å/fs` ceiling at 100 fs
  (`7.144552366951081e-6 Å/fs`). Four samples were captured through 400 fs;
  peak `8.357269209836094e-6 Å/fs`. This is an implementation diagnostic,
  not an equilibrium result.
- [MEASURED / OPEN] A Stage-C zero-step replay left COM at `4.8768857346949e-8
  Å/fs` after the final zero-linear command. The jump occurred during NVE
  integration; RATTLE/MPI is an unconfirmed mechanism hypothesis.
- [MEASURED] Checkpoint 10's one-rank comparison replayed Stage B from the
  Stage-A restart and completed 2 ps NVE; that pair used different Stage-B
  trajectories. Checkpoint 11 then started one-rank Stage C/NVE from the exact
  four-rank Stage-B restart. It completed 2 ps (exit 0); max COM was
  `1.2638e-18 Å/fs`. The four-rank path from this same restart breached at
  100 fs. This supports rank-count-sensitive behavior in Stage C/NVE, but the
  cause remains unresolved. See DECISION-011 and its report.
- [MEASURED FAILURE] Checkpoint 12 replayed the four-rank continuation from
  that exact restart with per-step output. COM speed rose at each of eight
  samples from `6.03e-8 Å/fs` after cleanup and crossed `1e-6 Å/fs` at 7 fs
  (`1.1198276995146967e-6 Å/fs` by the `fix halt` message). LAMMPS exited 0
  after the configured soft stop and wrote its diagnostic restart. A
  `+2.206 kcal/mol` total-energy-column change over those 7 fs is exploratory;
  no energy-drift criterion was frozen for this run. See DECISION-012.
- [TO TEST] LAMMPS equilibrium bridge, eHEX energy conservation, regional
  membership, heat accounting, and stationary profile/block uncertainty checks.
- Historical SIM-01 report has an empty command section and inconsistent temperature
  summaries; consult raw evidence if that discrepancy affects a decision.

Next scientific step: review the checkpoint-12 per-step trace and decide which
mechanism-focused diagnostic is justified. The full equilibrium bridge has
not been relaunched. The
source paper omits its NpT target pressure, so the bridge keeps the exact
published box rather than inventing that parameter. No equilibrium,
temperature-gradient, or polarization result is claimed here.

## Navigation
Use `scripts/graphify.ps1 query "SIM-02" --budget 1500` once the graph is built.
Graph is a retrieval index; source files remain authoritative. Avoid reading the
full graph JSON, bundled web assets, or trajectories into chat.
