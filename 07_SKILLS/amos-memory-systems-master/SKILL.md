---
schema_version: 1.0
title: SKILL — Amos Memory Systems Master
type: skill
source: 07_SKILLS/amos-memory-systems-master
name: amos-memory-systems-master
description: AMOS Memory Systems — 3 memory types, context compaction, memory conflict resolution, memory immune system, action-memory firewall. Use when memory management, context continuity, or memory conflict. Do not use for generic tasks outside memory domain.
parent_skill: none
domain: memory
origin_architect: Trang Phan
epistemic_class: SOURCE_CANON
tags:
- type/skill
- canon/skill
- domain/memory-systems
- rscf/source_claim
- hml/m
- epistemic/source_canon
- amos_os
rscf:
  state: DERIVED
  claim_class: DERIVED
  provenance: AMOS_corpus
  scope: AMOS_general
version: 1.1.0
rscf_state: SOURCE_CLAIM
hml_level: M
gmef_gates:
- L0_integrity
- L1_epistemic
- L2_provenance
- L5_scope
collapse_class: reversible
qfm_gate_set: QFM_v43
law_compliance:
- L0
- L1
- L2
- L4
- L5
- L16
- L17
license: MIT
steward: Trang Phan
---

# [[MEMORY]] [[README]]

## Identity

Origin architect: **Trang Phan**. Domain: memory. Parent: none. Epistemic class: SOURCE_CANON. H/M/L: M.
## When to Use

AMOS Memory Systems — 3 memory types, context compaction, memory conflict resolution, memory immune system, action-memory firewall. Use for memory management, context continuity, or memory conflict...
- When validating outputs against domain constraints and epistemic class

## Capabilities

- **memory_systems.evaluate_influence**: Evaluate whether memory may influence a pending action through the AMOS Memory Systems consent, provenance, and risk gates.
- **memory_systems.validate_gates**: Validate AMOS Memory Systems decisions against hard partition gates, epistemic class preservation, and consent state requirements.
- **memory_systems.analyze_state**: Analyze AMOS Memory Systems memory state: working, episodic, semantic stores, consolidation, and retrieval graph health.
- **memory_systems.trace_provenance**: Trace AMOS Memory Systems memory entries to source, encoding operation, consolidation history, and field-level lineage.
- **memory_systems.assess_claim**: Assess AMOS Memory Systems memory claims for epistemic class, freshness, contradiction status, and confidence ceiling.
- **memory_systems.manage_lifecycle**: Manage AMOS Memory Systems lifecycle: encode, normalize, admit, consolidate, index, retrieve, filter, update.
- **memory_systems.detect_drift**: Detect memory drift: stale entries, broken provenance, epistemic class erosion, and context discontinuity.
- **memory_systems.escalate_gaps**: Escalate AMOS Memory Systems memory gaps: flag UNKNOWN/GAP entries, quarantine untrusted data, trigger memory repair.
- **memory_systems.validate_outputs**: Validate outputs against domain constraints and epistemic class.

## Consolidated Sub-Skills (3)

This parent skill consolidates the following sub-skills. Each is a section within this domain:

## Vault-Sourced Domain Knowledge

> **Source**: `10_MEMORY/MEMORY_README.md` from the AMOS_OS Obsidian vault.
> This is substantive domain knowledge, not script-generated content.

# [[MEMORY]] [[README]]

## Purpose
`MEMORY README` is the package readme for the **Memory** plane segment at `10_MEMORY`.
The Memory plane governs durable memory stores, trust classes, admission, retrieval, and conflict policy. Normative load-bearing content lives in the sibling contract(s); this readme orients navigation.

## Sibling artifacts
- [[MEMORY_MEMORY_CONTRACT]]

## Contract discipline
Typed artifacts · provenance stamped · epistemic class declared · confidence ceiling · fail-closed on UNKNOWN/GAP · receipts for consequential effects · rollback basin before mutation.

## Gaps
Executable binding PARTIAL unless an executed validation receipt exists for this subsystem ([[ROUTING_POLICY_VALIDATION_RECEIPT]] · [[AUTHZ_ENGINE_VALIDATION_RECEIPT]]).

## Worked semantics
Given an operation touching `MEMORY · README` within the Memory plane:
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
- Governed by canon — [[LAW_HIERARCHY|AMOS Core Laws]] · [[LAW_HIERARCHY]]
- Kernel interaction — [[KERNEL_README]]
- Control-plane gates — [[CONTROL_PLANE_README]]
- Observed by — [[OBSERVABILITY_README]] · never treated as authority
- Recovered via operations — OPERATI
- [[AGENT_TEMPLATE]]

---
**MOC:** [[amos-memory-systems-master_MOC]]

## Examples

- **Scenario**: When validating outputs against domain constraints and epistemic class
  - **Input**: A query matching this skill's domain (memory)
  - **Output**: Structured result with epistemic labels and provenance


## Validation Gates

- **L0 Integrity**: All structural elements accounted for; no silent gaps
- **L1 Epistemic**: Every claim tagged with epistemic class (SOURCE_CLAIM / DERIVED / AMOS_MODEL)
- **L5 Scope**: Analysis confined to declared scope and domain
- **L7 Authority**: No autonomous action beyond authority boundary

## Anti-Patterns

- **Do not use** for tasks outside the memory domain
- **Do not use** when the query requires empirical validation that this skill cannot provide
- **Do not use** when a parent skill or higher-level orchestrator should route instead
- **Do not bypass** epistemic class labeling — every output must carry SOURCE/DERIVED/AMOS_MODEL tags
- **Do not chain** more than 3 skills without explicit orchestrator approval


## Composition

- **Parent**: `none` — routes to this skill when memory specialization is needed
- **Peers**: Other skills in the `memory` domain may be composed in sequence
- **Orchestrator**: The parent skill or `AMOS_HOME` orchestrates routing
- **Workflow**: Each skill has a corresponding workflow in `08_WORKFLOWS/`
- **Agent**: Each skill has a corresponding agent in `06_AGENTS/`


## Evaluation

### Success Criteria

- Output includes epistemic class label (SOURCE/DERIVED/AMOS_MODEL/EMPIRICAL)
- Output includes provenance reference to source evidence
- Output includes confidence ceiling (capped at 0.95 for DERIVED, 1.0 for SOURCE_CANON)
- Output includes gap flags for unresolved unknowns
- Output does not exceed declared scope

### Failure Modes

- **Overreach**: Output claims validity beyond its epistemic class
- **Scope creep**: Output addresses questions outside the declared domain
- **Provenance loss**: Output cannot trace back to source evidence
- **Confidence inflation**: Output confidence exceeds the weakest-premise ceiling


## Error Handling

- **On scope violation**: Reject the query and route back to parent skill
- **On missing evidence**: Flag as GAP and reduce confidence ceiling to 0.5
- **On contradiction**: Flag as CRITICAL_GAP and halt until resolved
- **On provenance loss**: Mark output as UNKNOWN and require human review
- **On drift**: Trigger drift alignment via `amos-ai-drift-alignment-governor`


## Do not use

- For generic memory analysis outside the AMOS memory framework
- To claim empirical validation of memory consolidation theories
- As a substitute for domain-specific memory or context evidence
- Outside memory systems domain reasoning

## References

- `references/brain_engine_specs.md` — loaded on demand
- `references/distinct_working_memory.md` — loaded on demand
- `references/learning_memory_fractal.md` — loaded on demand
- `references/memory_architecture.md` — loaded on demand
- `references/memory_optimization_kernel.md` — loaded on demand
- `references/memory_write_agent.md` — loaded on demand
- `references/new_memory.md` — loaded on demand
- `references/references_MOC.md` — loaded on demand
- `` — skill Map of Content
- `none` — parent skill
- `` — corresponding workflow
- `amos-memory-systems-master-agent` — corresponding agent
---

**Related:** [[00_HOME]] · [[AMOS_RSCF_NODES]] · [[LAW_HIERARCHY]] · [[07_SKILLS_MOC]] · [[references_MOC]]

**MOC:** [[07_SKILLS_MOC]]

**Trang Framework:** [[TRANG_FRAMEWORK_RECURSIVE_ONTOLOGY_DYNAMICS]]

---
RSCF-NODE
node_id: amos-memory-systems-master
node_type: skill
path: 07_SKILLS/amos-memory-systems-master/[[SKILL]].md
RSCF-RELATIONS:
- INDEXED_BY: [[00_HOME]]
- INDEXED_BY: [[AMOS_RSCF_NODES]]
- CHILD_OF: [[07_SKILLS_MOC]]
