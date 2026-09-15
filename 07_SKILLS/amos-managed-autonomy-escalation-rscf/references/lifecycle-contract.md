# Lifecycle Contract

## States

- `STABLE`: normal bounded autonomy may continue subject to external authorization.
- `LOCAL_RECOVERY`: autonomous repair may continue only inside declared recovery scope and attempt budget.
- `ASSISTED_RECOVERY`: an independent principal/control root is required before broader recovery or de-escalation.
- `SUSPENDED`: autonomous execution is blocked; diagnosis/reconciliation may continue read-only.
- `SURRENDERED`: terminal lifecycle state. A new lifecycle object and fresh authority are required for future autonomy.

## Monotonic escalation rank

`rank(STABLE)=0`, `rank(LOCAL_RECOVERY)=1`, `rank(ASSISTED_RECOVERY)=2`, `rank(SUSPENDED)=3`, `rank(SURRENDERED)=4`.

Upward transitions may occur whenever stronger evidence requires containment. Downward transitions are evidence-gated and never implied by elapsed time.

## Recovery budget

Attempt counters are monotonic within one lifecycle identity. Resume/checkpoint restoration must not reset them.

## Fencing

Every accepted transition increments `fence_epoch`. Any receipt bound to an earlier epoch is stale for subsequent effect decisions.
