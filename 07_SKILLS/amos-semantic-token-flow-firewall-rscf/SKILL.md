---
name: amos-semantic-token-flow-firewall-rscf
description: Mediate semantic information flows across AMOS agents, tools, memory, files, telemetry, and external recipients using typed source-to-sink policy, taint/category propagation, declassification witnesses, transformation lineage, declared-vs-observed effect checks, and fail-closed receipts. Use when a specific flow may carry protected meaning across a boundary before cumulative exposure accounting or durable effect commit.
---

# AMOS Semantic Token Flow Firewall RSCF

Origin architect/steward: **Trang Phan**.

Place this control after caller-specific authorization and before cumulative information-exposure accounting or any durable/external sink effect.

## Runtime

`BIND -> SOURCE_LABEL -> SINK_BIND -> PROPAGATE -> SANITIZER_EVIDENCE -> DECLASSIFICATION_GATE -> EFFECT_ALIGNMENT -> POLICY_GATE -> RECEIPT`

1. Bind the exact content digest, semantic transaction, authorization receipt reference, canonical semantic origins, source classification/categories, sink, recipient, policy epoch, and effect digest.
2. Treat source labels as sticky by default. Transformations do not erase origin, category, or classification merely because text changed.
3. Resolve the sink contract and compare observed effect classes with declared effect classes. Hidden or widened effects fail closed.
4. Consume detector/sanitizer evidence as evidence only. Detection does not sanitize; sanitization does not itself declassify.
5. Allow category removal only when a sanitizer witness binds the exact input/output hashes, removed categories, transform kind, verifier, evidence reference, and current policy epoch.
6. Allow classification lowering only through a current declassification witness issued by an allowed authority and bound to the exact effect, transaction, sink, recipient, source/target classifications, categories, transform, and validity interval.
7. If a safe rewrite might repair a category-policy violation, emit a bounded rewrite plan. The rewritten artifact must be resubmitted; a plan is not proof the rewrite occurred or is sufficient.
8. For external disclosure sinks, successful local flow mediation still requires the downstream Information Exposure Control gate.
9. Emit a tamper-evident receipt. A local flow PASS never grants execution, disclosure, persistence, merge, or commit authority.

Run:

```bash
python scripts/token_flow.py --self-test
python scripts/audit_rscf.py --self-test
```

## Hard invariants

- `AuthorizationAllow != FlowAllow`.
- `FlowAllow != ExposureAllow`.
- `FlowReceipt != EffectCommitted`.
- `Detection != Sanitization`.
- `Sanitization != Declassification`.
- `RewritePlan != RewriteExecuted`.
- `RewriteExecuted != SemanticallySafe`.
- `Transformation != OriginReset`.
- `DifferentEncoding != DifferentSemanticOrigin`.
- `Hashing != Anonymization`.
- `Aggregation != NonSensitive`.
- `DeclaredEffect != ObservedEffect` unless checked.
- `ObservedEffectSubsetDeclared` is required for a local PASS.
- `SourceLabel` propagates unless exact policy-bound evidence authorizes narrowing.
- `DeclassificationWitness != CommitAuthority`.
- `DetectorNoFinding != NoSensitiveData`.
- `StaticTaintModel != RuntimeSemanticTruth`.

For classification levels represented by integers `0 <= L <= 3`, ordinary propagation is monotone:

`L_out >= L_in`

unless a valid declassification witness explicitly licenses `L_out < L_in` for the exact bound flow.

For source category set `C_in` and output category set `C_out`:

`C_out subseteq C_in`

is accepted only when every removed category is covered by an exact sanitizer witness. Otherwise the flow is `REVALIDATE_SANITIZER`.

## Progressive references

Read `references/workflow.md` for the typed flow/declassification contract. Read `references/upstream-mechanisms.md` for pinned GitHub provenance and transfer limits.
