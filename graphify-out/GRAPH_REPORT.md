> Extraction token usage was not exposed by this session; any zero token counters below are placeholders, not measured zero consumption.
> Research claims are indexed from sources, not independently verified.

# Graph Report - Thermal-Polarization  (2026-09-30)

## Corpus Check
- Corpus is ~13,970 words - fits in a single context window. You may not need a graph.

## Summary
- 133 nodes · 149 edges · 12 communities (9 shown, 3 thin omitted)
- Extraction: 91% EXTRACTED · 9% INFERRED · 1% AMBIGUOUS · INFERRED: 13 edges (avg confidence: 0.95)
- Token cost: 0 input · 0 output

## Community Hubs (Navigation)
- Validation and historical decisions
- Analysis code dependencies
- Equilibrium simulation protocols
- NEMD design and literature
- Polarization observables and hypotheses
- Project handoff and retrieval
- Analysis environment packages
- SPC/E topology and molecule count
- NEMD draft thermostat configuration
- Density temperature data parsing

## God Nodes (most connected - your core abstractions)
1. `SIM-01 validation report: five criteria reported passing; not independently rerun in this extraction` - 13 edges
2. `Research question: reproducible spatial polarization under a controlled thermal gradient` - 12 edges
3. `SIM-02 two-region thermostat NEMD draft design` - 8 edges
4. `DECISION-005 selects LAMMPS eHEX for SIM-02` - 8 edges
5. `Pinned Python analysis and notebook environment` - 7 edges
6. `Supplied SIM-02 Claude prompt: reference proposal and workflow, not present authorization` - 7 edges
7. `SETTLE rigid water geometry: OH=0.1000 nm, HH=0.16330 nm` - 7 edges
8. `read_xvg()` - 5 edges
9. `SPC/E rigid water topology: qO=-0.8476 e, qH=+0.4238 e; oxygen LJ sigma=0.316557 nm, epsilon=0.650194 kJ/mol` - 5 edges
10. `SIM-01 equilibrium SPC/E validation baseline` - 4 edges

## Surprising Connections (you probably didn't know these)
- `SIM-02 two-region thermostat NEMD draft design` --conceptually_related_to--> `SIM-02 scope: thermal-gradient NEMD and spatial polarization evidence`  [AMBIGUOUS]
  research/decisions/DECISION-003-SIM-02-NEMD-design.md → README.md
- `Pinned Graphify dependency: graphifyy 0.9.72` --conceptually_related_to--> `Graphify query/path/explain and AST update workflow`  [INFERRED]
  environment/requirements-graphify.txt → CLAUDE.md
- `SIM-01 validation report: five criteria reported passing; not independently rerun in this extraction` --references--> `DECISION-001 supplementary fixed-volume NVT diffusion leg (historical approval; date placeholder)`  [EXTRACTED]
  results/reports/SIM-01-validation.md → research/decisions/DECISION-001-SIM-01-equilibrium-validation.md
- `SIM-01 validation report: five criteria reported passing; not independently rerun in this extraction` --references--> `DECISION-002: diffusion periodic-boundary correction (2026-09-19 record)`  [EXTRACTED]
  results/reports/SIM-01-validation.md → research/decisions/DECISION-002-msd-pbc-wrapping-correction.md
- `NVT diffusion continuation after NPT density/RDF production` --conceptually_related_to--> `Reported EM, 100 ps NVT, 100 ps NPT, 1 ns NPT, 1 ns supplementary NVT`  [INFERRED]
  research/decisions/DECISION-001-SIM-01-equilibrium-validation.md → results/reports/SIM-01-validation.md

## Import Cycles
- None detected.

## Hyperedges (group relationships)
- **Proposed joint NEMD stationarity and uncertainty assessment** — research_prompts_sim_02_claude_prompt_temperature_profile, research_prompts_sim_02_claude_prompt_density_profile, research_prompts_sim_02_claude_prompt_polarization_profile, research_prompts_sim_02_claude_prompt_orientation, research_prompts_sim_02_claude_prompt_heat_flux, research_prompts_sim_02_claude_prompt_block_uncertainty [EXTRACTED 1.00]

## Communities (12 total, 3 thin omitted)

### Community 1 - "Analysis code dependencies"
Cohesion: 0.10
Nodes (20): FAILED-001 historical preprocessing segfault; unresolved in this dated record, 2026-09-18 grompp produced no em.tpr even after package reinstall, DECISION-001 supplementary fixed-volume NVT diffusion leg (historical approval; date placeholder), DECISION-002: diffusion periodic-boundary correction (2026-09-19 record), RDF literature lead arXiv:1706.05491, RDF literature lead arXiv:1806.09956, RDF literature lead arXiv:1809.04996, Berendsen, Grigera, Straatsma (1987), The missing term in effective pair potentials (+12 more)

### Community 2 - "Equilibrium simulation protocols"
Cohesion: 0.15
Nodes (15): SIM-01 configured steepest-descent minimization: max 50000 steps, emtol=1000 kJ/mol/nm, PME, Verlet, 1.0 nm cutoffs, xyz PBC, EnerPres dispersion correction, h-bonds/LINCS, SIM-01 configured NPT production: 1 ns, 300 K, 1 bar, 2 fs timestep, 1 ps trajectory cadence, SIM-01 supplementary NVT diffusion configuration: 1 ns, 300 K, fixed volume, 1 ps trajectory cadence, SIM-01 intended density, O-O RDF, self-diffusion validation targets, SIM-01 configured NPT equilibration: provisional 100 ps, 300 K, 1 bar, PME, Verlet, 1.0 nm cutoffs, xyz PBC, EnerPres dispersion correction, h-bonds/LINCS, SIM-01 configured NVT equilibration: provisional 100 ps, 300 K, V-rescale tau=0.1 ps (+7 more)

### Community 3 - "NEMD design and literature"
Cohesion: 0.17
Nodes (12): Project guidance: SIM-02, graphify, token-reduction, Graphify bounded retrieval guidance, DECISION-005 selects LAMMPS eHEX for SIM-02, Local LAMMPS build provides eHEX rigid SHAKE RATTLE and PPPM, DECISION-006 approves 400 K validation before 300 K target, Pinned Graphify dependency: graphifyy 0.9.72, SIM-02 current state: LAMMPS eHEX selected and design choices open, SIM-02 LAMMPS eHEX design discussion (+4 more)

### Community 4 - "Polarization observables and hypotheses"
Cohesion: 0.15
Nodes (8): DECISION-003 SIM-02 NEMD design, historical approval claim; date placeholder, SIM-02 two-region thermostat NEMD draft design, Armstrong et al. 2013: Heat Flux and Dipole Moment Dynamic Correlations (unverified literature lead), Armstrong and Bresme 2015: Temperature Inversion of Thermal Polarization of Water (unverified literature lead), Bedeaux et al. 2025: Theory of Thermopolarization Effect (unverified literature lead), Bresme et al. 2008: Water Polarization under Thermal Gradients (unverified literature lead), Supplied SIM-02 Claude prompt: reference proposal and workflow, not present authorization, Lervik et al. 2022: molecular dipole and quadrupole moments (unverified literature lead)

### Community 5 - "Project handoff and retrieval"
Cohesion: 0.17
Nodes (5): H4 coupled mechanism (hypothesis), H1 density coupling (hypothesis), H3 molecular dynamics/heat-flux coupling (hypothesis), H2 local structure/hydrogen-bond coupling (hypothesis), Research question: reproducible spatial polarization under a controlled thermal gradient

### Community 6 - "Analysis environment packages"
Cohesion: 0.25
Nodes (8): Pinned Python analysis and notebook environment, Jupyter 1.1.1, marimo 0.24.2 (duplicate requirement), Matplotlib 3.11.2, MDAnalysis 2.10.0, NumPy 2.5.3, pandas 3.0.6, SciPy 1.18.1

### Community 7 - "SPC/E topology and molecule count"
Cohesion: 0.29
Nodes (7): Thermal-Polarization official project chronology, SIM-02 scope: thermal-gradient NEMD and spatial polarization evidence, YouTube roadmap links SIM-02 evidence-led long-form treatment, Academic claim classes separate established measured inferred hypothesis and open, Research lifecycle: learn discuss decide implement execute analyze synchronize, SIM-02 long-form YouTube research story, SIM-02 chronological academic narrative

### Community 8 - "NEMD draft thermostat configuration"
Cohesion: 0.33
Nodes (5): Berendsen, Grigera, Straatsma (1987), The missing term in effective pair potentials, J. Phys. Chem. 91, 6269-6271, SPC/E rigid water topology: qO=-0.8476 e, qH=+0.4238 e; oxygen LJ sigma=0.316557 nm, epsilon=0.650194 kJ/mol, SIM-01 topology: 510 SOL molecules, Unresolved SIM-02 molecule count from gmx solvate, SIM-02 draft topology: SOL molecule count remains __N_SOL_TBD__

### Community 9 - "Density temperature data parsing"
Cohesion: 0.40
Nodes (5): SIM-02 configured NEMD production: provisional 1.5 ns, 2 fs timestep, 0.5 ps trajectory cadence, Intended NEMD observables: T(z), rho(z), Pz(z), SIM-02 configured NEMD startup: provisional 500 ps, 2 fs timestep, no pressure coupling, DECISION-003 reference in NEMD startup comments, make_spatial_groups.md reference for spatial thermostat groups

## Ambiguous Edges - Review These
- `SIM-02 two-region thermostat NEMD draft design` → `SIM-02 scope: thermal-gradient NEMD and spatial polarization evidence`  [AMBIGUOUS]
  research/decisions/DECISION-003-SIM-02-NEMD-design.md · relation: conceptually_related_to

## Knowledge Gaps
- **47 isolated node(s):** `Pinned Graphify dependency: graphifyy 0.9.72`, `MDAnalysis 2.10.0`, `NumPy 2.5.3`, `pandas 3.0.6`, `SciPy 1.18.1` (+42 more)
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 76 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **3 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **What is the exact relationship between `SIM-02 two-region thermostat NEMD draft design` and `SIM-02 scope: thermal-gradient NEMD and spatial polarization evidence`?**
  _Edge tagged AMBIGUOUS (relation: conceptually_related_to) - confidence is low._
- **Why does `SIM-02 two-region thermostat NEMD draft design` connect `Polarization observables and hypotheses` to `SPC/E topology and molecule count`?**
  _High betweenness centrality (0.078) - this node is a cross-community bridge._
- **Why does `Supplied SIM-02 Claude prompt: reference proposal and workflow, not present authorization` connect `Polarization observables and hypotheses` to `Project handoff and retrieval`?**
  _High betweenness centrality (0.067) - this node is a cross-community bridge._
- **Why does `SIM-02 chronological academic narrative` connect `SPC/E topology and molecule count` to `NEMD design and literature`?**
  _High betweenness centrality (0.064) - this node is a cross-community bridge._
- **What connects `Pinned Graphify dependency: graphifyy 0.9.72`, `MDAnalysis 2.10.0`, `NumPy 2.5.3` to the rest of the system?**
  _47 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `Validation and historical decisions` be split into smaller, more focused modules?**
  _Cohesion score 0.13438735177865613 - nodes in this community are weakly interconnected._
- **Should `Analysis code dependencies` be split into smaller, more focused modules?**
  _Cohesion score 0.09523809523809523 - nodes in this community are weakly interconnected._