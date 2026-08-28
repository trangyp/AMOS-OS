---
title: 2026 08 22 GOVERNANCE ARCHITECTURE DECOMMISSIONING
tags: [dated, dated/2026-08-22, canon/knowledge]
type: document
source: 11_KNOWLEDGE/dated
rscf:
  state: SOURCE_CLAIM
  claim_class: SOURCE_CLAIM
  provenance: AMOS_corpus
  scope: temporal_log
---


# 2026-08-22 Governance Architecture & Decommissioning

## Summary
Closed gap cluster 280-290 (Governance Architecture & Decommissioning) — 11 gaps, 11 store methods, 1 governance module, 1 governor, 58 tests.

## Gaps Closed (280-290)
- 280 GovernanceSuccessionPlanner — governance succession (planned/active/completed/failed)
- 281 SeparationOfPowersChecker — separation of powers (legislative/executive/judicial/audit/emergency)
- 282 InsiderThreatMonitor — insider-threat model (none/low/medium/high/critical)
- 283 TwoPersonControlChecker — two-person control (verified/pending/failed/not_required)
- 284 GovernanceCaptureChecker — capture resistance (resistant/vulnerable/compromised/not_assessed)
- 285 VendorDependencyMapper — vendor dependency (none/low/medium/high/critical)
- 286 VendorExitPlanner — vendor exit (not_planned/planned/in_progress/completed/blocked)
- 287 DegradedOperationMonitor — degraded operation (normal/degraded/offline/emergency)
- 288 BusinessContinuityChecker — business continuity (active/recovering/degraded/interrupted/not_tested)
- 289 DecommissioningProtocol — decommissioning (active/scheduled/in_progress/completed/blocked)
- 290 OrphanStateHandler — orphan state (resolved/orphaned/adopted/quarantined)

## Files Created/Modified
- `amos/governance/governance_architecture.py` (new, 1066 lines) — 11 subsystems + GovernanceArchitectureGovernor
- `amos/state/store.py` — fixed 3 column count mismatches (governance_capture, vendor_dependency, degraded_operation)
- `tests/test_governance_architecture.py` (new, 373 lines, 58 tests)
- `amos/governance/seed_completion.py` — moved governance_architecture to CLOSED_CLUSTERS (200 closed, 30 open)
- `tests/test_completion.py` — updated counts (200 closed, 30 open)
- `AGENTS.md` — updated test count to 1405, added governance_architecture to file tree
- `global_rules.md` — updated test count, gate list, completion graph counts, closed clusters list
- `.devin/skills/amos-governance-architecture/SKILL.md` — new skill file
- `.devin/skills/amos-completion-graph-workflow/SKILL.md` — updated counts

## Key Learnings
1. **Store method naming**: The store uses singular form for some list methods (`list_governance_succession`, `list_business_continuity`, `list_decommissioning`, `list_governance_capture`) — always grep the actual method names before writing the governance module.
2. **Column count mismatch is #1 bug**: 3 of 11 store methods had column count mismatches in INSERT statements vs CREATE TABLE. Always count columns carefully.
3. **Aliases for __init__.py**: The `amos/__init__.py` may use different class names than the governance module (e.g., `GovernanceSuccessionTracker` vs `GovernanceSuccessionPlanner`, `InsiderThreatModeler` vs `InsiderThreatMonitor`, `DegradedOperationManager` vs `DegradedOperationMonitor`). Add backward-compatible aliases at the end of the module.
4. **GateResult pattern**: Each subsystem contributes one gate to `evaluate_post()`. FAIL for critical issues (failed, compromised, blocked, offline, interrupted), CONDITIONAL for warnings (unplanned, vulnerable, pending, degraded, not_tested, orphaned), PASS for clean state.
5. **Empty-store semantics**: For "has_X" checks that mean "not yet set up" (has_unplanned, has_not_planned, has_not_tested, has_unassessed), return True when the store is empty — this surfaces the gap as a CONDITIONAL gate.

## Test Results
- 58 new tests in `test_governance_architecture.py` — all pass
- Full suite: 1405 tests pass (was 1347)
- No regressions

## Completion Graph Status
- 200 closed gaps (91-290) across 21 clusters
- 30 open gaps (291-320) across 2 clusters
- 3 unknown-unknowns
- 19 cognitive matrix gaps (321-339)

---
**Related:** [[00_HOME]] · [[KNOWLEDGE_MOC]] · [[AMOS_SIMULATION_KERNEL_V0_MATH_FOUNDATIONS]] · [[SYSTEM_SCAN_AGENT]] · [[AUTOMATION_PROFILES]]

---
**MOC:** [[DATED_MOC]]
