# DECISION-002 — MSD periodic-boundary-wrapping correction

- **Date:** 2026-09-19
- **Stage:** SIM-01, self-diffusion analysis (supplementary NVT leg)

## Observation

[ESTABLISHED] Running `scripts/analysis/analyze_diffusion.py` directly
against `md-nvt-diffusion.xtc` (GROMACS's default periodicity-wrapped
trajectory output) gave D = 1.921e-11 +/- 4.324e-13 m^2/s.

[ESTABLISHED] This value is approximately 140x smaller than the locked
Checkpoint-01 reference (2.7e-9 +/- 0.5e-9 m^2/s) — not a tolerance failure,
but a magnitude inconsistent with liquid water behaving as SPC/E at 300 K.

## Diagnosis

[INFERRED] GROMACS `.xtc` trajectories store atom coordinates wrapped back
into the primary simulation box by default. When a molecule's unwrapped
trajectory crosses a periodic boundary, its wrapped coordinates jump
discontinuously. The Einstein MSD relation requires unwrapped (continuous)
displacement; feeding it wrapped coordinates artificially suppresses the
computed MSD and collapses the fitted diffusion coefficient.

## Correction

[ESTABLISHED] Generated an unwrapped trajectory with:
`gmx trjconv -f md-nvt-diffusion.xtc -s md-nvt-diffusion.tpr -pbc nojump -o md-nvt-diffusion_nojump.xtc`
(group 0 / System selected).

[ESTABLISHED] Re-running the identical analysis script against the
unwrapped trajectory gave D = 2.522e-9 +/- 5.941e-13 m^2/s — within the
locked tolerance range (2.2e-9 to 3.2e-9 m^2/s).

## Consequence for the analysis script

[OPEN] `scripts/analysis/analyze_diffusion.py` should document this
requirement in its usage instructions going forward (unwrap with
`gmx trjconv -pbc nojump` before use) rather than relying on the operator
to remember it. Not yet edited into the script itself.

## Scientific interpretation

- **Observation:** wrapped-trajectory MSD analysis produced a diffusion
  coefficient two orders of magnitude too small.
- **Interpretation:** the discrepancy is attributable to a methodological
  error (feeding wrapped coordinates to an Einstein-relation MSD
  calculation), not to any property of the SPC/E model or the simulation
  itself.
- **Confidence:** High — the corrected value falls within the literature
  tolerance, and the ~130x correction factor is consistent in direction
  and rough magnitude with what periodic-image discontinuities would be
  expected to produce over a 1 ns trajectory in a 2.5 nm box.
- **Alternative explanations considered:** a genuine SPC/E model
  deficiency was considered and rejected — SPC/E's diffusion behavior at
  300 K is well documented in the literature and not known to be this far
  off; the wrapped/unwrapped discrepancy provides a complete and sufficient
  explanation on its own.

## User approval status

Diagnosed and corrected within the same session; no separate approval
gate required as this is a methodology bugfix, not a scope change.
