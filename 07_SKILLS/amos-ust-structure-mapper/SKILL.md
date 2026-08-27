---
title: SKILL
type: skill
name: amos-ust-structure-mapper
description: Ust Structure Mapper — runtime and OS capability. Use when runtime reasoning, OS kernel operations, or adaptive stability. Use when amos-os-runtime-master routes to this specialized capability.
parent_skill: amos-os-runtime-master
domain: runtime
origin_architect: Trang Phan
epistemic_class: SOURCE_CLAIM
tags: [note, amos-ust-structure-mapper]
---


# Ust Structure Mapper

## Identity

- **Origin architect and steward**: Trang Phan
- **Parent skill**: `amos-os-runtime-master`
- **Domain**: runtime
- **Epistemic class**: SOURCE_CLAIM (vault-sourced from AMOS framework)

Runtime and OS engine for Ust Structure Mapper

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

- **ust_structure.monitor_stability**: Monitor runtime stability: drift, oscillation, divergence, and regime transitions
- **ust_structure.calibrate_feedback**: Calibrate feedback control loops to maintain stable operating conditions
- **ust_structure.decompose_primitive**: Decompose complex operations into primitive, atomic, verifiable steps
- **ust_structure.align_drift**: Align AI drift back to authorized operating envelope when deviation is detected
- **ust_structure.enforce_closed_loop**: Enforce closed-loop learning: every output feeds back into the next iteration
- **ust_structure.manage_lifecycle**: Manage lifecycle: classify, validate, trace, assess, detect.
- **ust_structure.detect_drift**: Detect drift in evidence chains, provenance freshness, or confidence calibration.
- **ust_structure.validate_outputs**: Validate outputs against domain constraints and epistemic class.

> **Reference**: See `references/vault_domain_knowledge.md` (content_hash: 5845760e81d7bada) for the full vault-sourced domain knowledge (7866 chars).

## 11_KNOWLEDGE Vault Content

> **Source**: `11_KNOWLEDGE/AMOS_COGNITIVE_ORGANISM_OS_DETAIL.md` (content_hash: 61279c4b00128110) (vault canon, SOURCE_CLAIM)

### UST (Universe Structure) Mapper

From Cognitive Organism OS: Universe structure mapping through the 7-part canon.

**7-part universe canon mapping**:
- **Constraint**: capacity, authority, identity boundaries
- **Flow**: events, memory, evidence, action
- **Structure**: organ topology and interfaces
- **Enforcement**: policy and authority gates
- **Time**: lifecycle, freshness, fatigue
- **Adaptation**: learning and repair
- **Termination**: shutdown, collapse, recovery

**UST mapping protocol**:
1. **Identify the system**: what system is being mapped?
2. **Apply 7-part canon**: map the system to each of the 7 parts
3. **Check completeness**: are all 7 parts represented?
4. **Check consistency**: are the parts internally consistent?
5. **Record**: record the UST mapping with provenance

**Law**: `MAPPING != REALITY`. A UST mapping is a structural description, not a reality claim. The 7-part canon is an analytical framework, not a physical theory.

### Epistemic Boundary

UST structure mapping is an analytical framework. It does not prove the 7-part canon is universal, that all systems can be mapped, or that the mapping captures all structural properties.

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
- **G6 (Failure mode)**: On validation failure, downgrade confidence, flag the gap, escalate — do not force-fit.

## Provenance

- **Skill**: `amos-ust-structure-mapper`
-

---
**Links:** [[07_SKILLS_MOC]]
