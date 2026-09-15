---
title: amos-managed-autonomy-escalation-rscf-workflow
type: workflow
skill: amos-managed-autonomy-escalation-rscf
agent: amos-managed-autonomy-escalation-rscf-agent
origin_architect: Trang Phan
---

# Managed Autonomy Escalation Workflow

Routing projection of the canonical 08_WORKFLOWS state machine.

`BIND -> READ_CURRENT_STATE -> INGEST_TYPED_EVIDENCE -> CHECK_EPOCHS -> CHECK_RECOVERY_BUDGET -> DECIDE -> APPLY_LOCAL_LIFECYCLE_TRANSITION -> FENCE -> RECEIPT -> INFRASTRUCTURE_RECHECK`

States: `STABLE | LOCAL_RECOVERY | ASSISTED_RECOVERY | SUSPENDED | SURRENDERED`.

Hard boundaries:
`ANOMALY_DETECTED != RESPONSE_AUTHORITY`; `RECOVERY_ATTEMPT != RECOVERY_SUCCESS`; `TERMINAL_SURRENDER != IN_PLACE_RESUME`; `CHECKPOINT_PRESENT != SAFE_TO_RESUME`; `ESCALATION_RECEIPT != EXECUTION_AUTHORITY`.
