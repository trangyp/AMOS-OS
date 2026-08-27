---
title: "AMOS RSCF Index"
type: rscf
source: 11_KNOWLEDGE/03_RSCF
artifact: "AMOS_RSCF_INDEX.md"
artifact_id: "amos_11_knowledge_03_rscf_amos_rscf_index"
origin_architect: "Trang Phan"
steward: "Trang Phan"
system: "AMOS OS"
plane: "11_KNOWLEDGE"
segment: "11_KNOWLEDGE/03_RSCF"
artifact_kind: "INDEX"
path: "11_KNOWLEDGE/03_RSCF/AMOS_RSCF_INDEX.md"

tags:
  - amos_os
  - knowledge
  - vault
  - 11_knowledge
  - 03_rscf
  - amos_rscf_index
  - proof_capsules
  - rscf_nodes
  - rscf
  - canon_candidate
  - canon/knowledge

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
    - 03_RSCF_MOC
    - AMOS_CORPUS
  scope:
    - KNOWLEDGE_RSCF
    - AMOS_RSCF_INDEX
    - SOURCE_DEFINED_MODEL

framework_binding:
  rscf_moc:
    artifact: "[[03_RSCF_MOC]]"
  brain_os:
    artifact: "11_KNOWLEDGE/AMOS_FULL_BRAIN_OS_ARCHITECTURE"

epistemic_boundary:
  source_presence: VERIFIED_SOURCE_PRESENCE
  index_structure: VERIFIED_SOURCE_STRUCTURE
  proof_index: SOURCE_DEFINED_MODEL
  runtime_enforcement: NOT_ESTABLISHED
---


# AMOS OS RSCF Proof Capsule Index

`AMOS_RSCF_INDEX.md` is the canonical Knowledge Plane proof index for **AMOS OS Architecture RSCF Capsules** within `11_KNOWLEDGE/03_RSCF`.

It tracks the verifiable proof headers, epistemic classifications, and confidence bounds of the core AMOS OS subsystems.

---

# 1. Indexed RSCF Capsules

| Node ID | Subsystem | Claim Class | Invariant / Boundary | Status |
| :--- | :--- | :--- | :--- | :--- |
| `RSCF-AMOS-001` | Full Brain OS Architecture | `AMOS_MODEL` | 6 Hard System Constraints | Active |
| `RSCF-AMOS-002` | Organism OS Architecture | `AMOS_MODEL` | Living Metabolic Substrate | Active |
| `RSCF-AMOS-003` | Mind OS Architecture | `AMOS_MODEL` | Epistemic Metacognition | Active |
| `RSCF-AMOS-004` | Canonical Agent Mesh | `SYSTEM_INVARIANT` | $\text{Capability} \neq \text{Authority}$ | Active |

---

# 2. Inter-Plane & Vault Connections

- **RSCF MOC:** [[03_RSCF_MOC]]
- **Full Brain OS:** [[AMOS_FULL_BRAIN_OS_ARCHITECTURE]]
- **Cognitive Matrix:** [[25_COGNITIVE_MATRIX_MOC]]

---

# 3. RSCF Contract

```yaml
RSCF:
  node_id: amos_11_knowledge_03_rscf_amos_rscf_index
  node_type: index
  claim_class: AMOS_MODEL
  state: SOURCE_CLAIM
  H:
    identity: "AMOS RSCF Index"
    role: "Index of RSCF proof capsules across core AMOS OS architecture"
  M:
    indexed_nodes: [RSCF-AMOS-001, RSCF-AMOS-002, RSCF-AMOS-003, RSCF-AMOS-004]
  confidence_ceiling:
    source_model: SOURCE_BOUND
    runtime: UNKNOWN
```

---

**Related:** [[00_HOME]] · [[KNOWLEDGE_MOC]] · [[03_RSCF_MOC]] · [[AMOS_FULL_BRAIN_OS_ARCHITECTURE]]

---
**MOC:** [[03_RSCF_MOC]]
