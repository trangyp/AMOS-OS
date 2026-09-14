---
title: Portable Agent Authorization Registry Extension
type: registry-extension
origin_architect: Trang Phan
epistemic_class: AMOS_MODEL
---

Register `amos-portable-agent-authorization` as a T1 local verifier bound to [[14_TOOLS/PORTABLE_AGENT_AUTHORIZATION_VERIFIER]].

Capability mask:
`PORTABLE_AUTH_OBJECT_VALIDATE | AUTH_OBJECT_HASH_VERIFY | AUTH_CHAIN_INTEGRITY_VERIFY | DELEGATION_ATTENUATION_VALIDATE | POLICY_REVOCATION_FRESHNESS_CHECK | PREFLIGHT_AUTH_DECIDE | COMMIT_TIME_AUTH_REVALIDATE | CUMULATIVE_CHAIN_USE_RESERVE_LOCAL | AUTH_DECISION_RECEIPT_VALIDATE | AUTH_LEDGER_VERIFY`

The registry entry grants no external execution, merge, deployment, canonical-promotion, identity-provider, cryptographic-verification, or effect-commit authority.
