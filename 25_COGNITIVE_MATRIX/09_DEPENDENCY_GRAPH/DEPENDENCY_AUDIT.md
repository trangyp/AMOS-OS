---
canon-group: meta
canon-type: validation_summary
rscf-state: derived
rscf-provenance: AMOS_corpus_plus_executable_repair
conclusion_class: DERIVED
epistemic_class: DERIVED
topic: Dependency Audit
created: 2026-08-22
updated: 2026-09-14
origin_architect: Trang Phan
---

# Dependency Audit

The typed dependency runtime separates load-bearing dependency from support, alternatives, contradiction, observation, supersession, invalidation proposal, and correlation.

## Incremental algorithm admission

`incremental_dependency_index.py` adds an insertion-incremental reachability index.

For an already closed reachability relation and a newly admitted edge `u -> v`, only nodes that already reach `u` (plus `u`) can acquire reachability to `v` or its existing descendants. The runtime therefore updates the Cartesian product:

`Pred+(u) x Succ+(v)`

where the `+` notation here means "include the endpoint itself". This is an implementation identity for single-edge insertion against the maintained transitive closure, not a causal equation.

Cycle localization uses Tarjan strongly connected components. When fixed-point cycle semantics are not explicitly enabled, a new edge that creates a cycle is rejected before state mutation.

Deletion is intentionally different: the insertion delta rule is not deletion-correct. By default edge removal returns `RECOMPUTE_REQUIRED`; an explicit bounded path may perform full recomputation.

## Local evidence

Current local incremental suite: `10/10 PASS`, including randomized DAG insertion differential checks against independent full reachability recomputation and non-mutation on blocked cycle attempts.

A synthetic benchmark with 220 nodes and 900 acyclic insertions produced the same final closure and measured approximately:

- incremental insertion maintenance: `0.0133 s`;
- full closure recomputed after every insertion: `0.6734 s`;
- observed ratio: about `50.8x` for that benchmark/environment.

This is a bounded synthetic benchmark, not a universal performance claim.

## External knowledge provenance

The implementation is informed by established graph/SCC methods and by semi-naive/differential incremental-computation principles. It does not copy external source code. External mechanism familiarity does not grant AMOS semantic or Canon authority.

RSCF-NODE
node_id: dependency_audit_graph_definition
node_type: VALIDATION_SUMMARY
path: 25_COGNITIVE_MATRIX/09_DEPENDENCY_GRAPH/DEPENDENCY_AUDIT.md
claim_class: DERIVED
rscf_state: DERIVED
