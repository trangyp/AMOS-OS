# Governed Agent Trace Model

## Purpose

Use this reference when agent/workflow observability needs executable trace structure, privacy-aware content capture, missingness accounting, effect evidence, or evaluation linkage.

The local reference runtime is:

`17_OBSERVABILITY/agent_trace_runtime.py`

It is an AMOS local implementation model. It is not a claim of OpenTelemetry protocol conformance, collector deployment, complete instrumentation coverage, or production observability.

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

- W3C-compatible trace/span identifier shapes;
- one local AMOS root span;
- typed child spans (`WORKFLOW`, `AGENT`, `MODEL`, `TOOL`, `MEMORY`, `EVALUATION`, `EFFECT`, `OTHER`);
- explicit span status;
- explicit capture mode;
- optional state epoch and provenance root;
- effect state distinct from span status;
- explicit missingness metadata;
- a canonical SHA-256 receipt identity.

The SHA-256 receipt binds the serialized trace content. It does not prove source trust, correctness, completeness, authorization, or external finality.

## Content capture

Default to `METADATA`.

Modes:

- `NONE`: no content payload.
- `METADATA`: structured non-payload attributes only.
- `HASH_ONLY`: payload omitted; a SHA-256 digest is retained.
- `REDACTED`: only content already redacted by an upstream policy may be attached as non-raw metadata.
- `FULL`: raw content is allowed only with an explicit `capture_authority_id`.

`FULL` does not itself prove that collection is lawful, necessary, privacy-safe, or permitted by a downstream exporter.

Raw prompt, completion, input/output, and tool argument/result fields are rejected outside `FULL`.

## Effect evidence

An `EFFECT` span must carry an explicit effect state.

A `COMMITTED` effect requires:

- `effect_id`;
- `authority_decision_id`;
- `receipt_ref`.

This records evidence that an authority decision/receipt was associated with the effect. The observability layer does not mint that authority.

An ambiguous effect uses both:

```text
effect_state = IN_DOUBT
status = IN_DOUBT
```

and must be reconciled by the control/runtime layer before blind retry.

## Missingness

When `expected_span_count` is unknown, coverage is `UNKNOWN`, not zero or complete.

When it is known:

```text
coverage = observed_span_count / expected_span_count
```

subject to the declared local counting contract.

Sampling, drops, collector gaps, and known uninstrumented paths keep the trace `PARTIAL` even when observed spans are internally valid.

## Mathematics

For a normalized discrete distribution `p = (p_1, ..., p_n)`, Shannon entropy in bits is:

```text
H(p) = -sum_i p_i log2(p_i)
```

with the standard convention `0 log 0 = 0`.

For successive distributions `p_t` and `p_(t+1)`, define:

```text
Delta_H_t = H(p_(t+1)) - H(p_t)
```

`Delta_H_t` may be negative, zero, or positive. No monotonic-decrease invariant is valid without additional assumptions.

For distributions `p` and `q` on the same finite support with `q_i > 0` whenever `p_i > 0`:

```text
D_KL(p || q) = sum_i p_i log2(p_i / q_i) >= 0
```

This is established mathematics. `D_KL` measures distributional divergence; it is not proof of truth gain, reasoning quality, or causal validity.

## Upstream mechanism provenance

Mechanisms are adapted, not vendored.

### OpenTelemetry semantic conventions

Repository: `open-telemetry/semantic-conventions`

Pinned research coordinate:

`a11c510432b66cca046e79908898856bf0ebfd1a`

Relevant mechanisms:

- standardized trace/span vocabulary;
- GenAI operation vocabulary including agent invocation and tool execution;
- opt-in tool call argument/result attributes;
- evaluation events;
- explicit stability/deprecation metadata.

The GenAI conventions observed at this coordinate include development/deprecated surfaces. AMOS must not label a local mapping protocol-conformant merely because names are similar.

### OpenLLMetry

Repository: `traceloop/openllmetry`

Pinned research coordinate:

`62e24c2ffde6c1ee04dc290e52d8d5dbda054cff`

Relevant mechanisms:

- OpenTelemetry instrumentation across LLM/agent/tool integrations;
- MCP instrumentation;
- explicit configuration to disable content tracing (`TRACELOOP_TRACE_CONTENT=false`).

AMOS adopts the principle that content capture is separately governed from structural tracing. It does not inherit OpenLLMetry defaults or exporter trust assumptions.

### Arize Phoenix

Repository: `Arize-ai/phoenix`

Pinned research coordinate:

`e12748298b366605cc0e2aa60e659f473efbff99`

Relevant mechanisms:

- trace/span/session views;
- annotations and notes bound to trace entities;
- session-turn reconstruction;
- evaluation and PII-detection surfaces;
- agent-facing tracing Skills.

AMOS adopts the separation of base telemetry from later annotations/evaluation. An annotation remains evidence/assessment, not a mutation of the original observation.

## Promotion boundary

The following remain `UNKNOWN/GAP` until separately executed and evidenced:

- full cross-tool trace propagation;
- actual OpenTelemetry SDK/exporter integration;
- collector durability and backpressure behavior;
- production privacy/compliance sufficiency;
- clock synchronization across hosts;
- production trace completeness;
- performance/overhead;
- distributed effect finality;
- semantic quality of model/judge annotations.
