# Wirnsberger et al. (2016) reproduction notes

- **Paper:** Wirnsberger, Dellago, Frenkel, and Reinhardt, *J. Chem. Phys.*
  **144**, 224102 (2016), DOI 10.1063/1.4953036
- **Author package:** Cambridge Data Repository, DOI 10.17863/CAM.118
- **Inspected:** 2026-09-30
- **Evidence class:** `[ESTABLISHED]` published paper and author-supplied files;
  no project simulation has been run from them

## Why this source matters

The paper and its author package provide a reproducible 400 K SPC/E eHEX
benchmark close to SIM-02. The package contains LAMMPS input, an equilibrated
structure, analysis code, and trajectory material. These notes transcribe the
scientific parameters needed for design review; they do not import the package
as project results.

## Published benchmark recovered from the sources

| Quantity | Published value | Provenance note |
|---|---:|---|
| Molecules / atoms | 4,500 / 13,500 | author data file and paper |
| Box | 36.3534308725 × 36.3534308725 × 109.060578798 Å³ | author data file |
| Volume | 144,131.400286 Å³ | calculated from data-file bounds |
| Mean density | 0.934 g cm⁻³ | paper; independently recovered from count and volume |
| Mean temperature | 400 K | paper and input |
| Water model | rigid SPC/E | paper and input |
| Lennard-Jones cutoff | 11 Å | paper and input |
| Long-range solver | Ewald, relative precision 10⁻⁵ | paper and input |
| Constraint method | RATTLE, tolerance 10⁻¹⁰, 400 iterations | author input |
| eHEX exchange rate | ±0.1614 kcal mol⁻¹ fs⁻¹ | author input |
| eHEX options | every step; molecular COM constrained | author input, translated to current syntax |
| Production timestep | 2 fs | paper and input |
| Hot reservoir | two 4 Å edge slabs, 8 Å total across periodic z boundary | author input |
| Cold reservoir | central slab from z = −4 to +4 Å, 8 Å total | author input |
| Heat flux per branch | 4.243 × 10¹⁰ W m⁻² | paper Table I; also recovered from F/(2A) |
| Reported gradient | −5.14 ± 0.04 K Å⁻¹ | paper Table I |
| NEMD transient / production | 10 ns / 60 ns | paper |
| Production blocks | 600 × 100 ps | paper |
| Reported energy change | approximately 0.005% | paper |

The factor of two in the heat-flux conversion is required because energy leaves
the periodic hot reservoir along two symmetric transport branches:

\[
J_q = \frac{F}{2L_xL_y}.
\]

With `F = 0.1614 kcal mol⁻¹ fs⁻¹` and the published transverse area, this gives
`4.2425 × 10¹⁰ W m⁻²`, consistent with the paper's rounded value.

## Equilibration and sampling chronology

`[ESTABLISHED]` The published preparation used 20 ps of velocity rescaling,
200 ps NpT with Nosé–Hoover relaxation times of 1 ps for temperature and 2.5 ps
for pressure, rescaling to the final dimensions, 500 ps NVT, then 1 ns NVE. The
authors report an NVE mean of 400 ± 0.1 K and checked structural and dielectric
properties before NEMD.

The author input records temperature and oxygen-density profiles in 120 bins
(`Δz = 0.9088 Å`) and writes coordinates every 25 steps, or 50 fs at the 2 fs
timestep. The paper presents temperature/density at 2.73 Å resolution and
multipole densities at 5.45 Å resolution. It warns that substantially finer
spatial resolution increases statistical uncertainty.

## Translation boundaries for SIM-02

- `[PROPOSED]` Use PPPM at relative precision 10⁻⁵ because the installed modern
  LAMMPS build supports it. The paper used Ewald at the same stated precision,
  so this is an implementation translation that must pass an equilibrium and
  field-profile bridge.
- `[PROPOSED]` Begin the project pilot at 1 fs and compare a matched 2 fs segment
  before adopting the published 2 fs production timestep.
- `[OPEN]` The published 50 fs coordinate cadence is expensive for a long ASCII
  trajectory. Storage format and the minimum cadence needed for polarization
  statistics remain part of the production decision.

## Primary links

- [Published paper](https://discovery.ucl.ac.uk/1518730/10/Saric_1.4953036.pdf)
- [Author replication package](https://www.repository.cam.ac.uk/items/cd3afc20-0c58-4319-bf34-0437eb62c92c)
- [LAMMPS eHEX documentation](https://docs.lammps.org/latest/fix_ehex.html)
- [LAMMPS SPC/E documentation](https://docs.lammps.org/Howto_spc.html)

