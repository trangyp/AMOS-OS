---
title: UBI Score Framework
type: biology
source: 11_KNOWLEDGE/05_FRAMEWORKS
artifact: UBI_SCORE_FRAMEWORK.md
artifact_id: amos_11_knowledge_05_frameworks_ubi_score_framework
origin_architect: Trang Phan
steward: Trang Phan
system: AMOS OS
plane: 11_KNOWLEDGE
segment: 11_KNOWLEDGE/05_FRAMEWORKS
artifact_kind: FRAMEWORK
path: 11_KNOWLEDGE/05_FRAMEWORKS/UBI_SCORE_FRAMEWORK.md
tags:
  - amos-os
  - knowledge
  - vault
  - 05_frameworks
  - ubi_score_framework
  - biological_scoring
  - alignment_metrics
  - e_equals_i_squared
  - diagnostic_metrics
  - rscf
  - canon_candidate
  - canon/knowledge
  - unified-biological-intelligence
  - amos-x-ubi-matrix
  - amos-x-ubi
  - ubi-homeostasis
  - ubi-neurobiological-intelligence
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
    - UNIFIED_BIOLOGICAL_INTELLIGENCE_UBI_OFFICIAL
    - AMOS_CORPUS
  scope:
    - KNOWLEDGE_FRAMEWORKS
    - BIOLOGICAL_METRICS
    - SOURCE_DEFINED_MODEL
framework_binding:
  master_framework:
    artifact:
      -   - UNIFIED_BIOLOGICAL_INTELLIGENCE
  matrix_binding:
    artifact:
      -   - AMOS_X_UBI_MATRIX
epistemic_boundary:
  source_presence: VERIFIED_SOURCE_PRESENCE
  framework_structure: VERIFIED_SOURCE_STRUCTURE
  scoring_model: SOURCE_DEFINED_MODEL
  clinical_diagnostic: NOT_ESTABLISHED
  runtime_enforcement: NOT_ESTABLISHED
---

# UBI Score Framework

`UBI_SCORE_FRAMEWORK.md` is the canonical Knowledge Plane reference artifact for the **UBI Score Framework & Measurement Protocols** within `11_KNOWLEDGE/05_FRAMEWORKS`.

It establishes quantifiable metrics and diagnostic protocols to measure alignment ($i$) and effectiveness ($e = i^2$) across the four living domains.

______________________________________________________________________

## 1. Measurement Dimensions & Scoring Protocol

| Domain  | Core Diagnostic Metric                           | Standard Scale                          | Normalized Variable     |
| ------- | ------------------------------------------------ | --------------------------------------- | ----------------------- |
| **NBI** | Cognitive flexibility & working memory bandwidth | Psychometric / reaction assay ($0–100$) | $\text{NBI} \in [0, 1]$ |
| **NEI** | Heart Rate Variability (HRV) & autonomic balance | Parasympathetic tone ratio ($0–100$)    | $\text{NEI} \in [0, 1]$ |
| **SI**  | Postural symmetry, breath depth & fascial tone   | Biomechanical posture score ($0–100$)   | $\text{SI} \in [0, 1]$  |
| **BEI** | Neural-cardiac oscillatory coherence             | EEG/ECG phase-locking index ($0–100$)   | $\text{BEI} \in [0, 1]$ |

$$\text{Composite Alignment } i = (\text{NBI} \cdot \text{NEI} \cdot \text{SI} \cdot \text{BEI})^{1/4}, \quad e = i^2$$

______________________________________________________________________

## 2. Inter-Plane & Vault Connections

- **Master Framework:** [[11_KNOWLEDGE/05_FRAMEWORKS/UNIFIED_BIOLOGICAL_INTELLIGENCE|UNIFIED_BIOLOGICAL_INTELLIGENCE]]
- **Cognitive Matrix:** [[25_COGNITIVE_MATRIX/AMOS_X_UBI|AMOS_X_UBI]] and [[25_COGNITIVE_MATRIX/AMOS_X_UBI_MATRIX|AMOS_X_UBI_MATRIX]]
- **Homeostasis Models:** [[05_COGNITIVE_ORGANISM/15_HOMEOSTASIS/UBI_HOMEOSTASIS|UBI_HOMEOSTASIS]]
- **Domain Breakdown:** [[11_KNOWLEDGE/06_DOMAIN_KNOWLEDGE/UBI_NEUROBIOLOGICAL_INTELLIGENCE|UBI_NEUROBIOLOGICAL_INTELLIGENCE]]

______________________________________________________________________

## 3. RSCF Contract

```yaml
RSCF:
  node_id: amos_11_knowledge_05_frameworks_ubi_score_framework
  node_type: framework
  claim_class: AMOS_MODEL
  state: SOURCE_CLAIM
  H:
    identity: "UBI Score Framework"
    role: "Quantifiable measurement protocols and composite alignment scoring across UBI domains"
  M:
    metrics: [NBI_score, NEI_score, SI_score, BEI_score, composite_alignment, effectiveness_score]
  confidence_ceiling:
    source_model: SOURCE_BOUND
    runtime: UNKNOWN
```

______________________________________________________________________

**Related:** [[00_ROOT/00_HOME|00_HOME]] · [[11_KNOWLEDGE/KNOWLEDGE_MOC|KNOWLEDGE_MOC]] · [[11_KNOWLEDGE/05_FRAMEWORKS/05_FRAMEWORKS_MOC|05_FRAMEWORKS_MOC]] · [[11_KNOWLEDGE/05_FRAMEWORKS/UNIFIED_BIOLOGICAL_INTELLIGENCE|UNIFIED_BIOLOGICAL_INTELLIGENCE]] · [[25_COGNITIVE_MATRIX/AMOS_X_UBI_MATRIX|AMOS_X_UBI_MATRIX]] · [[05_COGNITIVE_ORGANISM/15_HOMEOSTASIS/UBI_HOMEOSTASIS|UBI_HOMEOSTASIS]]

______________________________________________________________________

**MOC:** [[11_KNOWLEDGE/05_FRAMEWORKS/05_FRAMEWORKS_MOC|05_FRAMEWORKS_MOC]]
