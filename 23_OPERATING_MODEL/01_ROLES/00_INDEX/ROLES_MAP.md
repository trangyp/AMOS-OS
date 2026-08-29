---
title: ROLES MAP
type: map
source: 23_OPERATING_MODEL/01_ROLES/00_INDEX
tags:
- amos-os
- 23_operating_model
- canon/operating-model
- index-roles-operating-model-readme
- roles-operating-model-roles-contract
- 00-root-map
- amos-rscf-nodes
- routing-policy-validation-receipt
- authz-engine-validation-receipt
- law-hierarchy
- kernel-readme
- control-plane-readme
- observability-readme
- operations-readme
- 00-root-moc
- amos-moc
- 00-home
- 00-index-moc
rscf:
  state: DERIVED
  claim_class: DERIVED
  provenance: AMOS_corpus
  scope: index_navigation
---

# ROLES MAP

## Map — ROLES · MAP
Navigation map for the `23_OPERATING_MODEL/01_ROLES/00_INDEX` segment of the Operating Model plane.

- **Readme** — [[INDEX_ROLES_OPERATING_MODEL_README]]
- **Contract** — [[ROLES_OPERATING_MODEL_ROLES_CONTRACT]]

## Reading order
1. Readme → orientation.  2. Contract → normative terms.  3. Artifacts → instances bound by the contract.

## Gaps
This map covers its own directory only; cross-segment edges live in [[00_ROOT_MAP]] and [[AMOS_RSCF_NODES]]. Executable graph validation remains PARTIAL ([[ROUTING_POLICY_VALIDATION_RECEIPT]] · [[AUTHZ_ENGINE_VALIDATION_RECEIPT]]).
## Worked semantics
Given an operation touching `ROLES · MAP` within the Operating Model plane:
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
- Governed by canon — [[LAW_HIERARCHY]]|AMOS Core Laws · [[LAW_HIERARCHY]]
- Kernel interaction — [[KERNEL_README]]
- Control-plane gates — [[CONTROL_PLANE_README]]
- Observed by — [[OBSERVABILITY_README]] · never treated as authority
- Recovered via operations — [[OPERATIONS_README]]
---

[[00_ROOT_MOC]]|[[AMOS MOC]]

---
**Related:** [[00_HOME]] · [[AMOS_RSCF_NODES]]

---
RSCF-NODE
node_id: amos_23_operating_model_01_roles_00_index_roles_map_md
node_type: note
path: 23_OPERATING_MODEL/01_ROLES/00_INDEX/ROLES_MAP.md
claim_class: AMOS_MODEL

---
**MOC:** [[00_INDEX_MOC]]
