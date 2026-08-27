---
title: SKILL
type: skill
name: amos-repair-harm-auditor
description: Repair Harm Auditor — audit and repair capability. Use when auditing, failure analysis, gap discovery, or repair allocation. Use when amos-audit-repair-master routes to this specialized capability.
parent_skill: amos-audit-repair-master
domain: audit
origin_architect: Trang Phan
epistemic_class: SOURCE_CLAIM
tags: [note, amos-repair-harm-auditor]
---


# Repair Harm Auditor

## Identity

- **Origin architect and steward**: Trang Phan
- **Parent skill**: `amos-audit-repair-master`
- **Domain**: audit
- **Epistemic class**: SOURCE_CLAIM (vault-sourced from AMOS framework)

Audit and verification engine for Repair Harm Auditor

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

- **repair_harm.audit_claim**: Audit claims against evidence, provenance, and epistemic class
- **repair_harm.detect_gap**: Detect gaps: missing capabilities, missing evidence, missing tests, missing monitors
- **repair_harm.allocate_repair**: Allocate repair resources to highest-leverage gaps and failure modes
- **repair_harm.verify_closure**: Verify gap closure: requirement → capability → component → test → evidence
- **repair_harm.benchmark_forensics**: Benchmark forensic analysis: trace performance regressions to root causes
- **repair_harm.manage_lifecycle**: Manage lifecycle: classify, validate, trace, assess, detect.
- **repair_harm.detect_drift**: Detect drift in evidence chains, provenance freshness, or confidence calibration.
- **repair_harm.validate_outputs**: Validate outputs against domain constraints and epistemic class.

> **Reference**: See `references/vault_domain_knowledge.md` (content_hash: 2397f64f36ba675e) for the full vault-sourced domain knowledge (7564 chars).

## 11_KNOWLEDGE Vault Content

> **Source**: `_00_Cosmo brain/misc/O/overlooked.md` (content_hash: eb91d778a79b4c6a) (vault canon, SOURCE_CLAIM)
> **Additional source**: `_00_Cosmo brain/system/AMOS_Evolutionary_Adaptive_Systems_Cancer_to_AI_v2.md` (content_hash: 5843a9c7931441ea) (vault canon, SOURCE_CLAIM)
> **Additional source**: `_00_Cosmo brain/amos-general/A/PART/AMOS_7_PART_UNIVERSE_CANON_FULL_ARCHITECTURE_V2.md` (content_hash: f1acd357d7c51047) (vault canon, SOURCE_CLAIM)

### Repair Harm Auditor

From Cosmo Brain Overlooked: Repair Harm Auditor measures whether repair increases long-term coherence or only suppresses visible failure. From Evolutionary Adaptive Systems: Repair harm as defense externality. From 7-Part Universe Canon: Repair harm firewall.

**Repair harm definition**: A repair is invalid if it restores one part while causing larger structural damage elsewhere.

**Defense externality equation** (SOURCE_DERIVED):
```
NetDefenseValue = PreventedHarm - DefenseExternality
```
- Repair harm is a defense externality alongside: over-refusal, capability destruction, false quarantine, excessive friction, loss of useful diversity

**Repair Harm Auditor module** (from Overlooked):
- Measures whether repair increases long-term coherence
- Or only suppresses visible failure
- Key question: does the repair make the system genuinely better, or just quieter?

**Repair harm firewall** (from 7-Part Universe Canon):
- A repair is invalid if it restores one part while causing larger structural damage elsewhere
- Repair must be evaluated for system-wide impact, not just local fix

**Auditing protocol**:
1. **Measure local benefit**: measure the benefit of the repair at the repair site
2. **Measure systemic harm**: measure the harm caused elsewhere in the system
3. **Compute net value**: compute net defense value
4. **Decide**: if net value < 0, the repair is harmful; block it
5. **Record**: record with provenance

**Auditing laws**:
- `REPAIR != IMPROVEMENT`: repair fixes a specific issue; it does not always improve the system
- `LOCAL_FIX != SYSTEMIC_HEALTH**: a local fix may cause systemic harm
- `SUPPRESSION != RESOLUTION**: suppressing a visible failure is not resolving the underlying issue

### Epistemic Boundary

Repair harm auditing is an operational construct. It does not prove all repair harm is detected, that the net value calculation is always correct, or that harmful repairs can always be blocked.

## Failure Modes

- **Insufficient evidence**: If source material is insufficient, mark as UNKNOWN/GAP and fail closed — do not fabricate.
- **Scope violation**: If the query falls outside the skill's declared scope, escalate to 