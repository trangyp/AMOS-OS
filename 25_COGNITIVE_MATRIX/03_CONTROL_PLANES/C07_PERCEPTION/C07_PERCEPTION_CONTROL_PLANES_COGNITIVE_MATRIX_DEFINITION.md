---
canon-group: meta
canon-type: framework
rscf-state: source-claim
rscf-claim: conditional
rscf-provenance: AMOS_corpus
conclusion_class: AMOS_MODEL
epistemic_class: AMOS_MODEL
topic: C07 Perception Control Planes Cognitive Matrix Definition
created: 2026-08-22
updated: 2026-09-14
---

# C07 — Perception

**Package:** `C07_PERCEPTION`  
**Class:** `COGNITIVE_MATRIX_CONTROL_PLANE`  
**Origin architect / steward:** Trang Phan  
**Status:** `EXECUTABLE_BOUNDED_REFERENCE / TESTED`

## Scope

C07 represents bounded perception inputs without inventing unavailable sensing.

Domain tensor slice:

`T_UMPL[obj, modality, feature, primitive, time, observer, provenance, epistemic_origin, confidence, availability]`.

The local reference implements the load-bearing subset:

`Percept[obj, modality, feature, observer, provenance, origin, availability, confidence, intensity, valence, arousal, clarity]`.

## Origin classes

C07 preserves the distinction among:

- `OBSERVED`
- `USER_REPORTED`
- `INFERRED`
- `SIMULATED`
- `UNOBSERVED`

These labels are not interchangeable.

## Availability invariant

For modality `m`, availability is binary in the bounded schema:

`A_m in {0,1}`.

If `A_m = 0`, the modality must remain `UNOBSERVED` with confidence `0`.

An unavailable modality cannot be silently filled by inference or simulation and relabeled as observation.

## Fusion confidence

For the available channels participating in one object/feature fusion:

`C_fusion = min_i C_i`.

This is the conservative AMOS_MODEL fusion rule used by the reference runtime. It prevents confidence inflation; it is not asserted as a universal empirical sensor-fusion law.

Unavailable channels are excluded from the minimum rather than being treated as zero-valued observations.

## Causal firewall

```text
CROSS_MODAL_CORRELATION != CAUSATION
INFERRED != OBSERVED
SIMULATED != OBSERVED
USER_REPORTED != SENSOR_OBSERVED
UNAVAILABLE != NEGATIVE_OBSERVATION
```

The C07 fusion result is structurally unable to mint a causal claim.

## Executable binding

Reference runtime:

`04_RUNTIME/01_REFERENCE_IMPLEMENTATION/c07_perception_runtime.py`

Adversarial tests:

`04_RUNTIME/01_REFERENCE_IMPLEMENTATION/test_c07_perception_runtime.py`

The complete reference-runtime CI passed the C07 adversarial revision on 2026-09-14.

## Remaining gaps

- sensor calibration and physical measurement accuracy are not established;
- cross-modal alignment quality is not empirically benchmarked here;
- modality-specific units require domain validators;
- unavailable modalities remain unavailable rather than synthesized as facts;
- perception validity does not establish downstream causal or epistemic validity.

[[25_COGNITIVE_MATRIX/00_INDEX/COGNITIVE_MATRIX_MOC|COGNITIVE_MATRIX_MOC]] · [[00_ROOT/00_ROOT_MOC|00_ROOT_MOC]]
