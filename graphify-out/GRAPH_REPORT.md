> Extraction token usage was not exposed by this session; any zero token counters below are placeholders, not measured zero consumption.
> Research claims are indexed from sources, not independently verified.

# Graph Report - Thermal-Polarization  (2026-10-04)

## Corpus Check
- 21 files · ~37,755 words
- Verdict: corpus is large enough that graph structure adds value.

## Summary
- 253 nodes · 260 edges · 40 communities (24 shown, 16 thin omitted)
- Extraction: 95% EXTRACTED · 5% INFERRED · 0% AMBIGUOUS · INFERRED: 14 edges (avg confidence: 0.95)
- Token cost: 0 input · 0 output

## Community Hubs (Navigation)
- Python analysis symbols
- SIM-01 history and validation
- SPC/E water model
- Python standard libraries
- Checkpoint 10 rank comparison
- SIM-02 method decisions
- Historical NEMD design
- NEMD observables and uncertainty
- Checkpoint 11 same-restart result
- Notebook environment
- Checkpoint 07 baseline
- Same-restart rank test
- NEMD production proposal
- Project guidance and Graphify
- Checkpoint 08 MPI momentum
- SIM-02 current state
- Checkpoint 08 COM failure
- SIM-02 decision boundary
- Colab compute tradeoffs
- Marimo analysis notebooks
- Research workflow and claim classes
- Checkpoint 08 approval
- Checkpoint 08 bridge protocol
- Checkpoint 09 momentum control
- Checkpoint 09 measured outcomes
- Checkpoint 11 raw provenance
- Checkpoint 08 failure evidence
- Checkpoint 10 replay comparison
- Wirnsberger replication source
- Evidence-first project lifecycle
- Checkpoint 08 zero-step audit
- Timestep comparison
- Colab hardware and runtime
- YouTube research roadmap
- Checkpoint 10 one-rank record
- Checkpoint 10 run limitation
- DECISION-009 momentum scope
- LAMMPS method translation

## God Nodes (most connected - your core abstractions)
1. `SIM-01 validation report: five criteria reported passing; not independently rerun in this extraction` - 14 edges
2. `Research question: reproducible spatial polarization under a controlled thermal gradient` - 12 edges
3. `SETTLE rigid water geometry: OH=0.1000 nm, HH=0.16330 nm` - 7 edges
4. `SIM-02 two-region thermostat NEMD draft design` - 7 edges
5. `Supplied SIM-02 Claude prompt: reference proposal and workflow, not present authorization` - 7 edges
6. `Pinned Python analysis and notebook environment` - 7 edges
7. `read_xvg()` - 5 edges
8. `main()` - 5 edges
9. `SPC/E rigid water topology: qO=-0.8476 e, qH=+0.4238 e; oxygen LJ sigma=0.316557 nm, epsilon=0.650194 kJ/mol` - 5 edges
10. `DECISION-005 selects LAMMPS eHEX for SIM-02` - 5 edges

## Surprising Connections (you probably didn't know these)
- `2026-09-18 grompp produced no em.tpr even after package reinstall` --conceptually_related_to--> `Later SIM-01 report attributes resolved grompp failure to __N_SOL_TBD__ molecule-count placeholder`  [INFERRED]
  history/FAILED-001-grompp-segmentation-fault.md → results/reports/SIM-01-validation.md
- `NVT diffusion continuation after NPT density/RDF production` --conceptually_related_to--> `Reported EM, 100 ps NVT, 100 ps NPT, 1 ns NPT, 1 ns supplementary NVT`  [INFERRED]
  research/decisions/DECISION-001-SIM-01-equilibrium-validation.md → results/reports/SIM-01-validation.md
- `SIM-01 validation report: five criteria reported passing; not independently rerun in this extraction` --references--> `DECISION-001 supplementary fixed-volume NVT diffusion leg (historical approval; date placeholder)`  [EXTRACTED]
  results/reports/SIM-01-validation.md → research/decisions/DECISION-001-SIM-01-equilibrium-validation.md
- `Pinned Graphify dependency: graphifyy 0.9.72` --conceptually_related_to--> `Graphify query/path/explain and AST update workflow`  [INFERRED]
  environment/requirements-graphify.txt → CLAUDE.md
- `SIM-01 topology: 510 SOL molecules` --references--> `SPC/E rigid water topology: qO=-0.8476 e, qH=+0.4238 e; oxygen LJ sigma=0.316557 nm, epsilon=0.650194 kJ/mol`  [EXTRACTED]
  simulations/SIM-01/topol.top → models/SPC-E/spce.itp

## Import Cycles
- None detected.

## Hyperedges (group relationships)
- **Proposed joint NEMD stationarity and uncertainty assessment** — research_prompts_sim_02_claude_prompt_temperature_profile, research_prompts_sim_02_claude_prompt_density_profile, research_prompts_sim_02_claude_prompt_polarization_profile, research_prompts_sim_02_claude_prompt_orientation, research_prompts_sim_02_claude_prompt_heat_flux, research_prompts_sim_02_claude_prompt_block_uncertainty [EXTRACTED 1.00]

## Communities (40 total, 16 thin omitted)

### Community 1 - "SIM-01 history and validation"
Cohesion: 0.10
Nodes (21): FAILED-001 historical preprocessing segfault; unresolved in this dated record, 2026-09-18 grompp produced no em.tpr even after package reinstall, DECISION-001 supplementary fixed-volume NVT diffusion leg (historical approval; date placeholder), DECISION-002: diffusion periodic-boundary correction (2026-09-19 record), Planned documentary research series: six baseline episodes and future NEMD/electrical episodes, RDF literature lead arXiv:1706.05491, RDF literature lead arXiv:1806.09956, RDF literature lead arXiv:1809.04996 (+13 more)

### Community 2 - "SPC/E water model"
Cohesion: 0.10
Nodes (20): Berendsen, Grigera, Straatsma (1987), The missing term in effective pair potentials, J. Phys. Chem. 91, 6269-6271, SPC/E rigid water topology: qO=-0.8476 e, qH=+0.4238 e; oxygen LJ sigma=0.316557 nm, epsilon=0.650194 kJ/mol, SIM-01 configured steepest-descent minimization: max 50000 steps, emtol=1000 kJ/mol/nm, PME, Verlet, 1.0 nm cutoffs, xyz PBC, EnerPres dispersion correction, h-bonds/LINCS, SIM-01 configured NPT production: 1 ns, 300 K, 1 bar, 2 fs timestep, 1 ps trajectory cadence, SIM-01 supplementary NVT diffusion configuration: 1 ns, 300 K, fixed volume, 1 ps trajectory cadence, SIM-01 intended density, O-O RDF, self-diffusion validation targets, SIM-01 configured NPT equilibration: provisional 100 ps, 300 K, 1 bar (+12 more)

### Community 3 - "Python standard libraries"
Cohesion: 0.14
Nodes (9): audit(), main(), minimum_image(), nearest_oxygen_distance(), parse_args(), parse_data(), write_report(), main() (+1 more)

### Community 4 - "Checkpoint 10 rank comparison"
Cohesion: 0.14
Nodes (14): Frozen center-of-mass speed ceiling (1e-6 Å/fs), Four-rank NVE result: first ceiling exceedance at 100 fs, One-rank uncorrected NVE result: 2 ps, no ceiling exceedance, SIM-02 checkpoint 10 — one-rank NVE diagnostic, Fixed checkpoint-09 Stage-B restart, Rank-count-sensitive Stage-C/NVE sequence, SIM-02 checkpoint 11 — same-restart one-rank diagnostic, Research question: signed polarization profile in bulk SPC/E water under heat flux (+6 more)

### Community 5 - "SIM-02 method decisions"
Cohesion: 0.17
Nodes (13): DECISION-005 selects LAMMPS eHEX for SIM-02, Local LAMMPS build provides eHEX rigid SHAKE RATTLE and PPPM, DECISION-006 approves 400 K validation before 300 K target, DECISION-007 approves the exact 400 K benchmark and staged release gates, Wirnsberger 2016 author-package reproduction notes, SIM-02 checkpoint 07 exact benchmark and staged pilot proposal, SIM-02 LAMMPS eHEX design discussion, Gate 1 measured 4500 neutral waters, reservoir occupancy, RATTLE and PPPM initialization with zero steps (+5 more)

### Community 6 - "Historical NEMD design"
Cohesion: 0.15
Nodes (8): DECISION-003 SIM-02 NEMD design, historical approval claim; date placeholder, SIM-02 two-region thermostat NEMD draft design, Armstrong et al. 2013: Heat Flux and Dipole Moment Dynamic Correlations (unverified literature lead), Armstrong and Bresme 2015: Temperature Inversion of Thermal Polarization of Water (unverified literature lead), Bedeaux et al. 2025: Theory of Thermopolarization Effect (unverified literature lead), Bresme et al. 2008: Water Polarization under Thermal Gradients (unverified literature lead), Supplied SIM-02 Claude prompt: reference proposal and workflow, not present authorization, Lervik et al. 2022: molecular dipole and quadrupole moments (unverified literature lead)

### Community 7 - "NEMD observables and uncertainty"
Cohesion: 0.17
Nodes (5): H4 coupled mechanism (hypothesis), H1 density coupling (hypothesis), H3 molecular dynamics/heat-flux coupling (hypothesis), H2 local structure/hydrogen-bond coupling (hypothesis), Research question: reproducible spatial polarization under a controlled thermal gradient

### Community 8 - "Checkpoint 11 same-restart result"
Cohesion: 0.25
Nodes (8): Checkpoint 11 same-restart comparison, Four-rank same-restart path breached COM ceiling at 100 fs, Mechanism of rank-sensitive behavior unresolved, One-rank Stage-C/NVE completed 2 ps, Rank-count-sensitive behavior in Stage-C/NVE sequence, Same-restart rank comparison follow-up, Checkpoint 11 same-restart rank comparison story, Rank count is controlled for Stage C/NVE; mechanism remains unresolved

### Community 9 - "Notebook environment"
Cohesion: 0.25
Nodes (8): Pinned Python analysis and notebook environment, Jupyter 1.1.1, marimo 0.24.2 (duplicate requirement), Matplotlib 3.11.2, MDAnalysis 2.10.0, NumPy 2.5.3, pandas 3.0.6, SciPy 1.18.1

### Community 10 - "Checkpoint 07 baseline"
Cohesion: 0.25
Nodes (8): SIM-02 checkpoint 07, data.spce-4500.ness-ewald, Ewald 1e-5 long-range solver, Gate 1 zero-step audit, Hot and cold reservoirs, PPPM 1e-5 long-range solver, Rigid SPC/E model, Author-supplied steady-state Ewald configuration

### Community 11 - "Same-restart rank test"
Cohesion: 0.33
Nodes (3): Center-of-Mass Speed Ceiling, Checkpoint 10 Independent Stage-B Replay, Rank-Count-Sensitive Numerical Behavior

### Community 12 - "NEMD production proposal"
Cohesion: 0.40
Nodes (5): SIM-02 configured NEMD production: provisional 1.5 ns, 2 fs timestep, 0.5 ps trajectory cadence, Intended NEMD observables: T(z), rho(z), Pz(z), SIM-02 configured NEMD startup: provisional 500 ps, 2 fs timestep, no pressure coupling, DECISION-003 reference in NEMD startup comments, make_spatial_groups.md reference for spatial thermostat groups

### Community 13 - "Project guidance and Graphify"
Cohesion: 0.50
Nodes (3): Project guidance: SIM-02, graphify, token-reduction, Graphify bounded retrieval guidance, Pinned Graphify dependency: graphifyy 0.9.72

### Community 14 - "Checkpoint 08 MPI momentum"
Cohesion: 0.40
Nodes (4): Corrected MPI Dry-Run Output, MPI RATTLE COM-Velocity Floor, Checkpoint 08 MPI Momentum Initialization Record, Initial MPI Momentum Run Output

### Community 15 - "SIM-02 current state"
Cohesion: 0.40
Nodes (5): Checkpoint 11 same-restart diagnostic, Full equilibrium bridge remains on hold, No equilibrium or polarization result claimed, Rank-count-sensitive Stage-C/NVE behavior, Official simulation chronology

### Community 16 - "Checkpoint 08 COM failure"
Cohesion: 0.50
Nodes (4): Checkpoint 08 Frozen COM Criterion Failure, Checkpoint 08 Stage-A LAMMPS Log, Checkpoint 08 Stage-A COM-Drift Record, Checkpoint 08 Stage-A Standard Output

### Community 17 - "SIM-02 decision boundary"
Cohesion: 0.50
Nodes (4): SIM-02 scope: gradient to heat flux to polarization, Full equilibrium bridge on hold, Full bridge remains on hold, Full bridge remains on hold with no equilibrium or polarization claim

### Community 18 - "Colab compute tradeoffs"
Cohesion: 0.50
Nodes (3): LAMMPS Checkpoint 07 run 0, Imported 4,500-Molecule SPC/E Structure, Checkpoint 07 Structural Audit Pass

### Community 20 - "Marimo analysis notebooks"
Cohesion: 0.67
Nodes (3): Evidence classification labels, Research Book, Evidence-Preserving Research Workflow

### Community 21 - "Research workflow and claim classes"
Cohesion: 0.67
Nodes (3): DECISION-008 Equilibrium Bridge Approval, Fixed-Volume 400 K PPPM Equilibrium Bridge, Unreported NpT Pressure Boundary

### Community 22 - "Checkpoint 08 approval"
Cohesion: 0.67
Nodes (3): Checkpoint 08 Equilibrium Bridge Design, Four-Stage Fixed-Volume Bridge Protocol, Frozen Gate 2 Acceptance Criteria

### Community 23 - "Checkpoint 08 bridge protocol"
Cohesion: 1.00
Nodes (3): Checkpoint 09 Preparation Momentum-Control Design, Preparation-Only Momentum Removal, Uncorrected NVE COM-Ceiling Failure

### Community 25 - "Checkpoint 09 measured outcomes"
Cohesion: 0.67
Nodes (3): Bounded implementation diagnostic, not equilibrium or polarization, Checkpoint 11 raw diagnostic archive, Byte-identical four-rank checkpoint-09 Stage-B restart

### Community 26 - "Checkpoint 11 raw provenance"
Cohesion: 0.67
Nodes (3): Measured COM speeds: 1.02778929e-5 Å/fs at 1 ps and 1.25105105e-5 Å/fs at 2 ps, Checkpoint 08 stopped before NVT and NVE; no equilibrium, eHEX, or polarization result exists, SIM-02 gate 2 failed at 2 ps: Stage-A COM speed exceeded the frozen ceiling

## Knowledge Gaps
- **100 isolated node(s):** `Measured COM speeds: 1.02778929e-5 Å/fs at 1 ps and 1.25105105e-5 Å/fs at 2 ps`, `Checkpoint 08 stopped before NVT and NVE; no equilibrium, eHEX, or polarization result exists`, `DECISION-009 approved momentum removal only during Stage-A/B preparation; no periodic correction in NVE`, `Wirnsberger 2016 author-package reproduction notes`, `SIM-01 report actual commands section empty` (+95 more)
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 144 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **16 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `Research question: reproducible spatial polarization under a controlled thermal gradient` connect `NEMD observables and uncertainty` to `Historical NEMD design`?**
  _High betweenness centrality (0.006) - this node is a cross-community bridge._
- **Are the 6 inferred relationships involving `SETTLE rigid water geometry: OH=0.1000 nm, HH=0.16330 nm` (e.g. with `SIM-01 configured steepest-descent minimization: max 50000 steps, emtol=1000 kJ/mol/nm` and `SIM-01 configured NPT equilibration: provisional 100 ps, 300 K, 1 bar`) actually correct?**
  _`SETTLE rigid water geometry: OH=0.1000 nm, HH=0.16330 nm` has 6 INFERRED edges - model-reasoned connections that need verification._
- **What connects `Measured COM speeds: 1.02778929e-5 Å/fs at 1 ps and 1.25105105e-5 Å/fs at 2 ps`, `Checkpoint 08 stopped before NVT and NVE; no equilibrium, eHEX, or polarization result exists`, `DECISION-009 approved momentum removal only during Stage-A/B preparation; no periodic correction in NVE` to the rest of the system?**
  _100 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `Python analysis symbols` be split into smaller, more focused modules?**
  _Cohesion score 0.13438735177865613 - nodes in this community are weakly interconnected._
- **Should `SIM-01 history and validation` be split into smaller, more focused modules?**
  _Cohesion score 0.10276679841897234 - nodes in this community are weakly interconnected._
- **Should `SPC/E water model` be split into smaller, more focused modules?**
  _Cohesion score 0.10276679841897234 - nodes in this community are weakly interconnected._
- **Should `Python standard libraries` be split into smaller, more focused modules?**
  _Cohesion score 0.14285714285714285 - nodes in this community are weakly interconnected._