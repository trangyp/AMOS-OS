---
title: "04_RUNTIME — Causal Concurrency & Epoch Execution"
type: architecture_specification
source: 04_RUNTIME
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
    - 00_ROOT/FULL_BRAIN_OS_MECE_ARCHITECTURE
    - 12_STATE/STATE_README
  scope: runtime_architecture
tags:
  - amos-os
  - runtime
  - mvcc
  - causal-epochs
  - finality
---

# 04_RUNTIME — Master Runtime Architecture

## 1. Plane Purpose

The `04_RUNTIME` plane (**Partition B: Execution Core & Effect Governance**) provides the active execution environment for AMOS transactions, task dispatching, causal epoch management, and deterministic replay.

This plane is the execution substrate where cognitive decisions become computational effects. It enforces causal ordering, isolation, and finality guarantees for all state mutations produced by the cognitive organism and its agents.

```text
RUNTIME != CONTROL_PLANE
EXECUTION != COMMIT
REPLAY != RE-EXECUTION
DOCUMENTED != IMPLEMENTED
```

---

## 2. Architecture Overview

The runtime architecture is built on three foundational principles:

1. **Causal Isolation:** Concurrent transactions execute in isolated snapshots via Multi-Version Concurrency Control (MVCC), preventing dirty reads and write skew.
2. **Epoch Finality:** All state mutations are sealed in monotonically increasing epochs. An epoch is finalized only when all constituent transactions pass invariant verification.
3. **Deterministic Replay:** Every execution trace can be replayed bit-for-bit against a verified snapshot, enabling post-hoc debugging and regression testing.

---

## 3. Key Components

1. **MVCC Causal Concurrency Engine (`CAUSAL_CONCURRENCY_MVCC.md`)**: Manages multi-version isolated state transitions with conflict detection. Each transaction reads from a consistent snapshot and writes to a new version, with conflict detection via serializable isolation level.

2. **Deterministic Causal Epoch Engine (`EPOCH_FINALITY_ENGINE.md`)**: Provides monotonic epoch stepping, barrier synchronizations, and finalized transaction receipts. Epochs advance only when all in-scope transactions have reached a terminal state (committed or aborted).

3. **Execution Replay Harness**: Enables bit-for-bit replay of historical episodic event logs against verified snapshots. Replay uses deterministic scheduling with recorded random seeds and message ordering.

4. **Task Dispatch Scheduler**: Routes cognitive tasks to available execution resources with priority queues, preemption support, and deadline-aware scheduling.

5. **Sandboxed Execution Environment**: WASI-based microVM sandboxes for untrusted code execution with capability-scoped filesystem and network access.

---

## 4. Navigation

- **MVCC Engine:** [[04_RUNTIME/CAUSAL_CONCURRENCY_MVCC|CAUSAL_CONCURRENCY_MVCC]]
- **Epoch Finality:** [[04_RUNTIME/EPOCH_FINALITY_ENGINE|EPOCH_FINALITY_ENGINE]]
- **State Plane:** [[12_STATE/12_STATE_MOC|12_STATE_MOC]]
- **Control Plane:** [[03_CONTROL_PLANE/03_CONTROL_PLANE_MOC|03_CONTROL_PLANE_MOC]]
- **Tools & Sandboxes:** [[14_TOOLS/14_TOOLS_MOC|14_TOOLS_MOC]]
- **Tests & Replay:** [[19_TESTS/19_TESTS_MOC|19_TESTS_MOC]]
- **Root Architecture:** [[00_ROOT/FULL_BRAIN_OS_MECE_ARCHITECTURE|FULL_BRAIN_OS_MECE_ARCHITECTURE]]

---

## 5. Status & Gaps

- **Status:** `ACTIVE_SPECIFICATION` — all core runtime components are documented and structurally present.
- **MVCC Implementation:** MVCC concurrency control is specified as an architectural pattern. Production-grade MVCC with serializable isolation requires integration with the state plane's Arrow IPC bus. This integration is `DOCUMENTED != IMPLEMENTED`.
- **Epoch Finality in Distributed Mode:** Distributed epoch finality across multiple nodes requires BFT consensus integration with `09_PROTOCOLS`. The integration contract is specified but not yet executed.
- **Replay Fidelity:** Deterministic replay assumes recorded message ordering and random seeds. Non-deterministic hardware behavior (e.g., floating-point rounding differences across architectures) may break replay fidelity. This remains `UNKNOWN/GAP`.
- **WASI Sandbox Maturity:** WASI-based sandboxing is specified for untrusted code execution. Production deployment requires WASI preview2 compliance verification.
