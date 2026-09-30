# Graphify navigation

From the repository root in PowerShell:

```powershell
./scripts/graphify.ps1 query "SIM-02" --budget 1500
./scripts/graphify.ps1 explain "SPC/E"
./scripts/graphify.ps1 path "SIM-01" "SIM-02"
```

Open `graph.html` for interactive navigation. Use `graph.json` through the CLI;
avoid loading it wholesale into a chat. `GRAPH_REPORT.md` describes the graph.

Graphify 0.9.72 is installed in the ignored project `.venv`. Recreate that
environment with Python 3.12 and `pip install -r environment/requirements-graphify.txt`.
The wrapper avoids relying on a global Graphify installation or shell activation.

## Coverage and updates

The first build indexes research Markdown/text, Python/PowerShell code, and
explicitly adds GROMACS `.mdp`, `.top`, `.itp` files as semantic documents.
Graphify's default detector leaves those simulation extensions unclassified.
Preserve this extra inclusion when rebuilding; do not equate AST-only updates
with refreshed simulation parameters. `.graphifyignore` excludes generated site
assets, duplicate exports, numerical datasets, figures, and binary trajectories.
The graph's evidence links do not independently validate scientific claims.
Empty placeholder documents carry no substantive extracted claims.

For a full or semantic refresh, follow `.claude/skills/graphify/SKILL.md` and add
the three simulation extensions above to the detected document list before
extraction. Use the cache, re-extract changed notes/inputs, then regenerate the
graph, report, and HTML. `./scripts/graphify.ps1 update .` refreshes code only.

Agent extraction token usage is unavailable in this session. Placeholder counters
in extraction JSON are not actual measured zero usage. Any benchmark describes
estimated retrieval context sizes, not billing or whole-chat token savings.
