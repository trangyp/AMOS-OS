---
canon-group: cognition
canon-type: runtime_contract
rscf-state: derived
rscf-provenance: AMOS_corpus_plus_2026_09_14_URK_repair
conclusion_class: AMOS_MODEL
epistemic_class: DERIVED
topic: L09 Inference Primitives Cognitive Matrix Definition
created: 2026-08-22
updated: 2026-09-14
origin_architect: Trang Phan
amos_core_target: v4.4
canonical_status: CONDITIONAL
implementation_status: PARTIAL_EXECUTABLE_BINDING
---

# L09 — Inference Definition

**Package:** `L09_INFERENCE`  
**Origin architect / steward:** **Trang Phan**

## Purpose

L09 maps typed premises and a query into a scoped inference result while keeping URK mathematics, ULK logic routing, Core-19 semantic coordinates, executable syntax, empirical interpretation, and effect authority separate.

It is an inference boundary, not a universal truth engine.

## Typed contract

```text
InferenceRequest
  query_or_conclusion
  logic_fragment
  premises[]
  context
  scope
  regime
  source_version
  provenance[]
  optional_P02_namespace_binding
  causal_claim_flag
  causal_evidence_binding

InferenceResult
  status
  fragment_implementation_status
  dependency_claim_ids[]
  provenance[]
  scope
  regime
  source_version
  confidence_ceiling_or_unknown
  consistency_state
  entailment_state
  gap_or_competing_reason
```

## Governed pipeline

```text
TYPE
-> SOURCE_BIND
-> FRAGMENT_ROUTE
-> P02_BIND_IF_USED
-> CAUSAL_GATE_IF_USED
-> GLOBAL_CONSISTENCY_CHECK
-> INFER
-> STATUS_BIND
-> PROVENANCE_BIND
-> RETURN
```

## Fragment routing

Current repair-surface implementation state:

- `ClassicalPropositional` -> `EXECUTABLE_BOUNDED`.
- `QuantumLogic` -> `CANONICAL_BOUNDED_CLAIM_REBIND_PENDING`.
- FOL/unification, temporal/LTL, epistemic/modal, non-monotonic/Dung, dependent type, and categorical/topos -> `SPECIFICATION_ONLY` here.

A specification is not treated as an executable checker.

## P02 binding

Cross-lineage P02 is `COMPETING`:

```text
historical lineage -> NonExistence
recovered living-map lineage -> Distinction
```

Any inference that depends on P02 requires an explicit namespace/version binding. Unresolved P02 use returns `COMPETING` or `UNKNOWN/GAP`.

## Consistency and entailment

For the bounded classical fragment, L09 checks global satisfiability of the complete premise set. Pairwise compatibility alone is insufficient.

If the premise set is inconsistent, the contradiction remains inspectable and L09 returns `INCONSISTENT_INPUT` rather than promoting a conclusion.

For a declared conclusion, entailment is checked by testing whether:

```text
Premises AND NOT(Conclusion)
```

is satisfiable.

- unsatisfiable -> `VERIFIED_BOUNDED`;
- satisfiable -> `NOT_ENTAILED`;
- checker unavailable or bound exceeded -> `UNKNOWN/GAP`.

## Causal firewall

Logical implication, ordering, correlation, adjacency, prediction, and topology do not by themselves establish real-world causation. A causal result therefore requires a separately bound causal model/evidence contract.

## Core-19 ownership boundary

```text
ULK eight logic-engine ALUs
!= ULMK eight Atomic Logic Units
!= Core-19 semantic vocabulary
!= executable formula syntax
!= domain empirical mechanisms
```

The 19 semantic coordinates do not imply a total 19 x 19 algebra or an invented executable node.

## Partial semantics

Undefined Core-19 interactions remain `UNBOUND`.

```text
UNBOUND != false
UNBOUND != zero
UNBOUND != fabricated rule
```

## Truth-status boundary

The repaired meta-state can preserve four evidence states:

```text
NEITHER     = (false, false)
TRUE_ONLY   = (true, false)
FALSE_ONLY  = (false, true)
BOTH        = (true, true)
```

This does not make every `Paradox` or `DualLogic` occurrence universally identical to one classical contradiction formula. Historical runtime rewrites remain source-scoped behavior.

## Executable binding

Current bounded implementation:

- `04_RUNTIME/01_REFERENCE_IMPLEMENTATION/core19_runtime.py`
- `04_RUNTIME/01_REFERENCE_IMPLEMENTATION/classical_sat_firewall.py`
- `04_RUNTIME/01_REFERENCE_IMPLEMENTATION/inference_runtime.py`
- `04_RUNTIME/01_REFERENCE_IMPLEMENTATION/test_inference_runtime.py`

The staged L09 inference suite passes 10/10 reconstructed local tests. This is bounded reference-runtime evidence only.

## Remaining gaps

General FOL, temporal, modal, non-monotonic, dependent-type, quantum, categorical/topos, abductive-ranking, and domain-causal engines remain unbound or specification-only in this L09 runtime surface.

## Hard boundaries

```text
FORMALLY_ENTAILED != EMPIRICALLY_TRUE
IMPLICATION != CAUSATION
PAIRWISE_COMPATIBLE != GLOBALLY_CONSISTENT
CORE19_COORDINATE != PROVEN_SEMANTIC_RULE
CANON_VOCABULARY != EXECUTABLE_AST
SOURCE_RUNTIME_RULE != UNIVERSAL_SEMANTICS
CAPABILITY != AUTHORITY
MODEL != VERIFIED_EMPIRICAL_LAW
CANDIDATE_FRESHNESS != CANON_PROMOTION
UNKNOWN/GAP != PASS
```

## RSCF node

```text
node_id: l09_primitives_definition
node_type: runtime_contract
claim_class: AMOS_MODEL
rscf_state: DERIVED
canonical_status: CONDITIONAL
```

**MOC:** [[25_COGNITIVE_MATRIX/01_PRIMITIVES/L09_INFERENCE/L09_INFERENCE_MOC|L09_INFERENCE_MOC]]  
**Runtime:** [[04_RUNTIME/01_REFERENCE_IMPLEMENTATION/README|Runtime Reference Implementation]]
