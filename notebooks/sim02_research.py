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
    mo.md(r"""
    # SIM-02 — Thermal-gradient NEMD research record

    **Status: checkpoint 07 gate 1 passed; checkpoint 08 failed Stage A. The
    checkpoint 09 four-rank NVE path breached the frozen COM ceiling at 100 fs.
    Checkpoint 11 repeated Stage C/NVE at one rank from that exact four-rank
    Stage-B restart and completed 2 ps below the ceiling. Checkpoint 12
    replayed four-rank Stage C/NVE with per-step sampling and halted at the
    first COM-ceiling crossing, 7 fs after the NVE start. DECISION-013's matched
    one-rank control completed 400 fs with maximum COM 9.65e-19 Å/fs. Together,
    the traces support rank-count-sensitive behavior in this saved-state
    sequence; the cause remains unresolved. Checkpoint 13 closes this
    diagnostic branch. DECISION-014 authorizes one conditional final-results
    campaign, with the existing bridge, eHEX, stationarity, and production gates
    acting as automatic stop/proceed rules. Resource and restart-continuity
    preflight comes first; no equilibrium or polarization result exists yet.**

    This notebook is the executable companion to the SIM-02 research book.
    It keeps the chronological record, decisions, expected evidence, and later
    analysis in one place. Values marked **proposed** are not approved inputs;
    values marked **measured** must be traceable to preserved output.
    """)
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
                "date": "2026-10-01",
                "stage": "Checkpoint 08",
                "event": "The fixed-volume PPPM equilibrium bridge and acceptance tests were approved for execution.",
                "evidence": "DECISION-008; outcome not yet measured",
            },
            {
                "date": "2026-10-03",
                "stage": "Production-path check",
                "event": "The MPI RATTLE correction and 1e-6 Å/fs no-growth threshold were approved for relaunch from step zero.",
                "evidence": "measured initialization record + user approval",
            },
            {
                "date": "2026-10-03",
                "stage": "Checkpoint 08 failure",
                "event": "The four-rank OPT bridge was stopped at 2 ps when Stage-A COM speed exceeded the frozen ceiling.",
                "evidence": "measured acceptance failure",
            },
            {
                "date": "2026-10-03",
                "stage": "Checkpoint 09",
                "event": "DECISION-009 approved preparation-only momentum control; zero-step, 2 ps, and 20 ps Stage-A checks passed.",
                "evidence": "approved decision + measured implementation diagnostics",
            },
            {
                "date": "2026-10-03",
                "stage": "Checkpoint 09 NVT transition",
                "event": "The 2 ps Stage-B continuation completed; final sample was 399.81 K with COM below the frozen ceiling.",
                "evidence": "measured continuation from Stage-A restart",
            },
            {
                "date": "2026-10-03",
                "stage": "Checkpoint 09 NVE diagnostic",
                "event": "The four-rank uncorrected NVE segment crossed the 1e-6 Å/fs ceiling at 100 fs and was interrupted at 400 fs.",
                "evidence": "measured acceptance failure; full bridge held",
            },
            {
                "date": "2026-10-04",
                "stage": "Checkpoint 10 one-rank comparison",
                "event": "After replaying Stage B from the same Stage-A restart, the one-rank 2 ps uncorrected NVE segment completed with 20 samples and maximum COM 1.04e-18 Å/fs.",
                "evidence": "user-approved bounded diagnostic; DECISION-010",
            },
            {
                "date": "2026-10-04",
                "stage": "Checkpoint 11 same-restart comparison",
                "event": "From the exact four-rank Stage-B restart, the one-rank Stage-C/NVE path completed 2 ps with exit code 0 and maximum COM 1.264e-18 Å/fs; the four-rank path from that restart breached at 100 fs.",
                "evidence": "user-approved bounded diagnostic; DECISION-011",
            },
            {
                "date": "2026-10-04",
                "stage": "Checkpoint 12 four-rank high-cadence replay",
                "event": "From the same restart, four-rank COM speed rose at each of eight per-step samples and first exceeded 1e-6 Å/fs at 7 fs (1.1198277e-6 Å/fs); the run halted automatically.",
                "evidence": "user-approved bounded diagnostic; DECISION-012",
            },
            {
                "date": "2026-10-04",
                "stage": "Checkpoint 13 one-rank high-cadence control",
                "event": "The approved one-rank replay from the same restart completed all 400 fs; maximum COM was 9.653e-19 Å/fs and the 7 fs value was 2.320e-19 Å/fs.",
                "evidence": "measured result; DECISION-013",
            },
            {
                "date": "2026-10-05",
                "stage": "DECISION-014 integrated final-results campaign",
                "event": "The user approved one conditional campaign toward the final polarization result. Frozen gates stop or release later stages automatically; host/build and restart-continuity preflight comes first.",
                "evidence": "approved campaign; resource preflight authorized",
            },
        ]
    mo.ui.table(timeline)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ## Scientific chain and scope

    The long-term project asks whether a temperature gradient in water can
    create useful electrical behavior:

    $$\nabla T \rightarrow J_Q \rightarrow P(z) \rightarrow E(z)
    \rightarrow \Delta\phi \rightarrow V_\mathrm{OC}$$

    SIM-02 establishes the thermal-gradient molecular-dynamics experiment and
    its stationary spatial observables. It does **not** yet establish voltage,
    current, or extractable power.
    """)
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
    return


@app.cell
def _(mo):
    design_register = [
        {"item": "engine", "value": "LAMMPS eHEX", "status": "approved", "basis": "DECISION-005"},
        {"item": "water model", "value": "rigid SPC/E", "status": "approved project model", "basis": "SIM-01 / model files"},
        {"item": "temperature path", "value": "400 K benchmark, then 300 K target; freeze 300 K duration/replicates from pilot before launch", "status": "sequence approved; target run plan open", "basis": "DECISION-006 / DECISION-014"},
        {"item": "benchmark system", "value": "4,500 waters; 36.35343 × 36.35343 × 109.06058 Å³", "status": "approved; gate 1 passed", "basis": "DECISION-007 / audit"},
        {"item": "time step", "value": "1 fs pilot; test 2 fs", "status": "proposed", "basis": "published production used 2 fs"},
        {"item": "reservoirs", "value": "hot: edge 4+4 Å; cold: central 8 Å", "status": "approved; syntax passed", "basis": "DECISION-007 / run 0"},
        {"item": "profile acquisition", "value": "120 bins; Δz = 0.9088 Å", "status": "published / proposed", "basis": "merge for reported views"},
        {"item": "heat rate", "value": "±0.1614 kcal mol⁻¹ fs⁻¹", "status": "approved; not yet applied", "basis": "4.243 × 10¹⁰ W m⁻² per branch"},
        {"item": "pilot duration", "value": "100 ps smoke test, then 1 ns stationarity", "status": "proposed", "basis": "checkpoint 07"},
        {"item": "published reference", "value": "10 ns transient + 60 ns production", "status": "established", "basis": "not yet authorized for execution"},
        {"item": "replicates", "value": "independent seed before reproducible positive claim", "status": "proposed", "basis": "checkpoint 07"},
        {"item": "equilibrium bridge", "value": "20 ps rescale + 500 ps NVT + 1 ns NVE at 1 fs", "status": "failed at 2 ps; revision required", "basis": "Stage-A COM speed exceeded frozen ceiling"},
        {"item": "preparation momentum control", "value": "every 100 steps with kinetic-energy rescaling in Stages A/B; off before NVE", "status": "approved; Stage A/B checks passed", "basis": "DECISION-009"},
    ]
    mo.ui.table(design_register)
    return


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
    return


@app.cell
def _(Path, mo):
    repo_root = Path(__file__).resolve().parents[1]
    expected_paths = [
        ("LAMMPS zero-step input", "simulations/SIM-02/lammps/in.zero-step"),
        ("zero-step audit", "results/reports/SIM-02-checkpoint-07-zero-step.md"),
        ("equilibrium-bridge input", "simulations/SIM-02/lammps/in.equilibrium-bridge"),
        ("checkpoint-08 proposal", "research/designs/SIM-02-checkpoint-08-equilibrium-bridge.md"),
        ("checkpoint-08 zero-step parse", "results/raw/SIM-02/checkpoint-08-equilibrium/dry-run-log.lammps"),
        ("checkpoint-08 run-start metadata", "results/raw/SIM-02/checkpoint-08-equilibrium/run-start.json"),
        ("checkpoint-08 Stage-A failure report", "results/reports/SIM-02-checkpoint-08-stage-a-com-drift.md"),
        ("checkpoint-09 proposal", "research/designs/SIM-02-checkpoint-09-preparation-momentum-control.md"),
        ("checkpoint-09 approval", "research/decisions/DECISION-009-SIM-02-preparation-momentum-control.md"),
        ("checkpoint-09 diagnostic summary", "results/raw/SIM-02/checkpoint-09-diagnostics/checkpoint-09-summary.json"),
        ("checkpoint-09 diagnostic report", "results/reports/SIM-02-checkpoint-09-diagnostics.md"),
        ("checkpoint-10 review", "research/decisions/DECISION-010-SIM-02-NVE-COM-drift-review.md"),
        ("checkpoint-11 approval", "research/decisions/DECISION-011-SIM-02-same-restart-rank-diagnostic.md"),
        ("checkpoint-11 summary", "results/raw/SIM-02/checkpoint-11-same-restart-one-rank/checkpoint-11-summary.json"),
        ("checkpoint-11 report", "results/reports/SIM-02-checkpoint-11-same-restart-one-rank.md"),
        ("checkpoint-11 input", "simulations/SIM-02/lammps/in.checkpoint-11-same-restart-one-rank"),
        ("checkpoint-12 approval", "research/decisions/DECISION-012-SIM-02-four-rank-high-cadence-diagnostic.md"),
        ("checkpoint-12 summary", "results/raw/SIM-02/checkpoint-12-four-rank-high-cadence/checkpoint-12-summary.json"),
        ("checkpoint-12 report", "results/reports/SIM-02-checkpoint-12-four-rank-high-cadence.md"),
        ("checkpoint-12 input", "simulations/SIM-02/lammps/in.checkpoint-12-four-rank-high-cadence"),
        ("checkpoint-13 report", "results/reports/SIM-02-checkpoint-13-one-rank-high-cadence.md"),
        ("checkpoint-13 summary", "results/raw/SIM-02/checkpoint-13-one-rank-high-cadence/checkpoint-13-summary.json"),
        ("checkpoint-13 input", "simulations/SIM-02/lammps/in.checkpoint-13-one-rank-high-cadence"),
        ("DECISION-013 approval and outcome", "research/decisions/DECISION-013-SIM-02-one-rank-high-cadence-control-proposal.md"),
        ("DECISION-014 integrated final-results campaign", "research/decisions/DECISION-014-SIM-02-consolidated-bridge-go-no-go.md"),
        ("checkpoint-09 continuation diagnostic input", "simulations/SIM-02/lammps/in.checkpoint-09-continuation-b-nve"),
        ("checkpoint-09 Stage-C zero-step input", "simulations/SIM-02/lammps/in.checkpoint-09-stage-c-zero-step"),
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
    return (repo_root,)


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
    return


@app.cell
def _(json, mo, repo_root):
    run_start = json.loads(
        (repo_root / "results/raw/SIM-02/checkpoint-08-equilibrium/run-start.json").read_text()
    )
    init = run_start["initialization_observation"]
    records = run_start["runtime_observation"]["integrated_thermo_records"]
    gate_2_start = [
        {"field": "scientific status", "value": run_start["scientific_status"], "evidence class": "run state"},
        {"field": "commit", "value": run_start["git_commit"], "evidence class": "provenance"},
        {"field": "launch time", "value": run_start["started_at"], "evidence class": "provenance"},
        {"field": "execution", "value": "4 MPI ranks; OPT suffix", "evidence class": "measured startup"},
        {"field": "corrected step-zero COM speed", "value": f"{init['center_of_mass_speed_angstrom_per_fs']:.5g} Å/fs", "evidence class": "measured initialization"},
        {"field": "COM ceiling", "value": f"{init['approved_ceiling_angstrom_per_fs']:.1g} Å/fs", "evidence class": "approved criterion"},
        {"field": "step 1,000 COM speed", "value": f"{records[0]['center_of_mass_speed_angstrom_per_fs']:.9g} Å/fs", "evidence class": "measured failure"},
        {"field": "step 2,000 COM speed", "value": f"{records[1]['center_of_mass_speed_angstrom_per_fs']:.9g} Å/fs", "evidence class": "measured failure"},
        {"field": "checkpoint 08 outcome", "value": "FAIL — stopped during Stage A", "evidence class": "frozen criterion"},
        {"field": "checkpoint 09 zero-step", "value": "PASS", "evidence class": "production-path initialization"},
        {"field": "checkpoint 09 Stage A, 2 ps", "value": "PASS — 400 K; COM within ceiling", "evidence class": "bounded diagnostic"},
        {"field": "checkpoint 09 Stage A, 20 ps", "value": "PASS — 200 samples; max COM 9.65e-19 Å/fs", "evidence class": "bounded diagnostic"},
        {"field": "checkpoint 09 Stage B, 2 ps", "value": "PASS — endpoint 399.81 K; COM below ceiling", "evidence class": "bounded diagnostic"},
        {"field": "checkpoint 09 four-rank NVE, 0.4 ps captured", "value": "FAIL — first sample 7.14e-6 Å/fs at 100 fs", "evidence class": "frozen criterion"},
        {"field": "checkpoint 10 one-rank NVE, 2 ps", "value": "PASS — 20 samples; max COM 1.04e-18 Å/fs", "evidence class": "bounded cross-rank diagnostic"},
        {"field": "checkpoint 12 four-rank same-restart NVE", "value": "FAIL — first per-step COM ceiling crossing at 7 fs", "evidence class": "frozen criterion"},
        {"field": "checkpoint 13 one-rank same-restart NVE", "value": "PASS — 400 fs; max COM 9.65e-19 Å/fs; at 7 fs 2.32e-19 Å/fs", "evidence class": "bounded diagnostic"},
        {"field": "full gate-2 outcome", "value": "HOLD — rank-count-sensitive sequence supported; mechanism unresolved; bridge not released", "evidence class": "not released"},
    ]
    mo.vstack([
        mo.md("## Checkpoint 09 — NVE momentum gate failed"),
        mo.ui.table(gate_2_start),
        mo.md(
            "Checkpoint 08's failure remains in the chronology. DECISION-009 "
            "adds periodic momentum removal only during thermostat preparation "
            "and defines RATTLE after velocity-changing fixes. Stage A passed at "
            "2 ps and 20 ps; the 2 ps Stage-B transition returned to 399.81 K. "
            "With periodic correction removed, the four-rank NVE COM speed "
            "reached 7.14e-6 Å/fs at 100 fs and the run stopped at 400 fs. "
            "The approved one-rank continuation later completed 2 ps with 20 "
            "NVE samples and maximum COM 1.04e-18 Å/fs. Stage B was replayed "
            "under each rank count, so the phase-space states entering NVE "
            "differed. Checkpoint 11 then held the Stage-B restart fixed: one "
            "rank passed 2 ps, while the four-rank path from that restart had "
            "breached at 100 fs. Checkpoint 12's per-step trace located the "
            "first four-rank breach at 7 fs. Checkpoint 13 used the same "
            "restart at one rank with matched sampling and completed 400 fs; "
            "its maximum COM was 9.65e-19 Å/fs and its 7 fs value was "
            "2.32e-19 Å/fs. This supports rank-count-sensitive behavior in "
            "the saved-state sequence but does not identify a mechanism. "
            "Temperature and energy changes in the 400 fs run were exploratory "
            "because DECISION-013 froze no thresholds. Checkpoint 13 closes "
            "this diagnostic branch; DECISION-014 authorizes one conditional final-results "
            "campaign with frozen stop/proceed gates. Resource and restart- "
            "continuity preflight comes first; the long bridge has not relaunched."
        ),
    ])
    return


@app.cell
def _(mo):
    rank_comparison = [
        {"run": "Checkpoint 09; 4 MPI ranks", "NVE duration": "0.4 ps captured", "samples": 4, "first threshold breach": "100 fs; 7.1446e-6 Å/fs", "maximum COM": "8.3573e-6 Å/fs", "outcome": "Ceiling exceeded"},
        {"run": "Checkpoint 10; 1 MPI rank", "NVE duration": "2 ps completed", "samples": 20, "first threshold breach": "None", "maximum COM": "1.0435e-18 Å/fs at 1.9 ps", "outcome": "All sampled COM values below ceiling"},
        {"run": "Checkpoint 11; 1 MPI rank, same Stage-B restart", "NVE duration": "2 ps completed", "samples": 20, "first threshold breach": "None", "maximum COM": "1.2638e-18 Å/fs at step 23,600", "outcome": "Same-restart continuation below ceiling"},
        {"run": "Checkpoint 12; 4 MPI ranks, same Stage-B restart", "NVE duration": "7 fs until halt", "samples": 8, "first threshold breach": "7 fs; 1.1198e-6 Å/fs", "maximum COM": "1.1198e-6 Å/fs at step 22,007", "outcome": "Automatic stop at frozen ceiling"},
    ]
    mo.vstack([
        mo.md(r"""
        ## Checkpoint 10 — one-rank continuation diagnostic

        The user approved a one-rank replay of Stage B from the same 20 ps
        Stage-A restart, followed by 2 ps of uncorrected NVE. The NVE segment
        completed 2,000 steps with 20 samples: 392.66–402.38 K, endpoint
        399.70 K, and maximum COM speed `1.0435e-18 Å/fs`, far below the frozen
        `1e-6 Å/fs` ceiling.

        This differs from the four-rank run, which first exceeded the ceiling
        at 100 fs. Since Stage B was rerun at each rank count, the NVE starting
        states were not identical. The result suggested rank-sensitive
        continuation behavior but did not isolate an MPI, RATTLE, or NVE cause.
        Checkpoint 11 followed with the exact four-rank Stage-B restart.

        LAMMPS logged completion at step 24,000 and wrote its final restart in
        32:23. A shell-wrapper `printf` error after completion prevented capture
        of the process exit code; the diagnostic report records this limitation.
        """),
        mo.md(r"""
        ## Checkpoint 11 — same-restart rank comparison

        The user approved a one-rank Stage-C/NVE continuation from the exact
        four-rank Stage-B restart. It completed 2 ps, steps 22,000–24,000, in
        14:02 with LAMMPS exit code 0. Twenty NVE samples ranged from
        395.91302 to 406.10015 K and ended at 400.10536 K. Maximum sampled COM
        speed was `1.2638166834526734e-18 Å/fs` at step 23,600; none exceeded
        the frozen `1e-6 Å/fs` ceiling.

        The four-rank path from this same restart exceeded the ceiling at
        100 fs (`7.144552366951081e-6 Å/fs`). This supports rank-count-sensitive
        behavior in the Stage-C/NVE sequence from a common starting checkpoint.
        It does not identify a particular RATTLE, velocity-cleanup, PPPM, or
        reduction mechanism. The full bridge remains on hold; no equilibrium
        or polarization result follows.

        This diagnostic used the existing Ubuntu-on-WSL LAMMPS 10 Dec 2025
        build to keep the environment aligned. Google Colab can be evaluated
        for longer workloads after an environment and performance benchmark.
        """),
        mo.md(r"""
        ## Checkpoint 12 — four-rank high-cadence replay

        The user approved a four-rank replay from the checkpoint-11 Stage-B
        restart, preserving the 1 fs, 400 K, RATTLE, PPPM, OPT, and uncorrected
        NVE settings. Only output cadence and early-stop logic changed. COM
        components and speed were sampled every step, with a 400 fs maximum.

        After velocity cleanup, step 22,000 began at 400.02681 K and
        `6.0282895e-8 Å/fs` COM speed. The eight recorded NVE samples increased
        monotonically. The first ceiling crossing occurred at step 22,007
        (7 fs), with `1.1198276995146967e-6 Å/fs` in the halt message. LAMMPS
        returned exit code 0 after its configured soft halt and output
        finalization; this is a bounded COM failure, not a pass.

        The total-energy column changed by +2.206 kcal/mol over the same seven
        steps. This was not a preregistered acceptance metric and remains an
        exploratory observation. Neither trace identifies the mechanism. The
        full bridge remains on hold; no equilibrium or polarization result
        follows.
        """),
        mo.ui.table(rank_comparison),
    ])
    return


@app.cell
def _(mo):
    bridge_stages = [
        {"stage": "A", "control": "NVE + direct rescale / 100 fs", "duration": "20 ps", "purpose": "erase inherited NEMD velocities"},
        {"stage": "B", "control": "Nosé–Hoover NVT, 400 K, τ = 1 ps", "duration": "500 ps", "purpose": "relax PPPM liquid at exact volume"},
        {"stage": "C", "control": "exact velocity scale", "duration": "instant", "purpose": "set 400 K before NVE"},
        {"stage": "D", "control": "NVE", "duration": "1 ns", "purpose": "measure equilibrium acceptance"},
    ]
    mo.vstack([
        mo.md(
            r"""
            ## Checkpoint 08 and 09 implementation failures

            The supplied author file is a steady-state NEMD snapshot. Its
            velocities must be replaced before it can become the equilibrium
            reference. The source does not report its NpT pressure target, so
            this bridge preserves the exact published box instead of inventing
            one. **DECISION-008 approved this protocol. The first integrated
            attempt failed the frozen COM criterion at 2 ps and was stopped.
            DECISION-009 approved a preparation-only correction. Zero-step,
            2 ps Stage-A, 20 ps Stage-A, and 2 ps Stage-B checks passed. The
            four-rank uncorrected NVE check exceeded the COM ceiling at 100 fs
            and stopped at 400 fs. Checkpoint 11's one-rank Stage-C/NVE
            comparison from the exact four-rank Stage-B restart completed 2 ps
            below the ceiling; the four-rank path from that same restart had
            breached at 100 fs. Checkpoint 12's per-step replay located the
            first breach at 7 fs. This confirms early rank-sensitive COM
            growth in this path but does not identify the mechanism. The full
            bridge remains on hold.**
            """
        ),
        mo.ui.table(bridge_stages),
        mo.md(
            r"""
            Primary acceptance tests are frozen before execution: 400 ± 1 K NVE
            mean with block SE ≤ 0.5 K; fitted relative energy drift ≤ 0.005%;
            exact system integrity; bounded geometry errors and no O–O contact
            below 2.2 Å; no resolved z-temperature slope; stationary O–O first
            peak and coordination; and COM speed ≤ 1e-6 Å/fs with no systematic
            growth. The COM threshold was fixed before step 1 from the measured
            four-rank RATTLE initialization floor.
            """
        ),
    ])
    return


@app.cell
def _(mo):
    mo.md(r"""
    ## Checkpoint 07 release gates

    1. **PASS — build and zero-step audit:** count, box, neutrality,
       geometry, regions, RATTLE, eHEX syntax, and PPPM initialization.
    2. **FAIL — equilibrium bridge:** initialization met the COM ceiling, but
       Stage-A speeds at 1 ps and 2 ps exceeded it by more than 10×. The run
       stopped before NVT or NVE; a new momentum-control checkpoint is required.
    3. 100 ps eHEX smoke test at 1 fs: energy ledger, occupancy, profile
       direction, and absence of cavitation.
    4. Matched 1 fs versus 2 fs test from the same prepared state.
    5. 1 ns stationarity pilot with unfolded branches and block evolution.
    6. Production release only when those records justify the allocation;
       an independent seed is required before a positive reproducibility claim.

    A failed gate is a recorded result. It triggers a documented change and a
    new pilot; it cannot be silently tuned away.
    """)
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
        - Checkpoint 08: `{repo_root / 'research' / 'designs' / 'SIM-02-checkpoint-08-equilibrium-bridge.md'}`
        - Equilibrium decision: `{repo_root / 'research' / 'decisions' / 'DECISION-008-SIM-02-equilibrium-bridge.md'}`
        - Momentum-control proposal: `{repo_root / 'research' / 'designs' / 'SIM-02-checkpoint-09-preparation-momentum-control.md'}`
        - Published benchmark audit: `{repo_root / 'research' / 'literature' / 'Wirnsberger-2016-reproduction-notes.md'}`
        - Academic narrative: `{repo_root / 'research' / 'book' / 'SIM-02.md'}`
        - Technical report: `{repo_root / 'results' / 'reports' / 'SIM-02-report.md'}`
        - Checkpoint 10 one-rank NVE report: `{repo_root / 'results' / 'reports' / 'SIM-02-checkpoint-10-one-rank-nve.md'}`
        - DECISION-010 review: `{repo_root / 'research' / 'decisions' / 'DECISION-010-SIM-02-NVE-COM-drift-review.md'}`
        - Checkpoint 11 same-restart report: `{repo_root / 'results' / 'reports' / 'SIM-02-checkpoint-11-same-restart-one-rank.md'}`
        - DECISION-011 approval and outcome: `{repo_root / 'research' / 'decisions' / 'DECISION-011-SIM-02-same-restart-rank-diagnostic.md'}`
        - Long-form video treatment: `{repo_root / 'research' / 'media' / 'SIM-02-longform-youtube.md'}`
        """
    )
    return


if __name__ == "__main__":
    app.run()
