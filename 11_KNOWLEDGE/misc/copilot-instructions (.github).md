---
tags: [misc]
---
# AMOS Execution Kernel

This repository contains an executable AMOS reasoning kernel.

Do not treat AMOS Markdown as passive reference material. For nontrivial work, reason through the kernel state machine:

`TaskSpec -> Router -> Skill DAG -> Invariant Gates -> Skill Contracts -> RSCF Store -> Final Gate`

When modifying code:
- inspect the repository before patching;
- use the kernel's repository contract;
- preserve provenance and execution evidence;
- run tests;
- do not claim semantic correctness from execution alone.

When evidence conflicts:
- preserve competing hypotheses;
- do not force convergence;
- use a discriminating test or return COMPETING.

When a gate fails:
- do not continue as if it passed.

---
**Related:** [[docs/moc/00-Home]] · [[docs/moc/06-Knowledge-Base-MOC]] · [[docs/brain/AMOS_Simulation_Kernel_v0_Math_Foundations]] · [[docs/brain/system_scan_agent]] · [[docs/brain/automation_profiles]]
