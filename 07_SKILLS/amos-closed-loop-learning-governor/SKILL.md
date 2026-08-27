---
title: SKILL
type: skill
name: amos-closed-loop-learning-governor
description: Closed Loop Learning Governor — runtime and OS capability. Use when runtime reasoning, OS kernel operations, or adaptive stability. Use when amos-os-runtime-master routes to this specialized capability.
parent_skill: amos-os-runtime-master
domain: runtime
origin_architect: Trang Phan
epistemic_class: SOURCE_CLAIM
tags: [note, amos-closed-loop-learning-governor]
---


# Closed Loop Learning Governor

## Identity

- **Origin architect and steward**: Trang Phan
- **Parent skill**: `amos-os-runtime-master`
- **Domain**: runtime
- **Epistemic class**: SOURCE_CLAIM (vault-sourced from AMOS framework)

Runtime and OS engine for Closed Loop Learning Governor

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

- **closed_loop.monitor_stability**: Monitor runtime stability: drift, oscillation, divergence, and regime transitions
- **closed_loop.calibrate_feedback**: Calibrate feedback control loops to maintain stable operating conditions
- **closed_loop.decompose_primitive**: Decompose complex operations into primitive, atomic, verifiable steps
- **closed_loop.align_drift**: Align AI drift back to authorized operating envelope when deviation is detected
- **closed_loop.enforce_closed_loop**: Enforce closed-loop learning: every output feeds back into the next iteration

> **Reference**: See `references/vault_domain_knowledge.md` (content_hash: 43d76b1897997c62) for the full vault-sourced domain knowledge (9437 chars).
- **closed_loop.manage_lifecycle**: Manage lifecycle: classify, validate, trace, assess, detect.
- **closed_loop.detect_drift**: Detect drift in evidence chains, provenance freshness, or confidence calibration.
- **closed_loop.validate_outputs**: Validate outputs against domain constraints and epistemic class.

## 11_KNOWLEDGE Vault Content

> **Source**: `11_KNOWLEDGE/AMOS_C05_MIND_BEHAVIOR_MASTER_KNOWLEDGE.md` (content_hash: e3ca4951a743518b) (vault canon, SOURCE_CLAIM)
> **Additional source**: `11_KNOWLEDGE/AMOS_COGNITIVE_ORGANISM_OS_DETAIL.md` (content_hash: 61279c4b00128110) (vault canon, SOURCE_CLAIM)

### Closed-Loop Learning Governor

From C05 Mind & Behavior: Closed-loop learning with feedback. From Cognitive Organism OS: Self-audit gate and repair cycle.

**Closed-loop learning model**:
- **Observe**: observe the outcome of an action
- **Evaluate**: evaluate the outcome against expectations
- **Learn**: learn from the discrepancy (if any)
- **Adjust**: adjust the model based on learning
- **Re-execute**: re-execute with the adjusted model
- **Audit**: audit the learning loop for correctness

**Closed-loop laws**:
- `LEARNING != IMPROVEMENT`: learning changes the model; improvement requires validation that the change is better
- `FEEDBACK != TRUTH**: feedback is an observation; it is not truth
- `CLOSED_LOOP != CONVERGENCE**: a closed loop ensures feedback; it does not guarantee convergence

**Governor responsibilities**:
- **Loop integrity**: ensure the learning loop is closed (no missing feedback)
- **Loop speed**: ensure the loop runs fast enough to be useful
- **Loop safety**: ensure the loop does not cause runaway adaptation
- **Loop audit**: ensure the loop is auditable (every iteration recorded)

**Self-audit gate**: every runtime cycle passes through self-audit before finalization. The self-audit checks that the learning loop is functioning correctly.

**Repair cycle**: if the learning loop is broken (missing feedback, runaway adaptation), the repair cycle activates to fix the loop.

### Epistemic Boundary

Closed-loop learning governance is an operational construct. It does not prove learning always converges, that the loop is always closed, or that adaptation is always beneficial.

## Failure Modes

- **Insufficient evidence**: If source material is insufficient, mark as UNKNOWN/GAP and fail closed — do not fabricate.
- **Scope violation**: If the query falls outside the skill's declared scope, escalate to the parent skill or steward.
- **Binding broken**: If 1:1:1 binding (skill→agent→workflow) is broken, flag routing mismatch and block execution.
- **Validation failure**: If validation gates fail, downgrade confidence, flag the gap, and escalate — do not force-fit.
- **Epistemic overreach**: If a claim exceeds the established evidence or epistemic class, retract and relabel.

## Validation Gates

- **G1 (Law of Law)**: No unresolved contradictions with

---
**Links:** [[07_SKILLS_MOC]]
