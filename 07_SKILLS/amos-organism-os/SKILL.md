---
title: SKILL — Amos Organism Os
type: skill
source: 07_SKILLS/amos-organism-os
name: amos-organism-os
description: Organism Os — canon and universe capability. Use when canon reasoning,
  universe-level analysis, or invariant verification. Use when amos-canon-universe-master
  routes to this specialized capability.
parent_skill: amos-canon-universe-master
domain: canon
origin_architect: Trang Phan
epistemic_class: SOURCE_CLAIM
tags:
- type/skill
- canon/skill
- domain/canon-universe
- canon-group/tech-ai
- topic/canon
- rscf/epistemic
- rscf/C-constraint
- rscf/D-distinction
- rscf/G-relation
- rscf/S-state
- rscf/type-model
- sota/progressive-disclosure
- sota/anti-patterns
- amos_os
- amos-organism-os
- capability/reasoning
rscf:
  state: DERIVED
  claim_class: DERIVED
  provenance: AMOS_corpus
  scope: AMOS_general
version: 1.1.0
rscf_state: SOURCE_CLAIM
hml_level: H
gmef_gates:
- L0_integrity
- L1_epistemic
- L2_provenance
- L3_dependency
- L5_scope
- L7_authority
collapse_class: reversible
qfm_gate_set: QFM_v43
law_compliance:
- L0
- L1
- L2
- L3
- L4
- L5
- L7
- L16
- L17
- L18
- L19
---







# Organism Os

## Identity

- **Origin architect and steward**: Trang Phan
- **Parent skill**: `amos-canon-universe-master`
- **Domain**: canon
- **Epistemic class**: SOURCE_CLAIM (vault-sourced from AMOS framework)

Canon and universe engine for Organism Os

## When to Use

- When compiling canonical structure from vault sources
- When checking canon consistency for contradictions and gaps
- When enforcing canon invariants across all parts
- When navigating canon to locate parts for any topic
- When the parent skill (`amos-canon-universe-master`) routes to this specialized capability
- When managing lifecycle operations across classify, validate, trace, assess, and detect
- When detecting drift in evidence chains, provenance freshness, or confidence calibration
- When validating outputs against domain constraints and epistemic class

## Capabilities

- **organism.compile_canon**: Compile canonical structure from sources into a consistent, navigable canon
- **organism.check_consistency**: Check canon consistency: no contradictions, no gaps, no orphan references
- **organism.enforce_invariant**: Enforce canon invariants: structural laws that must hold across all parts
- **organism.navigate_canon**: Navigate canon: locate the canonical part for any topic or query
- **organism.validate_substrate**: Validate canonical software substrate against canon requirements
- **organism.manage_lifecycle**: Manage lifecycle: classify, validate, trace, assess, detect.
- **organism.detect_drift**: Detect drift in evidence chains, provenance freshness, or confidence calibration.
- **organism.validate_outputs**: Validate outputs against domain constraints and epistemic class.

## Vault-Sourced Domain Knowledge

> **Source**: `11_KNOWLEDGE/AMOS_COGNITIVE_ORGANISM_OS.md` (content_hash: 3c4ff0d94377f3fe) (vault canon, SOURCE_CLAIM)

### Organism Architecture (170 sections)

The Cognitive Organism OS defines a maximum-detail unified cognitive-life architecture with 170 sections covering:

- **Organism Core** (M1): Identity, state, flow, memory, governance
- **Organ Registry** (M2): Organ contracts, organ states, event bus, state mutation boundary
- **Perception Organ** (M3): Observation/interpretation separation, attention, context budget
- **Cognition Organ** (M4): Meta logic, Law of Law, Rule of 2/4, signal fidelity, structural integrity
- **Structural Reasoning Organ** (M5): Problem graph, causal graph, causal firewall, multi-possibility
- **Memory System** (M6): Working, episodic, semantic, canonical, procedural, case memory + immune + repair
- **World Model Organ** (M7): Reality-contact layer, emotion/regulation, emotional inference boundary
- **Decision Organ** (M8): Utility, future debt, option value, action authority, prepare/commit distinction
- **Learning Organ** (M9): Closed-loop learning, GMEF model evolution, learning firewall
- **Repair Organ** (M10): Repair priority, collapse model, recovery basin, graceful shutdown, restart capsule
- **Safety/Constraint Organ** (M11): Risk tensor, information boundary, exposure control, protected knowledge
- **Multi-Agent Organism** (M12): Agent roles, collective cognition, diversity-coherence governance

### Key Architectural Laws

- COMPUTE_BUDGET != BIOLOGICAL_ENERGY
- SELF_MODEL != SUBJECTIVE_SELF
- AUTONOMY != UNBOUNDED_PERMISSION
- Cognition != Control
- Capability != Authority

### Epistemic Boundary

AMOS Cognitive Organism OS is an operational systems architecture. It does not prove a software system is biologically alive, physically embodied, phenomenally conscious, emotionally sentient, self-causing, morally autonomous, independently sovereign, or causally closed. The organism vocabulary is architectural, not biological.


## Failure Modes

- **Insufficient evidence**: If source material is insufficient, mark as UNKNOWN/GAP and fail closed — do not fabricate.
- **Scope violation**: If the query falls outside the skill's declared scope, escalate to the parent skill or steward.
- **Binding broken**: If 1:1:1 binding (skill→agent→workflow) is broken, flag routing mismatch and block execution.
- **Validation failure**: If validation gates fail, downgrade confidence, flag the gap, and escalate — do not force-fit.
- **Epistemic overreach**: If a claim exceeds the established evidence or epistemic class, retract and relabel.

## Validation Gates

- **G1 (Law of Law)**: No unresolved contradictions within the skill's scope.
- **G2 (Epistemic class)**: All claims labeled SOURCE / DERIVED / AMOS_MODEL / EMPIRICAL — never claim beyond evidence.
- **G3 (Provenance)**: Source path recorded

---
**Links:** [[07_SKILLS_MOC]]

## Related

- [[amos-organism-os_MOC]]

## Examples

- **Scenario**: When compiling canonical structure from vault sources
  - **Input**: A query matching this skill's domain (canon)
  - **Output**: Structured result with epistemic labels and provenance

- **Scenario**: When checking canon consistency for contradictions and gaps
  - **Input**: A query matching this skill's domain (canon)
  - **Output**: Structured result with epistemic labels and provenance

- **Scenario**: When enforcing canon invariants across all parts
  - **Input**: A query matching this skill's domain (canon)
  - **Output**: Structured result with epistemic labels and provenance


## Anti-Patterns

- **Do not use** for tasks outside the canon domain
- **Do not use** when the query requires empirical validation that this skill cannot provide
- **Do not use** when a parent skill or higher-level orchestrator should route instead
- **Do not bypass** epistemic class labeling — every output must carry SOURCE/DERIVED/AMOS_MODEL tags
- **Do not chain** more than 3 skills without explicit orchestrator approval


## Composition

- **Parent**: `amos-canon-universe-master` — routes to this skill when canon specialization is needed
- **Peers**: Other skills in the `canon` domain may be composed in sequence
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


## References

- `references/bluememory_water_scarcity_os.md` — loaded on demand
- `references/references_MOC.md` — loaded on demand
- `[[amos-organism-os_MOC]]` — skill Map of Content
- `amos-canon-universe-master` — parent skill
- `[[amos-organism-os-workflow]]` — corresponding workflow
- `amos-organism-os-agent` — corresponding agent
---

**Related:** [[00_HOME]] · [[AMOS_RSCF_NODES]] · [[LAW_HIERARCHY]] · [[07_SKILLS_MOC]] · [[references_MOC]]

**MOC:** [[07_SKILLS_MOC]]

**Trang Framework:** [[TRANG_FRAMEWORK_RECURSIVE_ONTOLOGY_DYNAMICS]]

---
RSCF-NODE
node_id: amos-organism-os
node_type: skill
path: 07_SKILLS/amos-organism-os/SKILL.md
RSCF-RELATIONS:
- INDEXED_BY: [[00_HOME]]
- INDEXED_BY: [[AMOS_RSCF_NODES]]
- CHILD_OF: [[07_SKILLS_MOC]]
