---
title: EXECUTION PROVENANCE
tags: [misc]
type: document
source: 11_KNOWLEDGE/misc
---


# Execution Provenance Ledger

For consequential executions capture:
`Run = [run_id, parent_run_id, command, cwd, environment_fingerprint, input_hashes, output_hashes, start_time, end_time, exit_state, stdout_ref, stderr_ref, state_hash]`

Reproduction requires compatible environment, inputs, versions, and execution semantics.

A passing run is evidence only for the exercised conditions.

---
**Related:** [[docs/moc/00-Home]] · [[docs/moc/06-Knowledge-Base-MOC]] · [[AMOS_SIMULATION_KERNEL_V0_MATH_FOUNDATIONS]] · [[SYSTEM_SCAN_AGENT]] · [[AUTOMATION_PROFILES]]

---
**MOC:** [[MISC_MOC]]
