import marimo

__generated_with = "0.24.2"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    import pandas as pd
    from pathlib import Path

    return Path, mo, pd


@app.cell
def _(mo):
    mo.md(
        r"""
        # SIM-02 — Thermal-gradient NEMD research record

        **Status: design discussion. No SIM-02 trajectory or measured result exists yet.**

        This notebook is the executable companion to the SIM-02 research book.
        It keeps the chronological record, decisions, expected evidence, and later
        analysis in one place. Values marked **proposed** are not approved inputs;
        values marked **measured** must be traceable to preserved output.
        """
    )
    return


@app.cell
def _(pd):
    timeline = pd.DataFrame(
        [
            {
                "date": "before 2026-09-30",
                "stage": "Inherited draft",
                "event": "A GROMACS Hot/Cold/Rest thermostat design was drafted.",
                "evidence": "historical draft",
            },
            {
                "date": "2026-09-30",
                "stage": "Method audit",
                "event": "Static atom groups were rejected as spatial reservoirs for diffusing water.",
                "evidence": "DECISION-004",
            },
            {
                "date": "2026-09-30",
                "stage": "Engine decision",
                "event": "LAMMPS eHEX was selected for dynamic spatial heat-exchange regions.",
                "evidence": "DECISION-005",
            },
            {
                "date": "current",
                "stage": "Design discussion",
                "event": "Temperature path, heat rate, box geometry, replication, and pilot gates remain open.",
                "evidence": "SIM-02 eHEX design",
            },
            {
                "date": "future",
                "stage": "Pilot and production",
                "event": "Execution begins only after inputs and acceptance criteria are approved.",
                "evidence": "to test",
            },
        ]
    )
    timeline
    return (timeline,)


@app.cell
def _(mo):
    mo.md(
        r"""
        ## Scientific chain and scope

        The long-term project asks whether a temperature gradient in water can
        create useful electrical behavior:

        $$\nabla T \rightarrow J_Q \rightarrow P(z) \rightarrow E(z)
        \rightarrow \Delta\phi \rightarrow V_\mathrm{OC}$$

        SIM-02 establishes the thermal-gradient molecular-dynamics experiment and
        its stationary spatial observables. It does **not** yet establish voltage,
        current, or extractable power.
        """
    )
    return


@app.cell
def _(pd):
    method_comparison = pd.DataFrame(
        [
            {
                "method": "GROMACS tc-grps with initial slab groups",
                "spatial membership": "fixed atom identity",
                "current status": "rejected",
                "reason": "water diffusion destroys persistent spatial reservoirs",
            },
            {
                "method": "LAMMPS fix ehex with geometric regions",
                "spatial membership": "evaluated from current position",
                "current status": "selected",
                "reason": "implements controlled heat exchange in spatial reservoirs",
            },
        ]
    )
    method_comparison
    return (method_comparison,)


@app.cell
def _(pd):
    design_register = pd.DataFrame(
        [
            ["engine", "LAMMPS eHEX", "approved", "DECISION-005"],
            ["water model", "rigid SPC/E", "approved project model", "SIM-01 / model files"],
            ["temperature path", "400 K benchmark, then 300 K target", "proposed", "design discussion"],
            ["time step", "1 fs", "proposed", "pilot validation required"],
            ["reservoir width", "4 Å at each boundary region", "proposed", "sensitivity check required"],
            ["profile bin width", "about 0.5 Å", "proposed", "occupancy check required"],
            ["production duration", "up to 10 ns in checkpoints", "proposed", "stationarity decides usable window"],
            ["heat rate", "undecided", "open", "pilot sweep required"],
            ["replicates", "undecided", "open", "uncertainty design required"],
        ],
        columns=["item", "value", "status", "basis"],
    )
    design_register
    return (design_register,)


@app.cell
def _(Path, pd):
    repo_root = Path(__file__).resolve().parents[1]
    expected_paths = [
        ("LAMMPS input", "simulations/SIM-02/lammps/in.sim02"),
        ("run metadata", "results/raw/SIM-02/run-metadata.json"),
        ("temperature profile", "results/tables/SIM-02-temperature-profile.csv"),
        ("energy audit", "results/tables/SIM-02-energy-audit.csv"),
        ("production report", "results/reports/SIM-02-report.md"),
    ]
    evidence_registry = pd.DataFrame(
        {
            "artifact": [label for label, _ in expected_paths],
            "path": [path for _, path in expected_paths],
            "state": [
                "present" if (repo_root / path).exists() else "missing / not yet produced"
                for _, path in expected_paths
            ],
        }
    )
    evidence_registry
    return evidence_registry, repo_root


@app.cell
def _(mo):
    mo.md(
        r"""
        ## Pilot acceptance gates

        1. The constructed system has the recorded molecule count, dimensions,
           mass density, and charge neutrality.
        2. Constraints remain stable and equilibrium quantities are compatible
           with the validated SIM-01 baseline at the chosen condition.
        3. The imposed hot/cold exchange is equal and opposite within documented
           numerical tolerance, with no unacceptable secular energy drift.
        4. Regional membership follows molecular position and treats each rigid
           water molecule consistently.
        5. The temperature profile becomes stationary over documented time blocks.
        6. Any reported gradient includes block uncertainty and sensitivity to
           excluded reservoir/interface bins.

        A failed gate is a recorded result. It triggers a documented change and a
        new pilot; it cannot be silently tuned away.
        """
    )
    return


@app.cell
def _(mo, repo_root):
    mo.md(
        f"""
        ## Authoritative records

        - Workflow: `{repo_root / 'research' / 'WORKFLOW.md'}`
        - Engine decision: `{repo_root / 'research' / 'decisions' / 'DECISION-005-SIM-02-LAMMPS-eHEX.md'}`
        - Design discussion: `{repo_root / 'research' / 'designs' / 'SIM-02-LAMMPS-eHEX-design.md'}`
        - Academic narrative: `{repo_root / 'research' / 'book' / 'SIM-02.md'}`
        - Technical report: `{repo_root / 'results' / 'reports' / 'SIM-02-report.md'}`
        - Long-form video treatment: `{repo_root / 'research' / 'media' / 'SIM-02-longform-youtube.md'}`
        """
    )
    return


if __name__ == "__main__":
    app.run()
