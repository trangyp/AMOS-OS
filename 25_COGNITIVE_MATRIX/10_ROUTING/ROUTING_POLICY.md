---
canon-group: meta
canon-type: runtime_contract
rscf-state: derived
rscf-provenance: AMOS_corpus_plus_executable_repair
conclusion_class: AMOS_MODEL
epistemic_class: DERIVED
topic: Routing Policy
created: 2026-08-22
updated: 2026-09-14
origin_architect: Trang Phan
---

# Routing Policy

Origin architect / steward: **Trang Phan**

## Status

`AMOS_MODEL / EXECUTABLE_BOUNDED_REFERENCE / NOT_CANON_PROMOTION`

Executable owner:
`04_RUNTIME/01_REFERENCE_IMPLEMENTATION/cognitive_matrix_routing_runtime.py`

Historical structural-policy evidence remains useful but bounded: the prior routing-policy validator recorded 19/19 passing cases. That receipt is evidence for the tested policy surface, not proof of live deployment. The current bounded runtime is a separate implementation surface and must be tested separately.

## Routing order

The router evaluates in this order:

1. validate registry identity;
2. reject failed or `UNKNOWN/GAP` load-bearing premises;
3. bind an explicit target if requested;
4. hard-filter query kind, scope, regime, capabilities, implementation state, validation, load-bearing epochs, and explicitly requested evidence-root threshold;
5. rank only the remaining eligible routes by declared semantic policy priority, then specialist status;
6. preserve a material tie as `AMBIGUOUS`;
7. separate route eligibility from effect authority;
8. return an effectful route only as `PROPOSAL_ONLY` for the infrastructure/control plane.

Registration order, speed, convenience, or a soft score cannot override a failed hard gate.

## Current bounded logic routes

- Classical propositional inference: `EXECUTABLE_BOUNDED`.
- ALU-02 finite first-order **term unification with occurs-check**: `EXECUTABLE_BOUNDED_SUBFRAGMENT`.
- Full first-order theorem proving / quantifier proof search: not implemented.
- ALU-07 quantum logic: `REBIND_PENDING` until exact checker/receipt identity is rebound.
- Temporal/LTL, epistemic/modal, non-monotonic/Dung, dependent type, categorical/topos: no executable route in this reference registry yet.

ALU-02 source evidence is bound to the 2026-09-14 `_00_AMOS_CANON` candidate profile/checker/receipt. The source checker SHA-256 is `002a4c72adf0afaa7ad1b33792008ea6a525ca43b69ae4eff301c1b06a135275`. The repository runtime adds explicit resource bounds and therefore requires its own local regression evidence; it does not inherit Canon authority from the Drive candidate.

## Hard invariants

```text
HARD_GATE_FAIL -> INELIGIBLE
UNKNOWN/GAP != PASS
EXPLICIT_TARGET_MISSING -> VISIBLE_FAILURE
AMBIGUOUS != SILENT_WINNER
CAPABILITY != AUTHORITY
ROUTED != COMMITTED
VALIDATION_PASS != CANON_PROMOTION
REGISTRATION_ORDER != SEMANTIC_PRIORITY
SCOPE_MISMATCH != FALLBACK_PERMISSION
DEPENDENCY_FRESHNESS_IS_SELECTIVE
```

Shared provenance descendants do not create independent evidence roots merely by count.

## External algorithm admissions

External algorithms are admitted as mechanisms only after AMOS boundary checks:

- first-order unification: Robinson / Martelli-Montanari family semantics with occurs-check;
- Tarjan SCC: cycle localization for dependency topology;
- semi-naive / differential-style delta propagation: incremental dependency reachability for insertions;
- e-graphs/equality saturation: research candidate for future rewrite search, not admitted as Canon or current executor;
- SMT incremental scopes: research candidate for repeated constraint solving;
- symbolic model checking: research candidate for temporal/state transition verification.

`ALGORITHM_KNOWN_ON_INTERNET != AMOS_ADMITTED_IMPLEMENTATION`.

## Non-claims

- no live deployment claim;
- no full FOL theorem-prover claim;
- no effect authority;
- no Canon promotion;
- no universal optimality of policy priority;
- no claim that all internet algorithms have been exhaustively enumerated.

RSCF-NODE
node_id: 25_cognitive_matrix_10_routing_routing_policy
node_type: COGNITIVE_MATRIX_ROUTING_POLICY
path: 25_COGNITIVE_MATRIX/10_ROUTING/ROUTING_POLICY.md
claim_class: AMOS_MODEL
rscf_state: DERIVED
canonical_status: CONDITIONAL
