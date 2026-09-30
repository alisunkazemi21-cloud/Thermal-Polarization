# Long-form YouTube story — SIM-02

Working title: **We Tried to Make Water Polarize With Heat — Then Found a Flaw
Before Running the Experiment**

Target length: 45–60 minutes. Format: research documentary built from the real
chronology, including the method rejection and engine pivot.

## Audience promise

By the end, the viewer should understand:

1. what thermal polarization means at the molecular level;
2. why equilibrium validation is necessary but insufficient;
3. why a thermostat group is not automatically a spatial reservoir;
4. how eHEX imposes a measurable heat flux;
5. what evidence would distinguish polarization from noise;
6. why a null result can still be a successful experiment.

## Narrative rule

The video follows the lab timeline. Do not narrate a later discovery as if it was
known earlier. On-screen labels distinguish established literature, measured
project data, inference, hypothesis, and open questions. No placeholder curve or
illustrative animation may be styled as simulation output.

## Cold open — 0:00–2:30

**Hook:** “Can a temperature difference make ordinary water choose a direction?”

Show the causal chain one link at a time:
`gradient → heat flux → molecular polarization → possible electrical response`.
Stop visually at polarization. State that the experiment has not measured it.

Cut to the inherited GROMACS input with `tc-grps = Hot Cold Rest`, then to the
sentence: “This looked runnable. It was not the experiment we thought it was.”

## Act I — earning the right to ask the question, 2:30–13:00

### 1. The claim ladder

- Literature reports thermopolarization in water models.
- This project must reproduce ordinary SPC/E water first.
- SIM-01 checks density, temperature, O–O structure, and diffusion.
- Passing SIM-01 validates the baseline, not thermal polarization.

**Visuals:** SIM-01 comparison table; SPC/E three-site geometry; real RDF and MSD
plots; the PBC-wrapping failure and correction as a brief callback.

### 2. The next experiment

Explain a periodic elongated box, a source, a sink, and two mirror-related heat
paths. Introduce the four profiles the viewer will eventually see: T(z), ρ(z),
Pz(z), and <cos θ(z)>.

**Retention question:** “How do you keep the hot region in one place when every
water molecule is moving?”

## Act II — the inherited design fails the thought experiment, 13:00–24:00

### 3. Identity versus position

Animate ten water molecules in a slab. Color the molecules selected at time zero,
then let them diffuse. Their colors move; the slab does not. A fixed index keeps
heating identities, not the spatial region.

Show the actual GROMACS group model and `gmx select` help. Explain that dynamic
selection is available for trajectory analysis but does not redefine thermostat
membership inside `mdrun`.

### 4. Why this matters scientifically

- The intended gradient can decay or move.
- “Hot molecule” and “hot location” become different statements.
- A plausible-looking profile could answer a different physical question.

Open DECISION-004 on screen. Emphasize that rejecting a runnable-looking setup is
progress because it prevents an expensive ambiguous result.

## Act III — choosing eHEX, 24:00–34:00

### 5. What eHEX actually controls

Explain energy per time, current spatial membership, center-of-mass motion, and
equal energy added/removed. Use a simple ledger animation:

```text
hot reservoir:  +F Δt
cold reservoir: -F Δt
net imposed energy: 0
heat travels through two periodic branches
```

Describe why `constrain com` matters for a rigid water molecule: all sites move
consistently when the molecular center is inside a reservoir.

### 6. The engine pivot

Show the local capability check: LAMMPS 10 Dec 2025 with eHEX, RIGID,
SHAKE/RATTLE, and PPPM. Explain that changing engines creates a new obligation:
an equilibrium bridge back to SIM-01.

Open DECISION-005 on screen. The line to land is: “We did not change engines to
get the answer we wanted; we changed engines so the experiment asked the right
question.”

## Act IV — designing the experiment before touching Run, 34:00–43:00

Show how the author replication package replaced estimates with a reproducible
benchmark, while keeping the project proposal visibly distinct from literature:

- 4,500 waters in the exact published elongated box;
- hot slabs at the periodic edges and a cold central slab, 8 Å total each;
- ±0.1614 kcal mol⁻¹ fs⁻¹, including the factor of two in branch heat flux;
- a 1 fs conservative pilot before testing the published 2 fs timestep;
- PPPM as a documented translation from the published Ewald calculation;
- equilibrium preparation followed by NVE+eHEX;
- 400 K literature benchmark versus 300 K target;
- block uncertainty and an independent seed requirement.

Explain why 400 K is a method-validation condition and 300 K is the target, and
why this pair is not a fishing expedition or large sweep.

## Act V — execution begins, 43:00 onward

### 7. Gate 1 — proving the input exists before simulating

`[MEASURED]` Checkpoint 07 was approved and the zero-step gate passed. Show the
independent parser verifying 4,500 neutral waters, exact geometry, and COM
reservoir populations. Then show LAMMPS 10 Dec 2025 reading all atoms and
velocities, constructing 4,500 RATTLE clusters, initializing PPPM at
9.136047 × 10⁻⁶ relative accuracy, and completing zero steps.

The narration must state why zero steps matter: this proves that the imported
structure and modern syntax are internally runnable without presenting a
diagnostic temperature as an equilibrium or thermopolarization result.

### 8. Equilibrium bridge

Required footage/data: construction count, density relaxation, constraints,
energy behavior, temperature, O–O RDF, and comparison with the baseline.

The checkpoint-08 story begins with a scientific trap: the imported coordinates
are valid, but the attached velocities come from a driven steady state. Show the
404.21 K step-zero diagnostic, then wipe the velocity arrows while leaving every
molecule in place. Explain why the team did not blindly copy the paper's NpT
stage: the paper never states its target pressure, and it began from a lattice
rather than this shared snapshot.

Animate the proposed bridge as a time bar: 20 ps direct rescaling, 500 ps NVT,
one exact 400 K adjustment, then 1 ns NVE. Put the pass criteria on screen before
showing any result: temperature, fitted energy drift, molecular constraints,
flat z-temperature, O–O stationarity, and center-of-mass momentum. The audience
therefore knows what counts as success before seeing the curve.

### 9. The eHEX pilot

Required footage/data: reservoir occupancy, energy ledger, unfolded T(z), ρ(z),
symmetry, and any failed parameter choice. Preserve terminal footage of real
errors; do not recreate them later.

### 10. Is there a polarization signal?

Reveal Pz(z) only after T(z) and stationarity. Show block profiles and uncertainty
before a folded mean. Compare orientation and density to separate observation
from mechanism.

### 11. Ending logic

- If resolved: state magnitude, sign convention, uncertainty, replication, and
  limitations; do not jump to power generation.
- If unresolved: state the detection limit and which part of the causal chain was
  nevertheless validated.
- If the method fails: end with the failure boundary and the next controlled test.

## Visual inventory

| Visual | Source | Status |
|---|---|---|
| causal-chain animation | README/research book | Ready to design |
| SIM-01 comparison table | SIM-01 report/Marimo | Existing |
| fixed-identity versus spatial-region animation | DECISION-004 | To create |
| GROMACS draft close-up | `nemd-startup.mdp` | Existing historical input |
| eHEX energy ledger animation | DECISION-005/LAMMPS docs | To create |
| decision timeline | research book | Ready |
| LAMMPS capability terminal capture | environment check | Repeat on camera if desired |
| gate 1 structure and `run 0` audit | checkpoint 07 report and raw log | Existing measured evidence |
| T(z), ρ(z), Pz(z), orientation | SIM-02 notebook | Awaiting measured data |
| block uncertainty view | SIM-02 notebook | Awaiting measured data |

## Production discipline

- Record dates and commit hashes in screen captures.
- Put units and evidence labels directly on scientific graphics.
- Link every number in the script to the report table or notebook cell that
  produced it.
- Keep failed runs in the edit; they explain the final protocol.
- Update this outline after each checkpoint so narration grows with the research
  rather than being reconstructed after the outcome is known.
