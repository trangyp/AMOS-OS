---
title: SKILL
type: skill
name: amos-neural-ode-dynamics-rscf-engine
description: Neural Ode Dynamics — biology and neuroscience capability. Use when biological reasoning, neuroscience, or medical analysis. Use when amos-c04-bio-neuro-master routes to this specialized capability.
parent_skill: amos-c04-bio-neuro-master
domain: c04
origin_architect: Trang Phan
epistemic_class: SOURCE_CLAIM
tags: [note, amos-neural-ode-dynamics-rscf-engine]
---


# Neural Ode Dynamics Rscf Engine

## Identity

- **Origin architect and steward**: Trang Phan
- **Parent skill**: `amos-c04-bio-neuro-master`
- **Domain**: c04
- **Epistemic class**: SOURCE_CLAIM (vault-sourced from AMOS framework)

Bio-neuro engine for Neural Ode Dynamics Rscf Engine

## When to Use

- When mapping biological mechanisms: cellular, neural, developmental
- When assessing cross-species cognition and comparative intelligence
- When modeling morphogenesis: pattern formation and self-organization
- When the parent skill (`amos-c04-bio-neuro-master`) routes to this specialized capability
- When managing lifecycle operations across classify, validate, trace, assess, and detect
- When detecting drift in evidence chains, provenance freshness, or confidence calibration
- When validating outputs against domain constraints and epistemic class

## Capabilities

- **neural_ode.map_mechanism**: Map biological mechanisms: cellular, neural, developmental, and evolutionary
- **neural_ode.assess_cognition**: Assess cross-species cognition: comparative neural computation and intelligence
- **neural_ode.model_morphogenesis**: Model morphogenesis: pattern formation, self-organization, and development
- **neural_ode.manage_lifecycle**: Manage lifecycle: classify, validate, trace, assess, detect.
- **neural_ode.detect_drift**: Detect drift in evidence chains, provenance freshness, or confidence calibration.
- **neural_ode.validate_outputs**: Validate outputs against domain constraints and epistemic class.

> **Reference**: See `references/vault_domain_knowledge.md` (content_hash: 002c985da1b99ec1) for the full vault-sourced domain knowledge (6613 chars).

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
- **G4 (Anti-overreach)**: No claim beyond the skill's declared scope and epistemic class.
- **G5 (Equation firewall)**: Equations carry status tags (ESTABLISHED_MATH / SOURCE_DERIVED / AMOS_MODEL / EMPIRICALLY_CALIBRATED / UNVERIFIED).
- **G6 (Failure mode)**: On validation failure, downgrade confidence, flag the gap, escalate — do not force-fit.

## Provenance

- **Skill**: `amos-neural-ode-dynamics-rscf-engine`
- **Parent**: `amos-c04-bio-neuro-master`
- **Domain**: c04
- **Origin arch

---
**Links:** [[07_SKILLS_MOC]]
