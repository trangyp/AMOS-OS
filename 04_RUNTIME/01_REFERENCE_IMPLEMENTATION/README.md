---
canon-group: meta
canon-type: framework
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

## 0. Status

The AMOS OS runtime reference plane now contains executable bounded Core-19 and L09 inference repair components in addition to architecture documentation.

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

## 2. Executable bounded repair surface

### 2.1 Files

- `core19_runtime.py` — executable bounded URK/Core-19 repair runtime.
- `test_core19_runtime.py` — deterministic/property/adversarial regression tests.
- `classical_sat_firewall.py` — exact bounded propositional satisfiability firewall.
- `test_classical_sat_firewall.py` — pairwise-vs-global counterexample and bound tests.
- `inference_runtime.py` — executable bounded L09 inference gate.
- `test_inference_runtime.py` — L09 routing, consistency, P02, causal, confidence, and bound tests.

### 2.2 Implemented bounded behavior

- Exact 19-position Core-19 semantic coordinate registry.
- P02 is `COMPETING` across source lineages and requires explicit namespace/version binding.
- Four-valued evidence state `Truth4 = (supports_true, supports_false)` with involutive negation, explicit information partial order, and information-order join.
- No implicit Python total ordering is exposed for `Truth4`; lexicographic ordering is not substituted for the intended information order.
- Corrected unary rewrite precedence: `NLOGIC(NLOGIC(x))` is reduced before recursive child normalization.
- Normalizer idempotence checks for the bounded `ATOM | NOT | NLOGIC` fragment.
- Exact bounded Boolean satisfiability for `ATOM | NOT | AND | OR | IMPLIES | BOTTOM` with a declared atom bound.
- Pairwise compatibility is explicitly separated from global consistency.
- Bounded classical entailment uses the unsatisfiable-countermodel criterion.
- Inconsistent premise sets remain inspectable and are not promoted into an inference result.
- L09 routes only to locally executable logic fragments and fails closed for specification-only or rebind-pending fragments.
- L09 requires explicit P02 namespace/version binding when P02 is used.
- L09 separates logical inference from causal claims and requires separate causal evidence binding for a causal result.
- L09 carries dependency claim IDs, provenance, scope, regime, source version, consistency state, entailment state, and confidence ceiling/unknown.
- 19 x 19 is treated as 361 pair coordinates, not 361 proven equations.
- Tensor coordinates require explicit row, column, scale, context, and regime axes.
- Topology edges remain typed relations and are not automatically causal edges.
- Logic-fragment implementation status is explicit:
  - classical propositional: `EXECUTABLE_BOUNDED`;
  - quantum logic: `CANONICAL_BOUNDED_CLAIM_REBIND_PENDING`;
  - other canonical ULK fragments: `SPECIFICATION_ONLY` in this repair surface.
- Canon promotion requires every promotion-evidence gate; freshness alone cannot promote a candidate.

### 2.3 Explicit non-claims

This implementation does not claim:

- that ULK, ULMK, Core-19 semantics, and the executable AST are the same namespace;
- that `Distinction` and `NonExistence` are equivalent;
- that paradox or dual logic is universally classical contradiction;
- that adjacency, topology, temporal order, correlation, prediction, or implication establishes causation;
- that every 19 x 19 coordinate has semantics;
- that `1E∞` is a valid standard mathematical tensor dimension;
- that all eight canonical ULK logic fragments are executable;
- that formal entailment is empirical truth;
- that the host model's neural weights are self-modified by AMOS learning.

## 3. Verification evidence

Local reconstruction of the staged executable files on 2026-09-14 passed:

- Core-19 runtime suite: 13 tests PASS, 0 FAIL.
- Classical SAT firewall suite: 2 tests PASS, 0 FAIL.
- L09 inference runtime suite: 10 tests PASS, 0 FAIL.
- Persisted bounded repair total: **25 tests PASS, 0 FAIL** across the three suites.
- 50,000 seeded randomized unary rewrite trees with zero observed idempotence or double-NLOGIC involution failures.
- Full four-state Truth4 negation, information-join, and explicit information-order checks.
- Pairwise-compatible/global-inconsistent counterexample reproduced with `A`, `B`, and `NOT(A AND B)`.
- SAT atom-limit boundary fails closed.
- P02 unresolved/resolved routing checks.
- Unsupported-fragment and quantum-rebind fail-closed checks.
- Causal-evidence boundary check.
- Confidence-ceiling/unknown checks.
- Mathematical audit checks for `19 x 19 = 361`, Truth4 negation involution, information-join least-upper-bound behavior, the pairwise/global counterexample, and bounded entailment.

No GitHub Actions workflow run is currently attached to this branch. These are bounded local reconstruction receipts, not CI receipts.

These results are bounded to the staged repair implementation and test harness. They are not universal AMOS correctness evidence.

## 4. Source/canon boundary

The 2026-09-14 `_00_AMOS_CANON` `Reasoning kernel.txt` and `LOGIC.txt` revisions are treated as **candidate source inputs**. Their repair semantics may drive this runtime projection only where admissibility, typing, contradiction handling, and executable checks succeed.

The active lineage remains:

- AMOS_CORE baseline: `v4.4`.
- Canonical ULK artifact: `v2.1.0`.
- New repair material: `ACTIVE_REPAIR_SPEC / AMOS_MODEL` until separately admitted.

## 5. Remaining gaps

- FOL/unification executable binding: `NOT_ESTABLISHED` here.
- Temporal/LTL executable binding: `NOT_ESTABLISHED` here.
- Epistemic/modal executable binding: `NOT_ESTABLISHED` here.
- Non-monotonic/Dung executable binding: `NOT_ESTABLISHED` here.
- Dependent-type executable binding: `NOT_ESTABLISHED` here.
- Quantum checker/receipt rebind: `PENDING`.
- Categorical/topos executable binding: `NOT_ESTABLISHED` here.
- General abductive ranking/calibration: `NOT_ESTABLISHED` here.
- Domain causal identification: separate engine/evidence required.
- System-wide automated enforcement and executable closure: `NOT_ESTABLISHED`.

## 6. Ingestion rule

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
  uncertainty:
    action:
      - MARK_GAP_OR_COMPETING
      - QUARANTINE_IF_NEEDED
      - NEVER_INVENT_CANON
```

## 7. Cross-references

- [[02_KERNEL/02_KERNEL_MOC|02_KERNEL]]
- [[03_CONTROL_PLANE/03_CONTROL_PLANE_MOC|03_CONTROL_PLANE]]
- [[04_RUNTIME/04_RUNTIME_MOC|04_RUNTIME]]
- [[25_COGNITIVE_MATRIX/01_PRIMITIVES/L09_INFERENCE/L09_INFERENCE_MOC|L09_INFERENCE]]
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
- IMPLEMENTS_BOUNDED: `inference_runtime.py`
- VERIFIED_BY_BOUNDED: `test_core19_runtime.py`
- VERIFIED_BY_BOUNDED: `test_classical_sat_firewall.py`
- VERIFIED_BY_BOUNDED: `test_inference_runtime.py`
