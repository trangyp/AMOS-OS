---
title: Proof Capsule Schema (RSCF)
type: schema
source: 16_SCHEMAS/10_RSCF
artifact_id: AMOS-SCHEMA-PROOF-CAPSULE
canonical_name: PROOF_CAPSULE_SCHEMA
artifact_type: json_yaml_schema_contract
status: CANONICAL
conclusion_class: CANONICAL
amos_core_target: v4.4
origin_architect: Trang Phan
steward: Trang Phan
plane: 16_SCHEMAS
segment: 16_SCHEMAS/10_RSCF
schema_family: RSCF
domain: proof-capsules
scope: AMOS_OS
created: '2026-08-25'
updated: '2026-08-28'
tags:
- amos-os
- schema
- rscf
- proof-capsule
- epistemic-verification
- confidence-ceiling
- cryptographic-receipt
- rscf/claim
- rscf/state/canonical
- 10-rscf-moc
- 16-schemas-moc
- 00-home
- 00-root-moc
aliases:
- Proof Capsule Schema
- RSCF Proof Capsule Contract
- proof_capsule.schema
- AMOS Proof Capsule Specification
---

# Proof Capsule Schema (RSCF)

> **Origin Architect / Steward:** Trang Phan  
> **Plane:** `16_SCHEMAS/10_RSCF`  
> **Status:** `CANONICAL`  
> **Standard:** Strict Typed JSON/YAML Schema $\times$ Ed25519 Signature $\times$ Confidence Floor/Ceiling Enforced

---

## 1. Schema Purpose

The **Proof Capsule** is the fundamental atomic unit of verified knowledge in AMOS OS. Every load-bearing mathematical, logical, empirical, or systemic claim produced or ingested by the system must validate against this schema before it can authorize state transitions or downstream conclusions.

```
+-------------------------------------------------------------------------+
|                      PROOF CAPSULE STRUCTURE                            |
|                                                                         |
|  +-------------------------------------------------------------------+  |
|  | capsule_id: UUIDv4                                                |  |
|  | target_claim_node: Wikilink (e.g., [[K_CORE_LAWS]])              |  |
|  | epistemic_class: EMPIRICAL | AMOS_MODEL | DERIVED | HYPOTHESIS   |  |
|  | confidence: float [0.00 .. 0.95] (Max 0.95 for empirical)        |  |
|  | premises: list of string [ UUIDv4 / URI ]                         |  |
|  | falsifiers: list of string [ Explicit falsification tests ]      |  |
|  | bounds: list of object { name, lower_bound, upper_bound }         |  |
|  | invariants: list of string [ Invariant algebraic statements ]     |  |
|  | authorizing_epoch: string [ SHA-256 Epoch State Hash ]           |  |
|  | signature: string [ Ed25519 cryptographic attestation ]           |  |
|  +-------------------------------------------------------------------+  |
+-------------------------------------------------------------------------+
```

---

## 2. Formal JSON Schema Specification

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "https://amos-os.org/schemas/rscf/proof_capsule.schema.json",
  "title": "AMOS_RSCF_Proof_Capsule",
  "type": "object",
  "required": [
    "capsule_id",
    "target_claim_node",
    "epistemic_class",
    "confidence",
    "premises",
    "falsifiers",
    "authorizing_epoch",
    "signature"
  ],
  "properties": {
    "capsule_id": {
      "type": "string",
      "format": "uuid"
    },
    "target_claim_node": {
      "type": "string",
      "pattern": "^\\[\\[[A-Za-z0-9_\\-\\.]+\\]\\]$"
    },
    "epistemic_class": {
      "type": "string",
      "enum": ["EMPIRICAL", "AMOS_MODEL", "DERIVED", "HYPOTHESIS", "GAP"]
    },
    "confidence": {
      "type": "number",
      "minimum": 0.0,
      "maximum": 0.95
    },
    "premises": {
      "type": "array",
      "items": { "type": "string" },
      "minItems": 0
    },
    "falsifiers": {
      "type": "array",
      "items": { "type": "string" },
      "minItems": 1
    },
    "bounds": {
      "type": "array",
      "items": {
        "type": "object",
        "required": ["name", "lower_bound", "upper_bound"],
        "properties": {
          "name": { "type": "string" },
          "lower_bound": { "type": ["number", "string"] },
          "upper_bound": { "type": ["number", "string"] }
        }
      }
    },
    "authorizing_epoch": {
      "type": "string",
      "pattern": "^[a-f0-9]{64}$"
    },
    "signature": {
      "type": "string"
    }
  },
  "additionalProperties": false
}
```

---

## 3. Invariant Validation Rules

1. **Weakest Premise Bound:** $\text{confidence} \le \min_{p \in \text{premises}}(\text{confidence}(p))$.
2. **Ceiling Compliance:** If $\text{epistemic\_class} \ne \text{MATHEMATICAL\_AXIOM}$, $\text{confidence} \le 0.95$.
3. **No Empty Falsifiers:** Every valid proof capsule must provide at least one concrete condition that would falsify the claim.

---

## 4. Cross-Plane Bindings

- **Kernel Protocols:** [[K_RSCF]] · [[K_CIL]] · [[K_CORE_LAWS]]
- **Related Schemas:** [[RSCF_TRANSACTION_SCHEMA]] · [[CAUSAL_EPOCH_SCHEMA]] · [[COMPETING_HYPOTHESIS_SCHEMA]]
- **Navigation:** [[00_HOME]] · [[16_SCHEMAS_MOC]] · [[10_RSCF_MOC]] · [[00_ROOT_MOC]]

