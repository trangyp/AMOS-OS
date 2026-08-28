---
title: SKILL — Amos Artistic Expression Governor
type: skill
source: 07_SKILLS/amos-artistic-expression-governor
name: amos-artistic-expression-governor
description: Artistic Expression Governor — mind and behavior capability. Use when
  psychological analysis, behavioral reasoning, or cognitive modeling. Use when amos-c05-mind-behavior-master
  routes to this specialized capability.
parent_skill: amos-c05-mind-behavior-master
domain: c05
origin_architect: Trang Phan
epistemic_class: SOURCE_CLAIM
tags:
- type/skill
- canon/skill
- domain/mind-behavior
- canon-group/human-system
- topic/cognition
- capability/governance
- rscf/epistemic
- rscf/C-constraint
- rscf/G-relation
- rscf/M-memory
- rscf/S-state
- rscf/type-model
- sota/progressive-disclosure
- sota/anti-patterns
- amos_os
- amos-artistic-expression-governor
rscf:
  state: DERIVED
  claim_class: DERIVED
  provenance: AMOS_corpus
  scope: AMOS_general
version: 1.1.0
---






# Artistic Expression Governor

## Identity

- **Origin architect and steward**: Trang Phan
- **Parent skill**: `amos-c05-mind-behavior-master`
- **Domain**: c05
- **Epistemic class**: SOURCE_CLAIM (vault-sourced from AMOS framework)

Mind-behavior engine for Artistic Expression Governor

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

- **artistic_expression.model_cognition**: Model cognitive processes: attention, awareness, compression, and inference
- **artistic_expression.allocate_attention**: Allocate attention resources across competing demands and priorities
- **artistic_expression.assess_awareness**: Assess awareness levels: meta-cognition, self-monitoring, and calibration
- **artistic_expression.govern_expression**: Govern artistic and emotional expression within healthy bounds
- **artistic_expression.manage_lifecycle**: Manage lifecycle: classify, validate, trace, assess, detect.
- **artistic_expression.detect_drift**: Detect drift in evidence chains, provenance freshness, or confidence calibration.
- **artistic_expression.validate_outputs**: Validate outputs against domain constraints and epistemic class.

> **Reference**: See `references/vault_domain_knowledge.md` (content_hash: 287062260da3bd87) for the full vault-sourced domain knowledge (6676 chars).

## 11_KNOWLEDGE Vault Content

> **Source**: `11_KNOWLEDGE/AMOS_COGNITIVE_ORGANISM_OS_DETAIL.md` (content_hash: 61279c4b00128110) (vault canon, SOURCE_CLAIM)

### Artistic Expression Governance

The Cognitive Organism OS defines artistic expression as a creative output mode governed by aesthetic, emotional, and cultural constraints.

**Expression modes**:
- **Visual**: images, diagrams, design -- governed by visual coherence and aesthetic principles
- **Textual**: prose, poetry, narrative -- governed by linguistic coherence and emotional resonance
- **Musical**: composition, rhythm, harmony -- governed by musical structure and emotional progression
- **Multimodal**: combinations of above -- governed by cross-modal coherence

**Governance laws**:
- `ART != SCIENCE`: artistic expression does not follow scientific method; it follows aesthetic principles
- `EXPRESSION != CLAIM`: artistic expression is not a factual claim; it is a creative output
- `AESTHETIC != EPISTEMIC`: aesthetic quality is not epistemic quality

**Governance protocol**:
1. **Classify**: classify the expression mode and its constraints
2. **Generate**: generate the artistic output within constraints
3. **Validate**: validate aesthetic coherence and emotional resonance
4. **Label**: label the output as AMOS_MODEL (creative, not factual)
5. **Record**: record provenance and constraints

### Epistemic Boundary

Artistic expression governance is a creative construct. It does not prove aesthetic universality, that artistic quality is objective, or that expression follows deterministic rules.

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
- **G5 (Equation firewall)**: Equations carry status tags (ESTABLISHED_MATH / SOURCE_DERIVED / AMOS_MOD

---
**Links:** [[07_SKILLS_MOC]]

## Related

- [[amos-artistic-expression-governor_MOC]]

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


## References

- `references/references_MOC.md` — loaded on demand
- `references/vault_domain_knowledge.md` — loaded on demand
- `[[amos-artistic-expression-governor_MOC]]` — skill Map of Content
- `amos-c05-mind-behavior-master` — parent skill
- `[[amos-artistic-expression-governor-workflow]]` — corresponding workflow
- `amos-artistic-expression-governor-agent` — corresponding agent
---

**Related:** [[00_HOME]] · [[AMOS_RSCF_NODES]] · [[LAW_HIERARCHY]] · [[07_SKILLS_MOC]] · [[references_MOC]]

**MOC:** [[07_SKILLS_MOC]]

**Trang Framework:** [[TRANG_FRAMEWORK_RECURSIVE_ONTOLOGY_DYNAMICS]]

---
RSCF-NODE
node_id: amos-artistic-expression-governor
node_type: skill
path: 07_SKILLS/amos-artistic-expression-governor/SKILL.md
RSCF-RELATIONS:
- INDEXED_BY: [[00_HOME]]
- INDEXED_BY: [[AMOS_RSCF_NODES]]
- CHILD_OF: [[07_SKILLS_MOC]]
