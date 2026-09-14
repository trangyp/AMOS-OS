---
title: amos-information-exposure-control-workflow
type: workflow
skill: amos-information-exposure-control
agent: amos-information-exposure-control-agent
origin_architect: Trang Phan
epistemic_class: AMOS_MODEL
---

# Information Exposure Control Workflow

`BIND_EFFECT -> AUTH_RECEIPT -> RESOLVE_ORIGINS -> AGGREGATE_ALIASES -> ACCOUNTANT_GATE -> COALITION_BUDGET_GATE -> REQUIRED_PROOF_JOIN -> COMMIT_RECHECK -> ATOMIC_RESERVATION -> RECEIPT`

## Preconditions

- Caller-specific authorization evidence exists but is not treated as exposure approval.
- Effect, semantic transaction, environment, policy, capability-contract and proof epoch identities are frozen.
- Every disclosure component can be mapped to a semantic-origin reference or the workflow stops at `REVALIDATE_ORIGIN`.

## Gates

1. **Origin gate** — resolve aliases/object IDs to canonical origins and aggregate duplicates.
2. **Accountant gate** — require current supported accountant identity; reference runtime supports only integer `POLICY_UNIT_SUM`.
3. **Coalition gate** — bind recipients to policy coalition; account/session changes do not create new budgets.
4. **Budget gate** — every canonical origin must remain within its coalition budget.
5. **Proof join gate** — all required specialist proofs must PASS under one exact effect/policy/authority/environment/capability/proof epoch.
6. **Commit gate** — re-read control state under transaction and reserve every canonical origin atomically.
7. **Receipt gate** — emit bounded tamper-evident evidence. Receipt is not external effect authority.

## Terminal states

`COMMITTABLE_EXPOSURE | REVALIDATE_ORIGIN | REVALIDATE_ACCOUNTANT | REVALIDATE_MISSING_PROOF | REVALIDATE_PROOF_JOIN | BLOCK_BUDGET | DENY_POLICY | UNKNOWN_GAP`

No terminal state grants merge, deployment, canon, or external-effect authority.
