---
title: AMOS Agent Task Lifecycle Contract
type: agent_system_specification
version: 1.0.0
amos_core_target: v4.4
origin_architect: Trang Phan
steward: Trang Phan
status: EXECUTABLE_MODEL
conclusion_class: AMOS_MODEL
epistemic_class: AMOS_MODEL
rscf:
  state: DERIVED
  claim_class: AMOS_MODEL
  provenance:
    - 06_AGENT_SYSTEMS/AGENT_SCHEMA
    - 06_AGENT_SYSTEMS/DELEGATION_LIFECYCLE
    - 04_RUNTIME/AGENT_INTEROPERABILITY_ABI
    - a2aproject/A2A@6d6640c29b102f7a8d23784901351b5d2454fe71
  scope: governed_agent_task_lifecycle
---

# AMOS Agent Task Lifecycle Contract

## 1. Purpose

This artifact governs the lifecycle of a **task instance**. It does not replace the existing agent-instance lifecycle in [[06_AGENT_SYSTEMS/DELEGATION_LIFECYCLE]].

The separation is load-bearing:

```text
AgentLifecycle != TaskLifecycle
Message != Task
Message != Artifact
TaskCompletion != DurableCommit
```

A2A provides source-grounded task/message/artifact and `contextId` concepts. The transition, fencing, authority, and commit rules below are AMOS MODEL extensions governed by the AMOS infrastructure/control plane.

## 2. State space

Let the task-state set be

\[
S = \{\text{SUBMITTED},\text{WORKING},\text{INPUT_REQUIRED},\text{AUTH_REQUIRED},\text{WAITING_DEPENDENCY},\text{COMPLETED},\text{CANCELED},\text{REJECTED},\text{FAILED}\}.
\]

The terminal subset is

\[
S_T = \{\text{COMPLETED},\text{CANCELED},\text{REJECTED},\text{FAILED}\}.
\]

`WAITING_DEPENDENCY` is an AMOS extension. The other states align with the current A2A task-lifecycle vocabulary at the source revision above.

## 3. Admissible transition relation

Define the admissible transition relation \(R \subseteq S \times S\) by the following pairs:

- `SUBMITTED -> WORKING | CANCELED | REJECTED`
- `WORKING -> INPUT_REQUIRED | AUTH_REQUIRED | WAITING_DEPENDENCY | COMPLETED | CANCELED | FAILED`
- `INPUT_REQUIRED -> WORKING | CANCELED | FAILED`
- `AUTH_REQUIRED -> WORKING | CANCELED | FAILED`
- `WAITING_DEPENDENCY -> WORKING | CANCELED | FAILED`
- terminal states have no outgoing edge.

For current state \(s\) and proposed state \(s'\), transition legality is

\[
\operatorname{Legal}(s,s') \iff (s,s') \in R.
\]

Terminal immutability is

\[
s \in S_T \implies \nexists s'\; ((s,s') \in R).
\]

A retry or refinement creates a new task/attempt with ancestry; it never restarts a terminal task in place.

## 4. Task object

Minimum task state:

```yaml
task_id: string
context_id: string
attempt_id: string
attempt: positive_integer
retry_of_task_id: optional_string
owner_agent: string
state: task_state
state_epoch: non_negative_integer
capability_grant: [string]
authority_scope: [string]
delegation_depth: non_negative_integer
max_delegation_depth: non_negative_integer
lease:
  owner_agent: string
  fencing_token: positive_integer
  expires_at: RFC3339_timestamp
cancellation_epoch: optional_non_negative_integer
messages: []
artifacts: []
transition: optional_transition_object
```

`context_id` groups related tasks/messages. `task_id` identifies one immutable unit of work.

## 5. Epoch and fencing invariants

For current task epoch \(e \in \mathbb{N}_0\), a committed state transition must satisfy

\[
e_{next} = e + 1.
\]

Let a current lease be \(L=(a,f,t_{exp})\), where \(a\) is owner agent, \(f\) is fencing token, and \(t_{exp}\) is expiry. A non-initial worker transition is admissible only if

\[
a_{actor}=a,\quad f_{request}=f,\quad t_{verify}\le t_{exp}.
\]

A stale worker therefore cannot advance task state.

`SUBMITTED -> WORKING` requires a newly issued lease. The lifecycle validator checks structural freshness of that lease; it does not issue authority.

## 6. Interruption/resume rules

- `INPUT_REQUIRED -> WORKING` requires one or more explicit input artifact IDs.
- `AUTH_REQUIRED -> WORKING` requires an authority-witness identifier. Presence is not proof of valid authority; the control plane must verify it.
- `WAITING_DEPENDENCY -> WORKING` requires dependency artifact IDs.

A message saying “approved”, “done”, or “tests passed” is not an authority witness or execution receipt.

## 7. Artifact rule

A transition to `COMPLETED` must name at least one result artifact already present in the task artifact set.

If \(A\) is the set of task artifact IDs and \(A_r\) the declared result IDs, then

\[
\text{COMPLETED} \implies \varnothing \ne A_r \subseteq A.
\]

This preserves the distinction between transient communication and persisted deliverable evidence.

## 8. Cancellation fence

Let \(e_c\) be the cancellation epoch. If cancellation has become effective by the current epoch,

\[
e_c \le e,
\]

then the only permitted state target in this contract is `CANCELED`.

Compensation or reconciliation is a separate authorized workflow; cancellation does not invent rollback authority.

## 9. Delegation attenuation

For a parent task capability set \(C_p\), child task capability set \(C_c\), parent authority scope \(A_p\), and child authority scope \(A_c\):

\[
C_c \subseteq C_p,
\qquad
A_c \subseteq A_p.
\]

For parent delegation depth \(d\), child depth \(d_c\), and configured maximum \(d_{max}\):

\[
d_c = d+1 \quad \land \quad d_c \le d_{max}.
\]

Delegation can attenuate authority/capability. It cannot create either.

## 10. Commit boundary

A valid task transition proves only that the transition contract is structurally satisfied.

It does **not** prove:

- domain correctness;
- evidence sufficiency;
- current authorization;
- external-effect completion;
- durable commit eligibility.

Final durable effects remain governed by `03_CONTROL_PLANE` and its authority, semantic-transaction, observability, freshness, idempotency, receipt, and finality gates.

## 11. Executable validator

```bash
python3 scripts/validate_agent_task_lifecycle.py --self-test
python3 scripts/validate_agent_task_lifecycle.py task.json
```

Successful validation emits `commit_authority: NOT_EVALUATED` by design.

## 12. Source boundary

At A2A revision `6d6640c29b102f7a8d23784901351b5d2454fe71`, the upstream documentation distinguishes stateless Messages from stateful Tasks, uses `contextId` to group related interactions, identifies interrupted and terminal task states, requires terminal tasks to remain immutable, and models refinements as new tasks in the same context. Those are external SOURCE_CLAIM inputs.

The AMOS transition matrix, leases/fencing, epoch rules, capability attenuation, cancellation fence, artifact admission rule, and commit boundary are AMOS_MODEL controls and must not be attributed to A2A.
