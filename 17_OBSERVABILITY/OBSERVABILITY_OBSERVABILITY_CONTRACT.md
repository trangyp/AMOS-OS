---
canon-group: meta
canon-type: framework
rscf-state: source-claim
rscf-claim: verified
rscf-provenance: AMOS_corpus
conclusion_class: AMOS_MODEL
epistemic_class: SOURCE_CLAIM
topic: Observability Observability Contract
tags:
  - canon-group/tech-ai
  - rscf/claim
  - rscf/provenance
  - rscf/state/source-claim
  - misc
created: 2026-08-22
---
---
---

# Observability Plane Contract

## 1. Primary ownership

`17_OBSERVABILITY` owns attributable evidence about execution and system condition: events, metrics,
traces, receipts, health signals, failures, retries, effects, recovery observations and evidence
missingness.

```text
OBSERVABILITY != AUTHORITY
OBSERVATION != STATE
OBSERVATION != TEST DEFINITION
OBSERVED != COMPLETE
OBSERVED != CURRENT
LOGGED != CAUSED
```

Observability supplies evidence to governance and learning; it does not grant permission or commit
effects.

## 2. MECE evidence families

1. **Events** — timestamped observations of transitions or occurrences.
2. **Traces** — linked execution spans/causal-attribution candidates across components.
3. **Metrics** — transformed quantitative signals with declared construct and aggregation.
4. **Receipts** — scoped execution/validation/audit evidence bound to subject/version/environment.
5. **Health signals** — availability, integrity, latency, error, degradation and recovery indicators.
6. **Failure/retry/effect observations** — failure class, retries, partial effects, compensation, `IN_DOUBT`.
7. **Coverage/missingness evidence** — dropped, late, sampled, uninstrumented or parser-failed evidence.

A signal may feed another family, but root lineage remains preserved.

## 3. Observation envelope

```yaml
observation:
  id:
  signal_class:
  source_or_sensor:
  subject:
  subject_version_or_hash:
  event_time:
  observation_time:
  environment:
  scope:
  regime:
  state_version_or_epoch:
  schema_and_units:
  provenance_root:
  transformations: []
  freshness:
  uncertainty:
  missingness_state:
  correlation_family:
  retention_state:
```

Unknown, missing, stale and not-applicable are not coerced to zero.

## 4. Instrumentation pipeline

```text
RAW EVENT
→ STRUCTURED EVENT
→ TRACE / METRIC
→ RECEIPT / HEALTH SIGNAL
→ GOVERNED SYNTHESIS
```

Every transformation preserves lineage and declares any lossy aggregation.

Raw logs are not the default reasoning substrate when a smaller proof-bearing receipt is sufficient.

## 5. Event time / observation time / processing time

These times are distinct when relevant.

```text
EVENT_TIME != OBSERVATION_TIME != PROCESSING_TIME
```

Late arrival, clock skew and buffering can change freshness and ordering conclusions. Sequence alone
does not establish causality.

## 6. Receipt contract

A consequential receipt should bind:

- subject identity/version/hash;
- operation/check identity;
- inputs/read set where relevant;
- environment/runtime;
- execution time/epoch;
- result/status;
- partial effects;
- failures/counterexamples;
- provenance;
- scope and coverage;
- invalidation conditions.

```text
MESSAGE != ARTIFACT
"TESTS PASSED" != EXECUTION RECEIPT
ACKNOWLEDGED != DURABLY FINAL
```

## 7. Completeness / missingness

Coverage is a first-class dimension. Track:

- expected vs captured events;
- sampling policy;
- dropped/late signals;
- disabled instrumentation windows;
- parser/schema failures;
- uninstrumented paths;
- retention loss;
- clock/time uncertainty.

`NO ALERT != NO FAILURE` and `NO SECURITY ALERT != NO ATTACK`.

## 8. Metrics / Goodhart firewall

A metric must declare:
- construct being measured;
- source signals;
- transformation/aggregation;
- units;
- population/window;
- exclusions;
- known blind spots;
- companion metrics/falsifiers when Goodhart risk is material.

Metric optimization does not itself establish improvement in the underlying construct.

## 9. Provenance topology

Multiple telemetry products derived from one collector/event stream remain one evidence family where
independence matters.

```text
N DASHBOARDS FROM ONE STREAM != N INDEPENDENT OBSERVATIONS
```

Correlated instrumentation failure must be carried forward as uncertainty.

## 10. Failure / retry / IN_DOUBT

Distinguish:
`FAILED`, `RETRYABLE`, `RETRIED`, `PARTIAL_EFFECT`, `COMPENSATED`, `ROLLED_BACK`, `RECOVERED`,
`IN_DOUBT`, `UNKNOWN/GAP`.

For non-idempotent external effects:

```text
OUTCOME AMBIGUOUS
→ IN_DOUBT
→ OBSERVE / RECONCILE
→ RETRY, COMPENSATE OR FINALIZE ONLY AFTER DISCRIMINATION
```

Absence of a success receipt does not prove failure; absence of a failure receipt does not prove
success.

## 11. Causal firewall

```text
LOGGED != CAUSED
TEMPORAL ORDER != MECHANISM
CORRELATION != INTERVENTION EFFECT
TRACE EDGE != UNIQUE CAUSAL MEDIATION
```

Causal claims require evidence appropriate to the claim type.

## 12. Cross-plane ownership

- `12_STATE` owns state identity/version/epoch.
- `19_TESTS` owns executable validation definitions and run verdicts.
- `20_OPERATIONS` owns incident/audit/runbook lifecycle.
- `03_CONTROL_PLANE` owns authority/finality eligibility.
- `10_MEMORY` owns persistence/retrieval semantics.
- `11_KNOWLEDGE` owns admitted reusable knowledge.
- `18_SECURITY` owns protected-boundary assurance.

Cross-links do not transfer authority.

## 13. Retention / replay boundary

Retained telemetry may support replay, incident reconstruction and audit only if signal identity,
ordering, completeness, environment and transformation lineage are sufficient.

```text
LOG RETAINED != REPLAYABLE SYSTEM
REPLAYABLE TRACE != DETERMINISTIC REEXECUTION
```

## 14. Validation / promotion

Production-strength observability claims require scoped evidence for:
- typed signal schemas;
- stable identities/timestamps;
- completeness/missingness;
- negative-path instrumentation;
- trace continuity;
- stale/late behavior;
- receipt durability;
- retention/replay;
- incident/recovery reconstruction;
- provenance correlation.

## 15. Open gaps

Unless separately evidenced:
- system-wide instrumentation coverage is `UNKNOWN/GAP`;
- complete cross-tool trace continuity is `UNKNOWN/GAP`;
- global clock/order correctness is `UNKNOWN/GAP`;
- durable replay across all effects is `UNKNOWN/GAP`;
- absence of observed failure never proves absence of failure.

## 16. Falsifiers

Revise/downgrade this contract if:
- observations are used as authority;
- missing signals are silently treated as zero/success;
- receipt lineage loses subject/version/environment;
- correlated telemetry is treated as independent evidence;
- causal claims exceed the measurement design;
- ambiguous effects bypass `IN_DOUBT` reconciliation.

## Related

- [[17_OBSERVABILITY/17_OBSERVABILITY_MOC|MOC]]
- [[17_OBSERVABILITY/OBSERVABILITY_README|README]]
- [[17_OBSERVABILITY/EXECUTED_VALIDATION_LEDGER_2026-09-03|VALIDATION_LEDGER]]
- [[19_TESTS/19_TESTS_MOC|TESTS]]
- [[20_OPERATIONS/20_OPERATIONS_MOC|OPERATIONS]]
- [[18_SECURITY/18_SECURITY_MOC|SECURITY]]

---
RSCF-NODE
node_id: observability_plane_contract
node_type: contract
path: 17_OBSERVABILITY/OBSERVABILITY_OBSERVABILITY_CONTRACT.md
claim_class: AMOS_MODEL
