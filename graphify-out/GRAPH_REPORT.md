> Extraction token usage was not exposed by this session; any zero token counters below are placeholders, not measured zero consumption.
> Research claims are indexed from sources, not independently verified.

# Graph Report - Thermal-Polarization  (2026-10-04)

## Corpus Check
- Corpus is ~35,779 words - fits in a single context window. You may not need a graph.

## Summary
- 237 nodes · 243 edges · 38 communities (24 shown, 14 thin omitted)
- Extraction: 95% EXTRACTED · 5% INFERRED · 0% AMBIGUOUS · INFERRED: 13 edges (avg confidence: 0.95)
- Token cost: 0 input · 0 output

## Community Hubs (Navigation)
- Python analysis symbols
- SIM-01 history and validation
- SPC/E water model
- Python standard libraries
- SIM-02 method decisions
- Historical NEMD design
- NEMD observables and uncertainty
- SIM-02 research timeline
- Notebook environment
- Checkpoint 07 baseline
- NEMD production plan
- Project guidance and Graphify
- Checkpoint 08 MPI momentum
- Checkpoint 08 run records
- Project state and run status
- Polarization causal chain
- Checkpoint 07 zero-step audit
- Checkpoint 10 one-rank diagnostic
- Dynamic-region eHEX method
- Checkpoint 08 approval
- DECISION-010 rank comparison
- Checkpoint 08 bridge protocol
- Checkpoint 09 momentum control
- Wirnsberger reproduction
- Checkpoint 09 NVE failure
- Checkpoint 08 COM failure evidence
- LAMMPS method translation
- Equilibrium validation gates
- Open result limitations
- Research workflow and claim classes
- Checkpoint 08 dry run
- SIM-02 NEMD project
- Timestep decisions
- Thermal polarization objective
- YouTube research story
- DECISION-009 scope

## God Nodes (most connected - your core abstractions)
1. `SIM-01 validation report: five criteria reported passing; not independently rerun in this extraction` - 14 edges
2. `Research question: reproducible spatial polarization under a controlled thermal gradient` - 12 edges
3. `Pinned Python analysis and notebook environment` - 7 edges
4. `SIM-02 Research Book` - 7 edges
5. `SIM-02 two-region thermostat NEMD draft design` - 7 edges
6. `Supplied SIM-02 Claude prompt: reference proposal and workflow, not present authorization` - 7 edges
7. `SETTLE rigid water geometry: OH=0.1000 nm, HH=0.16330 nm` - 7 edges
8. `read_xvg()` - 5 edges
9. `main()` - 5 edges
10. `DECISION-005 selects LAMMPS eHEX for SIM-02` - 5 edges

## Surprising Connections (you probably didn't know these)
- `Pinned Graphify dependency: graphifyy 0.9.72` --conceptually_related_to--> `Graphify query/path/explain and AST update workflow`  [INFERRED]
  environment/requirements-graphify.txt → CLAUDE.md
- `2026-09-18 grompp produced no em.tpr even after package reinstall` --conceptually_related_to--> `Later SIM-01 report attributes resolved grompp failure to __N_SOL_TBD__ molecule-count placeholder`  [INFERRED]
  history/FAILED-001-grompp-segmentation-fault.md → results/reports/SIM-01-validation.md
- `SIM-01 validation report: five criteria reported passing; not independently rerun in this extraction` --references--> `DECISION-001 supplementary fixed-volume NVT diffusion leg (historical approval; date placeholder)`  [EXTRACTED]
  results/reports/SIM-01-validation.md → research/decisions/DECISION-001-SIM-01-equilibrium-validation.md
- `NVT diffusion continuation after NPT density/RDF production` --conceptually_related_to--> `Reported EM, 100 ps NVT, 100 ps NPT, 1 ns NPT, 1 ns supplementary NVT`  [INFERRED]
  research/decisions/DECISION-001-SIM-01-equilibrium-validation.md → results/reports/SIM-01-validation.md
- `SIM-01 topology: 510 SOL molecules` --references--> `SPC/E rigid water topology: qO=-0.8476 e, qH=+0.4238 e; oxygen LJ sigma=0.316557 nm, epsilon=0.650194 kJ/mol`  [EXTRACTED]
  simulations/SIM-01/topol.top → models/SPC-E/spce.itp

## Import Cycles
- None detected.

## Hyperedges (group relationships)
- **SIM-02 Validation Checkpoint Sequence** — research_book_sim_02_gate_1_validation, research_book_sim_02_checkpoint_08_com_failure, research_book_sim_02_checkpoint_09_preparation_control, research_book_sim_02_checkpoint_10_rank_sensitive_continuation [EXTRACTED 1.00]
- **Thermal-Gradient Polarization Causal Chain** — research_media_sim_02_longform_youtube_spatial_reservoirs, research_media_sim_02_longform_youtube_heat_flux, research_media_sim_02_longform_youtube_molecular_polarization [EXTRACTED 1.00]
- **Proposed joint NEMD stationarity and uncertainty assessment** — research_prompts_sim_02_claude_prompt_temperature_profile, research_prompts_sim_02_claude_prompt_density_profile, research_prompts_sim_02_claude_prompt_polarization_profile, research_prompts_sim_02_claude_prompt_orientation, research_prompts_sim_02_claude_prompt_heat_flux, research_prompts_sim_02_claude_prompt_block_uncertainty [EXTRACTED 1.00]
- **SIM-02 Validation Checkpoint Sequence** — research_book_sim_02_gate_1_validation, research_book_sim_02_checkpoint_08_com_failure, research_book_sim_02_checkpoint_09_preparation_control, research_book_sim_02_checkpoint_10_rank_sensitive_continuation [EXTRACTED 1.00]
- **Thermal-Gradient Polarization Causal Chain** — research_media_sim_02_longform_youtube_spatial_reservoirs, research_media_sim_02_longform_youtube_heat_flux, research_media_sim_02_longform_youtube_molecular_polarization [EXTRACTED 1.00]

## Communities (38 total, 14 thin omitted)

### Community 1 - "SIM-01 history and validation"
Cohesion: 0.10
Nodes (21): FAILED-001 historical preprocessing segfault; unresolved in this dated record, 2026-09-18 grompp produced no em.tpr even after package reinstall, DECISION-001 supplementary fixed-volume NVT diffusion leg (historical approval; date placeholder), DECISION-002: diffusion periodic-boundary correction (2026-09-19 record), Planned documentary research series: six baseline episodes and future NEMD/electrical episodes, RDF literature lead arXiv:1706.05491, RDF literature lead arXiv:1806.09956, RDF literature lead arXiv:1809.04996 (+13 more)

### Community 2 - "SPC/E water model"
Cohesion: 0.10
Nodes (20): Berendsen, Grigera, Straatsma (1987), The missing term in effective pair potentials, J. Phys. Chem. 91, 6269-6271, SPC/E rigid water topology: qO=-0.8476 e, qH=+0.4238 e; oxygen LJ sigma=0.316557 nm, epsilon=0.650194 kJ/mol, SIM-01 configured steepest-descent minimization: max 50000 steps, emtol=1000 kJ/mol/nm, PME, Verlet, 1.0 nm cutoffs, xyz PBC, EnerPres dispersion correction, h-bonds/LINCS, SIM-01 configured NPT production: 1 ns, 300 K, 1 bar, 2 fs timestep, 1 ps trajectory cadence, SIM-01 supplementary NVT diffusion configuration: 1 ns, 300 K, fixed volume, 1 ps trajectory cadence, SIM-01 intended density, O-O RDF, self-diffusion validation targets, SIM-01 configured NPT equilibration: provisional 100 ps, 300 K, 1 bar (+12 more)

### Community 3 - "Python standard libraries"
Cohesion: 0.14
Nodes (9): audit(), main(), minimum_image(), nearest_oxygen_distance(), parse_args(), parse_data(), write_report(), main() (+1 more)

### Community 4 - "SIM-02 method decisions"
Cohesion: 0.17
Nodes (13): DECISION-005 selects LAMMPS eHEX for SIM-02, Local LAMMPS build provides eHEX rigid SHAKE RATTLE and PPPM, DECISION-006 approves 400 K validation before 300 K target, DECISION-007 approves the exact 400 K benchmark and staged release gates, Wirnsberger 2016 author-package reproduction notes, SIM-02 checkpoint 07 exact benchmark and staged pilot proposal, SIM-02 LAMMPS eHEX design discussion, Gate 1 measured 4500 neutral waters, reservoir occupancy, RATTLE and PPPM initialization with zero steps (+5 more)

### Community 5 - "Historical NEMD design"
Cohesion: 0.15
Nodes (8): DECISION-003 SIM-02 NEMD design, historical approval claim; date placeholder, SIM-02 two-region thermostat NEMD draft design, Armstrong et al. 2013: Heat Flux and Dipole Moment Dynamic Correlations (unverified literature lead), Armstrong and Bresme 2015: Temperature Inversion of Thermal Polarization of Water (unverified literature lead), Bedeaux et al. 2025: Theory of Thermopolarization Effect (unverified literature lead), Bresme et al. 2008: Water Polarization under Thermal Gradients (unverified literature lead), Supplied SIM-02 Claude prompt: reference proposal and workflow, not present authorization, Lervik et al. 2022: molecular dipole and quadrupole moments (unverified literature lead)

### Community 6 - "NEMD observables and uncertainty"
Cohesion: 0.17
Nodes (5): H4 coupled mechanism (hypothesis), H1 density coupling (hypothesis), H3 molecular dynamics/heat-flux coupling (hypothesis), H2 local structure/hydrogen-bond coupling (hypothesis), Research question: reproducible spatial polarization under a controlled thermal gradient

### Community 7 - "SIM-02 research timeline"
Cohesion: 0.22
Nodes (9): Research Book, Checkpoint 08 COM Failure, Checkpoint 09 Preparation Momentum Control, Checkpoint 10 Rank-Sensitive Continuation, Dynamic Spatial Reservoirs, Equilibrium Bridge on Hold, Gate 1 Zero-Step Validation, SIM-02 Research Book (+1 more)

### Community 8 - "Notebook environment"
Cohesion: 0.25
Nodes (8): Pinned Python analysis and notebook environment, Jupyter 1.1.1, marimo 0.24.2 (duplicate requirement), Matplotlib 3.11.2, MDAnalysis 2.10.0, NumPy 2.5.3, pandas 3.0.6, SciPy 1.18.1

### Community 9 - "Checkpoint 07 baseline"
Cohesion: 0.25
Nodes (8): SIM-02 checkpoint 07, data.spce-4500.ness-ewald, Ewald 1e-5 long-range solver, Gate 1 zero-step audit, Hot and cold reservoirs, PPPM 1e-5 long-range solver, Rigid SPC/E model, Author-supplied steady-state Ewald configuration

### Community 10 - "NEMD production plan"
Cohesion: 0.40
Nodes (5): SIM-02 configured NEMD production: provisional 1.5 ns, 2 fs timestep, 0.5 ps trajectory cadence, Intended NEMD observables: T(z), rho(z), Pz(z), SIM-02 configured NEMD startup: provisional 500 ps, 2 fs timestep, no pressure coupling, DECISION-003 reference in NEMD startup comments, make_spatial_groups.md reference for spatial thermostat groups

### Community 11 - "Project guidance and Graphify"
Cohesion: 0.50
Nodes (3): Project guidance: SIM-02, graphify, token-reduction, Graphify bounded retrieval guidance, Pinned Graphify dependency: graphifyy 0.9.72

### Community 12 - "Checkpoint 08 MPI momentum"
Cohesion: 0.40
Nodes (4): Corrected MPI Dry-Run Output, MPI RATTLE COM-Velocity Floor, Checkpoint 08 MPI Momentum Initialization Record, Initial MPI Momentum Run Output

### Community 13 - "Checkpoint 08 run records"
Cohesion: 0.50
Nodes (4): Checkpoint 08 Frozen COM Criterion Failure, Checkpoint 08 Stage-A LAMMPS Log, Checkpoint 08 Stage-A COM-Drift Record, Checkpoint 08 Stage-A Standard Output

### Community 14 - "Project state and run status"
Cohesion: 0.50
Nodes (3): Checkpoint 10 One-Rank NVE Result, Project Handoff State, SIM-02 Equilibrium Bridge Status

### Community 15 - "Polarization causal chain"
Cohesion: 0.50
Nodes (4): eHEX Heat-Exchange Method, Imposed Heat Flux, Molecular Polarization, Spatial Heat Reservoirs

### Community 16 - "Checkpoint 07 zero-step audit"
Cohesion: 0.50
Nodes (3): LAMMPS Checkpoint 07 run 0, Imported 4,500-Molecule SPC/E Structure, Checkpoint 07 Structural Audit Pass

### Community 17 - "Checkpoint 10 one-rank diagnostic"
Cohesion: 0.50
Nodes (3): Checkpoint 10 One-Rank NVE Diagnostic, Full Equilibrium Bridge Remains on Hold, Four-Rank Versus One-Rank COM Comparison

### Community 20 - "Checkpoint 08 approval"
Cohesion: 0.67
Nodes (3): DECISION-008 Equilibrium Bridge Approval, Fixed-Volume 400 K PPPM Equilibrium Bridge, Unreported NpT Pressure Boundary

### Community 21 - "DECISION-010 rank comparison"
Cohesion: 1.00
Nodes (3): DECISION-010 NVE COM-Drift Review, Rank-Sensitive Stage-B-to-NVE Continuation, Same-Restart One-Rank Follow-Up Diagnostic

### Community 22 - "Checkpoint 08 bridge protocol"
Cohesion: 0.67
Nodes (3): Checkpoint 08 Equilibrium Bridge Design, Four-Stage Fixed-Volume Bridge Protocol, Frozen Gate 2 Acceptance Criteria

### Community 23 - "Checkpoint 09 momentum control"
Cohesion: 1.00
Nodes (3): Checkpoint 09 Preparation Momentum-Control Design, Preparation-Only Momentum Removal, Uncorrected NVE COM-Ceiling Failure

### Community 24 - "Wirnsberger reproduction"
Cohesion: 0.67
Nodes (3): Wirnsberger 2016 Reproduction Notes, Wirnsberger 2016 Replication Configuration, 400 K Fixed-Volume Equilibrium Bridge

### Community 26 - "Checkpoint 08 COM failure evidence"
Cohesion: 0.67
Nodes (3): Measured COM speeds: 1.02778929e-5 Å/fs at 1 ps and 1.25105105e-5 Å/fs at 2 ps, Checkpoint 08 stopped before NVT and NVE; no equilibrium, eHEX, or polarization result exists, SIM-02 gate 2 failed at 2 ps: Stage-A COM speed exceeded the frozen ceiling

### Community 27 - "LAMMPS method translation"
Cohesion: 0.67
Nodes (3): Ewald-to-PPPM LAMMPS Translation, Fixed-Identity Thermostat Limitation, Approved LAMMPS eHEX Method

## Knowledge Gaps
- **94 isolated node(s):** `Project guidance: SIM-02, graphify, token-reduction`, `SIM-02 Equilibrium Bridge Status`, `Thermal-Polarization Causal Chain`, `Pinned Graphify dependency: graphifyy 0.9.72`, `MDAnalysis 2.10.0` (+89 more)
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 137 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **14 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `Research question: reproducible spatial polarization under a controlled thermal gradient` connect `NEMD observables and uncertainty` to `Historical NEMD design`?**
  _High betweenness centrality (0.007) - this node is a cross-community bridge._
- **What connects `Project guidance: SIM-02, graphify, token-reduction`, `SIM-02 Equilibrium Bridge Status`, `Thermal-Polarization Causal Chain` to the rest of the system?**
  _94 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `Python analysis symbols` be split into smaller, more focused modules?**
  _Cohesion score 0.13438735177865613 - nodes in this community are weakly interconnected._
- **Should `SIM-01 history and validation` be split into smaller, more focused modules?**
  _Cohesion score 0.10276679841897234 - nodes in this community are weakly interconnected._
- **Should `SPC/E water model` be split into smaller, more focused modules?**
  _Cohesion score 0.10276679841897234 - nodes in this community are weakly interconnected._
- **Should `Python standard libraries` be split into smaller, more focused modules?**
  _Cohesion score 0.14285714285714285 - nodes in this community are weakly interconnected._