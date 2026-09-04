---
canon-group: meta
canon-type: framework
rscf-state: source-claim
topic: 09 Protocols Readme
tags:
  - canon-group/tech-ai
  - rscf/claim
  - rscf/provenance
  - rscf/state/source-claim
  - misc
created: 2026-08-22
---
---

# 09 Protocols — README

## 1. Role

Protocols define interaction and handoff contracts between components — how agents, skills, tools, runtime, state, knowledge, and authority communicate and coordinate. They are the **grammar** of the AMOS OS: without them, components may share data but cannot share meaning.

The Protocol Plane owns:
- Message format specifications and serialization schemas
- State machine definitions for every inter-component interaction
- Acknowledgment, timeout, retry, and rollback semantics
- Failure classification and recovery escalation paths
- Commit protocols with provenance receipts
- Version compatibility matrices for protocol evolution

> [!INVARIANT] Core Protocol Invariant
> Every protocol in AMOS must separate **capability** (how to interact) from **authority** (permission to interact). A protocol defines the message shape; the control plane authorizes the message content.

---

## 2. Protocol Lifecycle

Every protocol follows a governed lifecycle:

```text
PROPOSAL
    │  Drafted by origin architect or steward
    │  Provenance class: SOURCE_CLAIM
    │  No enforcement yet
    ▼
DRAFT
    │  Schema validated, negative cases identified
    │  Cross-plane references established
    │  Promotion gate checklist initiated
    ▼
ACTIVE_SPECIFICATION
    │  Promotion gate checklist complete
    │  At least one reference implementation exists
    │  Enforcement at governance boundaries
    ▼
IMPLEMENTED
    │  Runtime enforcement operational
    │  Validation receipts generated
    │  Observability hooks active
    ▼
DEPRECATED
    │  Superseded by newer protocol version
    │  Grace period for migration
    │  Backward compatibility maintained during grace period
    ▼
SUPERSEDED / ARCHIVED
    │  No active enforcement
    │  Provenance preserved for lineage
    │  Tombstone record retained
```

### 2.1 Lifecycle States

| State | Enforcement | Authority | Receipts |
| :--- | :--- | :--- | :--- |
| `PROPOSAL` | None | None | None |
| `DRAFT` | Soft validation | Origin architect | Warning only |
| `ACTIVE_SPECIFICATION` | Hard validation | Control plane | Blocking on violation |
| `IMPLEMENTED` | Runtime enforcement | Control plane + Kernel | Full audit trail |
| `DEPRECATED` | Legacy compatibility | Transitional | Deprecation warnings |
| `SUPERSEDED` | None (archived) | None | Lineage only |

### 2.2 Promotion Gate Checklist

Before a protocol may advance from DRAFT to ACTIVE_SPECIFICATION:

- [ ] Typed schema bound to the protocol artifact
- [ ] Identity + versioning implemented
- [ ] Negative cases covered (missing, malformed, stale, unauthorized input)
- [ ] Provenance edges persisted and validated
- [ ] Rollback basin demonstrated for consequential effects
- [ ] At least one reference implementation or executor exists
- [ ] Cross-plane bindings established and validated
- [ ] Failure modes documented with detection and recovery paths
- [ ] Falsifiers explicitly declared

---

## 3. Protocol Contract Template

Every protocol in AMOS must specify:

| Section | Description | Required |
| :--- | :--- | :--- |
| **Message Format** | Typed structure for all messages (YAML/JSON schema) | Yes |
| **State Transitions** | Finite state machine with labeled transitions | Yes |
| **Acknowledgment** | Positive/negative acknowledgment semantics | Yes |
| **Timeout** | Maximum wait duration before failure detection | Yes |
| **Retry** | Retry policy with backoff and jitter | Yes |
| **Failure Handling** | Failure classification, recovery, and escalation | Yes |
| **Commit** | Commit semantics with provenance receipt | Yes |
| **Rollback** | Rollback semantics with state restoration | Yes |
| **Versioning** | Protocol version format and compatibility rules | Yes |
| **Invariants** | System invariants enforced by the protocol | Yes |
| **Epistemic Class** | How protocol outputs are classified (OBSERVATION, DERIVED, etc.) | Yes |
| **Falsifiers** | Conditions that would falsify the protocol's correctness | Yes |

---

## 4. Protocol Classification Taxonomy

### 4.1 By Coordination Requirement

| Category | Description | Examples |
| :--- | :--- | :--- |
| **Coordination-Free** | No global synchronization required; I-confluent operations | Working memory mutations, local inferences |
| **Shard-Local** | Consensus within a shard boundary | RSCF observation logging, domain updates |
| **Epoch-Gated** | Global causal barrier required | Canonical law updates, authority grants |
| **Cross-Plane** | Spans multiple planes with mixed coordination | Agent-tool interaction, task handoff |

### 4.2 By Authority Level

| Level | Authority Source | Delegation Allowed | Examples |
| :--- | :--- | :--- | :--- |
| **L0 — Kernel** | Inherent in kernel logic | No | Deterministic logic, type checking |
| **L1 — Canon** | Core laws (M01–M20) | No | Invariant enforcement, epistemic classification |
| **L2 — Control Plane** | Governance authority | Scoped delegation | Authority grants, capability registration |
| **L3 — Agent-Local** | Agent-scoped authority | Within capability bounds | Tool invocation, memory access |
| **L4 — External** | Human/API authority | Per-session grants | User commands, API calls |

### 4.3 By Epistemic Class of Outputs

| Class | Protocol Output Type | Examples |
| :--- | :--- | :--- |
| `OBSERVATION` | Raw measurement from environment | Sensor data, API responses |
| `SOURCE_CLAIM` | Single-source claim, unverified | User statements, external assertions |
| `DERIVED` | Inference from verified premises | Agent reasoning, knowledge promotion |
| `MODEL` | System-level design or specification | Protocol specs, architecture documents |
| `DECISION` | Governance or authority action | Authority grants, policy changes |
| `UNKNOWN/GAP` | Acknowledged unknown | Missing data, unresolvable contradictions |

---

## 5. Protocol Versioning

### 5.1 Version Format

```
PROTOCOL_NAME vMAJOR.MINOR.PATCH
```

- **MAJOR**: Breaking changes to message format or state machine
- **MINOR**: Backward-compatible additions (new optional fields, new states)
- **PATCH**: Bug fixes, documentation corrections, non-semantic changes

### 5.2 Compatibility Rules

```yaml
version_compatibility:
  major_change:
    - "Message schema field removed or renamed"
    - "State machine transition removed"
    - "Invariant changed"
    - "Epistemic class of output changed"
    compatibility: "BREAKING — requires migration"
    grace_period: "90 days"
  
  minor_change:
    - "Optional field added to message schema"
    - "New state added to state machine"
    - "New failure mode documented"
    compatibility: "BACKWARD_COMPATIBLE"
    grace_period: "None — immediate adoption"
  
  patch_change:
    - "Documentation correction"
    - "Typo fix in schema"
    - "Non-semantic formatting change"
    compatibility: "FULLY_COMPATIBLE"
    grace_period: "None"
```

### 5.3 Version Negotiation

When two components communicate using a protocol:

```yaml
version_negotiation:
  step_1: "Both components declare supported versions"
  step_2: "Intersection computed: common_versions = supported_A ∩ supported_B"
  step_3: "Highest common version selected"
  step_4: "If intersection is empty → COMPATIBILITY_ERROR → escalation"
  step_5: "Communication proceeds at negotiated version"
```

---

## 6. Protocol Registration

Every active protocol must be registered in the Protocol Registry:

```yaml
protocol_registry_entry:
  protocol_id: "PROTO-AGENT-TOOL-INTERACTION"
  version: "1.2.0"
  status: "ACTIVE_SPECIFICATION"
  domain: "09_PROTOCOLS"
  file: "AGENT_TOOL_INTERACTION_PROTOCOL.md"
  state_machine: "7-state invocation lifecycle"
  invariants:
    - "INV-AT-01: TOOL_ACCESS != TOOL_PERMISSION"
    - "INV-AT-02: Output always classified before ingestion"
  epistemic_class: "AMOS_MODEL"
  authority_level: "L2"
  coordination_requirement: "Epoch-Gated"
  registered: "2026-09-04"
  last_validated: "2026-09-04"
  validation_receipt: "UNKNOWN/GAP"
```

---

## 7. Failure Taxonomy

| Failure Class | Description | Recovery | Severity |
| :--- | :--- | :--- | :--- |
| **Schema Violation** | Message does not match declared schema | Reject; log; return error | HIGH |
| **State Machine Violation** | Transition not valid in current state | Reject; log; quarantine | CRITICAL |
| **Timeout** | No response within declared timeout | Retry; escalate after max retries | MEDIUM |
| **Authority Exhaustion** | Authority token expired or revoked | Reject; re-request from control plane | HIGH |
| **Budget Overflow** | Resource budget exceeded during protocol execution | Terminate; return partial receipt | MEDIUM |
| **Invariant Violation** | Protocol execution would violate system invariant | Abort immediately; quarantine; escalate | CRITICAL |
| **Rollback Failure** | Rollback cannot restore consistent state | Mark state as QUARANTINED; escalate to human | CRITICAL |
| **Version Mismatch** | Components incompatible on protocol version | Negotiate; fail if no common version | HIGH |

---

## 8. Protocol Interactions

Protocols do not operate in isolation. The following interaction matrix describes how protocols compose:

| Protocol A | Protocol B | Interaction Type | Description |
| :--- | :--- | :--- | :--- |
| Agent-Tool | Task Handoff | Sequential | Tool invocation may be part of a delegated task |
| Task Handoff | Coordination Avoidance | Complementary | Handoff respects tier assignment from coordination avoidance |
| Knowledge Provenance | Agent-Tool | Cross-cutting | Tool outputs must be bound to provenance chains |
| Coordination Avoidance | Knowledge Provenance | Independent | Can execute concurrently; I-confluent |
| Task Handoff | Knowledge Provenance | Sequential | Task receipt feeds provenance chain |

---

## 9. Cross-Vault References

### 9.1 Protocol Specifications in This Plane

- [[09_PROTOCOLS/COORDINATION_AVOIDANCE_PROTOCOL|COORDINATION_AVOIDANCE_PROTOCOL]] — Coordination-free execution model
- [[09_PROTOCOLS/AGENT_TOOL_INTERACTION_PROTOCOL|AGENT_TOOL_INTERACTION_PROTOCOL]] — Agent-to-tool invocation protocol
- [[09_PROTOCOLS/KNOWLEDGE_PROVENANCE_BINDING_PROTOCOL|KNOWLEDGE_PROVENANCE_BINDING_PROTOCOL]] — Knowledge-provenance binding protocol
- [[09_PROTOCOLS/TASK_HANDOFF_PROTOCOL|TASK_HANDOFF_PROTOCOL]] — Inter-agent task delegation protocol

### 9.2 Related Planes

- **Runtime:** [[04_RUNTIME/04_RUNTIME_MOC|04_RUNTIME_MOC]] — Protocols govern runtime interactions
- **Control Plane:** [[03_CONTROL_PLANE/03_CONTROL_PLANE_MOC|03_CONTROL_PLANE_MOC]] — Protocols follow control plane authority
- **Kernel:** [[02_KERNEL/02_KERNEL_MOC|02_KERNEL_MOC]] — Kernel defines protocol invariants
- **Agents:** [[06_AGENTS/06_AGENTS_MOC|06_AGENTS_MOC]] — Agents execute protocol state machines
- **Tools:** [[14_TOOLS/14_TOOLS_MOC|14_TOOLS_MOC]] — Tools are invoked through protocols
- **Security:** [[18_SECURITY/18_SECURITY_MOC|18_SECURITY_MOC]] — Protocols are security boundaries

---

## 10. Epistemic Boundary

> [!CRITICAL] Protocol Epistemic Boundary
> A protocol specification is itself a `MODEL` — a design-time artifact describing intended behavior. It is **not** an `OBSERVATION` of actual behavior. Promotion to `IMPLEMENTED` status requires runtime evidence (validation receipts from executed validators). Until then, the protocol's correctness is a **claim**, not a fact.

$$\text{PROTOCOL\_SPEC}(p) \in \text{MODEL} \implies \text{confidence}(p) \leq 0.95$$

The confidence ceiling for any protocol specification is 0.95, regardless of how thorough the specification is. Only executed validation receipts can raise the effective confidence of the protocol's runtime behavior.

______________________________________________________________________

**Parent:** [[00_ROOT/00_HOME|00_HOME]] · [[00_ROOT/00_ROOT_MOC|00_ROOT_MOC]]
