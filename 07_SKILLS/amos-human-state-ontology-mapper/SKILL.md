---
title: SKILL
type: skill
name: amos-human-state-ontology-mapper
description: Human State Ontology Mapper — canon and universe capability. Use when canon reasoning, universe-level analysis, or invariant verification. Use when amos-canon-universe-master routes to this specialized capability.
parent_skill: amos-canon-universe-master
domain: canon
origin_architect: Trang Phan
epistemic_class: SOURCE_CLAIM
tags: [note, amos-human-state-ontology-mapper]
---


# Human State Ontology Mapper

## Identity

- **Origin architect and steward**: Trang Phan
- **Parent skill**: `amos-canon-universe-master`
- **Domain**: canon
- **Epistemic class**: SOURCE_CLAIM (vault-sourced from AMOS framework)

Canon and universe engine for Human State Ontology Mapper

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

- **human_state.compile_canon**: Compile canonical structure from sources into a consistent, navigable canon
- **human_state.check_consistency**: Check canon consistency: no contradictions, no gaps, no orphan references
- **human_state.enforce_invariant**: Enforce canon invariants: structural laws that must hold across all parts
- **human_state.navigate_canon**: Navigate canon: locate the canonical part for any topic or query
- **human_state.validate_substrate**: Validate canonical software substrate against canon requirements
- **human_state.manage_lifecycle**: Manage lifecycle: classify, validate, trace, assess, detect.
- **human_state.detect_drift**: Detect drift in evidence chains, provenance freshness, or confidence calibration.
- **human_state.validate_outputs**: Validate outputs against domain constraints and epistemic class.

> **Reference**: See `references/vault_domain_knowledge.md` (content_hash: caf6465c9fedb9cd) for the full vault-sourced domain knowledge (5861 chars).

## 11_KNOWLEDGE Vault Content

> **Source**: `_00_Cosmo brain/engine/H/Human_Interaction_Engine_Model.md` (content_hash: 7810e2f08c1532eb) (vault canon, SOURCE_CLAIM)
> **Additional source**: `11_KNOWLEDGE/AMOS_C04_BIO_NEURO_MASTER_KNOWLEDGE.md` (content_hash: 6fbde28c766c9d49) (vault canon, SOURCE_CLAIM)

### Human State Ontology Mapper

From Cosmo Brain Human Interaction Engine (HIE) Model: 7 internal state layers, threat/stability indices, strategy profiles. From C04 Bio & Neuro: UBI 4 domains for human state.

**HIE 7 state layers**: The 7 internal state layers dictate the agent's interaction posture, from base operational states to complex empathetic and advisory states.

**Threat & Stability indices**:
- Continuously calculates the stability of the human interlocutor based on linguistic markers
- Adjusts response density and complexity to prevent overwhelming a destabilized user

**8 Strategy Profiles (SP1-SP8)**:
- **SP1 (Direct/Execute)**: high speed, low empathy, action-oriented
- **SP5 (Advisory/Consultative)**: high nuance, balanced empathy, option-generating
- **SP8 (Containment/De-escalation)**: high empathy, low complexity, stabilizing tone

**10 Interaction Goals**: defines what the interaction is meant to achieve (Information Transfer, Consensus Building, Crisis Mitigation, etc.)

**UBI 4 domains for human state**:
- **NBI (Neurobiological)**: neural state, cognitive load, attention
- **NEI (Neuro-Emotional)**: emotional state, affect, mood
- **SI (Somatic)**: physical state, body signals, fatigue
- **BEI (Bio-Energetic)**: energy state, motivation, drive

**Mapping law**: `HUMAN_STATE != MACHINE_STATE`. Human state is complex, multi-domain, and context-dependent; it is not a simple machine state.

### Epistemic Boundary

Human state ontology mapping is an analytical model. It does not prove all human states are mapped, that the mapping is biologically accurate, or that the HIE captures all human factors.

## Failure Modes

- **Insufficient evidence**: If source material is insufficient, mark as UNKNOWN/GAP and fail closed — do not fabricate.
- **Scope violation**: If the query falls outside the skill's declared scope, escalate to the parent skill or steward.
- **Binding broken**: If 1:1:1 binding (skill→agent→workflow) is broken, flag routing mismatch and block execution.
- **Validation failure**: If validation gates fail, downgrade confidence, flag the gap, and escalate — do not force-fit.
- **Epistemic overreach**: If a claim exceeds the established evidence or epistemic class, retract and relabel.

## Validation Gates

- **G1 (Law of Law)**: No unresolved contradictions within the skill's

---
**Links:** [[07_SKILLS_MOC]]
