---
title: SKILL
type: skill
name: cosmo-human-problem-architecture
description: Cosmo Human Problem Architecture — runtime and OS capability. Use when runtime reasoning, OS kernel operations, or adaptive stability. Use when amos-os-runtime-master routes to this specialized capability.
parent_skill: amos-os-runtime-master
domain: runtime
origin_architect: Trang Phan
epistemic_class: SOURCE_CLAIM
tags: [note, cosmo-human-problem-architecture]
---


# Cosmo Human Problem Architecture

## Identity

- **Origin architect and steward**: Trang Phan
- **Parent skill**: `amos-os-runtime-master`
- **Domain**: runtime
- **Epistemic class**: SOURCE_CLAIM (vault-sourced from AMOS framework)

Runtime and OS engine for Cosmo Human Problem Architecture

## When to Use

- When monitoring runtime stability: drift, oscillation, divergence
- When calibrating feedback control loops for stable operation
- When decomposing complex operations into primitive steps
- When enforcing closed-loop learning and drift alignment
- When the parent skill (`amos-os-runtime-master`) routes to this specialized capability
- When managing lifecycle operations across classify, validate, trace, assess, and detect
- When detecting drift in evidence chains, provenance freshness, or confidence calibration
- When validating outputs against domain constraints and epistemic class

## Capabilities

- **cosmo_human.monitor_stability**: Monitor runtime stability: drift, oscillation, divergence, and regime transitions
- **cosmo_human.calibrate_feedback**: Calibrate feedback control loops to maintain stable operating conditions
- **cosmo_human.decompose_primitive**: Decompose complex operations into primitive, atomic, verifiable steps
- **cosmo_human.align_drift**: Align AI drift back to authorized operating envelope when deviation is detected
- **cosmo_human.enforce_closed_loop**: Enforce closed-loop learning: every output feeds back into the next iteration

> **Reference**: See `references/vault_domain_knowledge.md` (content_hash: 7d7937903a4bdea7) for the full vault-sourced domain knowledge (9579 chars).
- **cosmo_human.manage_lifecycle**: Manage lifecycle: classify, validate, trace, assess, detect.
- **cosmo_human.detect_drift**: Detect drift in evidence chains, provenance freshness, or confidence calibration.
- **cosmo_human.validate_outputs**: Validate outputs against domain constraints and epistemic class.

## 11_KNOWLEDGE Vault Content

> **Source**: `11_KNOWLEDGE/AMOS_C05_MIND_BEHAVIOR_MASTER_KNOWLEDGE.md` (content_hash: e3ca4951a743518b) (vault canon, SOURCE_CLAIM)

### Cosmo Human Problem Architecture

From C05 Mind & Behavior: Human problem architecture and cognitive modeling.

**Human problem architecture**:
- **Problem framing**: how a problem is framed determines the solution space
- **Cognitive biases**: systematic deviations from rational judgment
- **Emotional influences**: emotions affect problem perception and decision-making
- **Social context**: social dynamics affect problem definition and resolution
- **Cultural context**: cultural patterns affect problem interpretation

**Problem architecture model**:
1. **Identify**: identify the problem as perceived by the human
2. **Frame**: analyze how the problem is framed
3. **Contextualize**: place the problem in its cognitive, emotional, social, cultural context
4. **Decompose**: decompose the problem into sub-problems
5. **Reframe**: consider alternative framings
6. **Solve**: solve within the most productive framing

**Law**: `PROBLEM != OBJECTIVE`. A problem is a perceived gap; an objective is a desired state. Problems are subjective; objectives are declarative.

### Epistemic Boundary

Cosmo human problem architecture is an analytical model. It does not prove problems are always solvable, that reframing always helps, or that the architecture captures all human factors.

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
- **G6 (Failure mode

---
**Links:** [[07_SKILLS_MOC]]
