---
title: Neurobiological Intelligence (NBI) Domain Engine
type: domain
source: 21_DOMAINS/06_BIOLOGY
artifact: NBI.md
artifact_id: amos_21_domains_06_biology_nbi
origin_architect: Trang Phan
steward: Trang Phan
system: AMOS OS
plane: 21_DOMAINS
segment: 21_DOMAINS/06_BIOLOGY
artifact_kind: DOMAIN_ENGINE
path: 21_DOMAINS/06_BIOLOGY/NBI.md
tags:
- amos-os
- domain
- vault
- 21_domains
- 06_biology
- nbi
- neurobiological_intelligence
- cognitive_load_limits
- rscf
- canon_candidate
- canon/domain
- ubi-neurobiological-intelligence
- unified-biological-intelligence
- ubi-x-full-brain
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
  - 11_KNOWLEDGE/06_DOMAIN_KNOWLEDGE/UBI_NEUROBIOLOGICAL_INTELLIGENCE
  - 11_KNOWLEDGE/05_FRAMEWORKS/UNIFIED_BIOLOGICAL_INTELLIGENCE
  - AMOS_CORPUS
  scope:
  - DOMAIN_BIOLOGY
  - NBI_ENGINE
  - SOURCE_DEFINED_MODEL
framework_binding:
  domain_knowledge:
    artifact: 11_KNOWLEDGE/06_DOMAIN_KNOWLEDGE/UBI_NEUROBIOLOGICAL_INTELLIGENCE
  biological_master:
    artifact: 11_KNOWLEDGE/05_FRAMEWORKS/UNIFIED_BIOLOGICAL_INTELLIGENCE
  matrix_binding:
    artifact: 25_COGNITIVE_MATRIX/UBI_X_FULL_BRAIN
epistemic_boundary:
  source_presence: VERIFIED_SOURCE_PRESENCE
  domain_structure: VERIFIED_SOURCE_STRUCTURE
  telemetry_engine: SOURCE_DEFINED_MODEL
  runtime_enforcement: NOT_ESTABLISHED
---

# Neurobiological Intelligence (NBI) Domain Engine

`NBI.md` is the canonical Domain Plane specification governing the real-time telemetry ingestion, working memory load estimation, and neural frequency phase-locking of the **Neurobiological Intelligence (NBI)** subsystem within `21_DOMAINS/06_BIOLOGY`.

---

# 1. NBI Operational Mechanics

1. **Cortical Load Governance:** Monitors token ingestion rate and neural fatigue indices to prevent working memory saturation.
2. **Phase Synchronization:** Measures continuous theta/gamma oscillations to align inference pacing.
3. **Non-Compensatory Vector:** Emits normalized scalar $\text{NBI} \in [0, 1]$ into the UBI composite alignment formula $i_{\text{UBI}} = (\text{NBI} \cdot \text{NEI} \cdot \text{SI} \cdot \text{BEI})^{1/4}$.

---

# 2. Inter-Plane & Vault Connections

- **Knowledge Domain:** 11_KNOWLEDGE/06_DOMAIN_KNOWLEDGE/[[UBI_NEUROBIOLOGICAL_INTELLIGENCE]]
- **Biological Master:** 11_KNOWLEDGE/05_FRAMEWORKS/[[UNIFIED_BIOLOGICAL_INTELLIGENCE]]
- **Cognitive Matrix:** 25_COGNITIVE_MATRIX/[[UBI_X_FULL_BRAIN]]

---

# 3. RSCF Contract

```yaml
RSCF:
  node_id: amos_21_domains_06_biology_nbi
  node_type: domain_engine
  claim_class: AMOS_MODEL
  state: SOURCE_CLAIM
  H:
    identity: "NBI Domain Engine"
    role: "Real-time telemetry and cognitive load governance engine for Neurobiological Intelligence"
  M:
    primitives: [cortical_load_governance, phase_synchronization, non_compensatory_vector]
  confidence_ceiling:
    source_model: SOURCE_BOUND
    runtime: UNKNOWN
```

---

**Related:** [[00_HOME]] · [[21_DOMAINS_MOC]] · 11_KNOWLEDGE/06_DOMAIN_KNOWLEDGE/[[UBI_NEUROBIOLOGICAL_INTELLIGENCE]] · 11_KNOWLEDGE/05_FRAMEWORKS/[[UNIFIED_BIOLOGICAL_INTELLIGENCE]]

---
**MOC:** [[21_DOMAINS_MOC]]
