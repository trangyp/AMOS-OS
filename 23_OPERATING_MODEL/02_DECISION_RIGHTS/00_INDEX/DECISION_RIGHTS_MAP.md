---
title: DECISION RIGHTS MAP
type: map
source: 23_OPERATING_MODEL/02_DECISION_RIGHTS/00_INDEX
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
  scope: index_navigation
---

# DECISION RIGHTS MAP

## Map — DECISION RIGHTS · MAP
Navigation map for the `23_OPERATING_MODEL/02_DECISION_RIGHTS/00_INDEX` segment of the Operating Model plane.

- **Contract** — [[DECISION_RIGHTS_OPERATING_MODEL_DECISION_RIGHTS_CONTRACT]]
- **Readme** — [[INDEX_DECISION_RIGHTS_OPERATING_MODEL_README]]

## Reading order
1. Readme → orientation.  2. Contract → normative terms.  3. Artifacts → instances bound by the contract.

## Gaps
This map covers its own directory only; cross-segment edges live in [[00_ROOT_MAP]] and [[AMOS_RSCF_NODES]]. Executable graph validation remains PARTIAL ([[ROUTING_POLICY_VALIDATION_RECEIPT]] · [[AUTHZ_ENGINE_VALIDATION_RECEIPT]]).
## Worked semantics
Given an operation touching `DECISION RIGHTS · MAP` within the Operating Model plane:
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
node_id: amos_23_operating_model_02_decision_rights_00_index_decision_rights_map_md
node_type: note
path: 23_OPERATING_MODEL/02_DECISION_RIGHTS/00_INDEX/DECISION_RIGHTS_MAP.md
claim_class: AMOS_MODEL

---
**MOC:** [[00_INDEX_MOC]]
