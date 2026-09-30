# Graph Report - Thermal-Polarization  (2026-10-01)

## Corpus Check
- 59 files · ~22,820 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 24 file(s) not represented in the graph (top: .mdp 10, (none) 3, .lammps 2)

## Summary
- 205 nodes · 217 edges · 37 communities (12 shown, 25 thin omitted)
- Extraction: 93% EXTRACTED · 6% INFERRED · 0% AMBIGUOUS · INFERRED: 14 edges (avg confidence: 0.95)
- Token cost: 0 input · 0 output

## Community Hubs (Navigation)
- DECISION-005 selects LAMMPS eHEX for SIM-02
- analyze_density_temperature.py
- SIM-01 validation report: five criteria reported passing; not independently rerun in this extraction
- audit_sim02_lammps_data.py
- SETTLE rigid water geometry: OH=0.1000 nm, HH=0.16330 nm
- SIM-02 two-region thermostat NEMD draft design
- Research question: reproducible spatial polarization under a controlled thermal gradient
- Pinned Python analysis and notebook environment
- SPC/E rigid water topology: qO=-0.8476 e, qH=+0.4238 e; oxygen LJ sigma=0.316557 nm, epsilon=0.650194 kJ/mol
- SIM-02 configured NEMD startup: provisional 500 ps, 2 fs timestep, no pressure coupling
- SIM-02 checkpoint 08 — PPPM equilibrium bridge
- SIM-02 checkpoint 07 — zero-step structural audit
- SIM-02 LAMMPS implementation
- book/README.md
- literature/README.md
- checkpoint-08-equilibrium/README.md

## God Nodes (most connected - your core abstractions)
1. `SIM-01 validation report: five criteria reported passing; not independently rerun in this extraction` - 13 edges
2. `Research question: reproducible spatial polarization under a controlled thermal gradient` - 12 edges
3. `SIM-02 checkpoint 08 — PPPM equilibrium bridge` - 8 edges
4. `DECISION-005 selects LAMMPS eHEX for SIM-02` - 8 edges
5. `SIM-02 two-region thermostat NEMD draft design` - 8 edges
6. `SETTLE rigid water geometry: OH=0.1000 nm, HH=0.16330 nm` - 7 edges
7. `Supplied SIM-02 Claude prompt: reference proposal and workflow, not present authorization` - 7 edges
8. `Pinned Python analysis and notebook environment` - 7 edges
9. `SIM-02 current state: checkpoint 07 gate 1 passed and equilibrium bridge next` - 6 edges
10. `read_xvg()` - 5 edges

## Surprising Connections (you probably didn't know these)
- `SIM-02 two-region thermostat NEMD draft design` --conceptually_related_to--> `SIM-02 scope: thermal-gradient NEMD and spatial polarization evidence`  [AMBIGUOUS]
  research/decisions/DECISION-003-SIM-02-NEMD-design.md → README.md
- `Thermal-Polarization official project chronology` --references--> `Research lifecycle: learn discuss decide implement execute analyze synchronize`  [EXTRACTED]
  README.md → research/WORKFLOW.md
- `SIM-02 run status: engine selected and implementation pending` --references--> `DECISION-005 selects LAMMPS eHEX for SIM-02`  [EXTRACTED]
  simulations/SIM-02/README.md → research/decisions/DECISION-005-SIM-02-LAMMPS-eHEX.md
- `Project guidance: SIM-02, graphify, token-reduction` --references--> `SIM-02 current state: checkpoint 07 gate 1 passed and equilibrium bridge next`  [EXTRACTED]
  AGENTS.md → PROJECT_STATE.md
- `Pinned Graphify dependency: graphifyy 0.9.72` --conceptually_related_to--> `Graphify query/path/explain and AST update workflow`  [INFERRED]
  environment/requirements-graphify.txt → CLAUDE.md

## Import Cycles
- None detected.

## Hyperedges (group relationships)
- **Proposed joint NEMD stationarity and uncertainty assessment** — research_prompts_sim_02_claude_prompt_temperature_profile, research_prompts_sim_02_claude_prompt_density_profile, research_prompts_sim_02_claude_prompt_polarization_profile, research_prompts_sim_02_claude_prompt_orientation, research_prompts_sim_02_claude_prompt_heat_flux, research_prompts_sim_02_claude_prompt_block_uncertainty [EXTRACTED 1.00]

## Communities (37 total, 25 thin omitted)

### Community 0 - "DECISION-005 selects LAMMPS eHEX for SIM-02"
Cohesion: 0.10
Nodes (24): Project guidance: SIM-02, graphify, token-reduction, Graphify bounded retrieval guidance, DECISION-005 selects LAMMPS eHEX for SIM-02, Local LAMMPS build provides eHEX rigid SHAKE RATTLE and PPPM, DECISION-006 approves 400 K validation before 300 K target, DECISION-007 approves the exact 400 K benchmark and staged release gates, Pinned Graphify dependency: graphifyy 0.9.72, SIM-02 current state: checkpoint 07 gate 1 passed and equilibrium bridge next (+16 more)

### Community 2 - "SIM-01 validation report: five criteria reported passing; not independently rerun in this extraction"
Cohesion: 0.10
Nodes (20): FAILED-001 historical preprocessing segfault; unresolved in this dated record, 2026-09-18 grompp produced no em.tpr even after package reinstall, DECISION-001 supplementary fixed-volume NVT diffusion leg (historical approval; date placeholder), DECISION-002: diffusion periodic-boundary correction (2026-09-19 record), RDF literature lead arXiv:1706.05491, RDF literature lead arXiv:1806.09956, RDF literature lead arXiv:1809.04996, Berendsen, Grigera, Straatsma (1987), The missing term in effective pair potentials (+12 more)

### Community 3 - "audit_sim02_lammps_data.py"
Cohesion: 0.14
Nodes (9): audit(), main(), minimum_image(), nearest_oxygen_distance(), parse_args(), parse_data(), write_report(), main() (+1 more)

### Community 4 - "SETTLE rigid water geometry: OH=0.1000 nm, HH=0.16330 nm"
Cohesion: 0.15
Nodes (15): SIM-01 configured steepest-descent minimization: max 50000 steps, emtol=1000 kJ/mol/nm, PME, Verlet, 1.0 nm cutoffs, xyz PBC, EnerPres dispersion correction, h-bonds/LINCS, SIM-01 configured NPT production: 1 ns, 300 K, 1 bar, 2 fs timestep, 1 ps trajectory cadence, SIM-01 supplementary NVT diffusion configuration: 1 ns, 300 K, fixed volume, 1 ps trajectory cadence, SIM-01 intended density, O-O RDF, self-diffusion validation targets, SIM-01 configured NPT equilibration: provisional 100 ps, 300 K, 1 bar, PME, Verlet, 1.0 nm cutoffs, xyz PBC, EnerPres dispersion correction, h-bonds/LINCS, SIM-01 configured NVT equilibration: provisional 100 ps, 300 K, V-rescale tau=0.1 ps (+7 more)

### Community 5 - "SIM-02 two-region thermostat NEMD draft design"
Cohesion: 0.15
Nodes (8): DECISION-003 SIM-02 NEMD design, historical approval claim; date placeholder, SIM-02 two-region thermostat NEMD draft design, Armstrong et al. 2013: Heat Flux and Dipole Moment Dynamic Correlations (unverified literature lead), Armstrong and Bresme 2015: Temperature Inversion of Thermal Polarization of Water (unverified literature lead), Bedeaux et al. 2025: Theory of Thermopolarization Effect (unverified literature lead), Bresme et al. 2008: Water Polarization under Thermal Gradients (unverified literature lead), Supplied SIM-02 Claude prompt: reference proposal and workflow, not present authorization, Lervik et al. 2022: molecular dipole and quadrupole moments (unverified literature lead)

### Community 6 - "Research question: reproducible spatial polarization under a controlled thermal gradient"
Cohesion: 0.17
Nodes (5): H4 coupled mechanism (hypothesis), H1 density coupling (hypothesis), H3 molecular dynamics/heat-flux coupling (hypothesis), H2 local structure/hydrogen-bond coupling (hypothesis), Research question: reproducible spatial polarization under a controlled thermal gradient

### Community 7 - "Pinned Python analysis and notebook environment"
Cohesion: 0.25
Nodes (8): Pinned Python analysis and notebook environment, Jupyter 1.1.1, marimo 0.24.2 (duplicate requirement), Matplotlib 3.11.2, MDAnalysis 2.10.0, NumPy 2.5.3, pandas 3.0.6, SciPy 1.18.1

### Community 8 - "SPC/E rigid water topology: qO=-0.8476 e, qH=+0.4238 e; oxygen LJ sigma=0.316557 nm, epsilon=0.650194 kJ/mol"
Cohesion: 0.33
Nodes (5): Berendsen, Grigera, Straatsma (1987), The missing term in effective pair potentials, J. Phys. Chem. 91, 6269-6271, SPC/E rigid water topology: qO=-0.8476 e, qH=+0.4238 e; oxygen LJ sigma=0.316557 nm, epsilon=0.650194 kJ/mol, SIM-01 topology: 510 SOL molecules, Unresolved SIM-02 molecule count from gmx solvate, SIM-02 draft topology: SOL molecule count remains __N_SOL_TBD__

### Community 9 - "SIM-02 configured NEMD startup: provisional 500 ps, 2 fs timestep, no pressure coupling"
Cohesion: 0.40
Nodes (5): SIM-02 configured NEMD production: provisional 1.5 ns, 2 fs timestep, 0.5 ps trajectory cadence, Intended NEMD observables: T(z), rho(z), Pz(z), SIM-02 configured NEMD startup: provisional 500 ps, 2 fs timestep, no pressure coupling, DECISION-003 reference in NEMD startup comments, make_spatial_groups.md reference for spatial thermostat groups

### Community 12 - "SIM-02 checkpoint 08 — PPPM equilibrium bridge"
Cohesion: 0.18
Nodes (10): Thermal-Polarization official project chronology, SIM-02 scope: thermal-gradient NEMD and spatial polarization evidence, Acceptance criteria frozen before execution, Checkpoint question, Frozen evidence and output plan, Proposed bridge, Release consequence, Restart and Colab contract (+2 more)

### Community 13 - "SIM-02 checkpoint 07 — zero-step structural audit"
Cohesion: 0.50
Nodes (3): Checks, Observations, SIM-02 checkpoint 07 — zero-step structural audit

### Community 14 - "SIM-02 LAMMPS implementation"
Cohesion: 0.40
Nodes (4): Gate 1 commands, Proposed gate 2 command, Provenance, SIM-02 LAMMPS implementation

## Ambiguous Edges - Review These
- `SIM-02 scope: thermal-gradient NEMD and spatial polarization evidence` → `SIM-02 two-region thermostat NEMD draft design`  [AMBIGUOUS]
  research/decisions/DECISION-003-SIM-02-NEMD-design.md · relation: conceptually_related_to

## Knowledge Gaps
- **63 isolated node(s):** `Research book`, `Checkpoint question`, `Why a bridge is required`, `Proposed bridge`, `Frozen evidence and output plan` (+58 more)
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 123 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **25 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **What is the exact relationship between `SIM-02 scope: thermal-gradient NEMD and spatial polarization evidence` and `SIM-02 two-region thermostat NEMD draft design`?**
  _Edge tagged AMBIGUOUS (relation: conceptually_related_to) - confidence is low._
- **Why does `Thermal-Polarization official project chronology` connect `SIM-02 checkpoint 08 — PPPM equilibrium bridge` to `DECISION-005 selects LAMMPS eHEX for SIM-02`?**
  _High betweenness centrality (0.060) - this node is a cross-community bridge._
- **Why does `SIM-02 two-region thermostat NEMD draft design` connect `SIM-02 two-region thermostat NEMD draft design` to `SIM-02 checkpoint 08 — PPPM equilibrium bridge`?**
  _High betweenness centrality (0.051) - this node is a cross-community bridge._
- **Why does `SIM-02 scope: thermal-gradient NEMD and spatial polarization evidence` connect `SIM-02 checkpoint 08 — PPPM equilibrium bridge` to `SIM-02 two-region thermostat NEMD draft design`?**
  _High betweenness centrality (0.046) - this node is a cross-community bridge._
- **What connects `Research book`, `Checkpoint question`, `Why a bridge is required` to the rest of the system?**
  _63 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `DECISION-005 selects LAMMPS eHEX for SIM-02` be split into smaller, more focused modules?**
  _Cohesion score 0.09788359788359788 - nodes in this community are weakly interconnected._
- **Should `analyze_density_temperature.py` be split into smaller, more focused modules?**
  _Cohesion score 0.13438735177865613 - nodes in this community are weakly interconnected._