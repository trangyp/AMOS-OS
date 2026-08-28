---
title: K_METACOGNITIVE_LOOP — Metacognitive Loop Kernel
type: kernel
source: 02_KERNEL/02_COGNITION
artifact_id: AMOS-OS-K-METACOGNITIVE-LOOP
canonical_name: K_METACOGNITIVE_LOOP
artifact_type: kernel_metacognition_contract
status: AMOS_MODEL
conclusion_class: AMOS_MODEL
amos_core_target: v4.4
origin_architect: Trang Phan
steward: Trang Phan
plane: 02_KERNEL
segment: 02_KERNEL/02_COGNITION
kernel_family: COGNITION
domain: metacognitive-loop
scope: AMOS_OS
created: '2026-08-25'
updated: '2026-08-28'
tags:
- amos-os
- kernel
- metacognition
- 7-step-loop
- introspective-verification
- failure-memory
- convergence-detection
- rscf/claim
- rscf/state/model
- 02-cognition-moc
- 02-kernel-moc
- 00-home
- 00-root-moc
aliases:
- Metacognitive Loop Kernel
- K_METACOGNITIVE_LOOP
- AMOS Metacognitive Loop
---

# K_METACOGNITIVE_LOOP — Metacognitive Loop Kernel

> **Origin Architect / Steward:** Trang Phan  
> **Plane:** `02_KERNEL/02_COGNITION`  
> **Status:** `AMOS_MODEL`  
> **Execution Flow:** 7-Phase Deterministic Metacognitive Verification Loop

---

## 1. Purpose and Introspective Architecture

`K_METACOGNITIVE_LOOP` governs introspective self-evaluation, loop detection, unproductive step tracking, and convergence verification across all reasoning and coding subagents. It ensures that the system actively evaluates the quality and trajectory of its own reasoning before emitting answers or committing mutations.

```
+-------------------------------------------------------------------------+
|                  7-PHASE METACOGNITIVE CONTROL LOOP                     |
|                                                                         |
|  Phase 1: INTAKE       ---> Parse Intent & Explicit Constraints         |
|         |                                                               |
|         v                                                               |
|  Phase 2: DECOMPOSE    ---> Create Directed Acyclic Task Graph (DAG)    |
|         |                                                               |
|         v                                                               |
|  Phase 3: HYPOTHESIZE  ---> Generate Competing Pathways & Scenarios     |
|         |                                                               |
|         v                                                               |
|  Phase 4: EXECUTE      ---> Run Domain Specialist Engines               |
|         |                                                               |
|         v                                                               |
|  Phase 5: EVALUATE     ---> Check Progress, Convergence, & Invariants   |
|         |                                                               |
|         v                                                               |
|  Phase 6: MITIGATE     ---> Correct Errors, Break Loops, Re-route       |
|         |                                                               |
|         v                                                               |
|  Phase 7: REFLECT      ---> Update Failure Memory & Persist Audit Receipt|
+-------------------------------------------------------------------------+
```

---

## 2. Invariant Loop Detection & Convergence Rules

1. **Loop Detection Floor:** If identical semantic state or error signature occurs $\ge 3$ times within a single trajectory, an automatic interrupt is triggered to force alternative hypothesis generation.
2. **Convergence Metric:** Productive steps must strictly decrease remaining problem entropy: $\Delta H_{\text{unresolved}}(t+1) < \Delta H_{\text{unresolved}}(t)$.
3. **Failure Memory Persistence:** Every non-productive step or failed execution branch must record an entry in [[K_FAILURE_RECOVERY]] to prevent repeat exploration.

---

## 3. Epistemic Verification Gates

Before exiting Phase 5 (Evaluate):
- **Gate 1 (Axiom Check):** Does the candidate output violate any constitutional meta-law?
- **Gate 2 (Constraint Check):** Are all user-specified negative constraints and bounds satisfied?
- **Gate 3 (Grounding Check):** Is every factual assertion grounded in verifiable citations or verified execution traces?
- **Gate 4 (Completeness Check):** Have all required sub-tasks in the DAG been resolved?

---

## 4. Cross-Plane Bindings

- **Cognitive Infrastructure:** [[K_METACOGNITION]] · [[K_STRUCTURAL_REASONING]] · [[K_MULTI_HYPOTHESIS]]
- **Self-Correction & Memory:** [[K_FAILURE_RECOVERY]] · [[K_ANTI_AUTOPOISONING]] · [[K_FAIL_CLOSED]]
- **Navigation:** [[00_HOME]] · [[02_KERNEL_MOC]] · [[02_COGNITION_MOC]] · [[00_ROOT_MOC]]

---
**MOC:** [[02_COGNITION_MOC]]

