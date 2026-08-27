---
title: 2026 08 22 ASSURANCE DEBT GOVERNANCE
tags: [dated, dated/2026-08-22]
type: document
source: 11_KNOWLEDGE/dated
---



# Assurance, Debt Registers & Maturity Governance

**Date**: 2026-08-22
**Module**: `amos/governance/assurance_debt.py`
**Gaps**: 301-320 (20 gaps, all closed)
**Tests**: 69 tests in `tests/test_assurance_debt.py`

## Overview

The Assurance, Debt Registers & Maturity Governance module provides the final
layer of the AMOS OS Kernel's governance stack. It ensures that assurance
cases are properly reviewed, debt is tracked and managed, components reach
appropriate maturity levels before promotion, evidence/benchmarks/policies
are kept current, obsolete architecture is detected, and simplification
opportunities are pursued.

## Subsystems

### 301 — Independent Falsifier Manager
Tracks independent falsifier access for scientific claims.
Gate: CONDITIONAL if pending falsifier access.

### 302 — Red-Team Independence Manager
Ensures red teams are independent from the development team.
Gate: FAIL if non-independent red teams detected.

### 303 — Assurance Case Manager
Manages assurance cases (draft/under_review/approved/rejected/expired).
Gate: CONDITIONAL if unapproved or expired cases.

### 304 — Certification Profile Manager
Tracks certifications (standard/level/certifier/valid_until).
Gate: CONDITIONAL if expired certifications.

### 305 — Residual Risk Acceptance Manager
Tracks residual risk acceptance by designated authority.
Gate: CONDITIONAL if unaccepted residual risks.

### 306 — Known Gap Disclosure Manager
Ensures known gaps are disclosed to appropriate audiences.
Gate: FAIL if undisclosed known gaps.

### 307-310 — Debt Register Manager
Tracks four types of debt: epistemic, governance, security, architecture.
Gate: FAIL if debt amount > 0.75 threshold.

### 311 — Debt Interaction Manager
Analyzes interactions between different types of debt.
Gate: CONDITIONAL if high-severity interactions (> 0.5).

### 312 — Maturity State Manager
Tracks component maturity (experimental/prototype/beta/production/legacy/deprecated).
Gate: CONDITIONAL if immature components in use.

### 313 — Promotion Evidence Manager
Manages promotion evidence standards (pending/promoted/demoted/quarantined/rejected).
Gate: CONDITIONAL if pending promotions.

### 314 — Demotion/Quarantine Manager
Manages demotion and quarantine rules with authority tracking.
Gate: FAIL if quarantined without authority; CONDITIONAL if quarantined with authority.

### 315 — Continuous Revalidation Manager
Tracks continuous revalidation results.
Gate: FAIL if failed revalidations.

### 316-318 — Expiry Managers
Track expiry of evidence, benchmarks, and policies.
Gates: CONDITIONAL if expired items detected.

### 319 — Architecture Obsolescence Manager
Detects obsolete architecture components.
Gate: CONDITIONAL if obsolete architecture detected.

### 320 — Simplification Manager
Tracks simplification opportunities and their completion.
Gate: CONDITIONAL if pending simplifications.

## Gate Semantics

5 FAIL gates (302, 306, 307, 314-unauthorized, 315) block execution for critical assurance issues.
12 CONDITIONAL gates provide advisory warnings for less critical issues.
Total: 17 gates from 17 subsystems.

## Integration

- Wired into `AmosKernel.run()` as `self.assurance_debt_governor`
- Gate evaluation: `ad_post_gates = self.assurance_debt_governor.evaluate_post(state)`
- Exports: All 17 managers and governor exported via `amos/__init__.py`

## Completion Milestone

With gaps 301-320 closed, ALL 230 meta-gaps (91-320) are now closed.
The AMOS OS Kernel completion graph has 0 open gaps remaining.

---
**Related:** [[00_HOME]] · [[KNOWLEDGE_MOC]] · [[AMOS_SIMULATION_KERNEL_V0_MATH_FOUNDATIONS]] · [[SYSTEM_SCAN_AGENT]] · [[AUTOMATION_PROFILES]]

---
**MOC:** [[DATED_MOC]]
