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

The AMOS OS runtime reference plane now contains an executable bounded Core-19 repair implementation in addition to architecture documentation.

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

The new executable artifact does **not** establish system-wide AMOS executable closure and does **not** promote the 2026-09-14 repair material to Canon.

## 1. Runtime pipeline

```text
Perceive -> Route -> Admit -> Plan -> Schedule -> Execute -> Observe -> Repair -> Audit -> Finalize
```

## 2. Executable bounded Core-19 repair

### 2.1 Files

- `core19_runtime.py` — executable bounded URK/Core-19 repair runtime.
- `test_core19_runtime.py` — deterministic and adversarial regression tests.

### 2.2 Implemented bounded behavior

- Exact 19-position Core-19 semantic coordinate registry.
- P02 is `COMPETING` across source lineages and requires explicit namespace/version binding.
- Four-valued evidence state `Truth4 = (supports_true, supports_false)` with involutive negation and information-order join.
- Corrected unary rewrite precedence: `NLOGIC(NLOGIC(x))` is reduced before recursive child normalization.
- Normalizer idempotence checks for the bounded `ATOM | NOT | NLOGIC` fragment.
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
- that adjacency, topology, temporal order, correlation, or prediction establishes causation;
- that every 19 x 19 coordinate has semantics;
- that `1E∞` is a valid standard mathematical tensor dimension;
- that all eight canonical ULK logic fragments are executable;
- that the host model's neural weights are self-modified by AMOS learning.

## 3. Verification evidence

Local reconstruction of the exact staged files on 2026-09-14 passed:

- Python bytecode compilation.
- 12 unit/property tests.
- 50,000 seeded randomized unary rewrite trees with zero observed idempotence or double-NLOGIC involution failures.
- Full four-state Truth4 negation and join-law checks used by the test suite.
- Promotion-gate negative tests.
- AMOS math-audit scan of 110 equation-like records with zero hard failures attributable to the changed files.

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
- VERIFIED_BY_BOUNDED: `test_core19_runtime.py`
