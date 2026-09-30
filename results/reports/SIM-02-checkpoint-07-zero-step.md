# SIM-02 checkpoint 07 — gate 1 zero-step audit

- **Evidence class:** `[MEASURED]` deterministic structure audit plus LAMMPS
  zero-step execution
- **Date:** 2026-09-30
- **Overall:** PASS
- **Trajectory advancement:** zero steps
- **SHA-256:** `e7a84f120dc7e01479fe2fc0b8aed9fcaf4b8178cbfa0629923e83bdf8945e66`

## Independent structure checks

| Check | Result |
|---|---|
| atom_count | PASS |
| molecule_count | PASS |
| three_sites_per_molecule | PASS |
| bond_count | PASS |
| angle_count | PASS |
| velocity_count | PASS |
| neutral_system | PASS |
| neutral_molecules | PASS |
| spce_oh_geometry | PASS |
| spce_angle_geometry | PASS |

## Observations

- Atoms / molecules: 13500 / 4500
- Box: 36.353430872542 × 36.353430872542 × 109.060578798266 Å³
- Density from count and volume: 933.993861 kg m⁻³
- Net charge: 0.000e+00 e
- O–H distance, min/mean/max: 0.999999887 / 1.000000000 / 1.000000056 Å
- H–O–H angle, min/mean/max: 109.469995904 / 109.470000002 / 109.470006748°
- Molecules by COM region: hot 282, cold 369, bulk 3849
- Minimum periodic O–O distance: 2.399325846 Å

## LAMMPS zero-step execution

`[MEASURED]` LAMMPS 10 Dec 2025 read the full configuration and velocities,
constructed all 4,500 RATTLE clusters, accepted the current eHEX
`constrain com` syntax for both reservoirs, initialized PPPM, and completed
`run 0` without an error. No trajectory step was advanced.

| Diagnostic | Observed value |
|---|---:|
| PPPM estimated relative force accuracy | 9.136047 × 10⁻⁶ |
| Step-zero temperature | 404.21051 K |
| Step-zero pressure | 504.58835 atm |
| Potential energy | −44,166.098 kcal mol⁻¹ |
| Kinetic energy | 10,842.668 kcal mol⁻¹ |
| Total energy | −33,323.430 kcal mol⁻¹ |

The instantaneous temperature and pressure describe the imported nonequilibrium
source state evaluated with the translated PPPM calculation. They are diagnostic
values, not equilibrium estimates or acceptance targets.

## Gate outcome

**PASS.** The imported system, reservoir definitions, constraints, eHEX syntax,
and PPPM force initialization are internally consistent enough to release the
equilibrium-bridge design. This checkpoint does not establish equilibrium under
PPPM, stationarity, a temperature gradient, or thermopolarization.

Machine-readable evidence and the complete log are under
`results/raw/SIM-02/checkpoint-07-zero-step/`.
