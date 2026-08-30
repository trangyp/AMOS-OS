---
title: UBI Score
type: biology
source: 11_KNOWLEDGE/05_FRAMEWORKS
artifact: UBI_SCORE.md
artifact_id: amos_11_knowledge_05_frameworks_ubi_score
origin_architect: Trang Phan
steward: Trang Phan
system: AMOS OS
plane: 11_KNOWLEDGE
segment: 11_KNOWLEDGE/05_FRAMEWORKS
artifact_kind: METRIC
path: 11_KNOWLEDGE/05_FRAMEWORKS/UBI_SCORE.md
tags:
- amos-os
- knowledge
- vault
- 05_frameworks
- ubi_score
- biological_scoring
- alignment_metric
- non_compensatory_score
- rscf
- canon_candidate
- canon/knowledge
- ubi-score-framework
- unified-biological-intelligence
- amos-ubi-super-engine
- amos-x-ubi
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
  - UBI_SCORE_FRAMEWORK
  - UBI_OFFICIAL_MANUAL
  - AMOS_CORPUS
  scope:
  - KNOWLEDGE_FRAMEWORKS
  - BIOLOGICAL_METRICS
  - SOURCE_DEFINED_MODEL
framework_binding:
  score_framework:
    artifact:
    - - UBI_SCORE_FRAMEWORK
  biological_master:
    artifact:
    - - UNIFIED_BIOLOGICAL_INTELLIGENCE
epistemic_boundary:
  source_presence: VERIFIED_SOURCE_PRESENCE
  framework_structure: VERIFIED_SOURCE_STRUCTURE
  score_model: SOURCE_DEFINED_MODEL
  runtime_enforcement: NOT_ESTABLISHED
---

# UBI Score — Non-Compensatory Alignment Metric

`UBI_SCORE.md` is the canonical Knowledge Plane reference artifact for the **UBI Score Metric** within `11_KNOWLEDGE/05_FRAMEWORKS`.

It defines the exact mathematical computation of the multi-domain geometric mean score:

$$\text{UBI Score } (i) = (\text{NBI} \cdot \text{NEI} \cdot \text{SI} \cdot \text{BEI})^{1/4} \in [0, 1]$$

Where the emergence factor is calculated as $e = i^2$.

---

# 1. Measurement Invariants

1. **Strict Geometric Multiplicity:** If any single domain drops to zero, the total UBI Score collapses to zero ($\min = 0 \implies i = 0$).
2. **Bottleneck Identification:** System diagnosis targets $\arg\min_{d \in \{\text{NBI}, \text{NEI}, \text{SI}, \text{BEI}\}} d$ to prevent futile over-optimization of strong domains.
3. **Quadratic Scaling ($e = i^2$):** Systemic creative throughput and stress resilience grow non-linearly with balanced alignment.

---

# 2. Inter-Plane & Vault Connections

- **Parent Scoring Framework:** [[11_KNOWLEDGE/05_FRAMEWORKS/UBI_SCORE_FRAMEWORK|UBI_SCORE_FRAMEWORK]]
- **Biological Master:** [[11_KNOWLEDGE/05_FRAMEWORKS/UNIFIED_BIOLOGICAL_INTELLIGENCE|UNIFIED_BIOLOGICAL_INTELLIGENCE]]
- **Super Engine:** [[11_KNOWLEDGE/05_FRAMEWORKS/AMOS_UBI_SUPER_ENGINE|AMOS_UBI_SUPER_ENGINE]]
- **Cognitive Matrix:** [[25_COGNITIVE_MATRIX/AMOS_X_UBI|AMOS_X_UBI]]

---

# 3. RSCF Contract

```yaml
RSCF:
  node_id: amos_11_knowledge_05_frameworks_ubi_score
  node_type: metric
  claim_class: AMOS_MODEL
  state: SOURCE_CLAIM
  H:
    identity: "UBI Score Metric"
    role: "Exact geometric mean computation and bottleneck identification for biological alignment"
  M:
    formula: "i = (NBI * NEI * SI * BEI)^(1/4), e = i^2"
    invariants: [geometric_multiplicity, bottleneck_identification, quadratic_scaling]
  confidence_ceiling:
    source_model: SOURCE_BOUND
    runtime: UNKNOWN
```

---

**Related:** [[00_ROOT/00_HOME|00_HOME]] · [[11_KNOWLEDGE/KNOWLEDGE_MOC|KNOWLEDGE_MOC]] · [[11_KNOWLEDGE/05_FRAMEWORKS/05_FRAMEWORKS_MOC|05_FRAMEWORKS_MOC]] · [[11_KNOWLEDGE/05_FRAMEWORKS/UBI_SCORE_FRAMEWORK|UBI_SCORE_FRAMEWORK]] · [[11_KNOWLEDGE/05_FRAMEWORKS/UNIFIED_BIOLOGICAL_INTELLIGENCE|UNIFIED_BIOLOGICAL_INTELLIGENCE]] · [[11_KNOWLEDGE/05_FRAMEWORKS/AMOS_UBI_SUPER_ENGINE|AMOS_UBI_SUPER_ENGINE]]

---
**MOC:** [[11_KNOWLEDGE/05_FRAMEWORKS/05_FRAMEWORKS_MOC|05_FRAMEWORKS_MOC]]

