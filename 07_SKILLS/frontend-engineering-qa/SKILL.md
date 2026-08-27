---
title: SKILL
type: skill
name: frontend-engineering-qa
description: Frontend Engineering Qa — technology and engineering capability. Use when software development, engineering design, or technical architecture. Use when amos-c10-tech-engineering-master routes to this specialized capability.
parent_skill: amos-c10-tech-engineering-master
domain: c10
origin_architect: Trang Phan
epistemic_class: SOURCE_CLAIM
tags: [note, frontend-engineering-qa]
---


# Frontend Engineering Qa

## Identity

- **Origin architect and steward**: Trang Phan
- **Parent skill**: `amos-c10-tech-engineering-master`
- **Domain**: c10
- **Epistemic class**: SOURCE_CLAIM (vault-sourced from AMOS framework)

Tech-engineering engine for Frontend Engineering Qa

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

- **frontendering_qa.analyze_architecture**: Analyze software architecture: patterns, dependencies, coupling, cohesion
- **frontendering_qa.discover_program**: Discover program behavior: black-box analysis, symbolic execution, fuzzing
- **frontendering_qa.verify_code_facts**: Verify code facts: type safety, memory safety, termination, complexity
- **frontendering_qa.optimize_performance**: Optimize performance: profiling, bottleneck analysis, and resource tuning
- **frontendering_qa.enforce_bounds**: Enforce bounded code: resource limits, time limits, and capability limits
- **frontendering_qa.manage_lifecycle**: Manage lifecycle: classify, validate, trace, assess, detect.
- **frontendering_qa.detect_drift**: Detect drift in evidence chains, provenance freshness, or confidence calibration.
- **frontendering_qa.validate_outputs**: Validate outputs against domain constraints and epistemic class.

> **Reference**: See `references/vault_domain_knowledge.md` (content_hash: 9d19043fdc5ef7a6) for the full vault-sourced domain knowledge (6462 chars).

## 11_KNOWLEDGE Vault Content

> **Source**: `11_KNOWLEDGE/AMOS_C10_TECH_ENGINEERING_MASTER_KNOWLEDGE.md` (content_hash: f23d35766fe766bc) (vault canon, SOURCE_CLAIM)

### Frontend Engineering QA

From C10 Tech & Engineering: Frontend quality assurance.

**Frontend QA dimensions**:
- **Accessibility**: WCAG compliance, screen reader compatibility, keyboard navigation
- **Cross-browser**: compatibility across browsers and versions
- **Responsive**: layout correctness across viewport sizes
- **Performance**: render time, bundle size, runtime performance
- **Visual regression**: visual consistency across changes
- **User experience**: interaction correctness, error states, loading states

**Frontend QA protocol**:
1. **Unit test**: test individual components in isolation
2. **Integration test**: test component composition
3. **Visual regression**: compare visual output against baseline
4. **Accessibility audit**: audit against WCAG criteria
5. **Performance audit**: audit render time and bundle size
6. **Cross-browser test**: test across target browsers

### Epistemic Boundary

Frontend engineering QA is an engineering process. It does not prove the UI is perfect, that all browsers are covered, or that accessibility is complete.

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

- **Skill**: `fronte