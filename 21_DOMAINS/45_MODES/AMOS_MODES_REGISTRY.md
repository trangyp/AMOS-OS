---
title: AMOS Modes Master Registry
type: registry
source: 21_DOMAINS/45_MODES
origin_architect: Trang Phan
steward: Trang Phan
amos_core_target: v4.4
status: ACTIVE_REGISTRY
epistemic_class: AMOS_MODEL
conclusion_class: DERIVED
rscf:
  state: DERIVED
  claim_class: AMOS_MODEL
  provenance:
    - 21_DOMAINS/00_INDEX/DOMAIN_EXTENSION_PROTOCOL
    - 05_COGNITIVE_ORGANISM/05_COGNITIVE_ORGANISM_MOC
  scope: amos_modes
tags:
  - amos-os
  - modes
  - cognitive-modes
  - domain-modes
---

# AMOS Modes Master Registry

> **Origin Architect / Steward:** Trang Phan
> **AMOS_CORE Target:** `v4.4`
> **Conclusion Class:** `AMOS_MODEL`
> **Status:** `ACTIVE_REGISTRY`

---

## 1. Operating Modes Taxonomy

The AMOS operating system transitions dynamically across five fundamental operating modes depending on task stakes, epistemic certainty, and environmental feedback:

| Mode ID | Mode Name | Primary Focus | Invariant Stringency | Latency Profile |
| :--- | :--- | :--- | :--- | :--- |
| **MODE-01** | `EXPLORATORY` | Broad ideation, abductive hypothesis generation | Permissive ($\mathcal{C} \ge 0.50$) | Real-time interactive |
| **MODE-02** | `RIGOROUS_REASONING` | Formal deductive proofs, mathematical derivation | Strict ($\mathcal{C} \ge 0.90$) | Deliberate compute scaling |
| **MODE-03** | `CANONICAL_AUDIT` | Law compliance, axiom verification, code-fence checks | Absolute ($\mathcal{C} = 1.00$) | Barrier synchronized |
| **MODE-04** | `CRISIS_CONTAINMENT` | Fault isolation, quarantine enforcement, rollback | Fail-Closed Override | Immediate preemptive |
| **MODE-05** | `REPLAY_SYNTHESIS` | Deterministic event trace replay, historical audit | Deterministic Zero-Delta | Batch offline |

---

## 2. Mode State Machine Transitions

```mermaid
graph TD
    M1[MODE-01: EXPLORATORY] -->|Stakes Increase| M2[MODE-02: RIGOROUS_REASONING]
    M2 -->|Canon Mutation Proposed| M3[MODE-03: CANONICAL_AUDIT]
    M1 -->|Anomaly Detected| M4[MODE-04: CRISIS_CONTAINMENT]
    M2 -->|Invariant Violated| M4
    M3 -->|Audit Failure| M4
    M4 -->|Rollback Verified| M5[MODE-05: REPLAY_SYNTHESIS]
    M5 -->|Snapshot Re-established| M1
```

---

## 3. Integration

- **Domain Extension:** [[21_DOMAINS/00_INDEX/DOMAIN_EXTENSION_PROTOCOL|DOMAIN_EXTENSION_PROTOCOL]]
- **Cognitive Organism:** [[05_COGNITIVE_ORGANISM/05_COGNITIVE_ORGANISM_MOC|05_COGNITIVE_ORGANISM_MOC]]
- **Control Plane:** [[03_CONTROL_PLANE/03_CONTROL_PLANE_MOC|03_CONTROL_PLANE_MOC]]
