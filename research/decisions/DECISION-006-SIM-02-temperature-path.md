# DECISION-006 — validate at 400 K before the 300 K target

- **Date:** 2026-09-30
- **Status:** Approved
- **Stage:** SIM-02 detailed design

## Decision

Use a two-condition sequence for SIM-02:

1. validate the LAMMPS SPC/E + eHEX implementation at a 400 K mean
   temperature against the published thermopolarization method;
2. proceed to the project's 300 K target condition only after the 400 K
   equilibrium bridge and eHEX pilot acceptance gates pass.

This is a validation sequence, not a temperature sweep.

## Reason

The 400 K condition provides the most direct method comparison with the 2013
SPC/E heat-exchange study. The 300 K condition addresses the project's ambient
target but should not carry the full burden of validating a new engine,
translated force-field implementation, heat-exchange setup, and analysis code
at the same time.

## Gate

This decision approves the order of conditions. It does not yet approve the
exact box dimensions, molecule count, eHEX energy-transfer rate, sampling
interval, run length, or replicate count. Those values must be derived,
documented, and checked through the pilot workflow before production.

## Approval

The user explicitly approved the recommended two-condition path on 2026-09-30.

## Related records

- `DECISION-005-SIM-02-LAMMPS-eHEX.md`
- `../designs/SIM-02-LAMMPS-eHEX-design.md`
- `../../notebooks/sim02_research.py`
