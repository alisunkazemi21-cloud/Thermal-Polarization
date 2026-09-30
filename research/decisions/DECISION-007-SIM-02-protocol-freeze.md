# DECISION-007 — freeze the 400 K benchmark and staged release gates

- **Date:** 2026-09-30
- **Status:** Approved
- **Decision source:** user approval of checkpoint 07
- **Depends on:** DECISION-005 and DECISION-006

## Decision

Adopt the audited Wirnsberger et al. 400 K SPC/E configuration as the SIM-02
method-validation benchmark: 4,500 waters in the exact author-package box, hot
reservoir split across the periodic z edges, central cold reservoir, and
±0.1614 kcal mol⁻¹ fs⁻¹ exchange rate.

Implement the modern LAMMPS translation through sequential release gates:

1. build and zero-step audit;
2. equilibrium bridge;
3. 100 ps eHEX smoke test at 1 fs;
4. matched 1 fs versus 2 fs test;
5. 1 ns stationarity pilot;
6. production release only after the earlier evidence passes.

PPPM at 10⁻⁵ is a documented translation from the published Ewald calculation,
not an assumed identity. A positive reproducibility claim requires an
independent seed.

## First gate outcome

`[MEASURED]` Gate 1 passed on 2026-09-30. The deterministic structure audit and
LAMMPS 10 Dec 2025 `run 0` both passed. No trajectory step was advanced. The
measured evidence is in `results/reports/SIM-02-checkpoint-07-zero-step.md`.

## Consequence

The equilibrium-bridge design is released. NEMD execution and all polarization
claims remain blocked by their later gates.

