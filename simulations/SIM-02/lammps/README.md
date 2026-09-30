# SIM-02 LAMMPS implementation

Status: checkpoint 07 gate 1 passed. Checkpoint 08 proposes the fixed-volume
equilibrium bridge and its zero-step input parse passed. No equilibrium or NEMD
trajectory has run under checkpoint 08.

## Provenance

`data.spce-4500.ness-ewald` is the steady-state 4,500-molecule Ewald
configuration supplied by Wirnsberger et al. with the 2016 paper's replication
package, DOI 10.17863/CAM.118. Its SHA-256 digest is recorded in
`metadata.yaml`. The package's README, original input, and GPL-3.0 license are
preserved under `reference/`.

The project input is a deliberate translation to the installed LAMMPS 10 Dec
2025 build. It uses PPPM at 10⁻⁵ instead of the source input's Ewald solver and
current `fix ehex ... constrain com` syntax. Gate 1 uses a 1 fs declared
timestep and `run 0`; therefore it does not advance the supplied state.

## Gate 1 commands

From the repository root, first run the independent structural audit:

```powershell
.venv\Scripts\python.exe scripts\validation\audit_sim02_lammps_data.py `
  simulations\SIM-02\lammps\data.spce-4500.ness-ewald `
  --json results\raw\SIM-02\checkpoint-07-zero-step\structural-audit.json `
  --report results\raw\SIM-02\checkpoint-07-zero-step\structural-audit.md
```

Then, from WSL, ask the installed LAMMPS build to parse the translated model and
evaluate thermodynamics without advancing time:

```bash
cd simulations/SIM-02/lammps
lmp -in in.zero-step \
  -log ../../../results/raw/SIM-02/checkpoint-07-zero-step/log.lammps
```

Standard output is preserved beside the log. The checkpoint passes only when
the independent audit and LAMMPS zero-step parse both pass. Temperatures and
energies printed by `run 0` describe the imported source state under the
translated force calculation; they are diagnostic values, not an equilibrated
project measurement.

Convert the LAMMPS log to a structured audit record with:

```powershell
.venv\Scripts\python.exe scripts\validation\audit_sim02_zero_step_log.py `
  results\raw\SIM-02\checkpoint-07-zero-step\log.lammps `
  --json results\raw\SIM-02\checkpoint-07-zero-step\lammps-zero-step.json
```

## Proposed gate 2 command

`in.equilibrium-bridge` replaces the imported NEMD velocities, then schedules
20 ps direct rescaling, 500 ps NVT, and 1 ns NVE at 1 fs. Its full scientific
contract is `research/designs/SIM-02-checkpoint-08-equilibrium-bridge.md`.

After checkpoint review, run from the repository root under WSL:

```bash
mkdir -p results/raw/SIM-02/checkpoint-08-equilibrium
lmp -in simulations/SIM-02/lammps/in.equilibrium-bridge \
  -log results/raw/SIM-02/checkpoint-08-equilibrium/log.lammps
```

The checked-in dry-run logs used the same input with all three `run` durations
set to zero. They verify syntax, output styles, PPPM, and RATTLE ordering; they
are not equilibrium evidence.
