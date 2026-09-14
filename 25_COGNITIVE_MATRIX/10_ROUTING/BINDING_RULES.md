---
canon-group: meta
canon-type: runtime_contract
rscf-state: derived
rscf-provenance: AMOS_corpus_plus_executable_repair
conclusion_class: AMOS_MODEL
epistemic_class: DERIVED
topic: Routing Binding Rules
created: 2026-08-22
updated: 2026-09-14
origin_architect: Trang Phan
---

# Routing Binding Rules

Origin architect / steward: **Trang Phan**

Bindings are typed constraints, not naming conventions.

## Request binding

A `RouteRequest` binds:

- request identity;
- query kind;
- exact scope;
- exact regime;
- required capabilities;
- optional explicit target;
- load-bearing premise state;
- current named epochs;
- explicit minimum independent-evidence-root threshold when required;
- effectfulness and presence/absence of an authority binding;
- consequence class;
- payload.

Missing scope/regime identity is invalid. A wildcard candidate scope/regime is rejected by the bounded reference runtime.

## Candidate binding

A `RouteCandidate` binds:

- stable target identity;
- supported query kinds;
- exact scopes/regimes;
- capabilities;
- implementation state;
- validation state;
- semantic policy priority;
- specialist/default role;
- source version;
- provenance roots;
- load-bearing epoch dependencies.

Duplicate target IDs fail the candidate registry closed.

## Implementation-state boundary

```text
EXECUTABLE_BOUNDED
EXECUTABLE_BOUNDED_SUBFRAGMENT
REBIND_PENDING
SPECIFICATION_ONLY
UNKNOWN
```

`EXECUTABLE_BOUNDED_SUBFRAGMENT` is intentionally narrower than full-fragment execution. ALU-02 finite first-order term unification occupies this state; it does not license quantifier inference or theorem-prover completeness.

## Epoch rule

Only declared load-bearing epoch dependencies invalidate a cached route. An unrelated epoch change does not force global invalidation.

For candidate `c` with bound epoch dependencies `E_c` and current epoch map `E`:

`Fresh(c,E)` iff every `(k,v)` in `E_c` satisfies `E[k]=v`.

This is a definition of the reference contract, not a universal law of distributed systems.

## Authority rule

`authority_bound=True` means only that the routing request carries an authority binding. It does not authorize commit inside the router.

```text
ROUTE_ELIGIBLE + AUTHORITY_BOUND + EFFECTFUL
-> PROPOSAL_ONLY
```

Commit-time authorization remains a control-plane responsibility.

RSCF-NODE
node_id: 25_cognitive_matrix_10_routing_binding_rules
node_type: ROUTING_BINDING_CONTRACT
path: 25_COGNITIVE_MATRIX/10_ROUTING/BINDING_RULES.md
claim_class: AMOS_MODEL
rscf_state: DERIVED
