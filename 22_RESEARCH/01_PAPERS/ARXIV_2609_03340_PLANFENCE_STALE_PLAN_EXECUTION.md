---
title: "Fresh Memory, Stale Plans: Dependency-Scoped Validation for Distributed LLM-Agent Memory"
type: research_paper
source: arxiv
arxiv_id: "2609.03340"
url: "https://arxiv.org/abs/2609.03340"
amos_core_target: v4.4
origin_architect: Trang Phan
steward: Trang Phan
epistemic_class: SOURCE_CLAIM
conclusion_class: DERIVED
rscf:
  state: SOURCE_CLAIM
  claim_class: SOURCE_CLAIM
  provenance:
    - arxiv:2609.03340
    - 22_RESEARCH/BCI_AI_QUANTUM_SOTA_2026-09-04
  scope: distributed_llm_agent_plan_validation
tags:
  - research
  - arxiv
  - multi-agent
  - plan-validation
  - causal-epoch
  - memory-freshness
  - distributed-agents
created: 2026-09-04
---

# PlanFence — Dependency-Scoped Validation for Distributed LLM-Agent Memory

> **arXiv:** [2609.03340](https://arxiv.org/abs/2609.03340)
> **Epistemic class:** `SOURCE_CLAIM` (controlled safety/systems-cost results, not general task-accuracy gains)
> **AMOS bridge:** Causal Epoch Finality, Action-Memory Firewall, K_Binding, K_Causal_Closure

## Abstract summary

Distributed LLM-agent teams share a public memory of records (observations, facts, prior decisions). A planner agent reads public records and produces a plan; executor agents act on that plan. Between plan creation and execution, other agents may revise the public records the plan depended on. A naive executor that simply re-reads "fresh" memory before acting still executes a **stale plan** — the plan's logic was derived from records that no longer hold, but the executor has no way to know which records the plan actually used.

PlanFence is a **dependency-scoped action-validation protocol**. Plans cite the exact public records they used as dependencies. The executor validates only the records that can affect pending external action — not the entire memory. This scopes validation to the causal dependency cone of the action, avoiding both blind execution of stale plans and prohibitively expensive full-memory re-validation.

## Key results

- In 30 controlled live workflows with post-plan revision, a freshness-only executor (re-reads memory but does not check plan dependencies) acts on an obsolete plan in **every task** (30/30 invalid actions).
- PlanFence completes **all tasks without invalid action** (0/30 invalid actions) under the same revision conditions.
- Proactive synchronization (push updates to executors before action) yields lower coordination stall at low churn.
- As churn grows, PlanFence avoids repeated update-path coordination — dependency-scoped validation is cheaper than re-coordinating the full update path each time a record changes.
- Results are controlled safety/systems-cost metrics, not general task-accuracy benchmarks.

## AMOS bridge analysis

### Bridge to Causal Epoch Finality

PlanFence's dependency-scoped validation is structurally identical to AMOS causal epoch finality:

```text
AMOS Causal Epoch Finality:
  plan validity is tied to the source epoch from which it was derived
  if any source record in the plan's causal antecedent set is superseded,
  the plan's epoch is broken → plan must be re-validated or discarded

PlanFence dependency-scoped validation:
  plan cites exact public records it used (dependency set)
  executor validates only those records before acting
  if any cited record has been revised → plan is stale → block or re-validate
```

Both enforce the same invariant: **a derived artifact (plan/decision) is valid only for the epoch of its source records; supersession of any source invalidates the artifact.**

### Bridge to Action-Memory Firewall

PlanFence's core finding — "fresh memory ≠ valid plan" — is the operational form of AMOS's "Memory ≠ Knowledge" boundary:

```text
AMOS Action-Memory Firewall:
  Memory ≠ Knowledge — retrieved memory is not automatically valid authority for action
  memory must pass validation gates before it can authorize external effect

PlanFence:
  fresh memory ≠ valid plan — re-reading current memory does not rescue a plan
  built on stale records; the plan's dependency set must be validated, not just
  the executor's current memory view
```

Both enforce: **acting on memory without validating its relationship to the pending action is an unguarded externalization.**

### Bridge to K_Binding

PlanFence requires that a plan explicitly binds to the source records it depended on. This is an instance of AMOS K_Binding — the dependency binding must exist and must be validated before action:

```text
AMOS K_Binding:
  every derived claim/action must carry a binding to its source(s)
  the binding is validated before the derived artifact is trusted or executed

PlanFence:
  plan carries dependency citations to exact public records
  executor validates the binding (are cited records still current?) before acting
  missing or broken binding → plan cannot be safely executed
```

Without K_Binding, the executor has no way to know which records matter — it would have to re-validate the entire memory, which is intractable in distributed settings.

### Bridge to K_Causal_Closure

PlanFence's dependency set is the plan's causal antecedent set. The executor validates that set — this is AMOS K_Causal_Closure applied at action time:

```text
AMOS K_Causal_Closure:
  a derived artifact's causal antecedents must be traced and validated
  incomplete causal closure → unvalidated assumptions → cannot authorize action

PlanFence:
  plan's dependency citations define its causal closure
  executor validates every cited record (the closure) before acting
  uncited but load-bearing record → causal closure is incomplete → risk of stale action
```

PlanFence assumes the plan's dependency citations are complete. If a plan silently depended on a record it did not cite, the causal closure would be incomplete and PlanFence could not detect the staleness — this is the same residual risk AMOS K_Causal_Closure addresses.

## Epistemic boundary

- PlanFence is validated on 30 controlled live workflows with induced post-plan revision. These are safety/systems-cost results (invalid-action rate, coordination stall), **not** general task-accuracy gains. The epistemic class is `SOURCE_CLAIM` for the distributed-agent plan-validation domain.
- The AMOS bridges are `AMOS_MODEL` — structural analogies to AMOS mechanisms, not empirical validation of AMOS runtime.
- PlanFence's correctness depends on plans faithfully citing all load-bearing dependencies. If a plan omits a dependency (incomplete causal closure), PlanFence cannot detect staleness from that uncited record — the same residual risk as AMOS K_Causal_Closure under incomplete provenance.
- The proactive-synchronization vs. dependency-scoped-validation tradeoff is measured under controlled churn conditions; real-world churn patterns may differ.

## Related

- [[22_RESEARCH/BCI_AI_QUANTUM_SOTA_2026-09-04|BCI/AI/Quantum SOTA 2026-09-04]]
- [[07_SKILLS/amos-causal-epoch-finality/SKILL|Causal Epoch Finality]]
- [[07_SKILLS/amos-action-memory-firewall/SKILL|Action-Memory Firewall]]
- [[07_SKILLS/amos-k-binding/SKILL|K_Binding]]
- [[07_SKILLS/amos-k-causal-closure/SKILL|K_Causal_Closure]]
- [[07_SKILLS/amos-memory-conflict-governor/SKILL|Memory Conflict Governor]]
- [[07_SKILLS/amos-provenance-trust-firewall/SKILL|Provenance Trust Firewall]]
- [[22_RESEARCH/22_RESEARCH_MOC|22_RESEARCH_MOC]]
