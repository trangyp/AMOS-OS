---
title: SKILL
type: skill
name: amos-measurement-integrity-auditor
description: Measurement Integrity Auditor — audit and repair capability. Use when auditing, failure analysis, gap discovery, or repair allocation. Use when amos-audit-repair-master routes to this specialized capability.
parent_skill: amos-audit-repair-master
domain: audit
origin_architect: Trang Phan
epistemic_class: SOURCE_CLAIM
tags: [note, amos-measurement-integrity-auditor]
---


# Measurement Integrity Auditor

## Identity

- **Origin architect and steward**: Trang Phan
- **Parent skill**: `amos-audit-repair-master`
- **Domain**: audit
- **Epistemic class**: SOURCE_CLAIM (vault-sourced from AMOS framework)

Audit and verification engine for Measurement Integrity Auditor

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

- **measurement_integrity.audit_claim**: Audit claims against evidence, provenance, and epistemic class
- **measurement_integrity.detect_gap**: Detect gaps: missing capabilities, missing evidence, missing tests, missing monitors
- **measurement_integrity.allocate_repair**: Allocate repair resources to highest-leverage gaps and failure modes
- **measurement_integrity.verify_closure**: Verify gap closure: requirement → capability → component → test → evidence
- **measurement_integrity.benchmark_forensics**: Benchmark forensic analysis: trace performance regressions to root causes

> **Reference**: See `references/vault_domain_knowledge.md` (content_hash: d0d25eb4d17058d9) for the full vault-sourced domain knowledge (9047 chars).
- **measurement_integrity.manage_lifecycle**: Manage lifecycle: classify, validate, trace, assess, detect.
- **measurement_integrity.detect_drift**: Detect drift in evidence chains, provenance freshness, or confidence calibration.
- **measurement_integrity.validate_outputs**: Validate outputs against domain constraints and epistemic class.

## 11_KNOWLEDGE Vault Content

> **Source**: `_00_Cosmo brain/amos-general/A/Collapse/AMOS Collapse-Space Coverage Audit.md` (content_hash: 8a6e8edc4d87f23a) (vault canon, SOURCE_CLAIM)
> **Additional source**: `_00_Cosmo brain/dated/2026-08-23/2026-08-23 Vault Integrity Pass.md` (content_hash: ce31f8fdd0467e1e) (vault canon, SOURCE_CLAIM)
> **Additional source**: `11_KNOWLEDGE/AMOS_C01_META_LOGIC_MASTER_KNOWLEDGE.md` (content_hash: ff5575df755d7e25) (vault canon, SOURCE_CLAIM)

### Measurement Integrity Auditor

From Cosmo Brain Collapse-Space Coverage Audit: Measurement integrity in collapse-space auditing. From Vault Integrity Pass: 7-part canon lens applied to vault integrity.

**Measurement integrity model**:
- **Measurement validity**: measurements must be valid (measure what they claim to measure)
- **Measurement reliability**: measurements must be reliable (reproducible under same conditions)
- **Measurement accuracy**: measurements must be accurate (close to true value)
- **Measurement precision**: measurements must be precise (low variance)

**7-part canon lens for integrity auditing** (from Vault Integrity Pass):
1. **Constraint**: what bounded this audit (scope, limitations)
2. **Flow**: what was done (steps, actions)
3. **Structure**: what holds it (canon notes, validators, mappings)
4. **Enforcement**: what corrects errors (deterministic gates, re-runnable audits)
5. **Time**: lifecycle considerations (drift, new gaps)
6. **Adaptation**: how to handle new gaps (add pointer/anchor, never fabricate)
7. **Termination**: completion state (GREEN/RED, known-state)

**Integrity audit protocol**:
1. **Baseline**: file health (0 empty, 0 broken symlinks)
2. **Scan**: scan for broken targets, gaps, orphans
3. **Classify**: classify issues (drift, genuine gap, known-state)
4. **Repair**: repair drift links, create anchor notes for gaps
5. **Validate**: run deterministic validator
6. **Report**: report with honest status (don't claim zero broken if data-dump orphans exist)

**Integrity law**: `AUDIT_PASS != PERFECT`. An audit pass means declared checks pass; it does not prove perfection. Known-state issues are documented, not hidden.

### Epistemic Boundary

Measurement integrity auditing is an operational governance construct. It does not prove all issues are detected, that measurements are always correct, or that the audit is complete.

## Failure Modes

- **Insufficient evidence**: If source material is insufficient, mark as UNKNOWN/GAP and fail closed — do not fabricate.
- **Scope violation**: If the q