# SIM-02 LAMMPS implementation

Status: checkpoint 07 gate 1 implementation. The files here define and audit
the exact published 400 K reference configuration. No equilibration or NEMD
trajectory is authorized by this gate.

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
