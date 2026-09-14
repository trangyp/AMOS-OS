---
canon-group: meta
canon-type: runtime_reference
rscf-state: derived
rscf-provenance: AMOS_corpus_plus_executable_repair
conclusion_class: AMOS_MODEL
epistemic_class: DERIVED
topic: Runtime Reference Implementation
created: 2026-08-22
updated: 2026-09-14
origin_architect: Trang Phan
amos_core_target: v4.4
canonical_status: CONDITIONAL
---

# Runtime Reference Implementation

Origin architect / steward: **Trang Phan**

## Status

The reference plane contains bounded executable repairs for:

1. URK/Core-19 typed state and rewrite semantics;
2. bounded classical satisfiability;
3. L09 bounded classical inference;
4. ALU-02 finite first-order term unification;
5. L10 world-model / reality-contact separation;
6. shared Cognitive Matrix cell state/evidence/binding validation;
7. Cognitive Matrix scoped coverage and structural-gap accounting;
8. typed dependency relations and selective invalidation;
9. insertion-incremental dependency reachability and SCC cycle localization;
10. bounded Cognitive Matrix routing over the implemented surfaces.

```text
PLACEHOLDER != IMPLEMENTED
DOCUMENTED != EXECUTABLE
SOURCE_CLAIM != VERIFIED
MODEL != OBSERVATION
CANON_CANDIDATE != CANONICAL
CAPABILITY != AUTHORITY
ROUTED != COMMITTED
UNKNOWN/GAP != PASS
DEPENDENCY != CAUSATION
ALGORITHM_KNOWN != AMOS_ADMITTED_IMPLEMENTATION
```

These modules are bounded reference implementations. They do not establish system-wide AMOS executable closure, deployment validity, or Canon promotion.

## Runtime components

### URK / Core-19

- `core19_runtime.py`
- `test_core19_runtime.py`

Implements the 19-coordinate registry, P02 competing-lineage binding, Truth4 evidence state, typed matrix/tensor/topology coordinates, fragment status, promotion gates, and repaired `NLOGIC` normalization order.

### Classical satisfiability firewall

- `classical_sat_firewall.py`
- `test_classical_sat_firewall.py`

Implements exact truth-table satisfiability for the declared bounded Boolean grammar and separates pairwise compatibility from global consistency.

### L09 bounded classical inference

- `inference_runtime.py`
- `test_inference_runtime.py`

Implements fail-closed fragment routing, P02 binding, causal-claim separation, global premise consistency, bounded classical entailment, provenance/dependency carry, confidence ceilings, and atom bounds.

### ULK ALU-02 finite term unification

- `unification_runtime.py`
- `test_unification_runtime.py`
- `test_routing_unification_integration.py`

Implements a finite first-order **term-unification subfragment** over variables, constants, and finite function terms. It uses an occurs-check, explicit substitution normalization, malformed-input rejection, recursion/node/equation-step bounds, and a result self-check that verifies the returned substitution actually unifies the inputs.

This surface is intentionally narrower than full first-order logic:

```text
TERM_UNIFICATION != QUANTIFIER_INFERENCE
TERM_UNIFICATION != FOL_THEOREM_PROVER
TERM_UNIFICATION != MODEL_FINDER
TERM_UNIFICATION != HIGHER_ORDER_UNIFICATION
```

The implementation is derived from the 2026-09-14 `_00_AMOS_CANON` ALU-02 executable candidate plus independent local stress testing. It is **not** Canon merely because it is executable.

### L10 world modeling

- `world_model_runtime.py`
- `test_world_model_runtime.py`

Separates observed reality, measured proxy, model state, simulation, counterfactual, synthetic data, digital twin, forecast, and deployed outcome. Implements fidelity/reality-contact/commensurability gates and conservative provenance/generator ancestry.

### Cognitive Matrix cell contract

- `cognitive_matrix_cell_runtime.py`
- `test_cognitive_matrix_cell_runtime.py`

Implements typed cell axes, epistemic/runtime statuses, evidence roots/freshness/receipts, semantic/runtime/authority owner separation, `UNBOUND != zero`, and transform gates.

### Cognitive Matrix coverage and structural gaps

- `cognitive_matrix_coverage_runtime.py`
- `test_cognitive_matrix_coverage_runtime.py`

Implements declared scopes/requirements, active-stage versus exception-state separation, dependency adjacency/Boolean transitive closure, cycle/undeclared-dependency detection, dependency-aware completion states, typed structural gaps, and receipt-gated promotion.

### Typed dependency graph

- `cognitive_matrix_dependency_runtime.py`
- `test_cognitive_matrix_dependency_runtime.py`
- `test_dependency_coverage_integration.py`

Preserves typed relation semantics. Only `NECESSARY`, `DERIVED_FROM`, and `CONDITIONED_ON` enter load-bearing dependency closure. Support/sufficiency loss triggers review, while unrelated state remains preserved. Invalidation proposes `STALE` for load-bearing descendants; it does not fabricate falsity or durable authority.

### Incremental dependency index

- `incremental_dependency_index.py`
- `test_incremental_dependency_index.py`

Adds insertion-incremental exact reachability and Tarjan strongly-connected-component localization. For an admitted new load-bearing edge `u -> v`, closure propagation is restricted to the current predecessor set of `u` crossed with the current successor set of `v`, including endpoints. Deletions fail closed to recomputation because monotone insertion closure cannot safely remove reachability by local subtraction without extra support-count state.

This is an optimization of typed dependency topology only:

```text
REACHABILITY != CAUSALITY
SCC != LOGICAL_EQUIVALENCE
INCREMENTAL_INSERTION != SAFE_INCREMENTAL_DELETION
```

### Cognitive Matrix routing

- `cognitive_matrix_routing_runtime.py`
- `test_cognitive_matrix_routing_runtime.py`
- `test_routing_unification_integration.py`

Implements hard-gate-first routing over exact scope, regime, capabilities, executable status, validation, named epochs, and provenance-root requirements. Semantic priority is considered only after hard constraints pass. Equal best candidates remain `AMBIGUOUS`; explicit target failure does not silently fall back; registration order is non-semantic.

Effectful requests preserve the authority firewall:

```text
CAPABILITY != AUTHORITY
ROUTED != AUTHORIZED_EFFECT
AUTHORITY_PRESENT != EFFECT_COMMITTED
```

Even an authority-bound effectful route produces `PROPOSAL_ONLY`; durable commit remains owned by the AMOS infrastructure/control plane.

## Source/canon owner separation

The 2026-09-14 `_00_AMOS_CANON` repair material remains candidate source input until governed admission.

```text
URK -> mathematical/meta-structural substrate
       equations, invariants, tensors, matrices, topology,
       state spaces, operators, transforms

ULK -> formal-logic fragment routing, inference/proof semantics,
       proof-status binding

Core-19 -> typed semantic coordinate vocabulary
           not a total algebra by coordinate existence
```

`URK_MATH != ULK_LOGIC`, and mathematical validity, logical validity, empirical truth, execution evidence, and authority remain distinct.

### Current bounded logic execution map

- Classical propositional entailment: `EXECUTABLE_BOUNDED`.
- ALU-02 finite first-order term unification: `EXECUTABLE_BOUNDED_SUBFRAGMENT`.
- Full FOL quantifier inference / theorem proving: `SPECIFICATION_ONLY / NOT_IMPLEMENTED`.
- Quantum ALU-07: `CANONICAL_BOUNDED_CLAIM_REBIND_PENDING`.
- Temporal/LTL, epistemic/modal, non-monotonic/Dung, dependent type, categorical/topos: `SPECIFICATION_ONLY` in this reference plane.

No subfragment execution state is generalized into a stronger fragment claim.

## URK mathematical substrate boundary

The current candidate mathematical substrate uses typed partial maps such as:

```text
R : Core19 x Core19 x Context x Regime ->? TypedRelation
A : Core19 x Core19 x Context ->? TypedAdjacency
C : Core19 x Core19 x Time x Context x Regime ->? TypedCausalEdge
T : Core19 x Core19 x Scale x Context x Regime x Observer ->? Value
```

where `->?` denotes a partial map. A missing value remains unbound/unknown rather than fabricated as zero.

Hard invariants:

```text
TOPOLOGICAL_ADJACENCY != CAUSAL_EDGE
MATRIX_COORDINATE_EXISTS != EQUATION_PROVED
CORE19_SEMANTIC_COORDINATE != EXECUTABLE_AST_CONSTRUCTOR
SOURCE_CANON != EXECUTABLE_PROOF
AMOS_MODEL != ESTABLISHED_MATH
```

## Verification evidence

Local bounded receipts accumulated on 2026-09-14:

- previously represented branch suites: **88 PASS / 0 FAIL**;
- ALU-02 hardened unification suite: **13 PASS / 0 FAIL**;
- Cognitive Matrix routing suite: **24 PASS / 0 FAIL**;
- incremental dependency-index suite: **10 PASS / 0 FAIL**;
- routing/unification integration: **5 PASS / 0 FAIL**;
- new mutation subtotal: **52 PASS / 0 FAIL**;
- cumulative local receipt sum represented by these surfaces: **140 PASS / 0 FAIL**.

Additional bounded stress evidence:

- Core-19 unary rewrite stress: **50,000 trees / 0 observed failures** for tested rewrite properties;
- ALU-02 source-checker independent random stress: **20,000 term pairs / 0 observed property failures**;
- coverage topology differential stress: **5,000 graphs / 0 observed closure mismatches**;
- coverage promotion state-space check: **128 combinations / 0 observed invalid admissions**;
- dependency stress: **5,000 DAGs / 29,949 closure-node checks / 5,000 selective-invalidation checks / 0 observed mismatches**;
- incremental index randomized insertion suites matched full DFS closure in the tested space.

The incremental dependency benchmark used a 220-node / 900-edge synthetic insertion workload in the current local environment. Incremental maintenance took about `0.0133 s` versus `0.673 s` for full closure recomputation after every insertion, approximately `50.8x` faster in that benchmark. This is not a universal performance claim.

```text
LOCAL PASS != FORMAL PROOF
LOCAL PASS != UNIVERSAL AMOS CORRECTNESS
LOCAL PASS != DEPLOYMENT VALIDATION
LOCAL PASS != CANON PROMOTION
ONE SYNTHETIC SPEEDUP != UNIVERSAL SPEEDUP
```

No GitHub Actions receipt is attached to these staged changes at the time of this update.

## External-algorithm admission boundary

External algorithms are research inputs, not authority. An algorithm may enter the active reference plane only when its semantics are compatible with the target AMOS type/invariants, its scope is explicit, its failure modes are bounded, and executable validation exists for the admitted implementation.

Current admitted mechanisms in this repair include bounded first-order term unification, Boolean transitive closure, Tarjan SCC decomposition, and insertion-incremental reachability. Equality saturation/e-graphs, semi-naive/Datalog evaluation, differential dataflow, incremental SMT contexts, and symbolic model checking remain research candidates until a concrete AMOS use case and regression-preserving implementation justify admission.

## Effect-authority boundary

Reasoning/Cognitive Matrix runtimes compute, validate, route, and propose. They do not authorize durable effects.

Durable/external effects remain subordinate to the infrastructure control plane for current intent/policy, observed read sets, transaction lineage, fresh authority, idempotency, receipts/reconciliation, rollback, and finality.

## Remaining high-value gaps

- full FOL quantifier semantics, proof search, and model finding;
- temporal/LTL model checking;
- epistemic/modal execution;
- non-monotonic/Dung execution;
- dependent-type checking;
- ALU-07 exact checker/receipt rebind;
- categorical/topos execution;
- general abductive ranking/calibration;
- cross-scale world-model transforms with explicit information-loss contracts;
- probabilistic world-state estimation/calibration;
- repository-wide authoritative requirement extraction into coverage;
- persistent typed registry/dependency identity and version storage;
- authority-bound invalidation/supersession receipts;
- explicit fixed-point semantics for intentionally cyclic dependency graphs;
- system-wide CI-bound executable closure;
- reconciliation of this draft branch with newer `main` governance before merge.

## Canon ingestion rule

```yaml
candidate_source:
  promote_by_freshness: false
  require:
    - provenance_traceability
    - typed_semantics
    - contradiction_check
    - dependency_check
    - mathematical_checks_when_claimed
    - executable_or_formal_evidence_when_claimed
    - canon_authority_for_promotion
uncertainty:
  preserve:
    - UNKNOWN_GAP
    - COMPETING
    - STALE
    - QUARANTINED
```

## Cross-references

- [[02_KERNEL/02_KERNEL_MOC|02_KERNEL]]
- [[03_CONTROL_PLANE/03_CONTROL_PLANE_MOC|03_CONTROL_PLANE]]
- [[04_RUNTIME/04_RUNTIME_MOC|04_RUNTIME]]
- [[25_COGNITIVE_MATRIX/01_PRIMITIVES/L09_INFERENCE/L09_INFERENCE_MOC|L09_INFERENCE]]
- [[25_COGNITIVE_MATRIX/01_PRIMITIVES/L10_WORLD_MODELING/L10_WORLD_MODELING_MOC|L10_WORLD_MODELING]]
- [[25_COGNITIVE_MATRIX/06_CELL_CONTRACTS/06_CELL_CONTRACTS_MOC|CELL_CONTRACTS]]
- [[25_COGNITIVE_MATRIX/07_COVERAGE/07_COVERAGE_MOC|COVERAGE]]
- [[25_COGNITIVE_MATRIX/08_STRUCTURAL_GAPS/08_STRUCTURAL_GAPS_MOC|STRUCTURAL_GAPS]]
- [[25_COGNITIVE_MATRIX/09_DEPENDENCY_GRAPH/09_DEPENDENCY_GRAPH_MOC|DEPENDENCY_GRAPH]]
- [[25_COGNITIVE_MATRIX/10_ROUTING/10_ROUTING_MOC|ROUTING]]
- [[01_CANON/01_CORE_LAWS/LAW_HIERARCHY|LAW_HIERARCHY]]

RSCF-NODE
node_id: amos_04_runtime_reference_core19_repair
node_type: RUNTIME_REFERENCE
path: 04_RUNTIME/01_REFERENCE_IMPLEMENTATION/README.md
claim_class: AMOS_MODEL
rscf_state: DERIVED
canonical_status: CONDITIONAL
