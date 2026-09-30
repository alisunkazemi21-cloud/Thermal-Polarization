# SIM-02 LAMMPS eHEX design — discussion draft

- **Date opened:** 2026-09-30
- **Status:** Temperature sequence approved; detailed inputs and production remain gated
- **Engine decision:** DECISION-005

## Research question

Can rigid SPC/E water under a controlled, stationary heat flux develop a
reproducible signed polarization profile that exceeds block uncertainty?

## Minimal experiment shape

Use a periodic elongated water box. Add energy in a hot reservoir split across
the periodic z boundary and remove the same amount in a central cold reservoir.
This creates two mirror-related transport branches. Run NVE plus eHEX after
equilibrium preparation, then fold the two branches only after checking their
unfolded agreement.

## Proposed parameters for discussion

| Item | Proposal | Basis/status |
|---|---|---|
| Model | rigid SPC/E | Reuse SIM-01 parameters; official LAMMPS recipe available |
| Integrator | velocity Verlet + RATTLE | Required for highest eHEX constraint accuracy |
| Timestep | 1 fs initially | Conservative literature-compatible choice; 2 fs may be tested later |
| Electrostatics | `lj/cut/coul/long` + PPPM, 11 Å real-space cutoff, accuracy 10⁻⁵ | Deliberate modern translation from the published Ewald benchmark |
| System size | 4,500 waters; 36.3534308725 × 36.3534308725 × 109.060578798 Å³ | Exact author-package benchmark |
| Long dimension | 109.060578798 Å along z | Exact author-package benchmark |
| Reservoir thickness | hot: 4 Å at each periodic edge; cold: central 8 Å | Exact author-package benchmark |
| Ensemble | NPT preparation → fixed-volume NVE+eHEX | Avoid barostatting a nonequilibrium gradient |
| eHEX options | every step, `constrain com` | Dynamic molecular membership with constrained water |
| Spatial bins | acquire at 0.9088 Å; report merged 2.73 Å and 5.45 Å views | Author input and published presentation resolutions |
| Startup | staged 100 ps smoke test then 1 ns stationarity pilot | Checkpoint release before published-scale allocation |
| Published reference | 10 ns transient plus 60 ns production | Target only after pilot evidence justifies it |

## Decisions still open

### Mean temperature

`[DECIDED]` A direct method-validation run near 400 K offers the clearest comparison
with the 2013 SPC/E study. A 300 K run is more relevant to the project's ambient
goal but intersects the later literature on temperature-dependent sign inversion.

**Approved path:** first validate the eHEX implementation against one published
400 K condition, then run one 300 K target condition only if the method-validation
checkpoint passes. This is a two-condition validation path, not a parameter sweep
(DECISION-006).

### Heat rate

`[PROPOSED]` Use the recovered benchmark rate of ±0.1614 kcal mol⁻¹ fs⁻¹.
Dividing by twice the published transverse area gives
4.243 × 10¹⁰ W m⁻² per symmetric transport branch, matching the paper.

### Exact dimensions and molecule count

`[PROPOSED]` Reproduce the author-package system: 4,500 molecules and the exact
box listed above. The recovered count and volume independently give the
published density of 0.934 g cm⁻³.

### Replication

`[OPEN]` The first production estimate needs block uncertainty. An independent
seed replicate becomes mandatory before a positive polarization claim is called
reproducible; a pilot or unresolved null result may stop earlier.

## Required observables

- unfolded and folded T(z), with correct constrained-water degrees of freedom;
- mass density ρ(z);
- imposed heat rate and heat flux Jq;
- signed molecular orientation <cos θ(z)>;
- signed polarization Pz(z) in C/m² and an explicitly stated dipole convention;
- Pz versus ρ and density-normalized orientation/polarization;
- total energy drift and hot/cold energy balance;
- block means and uncertainty for every profile.

## Pilot acceptance gate

Production remains blocked until a short run demonstrates:

1. correct molecule count, density, charges, geometry, and neutrality;
2. stable constraints and acceptable NVE/eHEX energy behavior;
3. equal-and-opposite reservoir energy transfer;
4. no reservoir overlap and adequate molecules per reservoir;
5. a physically smooth, symmetric temperature profile away from reservoirs;
6. stable density without cavitation or dominant interface artifacts;
7. correct sign conventions and analysis on a synthetic/controlled trajectory.

## Expected files after approval

```text
simulations/SIM-02/lammps/
  README.md
  spce.mol
  in.build
  in.equilibrate
  in.ehex-pilot
  in.ehex-production
  metadata.yaml
scripts/analysis/
  analyze_sim02_profiles.py
notebooks/
  sim02_research.py
```

No simulation result is asserted in this design document.

The exact staged proposal is recorded in
`research/designs/SIM-02-checkpoint-07-protocol-freeze.md`.
