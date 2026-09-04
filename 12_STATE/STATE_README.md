---
title: "12_STATE — Causal State Substrate & Epoch Architecture"
type: architecture_specification
source: 12_STATE
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
    - 04_RUNTIME/RUNTIME_RUNTIME_CONTRACT
    - AMOS_CORE_v4_0_to_v4_4_lineage
  scope: state_architecture
tags:
  - amos-os
  - state
  - mvcc
  - causal-epochs
  - rollback-basin
---

# 12_STATE — Master State Substrate

## 1. Purpose & Hard Invariants

The `12_STATE` plane models the active and historical state of the AMOS operating system across all cognitive organs, runtime shards, and persistent databases.

```text
STATE != MODEL
STATE != KNOWLEDGE
PROPOSAL != COMMIT
MUTATION != FINALITY
```

## 2. MVCC Causal State Architecture

```mermaid
graph LR
    S0[Epoch E_0<br/>Genesis State] --> S1[Epoch E_1<br/>Shard A Commit]
    S0 --> S2[Epoch E_1'<br/>Shard B Commit]
    S1 --> S3[Epoch E_2<br/>Causal Merge]
    S2 --> S3
    S3 --> S4[Epoch E_3<br/>Finalized State]
```

### 2.1 Causal State Graph (`CAUSAL_STATE_GRAPH.md`)
- Multi-Version Concurrency Control (MVCC) with vector clocks.
- Immutable state snapshots: modifying state creates a new epoch version rather than mutating existing data in place.

### 2.2 Epoch Progression (`EPOCH_PROGRESSION_SPEC.md`)
- Monotonically increasing epoch counters (`E_k -> E_{k+1}`).
- Deterministic commit gates: a transaction is committed only when all invariant checks and authority verifications pass.

### 2.3 Rollback Basin (`ROLLBACK_BASIN_PROTOCOL.md`)
- Guaranteed recovery path: every state transition maintains an inverse compensation receipt.
- Failure containment: corrupted state is rolled back to the nearest verified snapshot without polluting unaffected shards.
