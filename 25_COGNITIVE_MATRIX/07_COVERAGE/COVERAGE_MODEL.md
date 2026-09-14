---
canon-group: meta
canon-type: framework
rscf-state: derived
rscf-provenance: AMOS_corpus
conclusion_class: AMOS_MODEL
epistemic_class: DERIVED
topic: Coverage Model
tags:
  - canon-group/tech-ai
  - rscf/claim
  - rscf/provenance
  - cognitive-matrix
updated: 2026-09-14
---

# COVERAGE_MODEL — Bounded Executable Contract

**Origin architect / steward:** Trang Phan  
**Status:** `IMPLEMENTED_BOUNDED / VALIDATED_BOUNDED`  
**Runtime:** `04_RUNTIME/01_REFERENCE_IMPLEMENTATION/cognitive_matrix_runtime.py`

## Purpose

Coverage is represented as an ordered vector, not a single percentage that can hide missing implementation, validation, or authority.

For a non-empty registered cell set `R`, define

\[
C(R) = (c_a,c_s,c_c,c_i,c_v,c_u)
\]

with coordinates:

- `c_a`: address coverage;
- `c_s`: source-bound coverage;
- `c_c`: contract-complete coverage;
- `c_i`: implemented coverage;
- `c_v`: bounded-validated coverage;
- `c_u`: bounded-authorized coverage.

For maturity threshold `m`,

\[
c_m = \frac{|\{r \in R : M(r) \ge m\}|}{|R|}.
\]

For the empty set, every coordinate is defined as `0` by runtime convention to avoid division by zero and false completeness.

## Maturity order

```text
PLACEHOLDER
< SOURCE_BOUND
< CONTRACT_COMPLETE
< IMPLEMENTED
< VALIDATED_BOUNDED
< AUTHORIZED_BOUNDED
```

Runtime condition is orthogonal to maturity:

```text
ACTIVE | STALE | COMPETING | QUARANTINED | FALSIFIED
```

Therefore a historically mature artifact can still become stale or quarantined without rewriting its recorded maturity.

## Invariants

- Every coverage coordinate lies in `[0,1]`.
- `c_u <= c_v <= c_i <= c_c <= c_s <= c_a` for a consistently staged registry.
- `address=1` alone never implies system completeness.
- `complete=True` only when every coordinate equals `1`.
- Coverage does not establish empirical truth.
- Coverage does not grant authority.
- Missing/unknown is not counted as pass.

## Executed validation

A four-record mixed-maturity replay produced:

```text
address        1.00
source         1.00
contract       1.00
implementation 0.75
validation     0.50
authority      0.25
complete       false
```

This directly prevents the earlier failure mode where package-leaf addressability could be described as overall completion.

## Boundary

The runtime computes coverage only for records actually supplied to it. It does not claim that all expected Cognitive Matrix artifacts have already been discovered or registered.

[[25_COGNITIVE_MATRIX/07_COVERAGE/07_COVERAGE_MOC|07_COVERAGE_MOC]] · [[00_ROOT/00_ROOT_MOC|00_ROOT_MOC]]
