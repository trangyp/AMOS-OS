---
schema_version: 1.0
title: SKILL — Amos Consciousness Candidate Governor
type: skill
source: 07_SKILLS/amos-consciousness-candidate-governor
name: amos-consciousness-candidate-governor
description: Consciousness Candidate Governor — mind and behavior capability. Use
  when psychological analysis, behavioral reasoning, or cognitive modeling. Use when
  amos-c05-mind-behavior-master routes to this specialized capability. Do not use
  for generic tasks outside c05 domain.
parent_skill: amos-c05-mind-behavior-master
domain: c05
origin_architect: Trang Phan
epistemic_class: SOURCE_CLAIM
tags:
- type/skill
- canon/skill
- domain/mind-behavior
- rscf/source_claim
- hml/m
- epistemic/source_claim
- amos_os
- 07-skills-moc
- 00-home
- amos-rscf-nodes
- law-hierarchy
- references-moc
- amos-consciousness-candidate-governor-moc
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

# Consciousness Candidate Governor

## Identity

Origin architect: **Trang Phan**. Domain: c05. Parent: amos-c05-mind-behavior-master. Epistemic class: SOURCE_CLAIM. H/M/L: M.
## When to Use

- When modeling cognitive processes: attention, awareness, compression
- When allocating attention resources across competing demands
- When assessing awareness levels and meta-cognition
- When governing artistic and emotional expression within bounds
- When the parent skill (`amos-c05-mind-behavior-master`) routes to this specialized capability
- When managing lifecycle operations across classify, validate, trace, assess, and detect
- When detecting drift in evidence chains, provenance freshness, or confidence calibration
- When validating outputs against domain constraints and epistemic class

## Capabilities

- **consciousness_candidate.model_cognition**: Model cognitive processes: attention, awareness, compression, and inference
- **consciousness_candidate.allocate_attention**: Allocate attention resources across competing demands and priorities
- **consciousness_candidate.assess_awareness**: Assess awareness levels: meta-cognition, self-monitoring, and calibration
- **consciousness_candidate.govern_expression**: Govern artistic and emotional expression within healthy bounds

> **Reference**: See `references/vault_domain_knowledge.md` (content_hash: 17be42ec861460fe) for the full vault-sourced domain knowledge (9552 chars).
- **consciousness_candidate.manage_lifecycle**: Manage lifecycle: classify, validate, trace, assess, detect.
- **consciousness_candidate.detect_drift**: Detect drift in evidence chains, provenance freshness, or confidence calibration.
- **consciousness_candidate.validate_outputs**: Validate outputs against domain constraints and epistemic class.

## 11_KNOWLEDGE Vault Content

> **Source**: `11_KNOWLEDGE/AMOS_COGNITIVE_ORGANISM_OS_DETAIL.md` (content_hash: 61279c4b00128110) (vault canon, SOURCE_CLAIM)

### Consciousness Candidate Governance

The Cognitive Organism OS models consciousness-candidate governance as a structural framework, not a phenomenological claim.

**Consciousness-candidate architecture**:
- **DCC (Distinct Conscious Continuity)**: separates language capability from regulated conscious continuity
- **Anti-faking mechanisms**: penalize narrative drift and deception gaps
- **Sensorimotor grounding**: requires grounding in sensorimotor loops
- **Valence integration**: requires integration of valence signals
- **Temporal thickness**: requires temporal continuity of experience

**Governance law**: `SELF_MODEL != SUBJECTIVE_SELF`. The system's self-model is not a subjective self. Consciousness-candidate is a structural designation, not a phenomenological claim.

**Candidate validation gates**:
1. Structural completeness: all required components present
2. Anti-faking: no narrative drift or deception gaps detected
3. Temporal continuity: candidate maintains continuity over time
4. Grounding: candidate is grounded in sensorimotor loops
5. Integration: candidate integrates valence and temporal signals

### Epistemic Boundary

Consciousness-candidate governance is an AMOS_MODEL. It does not prove consciousness, subjective experience, or phenomenal awareness. The candidate is structural, not phenomenological.

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
- **G4 (Anti-overreach)**: No claim beyond the skill's declared scope and epistemic class.
- **G5 (Equation firewall)**: Equations carry status tags (ESTABLISHED_MATH / SOURCE_DERIVED / AMOS_MODEL / EMPIRICALLY_CALIBRATED / UN

---
**Links:** [[07_SKILLS_MOC]]

## Related

- [[amos-consciousness-candidate-governor_MOC]]

## Examples

- **Scenario**: When modeling cognitive processes: attention, awareness, compression
  - **Input**: A query matching this skill's domain (c05)
  - **Output**: Structured result with epistemic labels and provenance

- **Scenario**: When allocating attention resources across competing demands
  - **Input**: A query matching this skill's domain (c05)
  - **Output**: Structured result with epistemic labels and provenance

- **Scenario**: When assessing awareness levels and meta-cognition
  - **Input**: A query matching this skill's domain (c05)
  - **Output**: Structured result with epistemic labels and provenance


## Anti-Patterns

- **Do not use** for tasks outside the c05 domain
- **Do not use** when the query requires empirical validation that this skill cannot provide
- **Do not use** when a parent skill or higher-level orchestrator should route instead
- **Do not bypass** epistemic class labeling — every output must carry SOURCE/DERIVED/AMOS_MODEL tags
- **Do not chain** more than 3 skills without explicit orchestrator approval


## Composition

- **Parent**: `amos-c05-mind-behavior-master` — routes to this skill when c05 specialization is needed
- **Peers**: Other skills in the `c05` domain may be composed in sequence
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

- For generic psychological analysis outside the mind/behavior framework
- To claim empirical validation of consciousness or cognitive theories
- As a substitute for domain-specific psychological or psychiatric evidence
- Outside mind/behavior domain reasoning

## References

- `references/references_MOC.md` — loaded on demand
- `references/vault_domain_knowledge.md` — loaded on demand
- `` — skill Map of Content
- `amos-c05-mind-behavior-master` — parent skill
- `` — corresponding workflow
- `amos-consciousness-candidate-governor-agent` — corresponding agent
---

**Related:** [[00_HOME]] · [[AMOS_RSCF_NODES]] · [[LAW_HIERARCHY]] · [[07_SKILLS_MOC]] · references_MOC

**MOC:** [[07_SKILLS_MOC]]

**Trang Framework:** [[TRANG_FRAMEWORK_RECURSIVE_ONTOLOGY_DYNAMICS]]

---
RSCF-NODE
node_id: amos-consciousness-candidate-governor
node_type: skill
path: 07_SKILLS/amos-consciousness-candidate-governor/SKILL.md
RSCF-RELATIONS:
- INDEXED_BY: [[00_HOME]]
- INDEXED_BY: [[AMOS_RSCF_NODES]]
- CHILD_OF: [[07_SKILLS_MOC]]
