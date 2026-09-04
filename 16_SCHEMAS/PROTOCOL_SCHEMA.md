---
canon-group: meta
canon-type: framework
rscf-state: source-claim
rscf-claim: verified
rscf-provenance: AMOS_corpus
conclusion_class: AMOS_MODEL
epistemic_class: SOURCE_CLAIM
topic: Protocol Schema
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

# Protocol Schema

## 0. Status

`PROTOCOL_SCHEMA.md` is a **typed schema specification** for AMOS protocol artifacts under `09_PROTOCOLS`. It is an `AMOS_MODEL` specification: NOT executed, NOT validated, and NOT enforced as a validator. Implementation and validation status are `NOT_ESTABLISHED` / `PARTIAL`.

Governing boundaries preserved:

```text
DOCUMENTED != ENFORCED
CAPABILITY != AUTHORITY
PROPOSAL != COMMIT
TOOL_ACCESS != TOOL_PERMISSION
UNKNOWN/GAP != PASS
```

Origin architect / steward: **Trang Phan**

---

## 1. Purpose

A protocol artifact formalizes an ordered, gated interaction sequence between participants — agents, tools, engines, planes — with explicit message contracts, state transitions, failure modes, and commit/rollback semantics. `PROTOCOL_SCHEMA.md` types every field of such an artifact so that a conforming protocol can be reasoned about, audited, and (eventually) executed.

---

## 2. Governing rules

- Every interaction boundary enforces `M10: TOOL_ACCESS != TOOL_PERMISSION`.
- Capability (knowing how to sequence) is distinct from authority (being permitted to execute).
- A protocol proposed is not a protocol committed; effects require gates.
- Unknown or untyped fields are `UNKNOWN/GAP`, never invented.

---

## 3. Protocol artifact schema

| name | type | required | description | constraints |
| :--- | :--- | :--- | :--- | :--- |
| `protocol_id` | string | true | Stable identifier for the protocol | regex `^PRT-[0-9]{4}-[0-9]+$` |
| `version` | string | true | Semantic version of this protocol spec | semver |
| `type` | string | true | Protocol family | enum: `request` / `handoff` / `interaction` / `recovery` |
| `trigger` | string | true | Condition(s) that initiate the protocol | non-empty |
| `prerequisites` | array | true | Preconditions required before start | each refers to a satisfiable condition |
| `participants` | array | true | Roles that take part | each participant maps to an agent/engine |
| `message_contract` | object | true | Typed message schemas exchanged | see §3.1 |
| `state_machine` | object | true | Legal state transitions of the protocol | see §3.2 |
| `ack_timeout_retry` | object | true | Acknowledgement, timeout, and retry policy | see §3.3 |
| `failure_modes` | array | true | Enumerated ways the protocol can fail | see §3.4 |
| `commit_rollback` | object | true | Commit and rollback semantics | see §3.5 |
| `invariants` | array | true | Rules that must hold at every step | see §3.6 |
| `authority` | object | true | Authority required per step | see §3.7 |
| `provenance` | object | true | Source and lineage of the artifact | see §3.8 |
| `tests` | array | false | Validation tests for the protocol | see §3.9 |
| `m10_m12_gates` | array | true | M10/M12 gate checkpoints | see §3.10 |

---

## 3.1 Message contract

Each message is typed with the following fields:

| name | type | required | description |
| :--- | :--- | :--- | :--- |
| `message_type` | string | true | Name of the message |
| `direction` | string | true | enum: `request` / `response` / `event` / `ack` |
| `payload_schema` | object | true | Typed fields of the payload |
| `expected_output_class` | string | false | Epistemic class of output (`OBSERVATION` / `DERIVED` / `SOURCE_CLAIM`) |
| `authentication_required` | boolean | true | Whether identity/auth is required for the message |

---

## 3.2 State machine

| name | type | required | description |
| :--- | :--- | :--- | :--- |
| `states` | array | true | Legal states (e.g. `INIT` / `READY` / `RUNNING` / `SUSPENDED` / `TERMINATED`) |
| `transitions` | array | true | Allowed state transitions with guard conditions |
| `terminal_states` | array | true | States that end the protocol |

A state machine MUST NOT permit a transition that bypasses an authority or commit gate. Invalid transitions fail closed.

---

## 3.3 Ack / timeout / retry

| name | type | required | description |
| :--- | :--- | :--- | :--- |
| `ack_required` | boolean | true | Whether acknowledgement is required for messages |
| `timeout_ms` | integer | false | Timeout for each step/await |
| `retry_limit` | integer | false | Max automatic retries before escalation |
| `retry_backoff` | string | false | Backoff strategy (e.g. `exponential`) |

Timeout and retry parameters must be bounded; exceeding `retry_limit` escalates to control plane instead of silent partial execution.

---

## 3.4 Failure modes

| name | type | required | description |
| :--- | :--- | :--- | :--- |
| `failure_id` | string | true | Unique failure identifier |
| `detection` | string | true | How the failure is detected |
| `recovery` | string | true | Recovery / quarantine / escalation behavior |

See also the protocol-failure table in §6.

---

## 3.5 Commit / rollback

| name | type | required | description |
| :--- | :--- | :--- | :--- |
| `commit_condition` | string | true | Condition that must hold to commit effects |
| `rollback_available` | boolean | true | Whether a rollback basin exists before mutation |
| `rollback_scope` | string | false | Which effects are rolled back on failure |

Hard invariant: a stale read or failed premise ⇒ `NO FINAL COMMIT`.

---

## 3.6 Invariants

Each invariant is:

- `invariant_id` (string, required)
- `invariant_statement` (string, required)
- `enforcement` (string, required) — how it is checked at runtime

---

## 3.7 Authority

| name | type | required | description |
| :--- | :--- | :--- | :--- |
| `authority_ref` | string | false | Reference to the authority grant enabling the step |
| `authority_epoch` | string | false | Authority epoch that must be valid at commit time |
| `capability_ref` | string | false | Capability required (distinct from authority) |

`Capability` alone never authorizes execution; every consequential step requires an epoch-valid `authority_ref`.

---

## 3.8 Provenance

| name | type | required | description |
| :--- | :--- | :--- | :--- |
| `source` | string | true | Origin of the artifact (e.g. `09_PROTOCOLS`) |
| `parent_ids` | array | false | Governing parents (contracts, laws) |
| `lineage` | string | false | Heritage / supersession chain |

---

## 3.9 Tests

Each test: `test_id` (string), `scenario` (string), `expected` (string), `status` (string, `PARTIAL` / `NOT_ESTABLISHED`).

---

## 3.10 M10 / M12 gates

| name | type | required | description |
| :--- | :--- | :--- | :--- |
| `gate_id` | string | true | Gate identifier (e.g. `M10`, `M12`) |
| `checkpoint` | string | true | Step in the state machine where the gate is enforced |
| `predicate` | string | true | Condition that must hold at the checkpoint |

---

## 4. `protocol_request` schema

A request protocol transfers a typed request with bounded authority and resource budget.

| name | type | required | description |
| :--- | :--- | :--- | :--- |
| `request_id` | string | true | Unique request identifier |
| `sender_id` | string | true | Identity of the requesting participant |
| `protocol_id` | string | true | The protocol this request instantiates |
| `parameters` | object | true | Typed invocation parameters |
| `authority_token` | string | true | Single-use authority token |
| `resource_budget` | object | true | Bounded tokens / time / memory |
| `expected_output_class` | string | false | Epistemic class of the expected output |
| `provenance_context` | object | false | Parent task, causal epoch |

---

## 5. `protocol_handoff` schema

A handoff protocol transfers responsibility/context between participants without transferring authority beyond its bounds.

| name | type | required | description |
| :--- | :--- | :--- | :--- |
| `handoff_id` | string | true | Unique handoff identifier |
| `from_participant` | string | true | Source of handoff |
| `to_participant` | string | true | Destination of handoff |
| `context` | object | true | State/context being transferred |
| `authority_transfer` | object | true | Bounds of any authority being transferred |
| `ack_required` | boolean | true | Whether destination must acknowledge |
| `completion_proof` | string | false | Proof the handoff completed |

Hard invariant for handoff: authority transferred may only tighten, never widen (`ChildAuthority ⊆ ParentAuthority`).

---

## 6. Protocol failure modes (canonical)

| Failure | Detection | Recovery |
| :--- | :--- | :--- |
| **Capability mismatch** | Gate `M10` fails | Reject; log unauthorized capability request |
| **Authority expired** | Authority token validation fails | Reject; escalate to control plane for re-authorization |
| **Budget exceeded** | Resource check fails | Throttle or reject; return partial results if available |
| **Timeout exceeded** | `timeout_ms` reached | Retry up to `retry_limit`, then escalate |
| **Output misclassification** | Epistemic classifier detects inconsistency | Block output; flag for review |

---

## 7. Status / gaps

- Implementation status: `NOT_ESTABLISHED` — no protocol validator exists.
- Validation status: `NOT_ESTABLISHED` — no executed receipt for this schema.
- Promotion beyond `AMOS_MODEL` requires an executed validation receipt specific to this schema plus the standard promotion-gate checklist.

---

## 8. Cross-plane bindings

- Governed by canon — [[01_CANON/01_CORE_LAWS/LAW_HIERARCHY|AMOS Core Laws]]
- Protocol grounds — [[09_PROTOCOLS/AGENT_TOOL_INTERACTION_PROTOCOL|AGENT_TOOL_INTERACTION_PROTOCOL]]
- Control-plane gates — [[03_CONTROL_PLANE/04_AUTHORITY/AUTHZ_ENGINE_VALIDATION_RECEIPT|AUTHZ_ENGINE_VALIDATION_RECEIPT]]
- Observed by — [[17_OBSERVABILITY/OBSERVABILITY_README|OBSERVABILITY_README]] · never treated as authority
- Recovered via operations — [[20_OPERATIONS/OPERATIONS_README|OPERATIONS_README]]

---

```RSCF-NODE
node_id: amos_16_schemas_protocol_schema
node_type: schema
path: 16_SCHEMAS/PROTOCOL_SCHEMA.md
claim_class: AMOS_MODEL
rscf_state: derived
canonical_status: UNKNOWN/GAP
RSCF-RELATIONS:
  - INDEXED_BY: [[00_ROOT/00_HOME|00_HOME]]
  - GOVERNED_BY: [[01_CANON/01_CORE_LAWS/LAW_HIERARCHY|LAW_HIERARCHY]]
  - GROUNDS: [[09_PROTOCOLS/AGENT_TOOL_INTERACTION_PROTOCOL|AGENT_TOOL_INTERACTION_PROTOCOL]]
```
