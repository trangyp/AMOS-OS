---
title: K_COGNITION_NBI — Neurobiological Intelligence (NBI) Kernel
type: kernel
source: 02_KERNEL/02_COGNITION
artifact_id: AMOS-OS-K-COGNITION-NBI
canonical_name: K_COGNITION_NBI
artifact_type: kernel_ubi_contract
status: AMOS_MODEL
conclusion_class: AMOS_MODEL
amos_core_target: v4.4
origin_architect: Trang Phan
steward: Trang Phan
plane: 02_KERNEL
segment: 02_KERNEL/02_COGNITION
kernel_family: COGNITION
domain: neurobiological-intelligence
scope: AMOS_OS
created: '2026-08-25'
updated: '2026-08-28'
tags:
- amos-os
- kernel
- ubi
- nbi
- neurobiological-intelligence
- cognitive-load
- attention-allocation
- working-memory-capacity
- rscf/claim
- rscf/state/model
- 02-cognition-moc
- 02-kernel-moc
- 00-home
- 00-root-moc
aliases:
- Neurobiological Intelligence Kernel
- NBI Kernel
- K_COGNITION_NBI
- UBI NBI Domain Contract
---

# K_COGNITION_NBI — Neurobiological Intelligence (NBI) Kernel

> **Origin Architect / Steward:** Trang Phan  
> **Plane:** `02_KERNEL/02_COGNITION`  
> **Status:** `AMOS_MODEL`  
> **UBI Domain:** Domain 1 — Neurobiological Intelligence™ (NBI)

---

## 1. Purpose and Neural Substrate

`K_COGNITION_NBI` governs neural bandwidth modeling, attention budget allocation, working memory compaction, and cognitive fatigue thresholds within the **Unified Biological Intelligence™ (UBI)** framework. It ensures that synthetic reasoning processes respect biological cognitive limits and do not induce catastrophic cognitive overload ($\Omega_{\text{cog}}$).

```
+-------------------------------------------------------------------------+
|                  NBI COGNITIVE BANDWIDTH GOVERNOR                       |
|                                                                         |
|  [ Inbound Task Stream ] ---> ( Miller/Cowan Capacity Filter: 7 ± 2 )   |
|                                         |                               |
|                                         v                               |
|                     ( Active Attention Budgeting Engine )               |
|                                         |                               |
|                +------------------------+------------------------+      |
|                |                                                 |      |
|     [ Within Working Memory ]                          [ Cognitive Overload ]
|                |                                                 |      |
|                v                                                 v      |
|    ( Parallel Path Evaluation )                     ( Context Compaction & Chunk )|
|                |                                                 |      |
|                v                                                 v      |
|    [ High-Fidelity Execution ]                      [ Preserve Attentional Focus ]|
+-------------------------------------------------------------------------+
```

---

## 2. Invariant Laws of NBI

1. **Working Memory Capacity Floor ($K_{\text{WM}}$):** Simultaneous active hypotheses in uncompacted working memory are bounded by $K_{\text{WM}} \le 7$ to prevent cross-hypothesis interference.
2. **Cognitive Load Ceiling:** When operational load $\Omega_{\text{cog}} = \frac{\text{TaskComplexity}}{\text{AvailableBandwidth}} > 0.85$, trigger automatic [[K_CONTEXT_COMPACTION]].
3. **Attention Allocation Law:** Attention weights across competing sub-problems must sum to unity ($\sum w_i = 1$) with zero negative allocations.

---

## 3. Cognitive Load Throttling Formulation

Let $\mathcal{T}$ be a task with depth $d$ and branching factor $b$. Cognitive load $\Omega_{\text{cog}}$ is computed as:

$$\Omega_{\text{cog}} = \frac{\sum_{i=1}^n \left( \text{Depth}(T_i) \cdot \log_2(\text{Breadth}(T_i)) \right)}{\mathcal{B}_{\text{neural}}}$$

- When $\Omega_{\text{cog}} \ge 0.85$: Switch speed tier to `precision_priority`, serialize sub-tasks, and compact intermediate memory.

---

## 4. Cross-Plane Bindings

- **UBI Framework:** [[BIO_LOGICAL_COMPUTING_MODEL]] · [[K_EMOTION_NEI]] · [[K_SOMATIC_SI]] · [[K_BIOELECTROMAGNETIC_BEI]]
- **Cognition & Memory:** [[K_CONTEXT_COMPACTION]] · [[K_MEMORY_ADMISSION]] · [[K_STRUCTURAL_REASONING]]
- **Control & Homeostasis:** [[K_CONTROL_PLANE]] · [[K_UBI_HOMEOSTASIS]] · [[K_FAIL_CLOSED]]
- **Navigation:** [[00_HOME]] · [[02_KERNEL_MOC]] · [[02_COGNITION_MOC]] · [[00_ROOT_MOC]]

---
**MOC:** [[02_COGNITION_MOC]]
