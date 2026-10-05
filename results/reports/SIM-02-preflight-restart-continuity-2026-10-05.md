# SIM-02 resource and restart-continuity preflight — 2026-10-05

## Decision status

**Execution completed; restart-continuity equivalence is not adjudicated; the
local host is not released for the long bridge.** DECISION-014 remains
unchanged. This preflight introduced no new scientific parameter or acceptance
threshold. The measured record is descriptive because DECISION-014 and the
approved bridge design ask for statistical agreement of conserved quantities
but do not freeze a numerical test for this 10 ps comparison.

No 400 K equilibrium bridge or NEMD production trajectory was launched.

## Reproducibility

- Host: Windows 11 with Ubuntu WSL2, kernel `6.18.33.2-microsoft-standard-WSL2`;
  4 logical CPUs, approximately 4.04 GB total memory and 3.52 GB available at
  inspection. Raw simulation files were written to the local C: drive
  (`/mnt/c` in WSL); the volume had about 48 GB free at inspection.
- Engine: LAMMPS `10 Dec 2025`, `/usr/bin/lmp`, OPT pair-style suffix,
  one MPI rank and one OpenMP thread. The restart reader warned that the source
  restart was written on four processors and was read on one.
- Source state: checkpoint-12 Stage-B restart, SHA-256
  `3b43042a7dceb3f774708d54a57d76bc701cff44cfe7231afea299ba8a9494ef`.
- Inputs and hashes:

| Input | SHA-256 |
|---|---|
| `simulations/SIM-02/lammps/in.preflight-restart-continuity-10ps` | `b05b9ea577c81d47172e8ff0b096a6fa35f5d580afccb3e4c88ed0be3f547fb5` |
| `simulations/SIM-02/lammps/in.preflight-restart-continuity-5ps-first` | `8316ef2e56ee527089b2af04a2344e2b10d80c8015ee06e2a4198efeb4b52017` |
| `simulations/SIM-02/lammps/in.preflight-restart-continuity-5ps-second` | `4d8a6112a72e8607f31960c7690445cb6feb50a95619756a24ffeb2a9d2a04de` |

Both branches used the same saved state and the approved one-rank Stage-C/NVE
setup. The uninterrupted branch integrated 10,000 steps. The split branch
integrated 5,000 steps, wrote a binary restart, reissued NVE and RATTLE, then
integrated 5,000 more steps. The first 5 ps samples match the uninterrupted
trace at the saved precision. All three LAMMPS processes exited 0 at step
32,000, the COM guard did not halt either branch, and each log reports zero
dangerous neighbor builds. The continuous path took `1:39:41`; the split
segments took `0:48:41` and `0:48:53`.

Raw logs, standard output, and restart binaries are preserved locally under
`results/raw/SIM-02/preflight-restart-continuity-2026-10-05/` and remain outside
Git. Their hashes, along with hashes of the source inputs and Stage-B restart,
are recorded in the tracked JSON summary. The compact paired data are tracked in
`results/tables/SIM-02-preflight-continuity-2026-10-05.csv`; rerun
`scripts/analysis/analyze_sim02_restart_continuity.py` to regenerate that table
and its JSON summary from the raw logs.

## Measurements

The analysis uses the post-preparation sample at step 22,000 and then paired
thermo samples every 1 ps through step 32,000: 11 samples per path. These
autocorrelated observations are descriptive samples, not independent
replicates.

| Measure | Uninterrupted 10 ps | Split 5 ps + restart + 5 ps |
|---|---:|---:|
| Mean sampled temperature | 403.070 K | 403.135 K |
| Sample SD of temperature | 2.852 K | 2.942 K |
| Mean sampled total energy | −33,188.728 kcal/mol | −33,189.342 kcal/mol |
| OLS total-energy slope across 10 ps | +0.1313 kcal/mol/ps | −0.0356 kcal/mol/ps |
| Endpoint minus starting sampled total energy | +2.550 kcal/mol | −0.505 kcal/mol |
| Maximum sampled COM speed | `1.600e-18 Å/fs` | `2.064e-18 Å/fs` |

At the 5 ps restart boundary (step 27,000), the first post-restart sample differs
from the pre-restart sample by `−2.412 kcal/mol` in total energy and `−0.090 K`
in temperature. The mean total-energy difference between the two 11-sample
series is `−0.613 kcal/mol` (`1.85e-5` of the absolute mean energy). Across the
six matched samples from steps 27,000–32,000, the split-minus-continuous energy
difference reaches `3.055 kcal/mol` in magnitude and has an RMS value of
`1.628 kcal/mol`. At step 29,000, the sampled temperatures differ by `6.839 K`
while total energy differs by only `0.158 kcal/mol`.

These numbers show a small mean-energy offset alongside a restart-boundary
change and diverging instantaneous states. The fitted slopes also differ in
sign, but 11 one-picosecond samples are too few and too correlated to support a
formal equivalence claim. No short-test energy threshold was frozen; the
DECISION-008 one-nanosecond energy criterion is not transferred to this
preflight.

## Interpretation and next boundary

LAMMPS documents that `fix shake`/`fix rattle` state is not written to binary
restart files and that such restarts need not be exact, while expected to give
statistically similar behavior. Its restart documentation also notes that
changing processor count can prevent exact restarts. Those facts make a
non-identical continuation unsurprising, but they do **not** identify the cause
of the measured energy jump or establish that these two short traces are
statistically equivalent. See the [LAMMPS fix shake/rattle documentation](https://docs.lammps.org/fix_shake.html)
and [read_restart documentation](https://docs.lammps.org/latest/read_restart.html).

The measured local rate from the uninterrupted test is about 1.67 steps/s.
Linear extrapolation for the approved 1.52-million-step bridge is roughly
10.5 days on this one-rank path. This is an estimate, not a measured bridge
runtime, and excludes subsequent eHEX stages. DECISION-014 says not to launch
the long bridge until a suitable sustained runtime and restart-recovery plan
are established. The local host therefore remains unsuitable for that launch.

The preflight demonstrates that the saved state can be restored and both
branches can complete with the COM guard intact. It does not resolve whether
the observed energy differences meet an unstated statistical-equivalence
criterion. Before any cloud trajectory, the campaign record needs a declared
continuity interpretation and a pinned runtime/build with durable 50 ps
restarts. No Colab session or other remote runtime was launched. Colab's
official FAQ says resource availability varies and free runtimes may run for
at most 12 hours depending on availability; that makes a free session a
candidate for a measured 50 ps recovery trial, not an assumed full-campaign
host: [Colab FAQ](https://research.google.com/colaboratory/faq.html).
