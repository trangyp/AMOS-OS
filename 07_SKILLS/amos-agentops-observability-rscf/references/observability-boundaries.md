# Observability boundaries and external mechanism provenance

Treat external repository claims as `SOURCE_CLAIM` until AMOS executes the relevant contract.

## Pinned mechanism sources

- OpenTelemetry semantic conventions `open-telemetry/semantic-conventions@a11c510432b66cca046e79908898856bf0ebfd1a`: shared GenAI/tool span vocabulary. Naming is not AMOS authority or causal proof.
- OpenTelemetry Protocol `open-telemetry/opentelemetry-proto@09f8394ecb171e889029fcd0036a3ab856c9b801`: stable OTLP trace/metric/log transport specification. OTLP/HTTP JSON uses protobuf JSON shape, base64 byte fields, integer enums, endpoint `/v1/traces`; partial success must not be retried; retryable HTTP codes are 429/502/503/504. OTLP acknowledgements cover one client/server hop, not end-to-end backend persistence.
- OpenTelemetry Collector `open-telemetry/opentelemetry-collector@a35b7a8db49df923c5add3dc34872b6e0b3af683`: bounded retry, sending queue, persistent queue/storage patterns. Persistent queues do not imply persistence of all caller context or authorization state.
- OpenTelemetry Collector Contrib `open-telemetry/opentelemetry-collector-contrib@647124d8f455e830606882e8923bf6bbd8d11e7f`: current extension ecosystem snapshot; use only mechanisms independently inspected for the task.
- OpenInference `Arize-ai/openinference@a332a5ca8f271356b48d450220e3cf364e45ccac`: end-to-end instrumentation verification by isolated run, export, and backend span read-back; process exit alone is insufficient.
- Phoenix `Arize-ai/phoenix@e12748298b366605cc0e2aa60e659f473efbff99`: trace read-back/analysis and error-analysis Skill patterns. Instrumentation gaps are evidence gaps; semantic failures can exist on non-error spans.
- OpenInference redaction `Arize-ai/openinference@e8ce013ab6e94e11c4a0f31c3e123594ce15d082`: apply capture controls before serialization/persistence.
- OpenLLMetry `traceloop/openllmetry@62e24c2ffde6c1ee04dc290e52d8d5dbda054cff`: multi-framework OpenTelemetry instrumentation patterns.
- Langfuse `langfuse/langfuse@99ecfca16d7241155c6bf705f2170f81f80b973f`: keep trace and evaluation surfaces distinct.
- AgentOps `AgentOps-AI/agentops@f8e907b92dabe47232978023fdcb01e2a7d4b752`: agent-monitoring ecosystem reference; provider-field robustness does not establish AMOS transport correctness.

## AMOS fields that must survive projection

Preserve subject/version, provenance root, environment/regime, span kind, effect state, authority reference as observation only, event vs observation time, content-capture mode, run ID, build ID, hashes, and missingness evidence.

## Transport state boundary

`QUEUED -> SENDING -> ACKED|PARTIAL|RETRYABLE|PERMANENT_FAILURE|PROTOCOL_ERROR|IN_DOUBT`.

`RECONCILED_PRESENT` means backend read-back found the trace after an ambiguous send; it is intentionally distinct from `ACKED` because no HTTP acknowledgement was observed.

- HTTP 200 with valid OTLP response and no partial-success field: `ACKED`.
- OTLP partial-success field: `PARTIAL`; do not resend the entire request automatically.
- 429/502/503/504: bounded `RETRYABLE`; honor `Retry-After` for throttling where supplied.
- 400 and other non-retryable responses: terminal failure.
- malformed HTTP 200 OTLP JSON: `PROTOCOL_ERROR`.
- disconnect/timeout/restart while `SENDING`: `IN_DOUBT`; reconcile before retry.

## Round-trip evidence

Strong backend evidence requires all of:

1. isolated trace/project/run identity;
2. exact running build identity;
3. transport attempt recorded without silently persisted credentials;
4. trace read back from backend;
5. exact span IDs and parentage;
6. expected names and required `amos.*` attributes;
7. no stale run/build contamination, duplicates, missing or extra spans.

Only that bounded comparison may return `VERIFIED_ROUNDTRIP`.

`VERIFIED_ROUNDTRIP != AUTHORIZED_EFFECT`

`VERIFIED_ROUNDTRIP != CAUSAL_PROOF`

`VERIFIED_ROUNDTRIP != SYSTEM_WIDE_INSTRUMENTATION_COMPLETENESS`

## Privacy

Default `METADATA_ONLY`. Hash payloads when content is unnecessary. Credentials/authorization headers are supplied at send time and must not enter the durable queue or receipts. Backend normalizers should ignore raw prompt/output fields unless a separately authorized analysis requires content.

Redaction and metadata-only capture reduce exposure but do not prove regulatory privacy/DLP sufficiency.
