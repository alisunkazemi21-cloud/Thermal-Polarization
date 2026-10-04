# Thermal Polarization

Computational study of whether a controlled thermal gradient can create a
statistically resolved polarization in a bulk polar liquid.

Project tags: `SIM-02` · `graphify` · `token-reduction`

## Scientific question

The full causal chain is

\[
\nabla T \rightarrow J_q \rightarrow P \rightarrow E \rightarrow V_{OC}
\rightarrow I \rightarrow P_{out}.
\]

The active study, SIM-02, addresses only
\(\nabla T \rightarrow J_q \rightarrow P\). It does not claim voltage,
current, or electrical power.

## Official simulation chronology

| Stage | Purpose | Status |
|---|---|---|
| SIM-01 | Validate equilibrium SPC/E water | Completed; five recorded checks passed |
| SIM-02 | Impose a thermal gradient and measure heat transport, orientation, and polarization | Checkpoint 12: the four-rank same-restart path crossed the COM ceiling 7 fs into NVE with per-step sampling; mechanism unresolved; full bridge held. A matched one-rank high-cadence control is proposed in DECISION-013 and awaits approval |
| SIM-03 | Evaluate the electrostatic/electrical consequences only after a validated SIM-02 signal | Not started |

Earlier files that used different stage names are historical records. The table
above is the official terminology from 2026-09-30 onward.

## Current decision

The initial SIM-02 draft used GROMACS `tc-grps` built from initial spatial
selections. Those are fixed atom groups and do not remain spatial reservoirs as
liquid water diffuses. The draft is preserved, marked non-runnable, and
superseded by the decision to use LAMMPS's dynamic-region eHEX implementation.

See:

- [current project state](PROJECT_STATE.md)
- [SIM-02 method audit](research/decisions/DECISION-004-SIM-02-method-audit.md)
- [LAMMPS eHEX selection](research/decisions/DECISION-005-SIM-02-LAMMPS-eHEX.md)
- [400 K → 300 K validation sequence](research/decisions/DECISION-006-SIM-02-temperature-path.md)
- [proposed eHEX design](research/designs/SIM-02-LAMMPS-eHEX-design.md)
- [checkpoint 08 equilibrium bridge](research/designs/SIM-02-checkpoint-08-equilibrium-bridge.md)
- [checkpoint 08 approval](research/decisions/DECISION-008-SIM-02-equilibrium-bridge.md)
- [checkpoint 08 Stage-A failure report](results/reports/SIM-02-checkpoint-08-stage-a-com-drift.md)
- [checkpoint 09 momentum-control proposal](research/designs/SIM-02-checkpoint-09-preparation-momentum-control.md)
- [checkpoint 09 approval](research/decisions/DECISION-009-SIM-02-preparation-momentum-control.md)
- [checkpoint 09 diagnostic results](results/reports/SIM-02-checkpoint-09-diagnostics.md)
- [checkpoint 10 one-rank NVE report](results/reports/SIM-02-checkpoint-10-one-rank-nve.md)
- [checkpoint 10 NVE COM-drift review](research/decisions/DECISION-010-SIM-02-NVE-COM-drift-review.md)
- [checkpoint 11 same-restart diagnostic](results/reports/SIM-02-checkpoint-11-same-restart-one-rank.md)
- [checkpoint 11 approval and result](research/decisions/DECISION-011-SIM-02-same-restart-rank-diagnostic.md)
- [checkpoint 12 high-cadence diagnostic](results/reports/SIM-02-checkpoint-12-four-rank-high-cadence.md)
- [checkpoint 12 approval and result](research/decisions/DECISION-012-SIM-02-four-rank-high-cadence-diagnostic.md)
- [proposed checkpoint 13 one-rank high-cadence control](research/decisions/DECISION-013-SIM-02-one-rank-high-cadence-control-proposal.md)

## Research workflow

Each stage follows the same evidence-preserving sequence:

1. Review repository evidence and relevant literature.
2. Discuss scientific choices and unresolved risks.
3. Record the decision and its alternatives before execution.
4. Implement traceable inputs and validation checks.
5. Run short checkpoints before long production.
6. Analyze stationarity and uncertainty before interpretation.
7. Synchronize the run README, Marimo notebook, research-book chapter,
   technical report, and media narrative.

The detailed rules are in [research/WORKFLOW.md](research/WORKFLOW.md).

## Evidence labels

- `[ESTABLISHED]`: supported by a source or direct environment inspection.
- `[MEASURED]`: calculated from recorded project output.
- `[INFERRED]`: interpretation supported by evidence but not directly measured.
- `[HYPOTHESIS]`: proposed physical explanation.
- `[OPEN]`: unresolved question.
- `[TO TEST]`: planned test with no result yet.

No value becomes a project result because it appears in a draft, notebook cell,
plot, or narration. Results must trace to preserved output and analysis code.

## Living records

| Artifact | Role |
|---|---|
| `simulations/SIM-02/README.md` | Exact run procedure and checkpoint status |
| `notebooks/sim02_research.py` | Executable Marimo analysis and interactive evidence |
| `research/book/SIM-02.md` | Academic narrative and chronological interpretation |
| `results/reports/SIM-02-report.md` | Frozen technical report for measured results |
| `research/media/SIM-02-longform-youtube.md` | Long-form video story tied to real evidence |
| `research/decisions/` | Decisions, rejected alternatives, and supersession history |
| `history/` | Failed runs and technical investigations |

## Repository map

```text
models/                 molecular models and parameter provenance
simulations/            engine inputs and reproducible run instructions
scripts/                build, analysis, validation, and visualization tools
data/raw/               preserved raw non-trajectory inputs/exports
data/processed/         derived analysis tables
results/figures/        generated scientific figures
results/tables/         compact numerical results
results/reports/        technical reports
notebooks/              executable Marimo research notebooks
research/book/          academic narrative and chronology
research/decisions/     decision records
research/literature/    literature evidence notes
research/media/         documentary and YouTube planning
graphify-out/           queryable project knowledge graph
```

For compact navigation, open the [interactive Graphify map](docs/project-graph.html)
in a browser, or query the graph locally:

```powershell
./scripts/graphify.ps1 query "SIM-02" --budget 1500
```
