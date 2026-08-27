---
tags: ['amos_os', '05_cognitive_organism']
---

# COGNITIVE ORGANISM README

## Purpose
`COGNITIVE ORGANISM README` is the package readme for the **Cognitive Organism** plane segment at `05_COGNITIVE_ORGANISM`.
The Cognitive Organism plane governs the organism-level cognitive assembly above kernels and below agents. Normative load-bearing content lives in the sibling contract(s); this readme orients navigation.

## Sibling artifacts
- [[COGNITIVE_ORGANISM_COGNITIVE_ORGANISM_CONTRACT]]

## Contract discipline
Typed artifacts · provenance stamped · epistemic class declared · confidence ceiling · fail-closed on UNKNOWN/GAP · receipts for consequential effects · rollback basin before mutation.

## Gaps
Executable binding PARTIAL unless an executed validation receipt exists for this subsystem ([[ROUTING_POLICY_VALIDATION_RECEIPT]] · [[AUTHZ_ENGINE_VALIDATION_RECEIPT]]).
## Worked semantics
Given an operation touching `COGNITIVE ORGANISM README` within the Cognitive Organism plane:
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
- Governed by canon — [[01_CANON/01_CORE_LAWS/LAW_HIERARCHY|AMOS Core Laws]] · [[LAW_HIERARCHY]]
- Kernel interaction — [[KERNEL_README]]
- Control-plane gates — [[CONTROL_PLANE_README]]
- Observed by — [[OBSERVABILITY_README]] · never treated as authority
- Recovered via operations — [[OPERATIONS_README]]
---

[[00_ROOT/00_ROOT_MOC.md|AMOS MOC]]

---
**Related:** [[00_ROOT/00-Home]] · [[AMOS_RSCF_NODES]]

---
RSCF-NODE
node_id: amos_05_cognitive_organism_cognitive_organism_readme_md
node_type: note
path: 05_COGNITIVE_ORGANISM/COGNITIVE_ORGANISM_README.md
claim_class: AMOS_MODEL
