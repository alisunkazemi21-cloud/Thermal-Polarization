# Graph Report - Thermal-Polarization  (2026-10-05)

## Corpus Check
- 33 files · ~42,955 words
- Verdict: corpus is large enough that graph structure adds value.

## Summary
- 265 nodes · 267 edges · 42 communities (22 shown, 20 thin omitted)
- Extraction: 94% EXTRACTED · 6% INFERRED · 0% AMBIGUOUS · INFERRED: 15 edges (avg confidence: 0.95)
- Token cost: unavailable for this refresh; no savings measured

## Community Hubs (Navigation)
- Python analysis symbols
- SIM-02 Research Record
- Historical NEMD design
- SPC/E water model
- SIM-01 history and validation
- Python standard libraries
- SIM-02 method decisions
- Rank-count and COM diagnostics
- Notebook environment
- Checkpoint 07 baseline
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
- Checkpoint 08 bridge protocol
- Checkpoint 09 momentum control
- Checkpoint 09 measured outcomes
- Research evidence
- Checkpoint 11 raw provenance
- Marimo analysis notebooks
- Checkpoint 08 failure evidence
- Checkpoint 10 replay comparison
- Wirnsberger replication source
- Evidence-first project lifecycle
- Checkpoint 08 zero-step audit
- DECISION-014 Bridge Go/No-Go
- SIM-02 decision boundary
- Checkpoint 11 same-restart result
- Colab hardware and runtime
- Checkpoint 12 diagnostic
- YouTube Research Story
- Checkpoint 10 one-rank record
- Checkpoint 10 run limitation
- DECISION-009 momentum scope
- LAMMPS method translation

## God Nodes (most connected - your core abstractions)
1. `SIM-01 validation report: five criteria reported passing; not independently rerun in this extraction` - 13 edges
2. `Research question: reproducible spatial polarization under a controlled thermal gradient` - 12 edges
3. `SETTLE rigid water geometry: OH=0.1000 nm, HH=0.16330 nm` - 7 edges
4. `SIM-02 two-region thermostat NEMD draft design` - 7 edges
5. `Supplied SIM-02 Claude prompt: reference proposal and workflow, not present authorization` - 7 edges
6. `Pinned Python analysis and notebook environment` - 7 edges
7. `DECISION-014 — Consolidated SIM-02 bridge go/no-go proposal` - 7 edges
8. `read_xvg()` - 5 edges
9. `main()` - 5 edges
10. `SPC/E rigid water topology: qO=-0.8476 e, qH=+0.4238 e; oxygen LJ sigma=0.316557 nm, epsilon=0.650194 kJ/mol` - 5 edges

## Surprising Connections (you probably didn't know these)
- `Notebook entry for proposed checkpoint-13 control` --references--> `DECISION-013 — One-rank high-cadence SIM-02 control`  [EXTRACTED]
  notebooks/sim02_research.py → research/decisions/DECISION-013-SIM-02-one-rank-high-cadence-control-proposal.md
- `2026-09-18 grompp produced no em.tpr even after package reinstall` --conceptually_related_to--> `Later SIM-01 report attributes resolved grompp failure to __N_SOL_TBD__ molecule-count placeholder`  [INFERRED]
  history/FAILED-001-grompp-segmentation-fault.md → results/reports/SIM-01-validation.md
- `NVT diffusion continuation after NPT density/RDF production` --conceptually_related_to--> `Reported EM, 100 ps NVT, 100 ps NPT, 1 ns NPT, 1 ns supplementary NVT`  [INFERRED]
  research/decisions/DECISION-001-SIM-01-equilibrium-validation.md → results/reports/SIM-01-validation.md
- `SIM-01 validation report: five criteria reported passing; not independently rerun in this extraction` --references--> `DECISION-001 supplementary fixed-volume NVT diffusion leg (historical approval; date placeholder)`  [EXTRACTED]
  results/reports/SIM-01-validation.md → research/decisions/DECISION-001-SIM-01-equilibrium-validation.md
- `SIM-01 validation report: five criteria reported passing; not independently rerun in this extraction` --references--> `DECISION-002: diffusion periodic-boundary correction (2026-09-19 record)`  [EXTRACTED]
  results/reports/SIM-01-validation.md → research/decisions/DECISION-002-msd-pbc-wrapping-correction.md

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

### Community 1 - "SIM-02 Research Record"
Cohesion: 0.08
Nodes (19): Notebook entry for proposed checkpoint-13 control, Checkpoint 13 status in project handoff, DECISION-014 status in project handoff, Checkpoint 13 matched rank-count comparison, SIM-02 research book, Bounded implementation pass, Matched rank-count high-cadence control, DECISION-013 — One-rank high-cadence SIM-02 control (+11 more)

### Community 2 - "Historical NEMD design"
Cohesion: 0.08
Nodes (13): DECISION-003 SIM-02 NEMD design, historical approval claim; date placeholder, SIM-02 two-region thermostat NEMD draft design, Armstrong et al. 2013: Heat Flux and Dipole Moment Dynamic Correlations (unverified literature lead), Armstrong and Bresme 2015: Temperature Inversion of Thermal Polarization of Water (unverified literature lead), Bedeaux et al. 2025: Theory of Thermopolarization Effect (unverified literature lead), Bresme et al. 2008: Water Polarization under Thermal Gradients (unverified literature lead), H4 coupled mechanism (hypothesis), H1 density coupling (hypothesis) (+5 more)

### Community 3 - "SPC/E water model"
Cohesion: 0.10
Nodes (20): Berendsen, Grigera, Straatsma (1987), The missing term in effective pair potentials, J. Phys. Chem. 91, 6269-6271, SPC/E rigid water topology: qO=-0.8476 e, qH=+0.4238 e; oxygen LJ sigma=0.316557 nm, epsilon=0.650194 kJ/mol, SIM-01 configured steepest-descent minimization: max 50000 steps, emtol=1000 kJ/mol/nm, PME, Verlet, 1.0 nm cutoffs, xyz PBC, EnerPres dispersion correction, h-bonds/LINCS, SIM-01 configured NPT production: 1 ns, 300 K, 1 bar, 2 fs timestep, 1 ps trajectory cadence, SIM-01 supplementary NVT diffusion configuration: 1 ns, 300 K, fixed volume, 1 ps trajectory cadence, SIM-01 intended density, O-O RDF, self-diffusion validation targets, SIM-01 configured NPT equilibration: provisional 100 ps, 300 K, 1 bar (+12 more)

### Community 4 - "SIM-01 history and validation"
Cohesion: 0.10
Nodes (20): FAILED-001 historical preprocessing segfault; unresolved in this dated record, 2026-09-18 grompp produced no em.tpr even after package reinstall, DECISION-001 supplementary fixed-volume NVT diffusion leg (historical approval; date placeholder), DECISION-002: diffusion periodic-boundary correction (2026-09-19 record), RDF literature lead arXiv:1706.05491, RDF literature lead arXiv:1806.09956, RDF literature lead arXiv:1809.04996, Berendsen, Grigera, Straatsma (1987), The missing term in effective pair potentials (+12 more)

### Community 5 - "Python standard libraries"
Cohesion: 0.21
Nodes (7): audit(), main(), minimum_image(), nearest_oxygen_distance(), parse_args(), parse_data(), write_report()

### Community 6 - "SIM-02 method decisions"
Cohesion: 0.17
Nodes (13): DECISION-005 selects LAMMPS eHEX for SIM-02, Local LAMMPS build provides eHEX rigid SHAKE RATTLE and PPPM, DECISION-006 approves 400 K validation before 300 K target, DECISION-007 approves the exact 400 K benchmark and staged release gates, Wirnsberger 2016 author-package reproduction notes, SIM-02 checkpoint 07 exact benchmark and staged pilot proposal, SIM-02 LAMMPS eHEX design discussion, Gate 1 measured 4500 neutral waters, reservoir occupancy, RATTLE and PPPM initialization with zero steps (+5 more)

### Community 7 - "Rank-count and COM diagnostics"
Cohesion: 0.20
Nodes (10): DECISION-012: Four-rank high-cadence SIM-02 NVE diagnostic, Per-timestep COM and temperature sampling with soft halt, Byte-identical checkpoint-11 Stage-B restart, Checkpoint 12 raw archive README, Frozen center-of-mass speed ceiling (1e-6 Å/fs), Four-rank NVE result: first ceiling exceedance at 100 fs, One-rank uncorrected NVE result: 2 ps, no ceiling exceedance, SIM-02 checkpoint 10 — one-rank NVE diagnostic (+2 more)

### Community 8 - "Notebook environment"
Cohesion: 0.25
Nodes (8): Pinned Python analysis and notebook environment, Jupyter 1.1.1, marimo 0.24.2 (duplicate requirement), Matplotlib 3.11.2, MDAnalysis 2.10.0, NumPy 2.5.3, pandas 3.0.6, SciPy 1.18.1

### Community 9 - "Checkpoint 07 baseline"
Cohesion: 0.25
Nodes (8): SIM-02 checkpoint 07, data.spce-4500.ness-ewald, Ewald 1e-5 long-range solver, Gate 1 zero-step audit, Hot and cold reservoirs, PPPM 1e-5 long-range solver, Rigid SPC/E model, Author-supplied steady-state Ewald configuration

### Community 10 - "Same-restart rank test"
Cohesion: 0.33
Nodes (3): Center-of-Mass Speed Ceiling, Checkpoint 10 Independent Stage-B Replay, Rank-Count-Sensitive Numerical Behavior

### Community 11 - "NEMD production proposal"
Cohesion: 0.40
Nodes (5): SIM-02 configured NEMD production: provisional 1.5 ns, 2 fs timestep, 0.5 ps trajectory cadence, Intended NEMD observables: T(z), rho(z), Pz(z), SIM-02 configured NEMD startup: provisional 500 ps, 2 fs timestep, no pressure coupling, DECISION-003 reference in NEMD startup comments, make_spatial_groups.md reference for spatial thermostat groups

### Community 12 - "Project guidance and Graphify"
Cohesion: 0.50
Nodes (3): Project guidance: SIM-02, graphify, token-reduction, Graphify bounded retrieval guidance, Pinned Graphify dependency: graphifyy 0.9.72

### Community 13 - "Checkpoint 08 MPI momentum"
Cohesion: 0.40
Nodes (4): Corrected MPI Dry-Run Output, MPI RATTLE COM-Velocity Floor, Checkpoint 08 MPI Momentum Initialization Record, Initial MPI Momentum Run Output

### Community 14 - "Checkpoint 08 COM failure"
Cohesion: 0.50
Nodes (4): Checkpoint 08 Frozen COM Criterion Failure, Checkpoint 08 Stage-A LAMMPS Log, Checkpoint 08 Stage-A COM-Drift Record, Checkpoint 08 Stage-A Standard Output

### Community 15 - "Colab compute tradeoffs"
Cohesion: 0.50
Nodes (3): LAMMPS Checkpoint 07 run 0, Imported 4,500-Molecule SPC/E Structure, Checkpoint 07 Structural Audit Pass

### Community 16 - "Checkpoint 10 rank comparison"
Cohesion: 0.50
Nodes (3): Fixed checkpoint-09 Stage-B restart, Rank-count-sensitive Stage-C/NVE sequence, SIM-02 checkpoint 11 — same-restart one-rank diagnostic

### Community 18 - "Research workflow and claim classes"
Cohesion: 0.67
Nodes (3): DECISION-008 Equilibrium Bridge Approval, Fixed-Volume 400 K PPPM Equilibrium Bridge, Unreported NpT Pressure Boundary

### Community 19 - "Checkpoint 08 approval"
Cohesion: 0.67
Nodes (3): Checkpoint 08 Equilibrium Bridge Design, Four-Stage Fixed-Volume Bridge Protocol, Frozen Gate 2 Acceptance Criteria

### Community 20 - "Checkpoint 08 bridge protocol"
Cohesion: 1.00
Nodes (3): Checkpoint 09 Preparation Momentum-Control Design, Preparation-Only Momentum Removal, Uncorrected NVE COM-Ceiling Failure

### Community 22 - "Checkpoint 09 measured outcomes"
Cohesion: 0.67
Nodes (3): Bounded implementation diagnostic, not equilibrium or polarization, Checkpoint 11 raw diagnostic archive, Byte-identical four-rank checkpoint-09 Stage-B restart

### Community 24 - "Checkpoint 11 raw provenance"
Cohesion: 0.67
Nodes (3): Measured COM speeds: 1.02778929e-5 Å/fs at 1 ps and 1.25105105e-5 Å/fs at 2 ps, Checkpoint 08 stopped before NVT and NVE; no equilibrium, eHEX, or polarization result exists, SIM-02 gate 2 failed at 2 ps: Stage-A COM speed exceeded the frozen ceiling

## Knowledge Gaps
- **101 isolated node(s):** `Measured COM speeds: 1.02778929e-5 Å/fs at 1 ps and 1.25105105e-5 Å/fs at 2 ps`, `Checkpoint 08 stopped before NVT and NVE; no equilibrium, eHEX, or polarization result exists`, `DECISION-009 approved momentum removal only during Stage-A/B preparation; no periodic correction in NVE`, `Wirnsberger 2016 author-package reproduction notes`, `SIM-01 report actual commands section empty` (+96 more)
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 149 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **20 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Are the 6 inferred relationships involving `SETTLE rigid water geometry: OH=0.1000 nm, HH=0.16330 nm` (e.g. with `SIM-01 configured steepest-descent minimization: max 50000 steps, emtol=1000 kJ/mol/nm` and `SIM-01 configured NPT equilibration: provisional 100 ps, 300 K, 1 bar`) actually correct?**
  _`SETTLE rigid water geometry: OH=0.1000 nm, HH=0.16330 nm` has 6 INFERRED edges - model-reasoned connections that need verification._
- **What connects `Measured COM speeds: 1.02778929e-5 Å/fs at 1 ps and 1.25105105e-5 Å/fs at 2 ps`, `Checkpoint 08 stopped before NVT and NVE; no equilibrium, eHEX, or polarization result exists`, `DECISION-009 approved momentum removal only during Stage-A/B preparation; no periodic correction in NVE` to the rest of the system?**
  _101 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `Python analysis symbols` be split into smaller, more focused modules?**
  _Cohesion score 0.10344827586206896 - nodes in this community are weakly interconnected._
- **Should `SIM-02 Research Record` be split into smaller, more focused modules?**
  _Cohesion score 0.08307692307692308 - nodes in this community are weakly interconnected._
- **Should `Historical NEMD design` be split into smaller, more focused modules?**
  _Cohesion score 0.08 - nodes in this community are weakly interconnected._
- **Should `SPC/E water model` be split into smaller, more focused modules?**
  _Cohesion score 0.10276679841897234 - nodes in this community are weakly interconnected._
- **Should `SIM-01 history and validation` be split into smaller, more focused modules?**
  _Cohesion score 0.09523809523809523 - nodes in this community are weakly interconnected._
