---
title: OPERATING MODEL README
type: model
source: 23_OPERATING_MODEL
tags:
- amos_os
- 23_operating_model
- canon/operating-model
- readme
- operating-model-operating-model-contract
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
- amos-rscf-nodes
- 23-operating-model-moc
rscf:
  state: DERIVED
  claim_class: DERIVED
  provenance: AMOS_corpus
  scope: AMOS_general
---

# OPERATING MODEL [[README]]

## Purpose
`OPERATING MODEL README` is the package readme for the **Operating Model** plane segment at `23_OPERATING_MODEL`.
The Operating Model plane governs roles, decision rights, governance forums, escalation paths, service levels. Normative load-bearing content lives in the sibling contract(s); this readme orients navigation.

## Sibling artifacts
- [[OPERATING_MODEL_OPERATING_MODEL_CONTRACT]]

## Contract discipline
Typed artifacts · provenance stamped · epistemic class declared · confidence ceiling · fail-closed on UNKNOWN/GAP · receipts for consequential effects · rollback basin before mutation.

## Gaps
Executable binding PARTIAL unless an executed validation receipt exists for this subsystem ([[ROUTING_POLICY_VALIDATION_RECEIPT]] · [[AUTHZ_ENGINE_VALIDATION_RECEIPT]]).
## Worked semantics
Given an operation touching `OPERATING MODEL · README` within the Operating Model plane:
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
node_id: amos_23_operating_model_operating_model_readme_md
node_type: note
path: 23_OPERATING_MODEL/OPERATING_MODEL_README.md
claim_class: AMOS_MODEL

---
**MOC:** [[23_OPERATING_MODEL_MOC]]
