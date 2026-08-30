---
title: HML Router Specification
type: runtime
source: 04_RUNTIME/02_ROUTER
artifact: HML_ROUTER.md
artifact_id: amos_04_runtime_02_router_hml_router
origin_architect: Trang Phan
steward: Trang Phan
system: AMOS OS
plane: 04_RUNTIME
segment: 04_RUNTIME/02_ROUTER
artifact_kind: ROUTER_SPEC
path: 04_RUNTIME/02_ROUTER/HML_ROUTER.md
tags:
- amos-os
- runtime
- vault
- 02_router
- hml_router
- high_mid_low
- progressive_disclosure
- rscf
- canon_candidate
- canon/runtime
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
  - 04_RUNTIME/02_ROUTER/02_ROUTER_MOC
  - 11_KNOWLEDGE/11_KNOWLEDGE_MOC
  - AMOS_CORPUS
  scope:
  - RUNTIME_ROUTER
  - HML_ROUTING
  - SOURCE_DEFINED_MODEL
framework_binding:
  router_moc:
    artifact: 04_RUNTIME/02_ROUTER/02_ROUTER_MOC
  knowledge_moc:
    artifact: 11_KNOWLEDGE/KNOWLEDGE_MOC
epistemic_boundary:
  source_presence: VERIFIED_SOURCE_PRESENCE
  spec_structure: VERIFIED_SOURCE_STRUCTURE
  routing_algorithm: SOURCE_DEFINED_MODEL
  runtime_enforcement: NOT_ESTABLISHED
---

# HML (High / Mid / Low) Progressive Disclosure Router Specification

`HML_ROUTER.md` is the canonical Runtime Plane specification governing the progressive context disclosure across **High (H - Metadata/Index)**, **Mid (M - Structure/Executive)**, and **Low (L - Deep Raw Corpus)** layers within `04_RUNTIME/02_ROUTER`.

---

# 1. H/M/L Progressive Disclosure Strategy

```text
  User Request / System Inquiry
     │
  ├── Tier H (High Level): Scans lightweight metadata, MOCs, and headers (~10-50 tokens)
     │   (Resolves 80% of simple routing and existence checks)
     ▼
  ├── Tier M (Mid Level): Loads formal frameworks, equations, and executive structures (~200-800 tokens)
     │   (Resolves detailed reasoning, synthesis, and matrix bindings)
     ▼
  └── Tier L (Low Level): Selectively retrieves deep raw source corpus / arXiv proof lines
         (Invoked ONLY when mathematical line-by-line verification is required)
```

---

# 2. Inter-Plane & Vault Connections

- **Router MOC:** 04_RUNTIME/02_ROUTER/[[02_ROUTER_MOC]]
- **Knowledge MOC:** 11_KNOWLEDGE/[[KNOWLEDGE_MOC]]
- **Cognitive Matrix:** 25_COGNITIVE_MATRIX/[[25_COGNITIVE_MATRIX_MOC]]

---

# 3. RSCF Contract

```yaml
RSCF:
  node_id: amos_04_runtime_02_router_hml_router
  node_type: router_spec
  claim_class: AMOS_MODEL
  state: SOURCE_CLAIM
  H:
    identity: "HML Router Specification"
    role: "Progressive context disclosure router optimizing token budget across H/M/L tiers"
  M:
    tiers: [tier_h_high, tier_m_mid, tier_l_low]
  confidence_ceiling:
    source_model: SOURCE_BOUND
    runtime: UNKNOWN
```

---

**Related:** [[00_HOME]] · [[04_RUNTIME_MOC]] · 04_RUNTIME/02_ROUTER/[[02_ROUTER_MOC]] · 11_KNOWLEDGE/[[KNOWLEDGE_MOC]]

---
**MOC:** 04_RUNTIME/02_ROUTER/[[02_ROUTER_MOC]]
