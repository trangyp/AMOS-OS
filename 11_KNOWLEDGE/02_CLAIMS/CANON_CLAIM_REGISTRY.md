---
canon-group: meta
canon-type: framework
rscf-state: source-claim
rscf-claim: verified
rscf-provenance: AMOS_corpus
conclusion_class: AMOS_MODEL
epistemic_class: SOURCE_CLAIM
topic: Canon Claim Registry
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

# Canon Claim Registry

`CANON_CLAIM_REGISTRY.md` is the canonical Knowledge Plane reference registry for **Canon System Claims** within `11_KNOWLEDGE/02_CLAIMS`.

It registers and classifies all formal assertions made across the 01_CANON plane, indexing their epistemic boundaries, proof status, and validation dependencies.

______________________________________________________________________

## 1. Registered Canon Claims

| Claim ID        | Source Artifact                       | Claim Statement                                                                            | Epistemic Class        | Status   |
| :-------------- | :------------------------------------ | :----------------------------------------------------------------------------------------- | :--------------------- | :------- |
| `CLM-CANON-001` | `01_CANON/01_CORE_LAWS/L0_INTEGRITY`  | Law of Law: Stability $\iff$ Admissibility under ($\mathcal{C}, \mathcal{E}, \mathcal{F}$) | `AMOS_MODEL`           | Grounded |
| `CLM-CANON-002` | `01_CANON/01_CORE_LAWS/L1_REALITY`    | Reality Grounding: Physical substrate invariants cannot be overridden                      | `OBSERVATION_GROUNDED` | Grounded |
| `CLM-CANON-003` | `01_CANON/01_CORE_LAWS/L2_COGNITION`  | Cognitive Conservatism: Inference must preserve null-state invariants ($S_0$)              | `AMOS_MODEL`           | Grounded |
| `CLM-CANON-004` | `01_CANON/01_CORE_LAWS/L3_GOVERNANCE` | Authority Separation: $\text{Capability} \neq \text{Authority}$                            | `SYSTEM_INVARIANT`     | Grounded |

______________________________________________________________________

## 2. Inter-Plane & Vault Connections

- **Claims MOC:** [[11_KNOWLEDGE/02_CLAIMS/02_CLAIMS_MOC|02_CLAIMS_MOC]]
- **RSCF Proof Index:** `11_KNOWLEDGE/03_RSCF/CANON_RSCF_INDEX`
- **Canon Plane:** `01_CANON/01_CANON_MOC`
- **Core Laws:** `01_CANON/01_CORE_LAWS/01_CORE_LAWS_MOC`

______________________________________________________________________

## 3. RSCF Contract

```yaml
RSCF:
  node_id: amos_11_knowledge_02_claims_canon_claim_registry
  node_type: registry
  claim_class: AMOS_MODEL
  state: SOURCE_CLAIM
  H:
    identity: "Canon Claim Registry"
    role: "Central registration and epistemic classification for 01_CANON plane assertions"
  M:
    registered_claims: [CLM-CANON-001, CLM-CANON-002, CLM-CANON-003, CLM-CANON-004]
  confidence_ceiling:
    source_model: SOURCE_BOUND
    runtime: UNKNOWN
```

______________________________________________________________________

**Related:** [[00_ROOT/00_HOME|00_HOME]] · [[11_KNOWLEDGE/KNOWLEDGE_MOC|KNOWLEDGE_MOC]] · [[11_KNOWLEDGE/02_CLAIMS/02_CLAIMS_MOC|02_CLAIMS_MOC]] · `11_KNOWLEDGE/03_RSCF/CANON_RSCF_INDEX` · `01_CANON/01_CANON_MOC`

______________________________________________________________________

**MOC:** [[11_KNOWLEDGE/02_CLAIMS/02_CLAIMS_MOC|02_CLAIMS_MOC]]
