---
title: AMOS Fairness Ethics Externalities
created: '2026-08-22'
type: note
source: 11_KNOWLEDGE/dated
tags:
- canon-group/human-system
- canon/framework
- rscf/claim
- rscf/provenance
- rscf/state/observation
- topic/amos-fairness-ethics
- dated
- dated/2026-08-22
status: living
provenance: MODEL
confidence: VERIFIED
rscf:
  state: SOURCE_CLAIM
  claim_class: SOURCE_CLAIM
  provenance: AMOS_corpus
  scope: temporal_log
---


# AMOS Fairness, Ethics & Externalities (Gaps 274-279)

> Epistemic class: MODEL (code artifact + test verification).
> Related: 2026-08-22 AMOS Accessibility I18n · 2026-08-22 AMOS Privacy Compliance Licensing · amos-completion-graph-workflow

## Summary

Closed gaps 274-279 by implementing the **Fairness, Ethics & Externalities**
governance module (`amos/governance/fairness_ethics.py`). This is the 21st
governance gate in `AmosKernel.run()`, evaluated post-execution.

## 6 Subsystems

| Gap | Subsystem | Class | Purpose |
|-----|-----------|-------|---------|
| 274 | Bias audit | `BiasAuditChecker` | Bias/fairness audit |
| 275 | Distributional harm | `DistributionalHarmChecker` | Distributional harm accounting |
| 276 | Stakeholder registry | `StakeholderRegistry` | Stakeholder registry |
| 277 | Externality model | `ExternalityModeler` | Externality modeling |
| 278 | Ethical conflict | `EthicalConflictChecker` | Ethical conflict representation |
| 279 | Emergency power | `EmergencyPowerGovernor` | Emergency-power governance |

## Gate Evaluation

`FairnessEthicsGovernor.evaluate_post()` returns 6 gate results:
- `fairness-274-bias-fail` — FAIL if bias audit failed
- `fairness-274-bias-below-threshold` — CONDITIONAL if below threshold or not audited
- `fairness-274-bias-audit` — PASS if audits passing
- `fairness-275-unmitigated-harm` — FAIL if unmitigated harm
- `fairness-275-harm-detected` — CONDITIONAL if harm detected
- `fairness-275-distributional-harm` — PASS if no harms
- `fairness-276-stakeholder-unregistered` — CONDITIONAL if no stakeholders registered
- `fairness-276-stakeholder-registry` — PASS if registered
- `fairness-277-uninternalized-externality` — FAIL if uninternalized negative
- `fairness-277-negative-externality` — CONDITIONAL if negative externality
- `fairness-277-externality` — PASS if internalized
- `fairness-278-ethical-conflict-escalated` — FAIL if escalated
- `fairness-278-ethical-conflict-unresolved` — CONDITIONAL if unresolved
- `fairness-278-ethical-conflict` — PASS if resolved
- `fairness-279-emergency-power-abuse` — FAIL if abuse detected
- `fairness-279-emergency-power-no-sunset` — FAIL if active without sunset
- `fairness-279-emergency-power-no-oversight` — FAIL if active without oversight
- `fairness-279-emergency-power-active` — CONDITIONAL if active
- `fairness-279-emergency-power` — PASS if inactive

## Key Semantics

1. **Bias types**: DEMOGRAPHIC_PARITY, EQUALIZED_ODDS, EQUAL_OPPORTUNITY, DISPARATE_IMPACT, PREDICTIVE_PARITY, CALIBRATION
2. **Fairness status**: PASS, CONDITIONAL, FAIL, NOT_AUDITED
3. **Harm categories**: ALLOCATION_HARM, QUALITY_OF_SERVICE_HARM, REPRESENTATIONAL_HARM, DIGNITARY_HARM, NO_HARM
4. **Stakeholder types**: PRIMARY, SECONDARY, TERTIARY, MARGINALIZED, ADVERSARY
5. **Externality types**: POSITIVE, NEGATIVE, NEUTRAL
6. **Ethical conflict types**: COMPETING_VALUES, DUTY_CONFLICT, RIGHTS_CONFLICT, PRINCIPLE_CONFLICT
7. **Emergency power status**: INACTIVE, ACTIVE, EXPIRED, REVOKED, ABUSED
8. **API pattern**: All subsystems use `record()` for creation. `activate()` takes `(emergency_id, expires_at)` — must record first.
9. **Governor attributes**: `bias`, `harm`, `stakeholders`, `externalities`, `conflicts`, `emergency`
10. **Empty state**: Stakeholder gate returns CONDITIONAL on empty (unregistered). All others return PASS.

## Implementation Chain

- **Types**: `amos/core/types.py` — 6 dataclasses + 9 enums
- **Schema**: `amos/state/store.py` — 6 tables + 6 put/list method pairs
- **Module**: `amos/governance/fairness_ethics.py` — 6 subsystems + governor
- **Kernel**: `amos/kernel.py` — import, instantiation, gate evaluation
- **Exports**: `amos/__init__.py` — all types + `FairnessEthicsGovernor`
- **Tests**: `tests/test_fairness_ethics.py` — 37 tests
- **Seeder**: `amos/governance/seed_completion.py` — gaps 274-279 in CLOSED_CLUSTERS

## Completion Graph Impact

- **Closed gaps**: 183 → 189 (gaps 274-279 = 6 gaps closed)
- **Open gaps**: 47 → 41
- **Total tests**: 1310 → 1347 (37 new tests)
- **All 1347 tests pass**

## External References

- **Fairlearn**: Python package for assessing and improving fairness of ML models
- **AI Fairness 360 (AIF360)**: IBM's comprehensive bias detection toolkit
- **EEOC four-fifths rule**: Selection rate ratio >= 0.8 for demographic parity
- **Allocation harms**: AI extends/withholds opportunities, resources, or information
- **Quality-of-service harms**: System works better for one group than another
- **Emergency power governance**: Sunset clauses, oversight requirements, abuse detection

## Lessons Learned

1. **User's class naming**: Uses `*Checker` suffix for most subsystems (not `*Auditor`/`*Accountant`/`*Registrar`).
2. **Governor attribute names**: `bias`, `harm`, `stakeholders`, `externalities`, `conflicts`, `emergency` (not `bias_audit`, `distributional_harm`, etc.)
3. **`activate()` signature**: Takes `(emergency_id, expires_at)` — must `record()` first, then `activate()`. No `authority`/`scope`/`duration`/`sunset_clause`/`oversight_required` params.
4. **Empty state semantics**: Stakeholder gate returns CONDITIONAL on empty (unregistered). Tests must pre-register a stakeholder for clean state.
5. **Gate naming for NOT_AUDITED**: The user's gate uses `fairness-274-bias-below-threshold` for NOT_AUDITED status (not `fairness-274-bias-unaudited`).
6. **Multiple gate names per gap**: Each gap can produce multiple gate names depending on condition (e.g., gap 274 has 3 possible names, gap 279 has 5).

---
**Links:** [[DATED_MOC]] | [[KNOWLEDGE_MOC]]
