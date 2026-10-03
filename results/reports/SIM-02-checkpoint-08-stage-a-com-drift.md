# SIM-02 checkpoint 08 — Stage-A momentum acceptance failure

## Outcome

**FAIL at the first integrated diagnostic.** The corrected initialization met
the predeclared COM-speed ceiling, but Stage A did not preserve it. The run was
stopped after the step-1,000 and step-2,000 records became visible.

| Step | Time (ps) | Temperature (K) | COM speed (Å/fs) | `≤ 1e-6 Å/fs` |
|---:|---:|---:|---:|---|
| 0 | 0 | 411.10151 | 4.3903e-7 | pass |
| 1,000 | 1 | 400.0 | 1.02778929e-5 | fail |
| 2,000 | 2 | 400.0 | 1.25105105e-5 | fail |

No LAMMPS warning or error preceded the failure. Stage A's direct rescaling
controlled temperature, while the system COM speed exceeded the frozen ceiling
by factors of 10.28 and 12.51. Because the bridge stopped at 2 ps of its planned
1,520 ps, none of the equilibrium acceptance tests can be evaluated.

## Decision required before relaunch

The next checkpoint must decide how preparation-stage momentum is controlled.
A scientifically limited candidate is to remove linear momentum periodically
during thermostatted preparation only, disable that operation before the NVE
measurement, and retain the same no-growth diagnostic in NVE. This is a proposal,
not an approved parameter change. A corrected input must receive a zero-step and
short integrated production-path check before another full bridge.

Raw evidence is preserved under
`history/SIM-02-checkpoint-08-stage-a-com-drift/`; compact provenance is in
`results/raw/SIM-02/checkpoint-08-equilibrium/run-start.json`.
