---
title: amos-agentops-observability-rscf-workflow
type: workflow
skill: amos-agentops-observability-rscf
agent: amos-agentops-observability-rscf-agent
version: 2.0.0
origin_architect: Trang Phan
epistemic_class: AMOS_MODEL
status: IMPLEMENTED_LOCAL_REFERENCE
---

# Workflow: AMOS AgentOps Observability

## State machine

```text
INTAKE
-> BIND_TARGET
-> CLASSIFY_SIGNAL
-> TRACE_VALIDATE
-> CAPTURE_POLICY_GATE
-> MISSINGNESS_GATE
-> EFFECT_GATE
-> EVALUATION_LINK
-> FORENSICS
-> VERDICT
-> TERMINAL
```

## Gates

### BIND_TARGET
Bind subject identity/version, environment, scope, regime, evidence source, and consequence.

If identity is unresolved, return `UNKNOWN/GAP`.

### CLASSIFY_SIGNAL
Classify each input as one of:

```text
SPECIFICATION
RAW_EVENT
SPAN
TRACE
METRIC
RECEIPT
EVALUATION
ANNOTATION
INCIDENT_EVIDENCE
```

Do not promote a specification into observed runtime evidence.

### TRACE_VALIDATE
For compatible trace JSON, run:

```bash
python 07_SKILLS/amos-agentops-observability-rscf/scripts/trace_contract.py trace.json --repo .
```

Failure -> `INVALID_TRACE_EVIDENCE` for the affected claim.

No executable trace artifact -> remain `MODEL` or `UNKNOWN/GAP`; do not fabricate one.

### CAPTURE_POLICY_GATE
Default raw-content policy:

```text
capture_mode = METADATA
```

Raw prompt/input/output/tool content without explicit capture authority -> `REJECT_CAPTURE`.

`CAPTURE_AUTHORIZED != PRIVACY_SAFE`.

### MISSINGNESS_GATE
Preserve:

- expected spans when known;
- observed spans;
- dropped spans;
- sampling;
- collector gaps;
- known uninstrumented paths.

Unknown expected coverage -> `UNKNOWN`, not zero or complete.

Any declared loss/gap -> `PARTIAL`.

### EFFECT_GATE
`SPAN_SUCCESS != EFFECT_COMMITTED`.

A locally recorded `COMMITTED` effect requires `effect_id`, `authority_decision_id`, and `receipt_ref`.

Ambiguous result -> `IN_DOUBT`; reconcile before retry.

### EVALUATION_LINK
Attach evaluations/annotations as later evidence bound to trace/span/session identity.

```text
ANNOTATION != ORIGINAL_OBSERVATION
JUDGE_SCORE != GROUND_TRUTH
```

### FORENSICS
Challenge:

- broken parentage/cycles;
- duplicate IDs;
- stale trace context;
- sampling/drop blind spots;
- raw-content leakage;
- effect/authority conflation;
- hash/trust conflation;
- trace-edge/causality conflation;
- semantic claims unsupported by deterministic evidence.

### VERDICT
Use only the narrowest supported result:

```text
VERIFIED
DERIVED
MODEL
CONDITIONAL
COMPETING
UNKNOWN/GAP
```

A PASS applies only to the contract that actually executed.

## Outputs

Return:

- target identity and scope;
- evidence class;
- trace/receipt identity if available;
- missingness state;
- capture/privacy state;
- effect state if relevant;
- evaluation/annotation lineage;
- failures/falsifiers;
- provenance;
- bounded verdict;
- unresolved gaps.

## Failure transitions

```text
INVALID TRACE STRUCTURE -> INVALID_TRACE_EVIDENCE
RAW CONTENT + NO CAPTURE AUTHORITY -> REJECT_CAPTURE
COMMITTED EFFECT + NO AUTHORITY/RECEIPT REF -> INVALID_EFFECT_EVIDENCE
AMBIGUOUS EXTERNAL EFFECT -> IN_DOUBT
UNKNOWN COVERAGE -> UNKNOWN
SAMPLING/DROPS/GAPS -> PARTIAL
PROVENANCE LOSS -> UNKNOWN/GAP
```

## Current boundary

Local trace-contract semantics are executable. Distributed propagation, collector/exporter integration, production overhead, privacy/compliance sufficiency, and complete instrumentation coverage remain `UNKNOWN/GAP` until independently tested.

**MOC:** [[08_WORKFLOWS/08_WORKFLOWS_MOC|08_WORKFLOWS_MOC]]
