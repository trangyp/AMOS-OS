# Observability boundaries and external mechanism provenance

## Source coordinates

Treat all external repository claims as `SOURCE_CLAIM` until independently validated in AMOS.

- OpenTelemetry semantic conventions: `open-telemetry/semantic-conventions@a11c510432b66cca046e79908898856bf0ebfd1a`.
  - Useful mechanism: consistent trace/span attributes and GenAI/tool-call semantic vocabulary.
  - Boundary: semantic naming does not confer AMOS authority, provenance admission, or causal validity.
- OpenLLMetry: `traceloop/openllmetry@62e24c2ffde6c1ee04dc290e52d8d5dbda054cff`.
  - Useful mechanism: OpenTelemetry-based LLM/agent instrumentation across model/tool frameworks.
  - Boundary: instrumentation coverage and exporter success must be observed, not assumed.
- OpenInference: `Arize-ai/openinference@a332a5ca8f271356b48d450220e3cf364e45ccac`.
  - Useful mechanism: prove instrumentation end-to-end by exporting to an isolated project and reading spans back; empty-project/run-tag discipline prevents stale spans from being mistaken for evidence.
- OpenInference redaction change: `Arize-ai/openinference@e8ce013ab6e94e11c4a0f31c3e123594ce15d082`.
  - Useful mechanism: apply capture configuration before serialization/persistence; recursively redact sensitive media/content.
- Langfuse: `langfuse/langfuse@99ecfca16d7241155c6bf705f2170f81f80b973f`.
  - Useful mechanism: traces and evaluations remain separate operational surfaces; observability data can be analyzed without becoming ground truth.

## AMOS extensions that must survive projection

Any external telemetry adapter should preserve or encode:

- AMOS subject identity/version;
- provenance root;
- environment/regime;
- span kind;
- effect state;
- authority-reference identity as observation only;
- missingness/coverage;
- event time vs observation time;
- content-capture mode;
- receipt/hash identity.

Dropping one of these fields may make the projection insufficient for AMOS reasoning even if the external backend accepts the span.

## Privacy/capture rules

Default: `METADATA_ONLY`.

Store hashes of payloads when identity/change detection is sufficient. Opt into `REDACTED_CONTENT` only when content inspection changes the decision and the caller has authority to persist it.

Redaction is risk reduction, not proof that all sensitive data was removed. High-stakes deployments need environment-specific DLP/privacy validation.

## End-to-end trace evidence

For a real exporter/instrumentor, a process exit code of zero is insufficient. Stronger evidence requires:

1. isolated target/project/trace namespace;
2. exporter configured to that target;
3. run log checked for export failures;
4. spans read back from the backend;
5. exact expected attributes/topology verified;
6. subject/build identity bound to the running code;
7. coverage/missingness recorded.

Until those checks are executed, classify backend integration as `UNKNOWN/GAP` or `CONDITIONAL`, not verified.
