---
title: RSCF Transaction Schema
type: schema
source: 16_SCHEMAS/10_RSCF
artifact_id: AMOS-SCHEMA-RSCF-TRANSACTION
canonical_name: RSCF_TRANSACTION_SCHEMA
artifact_type: json_yaml_schema_contract
status: CANONICAL
conclusion_class: CANONICAL
amos_core_target: v4.4
origin_architect: Trang Phan
steward: Trang Phan
plane: 16_SCHEMAS
segment: 16_SCHEMAS/10_RSCF
schema_family: RSCF
domain: transactions
scope: AMOS_OS
created: '2026-08-25'
updated: '2026-08-28'
tags:
- amos-os
- schema
- rscf
- transaction-schema
- atomic-mutation
- rollback-basin
- acid-contracts
- rscf/claim
- rscf/state/canonical
- 10-rscf-moc
- 16-schemas-moc
- 00-home
- 00-root-moc
aliases:
- RSCF Transaction Schema
- Transaction Schema Contract
- rscf_transaction.schema
- AMOS State Mutation Transaction Specification
---

# RSCF Transaction Schema

> **Origin Architect / Steward:** Trang Phan  
> **Plane:** `16_SCHEMAS/10_RSCF`  
> **Status:** `CANONICAL`  
> **Integrity:** ACID Invariants $\times$ Explicit Rollback Basin $\times$ Two-Phase Commit

---

## 1. Schema Purpose

`RSCF_TRANSACTION_SCHEMA` specifies the formal interface for all state mutations, note additions, tag updates, and dependency graph edits within AMOS OS. It guarantees that multi-file changes either complete in their entirety or cleanly abort and rollback without leaving orphan nodes or broken wikilinks.

```
+-------------------------------------------------------------------------+
|                    RSCF TRANSACTION LIFECYCLE                           |
|                                                                         |
|  [ PROPOSE ] -> Traverse Dependency Closure & Check Authority Tiers     |
|      |                                                                  |
|      v                                                                  |
|  [ STAGE ]   -> Snapshot Pre-State into Rollback Basin & Validate Type  |
|      |                                                                  |
|      v                                                                  |
|  [ COMMIT ]  -> Apply Atomic Write, Emit Proof Capsules & Update Index  |
|      |                                                                  |
|      v (On Any Invariant Violation)                                     |
|  [ ABORT / ROLLBACK ] -> Restore Pre-State Snapshot & Record Log        |
+-------------------------------------------------------------------------+
```

---

## 2. Formal JSON Schema Specification

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "https://amos-os.org/schemas/rscf/rscf_transaction.schema.json",
  "title": "AMOS_RSCF_Transaction",
  "type": "object",
  "required": [
    "tx_id",
    "initiator_agent",
    "timestamp",
    "mutations",
    "rollback_snapshot_ref",
    "authorization_receipt",
    "status"
  ],
  "properties": {
    "tx_id": {
      "type": "string",
      "format": "uuid"
    },
    "initiator_agent": {
      "type": "string"
    },
    "timestamp": {
      "type": "string",
      "format": "date-time"
    },
    "mutations": {
      "type": "array",
      "items": {
        "type": "object",
        "required": ["target_file", "operation", "payload"],
        "properties": {
          "target_file": { "type": "string" },
          "operation": { "type": "string", "enum": ["CREATE", "MODIFY", "DELETE", "LINK"] },
          "payload": { "type": "object" }
        }
      },
      "minItems": 1
    },
    "rollback_snapshot_ref": {
      "type": "string"
    },
    "authorization_receipt": {
      "type": "string"
    },
    "status": {
      "type": "string",
      "enum": ["PROPOSED", "STAGED", "COMMITTED", "ABORTED", "ROLLED_BACK"]
    }
  },
  "additionalProperties": false
}
```

---

## 3. Invariant Validation Rules

1. **Pre-Snapshot Mandate:** A transaction cannot advance to `COMMITTED` unless `rollback_snapshot_ref` is non-null and points to a verified filesystem snapshot.
2. **Deterministic Rollback:** If any mutation in the batch raises a schema or invariant violation, every mutation in that transaction is reverted immediately.
3. **No Unsigned Transactions:** `authorization_receipt` must validate against an epoch-valid authorization token.

---

## 4. Cross-Plane Bindings

- **Kernel Protocols:** [[K_RSCF]] · [[K_CONTROL_PLANE]] · [[K_FAIL_CLOSED]]
- **Schemas:** [[PROOF_CAPSULE_SCHEMA]] · [[CAUSAL_EPOCH_SCHEMA]]
- **Navigation:** [[00_HOME]] · [[16_SCHEMAS_MOC]] · [[10_RSCF_MOC]] · [[00_ROOT_MOC]]

