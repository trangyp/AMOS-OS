---
title: Runtime Session Schema
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
    - 16_SCHEMAS/01_RUNTIME/01_RUNTIME_MOC
  scope: runtime_session_schema
tags:
  - amos-os
  - 16_schemas
  - runtime
  - session-schema
---

# Runtime Session Schema

> **Origin Architect / Steward:** Trang Phan  
> **AMOS_CORE Target:** `v4.4`  
> **Epistemic Class:** `AMOS_MODEL`  
> **Conclusion Class:** `DERIVED`

---

## 1. Formal JSON Schema

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "https://amos-os.org/schemas/runtime/v4.4/runtime_session.json",
  "title": "AmosRuntimeSession",
  "type": "object",
  "required": [
    "session_id",
    "epoch",
    "active_tick",
    "origin_steward",
    "status",
    "lease_ttl_ms",
    "task_dag",
    "state_hash"
  ],
  "properties": {
    "session_id": {
      "type": "string",
      "format": "uuid"
    },
    "epoch": {
      "type": "integer",
      "minimum": 1
    },
    "active_tick": {
      "type": "integer",
      "minimum": 0
    },
    "origin_steward": {
      "type": "string",
      "const": "Trang Phan"
    },
    "amos_core_target": {
      "type": "string",
      "const": "v4.4"
    },
    "status": {
      "type": "string",
      "enum": ["BOOTING", "ACTIVE", "WAITING_DEPENDENCY", "COMMITTING", "TERMINATED", "FAILED_CLOSED"]
    },
    "lease_ttl_ms": {
      "type": "integer",
      "maximum": 60000
    },
    "state_hash": {
      "type": "string",
      "pattern": "^[a-f0-9]{64}$"
    },
    "task_dag": {
      "type": "array",
      "items": {
        "type": "object",
        "required": ["task_id", "agent_id", "dependencies", "status"],
        "properties": {
          "task_id": { "type": "string" },
          "agent_id": { "type": "string" },
          "dependencies": { "type": "array", "items": { "type": "string" } },
          "status": { "type": "string", "enum": ["PENDING", "RUNNING", "COMPLETED", "FAILED"] }
        }
      }
    }
  },
  "additionalProperties": false
}
```

---

## 2. Invariants

- **INV-RSS-001 (Lease Bound):** Active worker leases must expire within $60\text{ s}$ without heartbeats.
- **INV-RSS-002 (Epoch Integrity):** The session epoch must match the global monotonically increasing CAS state.
- **INV-RSS-003 (Origin Stewardship):** Origin steward is strictly bound to Trang Phan under AMOS v4.4.

---

## 3. Navigation

- [[16_SCHEMAS/01_RUNTIME/01_RUNTIME_MOC|01_RUNTIME_MOC]]
- [[04_RUNTIME/RUNTIME_RUNTIME_CONTRACT|RUNTIME_RUNTIME_CONTRACT]]
