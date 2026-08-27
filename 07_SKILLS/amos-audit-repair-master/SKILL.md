---
title: SKILL
type: skill
name: amos-audit-repair-master
description: AMOS Audit & Repair — failure recovery, gap discovery, quality auditing, validation gates, repair allocation. Use for system auditing, gap analysis, or failure recovery.
parent_skill: none
domain: audit
origin_architect: Trang Phan
epistemic_class: SOURCE_CANON
tags: [note, amos-audit-repair-master]
---

# L10 Failure & Recovery Laws

## Identity

Origin architect and steward: **Trang Phan**.

This is a **parent skill** that consolidates 8 sub-skills into a single domain master.
Following the skill-organizer best practice: fewer, richer skills beat many overlapping ones.
A parent skill with clearly labeled sections is better than 8 separate shallow skills.

**Epistemic class**: SOURCE_CLAIM (vault-sourced from `01_CANON/01_CORE_LAWS/L10_FAILURE_RECOVERY.md`).

## When to Use

AMOS Audit & Repair — failure recovery, gap discovery, quality auditing, validation gates, repair allocation. Use for system auditing, gap analysis, or failure recovery.
- When validating outputs against domain constraints and epistemic class

## Capabilities

- **audit_repair.execute_recovery**: Execute AMOS Audit & Repair failure recovery: detect failure, diagnose root cause, apply repair, verify recovery.
- **audit_repair.validate_quality**: Validate AMOS Audit & Repair outputs against validation gates, equation firewall, golden ratio, and integrity requirements.
- **audit_repair.discover_gaps**: Discover knowledge gaps using AMOS Audit & Repair gap discovery engine, completion graph, and unknown-unknown registry.
- **audit_repair.trace_provenance**: Trace AMOS Audit & Repair findings to test results, integrity scans, gap registry, and validation gate outputs.
- **audit_repair.assess_claim**: Assess AMOS Audit & Repair audit claims for severity, scope, evidence strength, and repair priority.
- **audit_repair.manage_lifecycle**: Manage AMOS Audit & Repair audit lifecycle: scan, detect, classify, allocate repair, verify, and document.
- **audit_repair.detect_drift**: Detect audit drift: test count drift, gap regression, integrity degradation, and validation gate erosion.
- **audit_repair.escalate_gaps**: Escalate AMOS Audit & Repair audit gaps: flag CRITICAL gaps, prioritize repair allocation, trigger bounded recovery.
- **audit_repair.validate_outputs**: Validate outputs against domain constraints and epistemic class.

## Consolidated Sub-Skills (8)

This parent skill consolidates the following sub-skills. Each is a section within this domain:

## 11_KNOWLEDGE Vault Content

> **Source**: `11_KNOWLEDGE/AMOS_COGNITIVE_ORGANISM_OS_DETAIL.md` (content_hash: 61279c4b00128110) (vault canon, SOURCE_CLAIM)
> **Additional source**: `11_KNOWLEDGE/AMOS_C01_META_LOGIC_MASTER_KNOWLEDGE.md` (content_hash: ff5575df755d7e25) (vault canon, SOURCE_CLAIM)

### Audit & Repair Architecture

From Cognitive Organism OS: Self-audit gate, proof checking, selective invalidation, rollback basins.

**Audit pipeline**:
1. **Self-audit gate**: every runtime cycle passes through self-audit before finalization
2. **Proof checking**: ProofChecker validates claims against scope, regime, confidence ceiling, causal level, falsifiers
3. **Selective invalidation**: invalidate only the affected claims, not the entire proof graph
4. **Rollback basins**: every state transition has a declared rollback target

**Repair priority levels** (P0-P4):
- P0 CRITICAL: system cannot function; repair immediately, block all other work
- P1 HIGH: core capability degraded; repair before any non-repair work
- P2 MEDIUM: secondary capability degraded; repair within current cycle
- P3 LOW: minor issue; repair when capacity allows
- P4 DEFERRED: known issue, no current impact; log and monitor

**Repair laws**:
- `RepairCapacity > RepairDemand` required for autonomous repair
- `REPAIR != IMPROVEMENT`: repair fixes a specific issue; it does not improve the system
- `SYMPTOM != CAUSE`: repairing the symptom does not repair the cause

**5 Meta-laws for audit**:
1. Law of Law: no unresolved contradictions
2. Rule of 2: at least 2 independent supports for any claim
3. Rule of 4: check scope, regime, evidence, falsifier
4. Signal Fidelity Preservation
5. Structural Integrity

### Epistemic Boundary

Audit & repair is an operational governance construct. It does not prove absolute correctness, that all issues are detectable, or that repair always succeeds.

## 0. Status
Proposed specification replacing placeholder. AMOS_MODEL. Canonical status: CONDITIONAL.

## 2. Laws
- **FR-1 Collapse Precedes Visible Failure**: detect degradation before user-visible breakage (critical slowing down signals).
- **FR-2 Repair Capacity Bounds**: recovery is bounded by independent repair capacity per failure mode; correlated damage amplifies (DMER L5).
- **FR-3 Fail Closed on Critical Unknown**: missing authority/provenance/validation blocks execution rather than defaulting open.
- **FR-4 Recovery Basins**: every consequential subsystem declares a rollback t
- [[AGENT_TEMPLATE]]
