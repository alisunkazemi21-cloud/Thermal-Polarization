# SIM-02 technical report — execution record

Status: **gate 1 passed; checkpoint 08 failed its Stage-A COM criterion;
checkpoint 09 four-rank NVE failed at 100 fs. Checkpoint 11 held the Stage-B
restart fixed: one-rank Stage-C/NVE passed 2 ps, while the four-rank path
failed at 100 fs. Checkpoint 12's per-step four-rank replay crossed the COM
ceiling at 7 fs. Checkpoint 13's matched one-rank replay completed 400 fs with
maximum COM `9.653e-19 Å/fs`; at 7 fs it was `2.320e-19 Å/fs`. This supports
rank-count-sensitive behavior for the saved-state sequence, but its mechanism
remains unresolved. Checkpoint 13 closes the diagnostic branch. DECISION-014
authorizes one conditional final-results campaign. The local 10 ps
restart-continuity preflight completed without a COM halt, but statistical
equivalence is not adjudicated and the measured host is not released for the
estimated 10.5-day bridge. No equilibrium or polarization result exists yet.**
Proposed values belong in the design document until their gate is released.

## 1. Research question

Can bulk rigid SPC/E water under a controlled heat flux develop a stationary,
statistically resolved signed polarization profile?

## 2. Approved method boundary

- Engine/mechanism: LAMMPS eHEX (DECISION-005).
- Scope: gradient, heat transport, orientation, polarization.
- Electrical field, voltage, current, and power are outside SIM-02.

## 3. Configuration

`[MEASURED]` The imported author configuration contains 4,500 neutral SPC/E
molecules in a 36.3534308725 × 36.3534308725 × 109.060578798 Å³ box. The
deterministic structure audit and LAMMPS 10 Dec 2025 `run 0` passed. See
`SIM-02-checkpoint-07-zero-step.md`; no trajectory step was advanced.

## 4. Equilibrium bridge

`[FAILED AT 2 PS]` Checkpoint 08 keeps the exact author box, replaces the imported
steady-state velocities using seed `20260930`, and schedules 20 ps direct
rescaling, 500 ps NVT, and 1 ns NVE at 1 fs. Temperature, O–O RDF, constraint
stability, energy drift, z-temperature flattening, and momentum have frozen
acceptance tests.

`[MEASURED FAILURE]` The corrected four-rank OPT launch began at
2026-10-03T20:22:39+03:30 from commit `a1da7bb`. Its corrected step-zero COM
speed was `4.3903e-7 Å/fs`, below the approved `1e-6 Å/fs` ceiling. The speed
then reached `1.02778929e-5 Å/fs` at step 1,000 and `1.25105105e-5 Å/fs` at
step 2,000. The run was stopped because both values exceed the ceiling and the
increase violates the no-growth condition. No LAMMPS warning or error occurred.
See
`results/raw/SIM-02/checkpoint-08-equilibrium/run-start.json`.

`[CHECKPOINT 09 IMPLEMENTATION CHECKS]` The approved input now applies
`fix momentum 100 linear 1 1 1 rescale` only during Stage A and Stage B, with
RATTLE defined after velocity-changing fixes. Periodic momentum control is
removed before Stage D. The four-rank production-path zero-step check passed.
The 2 ps Stage-A check passed with 20 samples and maximum COM speed
`6.5634e-19 Å/fs`. The 20 ps extension passed all 20,000 steps: 200 samples at
400 K and maximum COM speed `9.6548e-19 Å/fs`. The 2 ps Stage-B continuation
ended at 399.81022 K; maximum COM speed was `8.5079e-19 Å/fs`.

`[MEASURED FAILURE]` With periodic momentum control disabled, the NVE check
exceeded the `1e-6 Å/fs` ceiling at the first 100 fs sample
(`7.1446e-6 Å/fs`). It was interrupted after 400 fs; the maximum of four
samples was `8.3573e-6 Å/fs`. A Stage-C zero-step replay ended at
`4.8769e-8 Å/fs` after the final velocity cleanup, so the excursion developed
during integration, but its mechanism remains unknown. The full bridge was not
relaunched. See
`results/reports/SIM-02-checkpoint-09-diagnostics.md`; see the completed
`results/reports/SIM-02-checkpoint-10-one-rank-nve.md` and DECISION-010.


`[MEASURED FOLLOW-UP]` On 2026-10-04, the user-approved one-rank continuation
replayed Stage B from the same Stage-A restart and completed 2 ps uncorrected
NVE. The 20 integrated NVE samples had temperatures from 392.66022 to 402.37766
K, endpoint 399.69651 K, and maximum COM speed `1.0435411502651417e-18 Å/fs`;
no sample exceeded the ceiling. The four-rank path exceeded it at 100 fs.
Because Stage B was replayed under each rank count, the resulting NVE initial
states differed; that comparison indicated rank-sensitive continuation
behavior but did not isolate the mechanism. Checkpoint 11 then used the exact
four-rank Stage-B restart. The one-rank Stage-C/NVE path completed 2 ps with
exit code 0 in 14:02; 20 samples ranged from 395.91302 to 406.10015 K and ended
at 400.10536 K. Maximum COM speed was `1.2638166834526734e-18 Å/fs` at step
23,600, with no ceiling exceedance. The four-rank run from this same restart
first breached at 100 fs (`7.144552366951081e-6 Å/fs`). This supports a
rank-count-sensitive Stage-C/NVE sequence, while the mechanism remains
unresolved. See DECISION-011 and
`results/reports/SIM-02-checkpoint-11-same-restart-one-rank.md`.

`[MEASURED FAILURE, BOUNDED]` Checkpoint 12 replayed four-rank Stage C/NVE from
the same Stage-B restart, sampled COM each 1 fs, and halted at the first
exceedance. COM speed rose at each of eight recorded samples from
`6.0282895e-8 Å/fs` after velocity cleanup to `1.1198276995146967e-6 Å/fs` at
step 22,007, 7 fs into NVE. Temperature at the halt was 401.48097 K. LAMMPS
returned exit code 0 after the configured soft halt and output finalization;
the acceptance criterion failed. The thermo total-energy column also changed
by +2.206 kcal/mol over seven steps, an exploratory observation because no
energy-drift threshold was frozen for this timing test. The per-step trace
locates the onset but does not identify its cause. The full bridge remains on
hold. See DECISION-012 and
`results/reports/SIM-02-checkpoint-12-four-rank-high-cadence.md`.

`[MEASURED BOUNDED PASS]` Checkpoint 13 replayed the same Stage-B restart at one
rank with per-step sampling. It completed 400 fs without crossing the frozen
COM ceiling; the maximum of 401 NVE states was `9.6530431e-19 Å/fs`. At the
four-rank trace's 7 fs crossing time, one-rank COM was
`2.3195258e-19 Å/fs`. Temperature ranged from 395.87137 to 407.85020 K, and the
NVE total-energy column changed by +0.690 kcal/mol. Those thermal/energy values
are exploratory because no 400 fs acceptance thresholds were frozen. This
result closes the matched rank-count diagnostic but does not release Gate 2.
See DECISION-013 and
`results/reports/SIM-02-checkpoint-13-one-rank-high-cadence.md`.

`[CAMPAIGN AUTHORIZED — LOCAL PREFLIGHT RECORDED]` DECISION-014 consolidates SIM-02 into one conditional final-results campaign.
The unchanged DECISION-008 bridge criteria, DECISION-007 eHEX gates, the
stationarity pilot, and the production evidence requirements are automatic
stop/proceed rules; no new user approval is needed between passing stages.
The local host/build and 10 ps restart-continuity execution are recorded below.
Statistical equivalence is not adjudicated, and the local runtime is unsuitable
for the 10.5-day bridge estimate. Pin a suitable sustained host and durable
restart plan before Gate 2. Stop and document the first failed gate; make no
parameter sweep.

## 5. Resource and restart-continuity preflight

`[MEASURED, DESCRIPTIVE]` On 2026-10-05, LAMMPS 10 Dec 2025 ran on one MPI rank
and one OpenMP thread under Ubuntu WSL2. Both the uninterrupted 10 ps NVE path
and split 5 ps + binary restart + 5 ps path exited 0 at step 32,000 without a
COM halt; all three component runs logged zero dangerous neighbor builds.

The 11 paired 1 ps samples have mean temperatures of 403.070 K (continuous)
and 403.135 K (split), and mean total energies of −33,188.728 and
−33,189.342 kcal/mol. The 5 ps restart boundary has a −2.412 kcal/mol energy
jump; the endpoint split-minus-continuous difference is −3.055 kcal/mol. The
fitted energy slopes differ in sign (+0.1313 versus −0.0356 kcal/mol/ps). The
test's statistical-equivalence threshold was not frozen, and the samples are
not independent replicates. The result is descriptive; the DECISION-008
1 ns energy threshold is not applied here. LAMMPS documents that RATTLE state
is not saved in binary restarts and trajectories need not restart exactly, but
this does not identify the cause of the observed difference. See the detailed
[preflight report](SIM-02-preflight-restart-continuity-2026-10-05.md), paired
table, summary JSON, and analysis script.

The measured local rate implies about 10.5 days for the 1.52-million-step
bridge. DECISION-014 requires a suitable sustained runtime and recovery plan;
this host is not released, and no long bridge was launched.

## 6. eHEX pilot

`[TO TEST]` Energy balance, heat-flux conversion, reservoir occupancy,
temperature/density profiles, symmetry, and stability.

## 7. Steady state and production

`[TO TEST]` Stationarity windows and accepted production blocks.

## 8. Results

`[TO MEASURE]` T(z), ρ(z), Jq, Pz(z), <cos θ(z)>, Pz versus ρ, and uncertainty.

## 9. Interpretation and limitations

No interpretation is permitted until the measured profiles and block
uncertainties are available.

## 10. Reproducibility record

The completed report must list the LAMMPS version, installed packages, platform,
commit, SPC/E provenance, exact inputs, seeds, box/count, heat rate, durations,
sampling, analysis version, and every non-automated operation.
