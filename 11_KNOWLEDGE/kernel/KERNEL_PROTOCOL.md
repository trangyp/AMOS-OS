---
title: KERNEL PROTOCOL
tags: [kernel, core, runtime]
type: document
source: 11_KNOWLEDGE/kernel
---




# AMOS Kernel Protocol

## 1. Intake
Normalize request into `TaskSpec` and `QueryTensor`.

## 2. Complexity
Classify C0-C4. Complexity controls validation depth, not truth standard.

## 3. Routing
Select only skills that can change the outcome.

## 4. Dependency closure
Expand contract dependencies and topologically order execution.

## 5. Gates
Pre-gates must pass. A FAIL blocks execution. CONDITIONAL is preserved.

## 6. Skill execution
Every skill receives structured state and returns typed `SkillResult`.

## 7. Proof state
Claims become RSCFs with premises, provenance, scope/regime, confidence ceilings,
competing alternatives, and falsifiers.

## 8. Transactions
Coupled RSCFs are committed atomically to the local versioned store using CAS semantics.

## 9. Fast lane
Independent local updates may avoid unnecessary coordination only when independence
is demonstrated. Unknown independence escalates.

## 10. Final gate
Hard invariant failures return UNKNOWN/GAP. Unresolved alternatives return COMPETING.
Conditional evidence returns CONDITIONAL.

## 11. Repair
Failure invalidates only dependent descendants. Rollback preserves history.

---
**Related:** [[00_HOME]] · [[KNOWLEDGE_MOC]] · [[AMOS_SIMULATION_KERNEL_V0_MATH_FOUNDATIONS]] · [[SYSTEM_SCAN_AGENT]] · [[AUTOMATION_PROFILES]]

---
**MOC:** [[KERNEL_MOC]]
