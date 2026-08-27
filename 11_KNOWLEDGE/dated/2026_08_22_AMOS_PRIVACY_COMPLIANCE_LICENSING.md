---
title: "AMOS Privacy Compliance Licensing"
created: "2026-08-22"
type: note
tags: [canon-group/human-system, canon/framework, rscf/claim, rscf/provenance, rscf/state/observation, topic/amos-privacy-compliance, dated, dated/2026-08-22]
status: "living"
provenance: "MODEL"
confidence: "VERIFIED"
---


# AMOS Privacy, Compliance & Licensing (Gaps 258-269)

> Epistemic class: MODEL (code artifact + test verification).
> Related: 2026-08-22 AMOS Uncertainty Calibration · 2026-08-22 AMOS Adversarial Robustness · amos-completion-graph-workflow

## Summary

Closed gaps 258-269 by implementing the **Privacy, Compliance & Licensing**
governance module (`amos/governance/privacy_compliance.py`). This is the 19th
governance gate in `AmosKernel.run()`, evaluated post-execution.

## 12 Subsystems

| Gap | Subsystem | Class | Purpose |
|-----|-----------|-------|---------|
| 258 | Consent lifecycle | `ConsentLifecycleManager` | Consent grant/withdraw/expire |
| 259 | Purpose limitation | `PurposeLimitationEnforcer` | Purpose limitation enforcement |
| 260 | Data minimization | `DataMinimizationEngine` | Data minimization assessment |
| 261 | Right-to-delete | `RightToDeleteManager` | Right-to-delete mechanics |
| 262 | Deletion-audit conflict | `DeletionAuditResolver` | Deletion vs audit retention conflict |
| 263 | Data residency | `DataResidencyManager` | Data residency + cross-border transfer |
| 264 | Jurisdiction engine | `JurisdictionEngine` | Jurisdiction registration + deadlines |
| 265 | Compliance policy | `CompliancePolicyCompiler` | Compliance policy compilation |
| 266 | Regulatory change | `RegulatoryChangeMonitor` | Regulatory change monitoring |
| 267 | Licensing/IP | `LicensingIPTracker` | Licensing/IP lineage tracking |
| 268 | Derivative work | `DerivativeWorkTracker` | Derivative work tracking |
| 269 | Export control | `ExportControlChecker` | Export-control/sanctions checks |

## Gate Evaluation

`PrivacyComplianceGovernor.evaluate_post()` returns 12 gate results:
- `privacy-258-consent-lifecycle` — FAIL if withdrawn, CONDITIONAL if expired
- `privacy-259-purpose-limitation` — CONDITIONAL if incompatible purposes
- `privacy-260-data-minimization` — CONDITIONAL if excess data
- `privacy-261-right-to-delete` — CONDITIONAL if blocked requests
- `privacy-262-deletion-audit-conflict` — CONDITIONAL if unresolved conflicts
- `privacy-263-data-residency` — CONDITIONAL if unapproved transfers
- `privacy-264-jurisdiction-unregistered` — CONDITIONAL if no jurisdictions registered
- `privacy-265-compliance-policy` — CONDITIONAL if non-compliant policies
- `privacy-266-regulatory-change` — CONDITIONAL if unassessed changes
- `privacy-267-unlicensed-artifact` — CONDITIONAL if unlicensed artifacts
- `privacy-268-derivative-work` — CONDITIONAL if incompatible derivative works
- `privacy-269-export-control` — FAIL if denied, CONDITIONAL if sanctioned

## Key Semantics

1. **Consent states**: PENDING → GRANTED → WITHDRAWN/EXPIRED
2. **Export control status**: APPROVED, RESTRICTED, DENIED, REQUIRES_LICENSE, UNDER_REVIEW
3. **Empty state behavior**: Jurisdiction and licensing gates return CONDITIONAL when empty (no records = unregistered/unlicensed)
4. **Cross-border transfer**: Auto-approved if no cross-border; requires explicit approval otherwise
5. **Governor attribute names**: `consent`, `purpose`, `minimization`, `right_to_delete`, `deletion_conflict`, `residency`, `jurisdiction`, `compliance`, `regulatory`, `licensing`, `derivative`, `export_control`
6. **API pattern**: All subsystems use `record()` to create entries, plus domain-specific methods like `grant()`, `withdraw()`, `complete()`, `block()`, `resolve()`
7. **PrivacyConsentManager alias**: `PrivacyConsentManager = ConsentLifecycleManager` to avoid conflict with `ConsentManager` from `human_interaction` module

## Implementation Chain

- **Types**: `amos/core/types.py` — 11 dataclasses + 8 enums
- **Schema**: `amos/state/store.py` — 11 tables + 11 put/list method pairs
- **Module**: `amos/governance/privacy_compliance.py` — 12 subsystems + governor
- **Kernel**: `amos/kernel.py` — import, instantiation, gate evaluation
- **Exports**: `amos/__init__.py` — all types + `PrivacyComplianceGovernor`
- **Tests**: `tests/test_privacy.py` — 42 tests
- **Seeder**: `amos/governance/seed_completion.py` — gaps 258-269 in CLOSED_CLUSTERS

## Completion Graph Impact

- **Closed gaps**: 167 → 179 (gaps 258-269 = 12 gaps closed)
- **Open gaps**: 63 → 51
- **Total tests**: 1118 → 1160 (42 new tests)
- **All 1160 tests pass**

## External References

- **GDPR Art. 7**: Consent lifecycle (grant/withdraw as easy as grant)
- **GDPR Art. 17**: Right to erasure
- **CCPA**: Right to delete, 45-day DSR deadline
- **Open source frameworks**: ConsentOS, OpenFGC, django-compliance-shield, effaced
- **COSMO Privacy Policy**: `PRIVACY_POLICY.md` — audio telemetry, journaling, GDPR/CCPA rights

## Lessons Learned

1. **Naming conflicts**: `ConsentManager` already exists in `human_interaction`. Use `PrivacyConsentManager` alias for the privacy module.
2. **Empty state semantics**: Some gates (jurisdiction, licensing) return CONDITIONAL on empty state — "unregistered" is not "clean". Tests must pre-register to get PASS.
3. **User's API pattern**: The user uses `record()` as the universal creation method, not `register()` or `grant()`. Domain-specific methods like `grant()`, `withdraw()` are state transitions on existing records.
4. **Gate naming**: The user uses numbered gate names like `privacy-258-consent-lifecycle`, `privacy-259-purpose-limitation`, etc.

---
**Links:** [[DATED_MOC]] | [[KNOWLEDGE_MOC]]
