---
title: Task Handoff Protocol Specification
type: protocol_specification
source: 09_PROTOCOLS
origin_architect: Trang Phan
steward: Trang Phan
amos_core_target: v4.4
status: ACTIVE_SPECIFICATION
epistemic_class: AMOS_MODEL
conclusion_class: DERIVED
rscf:
  state: DERIVED
  claim_class: AMOS_MODEL
  provenance:
    - authoritative_AMOS_OS_structure
    - 06_AGENTS/06_AGENTS_MOC
    - 03_CONTROL_PLANE/CONTROL_PLANE_CONTROL_PLANE_CONTRACT
    - 08_WORKFLOWS/08_WORKFLOWS_MOC
    - 18_SECURITY/18_SECURITY_MOC
  scope: inter_agent_handoff
tags:
  - amos-os
  - protocols
  - task-handoff
  - agent-delegation
  - capability-attenuation
  - blake3-receipt
---

# Task Handoff Protocol Specification (THP-01)

**Origin Architect & Steward:** Trang Phan
**Target AMOS Lineage:** v4.4
**Plane:** `09_PROTOCOLS`
**Status:** `ACTIVE_SPECIFICATION`
**Epistemic Classification:** `AMOS_MODEL` / `DERIVED`

---

## 1. Executive Summary & Protocol Purpose

The **Task Handoff Protocol (THP-01)** formalizes the exact cryptographic sequence, state machine transitions, capability attenuation envelopes, and validation contracts required when an orchestrator or parent agent delegates a subtask to a specialist worker agent.

It ensures that delegated execution cannot escape assigned authorization bounds, violate epistemic rules, or corrupt the global system state upon subagent failure.

```text
┌─────────────────────────────────────────────────────────────────────────────┐
│                    TWO-PHASE TASK HANDOFF STATE MACHINE                     │
│                                                                             │
│  [Orchestrator Agent]                             [Specialist Worker Agent] │
│          │                                                   │              │
│          │ 1. PREPARE: Mint Attenuated Capability Token      │              │
│          │    & Task Capsule (Budget, Scope, Invariants)     │              │
│          ├──────────────────────────────────────────────────►│              │
│          │                                                   │ 2. VALIDATE: │
│          │                                                   │ Preconditions│
│          │ 3. ACK_PREPARE: Bind Local Working State          │ Scope Check  │
│          │◄──────────────────────────────────────────────────┤              │
│          │                                                   │              │
│          │ 4. COMMIT_EXECUTE: Start Bounded Routine          │              │
│          ├──────────────────────────────────────────────────►│              │
│          │                                                   │ 5. EXECUTE:  │
│          │                                                   │ Bounded Run  │
│          │ 6. EMIT_RECEIPT: Proof Capsule & BLAKE3 Digest    │ Trace Log    │
│          │◄──────────────────────────────────────────────────┤              │
│          │                                                   │              │
│          │ 7. FINALIZE: Verify Receipt & Ingest Output       │              │
│          │    (Or ROLLBACK on Invariant Violation)           │              │
└──────────┴───────────────────────────────────────────────────┴──────────────┘
```

---

## 2. Nine-Part AMOS Control Contract

### 2.1 ROLE
Governs secure, verifiable task delegation and context handoffs across autonomous agents while preventing capability leakage or hallucination propagation.

### 2.2 INTERFACES
- `ITaskCapsuleFactory`: Constructs strongly-typed task delegation capsules.
- `ICapabilityAttenuationEngine`: Mints cryptographically attenuated capability tokens with expiration deadlines and scoped tool permissions.
- `IHandoffStateMachine`: Enforces two-phase prepare/commit handoff transitions and timeout rollbacks.
- `IReceiptValidator`: Cryptographically validates execution proofs before parent ingestion.

### 2.3 DEPENDENCIES
- `03_CONTROL_PLANE`: Authority matrices and permission registries.
- `06_AGENTS`: Agent identity definitions and role boundaries.
- `08_WORKFLOWS`: Multi-step state machine engines.
- `18_SECURITY`: Cryptographic signing and token verification.

### 2.4 INVARIANTS
1. **Non-Escalation Invariant**: A delegated worker agent CAN NEVER acquire or grant itself permissions exceeding the scope of its parent orchestrator.
2. **Strict Provenance Invariant**: The returned execution receipt must explicitly record all intermediate claim DAG nodes, citations, and tools invoked.
3. **Fail-Closed Invariant**: In the event of an unresolvable contradiction or timeout, the worker MUST emit a structured `UNKNOWN/GAP` rather than hallucinating a completion.
4. **Linear Resource Bounding**: Every handoff capsule specifies hard caps on token consumption, wall-clock time, and tool invocations.

### 2.5 AUTHORITY
Governed by `AMOS_CORE v4.4`, origin architect **Trang Phan**.

### 2.6 PROVENANCE
Engineered from distributed RPC protocols, Macaroon/Biscuit capability tokens, and transactional state machine standards.

### 2.7 TESTS
- Unit verification of capability attenuation rules under privilege escalation attacks.
- Timeout injection and automatic rollback recovery benchmarks ($\Delta t < 5.0\text{ ms}$).
- Adversarial receipt tampering and signature forgery validation.

### 2.8 FAILURE MODES
- Worker agent crash or network partition during execution.
- Token budget exhaustion before task completion.
- Invariant breach or corrupted return schema.

### 2.9 RECOVERY
- Automatic task cancellation and compensation rollback on parent orchestrator.
- Re-delegation to alternative worker or emission of gap record to the human steward.

---

## 3. Data Structure & Capsule Schema

### YAML Task Capsule Specification:
```yaml
task_id: "TASK-2026-09-04-00284"
parent_task_id: "ORCH-TASK-9042"
delegating_agent: "amos-orchestrator-alpha"
target_agent: "amos-qfm-specialist-01"
objective: "Verify mathematical proof of Lemma 4.2 in singularity paper"
confidence_ceiling: 0.95
resource_budget:
  max_tokens: 4000
  timeout_seconds: 30
  max_tool_calls: 5
rscf_scope: "22_RESEARCH/01_MATHEMATICS"
required_invariants:
  - "L0_INTEGRITY: SOURCE_CLAIM != VERIFIED"
  - "L28_CRITICAL_GAP: FAIL_CLOSED_ON_UNKNOWN"
input_references:
  - "[[22_RESEARCH/01_MATHEMATICS/AMOS_137_MATH_REGISTRY]]"
authority_token: "AUTH-CAP-99182-SIG-ED25519-EXP-20260904T150000Z"
```

### Execution Return Receipt Schema:
```yaml
receipt_id: "RCPT-2026-09-04-00591"
task_id: "TASK-2026-09-04-00284"
status: "COMPLETED_VERIFIED"
epistemic_class: "DERIVED"
confidence_score: 0.942
proof_artifacts:
  - "22_RESEARCH/01_MATHEMATICS/LEMMA_4_2_LEAN4_PROOF"
tokens_consumed: 1842
wall_clock_elapsed_ms: 1248
blake3_receipt_hash: "3b9a8f2c1d0e4a5b6c7d8e9f0a1b2c3d4e5f6a7b8c9d0e1f2a3b4c5d6e7f8a9b"
```

---

## 4. AMOS OS MECE Plane Integration

| AMOS Plane | Role & Responsibilities |
| :--- | :--- |
| **[[03_CONTROL_PLANE/03_CONTROL_PLANE_MOC\|03_CONTROL_PLANE]]** | Validates capability delegation limits and mints authority tokens. |
| **[[06_AGENTS/06_AGENTS_MOC\|06_AGENTS]]** | Hosts orchestrator and specialist worker agent state lifecycles. |
| **[[08_WORKFLOWS/08_WORKFLOWS_MOC\|08_WORKFLOWS]]** | Manages handoff orchestration and timeout compensation logic. |
| **[[09_PROTOCOLS/09_PROTOCOLS_MOC\|09_PROTOCOLS]]** | Defines the physical wire protocol and Protobuf envelope contracts. |
| **[[17_OBSERVABILITY/17_OBSERVABILITY_MOC\|17_OBSERVABILITY]]** | Logs handoff latency, resource consumption, and delegation traces. |
| **[[18_SECURITY/18_SECURITY_MOC\|18_SECURITY]]** | Verifies cryptographic token signatures and enforces sandbox constraints. |

---

## 5. Structural Invariants & Governance

1. **Non-Escalation Boundary**: A subtask handoff can only attenuate authority, never amplify it.
2. **Immutable Traceability**: Every delegation event is logged to [[17_OBSERVABILITY/17_OBSERVABILITY_MOC|17_OBSERVABILITY]].
3. **No Unwarranted Promotion**: Output receipts remain subject to parent orchestrator and control plane admission.
4. **Lineage**: Governed under AMOS v4.4; origin steward **Trang Phan**.

---

## 6. Cross-Plane References

- Protocols MOC: [[09_PROTOCOLS/09_PROTOCOLS_MOC|09_PROTOCOLS MOC]]
- Agents MOC: [[06_AGENTS/06_AGENTS_MOC|06_AGENTS MOC]]
- Workflows MOC: [[08_WORKFLOWS/08_WORKFLOWS_MOC|08_WORKFLOWS MOC]]
- Control Plane Authority: [[03_CONTROL_PLANE/04_AUTHORITY/00_INDEX/CONTROL_PLANE_AUTHORITY_MAP|CONTROL_PLANE_AUTHORITY_MAP]]
- Multi-Agent Epistemic Chain: [[08_WORKFLOWS/AUTONOMOUS_MULTI_AGENT_EPISTEMIC_VERIFICATION_CHAIN|Autonomous Epistemic Verification]]
