---
title: amos-agentops-observability-rscf-workflow
type: workflow
skill: amos-agentops-observability-rscf
agent: amos-agentops-observability-rscf-agent
origin_architect: Trang Phan
version: 3.0.0
epistemic_class: AMOS_MODEL
---

# AMOS AgentOps Observability Workflow

State machine:

`INTAKE -> BIND -> LOCAL_TRACE_VERIFIED -> ENCODED -> QUEUED -> SENDING -> TRANSPORT_CLASSIFIED -> READBACK -> ROUNDTRIP_GATE -> RECEIPT -> TERMINAL`

## Gates

1. **INTAKE/BIND** — define the observed claim; bind trace, subject/version, environment, provenance root, run ID and build ID.
2. **LOCAL_TRACE_VERIFIED** — require closed typed spans, explicit missingness and intact trace ledger.
3. **ENCODED** — project one trace to bounded OTLP/HTTP JSON; preserve required `amos.*` attributes; persist no transport secrets.
4. **QUEUED/SENDING** — write the exact payload to the durable outbox before network send.
5. **TRANSPORT_CLASSIFIED** — distinguish `ACKED`, `PARTIAL`, `RETRYABLE`, `PERMANENT_FAILURE`, `PROTOCOL_ERROR`, and `IN_DOUBT`.
6. **READBACK** — query an isolated backend/project/run identity. Process exit or HTTP ACK alone is insufficient.
7. **ROUNDTRIP_GATE** — exact-match trace/span IDs, parentage, names, run/build IDs and required AMOS attributes; reject stale, duplicate, missing, extra or mismatched evidence.
8. **RECEIPT** — validate trace, transport and round-trip receipts.
9. **TERMINAL** — return `VERIFIED_ROUNDTRIP`, `NOT_VERIFIED`, `PARTIAL`, `IN_DOUBT`, `PERMANENT_FAILURE`, `PROTOCOL_ERROR`, or `INVALIDATED_EVIDENCE` with gaps.

## Non-compensatory firewalls

- `HTTP_ACK != BACKEND_READBACK_VERIFIED`
- `EXPORT_PROCESS_SUCCESS != TRACE_ARRIVED`
- `IN_DOUBT != SAFE_TO_BLIND_RETRY`
- `PERSISTENT_QUEUE != AUTHORITY_CONTEXT_PERSISTENCE`
- `VERIFIED_ROUNDTRIP != AUTHORITY`
- `VERIFIED_ROUNDTRIP != CAUSAL_PROOF`

## Recovery

- 429/502/503/504: bounded protocol retry; honor `Retry-After` when supplied.
- Partial success: preserve `PARTIAL`; do not resend the whole request automatically.
- Timeout/disconnect/restart while sending: `IN_DOUBT`; backend read-back must discriminate before retry.
- Trace found after ambiguous send: `RECONCILED_PRESENT`, never rewrite history to HTTP `ACKED`.
- Stale run/build contamination or topology mismatch: `NOT_VERIFIED`.
- Missing authority: record the gap; telemetry cannot mint it.

## Validation surfaces

- `python -m unittest -v 19_TESTS/test_agent_trace_runtime.py`
- `python -m unittest -v 19_TESTS/test_trace_transport_runtime.py`
- `python 07_SKILLS/amos-agentops-observability-rscf/scripts/trace_contract_check.py --self-test`
- `python 07_SKILLS/amos-agentops-observability-rscf/scripts/transport_roundtrip_check.py --self-test`

GitHub CI is the branch validation authority for the repository copy.
