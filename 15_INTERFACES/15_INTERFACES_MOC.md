---
canon-group: meta
canon-type: framework
rscf-state: source-claim
rscf-claim: verified
rscf-provenance: AMOS_corpus
conclusion_class: AMOS_MODEL
epistemic_class: SOURCE_CLAIM
topic: 15 Interfaces Moc
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

# 15 Interfaces — Map of Content

> [!ABSTRACT] Interfaces Plane Executive Summary
> The **Interfaces Plane** (`15_INTERFACES`) governs all boundary crossings between external agents/humans/sensors and the internal AMOS reasoning kernel.
> It enforces the **Expression Firewall**:
> $$\text{RAW LANGUAGE / NEURAL SIGNAL} \neq \text{INTERNAL LOGIC STATE}$$
> $$\text{USER EXPRESSION} \neq \text{AUTHORIZED STATE MUTATION}$$

---

## 1. Primary Boundary Interfaces

### 1.1 Expression Gateway (`T_expression`)

The Expression Gateway translates raw human expression, emotional cues, and symbolic constructs into logic-ready AMOS structural inputs:

| Stage | Input | Output | Epistemic Class |
| :--- | :--- | :--- | :--- |
| `EXPRESSION_CLASSIFY` | Raw expression | Intent type (speech, motor, cognitive, emotional) | OBSERVATION |
| `INTENT_EXTRACTION` | Classified intent | Specific intended content | OBSERVATION |
| `MEANING_CORE` | Extracted intent | Semantic interpretation | DERIVED |
| `STRUCTURAL_LOGIC_MAP` | Semantic interpretation | AMOS cognitive structures | DERIVED |
| `NORMALISE` | Logic structures | Epistemic-classified input | OBSERVATION → PROPOSAL |

**Detail:** [[11_KNOWLEDGE/AMOS_FULL_BRAIN_OS_ARCHITECTURE#25-expression-translation|Expression Translation Gateway]]

### 1.2 Brain-Computer Interface (BCI)

The BCI translates electrophysiological telemetry (spikes, ECoG, EEG) into discrete cognitive proposals:

| Modality | Signal Type | Channel Count | Latency | Foundation Model |
| :--- | :--- | :--- | :--- | :--- |
| Intracortical | Spikes + LFP + ECoG | 1,000–10,000+ | <80ms | RNN-T transducer |
| ECoG | High-gamma + LFP | 100–1,000 | <100ms | ST-EEGFormer |
| EEG | Scalp potentials | 32–256 | <12.5ms | DeeperBrain (SSM) |
| fNIRS | Hemodynamic | 16–64 | <500ms | Lightweight SSM |

**Detail:** [[21_DOMAINS/14_C04_BIO_NEURO/C04_NEURAL_DECODING_AND_BCI_ARCHITECTURE|C04 Neural Decoding & BCI Architecture]]

### 1.3 Interface Specification

Formal boundary protocol contracts and type schemas:

- **Message Format:** Typed YAML/JSON schemas for all cross-boundary messages
- **State Machines:** Finite state machines for every interface interaction
- **Authority Requirements:** Scoped authority tokens for each interface operation
- **Audit Trail:** Complete logging of all cross-boundary interactions

**Detail:** [[15_INTERFACES/INTERFACES_INTERFACE_CONTRACT|INTERFACES_INTERFACE_CONTRACT]]

### 1.4 Package Overview

Structural summary of the Interfaces plane:

- **Files:** Interface specifications, adapter definitions, contract documents
- **Coverage:** Human, agent, system, and external boundaries
- **Status:** PRODUCTION_MOC with PARTIAL implementation

**Detail:** [[15_INTERFACES/INTERFACES_README|INTERFACES_README]]

---

## 2. Interface Taxonomy

### 2.1 By Channel Type

| Channel | Description | Latency | Throughput | Reliability |
| :--- | :--- | :--- | :--- | :--- |
| **Human (H-MODE)** | CLI, UI, voice, gesture | High (ms–s) | Low | Eventual |
| **Agent (A-MODE)** | Inter-agent protocols, tool bindings | Low (ms) | High | At-least-once |
| **System (S-MODE)** | API contracts, file I/O, network | Low (ms) | High | Exactly-once |
| **Neural (N-MODE)** | BCI telemetry, neural signals | Ultra-low (μs–ms) | Medium | Best-effort |

### 2.2 By Protocol Binding

| Binding | Description | Examples |
| :--- | :--- | :--- |
| **Synchronous** | Request-response with blocking wait | CLI commands, API calls |
| **Asynchronous** | Fire-and-forget with callback | Background jobs, event streams |
| **Streaming** | Continuous data flow | Neural telemetry, log streams |
| **Bidirectional** | Full-duplex communication | WebSocket, BCI closed-loop |

### 2.3 By Security Level

| Level | Description | Requirements | Examples |
| :--- | :--- | :--- | :--- |
| **Public** | No authentication required | Rate limiting only | Public API endpoints |
| **Authenticated** | Identity verified | Authentication token | User-facing interfaces |
| **Authorized** | Identity + permission verified | Authorization token | Agent-tool interfaces |
| **Confidential** | Encrypted + authorized | Encryption + authorization | BCI neural data |
| **Restricted** | Multi-factor + audit | MFA + full audit trail | Authority management |

---

## 3. Interface Lifecycle

### 3.1 Lifecycle States

```text
DECLARED
    │  Interface registered with typed schema
    ▼
AVAILABLE
    │  Interface passes health check
    ▼
ACTIVE
    │  Interface processing messages
    │  Audit trail active
    ▼
THROTTLED
    │  Rate limiting active
    │  Resource budget near limit
    ▼
DEPRECATED
    │  Interface superseded
    │  Grace period for migration
    ▼
RETIRED
    │  No active connections
    │  Tombstone preserved
```

### 3.2 Promotion Gate Checklist

- [ ] Typed schema bound to interface artifact
- [ ] Identity + versioning implemented
- [ ] Negative cases covered (missing, malformed, stale, unauthorized input)
- [ ] Authority requirements declared
- [ ] Security level declared
- [ ] Audit trail hooks active
- [ ] Health monitoring configured
- [ ] At least one validation receipt generated

---

## 4. Invariants & Epistemic Boundaries

| ID | Invariant | Enforcement |
| :--- | :--- | :--- |
| `INV-INT-01` | All external inputs enter as `OBSERVATION` or `SOURCE_CLAIM` | Epistemic classifier at boundary |
| `INV-INT-02` | No external interface may directly mutate internal state | Must pass through Omni Kernel admission gate |
| `INV-INT-03` | Interface ≠ Implementation | UI component does not contain business logic |
| `INV-INT-04` | Protocol ≠ Transport | HTTP is transport; schema is protocol |
| `INV-INT-05` | Schema ≠ Validation | Schemas define structure; validation enforces constraints |
| `INV-INT-06` | All boundary interactions produce audit trail | Logging at interface boundary |
| `INV-INT-07` | Authentication at boundary, not propagated | Identity verified at entry point |
| `INV-INT-08` | Rate limiting per interface | Resource consumption bounded |

---

## 5. Cross-References

### 5.1 Internal Plane References

- [[15_INTERFACES/INTERFACES_INTERFACE_CONTRACT|INTERFACES_INTERFACE_CONTRACT]] — Formal interface contract
- [[15_INTERFACES/BCI_EXPRESSION_GATEWAY_ADAPTER|BCI_EXPRESSION_GATEWAY_ADAPTER]] — BCI adapter specification
- [[15_INTERFACES/INTERFACES_README|INTERFACES_README]] — Structural overview

### 5.2 External Plane References

- **Tools:** [[14_TOOLS/14_TOOLS_MOC|14_TOOLS_MOC]] — Interfaces expose tools; tools not directly accessible
- **Security:** [[18_SECURITY/18_SECURITY_MOC|18_SECURITY_MOC]] — Interfaces are security boundaries
- **Observability:** [[17_OBSERVABILITY/17_OBSERVABILITY_MOC|17_OBSERVABILITY_MOC]] — Interface interactions produce observability data
- **Runtime:** [[04_RUNTIME/04_RUNTIME_MOC|04_RUNTIME_MOC]] — Interfaces are runtime entry/exit points
- **Agents:** [[06_AGENTS/06_AGENTS_MOC|06_AGENTS_MOC]] — Agents communicate through interfaces
- **Control Plane:** [[03_CONTROL_PLANE/03_CONTROL_PLANE_MOC|03_CONTROL_PLANE_MOC]] — Interface authority enforced by control plane

---

## 6. Worked Semantics

Given an operation touching the Interfaces plane:

1. **Admit** — Resolve the interface by ID + version; unresolved ID ⇒ `UNKNOWN/GAP`, fail closed.
2. **Bind scope** — Declare channel type, security level, and protocol binding.
3. **Check authority** — Authority token must be epoch-valid; capability alone never authorizes.
4. **Validate schema** — Message validated against registered schema before processing.
5. **Classify epistemic** — All inbound data classified as OBSERVATION or SOURCE_CLAIM.
6. **Route** — Message routed to appropriate internal handler.
7. **Audit** — Full interaction logged with provenance and timestamp.

---

## 7. Promotion Gate Checklist

- [ ] Typed schema bound to this artifact
- [ ] Identity + versioning implemented
- [ ] Negative cases covered (missing · malformed · stale · unauthorized input)
- [ ] Provenance edges persisted and validated
- [ ] Rollback basin demonstrated for consequential effects
- [ ] Executed validation receipt specific to this artifact
- [ ] Unresolved critical gaps registered as UNKNOWN/GAP (visible)

---

## 8. Falsifiers

F1: canonical source contradicts declared semantics. F2: executed test violates a stated invariant. F3: artifact promotes UNKNOWN to PASS.

---
[[00_ROOT/00_ROOT_MOC|Root MOC]] · [[AMOS_HOME|AMOS Home]]
