# Control contract

## Canonical state

- `origin_id`: canonical semantic origin.
- `alias_id`: object/content/session-visible identifier resolving to one origin.
- `coalition_id`: recipient-equivalence group against which cumulative exposure is charged.
- `limit_units`: non-negative integer policy exposure budget.
- `used_units`: committed cumulative policy exposure units.
- `accountant_kind`: executable reference supports only `POLICY_UNIT_SUM`.
- `policy_id`, `policy_version`, `policy_epoch`, `exposure_epoch`: freshness identity.

## Release binding

A release binds `effect_hash`, `semantic_transaction_hash`, `authorization_receipt_hash`, `environment_hash`, `capability_contract_hash`, coalition, policy identity, proof epoch, and origin charges. Repeated aliases are canonicalized before aggregation.

## Proof join

All required proofs must be present and agree on effect, semantic transaction, policy id/version/epoch, authority, environment, capability contract, and proof epoch. A local PASS token cannot widen authority or substitute for missing proof.

## Result states

`COMMITTABLE_EXPOSURE | REVALIDATE_ORIGIN | REVALIDATE_ACCOUNTANT | REVALIDATE_MISSING_PROOF | REVALIDATE_PROOF_JOIN | BLOCK_BUDGET | DENY_POLICY | UNKNOWN_GAP`
