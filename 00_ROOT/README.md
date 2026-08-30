---
title: README — 00 Root
type: note
source: 00_ROOT
aliases:
- - - README
rscf-state: derived
tags:
- index
- readme
- canon/root
- routing-policy-validation-receipt
- authz-engine-validation-receipt
- law-hierarchy
rscf:
  state: SOURCE_CLAIM
  claim_class: SOURCE_CLAIM
  provenance: AMOS_corpus
  scope: root_index
---

# README

## Purpose
`README` is the package readme for the **Root** plane segment at `00_ROOT`.
The Root plane governs vault-wide identity, architecture map, authoritative state pointers, and release governance. Normative load-bearing content lives in the sibling contract(s); this readme orients navigation.

## Sibling artifacts
- [[00_HOME]]
- [[00_COSMO_BRAIN_MOC]]
- [[00_ROOT_ARCHITECTURE]]
- [[00_ROOT_AUDIT]]
- [[00_ROOT_AUTHORIZATION]]
- [[00_ROOT_BOUNDARIES]]
- [[00_ROOT_CHANGE_LOG]]
- [[00_ROOT_CONTRACT]]
- [[00_ROOT_COVERAGE]]
- [[00_ROOT_DEPENDENCIES]]
- [[00_ROOT_GLOSSARY]]
- [[00_ROOT_HISTORY]]
- [[00_ROOT_IDENTITY]]
- [[00_ROOT_INTEGRATION_CHECKLIST]]
- [[00_ROOT_LIFECYCLE]]
- [[00_ROOT_MAP]]
- [[00_ROOT_MOC]]
- [[00_ROOT_NAMING_STANDARD]]
- [[00_ROOT_PROVENANCE]]
- [[00_ROOT_README]]
- [[00_ROOT_REGISTRY]]
- [[00_ROOT_RELEASE_NOTES]]
- [[00_ROOT_STATUS]]
- [[00_ROOT_VERSIONING]]
- … 14 more

## Contract discipline
Typed artifacts · provenance stamped · epistemic class declared · confidence ceiling · fail-closed on UNKNOWN/GAP · receipts for consequential effects · rollback basin before mutation.

## Gaps
Executable binding PARTIAL unless an executed validation receipt exists for this subsystem ([[ROUTING_POLICY_VALIDATION_RECEIPT]] · [[AUTHZ_ENGINE_VALIDATION_RECEIPT]]).
## Worked semantics
Given an operation touching `README` within the Root plane:
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
RSCF-NODE
node_id: 00_ROOT_READMEmd
node_type: note
path: 00_ROOT/README.md
RSCF-RELATIONS:
  - INDEXED_BY: [[00_HOME]]
  - INDEXED_BY: [[AMOS_RSCF_NODES]]
claim_class: AMOS_MODEL

---
**MOC:** [[00_COSMO_BRAIN_MOC]]
