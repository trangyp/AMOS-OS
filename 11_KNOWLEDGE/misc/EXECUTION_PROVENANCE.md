---
tags: [misc]
---
# Execution Provenance Ledger

For consequential executions capture:
`Run = [run_id, parent_run_id, command, cwd, environment_fingerprint, input_hashes, output_hashes, start_time, end_time, exit_state, stdout_ref, stderr_ref, state_hash]`

Reproduction requires compatible environment, inputs, versions, and execution semantics.

A passing run is evidence only for the exercised conditions.

---
**Related:** [[docs/moc/00-Home]] · [[docs/moc/06-Knowledge-Base-MOC]] · [[docs/brain/AMOS_Simulation_Kernel_v0_Math_Foundations]] · [[docs/brain/system_scan_agent]] · [[docs/brain/automation_profiles]]
