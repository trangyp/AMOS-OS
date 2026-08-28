---
title: RSCF Router Specification
type: runtime
source: 04_RUNTIME/02_ROUTER
artifact: RSCF_ROUTER.md
artifact_id: amos_04_runtime_02_router_rscf_router
origin_architect: Trang Phan
steward: Trang Phan
system: AMOS OS
plane: 04_RUNTIME
segment: 04_RUNTIME/02_ROUTER
artifact_kind: ROUTER_SPEC
path: 04_RUNTIME/02_ROUTER/RSCF_ROUTER.md
tags:
- amos_os
- runtime
- vault
- 04_runtime
- 02_router
- rscf_router
- proof_capsule_routing
- confidence_ceiling
- rscf
- canon_candidate
- canon/runtime
- 02-router-moc
- 03-rscf-moc
- ulk-x-rscf
- 00-home
- 04-runtime-moc
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
  - 11_KNOWLEDGE/03_RSCF/03_RSCF_MOC
  - 04_RUNTIME/02_ROUTER/02_ROUTER_MOC
  - AMOS_CORPUS
  scope:
  - RUNTIME_ROUTER
  - RSCF_ROUTING
  - SOURCE_DEFINED_MODEL
framework_binding:
  router_moc:
    artifact: 04_RUNTIME/02_ROUTER/02_ROUTER_MOC
  rscf_moc:
    artifact: 11_KNOWLEDGE/03_RSCF/03_RSCF_MOC
  matrix_binding:
    artifact: 25_COGNITIVE_MATRIX/ULK_X_RSCF
epistemic_boundary:
  source_presence: VERIFIED_SOURCE_PRESENCE
  spec_structure: VERIFIED_SOURCE_STRUCTURE
  routing_algorithm: SOURCE_DEFINED_MODEL
  runtime_enforcement: NOT_ESTABLISHED
---

# RSCF Proof Capsule Router Specification

`RSCF_ROUTER.md` is the canonical Runtime Plane specification governing the dynamic lookup, resolution, and verification dispatch of **RSCF Proof Capsules** within `04_RUNTIME/02_ROUTER`.

---

# 1. RSCF Proof Routing Pipeline

```text
  Incoming Claim Proposition (P)
     │
  1. Epistemic Class Classification (AMOS_MODEL / OBSERVATION / INVARIANT)
     │
  2. Proof Graph Lookup (11_KNOWLEDGE/03_RSCF)
     │
  3. Source Independence Audit (HERITAGE_PROVENANCE)
     │
  4. Confidence Ceiling Resolution ($C_{\text{max}} = f(\text{Ancestry}, \text{Grounding})$)
     │
  5. Verified Proof Capsule Dispatch / Rejection
```

---

# 2. Inter-Plane & Vault Connections

- **Router MOC:** 04_RUNTIME/02_ROUTER/[[02_ROUTER_MOC]]
- **RSCF Proof MOC:** 11_KNOWLEDGE/03_RSCF/[[03_RSCF_MOC]]
- **Cognitive Matrix:** 25_COGNITIVE_MATRIX/[[ULK_X_RSCF]]

---

# 3. RSCF Contract

```yaml
RSCF:
  node_id: amos_04_runtime_02_router_rscf_router
  node_type: router_spec
  claim_class: AMOS_MODEL
  state: SOURCE_CLAIM
  H:
    identity: "RSCF Router Specification"
    role: "Dynamic lookup and confidence resolution router for RSCF proof capsules"
  M:
    routing_pipeline: [claim_classification, proof_graph_lookup, source_independence_audit, confidence_resolution, dispatch_action]
  confidence_ceiling:
    source_model: SOURCE_BOUND
    runtime: UNKNOWN
```

---

**Related:** [[00_HOME]] · [[04_RUNTIME_MOC]] · 04_RUNTIME/02_ROUTER/[[02_ROUTER_MOC]] · 11_KNOWLEDGE/03_RSCF/[[03_RSCF_MOC]]

---
**MOC:** 04_RUNTIME/02_ROUTER/[[02_ROUTER_MOC]]
