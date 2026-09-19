# YouTube Roadmap — Thermal Polarization → Electrical Work

Format: a documentary-style research series, following the actual
chronological process (including real failures), not a polished
after-the-fact summary. Authenticity is the hook.

---

## Episode 1 — "Can Heat Make Electricity, Just From Water?"
**Hook:** open on the central research question, cold — no context yet.
- The physical chain: ∇T → J_Q → P → E → V_OC → I → P_out
- What's ESTABLISHED (literature) vs. what's the actual open question
- Introduce the six core papers (Bresme 2008 → Bedeaux 2025) briefly
- End on: "Before we can even ask if this makes electricity, we have to
  prove our simulation can reproduce known water behavior first."
**Visual:** Research Book's causal-chain diagram (screen-recorded,
interactive) as the spine of the episode.
**Data to reference:** the six-paper literature hierarchy, Checkpoint 01.

## Episode 2 — "Building a Water Simulation From Scratch"
- What SPC/E actually is (rigid 3-site model, SETTLE constraints)
- Why we self-contained the force field instead of trusting a bundled one
- The four-stage protocol: EM → NVT → NPT → production
- Show the actual .itp/.mdp files on screen
**Visual:** the geometry ASCII diagram from the Simulation Log; the
spce.itp file itself, annotated.
**Data:** Berendsen et al. 1987 parameters (q, sigma, epsilon).

## Episode 3 — "It Crashed. Reinstalling GROMACS Didn't Fix It."
**Hook:** the segfault. This is your best retention episode — a real,
unresolved technical mystery with a satisfying payoff.
- Show the actual segfault, the failed reinstall attempt
- The reveal: `[ molecules ]` still had a placeholder — `__N_SOL_TBD__`
- Why that specific kind of bug can crash instead of erroring cleanly
**Visual:** terminal recording of the crash, then the one-line `sed` fix.
**Data:** FAILED-001-grompp-segmentation-fault.md, in full — read it on
camera, it's a genuine lab-notebook artifact.

## Episode 4 — "Watching Water Find Its Temperature"
- Running EM → NVT → NPT for real, on screen
- Explain equipartition: why 7.9 K of temperature *noise* is a GOOD sign,
  not an error — the system matching theoretical fluctuation prediction
- Side-note: the CPU heat/throttling check (relatable, human moment —
  "am I going to fry my laptop running this?")
**Visual:** density_temperature.png (once generated for this run);
HWiNFO64 screenshot.
**Data:** NVT T = 299.905 K, RMSD 7.90 K vs. predicted 7.68 K; NPT density
995.8 kg/m^3 (relaxing up from 976 kg/m^3 pre-equilibration).

## Episode 5 — "My Diffusion Coefficient Was 140x Too Small"
**Hook:** another real bug, different kind — silent wrong-answer, not a
crash. Great "MD simulations lie to you if you're not careful" narrative.
- Production run, RDF result (passes cleanly, quick win)
- Then diffusion: D = 1.9e-11 instead of ~2.7e-9
- The periodic-boundary-wrapping explanation, with a simple animation
  (a molecule "teleporting" across the box edge)
- Fix: `gmx trjconv -pbc nojump`, corrected result lands in range
**Visual:** msd_oxygen.png, before/after; a simple box-wrapping diagram.
**Data:** DECISION-002-msd-pbc-wrapping-correction.md, in full.

## Episode 6 — "Checkpoint 01: What We Actually Know Now"
- Walk the full comparison table: all 5 measured values vs. literature
- Explicitly state what SIM-01 does NOT claim (no thermopolarization,
  no voltage/current/power — still an open question)
- Tease SIM-02: three NEMD method choices, why the choice matters
**Visual:** the Research Book's Checkpoint 01 panel, live on screen.
**Data:** full SIM-01-validation.md comparison table.

## Future episodes (once SIM-02/03 exist)
- "Imposing a Thermal Gradient on Water" (SIM-02 method selection + build)
- "Is There Actually a Voltage?" (V_OC measurement)
- "Closing the Circuit" (SIM-03, the actual power question)

---

## Cross-cutting production notes
- Every episode should end by literally opening the Research Book /
  Simulation Log live and showing the real, current state — the "online
  notebook" becomes a recurring visual anchor across the whole series.
- Pull B-roll straight from real terminal sessions — don't restage the
  bugs, the actual first-time confusion is the content.
- Each episode maps to one or two DECISION-*.md / FAILED-*.md files —
  read from them directly on camera for authenticity and citability.
