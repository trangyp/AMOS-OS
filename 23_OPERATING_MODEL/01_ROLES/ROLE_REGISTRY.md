---
origin_architect: Trang Phan
steward: Trang Phan
amos_core_target: v4.4
title: ROLE REGISTRY
type: registry
source: 23_OPERATING_MODEL/01_ROLES
tags:
  - amos-os
  - canon/operating-model
  - routing-policy-validation-receipt
  - authz-engine-validation-receipt
  - law-hierarchy
rscf:
  state: DERIVED
  claim_class: DERIVED
  provenance: AMOS_corpus
  scope: AMOS_general
---

# ROLE REGISTRY

## Purpose

Registry for **ROLE REGISTRY** within the Operating Model plane (roles, decision rights, governance forums, escalation paths, service levels context).

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

Registry backend, uniqueness enforcement, and automated schema validation remain OPEN ([[25_COGNITIVE_MATRIX/11_VALIDATION/ROUTING_POLICY_VALIDATION_RECEIPT|ROUTING_POLICY_VALIDATION_RECEIPT]] · [[03_CONTROL_PLANE/04_AUTHORITY/AUTHZ_ENGINE_VALIDATION_RECEIPT|AUTHZ_ENGINE_VALIDATION_RECEIPT]]).

## Worked semantics

Given an operation touching `ROLE REGISTRY` within the Operating Model plane:

1. **Admit** — resolve the artifact by id + version; unresolved id ⇒ `UNKNOWN/GAP`, fail closed.
1. **Bind scope** — declare domain / regime / H-M-L applicability before any mutation.
1. **Check authority** — authority_ref must be epoch-valid; capability alone never authorizes.
1. **Validate preconditions** — dependency closure traversed to the smallest result-changing set.
1. **Propose** — candidate state is non-authoritative until gates pass (`PROPOSAL ≠ COMMIT`).
1. **Commit or hold** — on any failed premise: preserve unaffected state, invalidate dependent descendants only, record receipt.

## Promotion-gate checklist

- [ ] typed schema bound to this artifact
- [ ] identity + versioning implemented
- [ ] negative cases covered (missing · malformed · stale · unauthorized input)
- [ ] provenance edges persisted and validated
- [ ] rollback basin demonstrated for consequential effects
- [ ] executed validation receipt specific to this artifact
- [ ] unresolved critical gaps registered as UNKNOWN/GAP (visible)

## Cross-plane bindings

- Governed by canon — [[01_CANON/01_CORE_LAWS/LAW_HIERARCHY|LAW_HIERARCHY]]|AMOS Core Laws · [[01_CANON/01_CORE_LAWS/LAW_HIERARCHY|LAW_HIERARCHY]]
- Kernel interaction — [[02_KERNEL/KERNEL_README|KERNEL_README]]
- Control-plane gates — [[03_CONTROL_PLANE/CONTROL_PLANE_README|CONTROL_PLANE_README]]
- Observed by — [[17_OBSERVABILITY/OBSERVABILITY_README|OBSERVABILITY_README]] · never treated as authority
- Recovered via operations — [[20_OPERATIONS/OPERATIONS_README|OPERATIONS_README]]

______________________________________________________________________

[[00_ROOT/00_ROOT_MOC|00_ROOT_MOC]]|[[00_ROOT/AMOS MOC|AMOS MOC]]

______________________________________________________________________

**Related:** [[00_ROOT/00_HOME|00_HOME]] · [[00_ROOT/AMOS_RSCF_NODES|AMOS_RSCF_NODES]]

______________________________________________________________________

RSCF-NODE
node_id: amos_23_operating_model_01_roles_role_registry_md
node_type: note
path: 23_OPERATING_MODEL/01_ROLES/ROLE_REGISTRY.md
claim_class: AMOS_MODEL

______________________________________________________________________

**MOC:** [[23_OPERATING_MODEL/01_ROLES/01_ROLES_MOC|01_ROLES_MOC]]
