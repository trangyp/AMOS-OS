---
canon-group: meta
canon-type: framework
rscf-state: source-claim
rscf-claim: verified
rscf-provenance: AMOS_corpus
conclusion_class: AMOS_MODEL
epistemic_class: SOURCE_CLAIM
topic: Ubi Score
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

# UBI Score — Non-Compensatory Alignment Metric

`UBI_SCORE.md` is the canonical Knowledge Plane reference artifact for the **UBI Score Metric** within `11_KNOWLEDGE/05_FRAMEWORKS`.

It defines the exact mathematical computation of the multi-domain geometric mean score:

$$\text{UBI Score } (i) = (\text{NBI} \cdot \text{NEI} \cdot \text{SI} \cdot \text{BEI})^{1/4} \in [0, 1]$$

Where the emergence factor is calculated as $e = i^2$.

______________________________________________________________________

## 1. Measurement Invariants

1. **Strict Geometric Multiplicity:** If any single domain drops to zero, the total UBI Score collapses to zero ($\min = 0 \implies i = 0$).
1. **Bottleneck Identification:** System diagnosis targets $\arg\min_{d \in \{\text{NBI}, \text{NEI}, \text{SI}, \text{BEI}\}} d$ to prevent futile over-optimization of strong domains.
1. **Quadratic Scaling ($e = i^2$):** Systemic creative throughput and stress resilience grow non-linearly with balanced alignment.

______________________________________________________________________

## 2. Inter-Plane & Vault Connections

- **Parent Scoring Framework:** [[11_KNOWLEDGE/05_FRAMEWORKS/UBI_SCORE_FRAMEWORK|UBI_SCORE_FRAMEWORK]]
- **Biological Master:** [[11_KNOWLEDGE/05_FRAMEWORKS/UNIFIED_BIOLOGICAL_INTELLIGENCE|UNIFIED_BIOLOGICAL_INTELLIGENCE]]
- **Super Engine:** [[11_KNOWLEDGE/05_FRAMEWORKS/AMOS_UBI_SUPER_ENGINE|AMOS_UBI_SUPER_ENGINE]]
- **Cognitive Matrix:** [[25_COGNITIVE_MATRIX/AMOS_X_UBI|AMOS_X_UBI]]

______________________________________________________________________

## 3. RSCF Contract

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

______________________________________________________________________

**Related:** [[00_ROOT/00_HOME|00_HOME]] · [[11_KNOWLEDGE/KNOWLEDGE_MOC|KNOWLEDGE_MOC]] · [[11_KNOWLEDGE/05_FRAMEWORKS/05_FRAMEWORKS_MOC|05_FRAMEWORKS_MOC]] · [[11_KNOWLEDGE/05_FRAMEWORKS/UBI_SCORE_FRAMEWORK|UBI_SCORE_FRAMEWORK]] · [[11_KNOWLEDGE/05_FRAMEWORKS/UNIFIED_BIOLOGICAL_INTELLIGENCE|UNIFIED_BIOLOGICAL_INTELLIGENCE]] · [[11_KNOWLEDGE/05_FRAMEWORKS/AMOS_UBI_SUPER_ENGINE|AMOS_UBI_SUPER_ENGINE]]

______________________________________________________________________

**MOC:** [[11_KNOWLEDGE/05_FRAMEWORKS/05_FRAMEWORKS_MOC|05_FRAMEWORKS_MOC]]
