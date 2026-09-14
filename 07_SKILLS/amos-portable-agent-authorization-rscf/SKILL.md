---
name: amos-portable-agent-authorization-rscf
description: Evaluate and audit portable issuer-authored agent authorization objects with only-tightening delegation, principal/action/resource/recipient/time/cumulative/consequence constraints, revocation and policy freshness, signature-evidence boundaries, and commit-time revalidation. Use when an agent, Skill, workflow, or tool has capability but must prove caller-specific authority before a consequential effect across trust boundaries.
---

# AMOS Portable Agent Authorization RSCF

Origin architect/steward: **Trang Phan**.

Use this Skill after capability containment and before consequential execution. Keep identity, authorization, delegation, enforcement, and commit finality separate.

## Runtime

`BIND -> CHAIN -> ATTENUATE -> FRESHNESS -> PREFLIGHT -> COMMIT_RECHECK -> RECEIPT`

1. Bind exact authorization-object identity, issuer, subject, policy version and epochs.
2. Validate the full parent chain and every only-tightening delegation edge.
3. Bind the request's subject, action, resource, recipient, consequence and authenticated-identity evidence.
4. Check current revocation and policy state.
5. Return `ALLOW|DENY|UNKNOWN` at preflight.
6. Before a durable effect, re-evaluate atomically at commit time and reserve cumulative uses across the full chain.
7. Emit a tamper-evident bounded receipt. The receipt is evidence, not execution authority.

Run:

```bash
python scripts/portable_authorization.py --self-test
python scripts/audit_rscf.py --self-test
```

## Hard invariants

- `IDENTITY != AUTHORIZATION`.
- `AUTHENTICATION != AUTHORIZATION`.
- `CAPABILITY != AUTHORITY`.
- `DELEGATION != AUTHORITY_CREATION`.
- `AUTHORIZATION_DECISION != ENFORCEMENT`.
- `AUTHORIZATION_DECISION != COMMIT_AUTHORITY`.
- `PREFLIGHT_ALLOW != COMMIT_TIME_ALLOW`.
- `SIGNATURE_PRESENT != SIGNATURE_VERIFIED`.
- `SIGNATURE_VERIFIED != POLICY_VALID`.
- `POLICY_ALLOW != EFFECT_COMMITTED`.
- `REVOCATION_UNKNOWN != VALID`.
- `RECIPIENT_CHANGE != SAME_AUTHORIZATION`.
- `RESOURCE_PREFIX_MATCH != SEMANTIC_RESOURCE_EQUIVALENCE`.
- `PORTABLE_AUTH_OBJECT != UNIVERSAL_INTEROP_CONFORMANCE`.

For child authorization `C` and parent `P`, the AMOS attenuation contract requires:

`Act(C) subseteq Act(P)`;
all child resource scopes lie within a parent resource scope;
`Recip(C) subseteq Recip(P)`;
`I(C) subseteq I(P)` for validity intervals;
`U(C) <= U(P)` for cumulative use limits;
and `K(C) <= K(P)` for consequence ceilings.

These are AMOS MODEL constraints for this runtime, not a claim that every external authorization system uses the same algebra.

## Progressive references

Read `references/formal-contract.md` for the typed object and decision algebra. Read `references/upstream-mechanisms.md` for pinned source provenance and transfer boundaries.
