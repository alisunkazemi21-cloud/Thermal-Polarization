# DECISION-005 — use LAMMPS eHEX for SIM-02

- **Date:** 2026-09-30
- **Status:** Approved
- **Stage:** SIM-02 thermal-gradient NEMD

## Decision

Use LAMMPS with the enhanced heat-exchange (`fix ehex`) method for SIM-02.
The heat source and sink will be spatial regions whose membership is evaluated
during dynamics. Rigid SPC/E molecules will use RATTLE/SHAKE-compatible eHEX
options (`constrain com`) and long-range electrostatics.

## Evidence

- **[ESTABLISHED]** DECISION-004 found that the inherited GROMACS
  `Hot/Cold/Rest` groups were fixed atom memberships and therefore did not remain
  spatial reservoirs as water diffused.
- **[ESTABLISHED]** LAMMPS `fix ehex` applies the reservoir force according to a
  particle's current region and documents compatibility with constrained SPC/E
  water using `constrain com` and RATTLE.
- **[ESTABLISHED]** The local WSL installation is LAMMPS 10 Dec 2025 and exposes
  `ehex`, `RIGID`, `shake`, `pppm`, and `rattle` functionality.
- **[ESTABLISHED]** Armstrong and Bresme's SPC/E thermopolarization study used
  spatial heat exchange and an independent spatial thermostatting check.

## Why this method

eHEX supplies a traceable imposed energy-transfer rate, permits a defensible heat
flux, follows molecules dynamically through the reservoirs, and has a published
energy-conservation correction over the older HEX method. It answers the SIM-02
question more directly than restraining fixed thermostat molecules.

## Alternatives

- Custom GROMACS dynamic reservoirs: rejected because they add a new simulation
  implementation and validation burden without improving the first experiment.
- Restrained fixed-membership reservoirs in stock GROMACS: rejected because the
  restraint/interface artifacts weaken the bulk-liquid interpretation.
- Original static GROMACS groups: rejected as methodologically invalid for a
  diffusing liquid.

## Conditions

Switching engines requires a LAMMPS equilibrium bridge check before NEMD. The
SPC/E parameters, density, temperature, structure, and constraint/energy behavior
must be shown consistent with the validated SIM-01 baseline or explained.

This decision selects the engine and gradient mechanism. It does not approve a
box, mean temperature, heat rate, duration, or production run. Those remain in
the design gate.

## Approval

User explicitly approved proceeding in LAMMPS on 2026-09-30 and required the
learn → discuss → decide → document → execute → analyze workflow.

## Sources

- LAMMPS `fix ehex`: https://docs.lammps.org/fix_ehex.html
- LAMMPS SPC/E how-to: https://docs.lammps.org/Howto_spc.html
- Wirnsberger, Frenkel, and Dellago, J. Chem. Phys. 143, 124104 (2015),
  DOI: 10.1063/1.4931597.
- Armstrong and Bresme, J. Chem. Phys. 139, 014504 (2013),
  DOI: 10.1063/1.4811291.
