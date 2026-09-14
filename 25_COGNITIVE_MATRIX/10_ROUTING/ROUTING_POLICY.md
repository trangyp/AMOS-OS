---
canon-group: meta
canon-type: framework
rscf-state: derived
rscf-provenance: AMOS_corpus
conclusion_class: AMOS_MODEL
epistemic_class: DERIVED
topic: Routing Policy
tags:
  - canon-group/tech-ai
  - rscf/claim
  - rscf/provenance
  - cognitive-matrix
updated: 2026-09-14
---

# ROUTING_POLICY — Bounded Executable Contract

**Origin architect / steward:** Trang Phan  
**Canonical status:** `MODEL / NOT_CANON_PROMOTION`  
**Implementation status:** `IMPLEMENTED_BOUNDED / VALIDATED_BOUNDED`  
**Runtime:** `04_RUNTIME/01_REFERENCE_IMPLEMENTATION/cognitive_matrix_runtime.py`

## Purpose

Route a typed Cognitive Matrix gap to the subsystem capable of resolving it while preserving the separation between capability and authority.

## Gap routing map

```text
SOURCE            -> CANON_ADMISSION
SEMANTICS         -> MATH_SEMANTIC_AUDIT
IMPLEMENTATION    -> IMPLEMENTATION
VALIDATION        -> VALIDATION
AUTHORITY         -> AUTHORITY_CONTROL_PLANE
DEPENDENCY_CYCLE  -> GRAPH_REPAIR
STALENESS         -> REVALIDATION
CONTRADICTION     -> COMPETING_EVIDENCE
```

The map selects a capability domain. It does not authorize effects in that domain.

## Hard invariant

For every bounded route decision `r`:

```text
r.grants_authority = false
```

Authority must come from the relevant control-plane witness and commit-time gate. Routing cannot create, widen, inherit, or infer authority.

## Routing preconditions

A route requires:

- stable `gap_id`;
- explicit `GapKind`;
- normalized priority dimensions where ranking is requested;
- preserved source/provenance links outside this router.

Unknown semantic categories must not be coerced into a known route merely to obtain closure.

## Architecture boundaries

```text
ROUTING != EXECUTION
CAPABILITY != AUTHORITY
PROPOSAL != COMMIT
MATCHED_SKILL != VERIFIED_RESULT
RELATION != CAUSATION
UNKNOWN/GAP != PASS
```

## Algorithm-family registry

The same runtime now carries applicability contracts for:

- Kahn topological ordering — executable, DAG-only load-bearing graph;
- Tarjan SCC decomposition — executable directed-graph cycle/component audit;
- Dijkstra shortest path — executable only with finite non-negative edge costs;
- A* — registered but not implemented here; heuristic assumptions must be explicit;
- AC-3 — registered but not implemented here; arc consistency is not global satisfiability;
- CP-SAT — external integer-constraint solver contract;
- SMT — external theory-typed SAT/UNSAT/UNKNOWN contract;
- property-based testing — bounded generated evidence, not universal proof.

This registry prevents algorithm names from being treated as interchangeable reasoning operators.

## Executed validation

Bounded tests verify that authority gaps route to the authority control plane while `grants_authority` remains false, and that algorithm preconditions fail closed when required assumptions are absent.

## Status boundary

Only the routing map and declared local algorithms are implemented by this reference runtime. External solver registrations remain capability contracts until an exact implementation/version/receipt is bound.

[[25_COGNITIVE_MATRIX/10_ROUTING/10_ROUTING_MOC|10_ROUTING_MOC]] · [[03_CONTROL_PLANE/03_CONTROL_PLANE_MOC|03_CONTROL_PLANE_MOC]] · [[00_ROOT/00_ROOT_MOC|00_ROOT_MOC]]
