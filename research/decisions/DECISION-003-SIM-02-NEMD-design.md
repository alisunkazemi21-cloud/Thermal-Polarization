# DECISION-003 — SIM-02 NEMD design choices

- **Date:** [fill in today's date]
- **Decisions:**
  1. Two-thermostat (hot/cold-region) NEMD, not RNEMD or Muller-Plathe.
  2. NEMD production at fixed volume (pcoupl=no), continuing from a
     freshly NPT-equilibrated box for the new geometry.
  3. Hot slab centered in the box (z-center), cold slab split across the
     periodic boundary (z-edges) — symmetric double-gradient geometry.
  4. Three thermostat groups (Hot, Cold, Rest), with Rest weakly coupled
     at the mean temperature (300 K, long tau_t) rather than left
     uncoupled, to satisfy GROMACS's tc-grps atom-coverage requirement
     without materially constraining the bulk region's emergent T(z).

- **Reason:** Lower implementation risk than RNEMD/Muller-Plathe (no
  custom swap code, GROMACS-native tcoupl); fixed volume avoids an
  ill-defined system pressure under a temperature gradient; symmetric
  geometry avoids a periodic-boundary discontinuity and gives a free
  internal consistency check.
- **Evidence:** Standard practice in the cited two-region NEMD literature
  (Bresme et al. 2008, Armstrong et al. 2013).
- **Alternatives considered:** RNEMD/Muller-Plathe (rejected: GROMACS
  2025.4 has no verified native implementation; would require custom,
  untested swap-code engineering before the design could even be tested).
- **Unresolved issues:**
  - Exact GROMACS 2025.4 behavior when tc-grps do not cover 100% of atoms
    was not independently verified — the Rest group exists specifically
    to avoid relying on that ambiguity, not because its exact necessity
    was confirmed.
  - `gmx select` is new syntax for this project (not used in SIM-01) —
    to be verified against real `gmx select -h` output before use, not
    assumed correct.
- **User approval status:** Approved — full Stage B design accepted as
  proposed.
