---
canon-group: meta
canon-type: framework
rscf-state: source-claim
rscf-claim: verified
rscf-provenance: AMOS_corpus
conclusion_class: AMOS_MODEL
epistemic_class: SOURCE_CLAIM
topic: Hml Router
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

# HML (High / Mid / Low) Progressive Disclosure Router Specification

`HML_ROUTER.md` is the canonical Runtime Plane specification governing the progressive context disclosure across **High (H - Metadata/Index)**, **Mid (M - Structure/Executive)**, and **Low (L - Deep Raw Corpus)** layers within `04_RUNTIME/02_ROUTER`.

______________________________________________________________________

## 1. H/M/L Progressive Disclosure Strategy

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

______________________________________________________________________

## 2. Inter-Plane & Vault Connections

- **Router MOC:** 04_RUNTIME/02_ROUTER/[[04_RUNTIME/02_ROUTER/02_ROUTER_MOC|02_ROUTER_MOC]]
- **Knowledge MOC:** 11_KNOWLEDGE/[[11_KNOWLEDGE/KNOWLEDGE_MOC|KNOWLEDGE_MOC]]
- **Cognitive Matrix:** 25_COGNITIVE_MATRIX/[[25_COGNITIVE_MATRIX/25_COGNITIVE_MATRIX_MOC|25_COGNITIVE_MATRIX_MOC]]

______________________________________________________________________

## 3. RSCF Contract

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

______________________________________________________________________

**Related:** [[00_ROOT/00_HOME|00_HOME]] · [[04_RUNTIME/04_RUNTIME_MOC|04_RUNTIME_MOC]] · 04_RUNTIME/02_ROUTER/[[04_RUNTIME/02_ROUTER/02_ROUTER_MOC|02_ROUTER_MOC]] · 11_KNOWLEDGE/[[11_KNOWLEDGE/KNOWLEDGE_MOC|KNOWLEDGE_MOC]]

______________________________________________________________________

**MOC:** 04_RUNTIME/02_ROUTER/[[04_RUNTIME/02_ROUTER/02_ROUTER_MOC|02_ROUTER_MOC]]
