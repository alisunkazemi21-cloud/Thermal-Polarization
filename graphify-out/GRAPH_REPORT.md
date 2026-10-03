> Extraction token usage was not exposed by this session; any zero token counters below are placeholders, not measured zero consumption.
> Research claims are indexed from sources, not independently verified.

# Graph Report - Thermal-Polarization  (2026-10-03)

## Corpus Check
- Corpus is ~29,732 words - fits in a single context window. You may not need a graph.

## Summary
- 166 nodes · 193 edges · 16 communities (11 shown, 5 thin omitted)
- Extraction: 94% EXTRACTED · 6% INFERRED · 0% AMBIGUOUS · INFERRED: 12 edges (avg confidence: 0.95)
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
- SIM-02 checkpoint 08 — PPPM equilibrium bridge
- marimo
- graphify.ps1
- SIM-02 checkpoint 07 — zero-step structural audit
- SIM-02 LAMMPS implementation

## God Nodes (most connected - your core abstractions)
1. `SIM-01 validation report: five criteria reported passing; not independently rerun in this extraction` - 14 edges
2. `Research question: reproducible spatial polarization under a controlled thermal gradient` - 12 edges
3. `Pinned Python analysis and notebook environment` - 7 edges
4. `SIM-02 two-region thermostat NEMD draft design` - 7 edges
5. `Supplied SIM-02 Claude prompt: reference proposal and workflow, not present authorization` - 7 edges
6. `SETTLE rigid water geometry: OH=0.1000 nm, HH=0.16330 nm` - 7 edges
7. `SIM-02 gate 2 failed at 2 ps: Stage-A COM speed exceeded the frozen ceiling` - 6 edges
8. `read_xvg()` - 5 edges
9. `main()` - 5 edges
10. `SPC/E rigid water topology: qO=-0.8476 e, qH=+0.4238 e; oxygen LJ sigma=0.316557 nm, epsilon=0.650194 kJ/mol` - 5 edges

## Surprising Connections (you probably didn't know these)
- `Pinned Graphify dependency: graphifyy 0.9.72` --conceptually_related_to--> `Graphify query/path/explain and AST update workflow`  [INFERRED]
  environment/requirements-graphify.txt → CLAUDE.md
- `SIM-01 validation report: five criteria reported passing; not independently rerun in this extraction` --references--> `DECISION-001 supplementary fixed-volume NVT diffusion leg (historical approval; date placeholder)`  [EXTRACTED]
  results/reports/SIM-01-validation.md → research/decisions/DECISION-001-SIM-01-equilibrium-validation.md
- `NVT diffusion continuation after NPT density/RDF production` --conceptually_related_to--> `Reported EM, 100 ps NVT, 100 ps NPT, 1 ns NPT, 1 ns supplementary NVT`  [INFERRED]
  research/decisions/DECISION-001-SIM-01-equilibrium-validation.md → results/reports/SIM-01-validation.md
- `2026-09-18 grompp produced no em.tpr even after package reinstall` --conceptually_related_to--> `Later SIM-01 report attributes resolved grompp failure to __N_SOL_TBD__ molecule-count placeholder`  [INFERRED]
  history/FAILED-001-grompp-segmentation-fault.md → results/reports/SIM-01-validation.md
- `SIM-01 topology: 510 SOL molecules` --references--> `SPC/E rigid water topology: qO=-0.8476 e, qH=+0.4238 e; oxygen LJ sigma=0.316557 nm, epsilon=0.650194 kJ/mol`  [EXTRACTED]
  simulations/SIM-01/topol.top → models/SPC-E/spce.itp

## Import Cycles
- None detected.

## Hyperedges (group relationships)
- **Proposed joint NEMD stationarity and uncertainty assessment** — research_prompts_sim_02_claude_prompt_temperature_profile, research_prompts_sim_02_claude_prompt_density_profile, research_prompts_sim_02_claude_prompt_polarization_profile, research_prompts_sim_02_claude_prompt_orientation, research_prompts_sim_02_claude_prompt_heat_flux, research_prompts_sim_02_claude_prompt_block_uncertainty [EXTRACTED 1.00]

## Communities (16 total, 5 thin omitted)

### Community 1 - "analyze_density_temperature.py"
Cohesion: 0.10
Nodes (21): FAILED-001 historical preprocessing segfault; unresolved in this dated record, 2026-09-18 grompp produced no em.tpr even after package reinstall, DECISION-001 supplementary fixed-volume NVT diffusion leg (historical approval; date placeholder), DECISION-002: diffusion periodic-boundary correction (2026-09-19 record), Planned documentary research series: six baseline episodes and future NEMD/electrical episodes, RDF literature lead arXiv:1706.05491, RDF literature lead arXiv:1806.09956, RDF literature lead arXiv:1809.04996 (+13 more)

### Community 2 - "SIM-01 validation report: five criteria reported passing; not independently rerun in this extraction"
Cohesion: 0.14
Nodes (9): audit(), main(), minimum_image(), nearest_oxygen_distance(), parse_args(), parse_data(), write_report(), main() (+1 more)

### Community 3 - "audit_sim02_lammps_data.py"
Cohesion: 0.15
Nodes (15): SIM-01 configured steepest-descent minimization: max 50000 steps, emtol=1000 kJ/mol/nm, PME, Verlet, 1.0 nm cutoffs, xyz PBC, EnerPres dispersion correction, h-bonds/LINCS, SIM-01 configured NPT production: 1 ns, 300 K, 1 bar, 2 fs timestep, 1 ps trajectory cadence, SIM-01 supplementary NVT diffusion configuration: 1 ns, 300 K, fixed volume, 1 ps trajectory cadence, SIM-01 intended density, O-O RDF, self-diffusion validation targets, SIM-01 configured NPT equilibration: provisional 100 ps, 300 K, 1 bar, PME, Verlet, 1.0 nm cutoffs, xyz PBC, EnerPres dispersion correction, h-bonds/LINCS, SIM-01 configured NVT equilibration: provisional 100 ps, 300 K, V-rescale tau=0.1 ps (+7 more)

### Community 4 - "SETTLE rigid water geometry: OH=0.1000 nm, HH=0.16330 nm"
Cohesion: 0.17
Nodes (13): DECISION-005 selects LAMMPS eHEX for SIM-02, Local LAMMPS build provides eHEX rigid SHAKE RATTLE and PPPM, DECISION-006 approves 400 K validation before 300 K target, DECISION-007 approves the exact 400 K benchmark and staged release gates, Wirnsberger 2016 author-package reproduction notes, SIM-02 checkpoint 07 exact benchmark and staged pilot proposal, SIM-02 LAMMPS eHEX design discussion, Gate 1 measured 4500 neutral waters, reservoir occupancy, RATTLE and PPPM initialization with zero steps (+5 more)

### Community 5 - "SIM-02 two-region thermostat NEMD draft design"
Cohesion: 0.15
Nodes (8): DECISION-003 SIM-02 NEMD design, historical approval claim; date placeholder, SIM-02 two-region thermostat NEMD draft design, Armstrong et al. 2013: Heat Flux and Dipole Moment Dynamic Correlations (unverified literature lead), Armstrong and Bresme 2015: Temperature Inversion of Thermal Polarization of Water (unverified literature lead), Bedeaux et al. 2025: Theory of Thermopolarization Effect (unverified literature lead), Bresme et al. 2008: Water Polarization under Thermal Gradients (unverified literature lead), Supplied SIM-02 Claude prompt: reference proposal and workflow, not present authorization, Lervik et al. 2022: molecular dipole and quadrupole moments (unverified literature lead)

### Community 6 - "Research question: reproducible spatial polarization under a controlled thermal gradient"
Cohesion: 0.17
Nodes (5): H4 coupled mechanism (hypothesis), H1 density coupling (hypothesis), H3 molecular dynamics/heat-flux coupling (hypothesis), H2 local structure/hydrogen-bond coupling (hypothesis), Research question: reproducible spatial polarization under a controlled thermal gradient

### Community 7 - "Pinned Python analysis and notebook environment"
Cohesion: 0.20
Nodes (10): SIM-02 current state: gate 2 COM failure documented; checkpoint 09 is next, Checkpoint 09 awaits approval and does not release eHEX or change the frozen physical protocol, Proposed bounded change: fix momentum every 100 preparation steps, off before NVE, Checkpoint 09 proposal: preparation-only momentum removal with kinetic-energy rescaling, Measured COM speeds: 1.02778929e-5 Å/fs at 1 ps and 1.25105105e-5 Å/fs at 2 ps, Checkpoint 08 stopped before NVT and NVE; no equilibrium, eHEX, or polarization result exists, SIM-02 gate 2 failed at 2 ps: Stage-A COM speed exceeded the frozen ceiling, Official project status: SIM-02 gate 1 passed and checkpoint 08 failed at 2 ps (+2 more)

### Community 8 - "SPC/E rigid water topology: qO=-0.8476 e, qH=+0.4238 e; oxygen LJ sigma=0.316557 nm, epsilon=0.650194 kJ/mol"
Cohesion: 0.25
Nodes (8): Pinned Python analysis and notebook environment, Jupyter 1.1.1, marimo 0.24.2 (duplicate requirement), Matplotlib 3.11.2, MDAnalysis 2.10.0, NumPy 2.5.3, pandas 3.0.6, SciPy 1.18.1

### Community 9 - "SIM-02 checkpoint 08 — PPPM equilibrium bridge"
Cohesion: 0.33
Nodes (5): Berendsen, Grigera, Straatsma (1987), The missing term in effective pair potentials, J. Phys. Chem. 91, 6269-6271, SPC/E rigid water topology: qO=-0.8476 e, qH=+0.4238 e; oxygen LJ sigma=0.316557 nm, epsilon=0.650194 kJ/mol, SIM-01 topology: 510 SOL molecules, Unresolved SIM-02 molecule count from gmx solvate, SIM-02 draft topology: SOL molecule count remains __N_SOL_TBD__

### Community 10 - "marimo"
Cohesion: 0.40
Nodes (5): SIM-02 configured NEMD production: provisional 1.5 ns, 2 fs timestep, 0.5 ps trajectory cadence, Intended NEMD observables: T(z), rho(z), Pz(z), SIM-02 configured NEMD startup: provisional 500 ps, 2 fs timestep, no pressure coupling, DECISION-003 reference in NEMD startup comments, make_spatial_groups.md reference for spatial thermostat groups

### Community 11 - "graphify.ps1"
Cohesion: 0.50
Nodes (3): Project guidance: SIM-02, graphify, token-reduction, Graphify bounded retrieval guidance, Pinned Graphify dependency: graphifyy 0.9.72

## Knowledge Gaps
- **56 isolated node(s):** `Project guidance: SIM-02, graphify, token-reduction`, `Pinned Graphify dependency: graphifyy 0.9.72`, `MDAnalysis 2.10.0`, `NumPy 2.5.3`, `pandas 3.0.6` (+51 more)
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 92 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **5 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `SETTLE rigid water geometry: OH=0.1000 nm, HH=0.16330 nm` connect `audit_sim02_lammps_data.py` to `SIM-02 checkpoint 08 — PPPM equilibrium bridge`?**
  _High betweenness centrality (0.020) - this node is a cross-community bridge._
- **Why does `Research question: reproducible spatial polarization under a controlled thermal gradient` connect `Research question: reproducible spatial polarization under a controlled thermal gradient` to `SIM-02 two-region thermostat NEMD draft design`?**
  _High betweenness centrality (0.015) - this node is a cross-community bridge._
- **What connects `Project guidance: SIM-02, graphify, token-reduction`, `Pinned Graphify dependency: graphifyy 0.9.72`, `MDAnalysis 2.10.0` to the rest of the system?**
  _56 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `DECISION-005 selects LAMMPS eHEX for SIM-02` be split into smaller, more focused modules?**
  _Cohesion score 0.13438735177865613 - nodes in this community are weakly interconnected._
- **Should `analyze_density_temperature.py` be split into smaller, more focused modules?**
  _Cohesion score 0.10276679841897234 - nodes in this community are weakly interconnected._
- **Should `SIM-01 validation report: five criteria reported passing; not independently rerun in this extraction` be split into smaller, more focused modules?**
  _Cohesion score 0.14285714285714285 - nodes in this community are weakly interconnected._
- **Should `audit_sim02_lammps_data.py` be split into smaller, more focused modules?**
  _Cohesion score 0.14705882352941177 - nodes in this community are weakly interconnected._