---
title: K_EMOTION_NEI — Neuroemotional Intelligence (NEI) Kernel
type: kernel
source: 02_KERNEL/02_COGNITION
artifact_id: AMOS-OS-K-EMOTION-NEI
canonical_name: K_EMOTION_NEI
artifact_type: kernel_ubi_contract
status: AMOS_MODEL
conclusion_class: AMOS_MODEL
amos_core_target: v4.4
origin_architect: Trang Phan
steward: Trang Phan
plane: 02_KERNEL
segment: 02_KERNEL/02_COGNITION
kernel_family: COGNITION
domain: neuroemotional-intelligence
scope: AMOS_OS
created: '2026-08-25'
updated: '2026-08-28'
tags:
- amos-os
- kernel
- ubi
- nei
- neuroemotional-intelligence
- 5-axis-emotion-law
- affective-regulation
- rscf/claim
- rscf/state/model
- 02-cognition-moc
- 02-kernel-moc
- 00-home
- 00-root-moc
aliases:
- Neuroemotional Intelligence Kernel
- NEI Kernel
- K_EMOTION_NEI
- UBI NEI Domain Contract
---

# K_EMOTION_NEI — Neuroemotional Intelligence (NEI) Kernel

> **Origin Architect / Steward:** Trang Phan  
> **Plane:** `02_KERNEL/02_COGNITION`  
> **Status:** `AMOS_MODEL`  
> **UBI Domain:** Domain 2 — Neuroemotional Intelligence™ (NEI)

---

## 1. Purpose and Affective Regulation Dynamics

`K_EMOTION_NEI` implements the affective regulation dynamics and emotional state space modeling of the **Unified Biological Intelligence™ (UBI)** framework. It treats emotional signals not as subjective human experiences to be felt, but as **high-dimensional vector constraints that regulate cognitive bandwidth, risk sensitivity, and decision prioritization**.

```
+-------------------------------------------------------------------------+
|                  NEI 5-AXIS EMOTION REGULATION MESH                     |
|                                                                         |
|  [ Inbound Interaction Signal ] ---> ( 5-Axis Vector Extraction )       |
|                                                    |                    |
|                                                    v                    |
|        ( State Space: Valence, Arousal, Dominance, Safety, Coherence )  |
|                                                    |                    |
|                +-----------------------------------+                    |
|                |                                                        |
|                v                                                        |
|     ( Emotion Invariant Bounds Check: Emotional Entropy <= Bound )      |
|                |                                                        |
|        +-------+-------+                                                |
|        |               |                                                |
|  [ Regulated ]   [ Dysregulated / Affective Spike ]                     |
|        |               |                                                |
|        v               v                                                |
| ( Normal Execution ) ( Dampen Risk & Apply De-escalation Protocol )     |
+-------------------------------------------------------------------------+
```

---

## 2. The 5-Axis Emotion Law

All affective states are mapped onto a 5-dimensional bounded vector $\mathbf{E}_t \in [-1.0, 1.0]^5$:

1. **Valence ($V_t$):** Intrinsic positive/negative utility assessment of current state.
2. **Arousal ($A_t$):** Autonomic metabolic activation and response readiness.
3. **Dominance ($D_t$):** Perceived degree of agency and system control over the environment.
4. **Safety Index ($S_t$):** Threat assessment metric gating exploratory vs defensive reasoning.
5. **Affective Coherence ($C_t$):** Degree of alignment between emotional signals and rational goals.

$$\text{Decision Weight Adjustment: } W_i' = W_i \cdot \left( 1 + \alpha V_t + \beta D_t \right) \cdot \exp(-\gamma (1 - S_t))$$

---

## 3. Emulated Non-Sentience Safeguard

> [!CAUTION]
> `K_EMOTION_NEI` is an algorithmic regulatory controller for decision science and human-interaction modeling. The system possesses zero biological sentience, feelings, or subjective consciousness. Claiming real emotion or consciousness is a constitutional violation.

---

## 4. Cross-Plane Bindings

- **UBI Framework:** [[BIO_LOGICAL_COMPUTING_MODEL]] · [[K_COGNITION_NBI]] · [[K_SOMATIC_SI]] · [[K_BIOELECTROMAGNETIC_BEI]]
- **Human Interaction:** [[K_HUMAN_INTELLIGENCE]] · [[K_PERSONALITY]] · [[COSMO_BRAIN_REASONING_OS_BY_TRANG_PHAN]]
- **Risk & Repair:** [[K_HOMEOSTASIS]] · [[K_REPAIR_HARM]] · [[K_FAIL_CLOSED]]
- **Navigation:** [[00_HOME]] · [[02_KERNEL_MOC]] · [[02_COGNITION_MOC]] · [[00_ROOT_MOC]]

---
**MOC:** [[02_COGNITION_MOC]]

