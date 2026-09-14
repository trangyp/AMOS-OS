---
canon-group: meta
canon-type: framework
rscf-state: source-claim
rscf-claim: verified
rscf-provenance: AMOS_corpus
conclusion_class: AMOS_MODEL
epistemic_class: SOURCE_CLAIM
topic: Cognitive Matrix Primitives Contract
tags:
  - canon-group/tech-ai
  - rscf/claim
  - rscf/provenance
  - rscf/state/source-claim
  - misc
created: 2026-08-22
updated: 2026-09-14
---

# COGNITIVE MATRIX PRIMITIVES CONTRACT

## 0. Status

Cognitive Matrix contract for primitives `L00`–`L29`.

- Canonical class: `AMOS_MODEL / CONDITIONAL`.
- Generic primitive contract runtime: `IMPLEMENTED / VALIDATED_BOUNDED`.
- Per-primitive domain-semantic execution: `PARTIAL / UNKNOWN-GAP where not separately bound`.
- Production/deployment validity: `NOT ESTABLISHED`.

Origin architect / steward: **Trang Phan**.

## 1. Scope

The primitive plane contains exactly 30 declared identities from `L00_REALITY_ENVIRONMENT` through `L29_EVOLUTION`.

The generic contract runtime governs primitive identity, typed artifact admission, provenance, state-version identity, scope, regime, epistemic preservation, explicit dependency binding, and the non-authority boundary.

It does **not** infer that numbering defines causality, temporal order, control flow, or dependency.

## 2. Hard firewalls

```text
PRIMITIVE_ID != IMPLEMENTATION
PRIMITIVE_ORDER != DEPENDENCY
CAPABILITY != AUTHORITY
ACTION_PRIMITIVE != EFFECT_AUTHORITY
OBSERVATION != CURRENT_STATE
REPRESENTATION != REALITY
MODEL != VERIFIED
UNKNOWN/GAP != PASS
DOCUMENTED != EXECUTABLE
GENERIC_CONTRACT_EXECUTABLE != ALL_PRIMITIVE_SEMANTICS_COMPLETE
```

Every primitive artifact must carry:

- primitive identity;
- artifact identity and type;
- epistemic class;
- state version;
- scope;
- regime;
- provenance.

No generic primitive operation may upgrade epistemic class or mint effect authority.

## 3. Dependency semantics

Dependencies are explicit typed edges only.

The runtime does **not** generate edges from lexical or numeric order. `L00`, `L01`, ..., `L29` are identifiers, not a proof of a chain.

Where dependencies are admitted, they use the Cognitive Matrix dependency graph and retain edge type. Dependency reachability may support stale/impact propagation under separately satisfied invalidation gates; it does not establish causality, logical entailment, or falsity.

## 4. Executed reference

Repository-bound reference implementation:

- `04_RUNTIME/01_REFERENCE_IMPLEMENTATION/primitive_contract_runtime.py`
- `04_RUNTIME/01_REFERENCE_IMPLEMENTATION/test_primitive_contract_runtime.py`

Executed CI evidence on 2026-09-14:

- exact 30-primitive registry;
- malformed identity/scope/regime/version/provenance rejection;
- epistemic-class preservation;
- `L18_ACTION` cannot mint effect authority;
- numeric primitive order creates no dependency edges;
- only explicit typed dependencies are admitted;
- primitive self-dependency fails closed;
- complete reference-runtime unittest discovery passed for commit `6e3eea239e796e7bcdd2eb2cc7dced10684804e4`.

`TEST_PASS != TRUTH`: this receipt validates the bounded implementation contract only.

## 5. Mathematical typing boundary

Primitive documents frequently use multidimensional record notation. Current URK repair rules apply:

```text
INDEXED_FIELD != ALGEBRAIC_TENSOR
STRUCTURAL_ADJACENCY != POINT_SET_TOPOLOGY
STRUCTURAL_ADJACENCY != CAUSALITY
```

Any primitive artifact claiming algebraic tensor semantics must bind scalar/module structure, multilinearity/tensor-product evidence, and a basis witness when coordinate coefficients are used. Record-like axes alone are not sufficient.

## 6. Remaining gaps

The generic primitive substrate does not establish that all 30 primitive-specific semantic mechanisms are implemented.

Open work remains per primitive where applicable, including:

- domain-specific state/operator semantics;
- source/canon reconciliation;
- mathematical equation validation;
- empirical/measurement validity;
- cross-primitive dependency evidence;
- authority and commit integration;
- production persistence/concurrency;
- recovery and rollback evidence.

Unresolved items remain `UNKNOWN/GAP`; they are not converted to PASS by registry coverage.

## 7. Promotion gates

A primitive-specific semantic implementation may advance only when its load-bearing requirements are evidenced:

- typed schema and semantic owner resolved;
- source/provenance bound;
- assumptions and mathematical types explicit;
- negative and adversarial cases covered;
- runtime implementation receipt present;
- dependencies and epochs fresh;
- authority witness present where consequential;
- rollback/recovery demonstrated where mutation/effects occur.

Canon promotion remains a separate `K_CANON` decision.

## 8. Falsifiers

This contract must be revised if:

1. authoritative canon changes the primitive identity set;
2. executable tests contradict an invariant declared here;
3. runtime code infers dependency from primitive numbering;
4. any primitive or generic contract mints authority by capability/name alone;
5. an indexed record is promoted to algebraic tensor without the required mathematical structure;
6. generic contract coverage is represented as complete semantic implementation.

## Cross-plane bindings

- Canon: `01_CANON/01_CORE_LAWS/LAW_HIERARCHY`
- Cognitive runtime: `04_RUNTIME/01_REFERENCE_IMPLEMENTATION/cognitive_matrix_runtime.py`
- Primitive runtime: `04_RUNTIME/01_REFERENCE_IMPLEMENTATION/primitive_contract_runtime.py`
- Control-plane gates: `03_CONTROL_PLANE`
- Observability remains evidence, never authority.

RSCF-NODE
node_id: cm_25_cognitive_matrix_01_primitives_cognitive_matrix_primitives_contract
node_type: note
path: 25_COGNITIVE_MATRIX/01_PRIMITIVES/COGNITIVE_MATRIX_PRIMITIVES_CONTRACT.md
claim_class: AMOS_MODEL

**MOC:** [[25_COGNITIVE_MATRIX/01_PRIMITIVES/01_PRIMITIVES_MOC|01_PRIMITIVES_MOC]]

**Trang Framework:** [[11_KNOWLEDGE/TRANG_FRAMEWORK_RECURSIVE_ONTOLOGY_DYNAMICS|TRANG_FRAMEWORK_RECURSIVE_ONTOLOGY_DYNAMICS]]
