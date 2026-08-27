---
title: SKILL
type: skill
name: amos-metacognitive-confidence-auditor
description: Metacognitive Confidence Auditor — audit and repair capability. Use when auditing, failure analysis, gap discovery, or repair allocation. Use when amos-audit-repair-master routes to this specialized capability.
parent_skill: amos-audit-repair-master
domain: audit
origin_architect: Trang Phan
epistemic_class: SOURCE_CLAIM
tags: [note, amos-metacognitive-confidence-auditor]
---


# Metacognitive Confidence Auditor

## Identity

- **Origin architect and steward**: Trang Phan
- **Parent skill**: `amos-audit-repair-master`
- **Domain**: audit
- **Epistemic class**: SOURCE_CLAIM (vault-sourced from AMOS framework)

Audit and verification engine for Metacognitive Confidence Auditor

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

- **metacognitive_confidence.audit_claim**: Audit claims against evidence, provenance, and epistemic class
- **metacognitive_confidence.detect_gap**: Detect gaps: missing capabilities, missing evidence, missing tests, missing monitors
- **metacognitive_confidence.allocate_repair**: Allocate repair resources to highest-leverage gaps and failure modes
- **metacognitive_confidence.verify_closure**: Verify gap closure: requirement → capability → component → test → evidence
- **metacognitive_confidence.benchmark_forensics**: Benchmark forensic analysis: trace performance regressions to root causes
- **metacognitive_confidence.manage_lifecycle**: Manage lifecycle: classify, validate, trace, assess, detect.
- **metacognitive_confidence.detect_drift**: Detect drift in evidence chains, provenance freshness, or confidence calibration.
- **metacognitive_confidence.validate_outputs**: Validate outputs against domain constraints and epistemic class.

> **Reference**: See `references/vault_domain_knowledge.md` (content_hash: 308a3432feb5f1b0) for the full vault-sourced domain knowledge (5553 chars).

## 11_KNOWLEDGE Vault Content

> **Source**: `_00_Cosmo brain/cognitive/Metacognitive.md` (content_hash: 156abe467cfa7744) (vault canon, SOURCE_CLAIM)
> **Additional source**: `11_KNOWLEDGE/AMOS_C05_MIND_BEHAVIOR_MASTER_KNOWLEDGE.md` (content_hash: e3ca4951a743518b) (vault canon, SOURCE_CLAIM)

### Metacognitive Confidence Auditor

From Cosmo Brain Metacognitive: Metacognitive monitoring and control. From C05 Mind & Behavior: Confidence calibration and metacognitive awareness.

**Metacognitive confidence model**:
- **Confidence calibration**: confidence must be calibrated to evidence strength
- **Confidence ceiling**: confidence cannot exceed evidence support (from RSCF)
- **Confidence tracking**: track confidence changes through reasoning chains
- **Confidence audit**: audit confidence against actual outcomes

**Metacognitive monitoring**:
- **Self-monitoring**: the system monitors its own reasoning process
- **Error detection**: the system detects errors in its own reasoning
- **Uncertainty awareness**: the system is aware of its own uncertainty
- **Confidence awareness**: the system is aware of its own confidence level

**Auditing protocol**:
1. **Sample**: sample reasoning chains for audit
2. **Check confidence**: check confidence against evidence support
3. **Check calibration**: check confidence calibration against outcomes
4. **Check ceiling**: check confidence does not exceed evidence
5. **Report**: report audit findings with provenance

**Auditing laws**:
- `CONFIDENCE != ACCURACY`: high confidence does not imply high accuracy
- `CALIBRATION != CORRECTION**: calibration aligns confidence with accuracy; correction fixes errors
- `METACOGNITION != COGNITION**: metacognition is cognition about cognition; it is not cognition itself

### Epistemic Boundary

Metacognitive confidence auditing is an epistemic construct. It does not prove confidence is always calibrated, that metacognition is always accurate, or that auditing detects all confidence errors.

## Failure Modes
- **Insufficient evidence**: If source material is insufficient, mark as UNKNOWN/GAP and fail closed — do not fabricate.
- **Scope violation**: If the query falls outside the skill's declared scope, escalate to the parent skill or steward.
- **Binding broken**: If 1:1:1 binding (skill→agent→workflow) is broken, flag routing mismatch and block execution.
- **Validation failure**: If validation gates fail, downgrade confidence, flag the gap, and escalate — do not force-fit.
- **Epistemic overreach**: I

---
**Links:** [[07_SKILLS_MOC]]
