---
title: SKILL
type: skill
name: amos-semantic-grounding-auditor
description: Semantic Grounding Auditor — audit and repair capability. Use when auditing, failure analysis, gap discovery, or repair allocation. Use when amos-audit-repair-master routes to this specialized capability.
parent_skill: amos-audit-repair-master
domain: audit
origin_architect: Trang Phan
epistemic_class: SOURCE_CLAIM
tags: [note, amos-semantic-grounding-auditor]
---


# Semantic Grounding Auditor

## Identity

- **Origin architect and steward**: Trang Phan
- **Parent skill**: `amos-audit-repair-master`
- **Domain**: audit
- **Epistemic class**: SOURCE_CLAIM (vault-sourced from AMOS framework)

Audit and verification engine for Semantic Grounding Auditor

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

- **semantic_grounding.audit_claim**: Audit claims against evidence, provenance, and epistemic class
- **semantic_grounding.detect_gap**: Detect gaps: missing capabilities, missing evidence, missing tests, missing monitors
- **semantic_grounding.allocate_repair**: Allocate repair resources to highest-leverage gaps and failure modes
- **semantic_grounding.verify_closure**: Verify gap closure: requirement → capability → component → test → evidence
- **semantic_grounding.benchmark_forensics**: Benchmark forensic analysis: trace performance regressions to root causes
- **semantic_grounding.manage_lifecycle**: Manage lifecycle: classify, validate, trace, assess, detect.
- **semantic_grounding.detect_drift**: Detect drift in evidence chains, provenance freshness, or confidence calibration.
- **semantic_grounding.validate_outputs**: Validate outputs against domain constraints and epistemic class.

> **Reference**: See `references/vault_domain_knowledge.md` (content_hash: 85c573728ca44418) for the full vault-sourced domain knowledge (5667 chars).

## 11_KNOWLEDGE Vault Content

> **Source**: `_00_Cosmo brain/misc/O/overlooked.md` (content_hash: eb91d778a79b4c6a) (vault canon, SOURCE_CLAIM)
> **Additional source**: `_00_Cosmo brain/misc/N/New.md` (content_hash: 32c4e8fb2fe2d69f) (vault canon, SOURCE_CLAIM)

### Semantic Grounding Auditor

From Cosmo Brain Overlooked: Semantic Grounding Divergence Detector to measure distance between symbolic coherence and structural reality. From New.md: Concrete world model with safe semantics envelope.

**Semantic grounding divergence equations** (SOURCE_DERIVED):
```
Divergence = |Semantic_Coherence - Structural_Grounding|
Grounding_Loss = 1 - exp(-Divergence)
```
- **Semantic coherence**: internal consistency of symbols
- **Structural grounding**: correlation with measurable reality

**Concrete world model** (from New.md):
```
w = (S, T, Predicates, Ctx, Trace)
```
- S = states, T = transitions, Predicates = predicates, Ctx = context, Trace = execution trace
- Claims evaluated via `w ⊨ c` (world satisfies claim)

**Grounding loss examples**: over-academic abstraction, LLM hallucination, legal formalism detached from reality

**Auditing protocol**:
1. **Measure semantic coherence**: measure internal consistency of symbols
2. **Measure structural grounding**: measure correlation with measurable reality
3. **Compute divergence**: compute divergence between the two
4. **Compute grounding loss**: compute grounding loss from divergence
5. **Report**: report with provenance and epistemic class

**Auditing laws**:
- `COHERENCE != GROUNDING`: internal coherence does not imply external grounding
- `SYMBOL != REALITY`: symbols represent reality; they are not reality
- `GROUNDED != TRUE**: grounding connects to measurable reality; it does not prove truth

### Epistemic Boundary

Semantic grounding auditing is an epistemic construct. It does not prove all grounding loss is detected, that the divergence formula is universally applicable, or that grounding implies truth.

## Failure Modes
- **Insufficient evidence**: If source material is insufficient, mark as UNKNOWN/GAP and fail closed — do not fabricate.
- **Scope violation**: If the query falls outside the skill's declared scope, escalate to the parent skill or steward.
- **Binding broken**: If 1:1:1 binding (skill→agent→workflow) is broken, flag routing mismatch and block execution.
- **Validation failure**: If validation gates fail, downgrade confidence, flag the gap, and escalate — do not force-fit.
- **Epistemic overreach**: If a claim exceeds the established evidence or epistemic class, retract and relabel.

