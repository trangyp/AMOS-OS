---
canon-group: meta
canon-type: framework
rscf-state: source-claim
rscf-claim: verified
rscf-provenance: AMOS_corpus
conclusion_class: AMOS_MODEL
epistemic_class: SOURCE_CLAIM
topic: Canon Rscf Index
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

# Canon RSCF Proof Capsule Index

`CANON_RSCF_INDEX.md` is the canonical Knowledge Plane proof index for **01_CANON Plane RSCF Capsules** within `11_KNOWLEDGE/03_RSCF`.

It tracks the proof structures, epistemic boundaries, and verification dependencies of all canonical laws and operational contracts.

______________________________________________________________________

## 1. Indexed RSCF Capsules

| Node ID          | Canon Law / System | Claim Class            | Governing Invariant                                  | Status |
| :--------------- | :----------------- | :--------------------- | :--------------------------------------------------- | :----- |
| `RSCF-CANON-001` | L0 Integrity       | `AMOS_MODEL`           | Law of Law ($\mathcal{C}, \mathcal{E}, \mathcal{F}$) | Active |
| `RSCF-CANON-002` | L1 Reality         | `OBSERVATION_GROUNDED` | Physical Grounding Invariant                         | Active |
| `RSCF-CANON-003` | L2 Cognition       | `AMOS_MODEL`           | Cognitive Conservatism ($S_0$)                       | Active |
| `RSCF-CANON-004` | L3 Governance      | `SYSTEM_INVARIANT`     | $\text{Capability} \neq \text{Authority}$            | Active |

______________________________________________________________________

## 2. Inter-Plane & Vault Connections

- **RSCF MOC:** [[11_KNOWLEDGE/03_RSCF/03_RSCF_MOC|03_RSCF_MOC]]
- **Canon Plane:** [[01_CANON/01_CANON_MOC|01_CANON_MOC]]
- **Claims Registry:** [[11_KNOWLEDGE/02_CLAIMS/CANON_CLAIM_REGISTRY|CANON_CLAIM_REGISTRY]]

______________________________________________________________________

## 3. RSCF Contract

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

______________________________________________________________________

**Related:** [[00_ROOT/00_HOME|00_HOME]] · [[01_CANON/01_CORE_LAWS/ATOMIC_MULTI_RSCF|ATOMIC_MULTI_RSCF]] · [[02_KERNEL/K_ATOMIC_MULTI_RSCF|K_ATOMIC_MULTI_RSCF]] · [[11_KNOWLEDGE/KNOWLEDGE_MOC|KNOWLEDGE_MOC]] · [[11_KNOWLEDGE/03_RSCF/03_RSCF_MOC|03_RSCF_MOC]] · [[01_CANON/01_CANON_MOC|01_CANON_MOC]] · [[11_KNOWLEDGE/02_CLAIMS/CANON_CLAIM_REGISTRY|CANON_CLAIM_REGISTRY]]

______________________________________________________________________

**MOC:** [[11_KNOWLEDGE/03_RSCF/03_RSCF_MOC|03_RSCF_MOC]]
