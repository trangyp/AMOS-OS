---
canon-group: meta
canon-type: framework
rscf-state: source-claim
rscf-claim: verified
rscf-provenance: AMOS_corpus
conclusion_class: AMOS_MODEL
epistemic_class: SOURCE_CLAIM
topic: Ubi Claim Registry
tags:
  - canon-group/tech-ai
  - rscf/claim
  - rscf/provenance
  - rscf/state/source-claim
  - misc
created: 2026-08-22
---
---
---

# UBI Claim Registry

`UBI_CLAIM_REGISTRY.md` is the canonical Knowledge Plane reference registry for **Unified Biological Intelligence Claims** within `11_KNOWLEDGE/02_CLAIMS`.

It catalogues and classifies all formal assertions concerning the 4 non-compensatory biological domains, quadratic emergence ($e = i^2$), and living substrate firewalls.

______________________________________________________________________

## 1. Registered UBI Claims

| Claim ID      | Source Artifact                                                        | Claim Assertion                             | Epistemic Class                                                                                  | Status               |
| :------------ | :--------------------------------------------------------------------- | :------------------------------------------ | :----------------------------------------------------------------------------------------------- | :------------------- |
| `CLM-UBI-001` | \[\[11_KNOWLEDGE/05_FRAMEWORKS/UNIFIED_BIOLOGICAL_INTELLIGENCE         | UNIFIED_BIOLOGICAL_INTELLIGENCE\]\]         | Non-Compensatory Law: $i = (\text{NBI} \cdot \text{NEI} \cdot \text{SI} \cdot \text{BEI})^{1/4}$ | `AMOS_MODEL`         |
| `CLM-UBI-002` | \[\[11_KNOWLEDGE/05_FRAMEWORKS/UNIFIED_BIOLOGICAL_INTELLIGENCE         | UNIFIED_BIOLOGICAL_INTELLIGENCE\]\]         | Quadratic Emergence: Emergent capability $e = i^2$                                               | `MATHEMATICAL_MODEL` |
| `CLM-UBI-003` | \[\[11_KNOWLEDGE/05_FRAMEWORKS/UBI_ENTROPY_CORRECTION                  | UBI_ENTROPY_CORRECTION\]\]                  | Thermodynamic Dissipation: Living systems export entropy ($\frac{d_e S}{dt} < 0$)                | `PHYSICAL_MODEL`     |
| `CLM-UBI-004` | \[\[11_KNOWLEDGE/05_FRAMEWORKS/ABSOLUTE_BIOLOGICAL_INTEGRITY_FRAMEWORK | ABSOLUTE_BIOLOGICAL_INTEGRITY_FRAMEWORK\]\] | Substrate Veto: Biological distress signals override AI task queues                              | `SYSTEM_INVARIANT`   |

______________________________________________________________________

## 2. Inter-Plane & Vault Connections

- **Claims MOC:** [[11_KNOWLEDGE/02_CLAIMS/02_CLAIMS_MOC|02_CLAIMS_MOC]]
- **RSCF Proof Index:** [[11_KNOWLEDGE/03_RSCF/UBI_RSCF_INDEX|UBI_RSCF_INDEX]]
- **Biological Master:** [[11_KNOWLEDGE/05_FRAMEWORKS/UNIFIED_BIOLOGICAL_INTELLIGENCE|UNIFIED_BIOLOGICAL_INTELLIGENCE]]
- **Super Engine:** [[11_KNOWLEDGE/05_FRAMEWORKS/AMOS_UBI_SUPER_ENGINE|AMOS_UBI_SUPER_ENGINE]]

______________________________________________________________________

## 3. RSCF Contract

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

______________________________________________________________________

**Related:** [[00_ROOT/00_HOME|00_HOME]] · [[01_CANON/01_CORE_LAWS/ATOMIC_MULTI_RSCF|ATOMIC_MULTI_RSCF]] · [[02_KERNEL/K_ATOMIC_MULTI_RSCF|K_ATOMIC_MULTI_RSCF]] · [[11_KNOWLEDGE/KNOWLEDGE_MOC|KNOWLEDGE_MOC]] · [[11_KNOWLEDGE/02_CLAIMS/02_CLAIMS_MOC|02_CLAIMS_MOC]] · [[11_KNOWLEDGE/03_RSCF/UBI_RSCF_INDEX|UBI_RSCF_INDEX]] · [[11_KNOWLEDGE/05_FRAMEWORKS/UNIFIED_BIOLOGICAL_INTELLIGENCE|UNIFIED_BIOLOGICAL_INTELLIGENCE]] · [[25_COGNITIVE_MATRIX/25_COGNITIVE_MATRIX_MOC|25_COGNITIVE_MATRIX_MOC]]

______________________________________________________________________

**MOC:** [[11_KNOWLEDGE/02_CLAIMS/02_CLAIMS_MOC|02_CLAIMS_MOC]]
