---
canon-group: meta
canon-type: moc
rscf-state: derived
rscf-provenance: AMOS_corpus_plus_executable_repair
conclusion_class: AMOS_MODEL
epistemic_class: DERIVED
topic: Cognitive Matrix Routing MOC
updated: 2026-09-14
origin_architect: Trang Phan
---

# 10 Routing — Map of Content

**Path:** `25_COGNITIVE_MATRIX/10_ROUTING`

Active owners:

- [[25_COGNITIVE_MATRIX/10_ROUTING/ROUTING_POLICY|ROUTING_POLICY]] — executable routing semantics and hard gates.
- [[25_COGNITIVE_MATRIX/10_ROUTING/BINDING_RULES|BINDING_RULES]] — typed request/candidate/epoch/authority bindings.
- [[25_COGNITIVE_MATRIX/10_ROUTING/ROUTING_AUDIT|ROUTING_AUDIT]] — bounded evidence and falsifiers.
- [[25_COGNITIVE_MATRIX/10_ROUTING/COGNITIVE_MATRIX_ROUTING_CONTRACT|COGNITIVE_MATRIX_ROUTING_CONTRACT]] — package contract.

Executable reference surfaces:

- `04_RUNTIME/01_REFERENCE_IMPLEMENTATION/cognitive_matrix_routing_runtime.py`
- `04_RUNTIME/01_REFERENCE_IMPLEMENTATION/unification_runtime.py`
- `04_RUNTIME/01_REFERENCE_IMPLEMENTATION/test_cognitive_matrix_routing_runtime.py`
- `04_RUNTIME/01_REFERENCE_IMPLEMENTATION/test_routing_unification_integration.py`

Dependency inputs:

- [[25_COGNITIVE_MATRIX/09_DEPENDENCY_GRAPH/09_DEPENDENCY_GRAPH_MOC|09_DEPENDENCY_GRAPH]]
- [[25_COGNITIVE_MATRIX/11_VALIDATION/11_VALIDATION_MOC|11_VALIDATION]]

Hard boundary: routing proposes an eligible execution surface; it does not own semantic truth, Canon admission, or durable-effect authorization.
