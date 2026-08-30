---
title: SKILL MAP
type: skill
source: 07_SKILLS/00_INDEX
tags:
- amos-os
- type/skill
- skill
- skill-naming-audit
- skill-rename-manifest
- agent-naming-audit
- cloud-skill-rename-audit
- routing-policy-validation-receipt
- authz-engine-validation-receipt
- law-hierarchy
rscf:
  state: DERIVED
  claim_class: DERIVED
  provenance: AMOS_corpus
  scope: index_navigation
---

# SKILL MAP

## Map — SKILL MAP
Navigation map for the `07_SKILLS/00_INDEX` segment of the Skills plane.

- **Readme** — [[07_SKILLS/00_INDEX/INDEX_SKILLS_README|INDEX_SKILLS_README]]
- **Contract** — [[07_SKILLS/00_INDEX/INDEX_SKILLS_SKILL_CONTRACT|INDEX_SKILLS_SKILL_CONTRACT]]

## Artifacts
- [[07_SKILLS/SKILLS_SKILL_CONTRACT|SKILLS_SKILL_CONTRACT]] — skills plane contract
- [[07_SKILLS/SKILLS_README|SKILLS_README]] — skills plane readme
- [[07_SKILLS/SKILL_NAMING_AUDIT|SKILL_NAMING_AUDIT]] — skill naming audit
- [[07_SKILLS/SKILL_RENAME_MANIFEST|SKILL_RENAME_MANIFEST]] — skill rename manifest
- [[07_SKILLS/AGENT_NAMING_AUDIT|AGENT_NAMING_AUDIT]] — agent naming audit
- [[07_SKILLS/CLOUD_SKILL_RENAME_AUDIT|CLOUD_SKILL_RENAME_AUDIT]] — cloud skill rename audit

## Reading order
1. Readme → orientation.  2. Contract → normative terms.  3. Artifacts → instances bound by the contract.

## Gaps
This map covers its own directory only; cross-segment edges live in [[00_ROOT/00_ROOT_MAP|00_ROOT_MAP]] and [[00_ROOT/AMOS_RSCF_NODES|AMOS_RSCF_NODES]]. Executable graph validation remains PARTIAL ([[25_COGNITIVE_MATRIX/11_VALIDATION/ROUTING_POLICY_VALIDATION_RECEIPT|ROUTING_POLICY_VALIDATION_RECEIPT]] · [[03_CONTROL_PLANE/04_AUTHORITY/AUTHZ_ENGINE_VALIDATION_RECEIPT|AUTHZ_ENGINE_VALIDATION_RECEIPT]]).
## Worked semantics
Given an operation touching `SKILL MAP` within the Skills plane:
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
- Governed by canon — [[01_CANON/01_CORE_LAWS/LAW_HIERARCHY|LAW_HIERARCHY]]|AMOS Core Laws · [[01_CANON/01_CORE_LAWS/LAW_HIERARCHY|LAW_HIERARCHY]]
- Kernel interaction — [[02_KERNEL/KERNEL_README|KERNEL_README]]
- Control-plane gates — [[03_CONTROL_PLANE/CONTROL_PLANE_README|CONTROL_PLANE_README]]
- Observed by — [[17_OBSERVABILITY/OBSERVABILITY_README|OBSERVABILITY_README]] · never treated as authority
- Recovered via operations — [[20_OPERATIONS/OPERATIONS_README|OPERATIONS_README]]
---

[[00_ROOT/00_ROOT_MOC|00_ROOT_MOC]]|[[00_ROOT/AMOS MOC|AMOS MOC]]

---
**Related:** [[00_ROOT/00_HOME|00_HOME]] · [[00_ROOT/AMOS_RSCF_NODES|AMOS_RSCF_NODES]]

---
RSCF-NODE
node_id: amos_07_skills_00_index_skill_map_md
node_type: note
path: 07_SKILLS/00_INDEX/SKILL_MAP.md
claim_class: AMOS_MODEL

---
**MOC:** [[01_CANON/00_INDEX/00_INDEX_MOC|00_INDEX_MOC]]
