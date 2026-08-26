---
tags: ['cognitive_matrix', 'l14_valuation']
---

# L14 VALUATION MAP

## Map — L14 VALUATION MAP
Navigation map for the `25_COGNITIVE_MATRIX/01_PRIMITIVES/L14_VALUATION/00_INDEX` segment of the Cognitive Matrix plane.

- **Readme** — [[INDEX_L14_VALUATION_PRIMITIVES_COGNITIVE_MATRIX_README]]
- **Contract** — [[PRIMITIVES_COGNITIVE_MATRIX_L14_VALUATION_CONTRACT]]

## Reading order
1. Readme → orientation.  2. Contract → normative terms.  3. Artifacts → instances bound by the contract.

## Gaps
This map covers its own directory only; cross-segment edges live in [[00_ROOT_MAP]] and [[AMOS_RSCF_NODES]]. Executable graph validation remains PARTIAL ([[ROUTING_POLICY_VALIDATION_RECEIPT]] · [[AUTHZ_ENGINE_VALIDATION_RECEIPT]]).
## Worked semantics
Given an operation touching `L14 VALUATION MAP` within the Cognitive Matrix plane:
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
---

[[00_ROOT/00_ROOT_MOC.md|AMOS MOC]]

---
RSCF-NODE
node_id: cognitive_matrix_atrix_01_primitives_l14_valuation_00_index_l14_valuation_map
node_type: note
path: 25_COGNITIVE_MATRIX/01_PRIMITIVES/L14_VALUATION/00_INDEX/L14_VALUATION_MAP.md
claim_class: AMOS_MODEL
