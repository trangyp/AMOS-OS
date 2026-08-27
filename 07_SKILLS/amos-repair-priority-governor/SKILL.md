---
title: SKILL
type: skill
name: amos-repair-priority-governor
description: Repair Priority Governor — audit and repair capability. Use when auditing, failure analysis, gap discovery, or repair allocation. Use when amos-audit-repair-master routes to this specialized capability.
parent_skill: amos-audit-repair-master
domain: audit
origin_architect: Trang Phan
epistemic_class: SOURCE_CLAIM
tags: [note, amos-repair-priority-governor]
---


# Repair Priority Governor

## Identity

- **Origin architect and steward**: Trang Phan
- **Parent skill**: `amos-audit-repair-master`
- **Domain**: audit
- **Epistemic class**: SOURCE_CLAIM (vault-sourced from AMOS framework)

Audit and verification engine for Repair Priority Governor

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

- **repair_priority.audit_claim**: Audit claims against evidence, provenance, and epistemic class
- **repair_priority.detect_gap**: Detect gaps: missing capabilities, missing evidence, missing tests, missing monitors
- **repair_priority.allocate_repair**: Allocate repair resources to highest-leverage gaps and failure modes
- **repair_priority.verify_closure**: Verify gap closure: requirement → capability → component → test → evidence
- **repair_priority.benchmark_forensics**: Benchmark forensic analysis: trace performance regressions to root causes
- **repair_priority.manage_lifecycle**: Manage lifecycle: classify, validate, trace, assess, detect.
- **repair_priority.detect_drift**: Detect drift in evidence chains, provenance freshness, or confidence calibration.
- **repair_priority.validate_outputs**: Validate outputs against domain constraints and epistemic class.

> **Reference**: See `references/vault_domain_knowledge.md` (content_hash: a7b67e0c7ee84164) for the full vault-sourced domain knowledge (7564 chars).

## 11_KNOWLEDGE Vault Content

> **Source**: `_00_Cosmo brain/misc/D/Distinction–Mutation–Entropy–Repair.md` (content_hash: 551b49315372ac2d) (vault canon, SOURCE_CLAIM)
> **Additional source**: `11_KNOWLEDGE/AMOS_COGNITIVE_ORGANISM_OS_DETAIL.md` (content_hash: 61279c4b00128110) (vault canon, SOURCE_CLAIM)

### Repair Priority Governor

From Cosmo Brain Distinction-Mutation-Entropy-Repair: Repair priority formula and selective repair. Global recomputation is last resort.

**Repair priority formula** (SOURCE_DERIVED):
```
Priority_i = Impact_i × DependencyFanout_i × Irreversibility_i × UncertaintyReduction_i
```
subject to hard safety constraints.

**Priority factors**:
- **Impact**: how much does the issue affect the system?
- **Dependency fanout**: how many other components depend on this one?
- **Irreversibility**: how hard is it to undo the repair if it's wrong?
- **Uncertainty reduction**: how much does the repair reduce uncertainty?

**Selective repair principle**: `Invalid(p) => Repair(p)` not `Invalid(p) => ResetEverything`. Global recomputation is last resort.

**5 Priority levels** (P0-P4):
- **P0 CRITICAL**: system cannot function; repair immediately, block all other work
- **P1 HIGH**: core capability degraded; repair before any non-repair work
- **P2 MEDIUM**: secondary capability degraded; repair within current cycle
- **P3 LOW**: minor issue; repair when capacity allows
- **P4 DEFERRED**: known issue, no current impact; log and monitor

**Repair laws**:
- `RepairCapacity > RepairDemand` required for autonomous repair
- `REPAIR != IMPROVEMENT`: repair fixes a specific issue; it does not improve the system
- `SYMPTOM != CAUSE**: repairing the symptom does not repair the cause
- `SELECTIVE != GLOBAL**: selective repair targets the specific issue; global recomputation is last resort

### Epistemic Boundary

Repair priority governance is an operational construct. It does not prove optimal repair ordering, that all issues are prioritized, or that repair always succeeds.

## Failure Modes

- **Insufficient evidence**: If source material is insufficient, mark as UNKNOWN/GAP and fail closed — do not fabricate.
- **Scope violation**: If the query falls outside the skill's declared scope, escalate to the parent skill or steward.
- **Binding broken**: If 1:1:1 binding (skill→agent→workflow) is broken, flag routing mismatch and block execution.
- **Validation failure**: If validation gates fail, downgrade confidence, flag the gap, and escalate — do not force-fit.
- **Epistemic overreach**: If a claim exceeds the established evidence or epistemic class, retract and relabel.

## V