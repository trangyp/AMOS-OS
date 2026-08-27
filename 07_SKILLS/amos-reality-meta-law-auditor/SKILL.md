---
title: SKILL
type: skill
name: amos-reality-meta-law-auditor
description: Reality Meta Law Auditor — audit and repair capability. Use when auditing, failure analysis, gap discovery, or repair allocation. Use when amos-audit-repair-master routes to this specialized capability.
parent_skill: amos-audit-repair-master
domain: audit
origin_architect: Trang Phan
epistemic_class: SOURCE_CLAIM
tags: [note, amos-reality-meta-law-auditor]
---


# Reality Meta Law Auditor

## Identity

- **Origin architect and steward**: Trang Phan
- **Parent skill**: `amos-audit-repair-master`
- **Domain**: audit
- **Epistemic class**: SOURCE_CLAIM (vault-sourced from AMOS framework)

Audit and verification engine for Reality Meta Law Auditor

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

- **reality_meta.audit_claim**: Audit claims against evidence, provenance, and epistemic class
- **reality_meta.detect_gap**: Detect gaps: missing capabilities, missing evidence, missing tests, missing monitors
- **reality_meta.allocate_repair**: Allocate repair resources to highest-leverage gaps and failure modes
- **reality_meta.verify_closure**: Verify gap closure: requirement → capability → component → test → evidence
- **reality_meta.benchmark_forensics**: Benchmark forensic analysis: trace performance regressions to root causes

> **Reference**: See `references/vault_domain_knowledge.md` (content_hash: 82f89f9854baa4fc) for the full vault-sourced domain knowledge (9344 chars).
- **reality_meta.manage_lifecycle**: Manage lifecycle: classify, validate, trace, assess, detect.
- **reality_meta.detect_drift**: Detect drift in evidence chains, provenance freshness, or confidence calibration.
- **reality_meta.validate_outputs**: Validate outputs against domain constraints and epistemic class.

## 11_KNOWLEDGE Vault Content

> **Source**: `11_KNOWLEDGE/AMOS_C01_META_LOGIC_MASTER_KNOWLEDGE.md` (content_hash: ff5575df755d7e25) (vault canon, SOURCE_CLAIM)
> **Additional source**: `11_KNOWLEDGE/AMOS_COGNITIVE_ORGANISM_OS_DETAIL.md` (content_hash: 61279c4b00128110) (vault canon, SOURCE_CLAIM)

### Reality Meta-Law Auditor

From C01 Meta Logic: 5 meta-laws as the foundation for reality auditing. From Cognitive Organism OS: Reality Gate as L0 cognitive substrate.

**5 Meta-laws for reality auditing**:
1. **Law of Law**: no unresolved contradictions within the system
2. **Rule of 2**: at least 2 independent supports for any claim
3. **Rule of 4**: check 4 dimensions: scope, regime, evidence, falsifier
4. **Signal Fidelity Preservation**: no loss of signal fidelity through processing
5. **Structural Integrity**: system structure must be maintained under stress

**Reality auditing protocol**:
1. **Check contradictions**: verify no unresolved contradictions (Law of Law)
2. **Check independence**: verify at least 2 independent supports (Rule of 2)
3. **Check 4 dimensions**: verify scope, regime, evidence, falsifier (Rule of 4)
4. **Check signal fidelity**: verify no signal fidelity loss
5. **Check structural integrity**: verify structure maintained under stress
6. **Report**: report with audit outcome and provenance

**Reality Gate (L0)**:
- **Perception-as-science-substrate filter**: perceptions filtered through science substrate
- **Anti-autopoisoning**: system cannot poison its own perception
- **Reality check**: every observation must pass reality check

**Auditing laws**:
- `AUDIT != PROOF`: auditing checks declared properties; it does not prove truth
- `META-LAW != LAW**: meta-laws govern laws; they are not laws themselves
- `REALITY != PERCEPTION**: reality is independent of observation; perception is interpretation

### Epistemic Boundary

Reality meta-law auditing is an epistemic governance construct. It does not prove reality is knowable, that all meta-laws are covered, or that auditing always detects violations.

## Failure Modes

- **Insufficient evidence**: If source material is insufficient, mark as UNKNOWN/GAP and fail closed — do not fabricate.
- **Scope violation**: If the query falls outside the skill's declared scope, escalate to the parent skill or steward.
- **Binding broken**: If 1:1:1 binding (skill→agent→workflow) is broken, flag routing mismatch and block execution.
- **Validation failure**: If validation gates fail, downgrade confidence, flag the gap, and escalate — do not force-fit.
- **Epistemic overreach**: If a claim exceeds the established evidence or epistemic class, retrac

---
**Links:** [[07_SKILLS_MOC]]
