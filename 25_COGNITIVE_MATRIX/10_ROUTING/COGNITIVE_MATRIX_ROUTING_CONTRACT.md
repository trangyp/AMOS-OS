---
canon-group: meta
canon-type: framework
rscf-state: source-claim
rscf-claim: verified
rscf-provenance: AMOS_corpus
conclusion_class: AMOS_MODEL
epistemic_class: SOURCE_CLAIM
topic: Cognitive Matrix Routing Contract
tags:
  - canon-group/tech-ai
  - rscf/claim
  - rscf/provenance
  - rscf/state/source-claim
  - misc
created: 2026-08-22
---
---
---

# COGNITIVE MATRIX ROUTING CONTRACT

## 0. Status

Cognitive Matrix-plane contract for **ROUTING CONTRACT**. AMOS_MODEL; canonical status CONDITIONAL; implementation BOUNDED_PARTIAL. Bounded executors exist for gap routing and typed algorithm-capability routing. Routing selects a capability only; it cannot mint canon, execution, commit, or effect authority.

## 1. Scope

Governs primitives L00–L29, lifecycle operations O00–O16, control planes C01–C09, scales, cell registry, algorithm ingress, routing, validation, and generators as they bear on `ROUTING CONTRACT`. Conclusions inherit the weakest load-bearing premise.

## 2. Contract terms

- **Problem family is explicit** — algorithms are selected only within a declared family.
- **Preconditions are explicit** — a candidate is ineligible when any declared mathematical precondition is missing.
- **Finite/infinite temporal semantics are separate** — finite-trace ALU03 execution may not satisfy an ordinary infinite-word LTL request.
- **Local/external capability is separate** — an external-only registry entry is metadata until a runtime/tool binding is independently established.
- **Guarantee class is preserved** — EXACT, EXACT_IF_PRECONDITIONS, SOLVER_STATUS_BOUND, and HEURISTIC are not interchangeable.
- **No-match fails closed** — `NO_MATCH -> UNKNOWN/GAP`; the router may not guess a fallback.
- **Capability ≠ authority** — routing never authorizes an effect.

## 3. Invariants

- `ELIGIBLE != CORRECT_FOR_UNSTATED_OBJECTIVE`.
- `ROUTED != EXECUTED`.
- `EXECUTED != VERIFIED_OUTSIDE_CONTRACT`.
- `CAPABILITY != AUTHORITY`.
- `REACHABLE != ENTAILS != CAUSES`.
- Same algorithm name across libraries does not establish identical semantics or guarantees.
- External solver status is preserved; `UNKNOWN` is not converted to success.
- When `local_only=true`, external capability metadata is rejected rather than treated as executable.

## 4. Executed reference

Bounded executor and regression owners:

- `04_RUNTIME/01_REFERENCE_IMPLEMENTATION/cognitive_matrix_runtime.py` — typed gap routing; route never grants authority.
- `04_RUNTIME/01_REFERENCE_IMPLEMENTATION/internet_algorithm_registry.py` — provenance-bound algorithm capability registry and mathematical preconditions.
- `04_RUNTIME/01_REFERENCE_IMPLEMENTATION/foundational_algorithm_runtime.py` — bounded local deterministic reference algorithms.
- `04_RUNTIME/01_REFERENCE_IMPLEMENTATION/algorithm_routing_runtime.py` — deterministic routing over the canonical algorithm-ingress registry.
- `04_RUNTIME/01_REFERENCE_IMPLEMENTATION/test_cognitive_matrix_runtime.py`
- `04_RUNTIME/01_REFERENCE_IMPLEMENTATION/test_internet_algorithm_registry.py`
- `04_RUNTIME/01_REFERENCE_IMPLEMENTATION/test_foundational_algorithm_runtime.py`
- `04_RUNTIME/01_REFERENCE_IMPLEMENTATION/test_algorithm_routing_runtime.py`

The 01–12 execution registry previously passed GitHub Actions run `34851961830` at commit `fdeeb0eaa501d124847e0ad9b0e244409cfd4311`. New algorithm-routing changes require their own current regression result before being promoted to tested state.

## 5. Gaps

OPEN: complete algorithm-family coverage; benchmark-aware cost/latency routing; hardware/runtime availability; solver installation and version binding for external capabilities; domain-specific objective functions; empirical solver-quality calibration; authority/effect integration; proof that the registry is exhaustive. “All algorithms on the internet” is not a finite or stable set and is represented as progressive provenance-bound ingress, not as a completion claim.

## 6. Falsifiers

F1: canonical source defines different semantics. F2: a route is produced despite a missing declared precondition. F3: an external-only capability is represented as locally executable. F4: finite-trace and infinite-word temporal semantics are silently exchanged. F5: solver UNKNOWN is promoted to success. F6: routing grants effect/canon authority.

## Worked semantics

Given a routing request:

1. **Declare family** — shortest path, SAT, SMT, equality reasoning, term rewriting, constraint propagation, temporal model checking, etc.
1. **Declare preconditions** — domain, finiteness, weight/capacity assumptions, theory support, trace semantics, rewrite validity, or other load-bearing assumptions.
1. **Apply guarantee policy** — if exactness is required, reject heuristic/solver-status-only candidates unless policy explicitly allows them.
1. **Apply locality policy** — if local execution is required, reject metadata-only external candidates.
1. **Rank eligible candidates** deterministically under the declared routing policy.
1. **Return route or UNKNOWN/GAP** — never invent an algorithm or missing binding.
1. **Execute separately** — actual execution still requires an implementation/tool binding and any required authority gate.

## Promotion-gate checklist

- [x] typed problem-family registry exists
- [x] explicit precondition checking exists
- [x] guarantee classes remain distinct
- [x] finite/infinite temporal semantics are separated
- [x] local vs external capability is separated
- [x] no-match returns UNKNOWN/GAP
- [x] routing cannot grant authority
- [ ] complete live runtime/tool availability registry exists
- [ ] benchmark/resource-aware routing validated
- [ ] external solver versions and installation identities bound
- [ ] domain objective correctness independently validated

## Cross-plane bindings

- Governed by canon — [[01_CANON/01_CORE_LAWS/LAW_HIERARCHY|AMOS Core Laws]] · [[01_CANON/01_CORE_LAWS/LAW_HIERARCHY|LAW_HIERARCHY]]
- Kernel interaction — [[02_KERNEL/KERNEL_README|KERNEL_README]]
- Control-plane gates — [[03_CONTROL_PLANE/CONTROL_PLANE_README|CONTROL_PLANE_README]]
- Observed by — [[17_OBSERVABILITY/OBSERVABILITY_README|OBSERVABILITY_README]] · never treated as authority
- Recovered via operations — [[20_OPERATIONS/OPERATIONS_README|OPERATIONS_README]]

______________________________________________________________________

[[00_ROOT/00_ROOT_MOC|00_ROOT_MOC]] · [[00_ROOT/AMOS MOC|AMOS MOC]]

______________________________________________________________________

**Related:** [[25_COGNITIVE_MATRIX/00_INDEX/COGNITIVE_MATRIX_MOC|COGNITIVE_MATRIX_MOC]] · [[00_ROOT/00_HOME|00_HOME]]

______________________________________________________________________

RSCF-NODE
node_id: cm_25_cognitive_matrix_10_routing_cognitive_matrix_routing_contract
node_type: note
path: 25_COGNITIVE_MATRIX/10_ROUTING/COGNITIVE_MATRIX_ROUTING_CONTRACT.md
claim_class: AMOS_MODEL

______________________________________________________________________

**MOC:** [[25_COGNITIVE_MATRIX/10_ROUTING/10_ROUTING_MOC|10_ROUTING_MOC]]

______________________________________________________________________

**Trang Framework:** [[11_KNOWLEDGE/TRANG_FRAMEWORK_RECURSIVE_ONTOLOGY_DYNAMICS|TRANG_FRAMEWORK_RECURSIVE_ONTOLOGY_DYNAMICS]]
