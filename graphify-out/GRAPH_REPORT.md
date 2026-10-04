# Graph Report - Thermal-Polarization  (2026-10-05)

## Corpus Check
- Corpus is ~43,514 words - fits in a single context window. You may not need a graph.

## Summary
- 273 nodes · 276 edges · 42 communities (22 shown, 20 thin omitted)
- Extraction: 95% EXTRACTED · 5% INFERRED · 0% AMBIGUOUS · INFERRED: 15 edges (avg confidence: 0.95)
- Token cost: unavailable for this refresh; no savings measured

## Community Hubs (Navigation)
- Python analysis symbols
- Python standard libraries
- Checkpoint 11 raw provenance
- DECISION-009 momentum scope
- SIM-02 Research Record
- SIM-02 method decisions
- Same-restart rank test
- NEMD production proposal
- Project guidance and Graphify
- Checkpoint 08 MPI momentum
- Checkpoint 08 COM failure
- Colab compute tradeoffs
- Checkpoint 10 rank comparison
- Thermal Polarization project README
- Research workflow and claim classes
- Checkpoint 08 approval
- Historical NEMD design
- Checkpoint 08 bridge protocol
- Checkpoint 09 momentum control
- Checkpoint 09 measured outcomes
- Research evidence
- Marimo analysis notebooks
- Checkpoint 08 failure evidence
- Checkpoint 10 replay comparison
- Wirnsberger replication source
- Evidence-first project lifecycle
- SPC/E water model
- Checkpoint 08 zero-step audit
- DECISION-014 Bridge Go/No-Go
- SIM-02 decision boundary
- Checkpoint 11 same-restart result
- Colab hardware and runtime
- Checkpoint 12 diagnostic
- YouTube Research Story
- Checkpoint 10 one-rank record
- Checkpoint 10 run limitation
- SIM-01 history and validation
- LAMMPS method translation
- Rank-count and COM diagnostics
- Notebook environment
- Checkpoint 07 baseline

## God Nodes (most connected - your core abstractions)
1. `SIM-01 validation report: five criteria reported passing; not independently rerun in this extraction` - 13 edges
2. `Research question: reproducible spatial polarization under a controlled thermal gradient` - 12 edges
3. `DECISION-014 integrated SIM-02 final-results campaign` - 8 edges
4. `SIM-02 two-region thermostat NEMD draft design` - 7 edges
5. `Supplied SIM-02 Claude prompt: reference proposal and workflow, not present authorization` - 7 edges
6. `SETTLE rigid water geometry: OH=0.1000 nm, HH=0.16330 nm` - 7 edges
7. `Pinned Python analysis and notebook environment` - 7 edges
8. `read_xvg()` - 5 edges
9. `main()` - 5 edges
10. `SIM-02 checkpoint 13 one-rank high-cadence report` - 5 edges

## Surprising Connections (you probably didn't know these)
- `Notebook entry for proposed checkpoint-13 control` --references--> `DECISION-013 — One-rank high-cadence SIM-02 control`  [EXTRACTED]
  notebooks/sim02_research.py → research/decisions/DECISION-013-SIM-02-one-rank-high-cadence-control-proposal.md
- `Checkpoint 13 status in project handoff` --references--> `SIM-02 checkpoint 13 one-rank high-cadence report`  [EXTRACTED]
  PROJECT_STATE.md → results/reports/SIM-02-checkpoint-13-one-rank-high-cadence.md
- `SIM-02 run README` --references--> `SIM-02 checkpoint 13 one-rank high-cadence report`  [EXTRACTED]
  simulations/SIM-02/README.md → results/reports/SIM-02-checkpoint-13-one-rank-high-cadence.md
- `Pinned Graphify dependency: graphifyy 0.9.72` --conceptually_related_to--> `Graphify query/path/explain and AST update workflow`  [INFERRED]
  environment/requirements-graphify.txt → CLAUDE.md
- `SIM-01 topology: 510 SOL molecules` --references--> `SPC/E rigid water topology: qO=-0.8476 e, qH=+0.4238 e; oxygen LJ sigma=0.316557 nm, epsilon=0.650194 kJ/mol`  [EXTRACTED]
  simulations/SIM-01/topol.top → models/SPC-E/spce.itp

## Import Cycles
- None detected.

## Hyperedges (group relationships)
- **Checkpoint 12 high-cadence diagnostic setup** — research_decisions_decision_012_sim_02_four_rank_high_cadence_diagnostic, research_decisions_decision_012_sim_02_four_rank_high_cadence_diagnostic_stage_b_restart, research_decisions_decision_012_sim_02_four_rank_high_cadence_diagnostic_per_step_sampling [EXTRACTED 1.00]
- **Proposed joint NEMD stationarity and uncertainty assessment** — research_prompts_sim_02_claude_prompt_temperature_profile, research_prompts_sim_02_claude_prompt_density_profile, research_prompts_sim_02_claude_prompt_polarization_profile, research_prompts_sim_02_claude_prompt_orientation, research_prompts_sim_02_claude_prompt_heat_flux, research_prompts_sim_02_claude_prompt_block_uncertainty [EXTRACTED 1.00]
- **Checkpoint 12 COM threshold failure observation** — results_reports_sim_02_checkpoint_12_four_rank_high_cadence_first_crossing, results_reports_sim_02_checkpoint_10_one_rank_nve_com_speed_ceiling, results_reports_sim_02_checkpoint_12_four_rank_high_cadence_rank_sensitive_behavior [INFERRED 0.85]
- **Matched checkpoint 12 and 13 rank-count COM comparison** — research_book_checkpoint_13_comparison, research_decisions_decision_013_matched_rank_count_control, results_reports_sim_02_checkpoint_13_rank_sensitive_trace [INFERRED 0.95]
- **Matched checkpoint 12 and 13 rank-count COM comparison** — research_book_checkpoint_13_comparison, research_decisions_decision_013_matched_rank_count_control, results_reports_sim_02_checkpoint_13_rank_sensitive_trace [INFERRED 0.95]

## Communities (42 total, 20 thin omitted)

### Community 0 - "Python analysis symbols"
Cohesion: 0.10
Nodes (4): main(), read_xvg(), main(), required()

### Community 5 - "Python standard libraries"
Cohesion: 0.21
Nodes (7): audit(), main(), minimum_image(), nearest_oxygen_distance(), parse_args(), parse_data(), write_report()

### Community 24 - "Checkpoint 11 raw provenance"
Cohesion: 0.67
Nodes (3): Measured COM speeds: 1.02778929e-5 Å/fs at 1 ps and 1.25105105e-5 Å/fs at 2 ps, Checkpoint 08 stopped before NVT and NVE; no equilibrium, eHEX, or polarization result exists, SIM-02 gate 2 failed at 2 ps: Stage-A COM speed exceeded the frozen ceiling

### Community 1 - "SIM-02 Research Record"
Cohesion: 0.06
Nodes (28): Notebook entry for proposed checkpoint-13 control, Checkpoint 13 matched rank-count comparison, Bounded implementation pass, Matched rank-count high-cadence control, Checkpoint 13 final matched diagnostic chapter, SIM-02 equilibrium bridge, Dynamic spatial reservoir method, Checkpoint 13 status in project handoff (+20 more)

### Community 6 - "SIM-02 method decisions"
Cohesion: 0.17
Nodes (13): DECISION-007 approves the exact 400 K benchmark and staged release gates, Gate 1 measured 4500 neutral waters, reservoir occupancy, RATTLE and PPPM initialization with zero steps, SIM-02 release gates from zero-step audit through stationarity pilot, Published 400 K benchmark uses 4500 SPC/E waters and 4.243e10 W m-2 branch heat flux, Wirnsberger 2016 author-package reproduction notes, SIM-02 checkpoint 07 exact benchmark and staged pilot proposal, SIM-02 gate 1 structure and LAMMPS zero-step audit passed, DECISION-005 selects LAMMPS eHEX for SIM-02 (+5 more)

### Community 10 - "Same-restart rank test"
Cohesion: 0.33
Nodes (3): Center-of-Mass Speed Ceiling, Checkpoint 10 Independent Stage-B Replay, Rank-Count-Sensitive Numerical Behavior

### Community 11 - "NEMD production proposal"
Cohesion: 0.40
Nodes (5): Intended NEMD observables: T(z), rho(z), Pz(z), SIM-02 configured NEMD production: provisional 1.5 ns, 2 fs timestep, 0.5 ps trajectory cadence, SIM-02 configured NEMD startup: provisional 500 ps, 2 fs timestep, no pressure coupling, DECISION-003 reference in NEMD startup comments, make_spatial_groups.md reference for spatial thermostat groups

### Community 12 - "Project guidance and Graphify"
Cohesion: 0.50
Nodes (3): Project guidance: SIM-02, graphify, token-reduction, Graphify bounded retrieval guidance, Pinned Graphify dependency: graphifyy 0.9.72

### Community 13 - "Checkpoint 08 MPI momentum"
Cohesion: 0.40
Nodes (4): MPI RATTLE COM-Velocity Floor, Corrected MPI Dry-Run Output, Checkpoint 08 MPI Momentum Initialization Record, Initial MPI Momentum Run Output

### Community 14 - "Checkpoint 08 COM failure"
Cohesion: 0.50
Nodes (4): Checkpoint 08 Frozen COM Criterion Failure, Checkpoint 08 Stage-A LAMMPS Log, Checkpoint 08 Stage-A COM-Drift Record, Checkpoint 08 Stage-A Standard Output

### Community 15 - "Colab compute tradeoffs"
Cohesion: 0.50
Nodes (3): Imported 4,500-Molecule SPC/E Structure, LAMMPS Checkpoint 07 run 0, Checkpoint 07 Structural Audit Pass

### Community 16 - "Checkpoint 10 rank comparison"
Cohesion: 0.50
Nodes (3): Fixed checkpoint-09 Stage-B restart, Rank-count-sensitive Stage-C/NVE sequence, SIM-02 checkpoint 11 — same-restart one-rank diagnostic

### Community 18 - "Research workflow and claim classes"
Cohesion: 0.67
Nodes (3): Fixed-Volume 400 K PPPM Equilibrium Bridge, Unreported NpT Pressure Boundary, DECISION-008 Equilibrium Bridge Approval

### Community 19 - "Checkpoint 08 approval"
Cohesion: 0.67
Nodes (3): Four-Stage Fixed-Volume Bridge Protocol, Frozen Gate 2 Acceptance Criteria, Checkpoint 08 Equilibrium Bridge Design

### Community 2 - "Historical NEMD design"
Cohesion: 0.08
Nodes (13): SIM-02 two-region thermostat NEMD draft design, H4 coupled mechanism (hypothesis), H1 density coupling (hypothesis), H3 molecular dynamics/heat-flux coupling (hypothesis), H2 local structure/hydrogen-bond coupling (hypothesis), Research question: reproducible spatial polarization under a controlled thermal gradient, DECISION-003 SIM-02 NEMD design, historical approval claim; date placeholder, Supplied SIM-02 Claude prompt: reference proposal and workflow, not present authorization (+5 more)

### Community 20 - "Checkpoint 08 bridge protocol"
Cohesion: 1.00
Nodes (3): Preparation-Only Momentum Removal, Uncorrected NVE COM-Ceiling Failure, Checkpoint 09 Preparation Momentum-Control Design

### Community 22 - "Checkpoint 09 measured outcomes"
Cohesion: 0.67
Nodes (3): Bounded implementation diagnostic, not equilibrium or polarization, Byte-identical four-rank checkpoint-09 Stage-B restart, Checkpoint 11 raw diagnostic archive

### Community 3 - "SPC/E water model"
Cohesion: 0.10
Nodes (20): PME, Verlet, 1.0 nm cutoffs, xyz PBC, EnerPres dispersion correction, h-bonds/LINCS, SIM-01 intended density, O-O RDF, self-diffusion validation targets, PME, Verlet, 1.0 nm cutoffs, xyz PBC, EnerPres dispersion correction, h-bonds/LINCS, PME, Verlet, 1.0 nm cutoffs, xyz PBC, EnerPres dispersion correction, h-bonds/LINCS, PME, Verlet, 1.0 nm cutoffs, xyz PBC, EnerPres dispersion correction, h-bonds/LINCS, PME, Verlet, 1.0 nm cutoffs, xyz PBC, EnerPres dispersion correction, h-bonds/LINCS, PME, Verlet, 1.0 nm cutoffs, xyz PBC, EnerPres dispersion correction, h-bonds/LINCS, Unresolved SIM-02 molecule count from gmx solvate (+12 more)

### Community 4 - "SIM-01 history and validation"
Cohesion: 0.10
Nodes (20): 2026-09-18 grompp produced no em.tpr even after package reinstall, SIM-01 report actual commands section empty, Reported density: 998.55 ± 11.22 kg/m³, sample standard deviation, 1001 samples, Reported corrected self-diffusion: 2.522e-9 ± 5.941e-13 m²/s, fit error only, single 1 ns run, Reported EM, 100 ps NVT, 100 ps NPT, 1 ns NPT, 1 ns supplementary NVT, GROMACS 2025.4-Ubuntu_2025.4_1 on WSL2/Ubuntu (reported), SIM-01 limitations: no independent diffusion replication, instantaneous fixed volume, provisional RDF references, Later SIM-01 report attributes resolved grompp failure to __N_SOL_TBD__ molecule-count placeholder (+12 more)

### Community 7 - "Rank-count and COM diagnostics"
Cohesion: 0.20
Nodes (10): Per-timestep COM and temperature sampling with soft halt, Byte-identical checkpoint-11 Stage-B restart, Frozen center-of-mass speed ceiling (1e-6 Å/fs), Four-rank NVE result: first ceiling exceedance at 100 fs, One-rank uncorrected NVE result: 2 ps, no ceiling exceedance, First COM ceiling crossing at 7 fs, DECISION-012: Four-rank high-cadence SIM-02 NVE diagnostic, Checkpoint 12 raw archive README (+2 more)

### Community 8 - "Notebook environment"
Cohesion: 0.25
Nodes (8): Jupyter 1.1.1, marimo 0.24.2 (duplicate requirement), Matplotlib 3.11.2, MDAnalysis 2.10.0, NumPy 2.5.3, pandas 3.0.6, SciPy 1.18.1, Pinned Python analysis and notebook environment

### Community 9 - "Checkpoint 07 baseline"
Cohesion: 0.25
Nodes (8): Ewald 1e-5 long-range solver, Gate 1 zero-step audit, Hot and cold reservoirs, PPPM 1e-5 long-range solver, Rigid SPC/E model, Author-supplied steady-state Ewald configuration, SIM-02 checkpoint 07, data.spce-4500.ness-ewald

## Knowledge Gaps
- **106 isolated node(s):** `Measured COM speeds: 1.02778929e-5 Å/fs at 1 ps and 1.25105105e-5 Å/fs at 2 ps`, `Checkpoint 08 stopped before NVT and NVE; no equilibrium, eHEX, or polarization result exists`, `DECISION-009 approved momentum removal only during Stage-A/B preparation; no periodic correction in NVE`, `Wirnsberger 2016 author-package reproduction notes`, `Checkpoint 13 final matched diagnostic chapter` (+101 more)
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 153 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **20 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **What connects `Measured COM speeds: 1.02778929e-5 Å/fs at 1 ps and 1.25105105e-5 Å/fs at 2 ps`, `Checkpoint 08 stopped before NVT and NVE; no equilibrium, eHEX, or polarization result exists`, `DECISION-009 approved momentum removal only during Stage-A/B preparation; no periodic correction in NVE` to the rest of the system?**
  _106 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `Python analysis symbols` be split into smaller, more focused modules?**
  _Cohesion score 0.10344827586206896 - nodes in this community are weakly interconnected._
- **Should `SIM-02 Research Record` be split into smaller, more focused modules?**
  _Cohesion score 0.06417112299465241 - nodes in this community are weakly interconnected._
- **Should `Historical NEMD design` be split into smaller, more focused modules?**
  _Cohesion score 0.08 - nodes in this community are weakly interconnected._
- **Should `SPC/E water model` be split into smaller, more focused modules?**
  _Cohesion score 0.10276679841897234 - nodes in this community are weakly interconnected._
- **Should `SIM-01 history and validation` be split into smaller, more focused modules?**
  _Cohesion score 0.09523809523809523 - nodes in this community are weakly interconnected._