---
title: SKILL
type: skill
name: amos-observability-driven-harness-evolution-rscf
description: Observability Driven Harness Evolution — technology and engineering capability. Use when software development, engineering design, or technical architecture. Use when amos-c10-tech-engineering-master routes to this specialized capability.
parent_skill: amos-c10-tech-engineering-master
domain: c10
origin_architect: Trang Phan
epistemic_class: SOURCE_CLAIM
tags: [note, amos-observability-driven-harness-evolution-rscf]
---


# Observability Driven Harness Evolution Rscf

## Identity

- **Origin architect and steward**: Trang Phan
- **Parent skill**: `amos-c10-tech-engineering-master`
- **Domain**: c10
- **Epistemic class**: SOURCE_CLAIM (vault-sourced from AMOS framework)

Tech-engineering engine for Observability Driven Harness Evolution Rscf

## When to Use

- When analyzing software architecture: patterns, dependencies, coupling
- When discovering program behavior via black-box analysis or symbolic execution
- When verifying code facts: type safety, memory safety, termination
- When enforcing bounded code: resource, time, and capability limits
- When the parent skill (`amos-c10-tech-engineering-master`) routes to this specialized capability
- When managing lifecycle operations across classify, validate, trace, assess, and detect
- When detecting drift in evidence chains, provenance freshness, or confidence calibration
- When validating outputs against domain constraints and epistemic class

## Capabilities

- **observability_driven.analyze_architecture**: Analyze software architecture: patterns, dependencies, coupling, cohesion
- **observability_driven.discover_program**: Discover program behavior: black-box analysis, symbolic execution, fuzzing
- **observability_driven.verify_code_facts**: Verify code facts: type safety, memory safety, termination, complexity
- **observability_driven.optimize_performance**: Optimize performance: profiling, bottleneck analysis, and resource tuning
- **observability_driven.enforce_bounds**: Enforce bounded code: resource limits, time limits, and capability limits

> **Reference**: See `references/vault_domain_knowledge.md` (content_hash: 9a7bb863c0df9b77) for the full vault-sourced domain knowledge (9536 chars).
- **observability_driven.manage_lifecycle**: Manage lifecycle: classify, validate, trace, assess, detect.
- **observability_driven.detect_drift**: Detect drift in evidence chains, provenance freshness, or confidence calibration.
- **observability_driven.validate_outputs**: Validate outputs against domain constraints and epistemic class.

## 11_KNOWLEDGE Vault Content

> **Source**: `11_KNOWLEDGE/AMOS_COGNITIVE_ORGANISM_OS_DETAIL.md` (content_hash: 61279c4b00128110) (vault canon, SOURCE_CLAIM)

### RSCF Epistemic Substrate

This RSCF engine operates on the AMOS RSCF (Reasoning, Scope, Claim, Falsifier) epistemic substrate.

**RSCF objects**: claim / class / premises / evidence / provenance / scope / regime / freshness / dependencies / competing hypotheses / falsifiers / confidence ceiling.

**RSCF state kinds**: OBSERVATION, SOURCE_CLAIM, DERIVED, MODEL, DECISION, UNKNOWN.

**RSCF laws**:
- `CLAIM != FACT`: a claim is not a fact; it must be labeled with epistemic class
- `CONFIDENCE <= EVIDENCE`: confidence cannot exceed evidence support
- `FALSIFIER_REQUIRED`: every claim must declare its falsifier
- `SCOPE_BOUND`: every claim is valid only within its declared scope and regime
- `PROVENANCE_REQUIRED`: every claim must have traceable provenance

**RSCF validation gates**:
- G1 (Law of Law): no unresolved contradictions
- G2 (Epistemic class): all claims labeled, no class promotion without evidence
- G3 (Provenance): source path recorded for every derived claim
- G4 (Anti-overreach): no claim beyond declared scope
- G5 (Equation firewall): equations carry status tags
- G6 (Failure mode): on failure, downgrade, flag, escalate

### Epistemic Boundary

This RSCF engine is an epistemic governance tool. It does not prove claims are true, that all falsifiers are known, or that the RSCF framework is complete.

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
- *

---
**Links:** [[07_SKILLS_MOC]]
