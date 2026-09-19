
## Addendum — supplementary NVT diffusion leg

- **Date:** [fill in today's date]
- **Decision:** Run the primary production (md.mdp, NPT, 1 ns) as originally
  planned for density and O–O RDF validation, then append a second,
  fixed-volume NVT-only leg (md-nvt-diffusion.mdp) continuing from the
  end of that run, used only for the self-diffusion estimate.
- **Reason:** NPT volume fluctuations add noise to an MSD-based diffusion
  fit; a fixed-volume continuation gives a cleaner estimate without
  discarding the NPT run's density/RDF validity.
- **Evidence:** Flagged as an open tradeoff directly in md.mdp before any
  production run was executed (see Stage 1 notes).
- **Alternatives considered:** NPT-only production for all observables
  (rejected: diffusion noise); NVT-only for everything (rejected: would
  not validate density against the locked 1-bar target).
- **User approval status:** Approved — user selected option (b) explicitly.
