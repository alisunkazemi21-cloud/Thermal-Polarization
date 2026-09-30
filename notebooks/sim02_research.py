import marimo

__generated_with = "0.24.2"
app = marimo.App(width="medium")


@app.cell
def _():
    import json
    import marimo as mo
    from pathlib import Path

    return Path, json, mo


@app.cell
def _(mo):
    mo.md(
        r"""
        # SIM-02 — Thermal-gradient NEMD research record

        **Status: checkpoint 07 approved. Gate 1 structure and LAMMPS zero-step
        audits passed. No NEMD trajectory or polarization result exists yet.**

        This notebook is the executable companion to the SIM-02 research book.
        It keeps the chronological record, decisions, expected evidence, and later
        analysis in one place. Values marked **proposed** are not approved inputs;
        values marked **measured** must be traceable to preserved output.
        """
    )
    return


@app.cell
def _(mo):
    timeline = [
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
                "date": "2026-09-30",
                "stage": "Temperature decision",
                "event": "The 400 K validation → 300 K target sequence was approved.",
                "evidence": "DECISION-006",
            },
            {
                "date": "2026-09-30",
                "stage": "Source audit",
                "event": "The 2016 paper and author package fixed the benchmark geometry, reservoirs, heat rate, and reference duration.",
                "evidence": "Wirnsberger reproduction notes",
            },
            {
                "date": "current",
                "stage": "Protocol decision",
                "event": "Checkpoint 07 exact benchmark and staged release gates were approved.",
                "evidence": "DECISION-007",
            },
            {
                "date": "2026-09-30",
                "stage": "Gate 1",
                "event": "The independent structure audit and LAMMPS run 0 passed without advancing the trajectory.",
                "evidence": "measured zero-step audit",
            },
            {
                "date": "future",
                "stage": "Pilot and production",
                "event": "Execution begins only after inputs and acceptance criteria are approved.",
                "evidence": "to test",
            },
        ]
    mo.ui.table(timeline)
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
def _(mo):
    method_comparison = [
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
    mo.ui.table(method_comparison)
    return (method_comparison,)


@app.cell
def _(mo):
    design_register = [
        {"item": "engine", "value": "LAMMPS eHEX", "status": "approved", "basis": "DECISION-005"},
        {"item": "water model", "value": "rigid SPC/E", "status": "approved project model", "basis": "SIM-01 / model files"},
        {"item": "temperature path", "value": "400 K benchmark, then 300 K target", "status": "approved", "basis": "DECISION-006"},
        {"item": "benchmark system", "value": "4,500 waters; 36.35343 × 36.35343 × 109.06058 Å³", "status": "approved; gate 1 passed", "basis": "DECISION-007 / audit"},
        {"item": "time step", "value": "1 fs pilot; test 2 fs", "status": "proposed", "basis": "published production used 2 fs"},
        {"item": "reservoirs", "value": "hot: edge 4+4 Å; cold: central 8 Å", "status": "approved; syntax passed", "basis": "DECISION-007 / run 0"},
        {"item": "profile acquisition", "value": "120 bins; Δz = 0.9088 Å", "status": "published / proposed", "basis": "merge for reported views"},
        {"item": "heat rate", "value": "±0.1614 kcal mol⁻¹ fs⁻¹", "status": "approved; not yet applied", "basis": "4.243 × 10¹⁰ W m⁻² per branch"},
        {"item": "pilot duration", "value": "100 ps smoke test, then 1 ns stationarity", "status": "proposed", "basis": "checkpoint 07"},
        {"item": "published reference", "value": "10 ns transient + 60 ns production", "status": "established", "basis": "not yet authorized for execution"},
        {"item": "replicates", "value": "independent seed before reproducible positive claim", "status": "proposed", "basis": "checkpoint 07"},
    ]
    mo.ui.table(design_register)
    return (design_register,)


@app.cell
def _(mo):
    exchange_kcal_mol_fs = 0.1614
    lx_angstrom = 36.3534308725
    watts = exchange_kcal_mol_fs * 4184 / 6.02214076e23 / 1e-15
    area_m2 = (lx_angstrom * 1e-10) ** 2
    branch_flux_w_m2 = watts / (2 * area_m2)
    benchmark_calculation = [
        {"quantity": "exchange power", "value": watts, "unit": "W", "derivation": "converted from author input"},
        {"quantity": "transverse area", "value": area_m2, "unit": "m²", "derivation": "published box"},
        {"quantity": "heat flux per branch", "value": branch_flux_w_m2, "unit": "W m⁻²", "derivation": "F / (2 A)"},
    ]
    mo.ui.table(benchmark_calculation)
    return (benchmark_calculation,)


@app.cell
def _(Path, mo):
    repo_root = Path(__file__).resolve().parents[1]
    expected_paths = [
        ("LAMMPS zero-step input", "simulations/SIM-02/lammps/in.zero-step"),
        ("zero-step audit", "results/reports/SIM-02-checkpoint-07-zero-step.md"),
        ("run metadata", "results/raw/SIM-02/run-metadata.json"),
        ("temperature profile", "results/tables/SIM-02-temperature-profile.csv"),
        ("energy audit", "results/tables/SIM-02-energy-audit.csv"),
        ("production report", "results/reports/SIM-02-report.md"),
    ]
    evidence_registry = [
        {
            "artifact": label,
            "path": path,
            "state":
                "present" if (repo_root / path).exists() else "missing / not yet produced"
        }
        for label, path in expected_paths
    ]
    mo.ui.table(evidence_registry)
    return evidence_registry, repo_root


@app.cell
def _(json, mo, repo_root):
    structural = json.loads(
        (repo_root / "results/raw/SIM-02/checkpoint-07-zero-step/structural-audit.json").read_text()
    )
    lammps_audit = json.loads(
        (repo_root / "results/raw/SIM-02/checkpoint-07-zero-step/lammps-zero-step.json").read_text()
    )
    gate_1_results = [
        {"measurement": "gate outcome", "value": "PASS", "evidence": "two independent audit records"},
        {"measurement": "molecules / atoms", "value": "4,500 / 13,500", "evidence": "data parse + LAMMPS"},
        {"measurement": "density", "value": f"{structural['observations']['density_kg_m3']:.6f} kg m⁻³", "evidence": "count, mass, and box"},
        {"measurement": "reservoir COM counts", "value": str(structural['observations']['reservoir_molecule_counts_by_com']), "evidence": "independent geometry audit"},
        {"measurement": "PPPM relative accuracy", "value": f"{lammps_audit['observations']['pppm_relative_force_accuracy']:.7g}", "evidence": "LAMMPS initialization"},
        {"measurement": "diagnostic temperature", "value": f"{lammps_audit['observations']['temperature_K']:.5f} K", "evidence": "step 0; not equilibrium acceptance"},
        {"measurement": "trajectory steps", "value": "0", "evidence": "LAMMPS log"},
    ]
    mo.ui.table(gate_1_results)
    return (gate_1_results,)


@app.cell
def _(mo):
    mo.md(
        r"""
        ## Checkpoint 07 release gates

        1. **PASS — build and zero-step audit:** count, box, neutrality,
           geometry, regions, RATTLE, eHEX syntax, and PPPM initialization.
        2. Equilibrium bridge: NVE temperature, density, O–O structure,
           constraints, and energy behavior.
        3. 100 ps eHEX smoke test at 1 fs: energy ledger, occupancy, profile
           direction, and absence of cavitation.
        4. Matched 1 fs versus 2 fs test from the same prepared state.
        5. 1 ns stationarity pilot with unfolded branches and block evolution.
        6. Production release only when those records justify the allocation;
           an independent seed is required before a positive reproducibility claim.

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
        - Checkpoint 07: `{repo_root / 'research' / 'designs' / 'SIM-02-checkpoint-07-protocol-freeze.md'}`
        - Protocol decision: `{repo_root / 'research' / 'decisions' / 'DECISION-007-SIM-02-protocol-freeze.md'}`
        - Gate 1 report: `{repo_root / 'results' / 'reports' / 'SIM-02-checkpoint-07-zero-step.md'}`
        - Published benchmark audit: `{repo_root / 'research' / 'literature' / 'Wirnsberger-2016-reproduction-notes.md'}`
        - Academic narrative: `{repo_root / 'research' / 'book' / 'SIM-02.md'}`
        - Technical report: `{repo_root / 'results' / 'reports' / 'SIM-02-report.md'}`
        - Long-form video treatment: `{repo_root / 'research' / 'media' / 'SIM-02-longform-youtube.md'}`
        """
    )
    return


if __name__ == "__main__":
    app.run()
