---
title: PSI Framework
type: trang-framework
source: 11_KNOWLEDGE/05_FRAMEWORKS
artifact: PSI_FRAMEWORK.md
artifact_id: amos_11_knowledge_05_frameworks_psi_framework
origin_architect: Trang Phan
steward: Trang Phan
system: AMOS OS
plane: 11_KNOWLEDGE
segment: 11_KNOWLEDGE/05_FRAMEWORKS
artifact_kind: FRAMEWORK
path: 11_KNOWLEDGE/05_FRAMEWORKS/PSI_FRAMEWORK.md
tags:
  - amos_os
  - knowledge
  - vault
  - 11_knowledge
  - 05_frameworks
  - psi_framework
  - perceived_system_integrity
  - psi
  - integrity_metrics
  - structural_auditing
  - rscf
  - canon_candidate
  - canon/knowledge
version: 1.0.0
updated: '2026-08-27'
status: ACTIVE_REFERENCE
epistemic_class: AMOS_MODEL
canonical_status: SOURCE_GROUNDED_CANON_CANDIDATE
implementation_status: CONCEPTUAL_SOURCE_DEFINED
validation_status: NOT_INDEPENDENTLY_ESTABLISHED
executable_binding: NOT_ESTABLISHED
ingestion_action: NATIVE_CANON_INGESTION
raw_source_policy: DO_NOT_LOAD_UNLESS_REQUIRED
rscf:
  state: SOURCE_CLAIM
  claim_class: AMOS_MODEL
  provenance:
    - LAWFUL_SYSTEM_PERCEPTION_MODEL
    - AMOS_CORPUS
  scope:
    - KNOWLEDGE_FRAMEWORKS
    - SYSTEMIC_INTEGRITY
    - SOURCE_DEFINED_MODEL
framework_binding:
  primary:
    name: Perceived System Integrity (PSI) Framework
    acronym: PSI
    role: SYSTEMIC_INTEGRITY_AND_COHERENCE_EVALUATION
  psi_master:
    artifact: [[PSI_MASTER]]
  structural_integrity:
    artifact: [[ABSOLUTE_STRUCTURAL_INTEGRITY]]
epistemic_boundary:
  source_presence: VERIFIED_SOURCE_PRESENCE
  framework_structure: VERIFIED_SOURCE_STRUCTURE
  psi_model: SOURCE_DEFINED_MODEL
  runtime_enforcement: NOT_ESTABLISHED
---


# PSI — Perceived System Integrity Framework

`PSI_FRAMEWORK.md` is the canonical Knowledge Plane reference artifact for the **Perceived System Integrity (PSI) Framework** within `11_KNOWLEDGE/05_FRAMEWORKS`.

PSI evaluates whether a complex organization, software architecture, or cognitive system maintains genuine structural coherence versus superficial cosmetic performance.

---

# 1. Structural Diagnostic Layers

$$\text{PSI Score } = \frac{\text{Structural Grounding } \times \text{Cohesion } (H)}{\text{Hidden Debt } \times \text{Fragmentation } (F)}$$

1. **Substrate Depth:** Does the architecture rest on validated physical and logical foundations or ephemeral prompt abstractions?
2. **Boundary Enforcement:** Are domain separations, authority boundaries (`CAPABILITY != AUTHORITY`), and access gates strictly observed?
3. **Drift Resistance:** Can the system detect and correct internal degradation without external intervention?

---

# 2. Inter-Plane & Vault Connections

- **PSI Master:** [[PSI_MASTER]]
- **Structural Integrity:** [[ABSOLUTE_STRUCTURAL_INTEGRITY]] and [[DESIGN_FOR_ABSOLUTE_INTEGRITY]]
- **Lawful Perception:** [[LAWFUL_SYSTEM_PERCEPTION_MODEL]]
- **Cognitive Matrix:** [[25_COGNITIVE_MATRIX_MOC]]

---

# 3. RSCF Contract

```yaml
RSCF:
  node_id: amos_11_knowledge_05_frameworks_psi_framework
  node_type: framework
  claim_class: AMOS_MODEL
  state: SOURCE_CLAIM
  H:
    identity: "Perceived System Integrity (PSI) Framework"
    role: "Diagnostic framework for evaluating deep structural coherence and debt resistance"
  M:
    primitives: [substrate_depth, boundary_enforcement, drift_resistance, psi_formula]
  confidence_ceiling:
    source_model: SOURCE_BOUND
    runtime: UNKNOWN
```

---

**Related:** [[00_HOME]] · [[KNOWLEDGE_MOC]] · [[05_FRAMEWORKS_MOC]] · [[PSI_MASTER]] · [[ABSOLUTE_STRUCTURAL_INTEGRITY]] · [[LAWFUL_SYSTEM_PERCEPTION_MODEL]]

---
**MOC:** [[05_FRAMEWORKS_MOC]]
