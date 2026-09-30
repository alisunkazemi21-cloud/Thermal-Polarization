# SIM-02 LAMMPS eHEX design — discussion draft

- **Date opened:** 2026-09-30
- **Status:** Proposed; not approved for production
- **Engine decision:** DECISION-005

## Research question

Can rigid SPC/E water under a controlled, stationary heat flux develop a
reproducible signed polarization profile that exceeds block uncertainty?

## Minimal experiment shape

Use a periodic elongated water box. Add energy in a central z reservoir and
remove the same amount in a cold reservoir split across the periodic z boundary.
This creates two mirror-related transport branches. Run NVE plus eHEX after
equilibrium preparation, then fold the two branches only after checking their
unfolded agreement.

## Proposed parameters for discussion

| Item | Proposal | Basis/status |
|---|---|---|
| Model | rigid SPC/E | Reuse SIM-01 parameters; official LAMMPS recipe available |
| Integrator | velocity Verlet + RATTLE | Required for highest eHEX constraint accuracy |
| Timestep | 1 fs initially | Conservative literature-compatible choice; 2 fs may be tested later |
| Electrostatics | `lj/cut/coul/long` + PPPM, 10 Å real-space cutoff | Consistent with SIM-01 long-range electrostatics intent |
| System size | about 1800 waters in an elongated box | Literature scale; exact transverse dimensions derive from target density |
| Long dimension | about 110 Å along z | Resolves two gradients and reservoirs |
| Reservoir thickness | 4 Å hot and 4 Å total cold region | Armstrong/Bresme protocol scale |
| Ensemble | NPT preparation → fixed-volume NVE+eHEX | Avoid barostatting a nonequilibrium gradient |
| eHEX options | every step, `constrain com` | Dynamic molecular membership with constrained water |
| Spatial bins | start near 0.5 Å, merge for statistics if needed | Literature resolution; acceptance depends on occupancy/noise |
| Startup | at least 1 ns, extended until profile stationarity | Literature baseline; stationarity decides |
| Production | plan up to 10 ns, released in blocks | Literature baseline; pilot signal/noise decides |

## Decisions still open

### Mean temperature

`[OPEN]` A direct method-validation run near 400 K offers the clearest comparison
with the 2013 SPC/E study. A 300 K run is more relevant to the project's ambient
goal but intersects the later literature on temperature-dependent sign inversion.

**Recommendation:** first validate the eHEX implementation against one published
400 K condition, then run one 300 K target condition only if the method-validation
checkpoint passes. This is a two-condition validation path, not a parameter sweep.

### Heat rate

`[OPEN]` Select one published heat-flux condition after the final cross-sectional
area is known. In LAMMPS real units, `fix ehex` takes energy per time, so the
conversion from heat flux must include the transverse area and the two symmetric
transport branches. Record the derivation and verify it independently before use.

### Exact dimensions and molecule count

`[OPEN]` Prefer approximately 1800 molecules and Lz ≈ 110 Å. Derive Lx=Ly from
the chosen mean-temperature density rather than copying a dimension that implies
the wrong density. Confirm the realized count and density after construction.

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
