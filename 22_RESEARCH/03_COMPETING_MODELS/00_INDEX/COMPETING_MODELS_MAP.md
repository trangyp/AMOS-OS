---
title: COMPETING MODELS MAP
type: map
source: 22_RESEARCH/03_COMPETING_MODELS/00_INDEX
tags:
- amos_os
- 22_research
- canon/research
rscf:
  state: DERIVED
  claim_class: DERIVED
  provenance: AMOS_corpus
  scope: index_navigation
---


# COMPETING MODELS MAP

## Map — COMPETING MODELS · MAP
Navigation map for the `22_RESEARCH/03_COMPETING_MODELS/00_INDEX` segment of the Research plane.

- **Contract** — [[COMPETING_MODELS_RESEARCH_COMPETING_MODELS_CONTRACT]]
- **Readme** — [[INDEX_COMPETING_MODELS_RESEARCH_README]]

## Reading order
1. Readme → orientation.  2. Contract → normative terms.  3. Artifacts → instances bound by the contract.

## Gaps
This map covers its own directory only; cross-segment edges live in [[00_ROOT_MAP]] and [[AMOS_RSCF_NODES]]. Executable graph validation remains PARTIAL ([[ROUTING_POLICY_VALIDATION_RECEIPT]] · [[AUTHZ_ENGINE_VALIDATION_RECEIPT]]).
## Worked semantics
Given an operation touching `COMPETING MODELS · MAP` within the Research plane:
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
node_id: amos_22_research_03_competing_models_00_index_competing_models_map_md
node_type: note
path: 22_RESEARCH/03_COMPETING_MODELS/00_INDEX/COMPETING_MODELS_MAP.md
claim_class: AMOS_MODEL

---
**MOC:** [[00_INDEX_MOC]]
