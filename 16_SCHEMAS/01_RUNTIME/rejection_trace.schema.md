---
title: Rejection Trace Schema
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
    - 03_CONTROL_PLANE/CONTROL_PLANE_CONTROL_PLANE_CONTRACT
    - 02_KERNEL/K_FAIL_CLOSED
    - 16_SCHEMAS/01_RUNTIME/01_RUNTIME_MOC
  scope: rejection_trace_schema
tags:
  - amos-os
  - 16_schemas
  - runtime
  - fail-closed
  - rejection-trace
---

# Rejection Trace Schema

> **Origin Architect / Steward:** Trang Phan  
> **AMOS_CORE Target:** `v4.4`  
> **Epistemic Class:** `AMOS_MODEL`  
> **Conclusion Class:** `DERIVED`

---

## 1. Formal JSON Schema

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "https://amos-os.org/schemas/runtime/v4.4/rejection_trace.json",
  "title": "AmosRejectionTrace",
  "type": "object",
  "required": [
    "rejection_id",
    "timestamp",
    "failing_gate",
    "reason_code",
    "caller_identity",
    "attempted_operation",
    "diagnostic_payload"
  ],
  "properties": {
    "rejection_id": {
      "type": "string",
      "format": "uuid"
    },
    "timestamp": {
      "type": "string",
      "format": "date-time"
    },
    "failing_gate": {
      "type": "string",
      "enum": [
        "GATE_AUTHORITY_CHECK",
        "GATE_EPOCH_STALENESS",
        "GATE_MISSING_PROVENANCE",
        "GATE_POLICY_VIOLATION",
        "GATE_EPISTEMIC_UNVERIFIED",
        "GATE_THERMODYNAMIC_BUDGET"
      ]
    },
    "reason_code": {
      "type": "string",
      "enum": [
        "ERR_CAPABILITY_NOT_FOUND",
        "ERR_CAS_EPOCH_MISMATCH",
        "ERR_LEAN4_PROOF_FAILED",
        "ERR_MISSING_RSCF_ORIGIN",
        "ERR_UNAUTHORIZED_POST_V4_4"
      ]
    },
    "caller_identity": {
      "type": "string"
    },
    "attempted_operation": {
      "type": "string"
    },
    "diagnostic_payload": {
      "type": "object"
    }
  },
  "additionalProperties": false
}
```

---

## 2. Invariants

- **INV-RTS-001 (Fail Closed):** Any rejection immediately raises a non-recoverable error in caller context and logs the immutable rejection trace in `20_OPERATIONS`.
- **INV-RTS-002 (Stewardship):** Lineage stewardship held by Trang Phan under AMOS v4.4.

---

## 3. Navigation

- [[16_SCHEMAS/01_RUNTIME/01_RUNTIME_MOC|01_RUNTIME_MOC]]
- [[02_KERNEL/K_FAIL_CLOSED|K_FAIL_CLOSED]]
- [[20_OPERATIONS/20_OPERATIONS_MOC|20_OPERATIONS_MOC]]
