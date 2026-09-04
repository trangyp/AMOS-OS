---
origin_architect: Trang Phan
steward: Trang Phan
amos_core_target: v4.4
title: amos agent registry
tags:
  - stub
  - amos
  - agent
  - registry
type: note
source: 11_KNOWLEDGE/stubs
rscf:
  state: DERIVED
  claim_class: DERIVED
  provenance: AMOS_corpus
  scope: AMOS_general
---

# amos agent registry

## Purpose
Registry for **amos agent registry** within the Knowledge plane (knowledge base integration (excluded from this pass) context).

## Entry schema
```yaml
entry_id: null          # unique within registry
version: null           # explicit; material change ⇒ new version
artifact_type: null     # typed
epistemic_class: MODEL  # SOURCE | DERIVED | MODEL | UNKNOWN/GAP
scope: null             # domain / regime / H-M-L applicability
provenance: []          # source lineage, transformations
authority_ref: null     # granting authority, epoch-bound
freshness: null         # valid_until / max_age
status: REGISTERED      # REGISTERED | SUPERSEDED | REVOKED | QUARANTINED
```

## Current contents
Registry population is EMPTY-BY-HONESTY: no fabricated entries. Entries are added only with provenance and authority refs.

## Registry laws
- ADDRESSABLE ≠ IMPLEMENTED ≠ VALIDATED ≠ AUTHORIZED.
- Same id + changed semantics ⇒ version bump, never silent overwrite.
- Revocation preserves history (append-only).

## Gaps
Registry backend, uniqueness enforcement, and automated schema validation remain OPEN ([[ROUTING_POLICY_VALIDATION_RECEIPT]] · [[AUTHZ_ENGINE_VALIDATION_RECEIPT]]).
## Worked semantics
Given an operation touching `amos agent registry` within the Knowledge plane:
1. **Admit** — resolve the artifact by id + version; unresolved id ⇒ `UNKNOWN/GAP`, fail closed.
2. **Bind scope** — declare domain / regime / H-M-L applicability before any mutation.
3. **Check authority** — authority_ref must be epoch-valid; capability alone never authorizes.
4. **Validate preconditions** — dependency closure traversed to the smallest result-changing set.
5. **Propose** — candidate state is non-authoritative until gates pass (`PROPOSAL ≠ COMMIT`).
6. **Commit or hold** — on any failed premise: preserve unaffected state, invalidate dependent descendants only, record receipt.

## Promotion-gate checklist
- [ ] typed schema bound to this artifact
- [ ] identity + versioning implemented
- [ ] negative cases covered (missing · malformed · stale · unauthorized input)
- [ ] provenance edges persisted and validated
- [ ] rollback basin demonstrated for consequential effects
- [ ] executed validation receipt specific to this artifact
- [ ] unresolved critical gaps registered as UNKNOWN/GAP (visible)

## Cross-plane bindings
- Governed by canon — [[01_CANON_README]] · [[LAW_HIERARCHY]]
- Kernel interaction — [[KERNEL_README]]
- Control-plane gates — [[CONTROL_PLANE_README]]
- Observed by — [[17_OBSERVABILITY_README]] · never treated as authority
- Recovered via operations — [[20_OPERATIONS_README]]
