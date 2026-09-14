---
title: AMOS Distributed Attack Composition Verifier
type: tool
tier: T1
origin_architect: Trang Phan
epistemic_class: AMOS_MODEL
---

# AMOS Distributed Attack Composition Verifier

Local deterministic verifier for bounded cross-event composition rules.

Operations:
- `COMPOSITION_EVENT_VALIDATE`
- `COMPOSITION_RULE_VALIDATE`
- `LOCAL_ALLOW_FILTER`
- `TEMPORAL_WINDOW_APPLY`
- `POLICY_EPOCH_COMPATIBILITY_CHECK`
- `CROSS_EVENT_ATOM_COMPOSE`
- `MINIMAL_SATISFYING_EVENT_CUT`
- `COMPOSITION_RECEIPT_VALIDATE`
- `COMPOSITION_LEDGER_VERIFY`

Implementation: `07_SKILLS/amos-distributed-attack-composition-monitor-rscf/scripts/composition_monitor.py`.

`BLOCK_COMPOSITION` is a local control-plane recommendation/evidence state. It does not prove malicious intent and does not grant response, rollback, merge, quarantine, or deployment authority.
