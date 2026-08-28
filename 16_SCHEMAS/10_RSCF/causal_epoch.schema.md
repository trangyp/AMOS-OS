---
title: Causal Epoch Schema (RSCF)
type: schema
source: 16_SCHEMAS/10_RSCF
artifact_id: AMOS-SCHEMA-CAUSAL-EPOCH
canonical_name: CAUSAL_EPOCH_SCHEMA
artifact_type: json_yaml_schema_contract
status: CANONICAL
conclusion_class: CANONICAL
amos_core_target: v4.4
origin_architect: Trang Phan
steward: Trang Phan
plane: 16_SCHEMAS
segment: 16_SCHEMAS/10_RSCF
schema_family: RSCF
domain: causal-epochs
scope: AMOS_OS
created: '2026-08-25'
updated: '2026-08-28'
tags:
- amos-os
- schema
- rscf
- causal-epoch
- lamport-timestamps
- monotonic-clock
- merkle-dag-hash
- rscf/claim
- rscf/state/canonical
- 10-rscf-moc
- 16-schemas-moc
- 00-home
- 00-root-moc
aliases:
- Causal Epoch Schema
- Epoch Invariant Contract
- causal_epoch.schema
- AMOS Causal Ordering Specification
---

# Causal Epoch Schema (RSCF)

> **Origin Architect / Steward:** Trang Phan  
> **Plane:** `16_SCHEMAS/10_RSCF`  
> **Status:** `CANONICAL`  
> **Temporal Standard:** Monotonic Epoch Counter $\times$ Merkle DAG Hash $\times$ Strict Lamport Causality

---

## 1. Schema Purpose

`CAUSAL_EPOCH_SCHEMA` defines the global ordering, timestamping, and state-snapshot structure for all events in AMOS OS. It guarantees chronological consistency across distributed agents, ensuring that effect never precedes cause and that stale reads are immediately detected and rejected.

```
+-------------------------------------------------------------------------+
|                       CAUSAL EPOCH ARCHITECTURE                         |
|                                                                         |
|  [ Epoch t - 1 ] (Hash: H_{t-1})                                        |
|         |                                                               |
|         v                                                               |
|  [ Epoch Transition Delta: Validated Transactions & Proof Capsules ]   |
|         |                                                               |
|         v                                                               |
|  [ Epoch t ] (Hash: H_t = SHA256(H_{t-1} + Delta + Timestamp) )         |
|         |                                                               |
|         v                                                               |
|  [ Epoch State Commitment & Merkle Tree Root Broadcast ]                |
+-------------------------------------------------------------------------+
```

---

## 2. Formal JSON Schema Specification

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "https://amos-os.org/schemas/rscf/causal_epoch.schema.json",
  "title": "AMOS_Causal_Epoch",
  "type": "object",
  "required": [
    "epoch_id",
    "epoch_index",
    "parent_epoch_hash",
    "current_epoch_hash",
    "epoch_timestamp",
    "transaction_ids",
    "merkle_root"
  ],
  "properties": {
    "epoch_id": {
      "type": "string",
      "format": "uuid"
    },
    "epoch_index": {
      "type": "integer",
      "minimum": 0
    },
    "parent_epoch_hash": {
      "type": "string",
      "pattern": "^[a-f0-9]{64}$"
    },
    "current_epoch_hash": {
      "type": "string",
      "pattern": "^[a-f0-9]{64}$"
    },
    "epoch_timestamp": {
      "type": "string",
      "format": "date-time"
    },
    "transaction_ids": {
      "type": "array",
      "items": { "type": "string", "format": "uuid" }
    },
    "merkle_root": {
      "type": "string",
      "pattern": "^[a-f0-9]{64}$"
    }
  },
  "additionalProperties": false
}
```

---

## 3. Invariant Validation Rules

1. **Monotonic Index Law:** $\text{epoch\_index}_t = \text{epoch\_index}_{t-1} + 1$.
2. **Cryptographic Chaining:** $\text{current\_epoch\_hash} = \text{SHA256}(\text{parent\_epoch\_hash} \,||\, \text{merkle\_root} \,||\, \text{epoch\_timestamp})$.
3. **No Retroactive Mutation:** Once an epoch hash is committed, all descendant operations referencing past epochs treat them as immutable read-only baselines.

---

## 4. Cross-Plane Bindings

- **Causal Kernels:** [[K_REALITY_CAUSALITY]] · [[K_QUANTUM_CAUSALITY]] · [[K_CROSS_SCALE_CAUSALITY]]
- **Transactions & Proofs:** [[RSCF_TRANSACTION_SCHEMA]] · [[PROOF_CAPSULE_SCHEMA]]
- **Navigation:** [[00_HOME]] · [[16_SCHEMAS_MOC]] · [[10_RSCF_MOC]] · [[00_ROOT_MOC]]

