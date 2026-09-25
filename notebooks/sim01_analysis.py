import marimo

__generated_with = "0.24.2"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo

    return (mo,)


@app.cell
def _():
    import pandas as pd
    import numpy as np
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt

    return np, pd, plt


@app.cell
def _(mo):
    mo.md(r"""
    # SIM-01 — Interactive Validation Notebook

    Thermal Polarization → Electrical Work — SPC/E equilibrium
    validation, GROMACS 2025.4.

    This notebook reads the **real** output files bundled with it under
    `public/` — it does not recompute anything from raw trajectories,
    and it does not fabricate any number. If a file is missing, the
    corresponding section below will say so plainly rather than
    showing a placeholder value.

    Repository: [github.com/alisunkazemi21-cloud/Thermal-Polarization](https://github.com/alisunkazemi21-cloud/Thermal-Polarization)
    """)
    return


@app.cell
def _(mo, pd):
    def load_repo_csv(filename):
        """Works both in `marimo edit` (real filesystem path) and in a
        WASM/browser export (mo.notebook_location() becomes a URL there;
        pandas.read_csv fetches it directly either way). This is the
        pattern documented at https://docs.marimo.io/guides/wasm/ — no
        manual pyodide fetch code needed."""
        path = mo.notebook_location() / "public" / filename
        try:
            df = pd.read_csv(str(path))
            return df, mo.md(f"Loaded `{filename}` — {len(df)} row(s).")
        except Exception as e:
            return None, mo.md(f"**[TO MEASURE]** Could not load `{filename}`: {e}")

    return (load_repo_csv,)


@app.cell
def _(mo):
    mo.md(r"""
    ## 01 — Density & Temperature
    """)
    return


@app.cell
def _(load_repo_csv):
    df_dt, dt_status = load_repo_csv("density_temperature_summary.csv")
    return df_dt, dt_status


@app.cell
def _(df_dt, dt_status, mo):
    mo.vstack([dt_status, mo.ui.table(df_dt) if df_dt is not None else mo.md("")])
    return


@app.cell
def _(mo):
    mo.md(r"""
    **Checkpoint 01 targets:** density 997 ± 15 kg/m³, temperature
    300 ± 5 K. Compare the loaded values above directly against these —
    this notebook does not auto-grade pass/fail, so the comparison is
    left visible and explicit rather than silently judged.
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ## 02 — Oxygen–Oxygen Radial Distribution Function
    """)
    return


@app.cell
def _(load_repo_csv):
    df_rdf, rdf_status = load_repo_csv("oo_rdf.csv")
    return df_rdf, rdf_status


@app.cell
def _(df_rdf, np, plt):
    if df_rdf is not None:
        _peak_idx = int(np.argmax(df_rdf["g_OO_r"].values))
        peak_r = float(df_rdf["r_nm"].values[_peak_idx])
        peak_g = float(df_rdf["g_OO_r"].values[_peak_idx])

        fig_rdf, ax_rdf = plt.subplots(figsize=(6, 4.2))
        ax_rdf.plot(df_rdf["r_nm"], df_rdf["g_OO_r"], lw=1.2)
        ax_rdf.axvline(peak_r, color="k", ls="--", lw=0.8)
        ax_rdf.set_xlabel("r (nm)")
        ax_rdf.set_ylabel(r"g$_{OO}$(r)")
        ax_rdf.set_title(f"First peak: r={peak_r:.4f} nm, g(r)={peak_g:.3f}")
    else:
        peak_r, peak_g, fig_rdf = None, None, None
    return fig_rdf, peak_g, peak_r


@app.cell
def _(fig_rdf, mo, peak_g, peak_r, rdf_status):
    if fig_rdf is not None:
        rdf_display = mo.vstack([
            rdf_status,
            mo.as_html(fig_rdf),
            mo.md(
                f"**Measured:** r_peak = {peak_r:.4f} nm, "
                f"g(r_peak) = {peak_g:.4f}. "
                f"**Checkpoint 01 target:** ≈0.275 nm, ≈3.0 "
                f"(convergent literature range, not a single canonical source "
                f"— see Section 16 of `results/reports/SIM-01-validation.md`)."
            ),
        ])
    else:
        rdf_display = rdf_status
    return (rdf_display,)


@app.cell
def _(rdf_display):
    rdf_display
    return


@app.cell
def _(mo):
    mo.md(r"""
    ## 03 — Self-Diffusion (interactive re-fit)
    """)
    return


@app.cell
def _(load_repo_csv):
    df_msd, msd_status = load_repo_csv("msd_oxygen.csv")
    return df_msd, msd_status


@app.cell
def _(mo):
    mo.md(r"""
    Drag the sliders below to change the linear-fit window and watch
    the fitted diffusion coefficient update live. The original script
    used a fixed 20%–80% window — this lets you check how sensitive
    the result is to that choice, which the original single run could
    not show on its own.
    """)
    return


@app.cell
def _(mo):
    fit_start = mo.ui.slider(0.0, 0.6, value=0.2, step=0.05, label="Fit start (fraction)")
    fit_end = mo.ui.slider(0.4, 1.0, value=0.8, step=0.05, label="Fit end (fraction)")
    return fit_end, fit_start


@app.cell
def _(fit_end, fit_start, mo):
    mo.hstack([fit_start, fit_end])
    return


@app.cell
def _(df_msd, fit_end, fit_start, np, plt):
    if df_msd is not None:
        _lag = df_msd["lag_time_ps"].values
        _msd = df_msd["msd_A2"].values
        _n = len(_msd)
        _i0 = int(fit_start.value * _n)
        _i1 = int(fit_end.value * _n)

        if _i1 <= _i0 + 1:
            D_estimate = None
            fig_msd = None
            fit_note = "Fit window too narrow at these slider values — widen the range."
        else:
            _coeffs, _cov = np.polyfit(_lag[_i0:_i1], _msd[_i0:_i1], 1, cov=True)
            _slope = _coeffs[0]
            _slope_err = float(np.sqrt(_cov[0, 0]))
            # D = slope/6 (3D Einstein relation); Angstrom^2/ps -> m^2/s: factor 1e-8
            D_estimate = (_slope / 6.0) * 1e-8
            D_err = (_slope_err / 6.0) * 1e-8

            fig_msd, ax_msd = plt.subplots(figsize=(6, 4.2))
            ax_msd.plot(_lag, _msd, lw=1.0, label="MSD (oxygen)")
            _fit_line = _coeffs[0] * _lag[_i0:_i1] + _coeffs[1]
            ax_msd.plot(_lag[_i0:_i1], _fit_line, "k--", lw=1.2, label="fit window")
            ax_msd.set_xlabel("Lag time (ps)")
            ax_msd.set_ylabel(r"MSD ($\mathrm{\AA}^2$)")
            ax_msd.legend()
            fit_note = (
                f"D = {D_estimate:.3e} ± {D_err:.3e} m²/s "
                f"(fit window {_lag[_i0]:.0f}–{_lag[_i1-1]:.0f} ps)"
            )
    else:
        D_estimate, fig_msd, fit_note = None, None, "No MSD data loaded."
    return D_estimate, fig_msd, fit_note


@app.cell
def _(fig_msd, fit_note, mo, msd_status):
    if fig_msd is not None:
        msd_display = mo.vstack([msd_status, mo.as_html(fig_msd), mo.md(f"**{fit_note}**")])
    else:
        msd_display = mo.vstack([msd_status, mo.md(fit_note)])
    return (msd_display,)


@app.cell
def _(msd_display):
    msd_display
    return


@app.cell
def _(mo):
    mo.md(r"""
    **Checkpoint 01 target:** 2.7×10⁻⁹ ± 0.5×10⁻⁹ m²/s. The original
    analysis (fixed 20%–80% window, unwrapped trajectory) measured
    2.522×10⁻⁹ m²/s — a single, unreplicated 1 ns estimate. Use the
    sliders above to see how much that number moves with the fit
    window before treating it as precise.
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ## 04 — Checkpoint 01 summary (from loaded data, not hardcoded)
    """)
    return


@app.cell
def _(D_estimate, df_dt, pd, peak_g, peak_r):
    _rows = []
    if df_dt is not None:
        _rows.append({
            "Quantity": "Density (kg/m³)",
            "Target": "997 ± 15",
            "Measured": f"{df_dt['density_mean_kg_m3'].iloc[0]:.2f} ± {df_dt['density_std_kg_m3'].iloc[0]:.2f}",
        })
        _rows.append({
            "Quantity": "Temperature (K)",
            "Target": "300 ± 5",
            "Measured": f"{df_dt['temperature_mean_K'].iloc[0]:.2f} ± {df_dt['temperature_std_K'].iloc[0]:.2f}",
        })
    if peak_r is not None:
        _rows.append({
            "Quantity": "O-O RDF peak position (nm)",
            "Target": "≈0.275 ± 0.005",
            "Measured": f"{peak_r:.4f}",
        })
        _rows.append({
            "Quantity": "O-O RDF peak height",
            "Target": "≈3.0 ± 0.3",
            "Measured": f"{peak_g:.4f}",
        })
    if D_estimate is not None:
        _rows.append({
            "Quantity": "Self-diffusion (m²/s)",
            "Target": "2.7e-9 ± 0.5e-9",
            "Measured": f"{D_estimate:.3e} (current slider window)",
        })

    summary_df = pd.DataFrame(_rows) if _rows else None
    return (summary_df,)


@app.cell
def _(mo, summary_df):
    mo.ui.table(summary_df) if summary_df is not None else mo.md(
        "No data files loaded yet — nothing to summarize."
    )
    return


@app.cell
def _(mo):
    mo.md(r"""
    ---

    No thermopolarization, voltage, current, or power claim is made
    anywhere in this notebook. SIM-01 is equilibrium validation only.
    Full protocol files, decision records, and failure logs:
    [github.com/alisunkazemi21-cloud/Thermal-Polarization](https://github.com/alisunkazemi21-cloud/Thermal-Polarization)
    """)
    return


if __name__ == "__main__":
    app.run()
