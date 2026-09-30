# DECISION-004 — SIM-02 NEMD method audit

- **Date:** 2026-09-30
- **Status:** Resolved by DECISION-005 — LAMMPS eHEX selected
- **Supersedes:** the runnable-method assumption in DECISION-003; its historical
  approval record remains preserved

## Question audited

Can the drafted `Hot`, `Cold`, and `Rest` GROMACS temperature-coupling groups
implement spatial reservoirs for diffusing bulk water?

## Findings

1. **[ESTABLISHED]** The installed engine is
   `GROMACS 2025.4-Ubuntu_2025.4_1`, mixed precision, CPU-only. This was measured
   locally with `gmx --version` on 2026-09-30.
2. **[ESTABLISHED]** GROMACS `tc-grps` names groups coupled to separate thermal
   baths. Index groups are atom lists supplied to preprocessing. The 2025.4
   documentation does not provide an option for reevaluating a spatial
   selection as thermostat membership during `mdrun`.
3. **[ESTABLISHED]** Local `gmx select -h` confirms that dynamic selections act
   on trajectories and write analysis outputs. It does not expose a mechanism
   that updates `tc-grps` inside a running simulation.
4. **[INFERRED, high confidence]** An index made from initial z positions would
   keep thermostat membership attached to molecule identities. Diffusing water
   would carry those identities away from the intended reservoirs, so the
   proposed temperature control would cease to be spatial.
5. **[ESTABLISHED]** Armstrong and Bresme (2013) imposed the gradient by adding
   and removing kinetic energy from spatial regions using the heat-exchange
   algorithm; their independent check also thermostatted the molecules
   currently inside hot and cold regions. That is materially different from
   fixed initial atom groups.
6. **[ESTABLISHED]** `nstxout-compressed` writes positions. With `nstvout = 0`,
   the draft does not save the velocities needed for a kinetic local-temperature
   profile. GROMACS `gmx traj -ot` requires velocities and does not correct for
   constrained degrees of freedom, so a dedicated molecular/bin analysis is
   still preferable.
7. **[INFERRED]** A 1.5 ns production run is a pilot length, not a defensible
   final measurement. The 2013 SPC/E study used at least 1 ns to establish steady
   state and typically 10 ns production for its main gradient series. Signal and
   uncertainty must determine the final duration.

## Method options

### A — LAMMPS eHEX (scientific recommendation)

Use spatial regions whose membership is evaluated during dynamics and impose a
known, equal-and-opposite energy transfer with the enhanced heat-exchange
algorithm. This directly supplies the heat rate, supports a defensible heat flux,
and closely matches the published SPC/E workflow. Reproduce the SIM-01
equilibrium checks in LAMMPS before trusting NEMD results.

Trade-off: this changes the engine from the original GROMACS 2025.4 requirement.

### B — custom GROMACS 2025.4 implementation

Implement and validate dynamic spatial reservoirs that act on the molecules
currently inside each slab, conserve total momentum, and record cumulative
energy added and removed. This preserves the engine requirement but introduces
custom simulation code and a substantial verification burden.

### C — restrained fixed-membership reservoirs in stock GROMACS

Restrain selected reservoir molecules so they remain in their slabs, then apply
separate thermostats. This is technically possible but creates structured,
non-bulk reservoir layers and new restraint/interface artifacts. **Rejected for
the first clean bulk-water test.**

## Decision gate — resolved

On 2026-09-30 the user selected option A, LAMMPS eHEX. See DECISION-005.
Do not create an initial-position index and proceed with the superseded
`tc-grps` method.

After the method choice, lock the elongated box, molecule count, reservoir
thickness, imposed heat rate or thermostat rule, velocity/profile sampling,
steady-state diagnostics, block design, computational cost, and pilot acceptance
criteria. Run preprocessing and a short stability pilot before production.

## Sources

- GROMACS 2025.4, *Getting started* and *Molecular dynamics parameters*:
  https://manual.gromacs.org/documentation/2025.4/user-guide/getting-started.html
  and https://manual.gromacs.org/documentation/2025.4/manual-2025.4.pdf
- GROMACS 2025.4 command-line reference:
  https://manual.gromacs.org/documentation/2025.4/user-guide/cmdline.html
- J. A. Armstrong and F. Bresme, *Water polarization induced by thermal
  gradients: The extended simple point charge model (SPC/E)*,
  J. Chem. Phys. 139, 014504 (2013), DOI: 10.1063/1.4811291.
- P. Wirnsberger, D. Frenkel, and C. Dellago, *An enhanced version of the heat
  exchange algorithm with excellent energy conservation properties*,
  J. Chem. Phys. 143, 124104 (2015), DOI: 10.1063/1.4931597.
- LAMMPS `fix ehex` documentation: https://docs.lammps.org/fix_ehex.html
