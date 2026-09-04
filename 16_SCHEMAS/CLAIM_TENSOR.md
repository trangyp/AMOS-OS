---
title: "Claim Tensor Data Schema & Proof Merkle Tree"
type: data_schema
source: 16_SCHEMAS
amos_core_target: v4.4
origin_architect: Trang Phan
steward: Trang Phan
status: ACTIVE_SPECIFICATION
epistemic_class: AMOS_MODEL
conclusion_class: DERIVED
rscf:
  state: DERIVED
  provenance: authoritative_AMOS_OS_structure
  scope: active__AMOS_OS
---

# Claim Tensor Data Schema & Proof Merkle Tree

**Origin Architect / Steward:** Trang Phan
**AMOS_CORE Target:** `v4.4`
**Epistemic Class:** `AMOS_MODEL`

---

## 1. Executive Summary & Epistemic Role

The **Claim Tensor** ($\mathcal{C}$) represents derived inferences, predictive hypotheses, and cognitive propositions. It requires explicit bidirectional links to supporting Evidence Tensors ($\mathcal{E}$) and a declared epistemic conclusion class (`SOURCE_CLAIM`, `OBSERVATION`, `DERIVED`, `AMOS_MODEL`, `DECISION`, `COMPETING`, or `UNKNOWN/GAP`).

```
+----------------------------------------------------------------------------------------------------+
|                         CLAIM TENSOR PROVENANCE & MERKLE DAG STRUCTURE                             |
|                                                                                                    |
|    [ Claim Tensor $\mathcal{C}$ ] ===> [ Epistemic Class ] ===> [ Mathematical Statement / Loss ] |
|                   ||                                                                               |
|                   \/                                                                               |
|    [ Supporting Evidence Hashes $\mathcal{E}_1, \dots, \mathcal{E}_k$ ]                            |
|                   ||                                                                               |
|                   \/                                                                               |
|    [ Formal Derivation Proof DAG (Lean 4 / SMT Solver Token) ]                                     |
+----------------------------------------------------------------------------------------------------+
```

---

## 2. JSON Schema Definition

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "title": "AmosClaimTensorRecord",
  "type": "object",
  "required": [
    "claim_id",
    "epistemic_conclusion_class",
    "supporting_evidence_ids",
    "confidence_bound",
    "falsification_criteria",
    "origin_architect"
  ],
  "properties": {
    "claim_id": {
      "type": "string",
      "format": "uuid"
    },
    "epistemic_conclusion_class": {
      "type": "string",
      "enum": [
        "SOURCE_CLAIM",
        "OBSERVATION",
        "DERIVED",
        "AMOS_MODEL",
        "DECISION",
        "COMPETING",
        "UNKNOWN_GAP"
      ]
    },
    "supporting_evidence_ids": {
      "type": "array",
      "items": { "type": "string", "format": "uuid" },
      "minItems": 1
    },
    "confidence_bound": {
      "type": "number",
      "minimum": 0.0,
      "maximum": 1.0
    },
    "falsification_criteria": {
      "type": "string",
      "description": "Concrete empirical observation that would invalidate this claim"
    },
    "origin_architect": {
      "type": "string",
      "default": "Trang Phan"
    }
  }
}
```

---

## 3. Invariants & Falsifiability Rules

- `INV-CLM-001` (**Non-Empty Evidence Closure**): No claim of class `DERIVED` or `DECISION` may exist without at least one valid supporting `EVIDENCE_TENSOR` reference.
- `INV-CLM-002` (**Mandatory Falsifier**): Every scientific or model claim must define a non-empty `falsification_criteria` predicate.

---

## 4. Navigation

- **Master MOC:** [[16_SCHEMAS/16_SCHEMAS_MOC|16_SCHEMAS_MOC]]
- **Evidence Schema:** [[16_SCHEMAS/EVIDENCE_TENSOR|EVIDENCE_TENSOR]]
