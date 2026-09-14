---
title: AMOS Agent Trace Transport Verifier
type: tool-contract
origin_architect: Trang Phan
epistemic_class: AMOS_MODEL
status: IMPLEMENTED_LOCAL_REFERENCE
---

# AMOS Agent Trace Transport Verifier

## Purpose

Project closed AMOS traces into bounded OTLP/HTTP JSON, persist them in a durable local outbox, classify transport outcomes, and verify exact backend read-back evidence.

## Capability envelope

Local encoding, queue inspection and receipt validation are non-networked deterministic operations. Actual export/read-back is **T3 external network activity** and requires separately supplied endpoint/credential authority.

Capabilities:

- `TRACE_READ`
- `OTLP_HTTP_JSON_PROJECT`
- `DURABLE_OUTBOX_LOCAL`
- `TRANSPORT_RECEIPT_VALIDATE`
- `BACKEND_TRACE_READBACK` when explicitly authorized
- `ROUNDTRIP_COMPARE`

Not capabilities:

- mint credentials or authority;
- modify backend data;
- promote an effect to committed;
- infer causality from trace topology;
- claim system-wide instrumentation completeness.

## State contract

`QUEUED -> SENDING -> ACKED|PARTIAL|RETRYABLE|PERMANENT_FAILURE|PROTOCOL_ERROR|IN_DOUBT`

`IN_DOUBT -> RECONCILED_PRESENT|QUEUED` only after evidence-bound backend reconciliation.

## Firewalls

- `CAPABILITY != AUTHORITY`
- `HTTP_ACK != BACKEND_READBACK_VERIFIED`
- `EXPORT_PROCESS_SUCCESS != TRACE_ARRIVED`
- `IN_DOUBT != SAFE_TO_BLIND_RETRY`
- `PERSISTENT_QUEUE != AUTHORITY_CONTEXT_PERSISTENCE`
- `BACKEND_READBACK_MATCH != CAUSAL_PROOF`
- `TRANSPORT_CREDENTIAL != DURABLE_TELEMETRY_FIELD`

## Executable binding

- Runtime: `17_OBSERVABILITY/trace_transport_runtime.py`
- Tests: `19_TESTS/test_trace_transport_runtime.py`
- Receipt validator: `07_SKILLS/amos-agentops-observability-rscf/scripts/transport_roundtrip_check.py`
- CI: `.github/workflows/trace-transport-roundtrip-contract.yml`

Current evidence is bounded to the local reference runtime, mock HTTP server, durable SQLite outbox, deterministic verifier, and CI. A real external backend round-trip remains `UNKNOWN/GAP` until executed against a named isolated backend/project and read back successfully.
