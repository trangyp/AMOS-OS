---
title: UBI Claim Registry
type: biology
source: 11_KNOWLEDGE/02_CLAIMS
artifact: UBI_CLAIM_REGISTRY.md
artifact_id: amos_11_knowledge_02_claims_ubi_claim_registry
origin_architect: Trang Phan
steward: Trang Phan
system: AMOS OS
plane: 11_KNOWLEDGE
segment: 11_KNOWLEDGE/02_CLAIMS
artifact_kind: REGISTRY
path: 11_KNOWLEDGE/02_CLAIMS/UBI_CLAIM_REGISTRY.md
tags:
- amos-os
- knowledge
- vault
- 02_claims
- ubi_claim_registry
- biological_claims
- ubi
- non_compensatory_claims
- rscf
- canon_candidate
- canon/knowledge
- unified-biological-intelligence
- ubi-entropy-correction
- absolute-biological-integrity-framework
- amos-ubi-super-engine
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
  - KNOWLEDGE_CLAIMS
  - UBI_CLAIMS
  - SOURCE_DEFINED_MODEL
framework_binding:
  claims_moc:
    artifact:
    - - 02_CLAIMS_MOC
  rscf_index:
    artifact: 11_KNOWLEDGE/03_RSCF/UBI_RSCF_INDEX
  biological_master:
    artifact:
    - - UNIFIED_BIOLOGICAL_INTELLIGENCE
epistemic_boundary:
  source_presence: VERIFIED_SOURCE_PRESENCE
  registry_structure: VERIFIED_SOURCE_STRUCTURE
  claim_catalog: SOURCE_DEFINED_MODEL
  runtime_enforcement: NOT_ESTABLISHED
---

# UBI Claim Registry

`UBI_CLAIM_REGISTRY.md` is the canonical Knowledge Plane reference registry for **Unified Biological Intelligence Claims** within `11_KNOWLEDGE/02_CLAIMS`.

It catalogues and classifies all formal assertions concerning the 4 non-compensatory biological domains, quadratic emergence ($e = i^2$), and living substrate firewalls.

---

# 1. Registered UBI Claims

| Claim ID | Source Artifact | Claim Assertion | Epistemic Class | Status |
| :--- | :--- | :--- | :--- | :--- |
| `CLM-UBI-001` | [[11_KNOWLEDGE/05_FRAMEWORKS/UNIFIED_BIOLOGICAL_INTELLIGENCE|UNIFIED_BIOLOGICAL_INTELLIGENCE]] | Non-Compensatory Law: $i = (\text{NBI} \cdot \text{NEI} \cdot \text{SI} \cdot \text{BEI})^{1/4}$ | `AMOS_MODEL` | Grounded |
| `CLM-UBI-002` | [[11_KNOWLEDGE/05_FRAMEWORKS/UNIFIED_BIOLOGICAL_INTELLIGENCE|UNIFIED_BIOLOGICAL_INTELLIGENCE]] | Quadratic Emergence: Emergent capability $e = i^2$ | `MATHEMATICAL_MODEL` | Grounded |
| `CLM-UBI-003` | [[11_KNOWLEDGE/05_FRAMEWORKS/UBI_ENTROPY_CORRECTION|UBI_ENTROPY_CORRECTION]] | Thermodynamic Dissipation: Living systems export entropy ($\frac{d_e S}{dt} < 0$) | `PHYSICAL_MODEL` | Grounded |
| `CLM-UBI-004` | [[11_KNOWLEDGE/05_FRAMEWORKS/ABSOLUTE_BIOLOGICAL_INTEGRITY_FRAMEWORK|ABSOLUTE_BIOLOGICAL_INTEGRITY_FRAMEWORK]] | Substrate Veto: Biological distress signals override AI task queues | `SYSTEM_INVARIANT` | Grounded |

---

# 2. Inter-Plane & Vault Connections

- **Claims MOC:** [[11_KNOWLEDGE/02_CLAIMS/02_CLAIMS_MOC|02_CLAIMS_MOC]]
- **RSCF Proof Index:** `11_KNOWLEDGE/03_RSCF/UBI_RSCF_INDEX`
- **Biological Master:** [[11_KNOWLEDGE/05_FRAMEWORKS/UNIFIED_BIOLOGICAL_INTELLIGENCE|UNIFIED_BIOLOGICAL_INTELLIGENCE]]
- **Super Engine:** [[11_KNOWLEDGE/05_FRAMEWORKS/AMOS_UBI_SUPER_ENGINE|AMOS_UBI_SUPER_ENGINE]]

---

# 3. RSCF Contract

```yaml
RSCF:
  node_id: amos_11_knowledge_02_claims_ubi_claim_registry
  node_type: registry
  claim_class: AMOS_MODEL
  state: SOURCE_CLAIM
  H:
    identity: "UBI Claim Registry"
    role: "Central catalog of formal assertions regarding Unified Biological Intelligence and non-compensatory law"
  M:
    registered_claims: [CLM-UBI-001, CLM-UBI-002, CLM-UBI-003, CLM-UBI-004]
  confidence_ceiling:
    source_model: SOURCE_BOUND
    runtime: UNKNOWN
```

---

**Related:** [[00_ROOT/00_HOME|00_HOME]] · [[11_KNOWLEDGE/KNOWLEDGE_MOC|KNOWLEDGE_MOC]] · [[11_KNOWLEDGE/02_CLAIMS/02_CLAIMS_MOC|02_CLAIMS_MOC]] · `11_KNOWLEDGE/03_RSCF/UBI_RSCF_INDEX` · [[11_KNOWLEDGE/05_FRAMEWORKS/UNIFIED_BIOLOGICAL_INTELLIGENCE|UNIFIED_BIOLOGICAL_INTELLIGENCE]]

---
**MOC:** [[11_KNOWLEDGE/02_CLAIMS/02_CLAIMS_MOC|02_CLAIMS_MOC]]

