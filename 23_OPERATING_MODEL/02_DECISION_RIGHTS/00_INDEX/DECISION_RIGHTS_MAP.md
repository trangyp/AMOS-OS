---
canon-group: meta
canon-type: framework
rscf-state: source-claim
rscf-claim: verified
rscf-provenance: AMOS_corpus
conclusion_class: AMOS_MODEL
epistemic_class: SOURCE_CLAIM
topic: Decision Rights Map
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

# DECISION RIGHTS MAP

## Map — DECISION RIGHTS · MAP

Navigation map for the `23_OPERATING_MODEL/02_DECISION_RIGHTS/00_INDEX` segment of the Operating Model plane.

- **Contract** — [[23_OPERATING_MODEL/02_DECISION_RIGHTS/00_INDEX/DECISION_RIGHTS_OPERATING_MODEL_DECISION_RIGHTS_CONTRACT|DECISION_RIGHTS_OPERATING_MODEL_DECISION_RIGHTS_CONTRACT]]
- **Readme** — [[23_OPERATING_MODEL/02_DECISION_RIGHTS/00_INDEX/INDEX_DECISION_RIGHTS_OPERATING_MODEL_README|INDEX_DECISION_RIGHTS_OPERATING_MODEL_README]]

## Reading order

1. Readme → orientation. 2. Contract → normative terms. 3. Artifacts → instances bound by the contract.

## Gaps

This map covers its own directory only; cross-segment edges live in [[00_ROOT/00_ROOT_MAP|00_ROOT_MAP]] and [[00_ROOT/AMOS_RSCF_NODES|AMOS_RSCF_NODES]]. Executable graph validation remains PARTIAL ([[25_COGNITIVE_MATRIX/11_VALIDATION/ROUTING_POLICY_VALIDATION_RECEIPT|ROUTING_POLICY_VALIDATION_RECEIPT]] · [[03_CONTROL_PLANE/04_AUTHORITY/AUTHZ_ENGINE_VALIDATION_RECEIPT|AUTHZ_ENGINE_VALIDATION_RECEIPT]]).

## Worked semantics

Given an operation touching `DECISION RIGHTS · MAP` within the Operating Model plane:

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

- Governed by canon — [[01_CANON/01_CORE_LAWS/LAW_HIERARCHY|AMOS Core Laws]] · [[01_CANON/01_CORE_LAWS/LAW_HIERARCHY|LAW_HIERARCHY]]
- Kernel interaction — [[02_KERNEL/KERNEL_README|KERNEL_README]]
- Control-plane gates — [[03_CONTROL_PLANE/CONTROL_PLANE_README|CONTROL_PLANE_README]]
- Observed by — [[17_OBSERVABILITY/OBSERVABILITY_README|OBSERVABILITY_README]] · never treated as authority
- Recovered via operations — [[20_OPERATIONS/OPERATIONS_README|OPERATIONS_README]]

______________________________________________________________________

[[00_ROOT/00_ROOT_MOC|00_ROOT_MOC]] · [[00_ROOT/AMOS MOC|AMOS MOC]]

______________________________________________________________________

**Related:** [[00_ROOT/00_HOME|00_HOME]] · [[00_ROOT/AMOS_RSCF_NODES|AMOS_RSCF_NODES]]

______________________________________________________________________

RSCF-NODE
node_id: amos_23_operating_model_02_decision_rights_00_index_decision_rights_map_md
node_type: note
path: 23_OPERATING_MODEL/02_DECISION_RIGHTS/00_INDEX/DECISION_RIGHTS_MAP.md
claim_class: AMOS_MODEL

______________________________________________________________________

**MOC:** [[01_CANON/00_INDEX/00_INDEX_MOC|00_INDEX_MOC]]
