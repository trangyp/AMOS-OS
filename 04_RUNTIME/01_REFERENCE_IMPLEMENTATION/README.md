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

The reference plane now contains bounded executable repairs for:

1. URK/Core-19 typed state and rewrite semantics;
2. bounded classical satisfiability;
3. L09 inference routing and entailment;
4. L10 world-model / reality-contact separation;
5. shared Cognitive Matrix cell state/evidence/binding validation.

```text
PLACEHOLDER != IMPLEMENTED
DOCUMENTED != EXECUTABLE
SOURCE_CLAIM != VERIFIED
MODEL != OBSERVATION
CANON_CANDIDATE != CANONICAL
CAPABILITY != AUTHORITY
UNKNOWN/GAP != PASS
```

These modules are reference implementations. They do not establish system-wide AMOS executable closure.

## Runtime components

### URK / Core-19

- `core19_runtime.py`
- `test_core19_runtime.py`

Implements the 19-coordinate registry, P02 competing-lineage binding, four-valued evidence state, typed matrix/tensor/topology coordinates, fragment implementation status, promotion evidence gates, and repaired `NLOGIC` normalization order.

### Classical satisfiability firewall

- `classical_sat_firewall.py`
- `test_classical_sat_firewall.py`

Implements exact truth-table satisfiability for the declared bounded Boolean grammar and separates pairwise compatibility from global consistency.

### L09 inference

- `inference_runtime.py`
- `test_inference_runtime.py`

Implements fail-closed fragment routing, P02 binding, causal-claim separation, global premise consistency, bounded entailment, provenance/dependency carry, confidence ceiling/unknown, and atom-bound handling.

### L10 world modeling

- `world_model_runtime.py`
- `test_world_model_runtime.py`

Implements representation classes, fidelity envelopes, reality-contact gating, commensurability, exact absolute discrepancy, tolerance classification, conservative provenance/generator ancestry, and tensor-coordinate validation.

### Cognitive Matrix cell contract

- `cognitive_matrix_cell_runtime.py`
- `test_cognitive_matrix_cell_runtime.py`

Implements typed cell axes, epistemic/runtime statuses, evidence roots/freshness/receipts, semantic/runtime/authority owner separation, `UNBOUND != zero`, and safe transform gates.

## Core semantic repairs

### P02

Cross-lineage P02 remains `COMPETING`:

```text
historical lineage -> NonExistence
recovered living-map lineage -> Distinction
```

A namespace/version-local binding may choose one meaning locally. No global winner is inferred.

### Core-19 matrix

```text
19 x 19 = 361 coordinates
```

This is finite counting, not evidence for 361 semantic laws.

### Tensor state

Typed axes are explicit. Current repair surfaces use combinations of:

```text
primitive
field
row/column
scale
context
time
observer
regime
provenance
validation status
consequence
```

Axis order or cardinality is not empirical completeness.

### Logic routing

- Classical propositional: `EXECUTABLE_BOUNDED`.
- Quantum logic: `CANONICAL_BOUNDED_CLAIM_REBIND_PENDING`.
- FOL/unification, temporal/LTL, epistemic/modal, non-monotonic/Dung, dependent type, categorical/topos: `SPECIFICATION_ONLY` in this repair surface.

### Representation/reality boundary

```text
OBSERVED_REALITY
MEASURED_PROXY
MODEL_STATE
SIMULATION
COUNTERFACTUAL
SYNTHETIC_DATA
DIGITAL_TWIN
FORECAST
DEPLOYED_OUTCOME
```

These are separate representation classes. Model consistency never silently upgrades a model into an observation.

## Verification evidence

Local reconstruction on 2026-09-14:

- Core-19 suite: **13 PASS / 0 FAIL**.
- Classical SAT suite: **2 PASS / 0 FAIL**.
- L09 inference suite: **10 PASS / 0 FAIL**.
- L10 world-model suite: **10 PASS / 0 FAIL**.
- Cognitive Matrix shared-cell suite: **12 PASS / 0 FAIL**.
- Combined bounded suites: **47 PASS / 0 FAIL**.
- Seeded unary rewrite stress: **50,000 trees / 0 observed idempotence or double-NLOGIC involution failures**.
- Mathematical checks: `19 x 19 = 361`; four-state negation involution; information-join least-upper-bound behavior; pairwise/global SAT counterexample; bounded entailment countermodel criterion.

No GitHub Actions run is attached to these staged changes. These are local reconstructed branch-artifact receipts, not CI receipts.

```text
47 LOCAL PASS
!= UNIVERSAL AMOS CORRECTNESS
!= ALL-FRAGMENT LOGIC PROOF
!= DEPLOYMENT VALIDATION
!= CANON PROMOTION
```

## Source / canon boundary

The 2026-09-14 `_00_AMOS_CANON` revisions of `Reasoning kernel.txt` and `LOGIC.txt` are treated as candidate source inputs.

Active coordinates remain:

- AMOS_CORE governed baseline: `v4.4`.
- Canonical ULK artifact: `v2.1.0`.
- 2026-09-14 repair material: `ACTIVE_REPAIR_SPEC / AMOS_MODEL` until admitted through canon governance.

Newer timestamp or filename does not create canon authority.

## Effect-authority boundary

The Cognitive Matrix and reasoning runtimes can validate state and produce proposals. They do not authorize durable effects.

Durable/external effects remain subordinate to the AMOS infrastructure/control plane for current intent/policy, observed read sets, semantic transaction lineage, fresh authority, idempotency, release state, receipts/reconciliation, and rollback/finality.

```text
COMPUTE != AUTHORIZE
CELL_VALID != EFFECT_COMMITTABLE
COMMITTABLE != COMMITTED
```

## Remaining high-value gaps

- executable FOL/unification;
- temporal/LTL model checking;
- epistemic/modal engine;
- non-monotonic/Dung engine;
- dependent-type checker;
- quantum checker/receipt rebind;
- categorical/topos execution;
- general abductive ranking/calibration;
- cross-scale world-model transforms with information-loss contracts;
- probabilistic world-state estimation and calibration;
- sensor fusion / digital-twin synchronization;
- Cognitive Matrix coverage and gap registries still largely generated-contract level;
- system-wide CI-bound executable closure.

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
- [[01_CANON/01_CORE_LAWS/LAW_HIERARCHY|LAW_HIERARCHY]]

RSCF-NODE

node_id: amos_04_runtime_reference_core19_repair
node_type: RUNTIME_REFERENCE
path: 04_RUNTIME/01_REFERENCE_IMPLEMENTATION/README.md
claim_class: AMOS_MODEL
rscf_state: DERIVED
canonical_status: CONDITIONAL
