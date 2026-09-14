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

The AMOS OS runtime reference plane contains executable bounded Core-19, URK finite-relation mathematics, Cognitive Matrix, and selected ULK fragment components in addition to architecture documentation.

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

The executable artifacts do **not** establish system-wide AMOS executable closure and do **not** promote the 2026-09-14 repair material to Canon.

## 1. Runtime pipeline

```text
Perceive -> Route -> Admit -> Plan -> Schedule -> Execute -> Observe -> Repair -> Audit -> Finalize
```

## 2. Executable bounded reasoning substrate

### 2.1 Files

- `core19_runtime.py` — executable bounded URK/Core-19 repair runtime snapshot.
- `test_core19_runtime.py` — deterministic/property/adversarial Core-19 regression tests.
- `classical_sat_firewall.py` — exact bounded propositional satisfiability firewall.
- `test_classical_sat_firewall.py` — pairwise-vs-global consistency counterexample and bound tests.
- `core19_tensor_topology.py` — typed sparse Core-19 tensor and topology stores.
- `test_core19_tensor_topology.py` — tensor-axis, coordinate, and topology invariant tests.
- `urk_relation_algebra.py` — finite relation encoding, Boolean-semiring composition, and reflexive-transitive closure for URK-E1..E3.
- `amos_ulk_alu02_unification_reference_checker_v1.py` — bounded first-order term unification with occurs-check.
- `ulk_fragment_execution_registry.py` — evidence-bound current implementation status for the eight canonical ULK fragment namespaces.
- `internet_algorithm_registry.py` — typed external-algorithm capability ingress with applicability preconditions.
- `cognitive_matrix_runtime.py` — bounded executable Cognitive Matrix state, dependency, coverage, gap and routing substrate.
- `test_cognitive_matrix_runtime.py` — Cognitive Matrix invariant/regression tests.
- `test_urk_math_alu02_algorithms.py` — consolidated URK-E1..E3, ALU-02, and algorithm-ingress regression/adversarial tests.

### 2.2 Core-19 behavior

- Exact 19-position Core-19 semantic coordinate registry.
- P02 is `COMPETING` across source lineages and requires explicit namespace/version binding.
- Four-valued evidence state `Truth4 = (supports_true, supports_false)` with involutive negation, explicit information partial order, and information-order join.
- No implicit Python total ordering is exposed for `Truth4`; lexicographic ordering is not substituted for the intended information order.
- Corrected unary rewrite precedence: `NLOGIC(NLOGIC(x))` is reduced before recursive child normalization.
- Normalizer idempotence checks for the bounded `ATOM | NOT | NLOGIC` fragment.
- Exact bounded Boolean satisfiability for `ATOM | NOT | AND | OR | IMPLIES | BOTTOM` with a declared atom bound.
- Pairwise compatibility is explicitly separated from global consistency.
- 19 x 19 is treated as 361 pair coordinates, not 361 proven equations.
- Tensor coordinates require explicit row, column, scale, context, and regime axes.
- Topology edges remain typed relations and are not automatically causal edges.

### 2.3 URK finite mathematical layer

The fresh `_00_AMOS_CANON` URK mathematical-substrate candidate is projected only where the mathematics is independently executable and bounded.

Implemented finite mathematics:

```text
URK-E1
Enc(R)[i,j] = 1 iff (k_i,k_j) is in R
```

for a finite ordered namespace and binary relation, with executable encode/decode round-trip checks.

```text
URK-E2
(A_R odot A_S)[x,z]
  = OR_y (A_R[x,y] AND A_S[y,z])
```

using Boolean-semiring composition. This represents relation composition and is not ordinary path-count matrix multiplication.

`URK-E3` is implemented as finite reflexive-transitive closure to a fixed point, with containment, reflexivity, transitivity, and idempotence checks.

Hard firewall:

```text
GRAPH_REACHABILITY != LOGICAL_ENTAILMENT
GRAPH_REACHABILITY != CAUSATION
```

### 2.4 ULK execution bindings

Current implementation status must be read from `ulk_fragment_execution_registry.py`; the earlier fragment-status function inside `core19_runtime.py` is the original repair-snapshot view and is not the current evidence registry after later source ingestion.

Current bounded state:

- ALU-01 classical propositional: `EXECUTABLE_BOUNDED`.
- ALU-02 first-order/unification: `EXECUTABLE_BOUNDED_CANDIDATE_REBOUND` for **finite first-order term unification only**, including occurs-check.
- ALU-07 quantum logic: `CANONICAL_BOUNDED_CLAIM_REBIND_PENDING` on this repository surface.
- ALU-03 temporal/LTL: `SPECIFICATION_ONLY`.
- ALU-04 epistemic/modal: `SPECIFICATION_ONLY`.
- ALU-05 non-monotonic/Dung: `SPECIFICATION_ONLY`.
- ALU-06 dependent type: `SPECIFICATION_ONLY`.
- ALU-08 categorical/topos: `SPECIFICATION_ONLY`.

ALU-02 explicitly does **not** claim full first-order theorem proving, quantifier inference, model finding, higher-order unification, canon promotion, or effect authority.

### 2.5 External algorithm ingress

Internet-derived algorithm knowledge is admitted as typed capability metadata, not as an undifferentiated algorithm pool.

Current registry includes bounded routing metadata for:

- BFS;
- Dijkstra;
- Bellman-Ford;
- Floyd-Warshall;
- Johnson;
- maximum-weight matching;
- flow/connectivity methods;
- CP-SAT;
- SMT;
- SciPy numerical optimization.

Every algorithm requires explicit problem-family and mathematical preconditions. A solver result preserves its native status and scope; `UNKNOWN` is never silently converted into success.

## 3. Explicit non-claims

This implementation does not claim:

- that URK, ULK, ULMK, Core-19 semantics, and executable ASTs are the same namespace;
- that `Distinction` and `NonExistence` are equivalent;
- that paradox or dual logic is universally classical contradiction;
- that adjacency, topology, temporal order, correlation, prediction, or reachability establishes causation;
- that every 19 x 19 coordinate has semantics;
- that `1E∞` is a valid standard mathematical tensor dimension;
- that all eight canonical ULK logic fragments are executable;
- that bounded term unification is a complete FOL prover;
- that internet algorithm availability licenses use outside stated assumptions;
- that the host model's neural weights are self-modified by AMOS learning.

## 4. Verification evidence

Executed local bounded verification on 2026-09-14 includes:

- Core-19 runtime suite: 13 tests PASS, 0 FAIL.
- Classical SAT firewall suite: 2 tests PASS, 0 FAIL.
- Cognitive Matrix runtime suite: 16 tests PASS, 0 FAIL.
- Core-19 tensor/topology suite: 8 tests PASS, 0 FAIL.
- Consolidated URK-E1..E3 / ALU-02 / algorithm-ingress suite: 12 tests PASS, 0 FAIL.
- ALU-02 checker SHA-256 rebound to `002a4c72adf0afaa7ad1b33792008ea6a525ca43b69ae4eff301c1b06a135275`.
- ALU-02 source receipt cases reproduced and extended with 3,000 seeded symmetry/idempotence fuzz pairs.
- URK finite relation composition cross-checked against set-theoretic composition over randomized finite relations.
- URK reflexive-transitive closure randomized over finite graphs with containment, reflexivity, transitivity, and idempotence checks.
- 50,000 seeded randomized unary rewrite trees with zero observed idempotence or double-NLOGIC involution failures in the earlier Core-19 repair pass.
- Pairwise-compatible/global-inconsistent counterexample reproduced with `A`, `B`, and `NOT(A AND B)`.
- SAT atom-limit boundary test fails closed.
- Promotion-gate negative tests.

The AMOS math-audit harness continues to surface its known global T2 probability counterexample. That pre-existing audit failure is not attributed to these new URK-E1..E3 or ALU-02 modules and remains visible rather than being suppressed.

No GitHub Actions workflow receipt is asserted by this file. Local bounded execution is not equivalent to universal proof, production deployment, or Canon promotion.

## 5. Source/canon boundary

The 2026-09-14 `_00_AMOS_CANON` `Reasoning kernel.txt`, `LOGIC.txt`, URK mathematical-substrate candidate, and ALU-02 executable profile are candidate/source inputs. Their semantics may drive runtime projection only where admissibility, typing, contradiction handling, dependency checks, and executable/formal evidence succeed.

The active lineage remains:

- AMOS_CORE baseline: `v4.4`.
- Canonical ULK artifact: `v2.1.0`.
- URK mathematical substrate v1.1: candidate/model, not Canon by freshness.
- ALU-02 executable profile: bounded candidate implementation evidence, not Canon promotion.

## 6. Remaining gaps

- Full FOL theorem-prover binding: `NOT_ESTABLISHED`.
- Temporal/LTL executable binding: `NOT_ESTABLISHED`.
- Epistemic/modal executable binding: `NOT_ESTABLISHED`.
- Non-monotonic/Dung executable binding: `NOT_ESTABLISHED`.
- Dependent-type executable binding: `NOT_ESTABLISHED`.
- Quantum checker/receipt exact repository rebind: `PENDING`.
- Categorical/topos executable binding: `NOT_ESTABLISHED`.
- System-wide automated enforcement and executable closure: `NOT_ESTABLISHED`.
- Remaining legacy v0 brain/agent semantic-owner migration: `PARTIAL`.

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
- [[00_ROOT/00_HOME|00_HOME]]
- [[00_ROOT/AMOS_RSCF_NODES|AMOS_RSCF_NODES]]

RSCF-NODE

node_id: amos_04_runtime_reference_core19_repair
node_type: RUNTIME_REFERENCE
path: 04_RUNTIME/01_REFERENCE_IMPLEMENTATION/README.md
claim_class: AMOS_MODEL
rscf_state: DERIVED
canonical_status: CONDITIONAL

RSCF-RELATIONS:
- INDEXED_BY: [[00_ROOT/00_HOME|00_HOME]]
- INDEXED_BY: [[00_ROOT/AMOS_RSCF_NODES|AMOS_RSCF_NODES]]
- GOVERNED_BY: [[01_CANON/01_CORE_LAWS/LAW_HIERARCHY|LAW_HIERARCHY]]
- IMPLEMENTS_BOUNDED: `core19_runtime.py`
- IMPLEMENTS_BOUNDED: `classical_sat_firewall.py`
- IMPLEMENTS_BOUNDED: `core19_tensor_topology.py`
- IMPLEMENTS_BOUNDED: `urk_relation_algebra.py`
- IMPLEMENTS_BOUNDED: `amos_ulk_alu02_unification_reference_checker_v1.py`
- IMPLEMENTS_BOUNDED: `cognitive_matrix_runtime.py`
- BINDS_EXECUTION_STATUS: `ulk_fragment_execution_registry.py`
- BINDS_ALGORITHM_PRECONDITIONS: `internet_algorithm_registry.py`
- VERIFIED_BY_BOUNDED: `test_core19_runtime.py`
- VERIFIED_BY_BOUNDED: `test_classical_sat_firewall.py`
- VERIFIED_BY_BOUNDED: `test_core19_tensor_topology.py`
- VERIFIED_BY_BOUNDED: `test_cognitive_matrix_runtime.py`
- VERIFIED_BY_BOUNDED: `test_urk_math_alu02_algorithms.py`
