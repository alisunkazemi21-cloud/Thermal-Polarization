# Research decisions

- `DECISION-001-SIM-01-equilibrium-validation.md` — equilibrium validation
  protocol and the supplementary fixed-volume diffusion leg.
- `DECISION-002-msd-pbc-wrapping-correction.md` — PBC correction required for
  the SIM-01 diffusion calculation.
- `DECISION-003-SIM-02-NEMD-design.md` — preserved historical SIM-02 design and
  approval record; its static spatial-thermostat assumption is superseded.
- `DECISION-004-SIM-02-method-audit.md` — audit of the inherited GROMACS method;
  resolved by DECISION-005.
- `DECISION-005-SIM-02-LAMMPS-eHEX.md` — approved selection of LAMMPS eHEX,
  subject to an equilibrium bridge check and detailed design approval.
- `DECISION-006-SIM-02-temperature-path.md` — approved 400 K method validation
  followed by the 300 K target after the pilot gates pass.
- `DECISION-007-SIM-02-protocol-freeze.md` — approved exact 400 K benchmark and
  staged release gates; gate 1 zero-step audit passed.

Decision records preserve what was believed at the time. Later records may
supersede an assumption without rewriting its history.
