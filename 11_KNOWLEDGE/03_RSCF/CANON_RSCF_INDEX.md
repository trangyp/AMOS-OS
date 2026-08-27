---
title: "Canon RSCF Index"
type: canon
source: 11_KNOWLEDGE/03_RSCF
artifact: "CANON_RSCF_INDEX.md"
artifact_id: "amos_11_knowledge_03_rscf_canon_rscf_index"
origin_architect: "Trang Phan"
steward: "Trang Phan"
system: "AMOS OS"
plane: "11_KNOWLEDGE"
segment: "11_KNOWLEDGE/03_RSCF"
artifact_kind: "INDEX"
path: "11_KNOWLEDGE/03_RSCF/CANON_RSCF_INDEX.md"

tags:
  - amos_os
  - knowledge
  - vault
  - 11_knowledge
  - 03_rscf
  - canon_rscf_index
  - proof_capsules
  - canon_proofs
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
    - 01_CANON/01_CANON_MOC
    - AMOS_CORPUS
  scope:
    - KNOWLEDGE_RSCF
    - CANON_RSCF_INDEX
    - SOURCE_DEFINED_MODEL

framework_binding:
  rscf_moc:
    artifact: "[[03_RSCF_MOC]]"
  canon_moc:
    artifact: "01_CANON/01_CANON_MOC"
  claims_registry:
    artifact: "11_KNOWLEDGE/02_CLAIMS/CANON_CLAIM_REGISTRY"

epistemic_boundary:
  source_presence: VERIFIED_SOURCE_PRESENCE
  index_structure: VERIFIED_SOURCE_STRUCTURE
  proof_index: SOURCE_DEFINED_MODEL
  runtime_enforcement: NOT_ESTABLISHED
---


# Canon RSCF Proof Capsule Index

`CANON_RSCF_INDEX.md` is the canonical Knowledge Plane proof index for **01_CANON Plane RSCF Capsules** within `11_KNOWLEDGE/03_RSCF`.

It tracks the proof structures, epistemic boundaries, and verification dependencies of all canonical laws and operational contracts.

---

# 1. Indexed RSCF Capsules

| Node ID | Canon Law / System | Claim Class | Governing Invariant | Status |
| :--- | :--- | :--- | :--- | :--- |
| `RSCF-CANON-001` | L0 Integrity | `AMOS_MODEL` | Law of Law ($\mathcal{C}, \mathcal{E}, \mathcal{F}$) | Active |
| `RSCF-CANON-002` | L1 Reality | `OBSERVATION_GROUNDED` | Physical Grounding Invariant | Active |
| `RSCF-CANON-003` | L2 Cognition | `AMOS_MODEL` | Cognitive Conservatism ($S_0$) | Active |
| `RSCF-CANON-004` | L3 Governance | `SYSTEM_INVARIANT` | $\text{Capability} \neq \text{Authority}$ | Active |

---

# 2. Inter-Plane & Vault Connections

- **RSCF MOC:** [[03_RSCF_MOC]]
- **Canon Plane:** [[01_CANON_MOC]]
- **Claims Registry:** [[CANON_CLAIM_REGISTRY]]

---

# 3. RSCF Contract

```yaml
RSCF:
  node_id: amos_11_knowledge_03_rscf_canon_rscf_index
  node_type: index
  claim_class: AMOS_MODEL
  state: SOURCE_CLAIM
  H:
    identity: "Canon RSCF Index"
    role: "Index of RSCF proof capsules across 01_CANON core laws"
  M:
    indexed_nodes: [RSCF-CANON-001, RSCF-CANON-002, RSCF-CANON-003, RSCF-CANON-004]
  confidence_ceiling:
    source_model: SOURCE_BOUND
    runtime: UNKNOWN
```

---

**Related:** [[00_HOME]] · [[KNOWLEDGE_MOC]] · [[03_RSCF_MOC]] · [[01_CANON_MOC]] · [[CANON_CLAIM_REGISTRY]]

---
**MOC:** [[03_RSCF_MOC]]
