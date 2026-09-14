---
title: amos-portable-agent-authorization-rscf-workflow
type: workflow
version: 3.0.0
origin_architect: Trang Phan
epistemic_class: AMOS_MODEL
---

# Workflow: Portable Agent Authorization

`BIND -> OBJECT_INTEGRITY -> CHAIN -> ATTENUATE -> IDENTITY -> FRESHNESS -> PREFLIGHT -> COMMIT_RECHECK -> USAGE_RESERVE -> RECEIPT -> TERMINAL`

## Preconditions
- Bind exact authorization object, issuer, subject, policy identity/version and epochs.
- Bind the request subject/action/resource/recipient/consequence and identity-evidence state.
- Treat external signature verification and workload identity as evidence inputs, not local cryptographic proof.

## Gates
1. Reject authorization-object hash mismatch.
2. Validate every parent-child issuer and only-tightening attenuation edge.
3. Validate identity state without promoting authentication into authorization.
4. Recheck policy/revocation freshness and temporal validity.
5. Produce bounded `ALLOW|DENY|UNKNOWN` preflight evidence.
6. For a modeled commit, rerun all checks inside one immediate local transaction and reserve cumulative uses across the complete chain.
7. Validate the decision receipt hash and invariant semantics.
8. Preserve `PREFLIGHT_ALLOW != COMMIT_TIME_ALLOW` and `AUTHORIZATION_DECISION != COMMIT_AUTHORITY`.

## Terminal semantics
`ALLOW`, `DENY`, and `UNKNOWN` are authorization-evidence states only. None executes an external effect, grants merge/deployment authority, or proves external enforcement occurred.
