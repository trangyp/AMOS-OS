---
title: SKILL
type: skill
name: amos-instinct-pattern-governor
description: Instinct Pattern Governor — mind and behavior capability. Use when psychological analysis, behavioral reasoning, or cognitive modeling. Use when amos-c05-mind-behavior-master routes to this specialized capability.
parent_skill: amos-c05-mind-behavior-master
domain: c05
origin_architect: Trang Phan
epistemic_class: SOURCE_CLAIM
tags: [note, amos-instinct-pattern-governor]
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