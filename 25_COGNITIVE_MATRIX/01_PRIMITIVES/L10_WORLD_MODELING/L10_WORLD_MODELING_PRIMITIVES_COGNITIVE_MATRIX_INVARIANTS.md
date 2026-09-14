---
canon-group: cognition
canon-type: invariant_contract
rscf-state: derived
rscf-provenance: AMOS_corpus_plus_reality_simulation_distinction
conclusion_class: AMOS_MODEL
epistemic_class: DERIVED
topic: L10 World Modeling Primitives Cognitive Matrix Invariants
created: 2026-08-22
updated: 2026-09-14
origin_architect: Trang Phan
amos_core_target: v4.4
canonical_status: CONDITIONAL
---

# L10 — World Modeling Invariants

**Package:** `L10_WORLD_MODELING`  
**Origin architect / steward:** **Trang Phan**

## Representation invariants

- `INV-L10-01 / HARD`: Representation class is explicit for every world-model record.
- `INV-L10-02 / HARD`: `MODEL_STATE`, `SIMULATION`, `COUNTERFACTUAL`, `SYNTHETIC_DATA`, `DIGITAL_TWIN`, and `FORECAST` are not silently upgraded to `OBSERVED_REALITY`.
- `INV-L10-03 / HARD`: Digital-twin state is not assumed identical to the physical entity state.
- `INV-L10-04 / HARD`: Synthetic data cannot independently validate assumptions inherited from its own generator.
- `INV-L10-05 / HARD`: Unknown value/missingness is not converted to zero.

## Fidelity and reality-contact invariants

- `INV-L10-06 / HARD`: Reality contact requires an externally anchorable representation class, external observation, known measurement method, recoverable provenance, and fidelity-envelope compatibility.
- `INV-L10-07 / HARD`: Internal simulation consistency alone never satisfies the reality-contact gate.
- `INV-L10-08 / HIGH`: Validity travels with variable, regime, time, and measurement-method envelope.
- `INV-L10-09 / HIGH`: Regime or measurement changes stale only dependent claims unless broader dependency evidence exists.

## Tensor and coordinate invariants

- `INV-L10-10 / HARD`: Object, representation class, variable, scale, time, regime, observer, provenance, validation status, and consequence axes remain typed and non-interchangeable.
- `INV-L10-11 / HARD`: Numeric comparison requires identical object, variable, unit, time, and regime coordinates.
- `INV-L10-12 / HARD`: Unit mismatch blocks direct numeric discrepancy unless an explicit conversion is bound.
- `INV-L10-13 / HARD`: Cross-scale translation is not identity and is not assumed invertible.

## Discrepancy invariants

- `INV-L10-14 / HARD`: Model-observation mismatch remains first-class evidence; it is not dismissed by default as observation error.
- `INV-L10-15 / HARD`: Absolute discrepancy is computed only for commensurate numeric records with adequate observation reality contact.
- `INV-L10-16 / HIGH`: A tolerance must be explicit and non-negative before `WITHIN_TOLERANCE` or `EXCEEDS_TOLERANCE` classification.
- `INV-L10-17 / HIGH`: A mismatch invalidates/stales only claims that depend on the compared coordinate and declared tolerance contract.

## Provenance invariants

- `INV-L10-18 / HARD`: Repeated descendants, mirrors, or summaries with the same provenance root do not count as independent confirmation.
- `INV-L10-19 / HARD`: Shared generator identity blocks the simple bounded independent-support gate.
- `INV-L10-20 / HIGH`: Passing the simple ancestry gate is not sufficient proof of statistical or physical independence.

## World-model / inference boundary

- `INV-L10-21 / HARD`: Formal entailment over model statements does not upgrade their representation class to observed reality.
- `INV-L10-22 / HARD`: Structural similarity across scales does not establish the same causal mechanism.
- `INV-L10-23 / HARD`: Prediction accuracy alone does not establish causal validity.
- `INV-L10-24 / HARD`: A world model may inform an action proposal but does not mint effect authority.

## Executable binding

The staged bounded runtime directly enforces/tests invariants `01`, `02`, `05`–`12`, `14`–`16`, `18`, and `19` through `world_model_runtime.py` and `test_world_model_runtime.py`.

```text
DOCUMENTED_INVARIANT != EXECUTABLE_ENFORCEMENT
BOUNDED_TEST_PASS != UNIVERSAL_WORLD_MODEL_VALIDITY
MODEL != REALITY
```

RSCF-NODE

```text
node_id: l10_primitives_invariants
node_type: invariant_contract
claim_class: AMOS_MODEL
rscf_state: DERIVED
canonical_status: CONDITIONAL
```

**MOC:** [[25_COGNITIVE_MATRIX/01_PRIMITIVES/L10_WORLD_MODELING/L10_WORLD_MODELING_MOC|L10_WORLD_MODELING_MOC]]
