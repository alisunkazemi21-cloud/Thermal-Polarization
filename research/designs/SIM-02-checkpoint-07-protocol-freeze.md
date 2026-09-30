# SIM-02 checkpoint 07 — published protocol recovery and pilot freeze

- **Prepared:** 2026-09-30
- **Status:** `[PROPOSED — AWAITING USER DECISION]`
- **Depends on:** DECISION-005 and DECISION-006
- **Execution status:** no SIM-02 run has started

## Checkpoint question

Should SIM-02 adopt the recovered Wirnsberger et al. 400 K condition as its
method-validation benchmark, implemented through short release gates before any
long trajectory?

## Facts established before the decision

The author package fixes several values that were approximate or reversed in the
earlier discussion draft:

- 4,500 rigid SPC/E waters in a 36.3534308725 × 36.3534308725 ×
  109.060578798 Å³ periodic box;
- density 0.934 g cm⁻³ and mean temperature 400 K;
- hot reservoir split over the periodic z edges, 4 Å at each edge;
- cold reservoir centered at z = 0 with 8 Å total thickness;
- exchange rate ±0.1614 kcal mol⁻¹ fs⁻¹, equivalent to
  4.243 × 10¹⁰ W m⁻² per transport branch;
- 11 Å Lennard-Jones cutoff and long-range precision 10⁻⁵;
- RATTLE-constrained water, eHEX every step, and molecular COM treatment.

These are source facts, not measured project results.

## Proposed implementation translation

| Item | Proposed SIM-02 value | Reason |
|---|---|---|
| Molecules and box | reproduce the published 4,500-water box | removes geometry and flux ambiguity |
| Electrostatics | `lj/cut/coul/long` + PPPM, accuracy 10⁻⁵, 11 Å cutoff | modern supported solver; requires validation against the Ewald reference |
| Constraints | RATTLE, tolerance 10⁻¹⁰, 400 iterations | matches the author input |
| Reservoirs | hot: edge 4 Å + 4 Å; cold: central 8 Å | matches the author input and periodic geometry |
| Heat rate | +0.1614 hot / −0.1614 cold kcal mol⁻¹ fs⁻¹ | reproduces the published benchmark |
| eHEX | every step with `constrain com` | current LAMMPS syntax for the published molecular-COM treatment |
| Initial timestep | 1 fs | conservative construction and stability bridge |
| Candidate timestep | 2 fs only after matched comparison | published value; acceptance depends on constraints and energy behavior |
| Profiles | acquire at 0.9088 Å, report merged 2.73 Å and 5.45 Å views | preserves information while matching published presentation scales |
| Statistical blocks | 100 ps after stationarity | matches the published production analysis |

## Release gates

1. **Build and zero-step audit.** Verify 4,500 molecules, 13,500 atoms,
   neutrality, exact box, masses, charges, geometry, region volumes, and no
   overlaps. This produces metadata, not a physical result.
2. **Equilibrium bridge.** Reproduce the preparation sequence, then audit NVE
   temperature, density, O–O structure, constraints, and energy behavior.
3. **100 ps eHEX smoke test at 1 fs.** Verify energy bookkeeping, reservoir
   occupancy, constraint stability, temperature direction, and absence of
   cavitation. This is a software/physics sanity check, not a polarization claim.
4. **Matched 1 fs versus 2 fs test.** Compare normalized energy behavior,
   constraint errors, and early T(z)/ρ(z) profiles from the same prepared state.
   Adopt 2 fs only when the comparison is acceptable and documented.
5. **1 ns stationarity pilot.** Inspect both unfolded branches, reservoir
   populations, T(z), ρ(z), Pz(z), orientation, and block evolution. Decide
   whether evidence justifies the published 10 ns transient and longer
   production allocation.
6. **Production release.** A positive reproducibility claim remains blocked
   until an independent seed confirms the signal. A failed gate stops the
   sequence and becomes a documented result.

## Acceptance principles to freeze now

- Equal and opposite requested reservoir rates must be recorded independently
  of the observed temperature profile.
- Report both transport branches before any folding or symmetry averaging.
- Exclude reservoir slabs from the linear-gradient fit and record the fitted
  range explicitly.
- Compare the 400 K gradient to the published −5.14 ± 0.04 K Å⁻¹ only after a
  stationary interval exists; a short smoke test cannot pass that literature
  benchmark.
- Use block uncertainty for profiles and keep time-correlation assumptions
  explicit.
- Treat PPPM-versus-Ewald and timestep changes as tested translations, not as
  silent equivalences.
- Keep temperature/density establishment separate from any polarization claim.

## Decision requested

Approve, revise, or reject this exact 400 K protocol and staged release plan.
Approval authorizes creation of the LAMMPS build/equilibration inputs and the
zero-step audit; it does not authorize skipping later gates or claiming a SIM-02
result.

