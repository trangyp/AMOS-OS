---
title: TSS-TPE RSCF Index
type: tss
source: 11_KNOWLEDGE/03_RSCF
artifact: TSS_TPE_RSCF_INDEX.md
artifact_id: amos_11_knowledge_03_rscf_tss_tpe_rscf_index
origin_architect: Trang Phan
steward: Trang Phan
system: AMOS OS
plane: 11_KNOWLEDGE
segment: 11_KNOWLEDGE/03_RSCF
artifact_kind: INDEX
path: 11_KNOWLEDGE/03_RSCF/TSS_TPE_RSCF_INDEX.md
tags:
- amos-os
- knowledge
- vault
- 11_knowledge
- 03_rscf
- tss_tpe_rscf_index
- proof_capsules
- tss_proofs
- tpe_proofs
- rscf
- canon_candidate
- canon/knowledge
- tss-the-trang-system
- tpe-trang-prediction-engine
- amos-x-tss-tpe-matrix
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
  - TSS_THE_TRANG_SYSTEM
  - TPE_TRANG_PREDICTION_ENGINE
  - AMOS_CORPUS
  scope:
  - KNOWLEDGE_RSCF
  - TSS_TPE_RSCF_INDEX
  - SOURCE_DEFINED_MODEL
framework_binding:
  rscf_moc:
    artifact:
    - - 03_RSCF_MOC
  tss_master:
    artifact:
    - - TSS_THE_TRANG_SYSTEM
  tpe_master:
    artifact:
    - - TPE_TRANG_PREDICTION_ENGINE
epistemic_boundary:
  source_presence: VERIFIED_SOURCE_PRESENCE
  index_structure: VERIFIED_SOURCE_STRUCTURE
  proof_index: SOURCE_DEFINED_MODEL
  runtime_enforcement: NOT_ESTABLISHED
---

# TSS-TPE RSCF Proof Capsule Index

`TSS_TPE_RSCF_INDEX.md` is the canonical Knowledge Plane proof index for **TSS (The Trang System) & TPE (Trang Prediction Engine) RSCF Capsules** within `11_KNOWLEDGE/03_RSCF`.

It catalogs verifiable proof capsules governing system lifecycle state variables ($\Omega, H, F, S$), the 7 evolutionary cycles ($C_1 \dots C_7$), alignment formulation ($i$), and structural foresight prediction.

---

# 1. Indexed RSCF Capsules

| Node ID | Framework Module | Claim Class | Governing Equation / Invariant | Status |
| :--- | :--- | :--- | :--- | :--- |
| `RSCF-TSS-001` | TSS Core Model | `AMOS_MODEL` | $i_{\text{TSS}} = [H(1-\Omega)(1-F)(1-S)]^{1/4}$ | Active |
| `RSCF-TSS-002` | TSS 7 Cycles | `AMOS_MODEL` | Phase Sequence $C_1 \to C_2 \to \dots \to C_7$ | Active |
| `RSCF-TSS-003` | TSS Quadratic Scaling | `MATHEMATICAL_MODEL` | Capability Emergence $e = i_{\text{TSS}}^2$ | Active |
| `RSCF-TSS-004` | TPE Prediction Engine | `AMOS_MODEL` | 7-Layer Structural Foresight Pipeline | Active |

---

# 2. Inter-Plane & Vault Connections

- **RSCF MOC:** [[03_RSCF_MOC]]
- **TSS Master:** [[TSS_THE_TRANG_SYSTEM]]
- **TPE Master:** [[TPE_TRANG_PREDICTION_ENGINE]]
- **Cognitive Matrix:** [[AMOS_X_TSS_TPE_MATRIX]]

---

# 3. RSCF Contract

```yaml
RSCF:
  node_id: amos_11_knowledge_03_rscf_tss_tpe_rscf_index
  node_type: index
  claim_class: AMOS_MODEL
  state: SOURCE_CLAIM
  H:
    identity: "TSS-TPE RSCF Index"
    role: "Index of RSCF proof capsules across TSS lifecycles and TPE prediction engines"
  M:
    indexed_nodes: [RSCF-TSS-001, RSCF-TSS-002, RSCF-TSS-003, RSCF-TSS-004]
  confidence_ceiling:
    source_model: SOURCE_BOUND
    runtime: UNKNOWN
```

---

**Related:** [[00_HOME]] · [[KNOWLEDGE_MOC]] · [[03_RSCF_MOC]] · [[TSS_THE_TRANG_SYSTEM]] · [[TPE_TRANG_PREDICTION_ENGINE]] · [[AMOS_X_TSS_TPE_MATRIX]]

---
**MOC:** [[03_RSCF_MOC]]

