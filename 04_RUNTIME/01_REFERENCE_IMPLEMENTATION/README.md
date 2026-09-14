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

The AMOS OS runtime reference plane contains executable bounded Core-19, URK finite-relation/topology mathematics, Cognitive Matrix, and selected ULK fragment components.

```text
PLACEHOLDER != IMPLEMENTED
ADDRESSABLE != VALIDATED
DOCUMENTED != ENFORCED
MODEL != OBSERVATION
SOURCE_CLAIM != VERIFIED
CANON_CANDIDATE != CANONICAL
CAPABILITY != AUTHORITY
UNKNOWN/GAP != PASS
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
- `core19_tensor_topology.py` — typed sparse six-axis Core-19 tensor/topology stores.
- `finite_topology_runtime.py` — exact finite-carrier topology validation and specialization-preorder projection.
- `urk_relation_algebra.py` — finite relation encoding, Boolean-semiring composition, and reflexive-transitive closure for URK-E1..E3.
- `amos_ulk_alu02_unification_reference_checker_v1.py` — bounded first-order term unification with occurs-check.
- `amos_ulk_alu03_finite_trace_ltl_checker_v1.py` — bounded finite-trace temporal/LTL evaluation.
- `amos_ulk_alu04_finite_kripke_checker_v1.py` — bounded finite Kripke modal/epistemic evaluation.
- `amos_ulk_alu05_dung_checker_v1.py` — bounded finite Dung abstract-argumentation evaluation.
- `amos_ulk_alu07_reference_checker_current.py` — bounded classical finite-dimensional numerical ALU-07 reference checker.
- `ulk_fragment_execution_registry.py` — current evidence-bound implementation status for the canonical ULK fragment namespaces.
- `internet_algorithm_registry.py` — typed external-algorithm capability ingress with mathematical preconditions.
- `cognitive_matrix_runtime.py` — bounded Cognitive Matrix state, dependency, coverage, gap and routing substrate.

Primary bounded tests include:

- `test_core19_runtime.py`
- `test_classical_sat_firewall.py`
- `test_core19_tensor_topology.py`
- `test_finite_topology_runtime.py`
- `test_cognitive_matrix_runtime.py`
- `test_urk_math_alu02_algorithms.py`
- `test_alu03_alu07_rebind.py`
- `test_ulk_alu04_alu05.py`

### 2.2 Core-19 and tensor behavior

- Exact 19-position semantic coordinate registry.
- P02 remains `COMPETING` across source lineages and requires namespace/version binding.
- `Truth4 = (supports_true, supports_false)` preserves neither/true-only/false-only/both.
- `NLOGIC(NLOGIC(x))` precedence is repaired in the bounded unary normalizer.
- Pairwise compatibility is separated from global satisfiability.
- `19 x 19 = 361` denotes pair coordinates, not 361 established equations.
- Tensor coordinates bind six non-interchangeable axes:
  `row x column x scale x context x regime x observer`.
- Sparse absence means `UNBOUND`, not zero or false.
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

`finite_topology_runtime.py` adds exact bounded topology semantics for finite carriers. A finite open-set family must contain the empty set and full carrier and be closed under binary union and binary intersection; because the carrier is finite, arbitrary unions reduce to finite unions of distinct opens. The derived specialization relation is a preorder and remains a topological relation, never a causal edge by implication alone.

```text
GRAPH_REACHABILITY != LOGICAL_ENTAILMENT
GRAPH_REACHABILITY != CAUSATION
TOPOLOGICAL_PREORDER != CAUSATION
```

### 2.4 ULK execution bindings

`ulk_fragment_execution_registry.py` is the current implementation-evidence owner. The older `implementation_status()` function inside `core19_runtime.py` is retained as an earlier repair snapshot and must not override the current registry.

Current bounded state:

- ALU-01 classical propositional: `EXECUTABLE_BOUNDED`.
- ALU-02 first-order/unification: `EXECUTABLE_BOUNDED_CANDIDATE_REBOUND` for finite **term unification** with occurs-check only.
- ALU-03 temporal/LTL: `EXECUTABLE_BOUNDED_CANDIDATE_REBOUND` for finite traces and `ATOM/NOT/AND/OR/IMPLIES/X/F/G/U` only.
- ALU-04 epistemic/modal: `EXECUTABLE_BOUNDED_CANDIDATE_REBOUND` for finite Kripke models and propositional `NOT/AND/OR/IMPLIES/BOX/DIAMOND`; undeclared agents fail closed.
- ALU-05 non-monotonic/Dung: `EXECUTABLE_BOUNDED_CANDIDATE_REBOUND` for finite Dung frameworks, grounded semantics, admissibility, and explicitly bounded preferred-extension enumeration.
- ALU-07 quantum logic: `EXECUTABLE_BOUNDED_CANDIDATE_REBOUND` for the current classical finite-dimensional numerical reference checker over its explicitly enumerated operator surfaces.
- ALU-06 dependent type: `SPECIFICATION_ONLY`.
- ALU-08 categorical/topos: `SPECIFICATION_ONLY`.

ALU-02 does not establish full FOL theorem proving, quantifier inference, model finding, or higher-order unification.

ALU-03 does not establish infinite-trace LTL model checking, CTL/CTL*, timed automata, future prediction, or temporal causality.

ALU-04 does not establish common knowledge, dynamic epistemic logic, probabilistic epistemic logic, first-order modality, or infinite-model completeness.

ALU-05 does not establish every non-monotonic formalism or unbounded preferred-extension enumeration.

ALU-07 does not establish quantum-hardware execution, quantum advantage, physical state preparation, or universal quantum-logic completion.

### 2.5 Source identity hardening

Executable evidence is bound to exact implementation identity wherever a stable standalone checker exists.

- ALU-02 is bound to an exact checker SHA-256.
- ALU-04 and ALU-05 are bound to exact checker SHA-256 values and their tests recompute those hashes.
- ALU-03 and ALU-07 originate in a large evolving source surface, so the registry binds exact source revision identity plus callable-AST identity rather than trusting a stale monolithic-file hash.

Changing a hash-bound checker invalidates its old receipt and requires an explicit rebind; code repair without provenance repair is not accepted as complete.

### 2.6 External algorithm ingress

External algorithms are admitted as typed capability metadata, never as an interchangeable universal solver pool.

Current registry includes:

- BFS;
- Dijkstra;
- Bellman-Ford;
- Floyd-Warshall;
- Johnson;
- maximum-weight matching;
- connectivity/flow methods;
- CP-SAT;
- SMT;
- SciPy numerical optimization.

Algorithm selection requires an explicit problem family and mathematical preconditions. Solver status is preserved; `UNKNOWN` is never converted into success.

## 3. Explicit non-claims

This runtime does not claim:

- `URK == ULK == ULMK == Core19 == executable AST`;
- `Distinction == NonExistence`;
- paradox or dual logic is universally classical contradiction;
- adjacency/order/correlation/prediction/reachability establishes causation;
- every 19 x 19 coordinate has semantics;
- `1E∞` is a standard tensor dimension;
- all eight canonical ULK fragments are executable;
- finite term unification is complete FOL proof search;
- finite-trace evaluation is full temporal-model-checking closure;
- finite Kripke evaluation is complete epistemic-logic closure;
- Dung grounded/preferred evaluation covers all non-monotonic reasoning;
- numerical ALU-07 checking is quantum hardware;
- internet algorithm availability licenses execution outside assumptions;
- AMOS repository mutation changes the host model's neural weights.

## 4. Verification evidence

Bounded execution evidence on 2026-09-14 includes the previously recorded Core-19, SAT, Cognitive Matrix, relation-algebra, ALU-02/03/07, and tensor/topology tests plus the current-main reconciliation checks below.

Current-main reconciliation locally reconstructed and executed:

- 38 focused functional tests PASS across Core-19, six-axis tensor storage, finite topology, finite Kripke modal semantics, and Dung argumentation.
- The Core-19 suite retains 50,000 seeded unary rewrite probes with no observed idempotence/double-NLOGIC failures.
- ALU-04 exact checker SHA-256 after fail-closed repair:
  `869d095013dabdfdce089e1f4065350417b5e77722c26738d6beded0ec87eac0`.
- ALU-05 exact checker SHA-256 after fail-closed repair:
  `8e613729ca3a0ef9d24a8bafba432ab9b358fe3c2b4a8ac945ee7b1660ed658c`.
- ALU-04 now rejects malformed formula objects and undeclared agents instead of silently allowing an empty accessibility relation.
- ALU-05 now rejects unknown argument-set members and invalid enumeration bounds.

The AMOS math-audit harness continues to surface its known corpus-level T2 probability-labeling counterexample. That finding remains visible and is not attributed to the new runtime modules.

No full-repository CI receipt is asserted by this text. Focused local bounded execution is not universal proof, production deployment, or Canon promotion.

## 5. Source/canon boundary

Active lineage:

- AMOS_CORE baseline: `v4.4`.
- Canonical ULK artifact: `v2.1.0`.
- URK mathematical substrate repair: candidate/model, not Canon by freshness.
- ALU-02/03/04/05/07 runtime projections: bounded implementation evidence, not Canon promotion.

`_00_AMOS_CANON_` is treated as a governed ingress/legacy route into candidate admission, not as an automatic payload authority. Candidate material must pass source identity, semantic/type/equation/tensor/topology/scope/provenance/authority/replay gates before it can become promotion-eligible; eligibility is still not promotion.

See `01_CANON/07_PROVENANCE/URK_CORE19_REPAIR_CANDIDATE_2026-09-14.md` for source identity and candidate lineage.

## 6. Remaining gaps

- Full FOL theorem-prover binding: `NOT_ESTABLISHED`.
- ALU-06 dependent-type executable binding: `NOT_ESTABLISHED`.
- ALU-08 categorical/topos executable binding: `NOT_ESTABLISHED`.
- Formal compilation of the current Lean-style URK candidate: `NOT_ESTABLISHED` in this runtime branch.
- Candidate formal defects still requiring source-side repair include ill-typed cross-type P02 inequality, a definition-order dependency around `implementationStatus`, and remaining trivial/one-way topology invariants.
- Remaining legacy v0 brain/agent semantic-owner migration: `PARTIAL`.
- System-wide automated enforcement and executable closure: `NOT_ESTABLISHED`.

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
- IMPLEMENTS_BOUNDED: `finite_topology_runtime.py`
- IMPLEMENTS_BOUNDED: `urk_relation_algebra.py`
- IMPLEMENTS_BOUNDED: `amos_ulk_alu02_unification_reference_checker_v1.py`
- IMPLEMENTS_BOUNDED: `amos_ulk_alu03_finite_trace_ltl_checker_v1.py`
- IMPLEMENTS_BOUNDED: `amos_ulk_alu04_finite_kripke_checker_v1.py`
- IMPLEMENTS_BOUNDED: `amos_ulk_alu05_dung_checker_v1.py`
- IMPLEMENTS_BOUNDED: `amos_ulk_alu07_reference_checker_current.py`
- IMPLEMENTS_BOUNDED: `cognitive_matrix_runtime.py`
- BINDS_EXECUTION_STATUS: `ulk_fragment_execution_registry.py`
- BINDS_ALGORITHM_PRECONDITIONS: `internet_algorithm_registry.py`
- VERIFIED_BY_BOUNDED: `test_core19_runtime.py`
- VERIFIED_BY_BOUNDED: `test_classical_sat_firewall.py`
- VERIFIED_BY_BOUNDED: `test_core19_tensor_topology.py`
- VERIFIED_BY_BOUNDED: `test_finite_topology_runtime.py`
- VERIFIED_BY_BOUNDED: `test_cognitive_matrix_runtime.py`
- VERIFIED_BY_BOUNDED: `test_urk_math_alu02_algorithms.py`
- VERIFIED_BY_BOUNDED: `test_alu03_alu07_rebind.py`
- VERIFIED_BY_BOUNDED: `test_ulk_alu04_alu05.py`
