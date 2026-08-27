---
title: AGENTS AMOS EXECUTION KERNEL V1
tags: [kernel]
type: document
source: 11_KNOWLEDGE/kernel
---


# AMOS Kernel Agent Contract

Use the executable AMOS kernel as the reasoning control plane.

For every nontrivial task:
1. Construct a `TaskSpec`.
2. Call the router.
3. Resolve required skill contracts.
4. Build the dependency DAG.
5. Run pre-execution gates.
6. Execute contracts in topological order.
7. Commit resulting RSCFs atomically where coupled.
8. Run final integrity/adversarial gates.
9. Return the final bounded result.

Do not bypass the kernel simply because the answer seems obvious unless the router classifies the task C0.

If a required gate fails, return `UNKNOWN/GAP`, `CONDITIONAL`, or `COMPETING` as appropriate.
Never silently downgrade a failed gate to a prose caveat.

---
**Related:** [[00_HOME]] · [[KNOWLEDGE_MOC]] · [[AMOS_SIMULATION_KERNEL_V0_MATH_FOUNDATIONS]] · [[SYSTEM_SCAN_AGENT]] · [[AUTOMATION_PROFILES]]

---
**MOC:** [[KERNEL_MOC]]
