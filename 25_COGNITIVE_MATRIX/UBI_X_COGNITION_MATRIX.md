---
title: "UBI x Cognition Cross-Plane Matrix"
type: cognitive_matrix
source: 25_COGNITIVE_MATRIX
artifact: "UBI_X_COGNITION_MATRIX.md"
artifact_id: "amos_25_cognitive_matrix_ubi_x_cognition_matrix"
origin_architect: "Trang Phan"
steward: "Trang Phan"
system: "AMOS OS"
plane: "25_COGNITIVE_MATRIX"
segment: "25_COGNITIVE_MATRIX"
artifact_kind: "MATRIX_TABLE"
path: "25_COGNITIVE_MATRIX/UBI_X_COGNITION_MATRIX.md"

tags:
  - amos_os
  - cognitive_matrix
  - vault
  - 25_cognitive_matrix
  - ubi_x_cognition_matrix
  - matrix_table
  - cross_plane_routing
  - rscf
  - canon_candidate
  - canon/matrix

version: "1.0.0"
updated: "2026-08-27"

status: "ACTIVE_REFERENCE"
epistemic_class: "AMOS_MODEL"
canonical_status: "SOURCE_GROUNDED_CANON_CANDIDATE"
implementation_status: "CONCEPTUAL_SOURCE_DEFINED"
validation_status: "NOT_INDEPENDENTLY_ESTABLISHED"
executable_binding: "NOT_ESTABLISHED"

ingestion_action: "NATIVE_CANON_INGESTION"
raw_source_policy: "DO_NOT_LOAD_UNLESS_REQUIRED"

rscf:
  state: SOURCE_CLAIM
  claim_class: AMOS_MODEL
  provenance:
    - 25_COGNITIVE_MATRIX/UBI_X_COGNITION
    - 11_KNOWLEDGE/05_FRAMEWORKS/UBI_COGNITION_BINDING
    - AMOS_CORPUS
  scope:
    - COGNITIVE_MATRIX
    - CROSS_PLANE_MATRIX_TABLE
    - SOURCE_DEFINED_MODEL

framework_binding:
  matrix_spec:
    artifact: "[[UBI_X_COGNITION]]"
  mind_os:
    artifact: "[[11_KNOWLEDGE/05_FRAMEWORKS/AMOS_MIND_OS_FRAMEWORK]]"

epistemic_boundary:
  source_presence: VERIFIED_SOURCE_PRESENCE
  matrix_structure: VERIFIED_SOURCE_STRUCTURE
  cross_plane_routing: SOURCE_DEFINED_MODEL
  runtime_enforcement: NOT_ESTABLISHED
---


# UBI x Cognition Cross-Plane Routing Matrix Table

`UBI_X_COGNITION_MATRIX.md` provides the routing table mapping biological cognitive load indicators to real-time inference throttling and reasoning depth controls.

---

# 1. Cognitive Load Routing Grid

| Biological State | Cognitive Mode | Max Depth | Search Policy | Action on Limit |
| :--- | :--- | :--- | :--- | :--- |
| **High Alignment ($i > 0.8$)** | Deep System 2 Synthesis | Unconstrained | Multi-Branch Superposition | Full Proof Generation |
| **Moderate Alignment ($0.5 \le i \le 0.8$)** | Balanced Reasoning | Depth $\le 5$ | Constrained Heuristic Expansion | Prunes Weak Branches |
| **Low Alignment / Fatigue ($i < 0.5$)** | Fast System 1 Path | Depth $\le 2$ | Direct Ground Invariant Match ($S_0$) | Triggers Restorative Micro-Pause |
| **Substrate Distress ($\tau < 0.2$)** | Autonomic Freeze | Depth $= 0$ | Immediate State Snapshot & Abort | Mandates Biological Rest |

---

# 2. Inter-Plane & Vault Connections

- **Matrix Specification:** [[UBI_X_COGNITION]]
- **Knowledge Binding:** [[UBI_COGNITION_BINDING]]
- **Mind OS:** [[AMOS_MIND_OS_FRAMEWORK]]

---

# 3. RSCF Contract

```yaml
RSCF:
  node_id: amos_25_cognitive_matrix_ubi_x_cognition_matrix
  node_type: matrix_table
  claim_class: AMOS_MODEL
  state: SOURCE_GROUNDED
  H:
    identity: "UBI x Cognition Matrix Table"
    role: "Routing table connecting biological alignment state to reasoning depth and search policy"
  M:
    states: [high_alignment, moderate_alignment, low_alignment, substrate_distress]
  confidence_ceiling:
    source_model: SOURCE_BOUND
    runtime: UNKNOWN
```

---

**Related:** [[00_HOME]] · [[25_COGNITIVE_MATRIX_MOC]] · [[UBI_X_COGNITION]] · [[UBI_COGNITION_BINDING]]

---
**MOC:** [[25_COGNITIVE_MATRIX_MOC]]
