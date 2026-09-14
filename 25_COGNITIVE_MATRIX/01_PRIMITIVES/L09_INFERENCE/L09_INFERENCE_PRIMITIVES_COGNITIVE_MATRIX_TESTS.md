---
canon-group: cognition
canon-type: verification_contract
rscf-state: derived
rscf-provenance: AMOS_corpus_plus_2026_09_14_URK_repair
conclusion_class: VERIFIED_BOUNDED
epistemic_class: EXECUTION_EVIDENCE
topic: L09 Inference Primitives Cognitive Matrix Tests
created: 2026-08-22
updated: 2026-09-14
origin_architect: Trang Phan
amos_core_target: v4.4
canonical_status: CONDITIONAL
---

# L09 — Tests and Validators

**Package:** `L09_INFERENCE`  
**Origin architect / steward:** **Trang Phan**

## 1. Bound executable surface

Current L09 verification binds to:

- `04_RUNTIME/01_REFERENCE_IMPLEMENTATION/core19_runtime.py`
- `04_RUNTIME/01_REFERENCE_IMPLEMENTATION/classical_sat_firewall.py`
- `04_RUNTIME/01_REFERENCE_IMPLEMENTATION/inference_runtime.py`
- `04_RUNTIME/01_REFERENCE_IMPLEMENTATION/test_inference_runtime.py`

## 2. Executed L09 regression suite

Execution date: `2026-09-14`  
Execution class: `LOCAL_RECONSTRUCTED_BRANCH_ARTIFACT`  
Result: **10 passed / 0 failed**  
Runtime: Python + pytest  
Scope: bounded reference implementation only.

### Executed cases

1. `T-L09-001 / MODUS_PONENS`  
   `A`, `A -> B` entails `B` -> `VERIFIED_BOUNDED`.

2. `T-L09-002 / COUNTERMODEL`  
   `A` does not entail independent `B` -> `NOT_ENTAILED`.

3. `T-L09-003 / GLOBAL_CONSISTENCY`  
   `{A, B, NOT(A AND B)}` is pairwise satisfiable but globally inconsistent -> `INCONSISTENT_INPUT`.

4. `T-L09-004 / SPEC_ONLY_FRAGMENT`  
   Temporal/LTL execution request fails closed -> `UNKNOWN/GAP`.

5. `T-L09-005 / QUANTUM_REBIND`  
   Quantum execution request reports local checker/receipt rebind pending -> `UNKNOWN/GAP`.

6. `T-L09-006 / P02_UNRESOLVED`  
   P02-dependent inference without namespace/version binding -> `COMPETING`.

7. `T-L09-007 / P02_RESOLVED_LOCAL`  
   Explicit recovered-living-map/version binding permits local bounded inference.

8. `T-L09-008 / CAUSAL_FIREWALL`  
   Causal claim without separately bound causal evidence/model -> `UNKNOWN/GAP`.

9. `T-L09-009 / UNKNOWN_CONFIDENCE`  
   Missing premise confidence leaves derived confidence ceiling unknown.

10. `T-L09-010 / SAT_BOUND`  
    Atom-budget overflow fails closed -> `UNKNOWN/GAP`.

## 3. Verification properties

The suite directly checks these contract properties:

```text
FRAGMENT_CAPABILITY_BEFORE_EXECUTION
P02_NAMESPACE_BINDING_BEFORE_USE
GLOBAL_CONSISTENCY_BEFORE_ENTAILMENT
COUNTERMODEL_PRESERVATION
CAUSAL_EVIDENCE_SEPARATION
PROVENANCE/DEPENDENCY_CARRY
CONFIDENCE_CEILING_OR_UNKNOWN
BOUNDED_RESOURCE_FAIL_CLOSED
```

## 4. Related Core-19 repair evidence

The sibling bounded repair suites test:

- double-NLOGIC precedence;
- normalization idempotence;
- double-NLOGIC involution;
- four-valued negation/information behavior;
- 19 x 19 coordinate count;
- promotion gates;
- pairwise-vs-global satisfiability counterexample.

Those tests support L09 dependencies but do not turn unimplemented ULK fragments into executable engines.

## 5. Tests still required

Before stronger promotion, add or bind:

- property generation over full supported Boolean syntax;
- minimized counterexamples for every inference-status transition;
- source-version stale/revalidation tests;
- provenance loss/mutation tests;
- P02 conflicting-binding tests across multiple source namespaces;
- adversarial malformed-formula tests;
- exact checker receipt for quantum ALU-07 if recovered;
- separate executable validators for any newly implemented ULK fragment;
- integration tests between L09 and RSCF state/freshness infrastructure;
- CI execution bound to the exact branch/artifact digest.

## 6. Evidence ceiling

```text
10/10 LOCAL TESTS
!= GITHUB CI RECEIPT
!= ALL-FRAGMENT LOGIC PROOF
!= CANON PROMOTION
!= EMPIRICAL TRUTH
```

No GitHub Actions receipt is currently attached to this L09 test update.

## 7. Reproduction command

Within the reference implementation directory:

```text
python -m py_compile core19_runtime.py classical_sat_firewall.py inference_runtime.py test_inference_runtime.py
pytest -q test_inference_runtime.py
```

## 8. RSCF node

```text
node_id: l09_primitives_tests
node_type: verification_contract
claim_class: VERIFIED_BOUNDED
rscf_state: DERIVED_FROM_EXECUTION
canonical_status: CONDITIONAL
```

**MOC:** [[25_COGNITIVE_MATRIX/01_PRIMITIVES/L09_INFERENCE/L09_INFERENCE_MOC|L09_INFERENCE_MOC]]
