---
origin_architect: Trang Phan
steward: Trang Phan
amos_core_target: v4.4
title: Amos-Qls-Qic-Substrate-Mapper MOC
type: moc
source: 07_SKILLS/amos-qls-qic-substrate-mapper
tags:
  - amos-qls-qic-substrate-mapper
  - type/skill
  - skill
moc: true
rscf:
  state: DERIVED
  claim_class: DERIVED
  provenance: AMOS_corpus
  scope: AMOS_general
---

# Amos-Qls-Qic-Substrate-Mapper — Map of Content

## Map — amos-qls-qic-substrate-mapper MOC
Navigation map for the `07_SKILLS/amos-qls-qic-substrate-mapper` segment of the Skills plane.

- **Artifact** — [[SKILL]]

## Reading order
1. Readme → orientation.  2. Contract → normative terms.  3. Artifacts → instances bound by the contract.

## Gaps
This map covers its own directory only; cross-segment edges live in [[00_ROOT_MAP]] and [[AMOS_RSCF_NODES]]. Executable graph validation remains PARTIAL ([[ROUTING_POLICY_VALIDATION_RECEIPT]] · [[AUTHZ_ENGINE_VALIDATION_RECEIPT]]).
## Worked semantics
Given an operation touching `amos-qls-qic-substrate-mapper MOC` within the Skills plane:
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
