---
title: SKILL
type: skill
name: amos-target-of-repair-intelligence
description: Target Of Repair Intelligence — audit and repair capability. Use when auditing, failure analysis, gap discovery, or repair allocation. Use when amos-audit-repair-master routes to this specialized capability.
parent_skill: amos-audit-repair-master
domain: audit
origin_architect: Trang Phan
epistemic_class: SOURCE_CLAIM
tags: [note, amos-target-of-repair-intelligence]
---


# Target Of Repair Intelligence

## Identity

- **Origin architect and steward**: Trang Phan
- **Parent skill**: `amos-audit-repair-master`
- **Domain**: audit
- **Epistemic class**: SOURCE_CLAIM (vault-sourced from AMOS framework)

Audit and verification engine for Target Of Repair Intelligence

## When to Use

- When auditing claims against evidence and provenance
- When detecting gaps in capabilities, evidence, tests, or monitors
- When allocating repair resources to highest-leverage gaps
- When verifying gap closure across the full lifecycle chain
- When the parent skill (`amos-audit-repair-master`) routes to this specialized capability
- When managing lifecycle operations across classify, validate, trace, assess, and detect
- When detecting drift in evidence chains, provenance freshness, or confidence calibration
- When validating outputs against domain constraints and epistemic class

## Capabilities

- **target_of.audit_claim**: Audit claims against evidence, provenance, and epistemic class
- **target_of.detect_gap**: Detect gaps: missing capabilities, missing evidence, missing tests, missing monitors
- **target_of.allocate_repair**: Allocate repair resources to highest-leverage gaps and failure modes
- **target_of.verify_closure**: Verify gap closure: requirement → capability → component → test → evidence
- **target_of.benchmark_forensics**: Benchmark forensic analysis: trace performance regressions to root causes

> **Reference**: See `references/vault_domain_knowledge.md` (content_hash: e390ceb1dc8f0a41) for the full vault-sourced domain knowledge (9031 chars).
- **target_of.manage_lifecycle**: Manage lifecycle: classify, validate, trace, assess, detect.
- **target_of.detect_drift**: Detect drift in evidence chains, provenance freshness, or confidence calibration.
- **target_of.validate_outputs**: Validate outputs against domain constraints and epistemic class.

## 11_KNOWLEDGE Vault Content

> **Source**: `11_KNOWLEDGE/AMOS_COGNITIVE_ORGANISM_OS_DETAIL.md` (content_hash: 61279c4b00128110) (vault canon, SOURCE_CLAIM)

### Target-of-Repair Intelligence

The Cognitive Organism OS defines target-of-repair intelligence for identifying what needs to be repaired and why.

**Target identification**:
1. **Detect failure**: identify the failure symptom
2. **Trace cause**: trace the failure to its root cause
3. **Identify target**: identify the specific component that needs repair
4. **Classify repair**: classify the repair type (patch, replace, refactor, rebuild)
5. **Estimate impact**: estimate the impact of the repair on the system

**Target types**:
- **Capability target**: a capability that is not functioning correctly
- **Binding target**: a 1:1:1 binding that is broken
- **Provenance target**: a provenance chain that is broken
- **Consistency target**: a contradiction that needs resolution
- **Drift target**: a component that has drifted from its declaration

**Law**: `SYMPTOM != CAUSE`. Repairing the symptom does not repair the cause. Target-of-repair intelligence traces symptoms to causes.

### Epistemic Boundary

Target-of-repair intelligence is a diagnostic construct. It does not prove all failures are traceable, that root causes are always identifiable, or that repair always fixes the issue.

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

- **Skill**: `amos-target-of

---
**Links:** [[07_SKILLS_MOC]]
