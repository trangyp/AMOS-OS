---
origin_architect: Trang Phan
steward: Trang Phan
amos_core_target: v4.4
title: TOOL MAP
type: map
source: 14_TOOLS/00_INDEX
tags:
  - amos-os
  - canon/tool
  - routing-policy-validation-receipt
  - authz-engine-validation-receipt
  - law-hierarchy
rscf:
  state: DERIVED
  claim_class: DERIVED
  provenance: AMOS_corpus
  scope: index_navigation
---

# TOOL MAP

## Map — TOOL MAP

Navigation map for the `14_TOOLS/00_INDEX` segment of the Tools plane.

- **Readme** — [[14_TOOLS/00_INDEX/INDEX_TOOLS_README|INDEX_TOOLS_README]]
- **Contract** — [[14_TOOLS/00_INDEX/INDEX_TOOLS_TOOL_CONTRACT|INDEX_TOOLS_TOOL_CONTRACT]]

## Tool registry

This is the live index of concrete tool artifacts in the `14_TOOLS` plane. Each entry resolves to its canonical specification or MOC.

- [[14_TOOLS/00_INDEX/INDEX_TOOLS_README|INDEX_TOOLS_README]] — Tools segment readme
- [[14_TOOLS/00_INDEX/INDEX_TOOLS_TOOL_CONTRACT|INDEX_TOOLS_TOOL_CONTRACT]] — Normative tool contract
- [[14_TOOLS/00_INDEX/TOOLS_MAP|TOOLS_MAP]] — Alias to this map
- [[14_TOOLS/14_TOOLS_MOC|14_TOOLS_MOC]] — Plane MOC
- [[14_TOOLS/AMOS_LLM_WIKI_TOOL|AMOS_LLM_WIKI_TOOL]] — LLM wiki tool
- [[14_TOOLS/AMOS_OBSIDIAN_LINKING_PLUGINS|AMOS_OBSIDIAN_LINKING_PLUGINS]] — Obsidian linking plugins
- [[14_TOOLS/AMOS_SELF_HEALING_AUTONOMOUS_WASI_MICRO_SANDBOX_GUIDE|AMOS_SELF_HEALING_AUTONOMOUS_WASI_MICRO_SANDBOX_GUIDE]] — WASI micro-sandbox guide
- [[14_TOOLS/SANDBOX_TOOL_EXECUTION_PROTOCOL|SANDBOX_TOOL_EXECUTION_PROTOCOL]] — Sandbox execution protocol
- [[14_TOOLS/SIMULATION_KERNEL_DISCRETE_SYSTEM_DYNAMICS|SIMULATION_KERNEL_DISCRETE_SYSTEM_DYNAMICS]] — Discrete system dynamics simulation kernel
- [[14_TOOLS/TOOLS_README|TOOLS_README]] — Plane readme
- [[14_TOOLS/TOOLS_TOOL_CONTRACT|TOOLS_TOOL_CONTRACT]] — Plane tool contract

## Reading order

1. Readme → orientation. 2. Contract → normative terms. 3. Artifacts → instances bound by the contract.

## Gaps

This map covers its own directory only; cross-segment edges live in [[00_ROOT/00_ROOT_MAP|00_ROOT_MAP]] and [[00_ROOT/AMOS_RSCF_NODES|AMOS_RSCF_NODES]]. Executable graph validation remains PARTIAL ([[25_COGNITIVE_MATRIX/11_VALIDATION/ROUTING_POLICY_VALIDATION_RECEIPT|ROUTING_POLICY_VALIDATION_RECEIPT]] · [[03_CONTROL_PLANE/04_AUTHORITY/AUTHZ_ENGINE_VALIDATION_RECEIPT|AUTHZ_ENGINE_VALIDATION_RECEIPT]]).

## Worked semantics

Given an operation touching `TOOL MAP` within the Tools plane:

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

- Governed by canon — [[01_CANON/01_CORE_LAWS/LAW_HIERARCHY|LAW_HIERARCHY]]|AMOS Core Laws · [[01_CANON/01_CORE_LAWS/LAW_HIERARCHY|LAW_HIERARCHY]]
- Kernel interaction — [[02_KERNEL/KERNEL_README|KERNEL_README]]
- Control-plane gates — [[03_CONTROL_PLANE/CONTROL_PLANE_README|CONTROL_PLANE_README]]
- Observed by — [[17_OBSERVABILITY/OBSERVABILITY_README|OBSERVABILITY_README]] · never treated as authority
- Recovered via operations — [[20_OPERATIONS/OPERATIONS_README|OPERATIONS_README]]

______________________________________________________________________

[[00_ROOT/00_ROOT_MOC|00_ROOT_MOC]]|[[00_ROOT/AMOS MOC|AMOS MOC]]

______________________________________________________________________

**Related:** [[00_ROOT/00_HOME|00_HOME]] · [[00_ROOT/AMOS_RSCF_NODES|AMOS_RSCF_NODES]]

______________________________________________________________________

RSCF-NODE
node_id: amos_14_tools_00_index_tool_map_md
node_type: note
path: 14_TOOLS/00_INDEX/TOOL_MAP.md
claim_class: AMOS_MODEL

______________________________________________________________________

**MOC:** [[01_CANON/00_INDEX/00_INDEX_MOC|00_INDEX_MOC]]
