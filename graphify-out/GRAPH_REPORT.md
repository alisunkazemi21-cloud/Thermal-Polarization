# Graph Report - Thermal-Polarization  (2026-10-05)

## Corpus Check
- cluster-only mode — file stats not available

## Summary
- 284 nodes · 297 edges · 47 communities (23 shown, 24 thin omitted)
- Extraction: 95% EXTRACTED · 5% INFERRED · 0% AMBIGUOUS · INFERRED: 15 edges (avg confidence: 0.95)
- Token cost: 0 input · 0 output

## Community Hubs (Navigation)
- Research question: reproducible spatial polarization under a controlled thermal gradient
- analyze_density_temperature.py
- SETTLE rigid water geometry: OH=0.1000 nm, HH=0.16330 nm
- SIM-01 validation report: five criteria reported passing; not independently rerun in this extraction
- audit_sim02_lammps_data.py
- SIM-02 checkpoint 13 one-rank high-cadence report
- SIM-02 method decisions
- Rank-count and COM diagnostics
- DECISION-014 integrated SIM-02 final-results campaign
- analyze_sim02_restart_continuity.py
- Pinned Python analysis and notebook environment
- SIM-02 checkpoint 07
- Stage-C Uncorrected NVE Protocol
- SPC/E rigid water topology: qO=-0.8476 e, qH=+0.4238 e; oxygen LJ sigma=0.316557 nm, epsilon=0.650194 kJ/mol
- Token reduction project skill and evidence-first navigation
- MPI RATTLE COM-Velocity Floor
- Checkpoint 08 Frozen COM Criterion Failure
- Imported 4,500-Molecule SPC/E Structure
- Fixed checkpoint-09 Stage-B restart
- Thermal Polarization project README
- DECISION-008 Equilibrium Bridge Approval
- Checkpoint 08 Equilibrium Bridge Design
- Checkpoint 09 Preparation Momentum-Control Design
- Long-form YouTube story — SIM-02
- Uncorrected NVE COM-Speed Ceiling Failure
- Checkpoint 11 raw diagnostic archive
- Mechanism of COM growth remains unresolved
- SIM-02 gate 2 failed at 2 ps: Stage-A COM speed exceeded the frozen ceiling
- Research Book
- Checkpoint 10 one-rank comparison from replayed Stage B
- Wirnsberger 2016 Reproduction Notes
- Academic claim classes separate established measured inferred hypothesis and open
- Checkpoint 08 Zero-Step Input Validation
- SIM-02 technical report
- Gate 1 1.0 fs timestep
- DECISION-014 status in project handoff
- DECISION-014 bridge go/no-go
- Full bridge remains on hold
- Same-restart rank comparison follow-up
- DECISION-011 Same-Restart One-Rank SIM-02 Diagnostic
- Checkpoint 12 four-rank high-cadence diagnostic
- YouTube research-series roadmap
- Checkpoint 10 One-Rank NVE Diagnostic
- Checkpoint 10 execution-record limitation
- DECISION-009 approved momentum removal only during Stage-A/B preparation; no periodic correction in NVE
- Ewald-to-PPPM LAMMPS Translation

## God Nodes (most connected - your core abstractions)
1. `SIM-01 validation report: five criteria reported passing; not independently rerun in this extraction` - 13 edges
2. `Research question: reproducible spatial polarization under a controlled thermal gradient` - 12 edges
3. `DECISION-014 integrated SIM-02 final-results campaign` - 8 edges
4. `SIM-02 two-region thermostat NEMD draft design` - 7 edges
5. `Supplied SIM-02 Claude prompt: reference proposal and workflow, not present authorization` - 7 edges
6. `Pinned Python analysis and notebook environment` - 7 edges
7. `SETTLE rigid water geometry: OH=0.1000 nm, HH=0.16330 nm` - 7 edges
8. `read_xvg()` - 5 edges
9. `main()` - 5 edges
10. `main()` - 5 edges

## Surprising Connections (you probably didn't know these)
- `Notebook entry for proposed checkpoint-13 control` --references--> `DECISION-013 — One-rank high-cadence SIM-02 control`  [EXTRACTED]
  notebooks/sim02_research.py → research/decisions/DECISION-013-SIM-02-one-rank-high-cadence-control-proposal.md
- `SIM-01 topology: 510 SOL molecules` --references--> `SPC/E rigid water topology: qO=-0.8476 e, qH=+0.4238 e; oxygen LJ sigma=0.316557 nm, epsilon=0.650194 kJ/mol`  [EXTRACTED]
  simulations/SIM-01/topol.top → models/SPC-E/spce.itp
- `SIM-02 draft topology: SOL molecule count remains __N_SOL_TBD__` --references--> `SPC/E rigid water topology: qO=-0.8476 e, qH=+0.4238 e; oxygen LJ sigma=0.316557 nm, epsilon=0.650194 kJ/mol`  [EXTRACTED]
  simulations/SIM-02/topol.top → models/SPC-E/spce.itp
- `Pinned Graphify dependency: graphifyy 0.9.72` --conceptually_related_to--> `Graphify query/path/explain and AST update workflow`  [INFERRED]
  environment/requirements-graphify.txt → CLAUDE.md
- `SIM-01 configured steepest-descent minimization: max 50000 steps, emtol=1000 kJ/mol/nm` --conceptually_related_to--> `SETTLE rigid water geometry: OH=0.1000 nm, HH=0.16330 nm`  [INFERRED]
  simulations/SIM-01/em.mdp → models/SPC-E/spce.itp

## Import Cycles
- None detected.

## Hyperedges (group relationships)
- **Checkpoint 12 high-cadence diagnostic setup** — research_decisions_decision_012_sim_02_four_rank_high_cadence_diagnostic, research_decisions_decision_012_sim_02_four_rank_high_cadence_diagnostic_stage_b_restart, research_decisions_decision_012_sim_02_four_rank_high_cadence_diagnostic_per_step_sampling [EXTRACTED 1.00]
- **Proposed joint NEMD stationarity and uncertainty assessment** — research_prompts_sim_02_claude_prompt_temperature_profile, research_prompts_sim_02_claude_prompt_density_profile, research_prompts_sim_02_claude_prompt_polarization_profile, research_prompts_sim_02_claude_prompt_orientation, research_prompts_sim_02_claude_prompt_heat_flux, research_prompts_sim_02_claude_prompt_block_uncertainty [EXTRACTED 1.00]
- **Checkpoint 12 COM threshold failure observation** — results_reports_sim_02_checkpoint_12_four_rank_high_cadence_first_crossing, results_reports_sim_02_checkpoint_10_one_rank_nve_com_speed_ceiling, results_reports_sim_02_checkpoint_12_four_rank_high_cadence_rank_sensitive_behavior [INFERRED 0.85]
- **Matched checkpoint 12 and 13 rank-count COM comparison** — research_book_checkpoint_13_comparison, research_decisions_decision_013_matched_rank_count_control, results_reports_sim_02_checkpoint_13_rank_sensitive_trace [INFERRED 0.95]
- **Matched checkpoint 12 and 13 rank-count COM comparison** — research_book_checkpoint_13_comparison, research_decisions_decision_013_matched_rank_count_control, results_reports_sim_02_checkpoint_13_rank_sensitive_trace [INFERRED 0.95]

## Communities (47 total, 24 thin omitted)

### Community 0 - "Research question: reproducible spatial polarization under a controlled thermal gradient"
Cohesion: 0.08
Nodes (13): DECISION-003 SIM-02 NEMD design, historical approval claim; date placeholder, SIM-02 two-region thermostat NEMD draft design, Armstrong et al. 2013: Heat Flux and Dipole Moment Dynamic Correlations (unverified literature lead), Armstrong and Bresme 2015: Temperature Inversion of Thermal Polarization of Water (unverified literature lead), Bedeaux et al. 2025: Theory of Thermopolarization Effect (unverified literature lead), Bresme et al. 2008: Water Polarization under Thermal Gradients (unverified literature lead), H4 coupled mechanism (hypothesis), H1 density coupling (hypothesis) (+5 more)

### Community 2 - "SETTLE rigid water geometry: OH=0.1000 nm, HH=0.16330 nm"
Cohesion: 0.11
Nodes (20): SIM-01 configured steepest-descent minimization: max 50000 steps, emtol=1000 kJ/mol/nm, PME, Verlet, 1.0 nm cutoffs, xyz PBC, EnerPres dispersion correction, h-bonds/LINCS, SIM-01 configured NPT production: 1 ns, 300 K, 1 bar, 2 fs timestep, 1 ps trajectory cadence, SIM-01 supplementary NVT diffusion configuration: 1 ns, 300 K, fixed volume, 1 ps trajectory cadence, SIM-01 intended density, O-O RDF, self-diffusion validation targets, SIM-01 configured NPT equilibration: provisional 100 ps, 300 K, 1 bar, PME, Verlet, 1.0 nm cutoffs, xyz PBC, EnerPres dispersion correction, h-bonds/LINCS, SIM-01 configured NVT equilibration: provisional 100 ps, 300 K, V-rescale tau=0.1 ps (+12 more)

### Community 3 - "SIM-01 validation report: five criteria reported passing; not independently rerun in this extraction"
Cohesion: 0.10
Nodes (20): FAILED-001 historical preprocessing segfault; unresolved in this dated record, 2026-09-18 grompp produced no em.tpr even after package reinstall, DECISION-001 supplementary fixed-volume NVT diffusion leg (historical approval; date placeholder), DECISION-002: diffusion periodic-boundary correction (2026-09-19 record), RDF literature lead arXiv:1706.05491, RDF literature lead arXiv:1806.09956, RDF literature lead arXiv:1809.04996, Berendsen, Grigera, Straatsma (1987), The missing term in effective pair potentials (+12 more)

### Community 4 - "audit_sim02_lammps_data.py"
Cohesion: 0.14
Nodes (9): audit(), main(), minimum_image(), nearest_oxygen_distance(), parse_args(), parse_data(), write_report(), main() (+1 more)

### Community 5 - "SIM-02 checkpoint 13 one-rank high-cadence report"
Cohesion: 0.13
Nodes (11): Notebook entry for proposed checkpoint-13 control, Checkpoint 13 status in project handoff, Checkpoint 13 matched rank-count comparison, SIM-02 research book, Bounded implementation pass, Matched rank-count high-cadence control, DECISION-013 — One-rank high-cadence SIM-02 control, Checkpoint 13 raw evidence README (+3 more)

### Community 6 - "SIM-02 method decisions"
Cohesion: 0.17
Nodes (13): DECISION-005 selects LAMMPS eHEX for SIM-02, Local LAMMPS build provides eHEX rigid SHAKE RATTLE and PPPM, DECISION-006 approves 400 K validation before 300 K target, DECISION-007 approves the exact 400 K benchmark and staged release gates, Wirnsberger 2016 author-package reproduction notes, SIM-02 checkpoint 07 exact benchmark and staged pilot proposal, SIM-02 LAMMPS eHEX design discussion, Gate 1 measured 4500 neutral waters, reservoir occupancy, RATTLE and PPPM initialization with zero steps (+5 more)

### Community 7 - "Rank-count and COM diagnostics"
Cohesion: 0.20
Nodes (10): DECISION-012: Four-rank high-cadence SIM-02 NVE diagnostic, Per-timestep COM and temperature sampling with soft halt, Byte-identical checkpoint-11 Stage-B restart, Checkpoint 12 raw archive README, Frozen center-of-mass speed ceiling (1e-6 Å/fs), Four-rank NVE result: first ceiling exceedance at 100 fs, One-rank uncorrected NVE result: 2 ps, no ceiling exceedance, SIM-02 checkpoint 10 — one-rank NVE diagnostic (+2 more)

### Community 8 - "DECISION-014 integrated SIM-02 final-results campaign"
Cohesion: 0.26
Nodes (12): 100 ps eHEX smoke test at 1 fs, 1 ns stationarity pilot and profile checks, Derive and record the 300 K run length and replicate plan from pilot evidence, Conditional 300 K target after method validation, Final signed polarization profile Pz(z) with block uncertainty, Frozen 400 K equilibrium bridge under DECISION-008 criteria, Independent seed replicate required before a positive reproducibility claim, DECISION-014 integrated SIM-02 final-results campaign (+4 more)

### Community 9 - "analyze_sim02_restart_continuity.py"
Cohesion: 0.29
Nodes (6): by_step(), main(), mean_slope_and_change(), path_summary(), sha256(), thermo_rows()

### Community 10 - "Pinned Python analysis and notebook environment"
Cohesion: 0.25
Nodes (8): Pinned Python analysis and notebook environment, Jupyter 1.1.1, marimo 0.24.2 (duplicate requirement), Matplotlib 3.11.2, MDAnalysis 2.10.0, NumPy 2.5.3, pandas 3.0.6, SciPy 1.18.1

### Community 11 - "SIM-02 checkpoint 07"
Cohesion: 0.25
Nodes (8): SIM-02 checkpoint 07, data.spce-4500.ness-ewald, Ewald 1e-5 long-range solver, Gate 1 zero-step audit, Hot and cold reservoirs, PPPM 1e-5 long-range solver, Rigid SPC/E model, Author-supplied steady-state Ewald configuration

### Community 12 - "Stage-C Uncorrected NVE Protocol"
Cohesion: 0.33
Nodes (3): Center-of-Mass Speed Ceiling, Checkpoint 10 Independent Stage-B Replay, Rank-Count-Sensitive Numerical Behavior

### Community 13 - "SPC/E rigid water topology: qO=-0.8476 e, qH=+0.4238 e; oxygen LJ sigma=0.316557 nm, epsilon=0.650194 kJ/mol"
Cohesion: 0.33
Nodes (5): Berendsen, Grigera, Straatsma (1987), The missing term in effective pair potentials, J. Phys. Chem. 91, 6269-6271, SPC/E rigid water topology: qO=-0.8476 e, qH=+0.4238 e; oxygen LJ sigma=0.316557 nm, epsilon=0.650194 kJ/mol, SIM-01 topology: 510 SOL molecules, Unresolved SIM-02 molecule count from gmx solvate, SIM-02 draft topology: SOL molecule count remains __N_SOL_TBD__

### Community 14 - "Token reduction project skill and evidence-first navigation"
Cohesion: 0.50
Nodes (3): Project guidance: SIM-02, graphify, token-reduction, Graphify bounded retrieval guidance, Pinned Graphify dependency: graphifyy 0.9.72

### Community 15 - "MPI RATTLE COM-Velocity Floor"
Cohesion: 0.40
Nodes (4): Corrected MPI Dry-Run Output, MPI RATTLE COM-Velocity Floor, Checkpoint 08 MPI Momentum Initialization Record, Initial MPI Momentum Run Output

### Community 16 - "Checkpoint 08 Frozen COM Criterion Failure"
Cohesion: 0.50
Nodes (4): Checkpoint 08 Frozen COM Criterion Failure, Checkpoint 08 Stage-A LAMMPS Log, Checkpoint 08 Stage-A COM-Drift Record, Checkpoint 08 Stage-A Standard Output

### Community 17 - "Imported 4,500-Molecule SPC/E Structure"
Cohesion: 0.50
Nodes (3): LAMMPS Checkpoint 07 run 0, Imported 4,500-Molecule SPC/E Structure, Checkpoint 07 Structural Audit Pass

### Community 18 - "Fixed checkpoint-09 Stage-B restart"
Cohesion: 0.50
Nodes (3): Fixed checkpoint-09 Stage-B restart, Rank-count-sensitive Stage-C/NVE sequence, SIM-02 checkpoint 11 — same-restart one-rank diagnostic

### Community 20 - "DECISION-008 Equilibrium Bridge Approval"
Cohesion: 0.67
Nodes (3): DECISION-008 Equilibrium Bridge Approval, Fixed-Volume 400 K PPPM Equilibrium Bridge, Unreported NpT Pressure Boundary

### Community 21 - "Checkpoint 08 Equilibrium Bridge Design"
Cohesion: 0.67
Nodes (3): Checkpoint 08 Equilibrium Bridge Design, Four-Stage Fixed-Volume Bridge Protocol, Frozen Gate 2 Acceptance Criteria

### Community 22 - "Checkpoint 09 Preparation Momentum-Control Design"
Cohesion: 1.00
Nodes (3): Checkpoint 09 Preparation Momentum-Control Design, Preparation-Only Momentum Removal, Uncorrected NVE COM-Ceiling Failure

### Community 25 - "Checkpoint 11 raw diagnostic archive"
Cohesion: 0.67
Nodes (3): Bounded implementation diagnostic, not equilibrium or polarization, Checkpoint 11 raw diagnostic archive, Byte-identical four-rank checkpoint-09 Stage-B restart

### Community 27 - "SIM-02 gate 2 failed at 2 ps: Stage-A COM speed exceeded the frozen ceiling"
Cohesion: 0.67
Nodes (3): Measured COM speeds: 1.02778929e-5 Å/fs at 1 ps and 1.25105105e-5 Å/fs at 2 ps, Checkpoint 08 stopped before NVT and NVE; no equilibrium, eHEX, or polarization result exists, SIM-02 gate 2 failed at 2 ps: Stage-A COM speed exceeded the frozen ceiling

## Knowledge Gaps
- **106 isolated node(s):** `Measured COM speeds: 1.02778929e-5 Å/fs at 1 ps and 1.25105105e-5 Å/fs at 2 ps`, `Checkpoint 08 stopped before NVT and NVE; no equilibrium, eHEX, or polarization result exists`, `DECISION-009 approved momentum removal only during Stage-A/B preparation; no periodic correction in NVE`, `Wirnsberger 2016 author-package reproduction notes`, `H4 coupled mechanism (hypothesis)` (+101 more)
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 154 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **24 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `SETTLE rigid water geometry: OH=0.1000 nm, HH=0.16330 nm` connect `SETTLE rigid water geometry: OH=0.1000 nm, HH=0.16330 nm` to `SPC/E rigid water topology: qO=-0.8476 e, qH=+0.4238 e; oxygen LJ sigma=0.316557 nm, epsilon=0.650194 kJ/mol`?**
  _High betweenness centrality (0.007) - this node is a cross-community bridge._
- **What connects `Measured COM speeds: 1.02778929e-5 Å/fs at 1 ps and 1.25105105e-5 Å/fs at 2 ps`, `Checkpoint 08 stopped before NVT and NVE; no equilibrium, eHEX, or polarization result exists`, `DECISION-009 approved momentum removal only during Stage-A/B preparation; no periodic correction in NVE` to the rest of the system?**
  _106 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `Research question: reproducible spatial polarization under a controlled thermal gradient` be split into smaller, more focused modules?**
  _Cohesion score 0.08 - nodes in this community are weakly interconnected._
- **Should `analyze_density_temperature.py` be split into smaller, more focused modules?**
  _Cohesion score 0.13438735177865613 - nodes in this community are weakly interconnected._
- **Should `SETTLE rigid water geometry: OH=0.1000 nm, HH=0.16330 nm` be split into smaller, more focused modules?**
  _Cohesion score 0.1067193675889328 - nodes in this community are weakly interconnected._
- **Should `SIM-01 validation report: five criteria reported passing; not independently rerun in this extraction` be split into smaller, more focused modules?**
  _Cohesion score 0.09523809523809523 - nodes in this community are weakly interconnected._
- **Should `audit_sim02_lammps_data.py` be split into smaller, more focused modules?**
  _Cohesion score 0.14285714285714285 - nodes in this community are weakly interconnected._