---
schema_version: 1.0
title: SKILL — Amos Growth Graph
type: skill
source: 07_SKILLS/amos-growth-graph
name: amos-growth-graph
description: Growth Graph — society and culture capability. Use when social analysis, cultural reasoning, or anthropological study. Use when amos-c06-society-culture-master routes to this specialized capability. Do not use for generic tasks outside c06 domain.
parent_skill: amos-c06-society-culture-master
domain: c06
origin_architect: Trang Phan
epistemic_class: SOURCE_CLAIM
tags:
- type/skill
- canon/skill
- domain/society-culture
- rscf/source_claim
- hml/m
- epistemic/source_claim
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
- L7_authority
collapse_class: reversible
qfm_gate_set: QFM_v43
law_compliance:
- L0
- L1
- L2
- L4
- L5
- L7
- L16
- L17
- L18
license: MIT
steward: Trang Phan
---

# Growth Graph

## Identity

Origin architect: **Trang Phan**. Domain: c06. Parent: amos-c06-society-culture-master. Epistemic class: SOURCE_CLAIM. H/M/L: M.
## When to Use

- When modeling cognitive substrate memory graphs: field-level lineage, consolidation
- When analyzing memory operation graphs: vertices, edges, operations, queries
- When managing dependency-safe forgetting and reconsolidation
- When tracking growth patterns across knowledge and social networks
- When the parent skill (`amos-c06-society-culture-master`) routes to this specialized capability
- When managing lifecycle operations across classify, validate, trace, assess, and detect
- When detecting drift in evidence chains, provenance freshness, or confidence calibration
- When validating outputs against domain constraints and epistemic class

## Capabilities

- **growth_graph.analyze_social**: Analyze emergent social intelligence: norms, networks, and cultural dynamics
- **growth_graph.model_memory_graph**: Model cognitive substrate memory graphs: field-level lineage and consolidation
- **growth_graph.manage_forgetting**: Manage dependency-safe forgetting and reconsolidation governance
- **growth_graph.track_growth**: Track growth patterns across knowledge and social networks
- **growth_graph.detect_drift**: Detect drift in memory graphs, lineage chains, or growth patterns
- **growth_graph.manage_lifecycle**: Manage lifecycle: classify, validate, trace, assess, detect.
- **growth_graph.validate_outputs**: Validate outputs against domain constraints and epistemic class.

## Vault-Sourced Domain Knowledge

> **Sources**: `_00_Cosmo brain/dated/2026-08-22/2026-08-22 Cognitive Substrate Memory Graph.md` (content_hash: 89323199f0a3b075), `_00_Cosmo brain/cognitive/AMOS_Cognitive_Substrate_v2_Implementation_Notes.md` (content_hash: 39237d966cc491cf) (vault canon, SOURCE_CLAIM)

### Memory Operation Graph Formalization

`M_t = (V_t, E_t, O_t, I_t, Q_t, L_t)`

- `V_t`: vertices (memory items at time t)
- `E_t`: edges (relationships between memories)
- `O_t`: operations (create, update, merge, delete)
- `I_t`: indices (retrieval structures)
- `Q_t`: queries (retrieval requests)
- `L_t`: lineage (provenance chains)

### Field-Level Lineage

Partial-memory validity is tracked at the field level, not just the record level. Each field has its own lineage chain, enabling:
- Partial validity: some fields can be valid while others are stale
- Targeted reconsolidation: only invalid fields need refreshing
- Contradiction retention: conflicting values preserved with provenance

### Epistemic-Class Preservation Rules (8)

1. Class preservation: memory class must be preserved through operations
2. Modality: modal claims (possible, necessary) preserved
3. Negation: negative facts preserved as explicitly negated
4. Quantifier: universal vs existential quantifiers preserved
5. Correlation ≠ cause: correlations never promoted to causation
6. Future ≠ present: future predictions never stored as present facts
7. Perspective: observer perspective preserved
8. Provenance: source chain preserved for every field

### Retrieval Failure Attribution (6 types)

1. Missing index — no retrieval path exists
2. Stale entry — entry exists but is outdated
3. Scope violation — entry exists but outside query scope
4. Contradiction — multiple conflicting entries
5. Provenance gap — entry exists but provenance is broken
6. Epistemic class mismatch — entry class doesn't match query class

### 4-Slice Cognitive Architecture

- **Reality Gate**: filters inputs against reality constraints
- **Reasoning Graph**: 11 typed reasoning operators
- **Memory Graph**: 9 memory/structural operators
- **Interface Coupling**: external system integration

### Epistemic Boundary

Memory graph formalization is AMOS_MODEL. The cognitive substrate is a structural model of memory operations, NOT a neuroscience claim or cognitive architecture proof.

## Failure Modes

- **Insufficient evidence**: If source material is insufficient, mark as UNKNOWN/GAP and fail closed — do not fabricate.
- **Scope violation**: If the query falls outside the skill's declared scope, escalate to the parent skill or steward.
- **Binding broken**: If 1:1:1 binding (skill→agent→workflow) is broken, flag routing mismatch and block execution.
- **Validation failure**: If validation gates fail, downgrade confidence, flag the gap, and escalate — do not force-fit.
- **Epistemic overreach**: If a claim exceeds the established evide

---
**Links:** [[07_SKILLS_MOC]]

## Related

- [[amos-growth-graph_MOC]]

## Examples

- **Scenario**: When modeling cognitive substrate memory graphs: field-level lineage, consolidation
  - **Input**: A query matching this skill's domain (c06)
  - **Output**: Structured result with epistemic labels and provenance

- **Scenario**: When analyzing memory operation graphs: vertices, edges, operations, queries
  - **Input**: A query matching this skill's domain (c06)
  - **Output**: Structured result with epistemic labels and provenance

- **Scenario**: When managing dependency-safe forgetting and reconsolidation
  - **Input**: A query matching this skill's domain (c06)
  - **Output**: Structured result with epistemic labels and provenance


## Validation Gates

- **L0 Integrity**: All structural elements accounted for; no silent gaps
- **L1 Epistemic**: Every claim tagged with epistemic class (SOURCE_CLAIM / DERIVED / AMOS_MODEL)
- **L5 Scope**: Analysis confined to declared scope and domain
- **L7 Authority**: No autonomous action beyond authority boundary

## Anti-Patterns

- **Do not use** for tasks outside the c06 domain
- **Do not use** when the query requires empirical validation that this skill cannot provide
- **Do not use** when a parent skill or higher-level orchestrator should route instead
- **Do not bypass** epistemic class labeling — every output must carry SOURCE/DERIVED/AMOS_MODEL tags
- **Do not chain** more than 3 skills without explicit orchestrator approval


## Composition

- **Parent**: `amos-c06-society-culture-master` — routes to this skill when c06 specialization is needed
- **Peers**: Other skills in the `c06` domain may be composed in sequence
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

- For generic social analysis outside the society/culture framework
- To claim empirical validation of civilizational survival laws
- As a substitute for domain-specific historical or anthropological evidence
- Outside society/culture domain reasoning

## References

- `references/references_MOC.md` — loaded on demand
- `references/vault_domain_knowledge.md` — loaded on demand
- `[[amos-growth-graph_MOC]]` — skill Map of Content
- `amos-c06-society-culture-master` — parent skill
- `[[amos-growth-graph-workflow]]` — corresponding workflow
- `amos-growth-graph-agent` — corresponding agent
---

**Related:** [[00_HOME]] · [[AMOS_RSCF_NODES]] · [[LAW_HIERARCHY]] · [[07_SKILLS_MOC]] · [[references_MOC]]

**MOC:** [[07_SKILLS_MOC]]

**Trang Framework:** [[TRANG_FRAMEWORK_RECURSIVE_ONTOLOGY_DYNAMICS]]

---
RSCF-NODE
node_id: amos-growth-graph
node_type: skill
path: 07_SKILLS/amos-growth-graph/SKILL.md
RSCF-RELATIONS:
- INDEXED_BY: [[00_HOME]]
- INDEXED_BY: [[AMOS_RSCF_NODES]]
- CHILD_OF: [[07_SKILLS_MOC]]
