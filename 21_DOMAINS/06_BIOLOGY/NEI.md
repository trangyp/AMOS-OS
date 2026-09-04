---
title: Neuroemotional Intelligence (NEI) Domain Engine
type: domain
source: 21_DOMAINS/06_BIOLOGY
artifact: NEI.md
artifact_id: amos_21_domains_06_biology_nei
origin_architect: Trang Phan
steward: Trang Phan
system: AMOS OS
plane: 21_DOMAINS
segment: 21_DOMAINS/06_BIOLOGY
artifact_kind: DOMAIN_ENGINE
path: 21_DOMAINS/06_BIOLOGY/NEI.md
tags:
  - amos-os
  - domain
  - vault
  - 06_biology
  - nei
  - neuroemotional_intelligence
  - vagal_tone_regulation
  - rscf
  - canon_candidate
  - canon/domain
  - phuong-phap-trang
  - ubi-neuroemotional-intelligence
  - unified-biological-intelligence
  - ubi-x-emotion
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
    - 11_KNOWLEDGE/06_DOMAIN_KNOWLEDGE/UBI_NEUROEMOTIONAL_INTELLIGENCE
    - 11_KNOWLEDGE/05_FRAMEWORKS/UNIFIED_BIOLOGICAL_INTELLIGENCE
    - AMOS_CORPUS
  scope:
    - DOMAIN_BIOLOGY
    - NEI_ENGINE
    - SOURCE_DEFINED_MODEL
framework_binding:
  domain_knowledge:
    artifact: 11_KNOWLEDGE/06_DOMAIN_KNOWLEDGE/UBI_NEUROEMOTIONAL_INTELLIGENCE
  biological_master:
    artifact: 11_KNOWLEDGE/05_FRAMEWORKS/UNIFIED_BIOLOGICAL_INTELLIGENCE
  matrix_binding:
    artifact: 25_COGNITIVE_MATRIX/UBI_X_EMOTION
epistemic_boundary:
  source_presence: VERIFIED_SOURCE_PRESENCE
  domain_structure: VERIFIED_SOURCE_STRUCTURE
  telemetry_engine: SOURCE_DEFINED_MODEL
  runtime_enforcement: NOT_ESTABLISHED
---

# Neuroemotional Intelligence (NEI) Domain Engine

`NEI.md` is the canonical Domain Plane specification governing real-time autonomic vagal tone tracking, stress regulation, and emotional loop closure within `21_DOMAINS/06_BIOLOGY`.

______________________________________________________________________

## 1. NEI Operational Mechanics

1. **Autonomic Telemetry Sampling:** Continuous ingestion of heart-rate variability (HRV RMSSD) and galvanic skin conductance (EDA).
1. **Affective Loop Closure:** Detects escalating autonomic dissonance and injects [[11_KNOWLEDGE/05_FRAMEWORKS/PHUONG_PHAP_TRANG|PHUONG_PHAP_TRANG]] precise semantic labeling to de-escalate anxiety.
1. **Non-Compensatory Vector:** Emits scalar $\text{NEI} \in [0, 1]$ into the UBI master composite equation.

______________________________________________________________________

## 2. Inter-Plane & Vault Connections

- **Knowledge Domain:** 11_KNOWLEDGE/06_DOMAIN_KNOWLEDGE/[[11_KNOWLEDGE/06_DOMAIN_KNOWLEDGE/UBI_NEUROEMOTIONAL_INTELLIGENCE|UBI_NEUROEMOTIONAL_INTELLIGENCE]]
- **Biological Master:** 11_KNOWLEDGE/05_FRAMEWORKS/[[11_KNOWLEDGE/05_FRAMEWORKS/UNIFIED_BIOLOGICAL_INTELLIGENCE|UNIFIED_BIOLOGICAL_INTELLIGENCE]]
- **Cognitive Matrix:** 25_COGNITIVE_MATRIX/[[25_COGNITIVE_MATRIX/UBI_X_EMOTION|UBI_X_EMOTION]]

______________________________________________________________________

## 3. RSCF Contract

```yaml
RSCF:
  node_id: amos_21_domains_06_biology_nei
  node_type: domain_engine
  claim_class: AMOS_MODEL
  state: SOURCE_CLAIM
  H:
    identity: "NEI Domain Engine"
    role: "Autonomic vagal tone tracking and stress regulation engine for Neuroemotional Intelligence"
  M:
    primitives: [autonomic_telemetry_sampling, affective_loop_closure, non_compensatory_vector]
  confidence_ceiling:
    source_model: SOURCE_BOUND
    runtime: UNKNOWN
```

______________________________________________________________________

**Related:** [[00_ROOT/00_HOME|00_HOME]] · [[21_DOMAINS/21_DOMAINS_MOC|21_DOMAINS_MOC]] · 11_KNOWLEDGE/06_DOMAIN_KNOWLEDGE/[[11_KNOWLEDGE/06_DOMAIN_KNOWLEDGE/UBI_NEUROEMOTIONAL_INTELLIGENCE|UBI_NEUROEMOTIONAL_INTELLIGENCE]] · 11_KNOWLEDGE/05_FRAMEWORKS/[[11_KNOWLEDGE/05_FRAMEWORKS/UNIFIED_BIOLOGICAL_INTELLIGENCE|UNIFIED_BIOLOGICAL_INTELLIGENCE]]

______________________________________________________________________

**MOC:** [[21_DOMAINS/21_DOMAINS_MOC|21_DOMAINS_MOC]]
