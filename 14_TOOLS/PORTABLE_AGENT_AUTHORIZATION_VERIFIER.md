---
title: AMOS Portable Agent Authorization Verifier
type: tool
tier: T1
origin_architect: Trang Phan
epistemic_class: AMOS_MODEL
---

# AMOS Portable Agent Authorization Verifier

Local deterministic verifier for issuer-bound authorization objects, only-tightening delegation and commit-time freshness evidence.

## Operations

- `PORTABLE_AUTH_OBJECT_VALIDATE`
- `AUTH_OBJECT_HASH_VERIFY`
- `AUTH_CHAIN_INTEGRITY_VERIFY`
- `DELEGATION_ATTENUATION_VALIDATE`
- `POLICY_REVOCATION_FRESHNESS_CHECK`
- `PREFLIGHT_AUTH_DECIDE`
- `COMMIT_TIME_AUTH_REVALIDATE`
- `CUMULATIVE_CHAIN_USE_RESERVE_LOCAL`
- `AUTH_DECISION_RECEIPT_VALIDATE`
- `AUTH_LEDGER_VERIFY`

Implementation:
`07_SKILLS/amos-portable-agent-authorization-rscf/scripts/portable_authorization.py`

Receipt verifier:
`07_SKILLS/amos-portable-agent-authorization-rscf/scripts/audit_rscf.py`

## Boundaries

- T1 local SQLite state mutation models authorization reservation only; it is not an external-world effect.
- `IDENTITY != AUTHORIZATION`.
- `CAPABILITY != AUTHORITY`.
- `AUTHENTICATION != AUTHORIZATION`.
- `DELEGATION != AUTHORITY_CREATION`.
- `PREFLIGHT_ALLOW != COMMIT_TIME_ALLOW`.
- `AUTHORIZATION_DECISION != ENFORCEMENT`.
- `AUTHORIZATION_DECISION != COMMIT_AUTHORITY`.
- `SIGNATURE_VERIFIED != POLICY_VALID`.
- `POLICY_ALLOW != EFFECT_COMMITTED`.
- External identity providers, cryptographic verifiers, policy engines and effect executors remain separately governed T3/T4 dependencies when actually invoked.
