---
title: Causal Transition Schema
source: 16_SCHEMAS/01_RUNTIME
type: schema_definition
origin_architect: Trang Phan
steward: Trang Phan
amos_core_target: v4.4
status: ACTIVE_SCHEMA
epistemic_class: AMOS_MODEL
conclusion_class: DERIVED
rscf:
  state: DERIVED
  claim_class: AMOS_MODEL
  provenance:
    - 04_RUNTIME/RUNTIME_RUNTIME_CONTRACT
    - 02_KERNEL/03_CAUSAL/00_INDEX/CAUSAL_MAP
    - 16_SCHEMAS/01_RUNTIME/01_RUNTIME_MOC
  scope: causal_transition_schema
tags:
  - amos-os
  - 16_schemas
  - runtime
  - causal-dag
  - transition-schema
---

# Causal Transition Schema

> **Origin Architect / Steward:** Trang Phan  
> **AMOS_CORE Target:** `v4.4`  
> **Epistemic Class:** `AMOS_MODEL`  
> **Conclusion Class:** `DERIVED`

---

## 1. Formal JSON Schema

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "https://amos-os.org/schemas/runtime/v4.4/causal_transition.json",
  "title": "AmosCausalTransition",
  "type": "object",
  "required": [
    "transition_id",
    "prior_epoch",
    "next_epoch",
    "pre_state_hash",
    "post_state_hash",
    "causal_parents",
    "delta_payload",
    "receipt_signature"
  ],
  "properties": {
    "transition_id": {
      "type": "string",
      "format": "uuid"
    },
    "prior_epoch": {
      "type": "integer",
      "minimum": 0
    },
    "next_epoch": {
      "type": "integer",
      "minimum": 1
    },
    "pre_state_hash": {
      "type": "string",
      "pattern": "^[a-f0-9]{64}$"
    },
    "post_state_hash": {
      "type": "string",
      "pattern": "^[a-f0-9]{64}$"
    },
    "causal_parents": {
      "type": "array",
      "minItems": 1,
      "items": { "type": "string", "pattern": "^[a-f0-9]{64}$" }
    },
    "delta_payload": {
      "type": "object",
      "required": ["mutation_type", "affected_planes", "changeset_digest"],
      "properties": {
        "mutation_type": { "type": "string", "enum": ["INSERT", "UPDATE", "REPAIR", "DEPRECATE"] },
        "affected_planes": { "type": "array", "items": { "type": "string" } },
        "changeset_digest": { "type": "string", "pattern": "^[a-f0-9]{64}$" }
      }
    },
    "receipt_signature": {
      "type": "string",
      "description": "Ed25519 signature of the transition envelope"
    }
  },
  "additionalProperties": false
}
```

---

## 2. Invariants

- **INV-CTS-001 (Monotonic Progress):** `next_epoch == prior_epoch + 1`.
- **INV-CTS-002 (Causal Acyclicity):** Causal parent hashes must form a directed acyclic graph (DAG) anchored to valid preceding transactions.
- **INV-CTS-003 (Stewardship):** Lineage stewardship held by Trang Phan under AMOS v4.4.

---

## 3. Navigation

- [[16_SCHEMAS/01_RUNTIME/01_RUNTIME_MOC|01_RUNTIME_MOC]]
- [[02_KERNEL/K_CAS|K_CAS]]
- [[04_RUNTIME/RUNTIME_RUNTIME_CONTRACT|RUNTIME_RUNTIME_CONTRACT]]
