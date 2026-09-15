---
title: AMOS Managed Autonomy Lifecycle Verifier
type: tool
tier: T1
origin_architect: Trang Phan
epistemic_class: AMOS_MODEL
---

# AMOS Managed Autonomy Lifecycle Verifier

Local deterministic verifier for autonomy-state transitions, recovery budgets, fencing epochs, and terminal surrender semantics.

Operations:
- `AUTONOMY_LIFECYCLE_CREATE_LOCAL`
- `AUTONOMY_EVIDENCE_RECORD_LOCAL`
- `AUTONOMY_TRANSITION_DECIDE`
- `AUTONOMY_TRANSITION_APPLY_LOCAL`
- `AUTONOMY_FENCE_VERIFY`
- `AUTONOMY_RECOVERY_BUDGET_VERIFY`
- `AUTONOMY_DECISION_RECEIPT_VALIDATE`
- `AUTONOMY_LEDGER_VERIFY`

Implementation: `07_SKILLS/amos-managed-autonomy-escalation-rscf/scripts/managed_autonomy.py`.

Boundaries:
`ANOMALY_DETECTED != RESPONSE_AUTHORITY`; `CHECKPOINT_PRESENT != SAFE_TO_RESUME`; `SURRENDERED != PAUSED`; `ESCALATION_RECEIPT != EXECUTION_AUTHORITY`.
