# Distributed Attack Composition Registry Extension

Candidate T1 row for `TOOL_REGISTRY_MASTER`:

`amos-distributed-attack-composition` | `DISTRIBUTED_ATTACK_COMPOSITION_VERIFIER` | T1 | `COMPOSITION_EVENT_VALIDATE | COMPOSITION_RULE_VALIDATE | LOCAL_ALLOW_FILTER | TEMPORAL_WINDOW_APPLY | POLICY_EPOCH_COMPATIBILITY_CHECK | CROSS_EVENT_ATOM_COMPOSE | MINIMAL_SATISFYING_EVENT_CUT | COMPOSITION_RECEIPT_VALIDATE | COMPOSITION_LEDGER_VERIFY` | bounded local SQLite/reference validation | 24-case regression suite + runtime/receipt self-tests; no response or effect authority.

`REGISTRY_EXTENSION != DEPLOYMENT`.
