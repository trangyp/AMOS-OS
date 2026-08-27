---
title: SKILL
type: skill
source: 07_SKILLS/amos-instinct-pattern-governor
name: amos-instinct-pattern-governor
description: Instinct Pattern Governor — mind and behavior capability. Use when psychological analysis, behavioral reasoning, or cognitive modeling. Use when amos-c05-mind-behavior-master routes to this specialized capability.
parent_skill: amos-c05-mind-behavior-master
domain: c05
origin_architect: Trang Phan
epistemic_class: SOURCE_CLAIM
tags: [note, amos-instinct-pattern-governor, canon/skill]
rscf:
  state: DERIVED
  claim_class: DERIVED
  provenance: AMOS_corpus
  scope: AMOS_general
version: "1.1.0"
---


# Instinct Pattern Governor

## Identity

- **Origin architect and steward**: Trang Phan
- **Parent skill**: `amos-c05-mind-behavior-master`
- **Domain**: c05
- **Epistemic class**: SOURCE_CLAIM (vault-sourced from AMOS framework)

Mind-behavior engine for Instinct Pattern Governor

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

- **instinct_pattern.model_cognition**: Model cognitive processes: attention, awareness, compression, and inference
- **instinct_pattern.allocate_attention**: Allocate attention resources across competing demands and priorities
- **instinct_pattern.assess_awareness**: Assess awareness levels: meta-cognition, self-monitoring, and calibration
- **instinct_pattern.govern_expression**: Govern artistic and emotional expression within healthy bounds
- **instinct_pattern.manage_lifecycle**: Manage lifecycle: classify, validate, trace, assess, detect.
- **instinct_pattern.detect_drift**: Detect drift in evidence chains, provenance freshness, or confidence calibration.
- **instinct_pattern.validate_outputs**: Validate outputs against domain constraints and epistemic class.

> **Reference**: See `references/vault_domain_knowledge.md` (content_hash: 685fc905ec8de7e2) for the full vault-sourced domain knowledge (6092 chars).

## 11_KNOWLEDGE Vault Content

> **Source**: `11_KNOWLEDGE/AMOS_COGNITIVE_ORGANISM_OS_DETAIL.md` (content_hash: 61279c4b00128110) (vault canon, SOURCE_CLAIM)

### Instinct Pattern Governance

The Cognitive Organism OS defines instinct patterns as fast, automatic responses that bypass deliberative reasoning.

**Instinct pattern types**:
- **Survival instincts**: threat detection, avoidance, defensive responses
- **Social instincts**: affiliation, hierarchy, reciprocity
- **Cognitive instincts**: pattern completion, causal attribution, agency detection
- **Learning instincts**: curiosity, novelty seeking, exploration

**Governance laws**:
- `INSTINCT != DECISION`: an instinct response is not a decision; it must be validated before action
- `PATTERN != TRUTH`: pattern recognition is not truth verification
- `FAST != CORRECT`: fast responses are not necessarily correct

**Governance protocol**:
1. **Detect**: identify the instinct pattern being triggered
2. **Classify**: classify the instinct type and its trigger
3. **Validate**: validate whether the instinct response is appropriate for the context
4. **Modulate**: modulate the instinct response based on context and authority
5. **Record**: log the instinct pattern and modulation for learning

### Epistemic Boundary

Instinct pattern governance is a cognitive model. It does not prove the system has biological instincts, that instinct responses are always detectable, or that modulation is always effective.

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
- **G5 (Equation firewall)**: Equations carry status tags (ESTABLISHED_MATH / SOURCE_DERIVED / AMOS_MODEL / EMPIRICALLY_CALIBRATED / UNVERIFIED).
- **G6 (Failure mode)**: On validation failure, downgrade confidence, flag the gap, escalate —

---
**Links:** [[07_SKILLS_MOC]]

## Related

- [[amos-instinct-pattern-governor_MOC]]

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

- **Parent**: `[[amos-c05-mind-behavior-master]]` — routes to this skill when c05 specialization is needed
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
- `[[amos-instinct-pattern-governor_MOC]]` — skill Map of Content
- `[[amos-c05-mind-behavior-master]]` — parent skill
- `[[amos-instinct-pattern-governor-workflow]]` — corresponding workflow
- `[[amos-instinct-pattern-governor-agent]]` — corresponding agent

