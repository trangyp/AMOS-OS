---
canon-group: meta
canon-type: framework
rscf-state: source-claim
rscf-claim: verified
rscf-provenance: AMOS_corpus
conclusion_class: AMOS_MODEL
epistemic_class: SOURCE_CLAIM
topic: Amos Rscf Index
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

# AMOS OS RSCF Proof Capsule Index

`AMOS_RSCF_INDEX.md` is the canonical Knowledge Plane proof index for **AMOS OS Architecture RSCF Capsules** within `11_KNOWLEDGE/03_RSCF`.

It tracks the verifiable proof headers, epistemic classifications, and confidence bounds of the core AMOS OS subsystems.

______________________________________________________________________

## 1. Indexed RSCF Capsules

| Node ID         | Subsystem                  | Claim Class        | Invariant / Boundary                      | Status |
| :-------------- | :------------------------- | :----------------- | :---------------------------------------- | :----- |
| `RSCF-AMOS-001` | Full Brain OS Architecture | `AMOS_MODEL`       | 6 Hard System Constraints                 | Active |
| `RSCF-AMOS-002` | Organism OS Architecture   | `AMOS_MODEL`       | Living Metabolic Substrate                | Active |
| `RSCF-AMOS-003` | Mind OS Architecture       | `AMOS_MODEL`       | Epistemic Metacognition                   | Active |
| `RSCF-AMOS-004` | Canonical Agent Mesh       | `SYSTEM_INVARIANT` | $\text{Capability} \neq \text{Authority}$ | Active |

______________________________________________________________________

## 2. Inter-Plane & Vault Connections

- **RSCF MOC:** [[11_KNOWLEDGE/03_RSCF/03_RSCF_MOC|03_RSCF_MOC]]
- **Full Brain OS:** [[11_KNOWLEDGE/AMOS_FULL_BRAIN_OS_ARCHITECTURE|AMOS_FULL_BRAIN_OS_ARCHITECTURE]]
- **Cognitive Matrix:** [[25_COGNITIVE_MATRIX/25_COGNITIVE_MATRIX_MOC|25_COGNITIVE_MATRIX_MOC]]

______________________________________________________________________

## 3. RSCF Contract

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

______________________________________________________________________

**Related:** [[00_ROOT/00_HOME|00_HOME]] · [[01_CANON/01_CORE_LAWS/ATOMIC_MULTI_RSCF|ATOMIC_MULTI_RSCF]] · [[02_KERNEL/K_ATOMIC_MULTI_RSCF|K_ATOMIC_MULTI_RSCF]] · [[11_KNOWLEDGE/KNOWLEDGE_MOC|KNOWLEDGE_MOC]] · [[11_KNOWLEDGE/03_RSCF/03_RSCF_MOC|03_RSCF_MOC]] · [[11_KNOWLEDGE/AMOS_FULL_BRAIN_OS_ARCHITECTURE|AMOS_FULL_BRAIN_OS_ARCHITECTURE]] · [[25_COGNITIVE_MATRIX/25_COGNITIVE_MATRIX_MOC|25_COGNITIVE_MATRIX_MOC]]

______________________________________________________________________

**MOC:** [[11_KNOWLEDGE/03_RSCF/03_RSCF_MOC|03_RSCF_MOC]]
