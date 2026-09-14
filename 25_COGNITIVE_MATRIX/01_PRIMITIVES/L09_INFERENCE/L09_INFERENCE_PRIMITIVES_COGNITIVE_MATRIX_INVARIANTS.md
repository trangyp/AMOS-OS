---
canon-group: cognition
canon-type: invariant_contract
rscf-state: derived
rscf-provenance: AMOS_corpus_plus_2026_09_14_URK_repair
conclusion_class: AMOS_MODEL
epistemic_class: DERIVED
topic: L09 Inference Primitives Cognitive Matrix Invariants
created: 2026-08-22
updated: 2026-09-14
origin_architect: Trang Phan
amos_core_target: v4.4
canonical_status: CONDITIONAL
---

# L09 — Invariants

**Package:** `L09_INFERENCE`  
**Origin architect / steward:** **Trang Phan**

These invariants govern the repaired inference boundary. Hard invariants are non-compensatory.

## Typed and semantic invariants

- `INV-L09-01 / HARD / TYPE`: Every executable formula belongs to one declared syntax type with valid arity and payload.
- `INV-L09-02 / HARD / LAYER`: URK mathematics, ULK logic fragments, Core-19 semantics, executable syntax, empirical interpretation, and effect authority remain distinct layers.
- `INV-L09-03 / HARD / CORE19`: The 19-name semantic vocabulary is not silently equated with the observed executable AST enumeration.
- `INV-L09-04 / HARD / PARTIALITY`: An unbound Core-19 interaction remains `UNBOUND`; it is not converted to zero, false, or a fabricated semantic rule.
- `INV-L09-05 / HARD / P02`: P02 remains cross-lineage `COMPETING` unless namespace and version explicitly resolve a local binding.
- `INV-L09-06 / HARD / P02`: `Distinction`, `NonExistence`, `UNKNOWN`, and missing evidence are not interchangeable states.

## Logic and proof invariants

- `INV-L09-07 / HARD / ROUTING`: A logic fragment may execute only when the bound runtime has executable evidence for that fragment.
- `INV-L09-08 / HARD / QUANTUM`: `CANONICAL_BOUNDED_CLAIM_REBIND_PENDING` is not treated as an available local quantum checker.
- `INV-L09-09 / HARD / CONSISTENCY`: Pairwise satisfiability never substitutes for a required global-consistency check.
- `INV-L09-10 / HARD / CONTRADICTION`: Contradictory premises remain inspectable and block bounded inference promotion in the reference runtime.
- `INV-L09-11 / HARD / ENTAILMENT`: `NOT_ENTAILED` is distinct from `FALSE`; existence of a countermodel only shows the declared premises do not force the conclusion.
- `INV-L09-12 / HARD / CAUSAL`: Logical implication, ordering, adjacency, correlation, prediction, or topology does not by itself establish real-world causation.

## Rewrite invariants

For the bounded `ATOM | NOT | NLOGIC` grammar:

- `INV-L09-13 / HARD / REWRITE`: `NLOGIC(NLOGIC(x))` is recognized before recursive child normalization.
- `INV-L09-14 / HARD / REWRITE`: repaired normalization is idempotent over the bound grammar.
- `INV-L09-15 / HARD / REWRITE`: double-NLOGIC normalization is involutive relative to the repaired normal form.
- `INV-L09-16 / HARD / TERMINATION`: every admitted rewrite path must terminate under a declared well-founded measure or reach an already-normal form.

## Truth-state invariants

- `INV-L09-17 / HARD / TRUTH4`: four-valued evidence states preserve both support channels; `BOTH` and `NEITHER` must not be collapsed into ordinary Boolean true/false.
- `INV-L09-18 / HARD / TRUTH4`: `neg4(neg4(x)) = x` for every four-valued evidence state.
- `INV-L09-19 / HARD / SEMANTICS`: historical `PARADOX`/`DLOGIC` executable rewrites remain source-scoped runtime behavior and are not universalized as semantics.

## Tensor and topology invariants

- `INV-L09-20 / HARD / MATRIX`: `19 x 19 = 361` is a coordinate-count identity, not evidence that all cells have semantic equations.
- `INV-L09-21 / HARD / TENSOR`: row, column, scale, context, and regime axes are non-interchangeable.
- `INV-L09-22 / HARD / TOPOLOGY`: relation presence or topological adjacency does not imply a causal edge.
- `INV-L09-23 / HARD / MATH`: nonstandard `1E∞` notation is not admitted as a standard tensor dimension/cardinality.

## RSCF and provenance invariants

- `INV-L09-24 / HIGH / PROVENANCE`: Every promoted inference result preserves dependency claim IDs, source provenance, scope, regime, and source/runtime version.
- `INV-L09-25 / HIGH / FRESHNESS`: A result cannot silently reuse a source binding after its version/regime dependency becomes stale.
- `INV-L09-26 / HIGH / CONFIDENCE`: For declared necessary conjunctive premises, derived confidence may not exceed the smallest known premise confidence unless a separately justified strengthening rule exists.
- `INV-L09-27 / HIGH / UNKNOWN`: Missing premise confidence leaves the executable confidence ceiling unknown; it is not imputed.
- `INV-L09-28 / HARD / CANON`: Freshness or filename recency does not promote a repair candidate to Canon.

## Implementation evidence

The staged reference runtime currently binds executable checks for `INV-L09-05`, `07`–`15`, `24`, `26`, and `27` through `inference_runtime.py` plus its regression suite. The remaining invariants are contract-level gates unless separately executable elsewhere.

```text
DOCUMENTED_INVARIANT != EXECUTABLE_ENFORCEMENT
EXECUTED_BOUNDED_CHECK != UNIVERSAL_PROOF
MODEL != EMPIRICAL_LAW
```

RSCF-NODE

```text
node_id: l09_primitives_invariants
node_type: invariant_contract
claim_class: AMOS_MODEL
rscf_state: DERIVED
canonical_status: CONDITIONAL
```

**MOC:** [[25_COGNITIVE_MATRIX/01_PRIMITIVES/L09_INFERENCE/L09_INFERENCE_MOC|L09_INFERENCE_MOC]]
