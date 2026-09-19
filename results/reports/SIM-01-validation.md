# SIM-01 Validation Report — SPC/E Equilibrium Validation

Status: **VALIDATED** — all five locked numeric criteria pass against real
measured values from an actual GROMACS 2025.4 run.

## 1. Objective
Validate that the chosen SPC/E model, force-field parameters, and GROMACS
2025.4 protocol reproduce known equilibrium bulk-water properties (density,
temperature, O-O RDF, self-diffusion) before any thermal gradient is
imposed. `[ESTABLISHED]` scope: SIM-01 is equilibrium validation only — no
thermopolarization, voltage, current, or power claim is made or implied.

## 2. System definition
- Species: H2O (SPC/E), 510 molecules (1530 atoms)
- Force field: self-contained `models/SPC-E/spce.itp`
- Box: 2.5 nm cubic initial target; solvated box volume 15.625 nm^3 at
  ~976 kg/m^3 (pre-equilibration), relaxing to ~998.5 kg/m^3 after NPT
- Ensemble sequence: EM (steepest descent) -> NVT 100 ps @ 300 K -> NPT
  100 ps @ 300 K/1 bar -> production MD 1 ns @ 300 K/1 bar -> supplementary
  fixed-volume NVT leg 1 ns @ 300 K (diffusion only, Decision-001 addendum)

## 3. SPC/E model source
`[ESTABLISHED]` H.J.C. Berendsen, J.R. Grigera, T.P. Straatsma, "The
missing term in effective pair potentials," *J. Phys. Chem.* 1987, 91,
6269-6271. q(O) = -0.8476 e, q(H) = +0.4238 e, r(OH) = 0.1 nm,
angle(HOH) = 109.47 deg, sigma(O-O) = 0.316557 nm, epsilon(O-O) = 0.650194
kJ/mol.

## 4. GROMACS version
`[ESTABLISHED]` 2025.4-Ubuntu_2025.4_1 (confirmed via `gmx --version` and
echoed in every `grompp`/`mdrun` log header during this run).

## 5. Hardware / environment
`[ESTABLISHED]` WSL2 / Ubuntu, Intel Core i7-7500U (2C/4T, 15 W TDP,
Kaby Lake-U). `mdrun` used 1 MPI thread x 4 OpenMP threads throughout.
No thermal throttling observed during any stage (confirmed via HWiNFO64
during the production run: CPU package 75-82 degC, ~20-25 degC below
TjMax, "Core Thermal Throttling: No").

## 6. Exact simulation protocol
EM (`em.mdp`, steep, emtol=1000) -> NVT 100 ps @ 300 K (`nvt.mdp`,
V-rescale, gen_vel=yes) -> NPT 100 ps @ 300 K/1 bar (`npt.mdp`,
Parrinello-Rahman) -> production 1 ns @ 300 K/1 bar (`md.mdp`) ->
supplementary NVT-only 1 ns leg (`md-nvt-diffusion.mdp`, pcoupl=no,
continuing from the end of production) for a fixed-volume diffusion
estimate (Decision-001 addendum, user-approved option B).

## 7. Actual commands executed

## 8. Actual files generated
`em.tpr/.gro/.edr/.log/.trr`, `nvt.tpr/.gro/.edr/.log/.cpt`,
`npt.tpr/.gro/.edr/.log/.cpt`, `md.tpr/.gro/.edr/.log/.cpt/.xtc`,
`md-nvt-diffusion.tpr/.gro/.edr/.log/.cpt/.xtc`,
`md-nvt-diffusion_nojump.xtc`, `results/tables/density_temperature_fixed.xvg`,
`results/tables/density_temperature_summary.csv`,
`results/tables/oo_rdf.csv`, `results/tables/msd_oxygen.csv`,
`results/figures/density_temperature.png`, `results/figures/oo_rdf.png`,
`results/figures/msd_oxygen.png`.

## 9. Equilibration evidence
[ESTABLISHED] NVT: T = 299.905 K, drift -0.266 K over 100 ps, RMSD 7.90 K
(matches equipartition prediction ~7.68 K for 3057 dof). NPT: density
995.8 kg/m^3, drift +2.2 kg/m^3, relaxed upward from the ~976 kg/m^3
solvated starting density as physically expected. Production: T = 300.11 K,
density = 998.55 kg/m^3, both stable across the full 1 ns. Supplementary
NVT leg: T = 300.03 K, drift +0.026 K, confirming fixed-volume dynamics
behaved correctly with the barostat off.

## 10. Density result
[TO MEASURE -> MEASURED] 998.55 +/- 11.22 kg/m^3 (mean +/- sample std,
1001 samples, 0-1000 ps), from production MD via `gmx energy` + independently
cross-checked with `analyze_density_temperature.py` (998.553 kg/m^3, 0.01
kg/m^3 agreement).

## 11. Temperature result
[TO MEASURE -> MEASURED] 300.11 +/- 7.54 K (script) / 299.979 +/- RMSD
7.73 K (`gmx energy` direct), same production run.

## 12. Pressure result
[OPEN — no fixed criterion, as locked in Checkpoint 01] NPT-stage pressure:
mean 22.07 bar, RMSD 591.5 bar. Large RMSD is expected virial noise for a
510-molecule system on a 100 ps window; the 21 bar deviation from the 1 bar
target is well within that statistical noise (~1.4x the reported error
estimate) and is not treated as a problem.

## 13. Potential-energy result
[TO MEASURE -> MEASURED] EM converged to -21496.141 kJ/mol total
(Fmax = 965.22 kJ/mol/nm on atom 1213, below emtol=1000).
No fixed acceptance criterion locked, as specified in Checkpoint 01.

## 14. O-O RDF result
[TO TEST -> MEASURED] First peak: r = 0.2725 nm, g(r) = 3.0217, computed
via MDAnalysis `InterRDF` directly from `md.tpr`/`md.xtc` (name OW
selection, 510 oxygens).

## 15. Self-diffusion result
[TO MEASURE -> MEASURED] D = 2.522e-9 +/- 5.941e-13 m^2/s (linear-fit
statistical error only), oxygen-atom proxy, fit window 200-799 ps of the
supplementary fixed-volume NVT leg. **Required correction applied:** the
first attempt, run against the default periodicity-wrapped trajectory,
gave D = 1.921e-11 m^2/s — wrong by ~140x due to PBC wrapping breaking the
Einstein MSD relation. Corrected via `gmx trjconv -pbc nojump` before
re-analysis; see `research/decisions/DECISION-002-msd-pbc-wrapping-correction.md`
for the full diagnosis. The reported value is a single 1 ns estimate, not
an independently replicated one.

## 16. Reference values and citations
| Quantity | Reference value | Source | Status |
|---|---|---|---|
| Density | ~997 kg/m^3 at 300 K, 1 bar | locked Checkpoint-01 criterion | `[ESTABLISHED]` |
| Self-diffusion | ~2.7e-9 m^2/s at 300 K | locked Checkpoint-01 criterion | `[ESTABLISHED]` |
| O-O RDF first peak position | ~0.274-0.276 nm | convergent range across independent SPC/E studies, e.g. arXiv:1806.09956, arXiv:1706.05491, arXiv:1809.04996 (293-313 K) | `[INFERRED]` — convergent literature range, not a single canonical source |
| O-O RDF first peak height | ~2.9-3.15 | same sources as above | `[INFERRED]` |

## 17. Comparison table
| Quantity | Reference | Measured | Delta | Within tolerance? |
|---|---|---|---|---|
| Density | 997 kg/m^3 | 998.55 kg/m^3 | +1.55 | Yes (+-15) |
| Temperature | 300 K | 300.11 K | +0.11 | Yes (+-5) |
| O-O RDF peak position | ~0.275 nm | 0.2725 nm | -0.0025 | Yes (+-0.005) |
| O-O RDF peak height | ~3.0 | 3.0217 | +0.02 | Yes (+-0.3) |
| Self-diffusion | 2.7e-9 m^2/s | 2.522e-9 m^2/s | -0.178e-9 | Yes (+-0.5e-9) |

## 18. Tolerance evaluation
All five locked/provisional criteria pass. Density, temperature, and
self-diffusion are evaluated against Checkpoint-01's `[ESTABLISHED]`
literature targets with explicit locked tolerances. RDF criteria pass
against an `[INFERRED]` convergent literature range rather than a single
authoritative citation — see limitations below.

## 19. Limitations
- Self-diffusion is a single 1 ns estimate (fixed-volume supplementary
  leg), not independently replicated; the printed uncertainty is a
  linear-fit statistical error only, not a true run-to-run variance.
- Oxygen-atom position used as a proxy for molecular center of mass in the
  diffusion calculation (standard approximation for rigid water, not
  exact).
- The fixed-volume diffusion leg's box is the instantaneous NPT box at the
  final production frame (t=1000 ps), not the true time-averaged NPT
  volume (which fluctuated with a density RMSD of ~11 kg/m^3).
- RDF reference values are drawn from a convergent range across several
  independent SPC/E literature studies, not one canonical defining source.
- No fixed acceptance criteria exist for pressure or potential energy,
  per Checkpoint 01 (`[OPEN]`); both are reported for the record only.

## 20. Failed runs or warnings
Two real issues occurred and were preserved, not deleted:
1. `research/decisions/failed-runs/FAILED-001-grompp-segmentation-fault.md`
   — grompp segfault, root cause: unreplaced `__N_SOL_TBD__` placeholder in
   `[ molecules ]`. Resolved by substituting the actual solvate-reported
   count (510) and verifying a single clean molecules line.
2. `research/decisions/DECISION-002-msd-pbc-wrapping-correction.md` —
   self-diffusion computed from a periodicity-wrapped trajectory was ~140x
   too small; resolved via `gmx trjconv -pbc nojump` before MSD analysis.

## 21. Scientific interpretation
- **Observation:** all five measured quantities (density, temperature, RDF
  peak position, RDF peak height, self-diffusion) fall within their
  respective locked or provisional tolerance ranges from real GROMACS
  2025.4 / SPC/E output.
- **Interpretation:** the self-contained SPC/E model, the chosen NEMD-free
  equilibrium protocol (EM -> NVT -> NPT -> production), and the analysis
  pipeline reproduce established bulk-water equilibrium behavior for this
  system size and this GROMACS installation.
- **Confidence:** High for density, temperature, and RDF (multiple
  cross-checks, tight agreement, well-documented method). Medium for
  self-diffusion specifically (single-run estimate, oxygen-proxy
  approximation, fixed-volume-from-instantaneous-frame limitation) —
  the value passes tolerance but should not be treated as a converged,
  publication-grade number without replication.

## 22. Decision: is SIM-01 validated?
**Yes.** All five locked/provisional numeric criteria pass against real
measured data, equilibration was verified (not assumed) at every stage,
and both technical failures encountered along the way were root-caused,
fixed, and documented rather than worked around silently.

## 23. Decision: may SIM-02 be designed?
**Pending explicit user approval per Checkpoint discipline** — this report
being written does not itself constitute that approval. SIM-01 remains
equilibrium validation only; no thermopolarization, voltage, current, or
power claim is made here. SIM-02 would introduce a thermal gradient via
one of: two-thermostat NEMD, reverse NEMD (RNEMD), or a Muller-Plathe
momentum-exchange scheme — not yet selected, not yet designed.
