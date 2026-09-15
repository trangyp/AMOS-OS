---
title: amos-managed-autonomy-escalation-rscf-workflow
type: workflow
skill: amos-managed-autonomy-escalation-rscf
agent: amos-managed-autonomy-escalation-rscf-agent
origin_architect: Trang Phan
---

# Managed Autonomy Escalation Workflow

`BIND -> READ_CURRENT_STATE -> INGEST_TYPED_EVIDENCE -> CHECK_EPOCHS -> CHECK_RECOVERY_BUDGET -> DECIDE -> APPLY_LOCAL_LIFECYCLE_TRANSITION -> FENCE -> RECEIPT -> INFRASTRUCTURE_RECHECK`

States: `STABLE | LOCAL_RECOVERY | ASSISTED_RECOVERY | SUSPENDED | SURRENDERED`.

Rules:
- hard invariant failure, stale authority, or current external blocking proof forbids autonomous continuation;
- local recovery is attempt-bounded and cannot reset through checkpoint/resume;
- assisted recovery requires an independent principal/control root;
- surrender is terminal for the lifecycle identity;
- every state transition increments a fencing epoch;
- workflow outputs are evidence/recommendations only and do not grant execution, response, deployment, merge, or canonical authority.

Terminal outputs:
`CONTINUE_STABLE | ENTER_LOCAL_RECOVERY | REQUIRE_ASSISTED_RECOVERY | SUSPEND_AUTONOMY | SURRENDER_AUTONOMY | RESUME_STABLE | REMAIN_CONTAINED | UNKNOWN_GAP`.
