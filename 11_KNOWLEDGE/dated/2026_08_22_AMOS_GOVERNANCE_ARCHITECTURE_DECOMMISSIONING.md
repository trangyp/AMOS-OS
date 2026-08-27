---
title: "AMOS Governance Architecture Decommissioning"
created: "2026-08-22"
type: note
tags: [canon-group/human-system, canon/framework, rscf/claim, rscf/provenance, rscf/state/observation, topic/amos-governance-architecture, dated, dated/2026-08-22]
status: "living"
provenance: "MODEL"
confidence: "VERIFIED"
---


# AMOS Governance Architecture & Decommissioning (Gaps 280-290)

> Epistemic class: MODEL (code artifact + test verification).
> Related: 2026-08-22 AMOS Fairness Ethics Externalities · 2026-08-22 AMOS Accessibility I18n · amos-completion-graph-workflow

## Summary

Closed gaps 280-290 by implementing the **Governance Architecture &
Decommissioning** governance module (`amos/governance/governance_architecture.py`).
This is the 22nd governance gate in `AmosKernel.run()`, evaluated post-execution.

## 11 Subsystems

| Gap | Subsystem | Class | Purpose |
|-----|-----------|-------|---------|
| 280 | Governance succession | `GovernanceSuccessionTracker` | Succession planning |
| 281 | Separation of powers | `SeparationOfPowersChecker` | Power balance checks |
| 282 | Insider threat | `InsiderThreatModeler` | Insider-threat modeling |
| 283 | Two-person control | `TwoPersonControlChecker` | Two-person verification |
| 284 | Capture resistance | `GovernanceCaptureChecker` | Capture resistance |
| 285 | Vendor dependency | `VendorDependencyMapper` | Vendor dependency map |
| 286 | Vendor exit | `VendorExitPlanner` | Vendor exit planning |
| 287 | Degraded operation | `DegradedOperationManager` | Offline/degraded operation |
| 288 | Business continuity | `BusinessContinuityChecker` | Business continuity |
| 289 | Decommissioning | `DecommissioningProtocol` | Decommissioning protocol |
| 290 | Orphan state | `OrphanStateHandler` | Orphan-state handling |

## Gate Evaluation

`GovernanceArchitectureGovernor.evaluate_post()` returns 11 gate results:
- `gov-280-succession-failed` (FAIL) / `gov-280-succession-not-planned` (CONDITIONAL) / `gov-280-succession` (PASS)
- `gov-281-unbalanced-powers` (CONDITIONAL) / `gov-281-separation-of-powers` (PASS)
- `gov-282-insider-threat-high` (FAIL) / `gov-282-insider-threat-detected` (CONDITIONAL) / `gov-282-insider-threat` (PASS)
- `gov-283-two-person-failed` (FAIL) / `gov-283-two-person-pending` (CONDITIONAL) / `gov-283-two-person-control` (PASS)
- `gov-284-capture-compromised` (FAIL) / `gov-284-capture-vulnerable` (CONDITIONAL) / `gov-284-governance-capture` (PASS)
- `gov-285-vendor-critical` (CONDITIONAL) / `gov-285-vendor-dependency` (PASS)
- `gov-286-vendor-exit-blocked` (CONDITIONAL) / `gov-286-vendor-exit-not-planned` (CONDITIONAL) / `gov-286-vendor-exit` (PASS)
- `gov-287-degraded-operation` (CONDITIONAL) / `gov-287-operation-mode` (PASS)
- `gov-288-continuity-interrupted` (FAIL) / `gov-288-continuity-not-tested` (CONDITIONAL) / `gov-288-business-continuity` (PASS)
- `gov-289-decommission-blocked` (CONDITIONAL) / `gov-289-decommission-no-notification` (CONDITIONAL) / `gov-289-decommissioning` (PASS)
- `gov-290-orphan-state` (CONDITIONAL/PASS)

## Key Semantics

1. **Succession status**: PLANNED, ACTIVE, COMPLETED, FAILED, NOT_PLANNED
2. **Power branches**: LEGISLATIVE, EXECUTIVE, JUDICIAL, AUDIT, EMERGENCY
3. **Insider threat levels**: NONE, LOW, MEDIUM, HIGH, CRITICAL
4. **Two-person control**: VERIFIED, PENDING, FAILED, NOT_REQUIRED
5. **Capture resistance**: RESISTANT, VULNERABLE, COMPROMISED, NOT_ASSESSED
6. **Vendor dependency**: NONE, LOW, MEDIUM, HIGH, CRITICAL
7. **Vendor exit**: NOT_PLANNED, PLANNED, IN_PROGRESS, COMPLETED, BLOCKED
8. **Degraded operation**: NORMAL, DEGRADED, OFFLINE, EMERGENCY
9. **Business continuity**: ACTIVE, RECOVERING, DEGRADED, INTERRUPTED, NOT_TESTED
10. **Decommissioning**: ACTIVE, SCHEDULED, IN_PROGRESS, COMPLETED, BLOCKED
11. **Orphan state**: RESOLVED, ORPHANED, ADOPTED, QUARANTINED
12. **Governor attributes**: `succession`, `separation`, `insider_threat`, `two_person`, `capture`, `vendor_dependency`, `vendor_exit`, `degraded`, `continuity`, `decommissioning`, `orphan`
13. **Kernel attribute**: `governance_arch_governor`
14. **Empty state**: All gates return PASS on empty state (no CONDITIONAL for empty).

## Implementation Chain

- **Types**: `amos/core/types.py` — 11 dataclasses + 11 enums
- **Schema**: `amos/state/store.py` — 11 tables + 11 put/list method pairs
- **Module**: `amos/governance/governance_architecture.py` — 11 subsystems + governor
- **Kernel**: `amos/kernel.py` — import, instantiation, gate evaluation
- **Exports**: `amos/__init__.py` — all types + `GovernanceArchitectureGovernor`
- **Tests**: `tests/test_governance_architecture.py` — 39 tests
- **Seeder**: `amos/governance/seed_completion.py` — gaps 280-290 in CLOSED_CLUSTERS

## Completion Graph Impact

- **Closed gaps**: 189 → 200 (gaps 280-290 = 11 gaps closed)
- **Open gaps**: 41 → 30
- **Total tests**: 1347 → 1386 (39 new tests)
- **All 1386 tests pass**

## Lessons Learned

1. **11 subsystems in one cluster**: This is the largest cluster so far (11 gaps). All subsystems follow the same `record()`/`get()`/`list_all()`/`has_*()` pattern.
2. **Governor attribute naming**: Uses short names (`succession`, `separation`, `insider_threat`, `two_person`, `capture`, `vendor_dependency`, `vendor_exit`, `degraded`, `continuity`, `decommissioning`, `orphan`).
3. **Kernel attribute**: `governance_arch_governor` (not `governance_architecture_governor` — shorter).
4. **Gate prefix**: All gates use `gov-` prefix (not `governance-` or `arch-`).
5. **Empty state**: All 11 gates return PASS on empty state — no CONDITIONAL for empty registries (unlike fairness_ethics where stakeholder gate was CONDITIONAL on empty).
6. **FAIL triggers**: succession-failed, insider-threat-high, two-person-failed, capture-compromised, continuity-interrupted.
7. **CONDITIONAL triggers**: succession-not-planned, unbalanced-powers, insider-threat-detected, two-person-pending, capture-vulnerable, vendor-critical, vendor-exit-blocked/not-planned, degraded-operation, continuity-not-tested, decommission-blocked/no-notification, orphan-state.

---
**Links:** [[DATED_MOC]] | [[KNOWLEDGE_MOC]]
