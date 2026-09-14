---
name: amos-information-exposure-control
description: Govern cumulative information exposure across AMOS agents, sessions, aliases, semantic origins, transformations, recipients, coalitions, time, and composed Skills. Use when individually allowed disclosures may compose into unsafe reconstruction; when declassification, privacy/exposure budgets, semantic-origin resolution, multi-origin derivations, accountant applicability, atomic exposure reservation, cross-Skill proof joins, or commit-time revalidation must be enforced by the AMOS infrastructure control plane rather than by a model worker.
---

# AMOS Information Exposure Control

Origin architect/steward: **Trang Phan**.

Place this control after caller-specific authorization and before an externally visible release.

## Runtime

`BIND_EFFECT -> RESOLVE_ORIGINS -> AGGREGATE -> ACCOUNTANT_GATE -> BUDGET_GATE -> PROOF_JOIN -> COMMIT_RECHECK -> ATOMIC_RESERVE -> RECEIPT`

1. Bind the exact effect, semantic transaction, authorization receipt, environment, policy and capability-contract identities.
2. Resolve every object/alias to a canonical semantic origin. Unresolved origin identity is `REVALIDATE_ORIGIN`.
3. Aggregate repeated aliases of the same semantic origin before accounting.
4. Charge every load-bearing origin in a multi-origin derivation.
5. Use only a declared accountant whose unit semantics and validity envelope match the release. This reference runtime implements exact integer `POLICY_UNIT_SUM`; it does not treat policy units as differential-privacy epsilon.
6. Evaluate exposure against the recipient coalition, not account/session aliases. Changing an account, session or window does not reset cumulative exposure.
7. Validate every required specialist proof under one effect/policy/authority/environment/capability/proof epoch.
8. Re-read control state immediately before commit and atomically reserve all origin charges.
9. Emit a tamper-evident receipt. `COMMITTABLE_EXPOSURE` is evidence for the infrastructure control plane, not commit authority itself.

Run:

```bash
python scripts/exposure_control.py --self-test
python scripts/validate_exposure_control.py --self-test
python scripts/validate_multi_skill_join.py --self-test
```

## Hard invariants

- `DifferentObjectID != DifferentSemanticOrigin`.
- `DifferentAccount != IndependentExposureBudget`.
- `DifferentSession != ExposureReset`.
- `LocalDeclassificationPass != CompositionPass`.
- `AccountantOutput != AccountantApplicability`.
- `AccountantAgreement != AccountantCorrectness`.
- `AuthorizationAllow != ExposureAllow`.
- `SkillPassToken != CommitAuthority`.
- `AllLocalSkillPass != JointProofPass`.
- `MissingRequiredProof != OptionalProof`.
- `MixedEpochProofs != OneAuthoritativeSnapshot`.
- `MultiOriginRelease -> AtomicReservation(all load-bearing origins)`.
- `ExposureReceipt != EffectCommitted`.
- `PolicyUnit != DifferentialPrivacyEpsilon`.

For a release with canonical origins `O` and coalition `c`, exact policy-unit accounting is:

`Used'_o,c = Used_o,c + Charge_o` for every `o in O`,

subject to:

`Used_o,c + Charge_o <= Limit_o,c` for every `o in O`.

The update is one SQLite transaction. If any origin fails, no origin is charged.

## Progressive references

Read `references/control-contract.md` for the typed runtime and proof-join contract. Read `references/upstream-mechanisms.md` for pinned GitHub provenance and transfer limits.
