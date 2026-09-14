---
canon-group: meta
canon-type: framework
rscf-state: source-claim
rscf-claim: verified
rscf-provenance: AMOS_corpus
conclusion_class: AMOS_MODEL
epistemic_class: SOURCE_CLAIM
topic: Cognitive Matrix Scales Contract
tags:
  - canon-group/tech-ai
  - rscf/claim
  - rscf/provenance
  - rscf/state/source-claim
created: 2026-08-22
updated: 2026-09-14
---

# COGNITIVE MATRIX SCALES CONTRACT

## 0. Status

- Scale registry: `H_HIGH`, `M_MID`, `L_LOW`.
- Generic scale contract runtime: `IMPLEMENTED / VALIDATED_BOUNDED`.
- Domain-specific cross-scale transforms: `UNKNOWN/GAP unless separately evidenced`.
- Canonical class: `AMOS_MODEL / CONDITIONAL`.
- Production validity: `NOT ESTABLISHED`.

Origin architect / steward: **Trang Phan**.

## 1. Hard boundaries

```text
H != M != L
SAME_PATTERN_ACROSS_SCALE != SAME_MECHANISM
CROSS_SCALE_SIMILARITY != EQUIVALENCE
CROSS_SCALE_ASSOCIATION != CAUSATION
TRANSFORM_DECLARED != TRANSFORM_VALIDATED
STRUCTURALLY_BOUND != SEMANTICALLY_EQUIVALENT
MODEL != VERIFIED
UNKNOWN/GAP != PASS
```

Scale is a typed coordinate. Scale labels are non-interchangeable and may not be silently collapsed during translation, routing, inference, aggregation, or tensor/field projection.

## 2. Scale artifact contract

A scale-bound artifact must declare:

- artifact identity;
- scale identity;
- state version;
- scope;
- regime;
- provenance.

The artifact's scale cannot be inferred from filename, directory position, or descriptive resemblance alone.

## 3. Cross-scale transform contract

A cross-scale transform requires all of:

- explicit transform identity;
- distinct source and target scales;
- assumptions;
- invariants to be preserved/tested;
- provenance;
- validation receipt identity.

Passing this structural contract does not prove that the two scales have identical semantics, mechanisms, causal structure, units, uncertainty, or observability.

## 4. Executed reference

Repository implementation:

- `04_RUNTIME/01_REFERENCE_IMPLEMENTATION/scale_contract_runtime.py`
- `04_RUNTIME/01_REFERENCE_IMPLEMENTATION/test_scale_contract_runtime.py`

Executed full reference-runtime CI on 2026-09-14 for commit `a0bbb2f87e00855d93f22d2c1864ff5173a1ebf5` passed, including:

- exact H/M/L registry;
- mandatory state/scope/regime/provenance on scale artifacts;
- explicit cross-scale transform evidence requirements;
- same-scale requests rejected as cross-scale transforms;
- bounded transform receipts explicitly refuse to claim semantic or causal equivalence.

`TEST_PASS != TRUTH` and `VALIDATED_CONTRACT != VALIDATED_DOMAIN_TRANSFORM`.

## 5. Tensor/field interaction

Scale may be an axis of a typed coordinate/data field. That fact alone does not establish algebraic tensor semantics.

```text
INDEXED_FIELD_WITH_SCALE_AXIS != ALGEBRAIC_TENSOR
```

Algebraic tensor claims remain subject to the URK scalar/module/multilinearity/tensor-product and basis firewalls.

## 6. Remaining gaps

Domain-specific scale transformations require their own mathematical and empirical evidence, including units, observer/resolution assumptions, information loss, uncertainty propagation, invariants, counterexamples, and regime boundaries.

No generic H/M/L analogy may fill those gaps automatically.

## 7. Falsifiers

Revise this contract if:

1. authoritative source changes the scale registry;
2. an implementation silently interchanges H/M/L;
3. cross-scale resemblance is used as proof of mechanism or causality;
4. a transform executes without explicit assumptions/invariants/provenance/receipt;
5. a scale-axis record is mislabeled an algebraic tensor by dimensional shape alone.

RSCF-NODE
node_id: cognitive_matrix_scales_contract
node_type: note
path: 25_COGNITIVE_MATRIX/04_SCALES/COGNITIVE_MATRIX_SCALES_CONTRACT.md
claim_class: AMOS_MODEL

**MOC:** [[25_COGNITIVE_MATRIX/04_SCALES/04_SCALES_MOC|04_SCALES_MOC]]

**Trang Framework:** [[11_KNOWLEDGE/TRANG_FRAMEWORK_RECURSIVE_ONTOLOGY_DYNAMICS|TRANG_FRAMEWORK_RECURSIVE_ONTOLOGY_DYNAMICS]]
