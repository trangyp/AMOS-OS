---
canon-group: meta
canon-type: framework
rscf-state: source-claim
rscf-claim: verified
rscf-provenance: AMOS_corpus
conclusion_class: AMOS_MODEL
epistemic_class: SOURCE_CLAIM
topic: Cognitive Matrix Dependency Graph Contract
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

# COGNITIVE MATRIX DEPENDENCY GRAPH CONTRACT

## 0. Status

Cognitive Matrix-plane contract for **DEPENDENCY GRAPH CONTRACT**. AMOS_MODEL; canonical status CONDITIONAL; bounded reference implementation exists for typed directed dependencies, strongly connected components, DAG ordering, descendant closure, and conditional selective invalidation. Graph structure is not causality unless a separate causal contract establishes that interpretation.

## 1. Scope

Governs primitives L00–L29, lifecycle operations O00–O16, control planes C01–C09, scales, cell registry, routing, validation, generators as they bear on `DEPENDENCY GRAPH CONTRACT`. Bounded by dependency closure: conclusions inherit the weakest load-bearing premise.

## 2. Contract terms

- **Edges are typed** — HARD, EVIDENCE, AUTHORITY, and SOFT edges retain distinct propagation semantics.
- **Direction is explicit** — an edge is `dependency -> dependent`; file order, numeric primitive order, adjacency, similarity, or co-occurrence do not create dependency edges.
- **Cycles are typed findings** — load-bearing cycles block topological ordering; a cycle is not automatically a causal loop.
- **Reachability is structural** — graph reachability does not imply logical entailment or real-world causation.
- **Selective invalidation is conditional** — descendant-only invalidation is licensed only for current, typed, sufficiently complete decision-relevant dependency graphs.

## 3. Invariants

- Self-dependency is rejected.
- An existing edge cannot be silently retagged with a different dependency kind.
- Topological ordering is returned only when the load-bearing subgraph is acyclic.
- SOFT edges do not propagate staleness in the bounded reference model.
- Invalidating a node may mark only demonstrated load-bearing descendants stale; unknown dependency coverage requires conservative quarantine rather than assumed locality.
- `REACHABLE != ENTAILS != CAUSES`.

## 4. Executed reference

Bounded executor and regression owners:

- `04_RUNTIME/01_REFERENCE_IMPLEMENTATION/cognitive_matrix_runtime.py`
- `04_RUNTIME/01_REFERENCE_IMPLEMENTATION/cognitive_matrix_contract_runtime.py`
- `04_RUNTIME/01_REFERENCE_IMPLEMENTATION/test_cognitive_matrix_runtime.py`
- `04_RUNTIME/01_REFERENCE_IMPLEMENTATION/test_cognitive_matrix_contract_runtime.py`
- `04_RUNTIME/01_REFERENCE_IMPLEMENTATION/urk_relation_algebra.py` for finite Boolean reachability closure
- `04_RUNTIME/01_REFERENCE_IMPLEMENTATION/cognitive_matrix_plane_registry.py`
- `04_RUNTIME/01_REFERENCE_IMPLEMENTATION/test_cognitive_matrix_plane_registry.py`

The 01–12 execution registry passed GitHub Actions run `34851961830` at commit `fdeeb0eaa501d124847e0ad9b0e244409cfd4311`. This validates bounded graph behavior only.

## 5. Gaps

OPEN: complete repository-wide dependency extraction; proof that decision-relevant graphs are complete enough for local finality; temporal/versioned edge validity; dynamic dependency updates under concurrent state; causal-edge semantics where required; durable graph persistence; empirical validation of any domain-specific dependency claim.

## 6. Falsifiers

F1: canonical source defines different semantics. F2: an edge is inferred solely from numeric/order adjacency. F3: reachability is promoted to entailment or causality. F4: selective invalidation is used despite unknown load-bearing edges. F5: a load-bearing cycle receives a DAG order.

## Worked semantics

Given a dependency operation:

1. **Declare nodes** by exact identity.
1. **Admit edges** only from explicit evidence/contracts and assign a dependency kind.
1. **Audit SCCs** before assuming a DAG.
1. **Compute topological order** only for acyclic load-bearing structure.
1. **Compute descendants** only over the propagation classes relevant to the operation.
1. **Invalidate narrowly** only when dependency coverage is sufficient for that scope; otherwise quarantine a broader region or return UNKNOWN/GAP.
1. **Never reinterpret** structural graph output as logical or causal proof without a separate mapping.

## Promotion-gate checklist

- [x] typed directed graph implemented
- [x] SCC and load-bearing cycle audit implemented
- [x] deterministic topological ordering implemented for DAGs
- [x] bounded descendant invalidation implemented
- [x] reachability/causality firewall documented and tested
- [ ] repository-wide dependency completeness demonstrated
- [ ] temporal/versioned edge persistence demonstrated
- [ ] causal interpretation separately validated where used
- [ ] local-finality claims carry dependency-completeness evidence

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
node_id: cm__matrix_09_dependency_graph_cognitive_matrix_dependency_graph_contract
node_type: note
path: 25_COGNITIVE_MATRIX/09_DEPENDENCY_GRAPH/COGNITIVE_MATRIX_DEPENDENCY_GRAPH_CONTRACT.md
claim_class: AMOS_MODEL

______________________________________________________________________

**MOC:** [[25_COGNITIVE_MATRIX/09_DEPENDENCY_GRAPH/09_DEPENDENCY_GRAPH_MOC|09_DEPENDENCY_GRAPH_MOC]]

______________________________________________________________________

**Trang Framework:** [[11_KNOWLEDGE/TRANG_FRAMEWORK_RECURSIVE_ONTOLOGY_DYNAMICS|TRANG_FRAMEWORK_RECURSIVE_ONTOLOGY_DYNAMICS]]
