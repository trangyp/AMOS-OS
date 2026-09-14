---
title: "08 Workflows — README"
type: readme
source: 08_WORKFLOWS
origin_architect: Trang Phan
steward: Trang Phan
amos_core_target: v4.4
status: ACTIVE
rscf:
  state: DERIVED
  claim_class: AMOS_MODEL
  provenance: AMOS_corpus
  scope: workflows_readme
---

# 08 Workflows — README

## 1. Role

Workflows coordinate multi-step execution across skills, agents, tools, state, validation, and human/control-plane gates.

```text
WORKFLOW != AGENT
WORKFLOW != SKILL
WORKFLOW != AUTHORITY
WORKFLOW_STATE != AUTHORITATIVE_WORLD_STATE
CHECKPOINT != FRESH_PERMISSION
```

## 2. Baseline lifecycle

```text
DEFINE
-> VALIDATE
-> RESOLVE DEPENDENCIES
-> RESOLVE AUTHORITY
-> EXECUTE
-> OBSERVE
-> CHECKPOINT
-> VERIFY
-> COMMIT/EXPORT WHEN AUTHORIZED
-> LEARN/REPAIR
-> RETIRE OR CONTINUE
```

Not every workflow contains every stage. Consequential effects require more gates, not fewer.

## 3. Execution topology

AMOS workflows may use:

- sequential stages;
- conditional routing;
- fan-out/fan-in;
- bounded loops;
- nested workflows/subgraphs;
- explicit agent handoffs;
- agents-as-tools/specialists;
- retry with bounded budgets;
- human interrupts;
- checkpoint/resume;
- compensation/reconciliation for side effects.

The topology must be explicit enough to recover state and provenance.

## 4. Stage ownership and cardinality

Every stage requires an accountable owner and typed dependencies, but **one stage is not universally restricted to exactly one agent and one Skill**.

Valid forms include:

```text
one agent + one skill
one agent + multiple bounded skills
one orchestrator + parallel specialist agents
one workflow node + nested governed subworkflow
```

For multi-participant stages, preserve:

```text
primary owner
participants
capability contracts
input/output lineage
join rule
authority boundary
failure propagation
```

Cardinality must not erase accountability.

## 5. Durable workflow state

Long-running workflows should externalize recoverable state:

```text
WorkflowState = (
  workflow_id,
  task_id,
  node_or_stage,
  data_state_hash,
  dependency_versions,
  source_pins,
  unresolved_gaps,
  retry_budget,
  authority_epoch_observed,
  checkpoint_id
)
```

This is an AMOS model of required state fields, not a claim that every current workflow implements them.

## 6. Checkpoint and resume invariant

A checkpoint enables recovery. It does not preserve stale entitlement.

On resume:

1. validate checkpoint integrity;
2. compare current dependencies/state;
3. invalidate stale descendants selectively;
4. re-resolve capability where changed;
5. revalidate current authority for future effects;
6. continue only from an admissible state.

## 7. Retry and recovery

Retry must be bounded and effect-aware.

```text
pure/read failure
-> bounded retry may be safe

idempotent mutation with stable key
-> retry only under idempotency/release rules

ambiguous external effect
-> reconcile before retry
```

A retry count is part of the workflow budget and state.

## 8. Fan-out / fan-in

Parallel work is allowed when branches are sufficiently independent.

At fan-in require:

- branch identity;
- provenance retained per branch;
- explicit merge/join rule;
- contradiction visibility;
- timeout/partial-result policy;
- no double-counting of correlated evidence.

The fastest branch does not silently become truth.

## 9. Human/control-plane interrupts

High-impact or ambiguous transitions may enter:

```text
WAITING_FOR_REVIEW
WAITING_FOR_AUTHORITY
WAITING_FOR_INPUT
```

The transition is part of the state machine. Human-in-the-loop is not satisfied by adding advisory prose after the effect occurred.

## 10. Workflow validation

Before activation or PR readiness, validate the smallest load-bearing set:

- structure and reachable termination/stop behavior;
- dependency existence;
- agent/skill/tool identity;
- input/output compatibility;
- state/checkpoint behavior where durable;
- bounded loops/retries;
- authority/effect boundary;
- failure/recovery behavior;
- provenance/observability;
- focused executable tests where implementation exists.

`DEFINED != VALIDATED` and `VALIDATED != DEPLOYED` remain hard distinctions.

## 11. GitHub-native repository change workflow

Repository mutation by coding agents is governed by:

`[[08_WORKFLOWS/GITHUB_AGENTIC_CHANGE_WORKFLOW|GITHUB_AGENTIC_CHANGE_WORKFLOW]]`

That workflow separates:

```text
research/planning
implementation
independent audit
CI evidence
merge authority
```

and defaults autonomous repository mutation to branch/PR scope rather than protected-branch merge.

## 12. Inter-plane connections

- **Agents:** [[06_AGENTS/06_AGENTS_MOC|06_AGENTS_MOC]]
- **Agent systems:** [[06_AGENT_SYSTEMS/GITHUB_AGENT_SKILL_INTEROP|GITHUB_AGENT_SKILL_INTEROP]]
- **Skills:** [[07_SKILLS/07_SKILLS_MOC|07_SKILLS_MOC]]
- **Protocols:** [[09_PROTOCOLS/09_PROTOCOLS_MOC|09_PROTOCOLS_MOC]]
- **Runtime:** [[04_RUNTIME/04_RUNTIME_README|04_RUNTIME_README]]
- **State:** `12_STATE`
- **Tools:** [[14_TOOLS/14_TOOLS_MOC|14_TOOLS_MOC]]
- **Observability:** `17_OBSERVABILITY`
- **Control Plane:** [[03_CONTROL_PLANE/03_CONTROL_PLANE_MOC|03_CONTROL_PLANE_MOC]]

## 13. Repository truth rule

Do not present historical workflow counts, mirror directories, or prior audit results as current truth without a current executable scan.

Host-specific `.devin/workflows` or other projections may exist in a deployment, but `08_WORKFLOWS/` is the repository-native plane in this source tree.

## 14. Invariants

1. `CAPABILITY != AUTHORITY`.
2. `CHECKPOINT != FRESH_AUTHORITY`.
3. `RETRY != SAFE_REPLAY`.
4. `PARALLEL_OUTPUTS != INDEPENDENT_EVIDENCE`.
5. `WORKFLOW_COMPLETE != EFFECT_COMMITTED`.
6. `CI_PASS != MERGE_AUTHORITY`.
7. Unknown dependency/effect state fails closed for consequential transitions.
8. Recovery preserves unaffected state and invalidates only dependent descendants when possible.

______________________________________________________________________

**MOC:** [[08_WORKFLOWS/08_WORKFLOWS_MOC|08_WORKFLOWS_MOC]]  
**Parent:** [[00_ROOT/00_HOME|00_HOME]] · [[00_ROOT/00_ROOT_MOC|00_ROOT_MOC]]
