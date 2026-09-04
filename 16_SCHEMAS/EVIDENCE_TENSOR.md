---
title: "Evidence Tensor Data Schema & Arrow Layout"
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

# Evidence Tensor Data Schema & Apache Arrow Layout

**Origin Architect / Steward:** Trang Phan
**AMOS_CORE Target:** `v4.4`
**Epistemic Class:** `AMOS_MODEL`

---

## 1. Executive Summary & Epistemic Role

The **Evidence Tensor** ($\mathcal{E}$) encapsulates structured, verifiable observations, empirical measurements, and cryptographic receipts within the AMOS Full Brain OS. It enforces strict separation between raw observations ($\mathcal{E}_{obs}$) and derived claims ($\mathcal{C}_{claim}$).

```
+----------------------------------------------------------------------------------------------------+
|                         EVIDENCE TENSOR MULTIDIMENSIONAL STRUCTURE                                 |
|                                                                                                    |
|    Dimension 0: Batch / Time Index $t \in [0, T]$                                                  |
|    Dimension 1: Modality Channel (0: Telemetry, 1: Neural, 2: Document, 3: Crypto-Proof)           |
|    Dimension 2: Epistemic Confidence Interval $[\mu - \sigma, \mu + \sigma]$                       |
|    Dimension 3: BLAKE3 256-bit Digest Merkle Root Slice                                           |
+----------------------------------------------------------------------------------------------------+
```

---

## 2. Apache Arrow RecordBatch Schema Definition

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "title": "AmosEvidenceTensorRecord",
  "type": "object",
  "required": [
    "evidence_id",
    "timestamp_epoch_ns",
    "modality",
    "confidence_score",
    "entropy_bits",
    "blake3_payload_hash",
    "raw_tensor_payload"
  ],
  "properties": {
    "evidence_id": {
      "type": "string",
      "format": "uuid",
      "description": "Unique deterministic evidence identifier"
    },
    "timestamp_epoch_ns": {
      "type": "integer",
      "minimum": 0,
      "description": "Monotonic nanosecond timestamp"
    },
    "modality": {
      "type": "string",
      "enum": ["NEURAL_LFP", "OPTICAL_HD_DOT", "MARKET_TICK", "DOCUMENT_ARXIV", "CRYPTO_ZK_PROOF"]
    },
    "confidence_score": {
      "type": "number",
      "minimum": 0.0,
      "maximum": 1.0
    },
    "entropy_bits": {
      "type": "number",
      "minimum": 0.0
    },
    "blake3_payload_hash": {
      "type": "string",
      "pattern": "^[a-f0-9]{64}$"
    },
    "raw_tensor_payload": {
      "type": "array",
      "items": { "type": "number" },
      "description": "Dense flattened float32 tensor coordinates"
    }
  }
}
```

---

## 3. Schema Invariants

- `INV-SCH-001` (**Non-Null BLAKE3 Hash**): Every evidence record must compute and seal a valid 32-byte BLAKE3 payload checksum.
- `INV-SCH-002` (**Arrow Memory Alignment**): Binary representations must maintain 64-byte SIMD cache-line alignment.

---

## 4. Navigation

- **Master MOC:** [[16_SCHEMAS/16_SCHEMAS_MOC|16_SCHEMAS_MOC]]
- **Related Claims:** [[16_SCHEMAS/CLAIM_TENSOR|CLAIM_TENSOR]]
