---
title: SKILL
type: skill
name: amos-cognitive-process-orchestrator
description: Cognitive Process Orchestrator — mind and behavior capability. Use when psychological analysis, behavioral reasoning, or cognitive modeling. Use when amos-c05-mind-behavior-master routes to this specialized capability.
parent_skill: amos-c05-mind-behavior-master
domain: c05
origin_architect: Trang Phan
epistemic_class: SOURCE_CLAIM
tags: [note, amos-cognitive-process-orchestrator]
---


# Cognitive Process Orchestrator

## Identity

- **Origin architect and steward**: Trang Phan
- **Parent skill**: `amos-c05-mind-behavior-master`
- **Domain**: c05
- **Epistemic class**: SOURCE_CLAIM (vault-sourced from AMOS framework)

Mind-behavior engine for Cognitive Process Orchestrator

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

- **cognitive_process.model_cognition**: Model cognitive processes: attention, awareness, compression, and inference
- **cognitive_process.allocate_attention**: Allocate attention resources across competing demands and priorities
- **cognitive_process.assess_awareness**: Assess awareness levels: meta-cognition, self-monitoring, and calibration
- **cognitive_process.govern_expression**: Govern artistic and emotional expression within healthy bounds
- **cognitive_process.manage_lifecycle**: Manage lifecycle: classify, validate, trace, assess, detect.
- **cognitive_process.detect_drift**: Detect drift in evidence chains, provenance freshness, or confidence calibration.
- **cognitive_process.validate_outputs**: Validate outputs against domain constraints and epistemic class.

> **Reference**: See `references/vault_domain_knowledge.md` (content_hash: 17b6beae69565d78) for the full vault-sourced domain knowledge (7950 chars).

## 11_KNOWLEDGE Vault Content

> **Source**: `11_KNOWLEDGE/AMOS_COGNITIVE_ORGANISM_OS_DETAIL.md` (content_hash: 61279c4b00128110) (vault canon, SOURCE_CLAIM)
> **Additional source**: `11_KNOWLEDGE/AMOS_C05_MIND_BEHAVIOR_MASTER_KNOWLEDGE.md` (content_hash: e3ca4951a743518b) (vault canon, SOURCE_CLAIM)

### Cognitive Process Orchestrator

From Cognitive Organism OS: 10-step runtime pipeline for cognitive process orchestration.

**10-step runtime pipeline**:
```
Perceive -> Route -> Admit -> Plan -> Schedule -> Execute -> Observe -> Repair -> Audit -> Finalize
```

**Orchestration principles**:
- Each step has declared inputs, outputs, and validation gates
- Steps are ordered; skipping steps requires explicit justification
- Repair can insert re-execution of earlier steps
- Audit checks all steps before finalization
- Finalization commits the result with provenance

**8 independent axes** for orchestration:
1. Cognitive organization
2. Capability granularity
3. Cognitive mode (EXPLORE/DIAGNOSE/DESIGN/AUDIT/MEASURE)
4. Scale (H/M/L)
5. Epistemic state (OBSERVATION/SOURCE_CLAIM/DERIVED/MODEL/DECISION/UNKNOWN)
6. Execution
7. Governance
8. Deployment

**5 Cognitive modes**:
- **EXPLORE**: discover and map the problem space
- **DIAGNOSE**: identify the root cause of a problem
- **DESIGN**: create a solution for a diagnosed problem
- **AUDIT**: verify that a solution meets its declared properties
- **MEASURE**: quantify the properties of a system or solution

**Orchestration laws**:
- `ORCHESTRATION != EXECUTION**: orchestration coordinates; execution does the work
- `STEP != CAPABILITY**: a step invokes a capability; it is not the capability
- `PIPELINE != WATERFALL**: the pipeline has feedback (repair -> re-execute); it is not a strict waterfall

### Epistemic Boundary

Cognitive process orchestration is a runtime architecture. It does not prove cognitive completeness, optimality, or that all cognitive processes can be decomposed into this pipeline.

## Failure Modes
- **Insufficient evidence**: If source material is insufficient, mark as UNKNOWN/GAP and fail closed — do not fabricate.
- **Scope violation**: If the query falls outside the skill's declared scope, escalate to the parent skill or steward.
- **Binding broken**: If 1:1:1 binding (skill→agent→workflow) is broken, flag routing mismatch and block execution.
- **Validation failure**: If validation gates fail, downgrade confidence, flag the gap, and escalate — do not force-fit.
- **Epistemic overreach**: If a claim exceeds the established evidence or epistemic class, retract and relabel.

## Validation Gates

- **G1 (Law of Law)**: No unresolved contradictions within the ski