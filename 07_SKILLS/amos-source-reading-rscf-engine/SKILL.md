---
schema_version: 1.0
title: SKILL — Amos Source Reading Rscf Engine
type: skill
source: 07_SKILLS/amos-source-reading-rscf-engine
name: amos-source-reading-rscf-engine
description: Source Reading — knowledge research capability. Use when knowledge management,
  research, or Obsidian vault integration. Use when amos-knowledge-research-master
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

# Source Reading Rscf Engine

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

- **source_reading_eng.search_corpus**: Search the corpus directly: retrieve relevant passages with provenance
- **source_reading_eng.manage_artifact**: Manage research artifacts: create, version, and link to vault sources
- **source_reading_eng.trace_footprint**: Trace agent storage footprint and optimize knowledge retention
- **source_reading_eng.validate_epistemology**: Validate knowledge epistemology: source quality, freshness, and scope
- **source_reading_eng.index_knowledge**: Index knowledge for rapid retrieval and cross-reference navigation

> **Reference**: See `references/vault_domain_knowledge.md` (content_hash: 51bd6ec4facfbd92) for the full vault-sourced domain knowledge (9404 chars).
- **source_reading_eng.manage_lifecycle**: Manage lifecycle: classify, validate, trace, assess, detect.
- **source_reading_eng.detect_drift**: Detect drift in evidence chains, provenance freshness, or confidence calibration.
- **source_reading_eng.validate_outputs**: Validate outputs against domain constraints and epistemic class.

## Operations

1. **source_reading_eng.search_corpus**: Search the corpus directly: retrieve relevant passages with provenance
2. **source_reading_eng.manage_artifact**: Manage research artifacts: create, version, and link to vault sources
3. **source_reading_eng.trace_footprint**: Trace agent storage footprint and optimize knowledge retention
4. **source_reading_eng.validate_epistemology**: Validate knowledge epistemology: source quality, freshness, and scope
5. **source_reading_eng.index_knowledge**: Index knowledge for rapid retrieval and cross-reference navigation
6. **source_reading_eng.manage_lifecycle**: Manage lifecycle: classify, validate, trace, assess, detect.
7. **source_reading_eng.detect_drift**: Detect drift in evidence chains, provenance freshness, or confidence calibration.
8. **source_reading_eng.validate_outputs**: Validate outputs against domain constraints and epistemic class.

## 11_KNOWLEDGE Vault Content

> **Source**: `11_KNOWLEDGE/AMOS_COGNITIVE_ORGANISM_OS_DETAIL.md` (content_hash: 61279c4b00128110) (vault canon, SOURCE_CLAIM)

### RSCF Epistemic Substrate

This RSCF engine operates on the AMOS RSCF (Reasoning, Scope, Claim, Falsifier) epistemic substrate.

**RSCF objects**: claim / class / premises / evidence / provenance / scope / regime / freshness / dependencies / competing hypotheses / falsifiers / confidence ceiling.

**RSCF state kinds**: OBSERVATION, SOURCE_CLAIM, DERIVED, MODEL, DECISION, UNKNOWN.

**RSCF laws**:
- `CLAIM != FACT`: a claim is not a fact; it must be labeled with epistemic class
- `CONFIDENCE <= EVIDENCE`: confidence cannot exceed evidence support
- `FALSIFIER_REQUIRED`: every claim must declare its falsifier
- `SCOPE_BOUND`: every claim is valid only within its declared scope and regime
- `PROVENANCE_REQUIRED`: every claim must have traceable provenance

**RSCF validation gates**:
- G1 (Law of Law): no unresolved contradictions
- G2 (Epistemic class): all claims labeled, no class promotion without evidence
- G3 (Provenance): source path recorded for every derived claim
- G4 (Anti-overreach): no claim beyond declared scope
- G5 (Equation firewall): equations carry status tags
- G6 (Failure mode): on failure, downgrade, flag, escalate

### Epistemic Boundary

This RSCF engine is an epistemic governance tool. It does not prove claims are true, that all falsifiers are known, or that the RSCF framework is complete.

## Failure Modes

- **Insufficient evidence**: If source material is insufficient, mark as UNKNOWN/GAP and fail closed — do not fabricate.
- **Scope violation**: If the query falls outside the skill's declared scope, escalate to the parent skill or steward.
- **Binding broken**: If 1:1:1 binding (skill→agent→workflow) is broken, flag routing mismatch and block execution.
- **Validation failure**: If validation gates fail, downgrade confidence, flag the gap, and escalate — do not force-fit.
- **Epistemic overreach**: If a claim exceeds the established evidence or epistemic class, retract and relabel.

## Validation Gates

- **G1 (Law of Law)**: No unresolved contradictions within the skill's scope.
- **G2 (Epistemic class)**: All claims labeled SOURCE / DERIVED / AMOS_MODEL / EMPIRICAL — never claim beyond evidence.
- **G3 (Provenance)**: Source path recorded for every derived claim.
- **G4 (Anti-overreach)**: No claim beyond the skill's d

---
**Links:** [[07_SKILLS/07_SKILLS_MOC|07_SKILLS_MOC]]

## Related

- [[07_SKILLS/amos-source-reading-rscf-engine/amos-source-reading-rscf-engine_MOC|amos-source-reading-rscf-engine_MOC]]

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
- `amos-source-reading-rscf-engine-agent` — corresponding agent
---

**Related:** [[00_ROOT/00_HOME|00_HOME]] · [[00_ROOT/AMOS_RSCF_NODES|AMOS_RSCF_NODES]] · [[01_CANON/01_CORE_LAWS/LAW_HIERARCHY|LAW_HIERARCHY]] · [[07_SKILLS/07_SKILLS_MOC|07_SKILLS_MOC]] · references_MOC

**MOC:** [[07_SKILLS/07_SKILLS_MOC|07_SKILLS_MOC]]

**Trang Framework:** [[11_KNOWLEDGE/TRANG_FRAMEWORK_RECURSIVE_ONTOLOGY_DYNAMICS|TRANG_FRAMEWORK_RECURSIVE_ONTOLOGY_DYNAMICS]]

---
RSCF-NODE
node_id: amos-source-reading-rscf-engine
node_type: skill
path: 07_SKILLS/amos-source-reading-rscf-engine/SKILL.md
RSCF-RELATIONS:
- INDEXED_BY: [[00_ROOT/00_HOME|00_HOME]]
- INDEXED_BY: [[00_ROOT/AMOS_RSCF_NODES|AMOS_RSCF_NODES]]
- CHILD_OF: [[07_SKILLS/07_SKILLS_MOC|07_SKILLS_MOC]]
