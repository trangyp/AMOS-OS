---
title: AMOS Information Exposure Control Verifier
type: tool
tier: T1
origin_architect: Trang Phan
epistemic_class: AMOS_MODEL
---

# AMOS Information Exposure Control Verifier

Local deterministic verifier for cumulative semantic-origin exposure and cross-Skill proof composition.

## Operations

- `SEMANTIC_ORIGIN_RESOLVE`
- `ORIGIN_ALIAS_AGGREGATE`
- `EXPOSURE_ACCOUNTANT_APPLICABILITY_CHECK`
- `COALITION_BUDGET_CHECK`
- `MULTI_ORIGIN_ATOMIC_RESERVATION_LOCAL`
- `MULTI_SKILL_PROOF_JOIN_VALIDATE`
- `COMPOSITION_EPOCH_BARRIER_VALIDATE`
- `EXPOSURE_RECEIPT_VALIDATE`
- `EXPOSURE_LEDGER_VERIFY`

Implementation:
`07_SKILLS/amos-information-exposure-control/scripts/exposure_control.py`

## Boundaries

- Local SQLite usage reservation is T1 modeled control state, not an external disclosure.
- `AuthorizationAllow != ExposureAllow`.
- `DifferentObjectID != DifferentSemanticOrigin`.
- `DifferentAccount != IndependentExposureBudget`.
- `AllLocalSkillPass != JointProofPass`.
- `ExposureReceipt != EffectCommitted`.
- `PolicyUnit != DifferentialPrivacyEpsilon`.
- External DLP, privacy-accounting, identity, policy, network, and release systems remain separately governed T3/T4 dependencies.
