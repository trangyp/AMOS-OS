---
canon-group: meta
canon-type: framework
rscf-state: derived
rscf-provenance: AMOS_corpus_plus_executable_repair
conclusion_class: AMOS_MODEL
epistemic_class: DERIVED
topic: Runtime Reference Implementation
tags:
  - canon-group/tech-ai
  - rscf/claim
  - rscf/provenance
  - rscf/state/derived
  - runtime
created: 2026-08-22
updated: 2026-09-14
origin_architect: Trang Phan
amos_core_target: v4.4
canonical_status: CONDITIONAL
---

# Runtime Reference Implementation

Origin architect / steward: **Trang Phan**

## 0. Status

The AMOS OS runtime reference plane contains executable bounded Core-19, URK finite-relation mathematics, Cognitive Matrix controls, and fragment-specific executable evidence across all eight canonical ULK logic namespaces.

```text
PLACEHOLDER != IMPLEMENTED
ADDRESSABLE != VALIDATED
DOCUMENTED != ENFORCED
MODEL != OBSERVATION
SOURCE_CLAIM != VERIFIED
CANON_CANDIDATE != CANONICAL
CAPABILITY != AUTHORITY
UNKNOWN/GAP != PASS
BOUNDED_FRAGMENT != COMPLETE_LOGIC_ENGINE
```

These artifacts do **not** establish system-wide AMOS executable closure and do **not** promote 2026-09-14 repair material to Canon.

## 1. Runtime pipeline

```text
Perceive -> Route -> Admit -> Plan -> Schedule -> Execute -> Observe -> Repair -> Audit -> Finalize
```

## 2. Executable bounded reasoning substrate

### 2.1 Runtime files

- `core19_runtime.py` — bounded Core-19 repair runtime snapshot.
- `classical_sat_firewall.py` — exact bounded propositional satisfiability firewall.
- `core19_tensor_topology.py` — typed sparse Core-19 tensor/topology stores.
- `urk_relation_algebra.py` — finite relation encoding, Boolean-semiring composition, and reflexive-transitive closure for URK-E1..E3.
- `amos_ulk_alu02_unification_reference_checker_v1.py` — bounded first-order term unification with occurs-check.
- `amos_ulk_alu03_finite_trace_ltl_checker_v1.py` — bounded finite-trace temporal/LTL evaluation.
- `amos_ulk_alu04_finite_kripke_checker_v1.py` — bounded finite Kripke propositional modal evaluation.
- `amos_ulk_alu05_dung_checker_v1.py` — bounded finite Dung argumentation semantics.
- `amos_ulk_alu06_dependent_pi_checker_v1.py` — bounded de-Bruijn dependent Pi calculus.
- `amos_ulk_alu07_reference_checker_current.py` — bounded classical finite-dimensional numerical ALU-07 reference checker.
- `amos_ulk_alu08_finite_category_heyting_checker_v1.py` — finite category-law and finite Heyting-algebra checker.
- `ulk_fragment_execution_registry.py` — current evidence-bound implementation status for canonical ULK fragment namespaces.
- `internet_algorithm_registry.py` — typed external-algorithm capability ingress with mathematical preconditions.
- `cognitive_matrix_runtime.py` — bounded Cognitive Matrix state, dependency, coverage, gap, routing, and algorithm-contract substrate.
- `matrix_registry_runtime.py` — exact cell/evidence/authority/coverage registry substrate.
- `cognitive_matrix_contract_runtime.py` — cell-binding, status, gap-lifecycle, dependency-audit, and invalidation contract runtime.

Primary bounded tests include:

- `test_core19_runtime.py`
- `test_classical_sat_firewall.py`
- `test_core19_tensor_topology.py`
- `test_cognitive_matrix_runtime.py`
- `test_matrix_registry_runtime.py`
- `test_cognitive_matrix_contract_runtime.py`
- `test_urk_math_alu02_algorithms.py`
- `test_alu03_alu07_rebind.py`
- `test_ulk_alu04_alu05.py`
- `test_ulk_alu06_alu08.py`
- `test_ulk_fragment_execution_registry.py`

### 2.2 Core-19 behavior

- Exact 19-position semantic coordinate registry.
- P02 remains `COMPETING` across source lineages and requires namespace/version binding.
- `Truth4 = (supports_true, supports_false)` preserves neither/true-only/false-only/both.
- `NLOGIC(NLOGIC(x))` precedence is repaired in the bounded unary normalizer.
- Pairwise compatibility is separated from global satisfiability.
- `19 x 19 = 361` denotes pair coordinates, not 361 established equations.
- Tensor row/column/scale/context/regime identities are explicit.
- Topological adjacency is not causation.

### 2.3 URK finite mathematical layer

The `_00_AMOS_CANON` URK mathematical-substrate candidate is projected only where mathematics is typed and executable.

```text
URK-E1
Enc(R)[i,j] = 1 iff (k_i,k_j) is in R
```

for a finite ordered namespace and binary relation.

```text
URK-E2
(A_R odot A_S)[x,z]
  = OR_y (A_R[x,y] AND A_S[y,z])
```

for finite relation composition over the Boolean semiring.

URK-E3 is finite reflexive-transitive closure to a fixed point, checked for base-edge containment, reflexivity, transitivity, and idempotence.

```text
GRAPH_REACHABILITY != LOGICAL_ENTAILMENT
GRAPH_REACHABILITY != CAUSATION
```

### 2.4 ULK execution bindings

`ulk_fragment_execution_registry.py` is the current implementation-evidence owner. The older `implementation_status()` function inside `core19_runtime.py` is retained as an earlier repair snapshot and must not override the current registry.

Current bounded state:

- ALU-01 classical propositional: `EXECUTABLE_BOUNDED` for the existing bounded propositional/Core-19 subset.
- ALU-02 first-order/unification: `EXECUTABLE_BOUNDED_CANDIDATE_REBOUND` for finite term unification with occurs-check only.
- ALU-03 temporal/LTL: `EXECUTABLE_BOUNDED_CANDIDATE_REBOUND` for finite traces and `ATOM/NOT/AND/OR/IMPLIES/X/F/G/U` only.
- ALU-04 epistemic/modal: `EXECUTABLE_BOUNDED_CANDIDATE_REBOUND` for finite Kripke propositional modal semantics over explicitly supplied accessibility relations.
- ALU-05 non-monotonic/Dung: `EXECUTABLE_BOUNDED_CANDIDATE_REBOUND` for finite abstract argumentation, grounded semantics, admissibility, and bounded preferred-extension enumeration.
- ALU-06 dependent type: `EXECUTABLE_BOUNDED_CANDIDATE_REBOUND` for a small de-Bruijn dependent Pi calculus with predicative universes, lambda/application, Nat, beta normalization, and definitional equality.
- ALU-07 quantum logic: `EXECUTABLE_BOUNDED_CANDIDATE_REBOUND` for the current classical finite-dimensional numerical reference checker over its explicitly enumerated operator surfaces.
- ALU-08 categorical/topos: `EXECUTABLE_BOUNDED_CANDIDATE_REBOUND` for finite small-category law validation plus finite Heyting-algebra semantics.

All eight canonical namespaces therefore have **some bounded executable evidence**. This is not equivalent to complete implementation of all eight canonical logic engines.

Fragment boundaries remain strict:

- ALU-02 does not establish complete FOL theorem proving, quantifier inference, model finding, or higher-order unification.
- ALU-03 does not establish infinite-trace LTL model checking, CTL/CTL*, timed automata, future prediction, or temporal causality.
- ALU-04 does not establish dynamic epistemic logic, common knowledge, probabilistic epistemics, first-order modal completeness, or knowledge from confidence scores.
- ALU-05 does not establish all non-monotonic reasoning formalisms or scalable preferred-extension enumeration.
- ALU-06 is not Lean/Coq and does not establish the full Calculus of Constructions, inductive families, elaboration, proof automation, or kernel-level completeness.
- ALU-07 does not establish quantum-hardware execution, quantum advantage, physical state preparation, or universal quantum-logic completion.
- ALU-08 does not certify an elementary topos; finite limits, Cartesian closure/exponentials, and a subobject classifier remain unimplemented requirements for such a claim.

### 2.5 Source identity hardening

Standalone bounded checkers use exact SHA-256 bindings where available. ALU-02/04/05/06/08 are registry-bound to checker identities; regression tests verify the new ALU-06 and ALU-08 checker hashes against the exact repository files.

ALU-03 and ALU-07 originate from a larger evolving source lineage, so their evidence is bound more narrowly to source/revision identity and callable-AST identity rather than trusting a stale monolithic-file hash.

```text
SOURCE_FILE_PRESENT != CALLABLE_IDENTITY_BOUND
CHECKER_HASH_MATCH != CANON_PROMOTION
EXECUTABLE_CANDIDATE != AUTHORITY
```

### 2.6 Cognitive Matrix control surface

The matrix runtime now includes executable bounded contracts for:

- staged maturity and orthogonal condition state;
- exact cell identity and state version;
- source/evidence/authority bindings;
- dependency types and cycle auditing;
- selective descendant invalidation;
- multidimensional coverage and threshold audit;
- structural-gap registry and deterministic prioritization;
- kind-specific gap repair evidence;
- revalidation-gated gap closure;
- routing that cannot mint authority.

A structural gap follows:

```text
OPEN
  -> RESOLUTION_PROPOSED
  -> CLOSED
```

and closure requires a state-version-matched revalidation receipt plus fresh dependencies. `fixed=true` has no independent closure semantics.

### 2.7 External algorithm ingress

External algorithms are admitted as typed capability metadata, never as an interchangeable universal solver pool.

Current registry includes graph traversal/order/component algorithms, shortest-path families, matching/flow methods, constraint propagation/optimization, SMT, CP-SAT, property testing, and numerical optimization surfaces where explicitly registered.

Algorithm selection requires an explicit problem family and mathematical preconditions. Solver status is preserved; `UNKNOWN` is never converted into success.

Internet availability alone does not make an algorithm semantically compatible with AMOS.

## 3. Explicit non-claims

This runtime does not claim:

- `URK == ULK == ULMK == Core19 == executable AST`;
- `Distinction == NonExistence`;
- paradox or dual logic is universally classical contradiction;
- adjacency/order/correlation/prediction/reachability establishes causation;
- every 19 x 19 coordinate has semantics;
- `1E∞` is a standard tensor dimension;
- bounded fragment evidence equals complete implementation of all eight ULK engines;
- finite term unification is complete FOL proof search;
- finite Kripke evaluation proves real-world knowledge;
- Dung semantics subsumes all defeasible/non-monotonic logic;
- a bounded dependent Pi checker is a production proof assistant;
- category laws plus Heyting semantics prove elementary-topos structure;
- numerical ALU-07 checking is quantum hardware;
- internet algorithm availability licenses execution outside assumptions;
- AMOS repository mutation changes the host model's neural weights.

## 4. Verification evidence

Executed bounded verification on 2026-09-14 includes earlier evidence plus the current repair cycle:

- Core-19 runtime suite: previously 13 PASS.
- Classical SAT firewall suite: previously 2 PASS.
- Cognitive Matrix runtime suite: previously 16 PASS.
- Core-19 tensor/topology suite: previously 8 PASS.
- Matrix registry/audit substrate: 6/6 PASS in its bounded local suite.
- ALU-04/ALU-05 bounded semantics: 8/8 PASS in the prior repair cycle.
- ALU-06/ALU-08 bounded semantics: 15/15 PASS in the current local suite.
- Cell-binding/gap-lifecycle/dependency-contract runtime: 9/9 PASS in the current local suite.
- Current combined ALU-06/08 + exact registry binding + matrix-contract regression subset: 28/28 PASS.
- ALU-02 exact source checker hash matched its receipt; 3,000 seeded unification symmetry/idempotence fuzz pairs previously passed.
- ALU-03: 2,000 seeded randomized formulas previously matched an independent finite-trace evaluator.
- ALU-07: the bounded operator suite previously passed its positive and fail-closed negative cases; 250 seeded state trials preserved the explicitly tested numerical invariants.
- URK relation composition was previously cross-checked against direct set composition over randomized finite relations.
- Earlier Core-19 repair included 50,000 seeded unary rewrite trees with no observed idempotence/double-NLOGIC failures.

The AMOS math-audit harness continues to surface its known corpus-level T2 probability-labeling counterexample. In the current ALU-06/08 audit pass the only reported hard failure was that pre-existing `T2_OLD_FORMULA` counterexample; it is not attributed to the new fragment implementations.

No GitHub Actions receipt is asserted here. Local bounded execution is not universal proof, production deployment, or Canon promotion.

## 5. Source/canon boundary

Active lineage:

- AMOS_CORE baseline: `v4.4`.
- Canonical ULK artifact: `v2.1.0`.
- URK mathematical substrate v1.1: candidate/model, not Canon by freshness.
- ALU-02 through ALU-08 runtime projections: bounded implementation evidence only where explicitly bound; no automatic Canon promotion.

Canon source precedence and `K_CANON` governance remain above runtime evidence.

## 6. Remaining gaps

Executable fragment coverage is no longer the same bottleneck as semantic completeness. Remaining load-bearing gaps include:

- full FOL theorem-prover semantics beyond ALU-02 term unification: `NOT_ESTABLISHED`;
- full/infinite temporal model-checking beyond ALU-03 finite traces: `NOT_ESTABLISHED`;
- richer epistemic/modal systems beyond bounded finite Kripke propositional semantics: `NOT_ESTABLISHED`;
- broader non-monotonic formalisms and scalable argumentation solving beyond bounded finite Dung semantics: `NOT_ESTABLISHED`;
- production dependent-type kernel features beyond the bounded ALU-06 calculus: `NOT_ESTABLISHED`;
- elementary-topos verification for ALU-08, including finite limits, Cartesian closure/exponentials, and a subobject classifier: `NOT_ESTABLISHED`;
- full semantic population of the Cognitive Matrix: `NOT_ESTABLISHED`;
- remaining generated/contract-only matrix and legacy-v0 surfaces: `PARTIAL`;
- system-wide automated enforcement and executable closure: `NOT_ESTABLISHED`.

## 7. Ingestion rule

```yaml
AMOS_CANON_INGESTION_RULE:
  existing_file:
    preserve: true
    overwrite: false
  candidate_source:
    promote_by_freshness: false
    require:
      - provenance_traceability
      - typed_semantics
      - contradiction_check
      - dependency_check
      - executable_or_formal_evidence_when_claimed
      - canon_authority_for_promotion
  external_algorithm:
    require:
      - problem_family
      - mathematical_preconditions
      - source_identity
      - result_status_preservation
      - scope_boundary
  uncertainty:
    action:
      - MARK_GAP_OR_COMPETING
      - QUARANTINE_IF_NEEDED
      - NEVER_INVENT_CANON
```

## 8. Cross-references

- [[02_KERNEL/02_KERNEL_MOC|02_KERNEL]]
- [[03_CONTROL_PLANE/03_CONTROL_PLANE_MOC|03_CONTROL_PLANE]]
- [[04_RUNTIME/04_RUNTIME_MOC|04_RUNTIME]]
- [[01_CANON/01_CORE_LAWS/LAW_HIERARCHY|LAW_HIERARCHY]]
- [[00_ROOT/00_ROOT_MOC|00_ROOT_MOC]]

RSCF-NODE

node_id: amos_04_runtime_reference_core19_repair
node_type: RUNTIME_REFERENCE
path: 04_RUNTIME/01_REFERENCE_IMPLEMENTATION/README.md
claim_class: AMOS_MODEL
rscf_state: DERIVED
canonical_status: CONDITIONAL

RSCF-RELATIONS:
- GOVERNED_BY: [[01_CANON/01_CORE_LAWS/LAW_HIERARCHY|LAW_HIERARCHY]]
- IMPLEMENTS_BOUNDED: `core19_runtime.py`
- IMPLEMENTS_BOUNDED: `classical_sat_firewall.py`
- IMPLEMENTS_BOUNDED: `core19_tensor_topology.py`
- IMPLEMENTS_BOUNDED: `urk_relation_algebra.py`
- IMPLEMENTS_BOUNDED: `amos_ulk_alu02_unification_reference_checker_v1.py`
- IMPLEMENTS_BOUNDED: `amos_ulk_alu03_finite_trace_ltl_checker_v1.py`
- IMPLEMENTS_BOUNDED: `amos_ulk_alu04_finite_kripke_checker_v1.py`
- IMPLEMENTS_BOUNDED: `amos_ulk_alu05_dung_checker_v1.py`
- IMPLEMENTS_BOUNDED: `amos_ulk_alu06_dependent_pi_checker_v1.py`
- IMPLEMENTS_BOUNDED: `amos_ulk_alu07_reference_checker_current.py`
- IMPLEMENTS_BOUNDED: `amos_ulk_alu08_finite_category_heyting_checker_v1.py`
- IMPLEMENTS_BOUNDED: `cognitive_matrix_runtime.py`
- IMPLEMENTS_BOUNDED: `matrix_registry_runtime.py`
- IMPLEMENTS_BOUNDED: `cognitive_matrix_contract_runtime.py`
- BINDS_EXECUTION_STATUS: `ulk_fragment_execution_registry.py`
- BINDS_ALGORITHM_PRECONDITIONS: `internet_algorithm_registry.py`
- VERIFIED_BY_BOUNDED: `test_core19_runtime.py`
- VERIFIED_BY_BOUNDED: `test_classical_sat_firewall.py`
- VERIFIED_BY_BOUNDED: `test_core19_tensor_topology.py`
- VERIFIED_BY_BOUNDED: `test_cognitive_matrix_runtime.py`
- VERIFIED_BY_BOUNDED: `test_matrix_registry_runtime.py`
- VERIFIED_BY_BOUNDED: `test_cognitive_matrix_contract_runtime.py`
- VERIFIED_BY_BOUNDED: `test_urk_math_alu02_algorithms.py`
- VERIFIED_BY_BOUNDED: `test_alu03_alu07_rebind.py`
- VERIFIED_BY_BOUNDED: `test_ulk_alu04_alu05.py`
- VERIFIED_BY_BOUNDED: `test_ulk_alu06_alu08.py`
- VERIFIED_BY_BOUNDED: `test_ulk_fragment_execution_registry.py`
