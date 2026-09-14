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

## Workflow

1. Bind subject, version/hash, environment, scope, regime, and consequence.
2. Classify specification, emitted span, collected trace, evaluation, receipt, and runtime observation separately.
3. Validate compatible trace JSON with the deterministic contract.
4. Check capture policy; metadata is default and raw payload requires explicit authority.
5. Preserve expected/observed spans, sampling, drops, collector gaps, and known uninstrumented paths.
6. Keep span status separate from effect state and require authority/receipt references for locally recorded committed effects.
7. Attach evaluations/annotations as later evidence, never rewrites of the original observation.
8. Challenge stale context, missing parents, duplicate IDs, ambiguous effects, content leakage, tampering, and unsupported causal claims.
9. Return `VERIFIED`, `DERIVED`, `MODEL`, `CONDITIONAL`, `COMPETING`, or `UNKNOWN/GAP` at the narrowest supported scope.

Do not use telemetry as a substitute for authorization, state finality, scientific validation, or causal identification.

## Executable contract

The canonical portable implementation is bundled at:

```text
scripts/agent_trace_runtime.py
```

Validate a trace document from the Skill bundle:

```bash
python scripts/trace_contract.py trace.json
```

Run the deterministic self-test:

```bash
python scripts/trace_contract.py --self-test
```

Inside the AMOS repository, the compatibility adapter at `17_OBSERVABILITY/agent_trace_runtime.py` executes the same Skill-local implementation. This is a bounded local reference runtime, not evidence of a deployed collector/exporter stack.

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

Read `references/trace-model.md` for exact entropy/KL definitions, assumptions, upstream GitHub provenance, privacy rules, and promotion boundaries.

Historical corpus/MOC files may remain in the repository for lineage but are not part of the active runtime loading path.

## Output contract

Return the smallest sufficient evidence object containing target identity/scope, evidence class, trace/receipt identity when available, missingness, effect state, capture/privacy state, failures/falsifiers, provenance, bounded verdict, and unresolved gaps.

Do not request or expose hidden chain-of-thought. Trace observable actions, states, tool calls, effects, and evaluation artifacts instead.
