---
title: UBI RSCF Index
type: biology
source: 11_KNOWLEDGE/03_RSCF
artifact: UBI_RSCF_INDEX.md
artifact_id: amos_11_knowledge_03_rscf_ubi_rscf_index
origin_architect: Trang Phan
steward: Trang Phan
system: AMOS OS
plane: 11_KNOWLEDGE
segment: 11_KNOWLEDGE/03_RSCF
artifact_kind: INDEX
path: 11_KNOWLEDGE/03_RSCF/UBI_RSCF_INDEX.md
tags:
- amos_os
- knowledge
- vault
- 11_knowledge
- 03_rscf
- ubi_rscf_index
- proof_capsules
- ubi_proofs
- biological_proofs
- rscf
- canon_candidate
- canon/knowledge
- 03-rscf-moc
- unified-biological-intelligence
- ubi-claim-registry
- amos-x-ubi
- 00-home
- knowledge-moc
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
  - UBI_OFFICIAL_MANUAL
  - UNIFIED_BIOLOGICAL_INTELLIGENCE
  - AMOS_CORPUS
  scope:
  - KNOWLEDGE_RSCF
  - UBI_RSCF_INDEX
  - SOURCE_DEFINED_MODEL
framework_binding:
  rscf_moc:
    artifact:
    - - 03_RSCF_MOC
  biological_master:
    artifact:
    - - UNIFIED_BIOLOGICAL_INTELLIGENCE
  claims_registry:
    artifact: 11_KNOWLEDGE/02_CLAIMS/UBI_CLAIM_REGISTRY
epistemic_boundary:
  source_presence: VERIFIED_SOURCE_PRESENCE
  index_structure: VERIFIED_SOURCE_STRUCTURE
  proof_index: SOURCE_DEFINED_MODEL
  runtime_enforcement: NOT_ESTABLISHED
---

# UBI RSCF Proof Capsule Index

`UBI_RSCF_INDEX.md` is the canonical Knowledge Plane proof index for **Unified Biological Intelligence (UBI) RSCF Capsules** within `11_KNOWLEDGE/03_RSCF`.

It catalogs verifiable proof capsules governing the 4 non-compensatory biological domains, quadratic emergence, thermodynamic entropy dissipation, and biological substrate firewalls.

---

# 1. Indexed RSCF Capsules

| Node ID | Biological Module | Claim Class | Core Equation / Invariant | Status |
| :--- | :--- | :--- | :--- | :--- |
| `RSCF-UBI-001` | UBI Core Model | `AMOS_MODEL` | $i_{\text{UBI}} = (\text{NBI} \cdot \text{NEI} \cdot \text{SI} \cdot \text{BEI})^{1/4}$ | Active |
| `RSCF-UBI-002` | UBI Quadratic Emergence | `MATHEMATICAL_MODEL` | Emergent Capability $e = i_{\text{UBI}}^2$ | Active |
| `RSCF-UBI-003` | UBI Entropy Correction | `PHYSICAL_MODEL` | Thermodynamic Dissipation ($\frac{d_e S}{dt} < 0$) | Active |
| `RSCF-UBI-004` | Biological Integrity Firewall | `SYSTEM_INVARIANT` | Substrate Protection Threshold ($\tau_{\text{crit}} = 0.2$) | Active |

---

# 2. Inter-Plane & Vault Connections

- **RSCF MOC:** [[03_RSCF_MOC]]
- **Biological Master:** [[UNIFIED_BIOLOGICAL_INTELLIGENCE]]
- **Claims Registry:** [[UBI_CLAIM_REGISTRY]]
- **Cognitive Matrix:** [[AMOS_X_UBI]]

---

# 3. RSCF Contract

```yaml
RSCF:
  node_id: amos_11_knowledge_03_rscf_ubi_rscf_index
  node_type: index
  claim_class: AMOS_MODEL
  state: SOURCE_CLAIM
  H:
    identity: "UBI RSCF Index"
    role: "Index of RSCF proof capsules across Unified Biological Intelligence"
  M:
    indexed_nodes: [RSCF-UBI-001, RSCF-UBI-002, RSCF-UBI-003, RSCF-UBI-004]
  confidence_ceiling:
    source_model: SOURCE_BOUND
    runtime: UNKNOWN
```

---

**Related:** [[00_HOME]] · [[KNOWLEDGE_MOC]] · [[03_RSCF_MOC]] · [[UNIFIED_BIOLOGICAL_INTELLIGENCE]] · [[UBI_CLAIM_REGISTRY]] · [[AMOS_X_UBI]]

---
**MOC:** [[03_RSCF_MOC]]
