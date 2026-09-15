---
title: AMOS Managed Autonomy Registry Extension
type: registry-extension
origin_architect: Trang Phan
epistemic_class: AMOS_MODEL
---

# Managed Autonomy Registry Extension

Candidate registry row:

| Tool ID | Entry File | Tier | Capability Mask | Resource Bound | Executed Evidence |
| :--- | :--- | :--- | :--- | :--- | :--- |
| `amos-managed-autonomy-lifecycle` | `14_TOOLS/MANAGED_AUTONOMY_LIFECYCLE_VERIFIER.md` | T1 | `AUTONOMY_LIFECYCLE_CREATE_LOCAL | AUTONOMY_EVIDENCE_RECORD_LOCAL | AUTONOMY_TRANSITION_DECIDE | AUTONOMY_TRANSITION_APPLY_LOCAL | AUTONOMY_FENCE_VERIFY | AUTONOMY_RECOVERY_BUDGET_VERIFY | AUTONOMY_DECISION_RECEIPT_VALIDATE | AUTONOMY_LEDGER_VERIFY` | bounded local SQLite/reference validation | 24-case regression suite + runtime/receipt self-tests; no external response/execution authority |

`REGISTRY_ENTRY != DEPLOYMENT`. `LIFECYCLE_DECISION != EXECUTION_AUTHORITY`.
