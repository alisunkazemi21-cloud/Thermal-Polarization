# DECISION-014 — Integrated SIM-02 final-results campaign

- Date: 2026-10-05
- Status: **Approved 2026-10-05 for one conditional campaign; scientific gates remain binding**
- Depends on: DECISION-007 through DECISION-013

## Objective

Reach one defensible SIM-02 result for thermopolarization in the approved SPC/E
water system: report signed `Pz(z)` with heat flux, temperature and density
profiles, block uncertainty, and an explicit outcome (reproduced, not detected,
or unresolved). A positive reproducibility claim still requires the independent
seed replicate required by DECISION-007 and the SIM-02 design. Do not imply an
electrical-power result; SIM-02 measures polarization, not loaded-circuit power.

Checkpoint 13 closes the rank-count diagnostic. Its matched traces support
rank-count-sensitive behavior for this saved-state Stage-C/NVE sequence: the
four-rank trace crossed the COM ceiling at 7 fs, while the one-rank trace
completed 400 fs below it. The mechanism remains unresolved. Do not add further
COM-mechanism probes to this campaign.

## Approved campaign structure

Treat the existing sequential gates as internal stop/proceed rules in one
campaign. Do not pause for a new user decision after each passing gate, and do
not relax a criterion or start a parameter sweep. Record and publish each
checkpoint as execution proceeds.

| Order | Stage | Continue only when |
|---|---|---|
| 0 | Resource and restart preflight | Pin and record the host, LAMMPS build, rank/thread layout, durable storage, restart cadence, and wall-time estimate. Before any cloud trajectory, pass the already specified 10 ps uninterrupted-versus-restarted NVE continuity test. |
| 1 | 400 K equilibrium bridge (Gate 2) | All eight unchanged DECISION-008 criteria pass. Any failure stops the campaign and is reported; no corrective sweep is authorized. |
| 2 | 100 ps eHEX smoke test at 1 fs | DECISION-007 checks pass: energy bookkeeping, reservoir occupancy, constraints, temperature direction, and no cavitation. This stage validates implementation; it is not a polarization result. |
| 3 | Matched timestep check and 1 ns stationarity pilot | Complete the DECISION-007 comparison and pilot at the frozen model and heat rate. Use the existing pilot checks for both unfolded branches, reservoir populations, `T(z)`, `rho(z)`, `Pz(z)`, orientation, and block evolution. A failed check stops the campaign. Keep 1 fs unless the documented comparison supports the already proposed 2 fs option. |
| 4 | Published-scale 400 K measurement | Only after the pilot passes, run the published-reference 10 ns transient plus 60 ns production target. Report both branches before folding, the 2.73 and 5.45 Angstrom profile views, block means and uncertainty, and energy balance. |
| 5 | 300 K target condition | Proceed only after the 400 K method-validation gates pass, as already ordered in DECISION-006. Before launch, derive and record the 300 K run length and replicate plan through the approved pilot workflow; DECISION-006 leaves these values open. Apply the validated method and the same evidence/reporting discipline. An independent seed is required before calling a positive signal reproducible. |

The campaign's final report states the measured result and uncertainty, or the
first gate that stopped it. A smoke-test or pilot signal alone is not called the
final thermopolarization result. Passing or failing these stages does not
establish electrical voltage, current, or extractable power.

## Scientific and execution boundaries

Keep the force field, 4,500-water geometry, reservoir locations, heat rate,
PPPM/RATTLE implementation, and every frozen DECISION-008 threshold unchanged.
The approved initial timestep is 1 fs. The 2 fs option is adopted only if the
already approved matched comparison is documented as acceptable; otherwise
continue at 1 fs. Do not add temperatures, force fields, rank-count probes, or
other variants.

The local CP13 rate (400 steps in 3:57) gives a rough linear estimate of about
10.4 days for the 1.52-million-step equilibrium bridge on that path. This is
not a measured full-run time and excludes the NEMD stages. Do not launch the
long bridge until the preflight records a suitable sustained runtime and
restart recovery plan. For cloud execution, follow DECISION-008's version-pin,
10 ps restart-continuity, durable 50 ps restart, and fix-reissue requirements.

This decision authorizes the integrated, conditional campaign and its required
preflight. Existing gates remain automatic stop conditions; they do not invite
new user-approval checkpoints. A change to a scientific parameter, threshold,
or method is outside this authorization and requires a new decision.
