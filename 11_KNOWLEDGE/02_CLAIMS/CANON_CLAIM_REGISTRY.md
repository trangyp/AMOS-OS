---
title: "Canon Claim Registry"
type: canon
source: 11_KNOWLEDGE/02_CLAIMS
artifact: "CANON_CLAIM_REGISTRY.md"
artifact_id: "amos_11_knowledge_02_claims_canon_claim_registry"
origin_architect: "Trang Phan"
steward: "Trang Phan"
system: "AMOS OS"
plane: "11_KNOWLEDGE"
segment: "11_KNOWLEDGE/02_CLAIMS"
artifact_kind: "REGISTRY"
path: "11_KNOWLEDGE/02_CLAIMS/CANON_CLAIM_REGISTRY.md"

tags:
  - amos_os
  - knowledge
  - vault
  - 11_knowledge
  - 02_claims
  - canon_claim_registry
  - epistemic_claims
  - claim_verification
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
    - 01_CANON/01_CORE_LAWS/L0_INTEGRITY
    - AMOS_CORPUS
  scope:
    - KNOWLEDGE_CLAIMS
    - CANON_CLAIMS
    - SOURCE_DEFINED_MODEL

framework_binding:
  claims_moc:
    artifact: "[[02_CLAIMS_MOC]]"
  rscf_index:
    artifact: "`11_KNOWLEDGE/03_RSCF/CANON_RSCF_INDEX`"
  core_laws:
    artifact: "`01_CANON/01_CORE_LAWS/01_CORE_LAWS_MOC`"

epistemic_boundary:
  source_presence: VERIFIED_SOURCE_PRESENCE
  registry_structure: VERIFIED_SOURCE_STRUCTURE
  claim_catalog: SOURCE_DEFINED_MODEL
  runtime_enforcement: NOT_ESTABLISHED
---


# Canon Claim Registry

`CANON_CLAIM_REGISTRY.md` is the canonical Knowledge Plane reference registry for **Canon System Claims** within `11_KNOWLEDGE/02_CLAIMS`.

It registers and classifies all formal assertions made across the 01_CANON plane, indexing their epistemic boundaries, proof status, and validation dependencies.

---

# 1. Registered Canon Claims

| Claim ID | Source Artifact | Claim Statement | Epistemic Class | Status |
| :--- | :--- | :--- | :--- | :--- |
| `CLM-CANON-001` | `01_CANON/01_CORE_LAWS/L0_INTEGRITY` | Law of Law: Stability $\iff$ Admissibility under ($\mathcal{C}, \mathcal{E}, \mathcal{F}$) | `AMOS_MODEL` | Grounded |
| `CLM-CANON-002` | `01_CANON/01_CORE_LAWS/L1_REALITY` | Reality Grounding: Physical substrate invariants cannot be overridden | `OBSERVATION_GROUNDED` | Grounded |
| `CLM-CANON-003` | `01_CANON/01_CORE_LAWS/L2_COGNITION` | Cognitive Conservatism: Inference must preserve null-state invariants ($S_0$) | `AMOS_MODEL` | Grounded |
| `CLM-CANON-004` | `01_CANON/01_CORE_LAWS/L3_GOVERNANCE` | Authority Separation: $\text{Capability} \neq \text{Authority}$ | `SYSTEM_INVARIANT` | Grounded |

---

# 2. Inter-Plane & Vault Connections

- **Claims MOC:** [[02_CLAIMS_MOC]]
- **RSCF Proof Index:** `11_KNOWLEDGE/03_RSCF/CANON_RSCF_INDEX`
- **Canon Plane:** `01_CANON/01_CANON_MOC`
- **Core Laws:** `01_CANON/01_CORE_LAWS/01_CORE_LAWS_MOC`

---

# 3. RSCF Contract

```yaml
RSCF:
  node_id: amos_11_knowledge_02_claims_canon_claim_registry
  node_type: registry
  claim_class: AMOS_MODEL
  state: SOURCE_GROUNDED
  H:
    identity: "Canon Claim Registry"
    role: "Central registration and epistemic classification for 01_CANON plane assertions"
  M:
    registered_claims: [CLM-CANON-001, CLM-CANON-002, CLM-CANON-003, CLM-CANON-004]
  confidence_ceiling:
    source_model: SOURCE_BOUND
    runtime: UNKNOWN
```

---

**Related:** [[00_HOME]] · [[KNOWLEDGE_MOC]] · [[02_CLAIMS_MOC]] · `11_KNOWLEDGE/03_RSCF/CANON_RSCF_INDEX` · `01_CANON/01_CANON_MOC`

---
**MOC:** [[02_CLAIMS_MOC]]
