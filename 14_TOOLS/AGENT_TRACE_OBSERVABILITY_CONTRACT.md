---
title: AMOS Agent Trace Observability Contract
type: tool_contract
status: IMPLEMENTED_LOCAL_REFERENCE
epistemic_class: AMOS_MODEL
origin_architect: Trang Phan
steward: Trang Phan
---

# AMOS Agent Trace Observability Contract

## Tool identity

```text
tool_id = amos-agent-trace-audit
entry = 17_OBSERVABILITY/agent_trace_runtime.py
validator = 07_SKILLS/amos-agentops-observability-rscf/scripts/trace_contract.py
tier = T1_READ_ONLY_ANALYSIS
```

The tool validates supplied trace artifacts. It does not attach to live processes, export telemetry, mutate authoritative state, or grant effect authority.

## Inputs

A compatible trace envelope contains:

- trace identity;
- spans with typed parent relations;
- explicit capture mode;
- explicit effect state where applicable;
- optional expected span count;
- dropped/sampled/collector/uninstrumented-path metadata;
- resource metadata.

## Outputs

On success the validator returns:

- `TRACE_CONTRACT_PASS`;
- canonical SHA-256 receipt identity;
- missingness state;
- coverage when the expected span count is known.

On failure it exits nonzero with the violated contract.

## Capability envelope

Allowed:

```text
TRACE_PARSE
TRACE_STRUCTURE_VALIDATE
MISSINGNESS_CLASSIFY
CAPTURE_POLICY_VALIDATE
EFFECT_EVIDENCE_VALIDATE
RECEIPT_HASH
ENTROPY_KL_CALCULATE
```

Not granted:

```text
LIVE_PROCESS_ATTACH
NETWORK_EXPORT
RAW_CONTENT_CAPTURE_AUTHORITY
STATE_COMMIT
EFFECT_COMMIT
CANON_PROMOTION
DEPLOYMENT
```

## Hard invariants

```text
TRACE != AUTHORITY
TRACE_EDGE != CAUSAL_PROOF
SPAN_SUCCESS != EFFECT_COMMITTED
HASH_MATCH != TRUST
NO_SPAN != NO_EVENT
SAMPLED_TRACE != COMPLETE_TRACE
```

## Privacy boundary

Metadata capture is the default local policy. Raw prompt/input/output/tool payload fields are rejected unless the artifact explicitly declares `FULL` capture plus `capture_authority_id`.

This validates presence of an authority reference only.

```text
REFERENCE_PRESENT != AUTHORITY_FRESH
CAPTURE_AUTHORIZED != PRIVACY_SAFE
```

Commit-time or export-time authority must be revalidated by the owning control plane when consequential.

## Evidence boundary

A PASS proves only that the supplied artifact satisfies the implemented local contract.

It does not prove:

- the trace is complete;
- an event really occurred in the external world;
- the source is trustworthy;
- a committed effect was actually finalized;
- the trace is OpenTelemetry protocol-conformant end-to-end;
- an annotation/evaluation is correct;
- production telemetry has acceptable latency or overhead.

## Upstream mechanism coordinates

- OpenTelemetry semantic conventions: `a11c510432b66cca046e79908898856bf0ebfd1a`
- OpenLLMetry: `62e24c2ffde6c1ee04dc290e52d8d5dbda054cff`
- Arize Phoenix: `e12748298b366605cc0e2aa60e659f473efbff99`

These are provenance coordinates, not AMOS authority roots.
