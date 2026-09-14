---
name: amos-agentops-observability-rscf
description: Govern and diagnose AMOS agent/workflow observability using typed traces, span/effect separation, missingness accounting, privacy-aware content capture, provenance-bound receipts, evaluations, and incident evidence. Use for agent telemetry, OpenTelemetry-style tracing, tool/model/memory spans, trace continuity, effect reconciliation, observability gaps, or when logs must not be mistaken for authority, causality, truth, or complete execution evidence.
---

# AMOS AgentOps Observability RSCF

Origin architect / steward: **Trang Phan**.

Apply:

`integrity > completeness > fluency > speed`

## Hard invariants

```text
OBSERVABILITY != AUTHORITY
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

Missing, stale, sampled, dropped, redacted, and not-instrumented states remain explicit. Never coerce them to zero, success, or completeness.

## Use this Skill for

- agent/workflow/model/tool/memory trace design or audit;
- OpenTelemetry-style span mapping and trace continuity;
- effect spans that must remain separate from commit authority;
- content-capture and telemetry privacy decisions;
- dropped/sampled/late/uninstrumented evidence accounting;
- trace/session annotations and evaluation evidence;
- incident reconstruction and observability root-cause analysis;
- determining whether a telemetry claim is executable evidence or only a specification.

Do not use telemetry as a substitute for authorization, state finality, scientific validation, or causal identification.

## Workflow

1. **Bind target** — identify subject, version/hash, environment, scope, regime, and consequence.
2. **Classify evidence** — distinguish specification, emitted span, collected trace, evaluation, receipt, and runtime observation.
3. **Validate structure** — run the deterministic trace contract when a compatible trace JSON exists.
4. **Check capture policy** — metadata by default; raw payload capture requires explicit authority and remains privacy/compliance bounded.
5. **Check missingness** — record expected/observed spans, sampling, drops, collector gaps, and known uninstrumented paths.
6. **Separate effects** — span status never commits an external effect; committed effect evidence must reference authority and receipt identity.
7. **Attach assessments** — evaluations/annotations are later evidence attached to trace entities, not rewrites of the original observation.
8. **Challenge** — test stale context, missing parents, duplicate IDs, ambiguous effects, content leakage, tampering, and unsupported causal claims.
9. **Return bounded verdict** — `VERIFIED`, `DERIVED`, `MODEL`, `CONDITIONAL`, `COMPETING`, or `UNKNOWN/GAP`.

## Executable contract

Validate a trace document:

```bash
python 07_SKILLS/amos-agentops-observability-rscf/scripts/trace_contract.py trace.json --repo .
```

Run the deterministic self-test:

```bash
python 07_SKILLS/amos-agentops-observability-rscf/scripts/trace_contract.py --self-test --repo .
```

The implementation is `17_OBSERVABILITY/agent_trace_runtime.py` and is a bounded local reference runtime, not evidence of a deployed collector/exporter stack.

## Content capture

Default: `METADATA`.

`FULL` raw prompt/input/output/tool content requires an explicit `capture_authority_id`. Even then:

```text
CAPTURE_AUTHORIZED != PRIVACY_SAFE
CAPTURED != EXPORT_AUTHORIZED
```

Prefer `NONE`, `METADATA`, `HASH_ONLY`, or upstream-redacted content when raw payload is not decision-critical.

## Effect tracing

An `EFFECT` span records observed/proposed effect state. It does not mint authority.

A locally valid `COMMITTED` effect record requires:

- `effect_id`;
- `authority_decision_id`;
- `receipt_ref`.

Ambiguous external outcomes remain `IN_DOUBT` and must be reconciled before retry.

## Mathematics boundary

If uncertainty distributions are supplied, Shannon entropy change may be positive, zero, or negative. Never enforce monotonic entropy reduction as a truth invariant.

Read `references/trace-model.md` for the exact entropy/KL definitions, assumptions, upstream GitHub provenance, privacy rules, and promotion boundary.

## Progressive reference

- `references/trace-model.md` — load for trace schema, mathematics, privacy, effect evidence, upstream observability provenance, or promotion boundaries.

Historical corpus/MOC files may remain in the repository for lineage but are not part of the active runtime loading path.

## Output contract

Return the smallest sufficient evidence object containing:

- target identity/scope;
- evidence class;
- trace/receipt identity when available;
- missingness state;
- effect state when relevant;
- privacy/capture state;
- failures or falsifiers;
- provenance;
- bounded verdict and unresolved gaps.

Do not request or expose hidden chain-of-thought. Trace observable actions, states, tool calls, effects, and evaluation artifacts instead.
