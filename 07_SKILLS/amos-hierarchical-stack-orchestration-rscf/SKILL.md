---
title: SKILL
type: skill
name: amos-hierarchical-stack-orchestration-rscf
description: Hierarchical Stack Orchestration — RSCF epistemic capability. Use when classifying claims by epistemic state, validating outputs against epistemic and scope constraints, or analyzing evidence structure. Use when amos-rscf-epistemic-master routes t...
parent_skill: amos-rscf-epistemic-master
domain: rscf
origin_architect: Trang Phan
epistemic_class: SOURCE_CLAIM
tags: [note, amos-hierarchical-stack-orchestration-rscf]
---


# Hierarchical Stack Orchestration Rscf

## Identity

- **Origin architect and steward**: Trang Phan
- **Parent skill**: `amos-rscf-epistemic-master`
- **Domain**: rscf
- **Epistemic class**: SOURCE_CLAIM (vault-sourced from AMOS framework)

RSCF epistemic engine for Hierarchical Stack Orchestration Rscf

## When to Use

- When classifying claims by epistemic state (VERIFIED, DERIVED, MODEL, UNKNOWN/GAP)
- When validating evidence chains for provenance, freshness, and scope
- When assessing confidence ceilings based on epistemic class
- When detecting falsifiers that would downgrade confidence
- When the parent skill (`amos-rscf-epistemic-master`) routes to this specialized capability
- When managing lifecycle operations across classify, validate, trace, assess, and detect
- When detecting drift in evidence chains, provenance freshness, or confidence calibration
- When validating outputs against domain constraints and epistemic class

## Capabilities

- **hierarchical_stack.classify_claim**: Classify claims by epistemic state (VERIFIED, DERIVED, MODEL, UNKNOWN/GAP) and bind to evidence
- **hierarchical_stack.validate_evidence**: Validate evidence chains: provenance, freshness, scope, and regime validity
- **hierarchical_stack.trace_provenance**: Trace output provenance to vault sources and tag with content_hash
- **hierarchical_stack.assess_confidence**: Assess confidence ceiling based on epistemic class and evidence strength
- **hierarchical_stack.detect_falsifier**: Detect falsifiers and downgrade confidence when counter-evidence emerges

> **Reference**: See `references/vault_domain_knowledge.md` (content_hash: f0025be77a376c73) for the full vault-sourced domain knowledge (8705 chars).
- **hierarchical_stack.manage_lifecycle**: Manage lifecycle: classify, validate, trace, assess, detect.
- **hierarchical_stack.detect_drift**: Detect drift in evidence chains, provenance freshness, or confidence calibration.
- **hierarchical_stack.validate_outputs**: Validate outputs against domain constraints and epistemic class.

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
- **G4 (Anti-overreach)**: No claim beyond the skill'