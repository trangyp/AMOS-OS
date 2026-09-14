---
canon-group: meta
canon-type: runtime_contract
rscf-state: derived
rscf-provenance: AMOS_corpus_plus_executable_repair
conclusion_class: AMOS_MODEL
epistemic_class: DERIVED
topic: Cognitive Matrix Routing Contract
created: 2026-08-22
updated: 2026-09-14
origin_architect: Trang Phan
---

# Cognitive Matrix Routing Contract

## Status

`AMOS_MODEL / EXECUTABLE_BOUNDED_REFERENCE / CANONICAL_STATUS_CONDITIONAL`

## Contract

Routing is a constrained selection function over a declared candidate set. Let `C(q)` be the candidates matching query kind `q`. Let `H(c,q)` be the conjunction of hard admissibility predicates for scope, regime, capabilities, implementation state, validation, epoch freshness, and explicit evidence requirements.

The admissible set is defined by:

`A(q) := { c in C(q) : H(c,q) }`.

This is ordinary set-builder notation. It does not imply that every routing criterion is mathematical truth; the predicates are policy/model definitions.

Decision behavior:

- `A(q)=empty` -> visible `DENY`, `REBIND_REQUIRED`, or `UNKNOWN/GAP` according to the blocking state;
- one policy-maximal candidate -> `ROUTED` for non-effectful work;
- multiple materially equal policy-maximal candidates -> `AMBIGUOUS`;
- effectful eligible route without authority binding -> `AUTHORITY_REQUIRED`;
- effectful eligible route with an authority binding -> `PROPOSAL_ONLY`, never commit.

## Protected distinctions

```text
ELIGIBLE != AUTHORIZED_TO_COMMIT
SUBFRAGMENT_EXECUTABLE != WHOLE_FRAGMENT_EXECUTABLE
PROVENANCE_ROOT_COUNT != PROVEN_INDEPENDENCE
ROUTING_DEPENDENCY != CAUSATION
VALIDATED_POLICY != LIVE_DEPLOYMENT
```

## Integration

- logic semantics remain owned by ULK;
- mathematical/meta-structural objects remain owned by URK;
- epistemic state remains RSCF-governed;
- durable effects remain control-plane governed;
- dependency freshness consumes typed dependency relations rather than generic graph adjacency.

## Current implementation

- runtime: `04_RUNTIME/01_REFERENCE_IMPLEMENTATION/cognitive_matrix_routing_runtime.py`
- tests: `test_cognitive_matrix_routing_runtime.py`
- ALU-02 executor: `unification_runtime.py`
- integration tests: `test_routing_unification_integration.py`

RSCF-NODE
node_id: cm_25_cognitive_matrix_10_routing_contract
node_type: ROUTING_CONTRACT
path: 25_COGNITIVE_MATRIX/10_ROUTING/COGNITIVE_MATRIX_ROUTING_CONTRACT.md
claim_class: AMOS_MODEL
rscf_state: DERIVED
