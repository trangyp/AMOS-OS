# Governed Agent Trace Model

## Runtime ownership

Canonical portable implementation:

```text
scripts/agent_trace_runtime.py
```

Within AMOS OS, `17_OBSERVABILITY/agent_trace_runtime.py` is a compatibility adapter that executes this same implementation.

This is a bounded implementation model. It is not evidence of OpenTelemetry end-to-end conformance, collector deployment, complete instrumentation, production durability, or commit authority.

## Hard boundaries

```text
TRACE != AUTHORITY
TRACE_EDGE != CAUSAL_PROOF
SPAN_SUCCESS != EFFECT_COMMITTED
TELEMETRY != MEMORY
TELEMETRY != KNOWLEDGE
HASH_MATCH != TRUST
NO_SPAN != NO_EVENT
SAMPLED_TRACE != COMPLETE_TRACE
OBSERVED_SEQUENCE != UNIQUE_MECHANISM
```

## Trace envelope

A bounded trace carries:

- nonzero 32-hex trace and 16-hex span identifier shapes;
- one root under the local AMOS trace contract;
- typed `WORKFLOW`, `AGENT`, `MODEL`, `TOOL`, `MEMORY`, `EVALUATION`, `EFFECT`, or `OTHER` spans;
- explicit span status and separate effect state;
- explicit capture mode;
- optional state epoch/provenance root;
- explicit missingness metadata;
- canonical SHA-256 receipt identity.

The digest binds serialized content under the local contract. It does not prove source trust, completeness, authorization, external finality, or semantic correctness.

## Content capture

Default: `METADATA`.

Modes:

- `NONE` — no payload.
- `METADATA` — non-payload structural attributes.
- `HASH_ONLY` — omit payload and retain its SHA-256 digest.
- `REDACTED` — upstream policy has already removed sensitive payload content.
- `FULL` — raw content; requires explicit `capture_authority_id`.

Raw prompts, completions, input/output, and tool argument/result fields are rejected outside `FULL`.

```text
CAPTURE_AUTHORIZED != PRIVACY_SAFE
CAPTURED != EXPORT_AUTHORIZED
```

## Effect evidence

An `EFFECT` span requires explicit effect state and `effect_id`.

A locally recorded `COMMITTED` effect additionally requires:

- `authority_decision_id`;
- `receipt_ref`.

These fields record evidence references. Observability does not mint or refresh authority.

Ambiguous effects use:

```text
effect_state = IN_DOUBT
status = IN_DOUBT
```

and must be reconciled before blind retry.

## Missingness

Unknown expected coverage remains `UNKNOWN`, not zero or complete.

When `N_expected > 0` is known, define local span coverage:

```text
C := N_observed / N_expected
```

Sampling, drops, collector gaps, and known uninstrumented paths keep the evidence `PARTIAL` even when all observed spans are internally valid.

## Mathematics

For a normalized finite distribution `p = (p_1, ..., p_n)`:

```text
H(p) := -sum_i p_i log2(p_i)
```

with `0 log 0 := 0`.

For successive distributions:

```text
Delta_H_t := H(p_(t+1)) - H(p_t)
```

`Delta_H_t` may be negative, zero, or positive. No monotonic uncertainty-reduction invariant is valid without additional assumptions.

For normalized `p` and `q` on the same finite index set, with `q_i > 0` whenever `p_i > 0`:

```text
D_KL(p || q) := sum_i p_i log2(p_i / q_i) >= 0
```

This established non-negativity is not proof of truth gain, reasoning quality, or causal validity.

## Upstream mechanism provenance

Mechanisms are adapted, not vendored.

### OpenTelemetry semantic conventions

Repository: `open-telemetry/semantic-conventions`  
Pinned coordinate: `a11c510432b66cca046e79908898856bf0ebfd1a`

Useful mechanisms:

- trace/span vocabulary;
- GenAI agent/tool operation vocabulary;
- opt-in tool call argument/result attributes;
- evaluation events;
- stability/deprecation metadata.

Observed GenAI surfaces include development/deprecated elements. Local naming similarity is not protocol-conformance evidence.

### OpenLLMetry

Repository: `traceloop/openllmetry`  
Pinned coordinate: `62e24c2ffde6c1ee04dc290e52d8d5dbda054cff`

Useful mechanisms:

- agent/LLM/tool/MCP instrumentation;
- content tracing separable from structural tracing;
- configuration to disable content tracing.

AMOS does not inherit exporter trust, privacy, or default-capture assumptions.

### Arize Phoenix

Repository: `Arize-ai/phoenix`  
Pinned coordinate: `e12748298b366605cc0e2aa60e659f473efbff99`

Useful mechanisms:

- trace/span/session views;
- annotations/notes linked to trace entities;
- session-turn reconstruction;
- evaluation and PII-detection surfaces;
- agent-facing tracing Skills.

Annotations/evaluations remain later evidence. They do not rewrite the original observation.

## Promotion boundary

Still `UNKNOWN/GAP` until separately executed and evidenced:

- full cross-tool/cross-host propagation;
- OpenTelemetry SDK/exporter/collector conformance;
- collector durability/backpressure;
- production privacy/compliance sufficiency;
- global clock/order correctness;
- production trace completeness;
- telemetry performance/overhead;
- deployed distributed-effect finality;
- semantic quality of model/judge annotations.
