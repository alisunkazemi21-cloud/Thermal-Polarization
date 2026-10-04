# DECISION-011 — Same-restart one-rank SIM-02 continuation diagnostic

- Date: 2026-10-04
- Status: **Approved diagnostic complete; follow-up review pending**
- Depends on: DECISION-009, DECISION-010, and the checkpoint-09 raw archive

## Question

Checkpoint 10 compared four-rank and one-rank continuations, but each rank
count replayed Stage B independently from the Stage-A restart. The phase-space
state entering NVE therefore differed. This diagnostic tests the rank-count
change from one common Stage-B checkpoint.

## Approved scope

The user approved starting from the saved four-rank Stage-B restart
`results/raw/SIM-02/checkpoint-09-diagnostics/stage-b-nve/stage-b-2ps.restart`
and running only Stage-C initialization plus up to 2 ps of uncorrected NVE at
one MPI rank. Preserve the 1 fs timestep, 100-step thermo cadence, 400 K scale,
RATTLE settings, OPT suffix, one OpenMP thread, and the frozen `1e-6 Å/fs`
COM-speed ceiling. Keep momentum removal disabled throughout NVE. Do not change
any scientific parameter or restart state.

The Stage-B restart is the four-rank artifact from checkpoint 09, SHA-256
`3b43042a7dceb3f774708d54a57d76bc701cff44cfe7231afea299ba8a9494ef`.

## Measured result (2026-10-04)

The one-rank run completed 2 ps from step 22,000 to 24,000 with exit code 0;
wall time was 14:02. It produced 20 NVE samples (steps 22,100–24,000), with
temperature from 395.91302 to 406.10015 K and final temperature 400.10536 K.
Maximum sampled COM speed was `1.2638166834526734e-18 Å/fs` at step 23,600;
there were no exceedances of the `1e-6 Å/fs` ceiling.

The four-rank continuation from this same Stage-B restart exceeded the ceiling
at 100 fs (`7.144552366951081e-6 Å/fs`). The one-rank path therefore passes
while the four-rank path fails for the same saved starting restart and frozen
Stage-C/NVE protocol. This supports rank-count-sensitive numerical behavior in
the Stage-C/NVE sequence. It does not identify whether the mechanism is in
RATTLE, velocity cleanup, PPPM/MPI reductions, or another rank-dependent
operation. The full bridge remains on hold; no equilibrium or polarization
claim follows from this bounded diagnostic.

Reproducibility records are in `results/reports/SIM-02-checkpoint-11-same-restart-one-rank.md`
and `results/raw/SIM-02/checkpoint-11-same-restart-one-rank/`.

## Compute environment choice

For this controlled comparison, run on the existing Ubuntu-on-WSL LAMMPS
10 Dec 2025 installation. This holds the host and build close to the earlier
four-rank diagnostic while rank count changes. Google Colab remains an option
for larger future workloads, but its available CPU, memory, accelerators, and
runtime limits are variable; a hosted GPU is not automatically used by the
current CPU OPT build. Google's FAQ says free-tier resources and usage limits
vary and are not guaranteed; free notebooks can run for at most 12 hours,
depending on availability and usage. LAMMPS GPU acceleration requires the
relevant GPU/KOKKOS styles and build, and performance depends on the input and
hardware. See the [Colab FAQ](https://research.google.com/colaboratory/faq.html)
and [LAMMPS accelerator-package guide](https://docs.lammps.org/Speed_packages.html).
Any later cloud run must record its runtime, hardware, LAMMPS build, package
set, and input hashes, and must be benchmarked before a performance claim.

## Decision boundary

This is an implementation diagnostic only. Passing the COM ceiling does not
release the full equilibrium bridge or establish equilibrium, eHEX heat
transfer, a stationary thermal gradient, or polarization. A threshold breach
stops the run at the first sampled exceedance. This decision authorizes only
the bounded diagnostic; any full bridge release or hardware-changing compute
path requires separate review.
