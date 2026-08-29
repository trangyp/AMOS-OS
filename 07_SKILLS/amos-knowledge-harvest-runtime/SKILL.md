---
schema_version: 1.0
title: SKILL — Amos Knowledge Harvest Runtime
type: skill
source: 07_SKILLS/amos-knowledge-harvest-runtime
name: amos-knowledge-harvest-runtime
description: Knowledge Harvest Runtime — knowledge research capability. Use when knowledge
  management, research, or Obsidian vault integration. Use when amos-knowledge-research-master
  routes to this specialized capability. Do not use for generic tasks outside knowledge
  domain.
parent_skill: amos-knowledge-research-master
domain: knowledge
origin_architect: Trang Phan
epistemic_class: SOURCE_CLAIM
tags:
- type/skill
- type/skill
- domain/knowledge-research
- epistemic/source_claim
- hml/m
- epistemic/source_claim
- amos-os
- law-hierarchy
- trang-framework-recursive-ontology-dynamics
- skill
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

# Knowledge Harvest Runtime

## Identity

Origin architect: **Trang Phan**. Domain: knowledge. Parent: amos-knowledge-research-master. Epistemic class: SOURCE_CLAIM. H/M/L: M.
## When to Use

- When searching the corpus for relevant passages with provenance
- When managing research artifacts and linking to vault sources
- When tracing agent storage footprint and optimizing retention
- When validating knowledge epistemology and source quality
- When the parent skill (`amos-knowledge-research-master`) routes to this specialized capability
- When managing lifecycle operations across classify, validate, trace, assess, and detect
- When detecting drift in evidence chains, provenance freshness, or confidence calibration
- When validating outputs against domain constraints and epistemic class

## Capabilities

- **knowledge_harvest.search_corpus**: Search the corpus directly: retrieve relevant passages with provenance
- **knowledge_harvest.manage_artifact**: Manage research artifacts: create, version, and link to vault sources
- **knowledge_harvest.trace_footprint**: Trace agent storage footprint and optimize knowledge retention
- **knowledge_harvest.validate_epistemology**: Validate knowledge epistemology: source quality, freshness, and scope
- **knowledge_harvest.index_knowledge**: Index knowledge for rapid retrieval and cross-reference navigation
- **knowledge_harvest.manage_lifecycle**: Manage lifecycle: classify, validate, trace, assess, detect.
- **knowledge_harvest.detect_drift**: Detect drift in evidence chains, provenance freshness, or confidence calibration.
- **knowledge_harvest.validate_outputs**: Validate outputs against domain constraints and epistemic class.

> **Reference**: See `references/vault_domain_knowledge.md` (content_hash: d13ba2328adc6f64) for the full vault-sourced domain knowledge (7366 chars).

## Operations

1. **knowledge_harvest.search_corpus**: Search the corpus directly: retrieve relevant passages with provenance
2. **knowledge_harvest.manage_artifact**: Manage research artifacts: create, version, and link to vault sources
3. **knowledge_harvest.trace_footprint**: Trace agent storage footprint and optimize knowledge retention
4. **knowledge_harvest.validate_epistemology**: Validate knowledge epistemology: source quality, freshness, and scope
5. **knowledge_harvest.index_knowledge**: Index knowledge for rapid retrieval and cross-reference navigation
6. **knowledge_harvest.manage_lifecycle**: Manage lifecycle: classify, validate, trace, assess, detect.
7. **knowledge_harvest.detect_drift**: Detect drift in evidence chains, provenance freshness, or confidence calibration.
8. **knowledge_harvest.validate_outputs**: Validate outputs against domain constraints and epistemic class.

## 11_KNOWLEDGE Vault Content

> **Source**: `_00_Cosmo brain/misc/K/KNOWLEDGE_HARVEST.md` (content_hash: ebf6cf9c8fcd5127) (vault canon, SOURCE_CLAIM)
> **Additional source**: `11_KNOWLEDGE/AMOS_COGNITIVE_ORGANISM_OS_DETAIL.md` (content_hash: 61279c4b00128110) (vault canon, SOURCE_CLAIM)

### Knowledge Harvest Runtime

From Cosmo Brain Knowledge Harvest: Ephemeral Code -> Persistent Evidence -> Validated Knowledge. Reject: Ephemeral Code -> LLM Summary -> Delete Evidence.

**Principle**: `Ephemeral Code -> Persistent Evidence -> Validated Knowledge`
**Rejected pattern**: `Ephemeral Code -> LLM Summary -> Delete Evidence`

**Structural equation**: `PermanentKnowledge = Claim + Scope + Evidence + Provenance + Constraint + FailureMode + Validity + Lineage`

**7-step pipeline**:
1. **Acquire/fingerprint**: acquire the knowledge and fingerprint it
2. **Deterministic structure extraction**: extract structure deterministically
3. **Small falsifiable semantic claims**: break into small falsifiable claims
4. **Provenance/evidence/regime/governance validation**: validate with full governance
5. **Structured storage**: store in structured form
6. **Retention-class-controlled cleanup**: cleanup with retention class control
7. **Compact retrieval compilation**: compile for compact retrieval

**Retrieval compiler**: `user_problem -> AMOS_structural_decomposition -> knowledge_registry_query -> candidate_RSCF_retrieval -> scope_filter -> evidence_filter -> freshness_filter -> governance_filter -> conflict_field_resolution -> compact_context_compile -> LLM_or_agent`

**Anti-pattern**: `vector_search -> dump_many_raw_repository_chunks -> LLM` (rejected -- no scope/evidence/freshness/governance filtering)

**Harvest laws**:
- `EPHEMERAL != PERMANENT`: ephemeral code is not permanent knowledge; it must be harvested
- `SUMMARY != EVIDENCE**: LLM summary is not evidence; evidence must be independently validated
- `CLAIM != KNOWLEDGE**: a claim is not knowledge; knowledge requires claim + scope + evidence + provenance + constraint + failure mode + validity + lineage

### Epistemic Boundary

Knowledge harvest runtime is an operational construct. It does not prove all knowledge is harvested, that the pipeline is optimal, or that harvested knowledge is always correct.

## Failure Modes

- **Insufficient evidence**: If source material is insufficient, mark as UNKNOWN/GAP and fail closed — do not fabricate.
- **Scope violation**: If the query falls outside the skill's declared scope, escalate to the parent skill or steward.
- **Binding broken**: If 1:1:1 binding

---
**Links:** [[07_SKILLS_MOC]]

## Related

- [[amos-knowledge-harvest-runtime_MOC]]

## Examples

- **Scenario**: When searching the corpus for relevant passages with provenance
  - **Input**: A query matching this skill's domain (knowledge)
  - **Output**: Structured result with epistemic labels and provenance

- **Scenario**: When managing research artifacts and linking to vault sources
  - **Input**: A query matching this skill's domain (knowledge)
  - **Output**: Structured result with epistemic labels and provenance

- **Scenario**: When tracing agent storage footprint and optimizing retention
  - **Input**: A query matching this skill's domain (knowledge)
  - **Output**: Structured result with epistemic labels and provenance


## Validation Gates

- **L0 Integrity**: All structural elements accounted for; no silent gaps
- **L1 Epistemic**: Every claim tagged with epistemic class (SOURCE_CLAIM / DERIVED / AMOS_MODEL)
- **L5 Scope**: Analysis confined to declared scope and domain
- **L7 Authority**: No autonomous action beyond authority boundary

## Anti-Patterns

- **Do not use** for tasks outside the knowledge domain
- **Do not use** when the query requires empirical validation that this skill cannot provide
- **Do not use** when a parent skill or higher-level orchestrator should route instead
- **Do not bypass** epistemic class labeling — every output must carry SOURCE/DERIVED/AMOS_MODEL tags
- **Do not chain** more than 3 skills without explicit orchestrator approval


## Composition

- **Parent**: `amos-knowledge-research-master` — routes to this skill when knowledge specialization is needed
- **Peers**: Other skills in the `knowledge` domain may be composed in sequence
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

- For generic knowledge management outside the AMOS knowledge framework
- To claim empirical validation of knowledge representation theories
- As a substitute for domain-specific research or curatorial evidence
- Outside knowledge research domain reasoning

## References

- `references/references_MOC.md` — loaded on demand
- `references/vault_domain_knowledge.md` — loaded on demand
- `` — skill Map of Content
- `amos-knowledge-research-master` — parent skill
- `` — corresponding workflow
- `amos-knowledge-harvest-runtime-agent` — corresponding agent
---

**Related:** [[00_HOME]] · [[AMOS_RSCF_NODES]] · [[LAW_HIERARCHY]] · [[07_SKILLS_MOC]] · references_MOC

**MOC:** [[07_SKILLS_MOC]]

**Trang Framework:** [[TRANG_FRAMEWORK_RECURSIVE_ONTOLOGY_DYNAMICS]]

---
RSCF-NODE
node_id: amos-knowledge-harvest-runtime
node_type: skill
path: 07_SKILLS/amos-knowledge-harvest-runtime/SKILL.md
RSCF-RELATIONS:
- INDEXED_BY: [[00_HOME]]
- INDEXED_BY: [[AMOS_RSCF_NODES]]
- CHILD_OF: [[07_SKILLS_MOC]]
