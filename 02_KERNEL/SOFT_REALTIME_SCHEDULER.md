---
canon-group: meta
canon-type: framework
rscf-state: source-claim
rscf-claim: verified
rscf-provenance: AMOS_corpus
conclusion_class: AMOS_MODEL
epistemic_class: SOURCE_CLAIM
topic: Soft Realtime Scheduler
tags:
  - canon-group/tech-ai
  - rscf/claim
  - rscf/provenance
  - rscf/state/source-claim
  - misc
created: 2026-08-22
---
---
---

# SOFT_REALTIME_SCHEDULER — Soft Real-Time Scheduling Kernel

## 1. Role

The Soft Real-Time Scheduler kernel governs how AMOS_OS admits, orders, and dispatches computational work when deadlines are **soft** — meaning a deadline miss degrades quality or imposes bounded cost, but does not constitute a safety-or-integrity failure equivalent to a hard real-time miss. AMOS reasoning, RSCF updates, epoch finalization, and neural grounding are soft real-time workloads: they have freshness bounds, latency targets, and energy budgets, but bounded overrun is tolerable.

The scheduler must reconcile two tensions introduced by the 2026 compute landscape:
1. **Deterministic deadline modeling** for symbolic commit and epoch closing.
2. **Event-driven, energy-proportional execution** on neuromorphic/photonic/spike backends where work cost scales with relevance rather than a constant per-tick load.

## 2. Scheduling Model

### 2.1 Work Item

```
WorkItem {
    id: UUID
    deadline: TIME          // soft deadline
    period: TIME | NULL     // if periodic
    budget: ENERGY          // energy budget for the item
    class: SCHED_CLASS      // NEURAL | SYMBOLIC | EPOCH | COMMIT | RSCF
    release_time: TIME      // earliest start
    partition: UUID         // shard/tier affinity
    priority: INT           // base priority
}
```

### 2.2 Scheduling Classes

| Class | Deadline nature | Determinism | Example |
|-------|-----------------|-------------|---------|
| NEURAL-GROUND | soft, data-dependent | statistical | SNN perception grounding |
| SYMBOLIC-STEP | soft, step-bounded | deterministic | rule application |
| EPOCH-CLOSE | soft-ish, bounded | deterministic | epoch finalization |
| COMMIT | soft, authority-gated | deterministic | CAS commit of a decision |
| RSCF-LOG | soft, low-priority | best-effort | observation logging |

## 3. Mathematical Foundations

### 3.1 Feasibility: Utilization Bound

For a set of periodic soft tasks, a classic sufficient feasibility condition is the utilization bound. For `n` tasks with per-task utilization $U_i = C_i / T_i$ (worst-case compute $C_i$, period $T_i$):

$$
\sum_{i=1}^{n} U_i \le n (2^{1/n} - 1)
\]

When the bound holds, all deadlines are schedulable under RM/EDF under the stated worst-case model. Soft real-time relaxes this: bounded overload is allowed, but an **overload admission policy** decides which tasks degrade.

### 3.2 Overrun / Degradation Policy

Because deadlines are soft, the scheduler selects a degradation function for each item on anticipated miss:
- **Drop** (skip work, mark `DEFERRED`) for low-criticality grounding/logging.
- **Reduce fidelity** (fewer spikes, lower precision) for neural grounding.
- **Defer** (push deadline, keep priority) for symbolic steps that can be rescheduled.
- **Escalate** for items near a safety/authority boundary.

### 3.3 Energy-Proportional Scheduling

For backend models where effort ∝ data relevance (spike density $\lambda$), the *effective* compute budget is:

$$
C_{eff} = \alpha + \beta \cdot \lambda
$$

so the scheduler can admit items whose *expected* utilization — not worst-case — fits the budget, while reserving a worst-case reserve for determinism-critical items. This is a crucial departure from classic hard-RT models and is AMOS-specific given the 2026 substrate shift.

### 3.4 Earliest Deadline First (EDF) Dispatch

At each dispatch, the ready queue is sorted by dynamic deadline; preemptively running the earliest-deadline job is optimal for dynamic-priority soft systems under uniprocessor assumptions. AMOS augments EDF with class-aware energy weighting:

```
priority(wi) = -deadline(wi)  (earlier = higher)
tiebreak(wi,wj): by class criticality, then shard-ID (fairness)
admit(wi): if E_available >= expected_effort(wi): admit; else degrade or defer
```

## 4. Event-Driven (Spike-Aware) Scheduling

### 4.1 Gated Activation

Neuromorphic workloads should not run on a fixed cadence; they activate on `EVENT` arrival (an `OBSERVATION`-grade signal). The scheduler maintains an event→work mapping and only enqueues work when its trigger fires:

```
ON-EVENT(ev):
    for each workItem w in subscribers(ev):
        w.release_time = now
        enqueue(w)

ON-TICK (for periodic/deterministic items only):
    release periodic items, check epoch deadlines
```

### 4.2 Mixed Backend Transparency

Whether the backend is a CPU, GPU, photonic processor (Environment Envise-class), or neuromorphic chip, the scheduler exposes a uniform interface:
`estimate_effort(wi)`, `dispatch(wi)`, `update_budget(aligned)`. Backend-specific energy models plug in below this interface — preserving the soft-RT guarantee above the substrate while optimizing below it.

## 5. AMOS-Specific Constraints

### 5.1 Freshness: Soft Real-Time *Freshness*

AMOS observations and derived claims carry a `freshness` bound: reasoning must occur before the evidence is stale. The scheduler folds freshness into deadline: `deadline(wi) = min(timeliness_bound, freshness_bound)`.

### 5.2 Deterministic Epoch Closing

Epoch closing (see MULTI_EPOCH_COORDINATION) must not starve: it is scheduled with a guaranteed minimum budget so CAS-addressable version vectors advance within a bounded window even under neural overload.

### 5.3 Commit Authority Not Preempted

A `COMMIT` item that has passed COMMIT_GATE must reach its CAS operation within a bounded latency; the scheduler guarantees a commit fast-lane. This preserves K_AUTHORITY determinism even when perceptual load spikes.

### 5.4 Fail-Closed on Miss

If a critical symbolic/commit item cannot be admitted within its freshness bound, the scheduler fails closed (K_FAIL_CLOSED): it does not silently drop the item; it escalates to the authority/recovery plane with a `DEFERRED_BY_SCHEDULER` receipt.

## 6. Admission Control

```
ADMIT(wi):
    effort = estimate_effort(wi)          # backend-specific (maybe energy-prop.)
    if not enough_budget(wi) :
        deg = select_degradation(wi)      # drop|reduce|defer|escalate
        apply(deg, wi)
        if deg == DROP and wi.critical:
            fail_closed(wi)
            return
    dispatch(wi)
```

Admission control runs opportunistically and at epoch boundaries to avoid re-arbitration storms.

## 7. Invariants

- **SRT-01:** Every accepted soft item has an explicit deadline and budget.
- **SRT-02:** Critical symbolic/commit items never silently dropped (fail closed).
- **SRT-03:** Epoch-close and commit items receive a guaranteed minimum budget.
- **SRT-04:** Deadlines incorporate freshness bounds, not just period.
- **SRT-05:** Event-gated work is dispatched only on its trigger (no wasteful polling).
- **SRT-06:** Degradation is explicit and receipted; never implicit.

## 8. Inter-Plane Connections

- **Deterministic logic:** [[02_KERNEL/DETERMINISTIC_LOGIC_KERNEL|DETERMINISTIC_LOGIC_KERNEL]] — symbolic step timing
- **Neural-symbolic:** [[02_KERNEL/NEURAL_SYMBOLIC_HYBRID|NEURAL_SYMBOLIC_HYBRID]] — grounding cost models
- **CAS/commit:** [[02_KERNEL/K_CAS|K_CAS]] — commit fast-lane
- **MVCC/CAS:** [[02_KERNEL/MVCC_CAS|MVCC_CAS]] — transactional timing
- **Epoch coordination:** [[04_RUNTIME/MULTI_EPOCH_COORDINATION|MULTI_EPOCH_COORDINATION]] — epoch budget guarantee
- **Fail-closed:** [[02_KERNEL/K_FAIL_CLOSED|K_FAIL_CLOSED]] — escalation semantics
- **Runtime execution:** [[04_RUNTIME/06_EXECUTION|06_EXECUTION]]

______________________________________________________________________

**MOC:** [[02_KERNEL/02_KERNEL_MOC|02_KERNEL_MOC]] · [[00_ROOT/00_HOME|00_HOME]]

**Related:** [[02_KERNEL/NEURAL_SYMBOLIC_HYBRID|NEURAL_SYMBOLIC_HYBRID]] · [[04_RUNTIME/MULTI_EPOCH_COORDINATION|MULTI_EPOCH_COORDINATION]] · [[02_KERNEL/K_CAS|K_CAS]]
