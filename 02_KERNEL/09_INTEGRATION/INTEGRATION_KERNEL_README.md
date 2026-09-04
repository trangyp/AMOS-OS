---
canon-group: meta
canon-type: framework
rscf-state: source-claim
rscf-claim: verified
rscf-provenance: AMOS_corpus
conclusion_class: AMOS_MODEL
epistemic_class: SOURCE_CLAIM
topic: Integration Kernel Readme
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

# INTEGRATION KERNEL README

## Purpose

`INTEGRATION KERNEL README` is the package readme for the **Kernel** plane segment at `02_KERNEL/09_INTEGRATION`.
The Kernel plane governs kernel-plane reasoning primitives: meta-logic, cognition, causality, state, memory, risk-repair, authority, provenance, integration. Normative load-bearing content lives in the sibling contract(s); this readme orients navigation.

## Sibling artifacts

- [[02_KERNEL/09_INTEGRATION/KERNEL_INTEGRATION_CONTRACT|KERNEL_INTEGRATION_CONTRACT]]
- [[02_KERNEL/09_INTEGRATION/K_BINDING|K_BINDING]]
- [[02_KERNEL/09_INTEGRATION/K_CONSTRAINT_PROPAGATION|K_CONSTRAINT_PROPAGATION]]
- [[02_KERNEL/09_INTEGRATION/K_GMEF|K_GMEF]]
- [[02_KERNEL/09_INTEGRATION/K_HML|K_HML]]
- [[02_KERNEL/09_INTEGRATION/K_RSCF|K_RSCF]]
- [[02_KERNEL/09_INTEGRATION/K_TRANSLATION|K_TRANSLATION]]

## Contract discipline

Typed artifacts · provenance stamped · epistemic class declared · confidence ceiling · fail-closed on UNKNOWN/GAP · receipts for consequential effects · rollback basin before mutation.

## Gaps

Executable binding PARTIAL unless an executed validation receipt exists for this subsystem ([[25_COGNITIVE_MATRIX/11_VALIDATION/ROUTING_POLICY_VALIDATION_RECEIPT|ROUTING_POLICY_VALIDATION_RECEIPT]] · [[03_CONTROL_PLANE/04_AUTHORITY/AUTHZ_ENGINE_VALIDATION_RECEIPT|AUTHZ_ENGINE_VALIDATION_RECEIPT]]).

## Worked semantics

Given an operation touching `INTEGRATION KERNEL README` within the Kernel plane:

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
node_id: amos_02_kernel_09_integration_integration_kernel_readme_md
node_type: note
path: 02_KERNEL/09_INTEGRATION/INTEGRATION_KERNEL_README.md
claim_class: AMOS_MODEL

______________________________________________________________________

**MOC:** [[02_KERNEL/09_INTEGRATION/09_INTEGRATION_MOC|09_INTEGRATION_MOC]]

______________________________________________________________________

**Trang Framework:** [[11_KNOWLEDGE/TRANG_FRAMEWORK_RECURSIVE_ONTOLOGY_DYNAMICS|TRANG_FRAMEWORK_RECURSIVE_ONTOLOGY_DYNAMICS]]
