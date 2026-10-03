# DECISION-009 — Preparation-stage momentum control

- Date: 2026-10-03
- Status: **Approved by the user**
- Scope: revise checkpoint-08 preparation fixes and execute the bounded
  validation sequence in checkpoint 09.

## Decision

Apply `fix momentum 100 linear 1 1 1 rescale` during the 400 K Stage-A
rescaling preparation and Stage-B NVT preparation only. In both stages, define
the velocity-modifying fixes before RATTLE so that `fix rattle` is last in the
fix order. Remove periodic momentum control before Stage C and the 1 ns NVE
acceptance stage. Retain the frozen NVE COM-speed ceiling of `1e-6 Å/fs` and the
no-systematic-growth requirement.

## Authorized validation sequence

1. Four-rank production-path zero-step initialization.
2. Two-ps Stage-A diagnostic with thermo every 100 steps.
3. If it passes, 20-ps Stage-A diagnostic.
4. Short Stage-B transition diagnostic.
5. Short NVE diagnostic with periodic momentum control disabled.
6. A new full-bridge launch only after the preceding diagnostics pass.

## Basis

The previous Stage-A trajectory failed its approved momentum criterion at 1 ps
and 2 ps, despite the corrected zero-step initialization. LAMMPS documents that
`fix momentum` removes the group COM velocity without changing pairwise relative
velocities; its `rescale` option restores group kinetic energy. LAMMPS documents
that RATTLE must follow other integration fixes that modify forces or
velocities. The user approved this bounded correction on 2026-10-03.

Sources: <https://docs.lammps.org/fix_momentum.html> and
<https://docs.lammps.org/fix_shake.html>.

## Limits

This decision does not release eHEX, alter the frozen physical protocol, or
declare the equilibrium bridge passed. Each diagnostic outcome must be recorded
before the next sequence step.
