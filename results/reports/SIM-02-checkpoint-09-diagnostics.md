# SIM-02 checkpoint 09 — bounded validation results

**Date:** 2026-10-03
**Decision:** [DECISION-009](../../research/decisions/DECISION-009-SIM-02-preparation-momentum-control.md)
**Status:** Stage A and Stage B passed their short implementation checks; the
uncorrected NVE check failed the frozen COM-speed ceiling. The 1.52 ns bridge
was not relaunched.

## Stage A: 20 ps

The four-rank LAMMPS 10 Dec 2025 OPT run completed all 20,000 steps in 1:39:34.
Thermo output was requested every 100 steps. The Stage-A interval contains 200
unique integrated samples (steps 100–20,000); every reported temperature was
400 K. The maximum sampled COM speed was
`9.654782345768524e-19 Å/fs`, versus the frozen `1e-6 Å/fs` ceiling. At
constraint initialization, the largest of the two step-zero readings was
`5.9215e-7 Å/fs`; the post-velocity-cleanup reading was `4.3919e-7 Å/fs`.
Both are below the ceiling, and the integrated samples remained much lower.

The LAMMPS input continued through zero-step Stage-B/Stage-C setup after Stage A.
For the Stage-A statistic, only the first thermo row at each timestep was used;
later repeated rows at step 20,000 belong to the separate `run 0` transition
checks, not the 20 ps trajectory.

## Stage B: 2 ps transition

The follow-on run started from the saved Stage-A restart and advanced 2,000 NVT
steps at 400 K with 1 ps damping. Twenty integrated samples (steps 20,100–22,000)
completed without a LAMMPS error. Reported temperature ranged from 395.59333 K
to 408.00767 K and was 399.81022 K at the final Stage-B sample. The maximum
sampled COM speed was `8.507873362730173e-19 Å/fs`. These are short transition
observations, not a claim that the 500 ps NVT stage has equilibrated.

## Stage C/D: uncorrected NVE check

Periodic momentum correction was disabled as required. The first 100 fs sample
after entering NVE, at step 22,100, measured COM speed
`7.144552366951081e-6 Å/fs`, exceeding the `1e-6 Å/fs` ceiling. The run was
interrupted after reaching step 22,400 (0.4 ps); its largest sampled COM speed
was `8.357269209836094e-6 Å/fs`. The four recorded NVE speeds were not
monotonically increasing, but the ceiling was already violated at the first
sample. This is a failed implementation diagnostic, not an equilibrium or
physical result.

A separate zero-trajectory-step replay from the Stage-B restart reproduced the
Stage-C initialization sequence. The COM speed was approximately `7.93e-8`
before velocity adjustment and `4.88e-8 Å/fs` after the final `velocity all
zero linear` command and a zero-step evaluation. Thus the measured excursion
appeared during the subsequent NVE integration. This locates the interval of
the failure but does not identify its mechanism. RATTLE/MPI momentum transfer is
one hypothesis to test, not an established cause.

## Consequence and next decision

The approved sequence did not pass all gates, so the full equilibrium bridge
remains on hold. No NVE correction, alternative COM threshold, or physical
parameter change has been selected. The next review is documented in
[DECISION-010](../../research/decisions/DECISION-010-SIM-02-NVE-COM-drift-review.md).

Raw stdout, stderr, restart files, and the zero-step transition trace remain in
`results/raw/SIM-02/checkpoint-09-diagnostics/` and are excluded from Git. The
compact status and SHA-256 manifest there identify the captured evidence.
The replayable diagnostic inputs are tracked at
`simulations/SIM-02/lammps/in.checkpoint-09-continuation-b-nve` and
`simulations/SIM-02/lammps/in.checkpoint-09-stage-c-zero-step`.
