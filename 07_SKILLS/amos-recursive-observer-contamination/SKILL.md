---
title: SKILL
type: skill
name: amos-recursive-observer-contamination
description: Recursive Observer Contamination — runtime and OS capability. Use when runtime reasoning, OS kernel operations, or adaptive stability. Use when amos-os-runtime-master routes to this specialized capability.
parent_skill: amos-os-runtime-master
domain: runtime
origin_architect: Trang Phan
epistemic_class: SOURCE_CLAIM
tags: [note, amos-recursive-observer-contamination]
---


# Recursive Observer Contamination

## Identity

- **Origin architect and steward**: Trang Phan
- **Parent skill**: `amos-os-runtime-master`
- **Domain**: runtime
- **Epistemic class**: SOURCE_CLAIM (vault-sourced from AMOS framework)

Runtime and OS engine for Recursive Observer Contamination

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

- **recursive_observer.monitor_stability**: Monitor runtime stability: drift, oscillation, divergence, and regime transitions
- **recursive_observer.calibrate_feedback**: Calibrate feedback control loops to maintain stable operating conditions
- **recursive_observer.decompose_primitive**: Decompose complex operations into primitive, atomic, verifiable steps
- **recursive_observer.align_drift**: Align AI drift back to authorized operating envelope when deviation is detected
- **recursive_observer.enforce_closed_loop**: Enforce closed-loop learning: every output feeds back into the next iteration
- **recursive_observer.manage_lifecycle**: Manage lifecycle: classify, validate, trace, assess, detect.
- **recursive_observer.detect_drift**: Detect drift in evidence chains, provenance freshness, or confidence calibration.
- **recursive_observer.validate_outputs**: Validate outputs against domain constraints and epistemic class.

> **Reference**: See `references/vault_domain_knowledge.md` (content_hash: f62c9ba2a91fa4ab) for the full vault-sourced domain knowledge (7634 chars).

## 11_KNOWLEDGE Vault Content

> **Source**: `11_KNOWLEDGE/AMOS_COGNITIVE_ORGANISM_OS_DETAIL.md` (content_hash: 61279c4b00128110) (vault canon, SOURCE_CLAIM)

### Recursive Observer Contamination

The Cognitive Organism OS defines recursive observer contamination as the distortion that occurs when the observer is part of the system being observed.

**Contamination types**:
- **Self-observation contamination**: observing oneself changes the observed state
- **Feedback contamination**: observation results feed back into the system, changing it
- **Measurement contamination**: the act of measurement changes the measured system
- **Recursive depth contamination**: each level of recursion adds distortion

**Contamination law**: `OBSERVER != EXTERNAL`. The observer is not external to the system; observation is participation.

**Mitigation protocols**:
1. **Declare observer position**: explicitly declare the observer's relationship to the system
2. **Separate observation from participation**: where possible, separate the observation channel from the participation channel
3. **Track contamination**: track the level of contamination at each recursion level
4. **Compensate**: apply compensation for known contamination effects
5. **Limit recursion depth**: limit the depth of recursive observation to control contamination

### Epistemic Boundary

Recursive observer contamination is an epistemic construct. It does not prove all contamination is detectable, that compensation is always effective, or that observation can be fully separated from participation.

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
- **G4 (Anti-overreach)**: No claim beyond the skill's declared scope and

---
**Links:** [[07_SKILLS_MOC]]
