---
title: URK / Core-19 Repair Candidate Provenance — 2026-09-14
origin_architect: Trang Phan
type: candidate_canon_provenance
status: ACTIVE_REPAIR_SPEC
conclusion_class: AMOS_MODEL
canonical_status: NOT_PROMOTED
amos_core_target: v4.4
created: 2026-09-14
updated: 2026-09-14
---

# URK / Core-19 Repair Candidate Provenance — 2026-09-14

## Authority boundary

This record admits source material into the **candidate** layer only. It does not promote candidate sources, repair specifications, executable projections, or validation receipts to Canon.

Canonical precedence remains governed by `K_CANON`. Freshness, filename, apparent completeness, successful bounded tests, or runtime binding are insufficient by themselves for canon promotion.

Origin architect / steward: **Trang Phan**.

## Current source identities

### C1 — Reasoning kernel

- Collection: Google Drive `_00_AMOS_CANON:`
- File: `Reasoning kernel.txt`
- Drive file ID: `1Pbd9Tj03FDzgmV09vkVVZv5Ml2uak1-f`
- Current revision ID: `0B_FlOTCuYcaFdGZTc25IYkhWQVJZQTJaR090R2IzNTdhMXNJPQ`
- Current modified time: `2026-09-14T11:24:42.693Z`
- Previous revision ID: `0B_FlOTCuYcaFZmtzdVRRaTIvcW5rcDBVQ3VQbHBWMGE3VHhvPQ`
- Declared source status: `ACTIVE_REPAIR_SPEC / AMOS_MODEL`
- Target: `AMOS_CORE v4.4`

### C2 — LOGIC compatibility registry

- File: `LOGIC.txt`
- Drive file ID: `1t4ePB_idXl3alYpZHzgc9jm_0tJjsz6w`
- Current revision ID: `0B_FlOTCuYcaFZ2ZkelhpT1ZOOW13YWE3dkd0L1liSG40QzVrPQ`
- Current modified time: `2026-09-14T11:30:15.504Z`
- Previous revision ID: `0B_FlOTCuYcaFQUpnMVNOMjZVY29CczRMYjBIMmIzOGw3VlQ4PQ`
- Declared source status: `ACTIVE_REPAIR_SPEC / AMOS_MODEL`
- Target: `AMOS_CORE v4.4`

### C3 — URK mathematical substrate candidate v1.1

- File: `AMOS_URK_MATHEMATICAL_SUBSTRATE_CANDIDATE_v1.1.json`
- Drive file ID: `1cEomX8WidF_nQurE2f7tJ8zMlAdfxc2V`
- Recorded SHA-256: `0ee4aea0cda88388e1bf5d116ed34d95dd87d90a61c2b210fc3c8ff0c55c9d59`
- Status: `PROPOSED_ARCHITECTURE / ACTIVE_CANON_CANDIDATE / NOT_CANON`
- Validation receipt file ID: `1f2ue6Szb1B7YGq_L_DOHRQ-vzdOo3InG`
- Recorded receipt SHA-256: `f55fb040dcf1eb34f077bf3e6158da3bc2c90a8def10ea02f1693354545efbbb`

### C4 — unified brain source for ALU-03 and ALU-07

- File: `unified_brain.py`
- Drive file ID: `1oDrxdqfF-1HFxwDbW5ooSfsfYfJm05iQ`
- Bound revision ID: `0B_FlOTCuYcaFdVpKNEFLOTNHcFM3Q01GVGx4TmpVTTBHVytrPQ`
- Recorded whole-file SHA-256: `c04cbe63b3a8d3b67095c17bcfb1c471ccb9841d78412aa086f44fcb35b14d8e`
- ALU-03 callable AST SHA-256: `9eecefbdc60faa0fe70ff758400174130ac536fc92debe7d85f22d55759c7f9f`
- ALU-07 callable AST SHA-256: `754402e1a342f4eee7d4bf6c19c155a0ff6257cab82bcaf1f1e3bedbcec98410`

## Latest source-delta admission

The current C1/C2 revisions strengthen the repaired mathematical/type boundaries. Candidate admission includes:

1. **Coordinate field versus tensor**
   - `URKField : Core19 × Core19 × Scale × Context × Regime × Observer ⇀ Value` is a typed partial coordinate/data field.
   - an indexed field/array is not an algebraic tensor by shape or naming alone;
   - algebraic tensor language requires a scalar structure, module/vector-space axis structures, multilinearity/tensor-product semantics, and a basis/variance witness when coordinate coefficients are used.

2. **Structural adjacency versus point-set topology**
   - the former `TopologyMatrix` name is compatibility terminology for a structural adjacency field only;
   - graph adjacency/reachability, point-set topology, and causality remain separate mathematical/semantic objects.

3. **Selective invalidation governance**
   - dependency propagation is an AMOS governance/runtime rule, not a universal mathematical axiom;
   - execution requires explicit dependency orientation, state/epoch binding, closure algorithm binding, and validation receipt;
   - stale/affected descendants are not thereby proven false.

4. **Partial Core-19 semantics**
   - 19 positions produce 361 pair coordinates;
   - coordinate existence does not prove 361 semantic equations;
   - `UNBOUND` is a valid state.

5. **P02 source competition**
   - historical `NonExistence` and recovered `Distinction` remain `COMPETING` across source lineages;
   - namespace/version binding is required for local use.

6. **Four-valued evidence state**
   - `(supports_true, supports_false)` preserves neither/true-only/false-only/both;
   - paradox and null states are not collapsed into classical booleans.

7. **Core-19 rewrite order**
   - `NLOGIC(NLOGIC(x)) -> x` is resolved before child descent;
   - the bounded normalizer is required to remain idempotent and involutive under the admitted fragment.

8. **Finite Boolean reachability**
   - relation composition uses Boolean-semiring `OR/AND` semantics;
   - reflexive transitive closure computes graph reachability only;
   - `REACHABLE != ENTAILS` and `REACHABLE != CAUSES`.

## Current executable projection

Repository reference components include:

- `core19_runtime.py`
- `core19_tensor_topology.py` (legacy filename; canonical runtime semantics are coordinate field + structural adjacency)
- `finite_topology_runtime.py`
- `urk_relation_algebra.py`
- `internet_algorithm_registry.py`
- `primitive_contract_runtime.py`
- `cognitive_matrix_runtime.py`
- `cognitive_matrix_contract_runtime.py`
- `ulk_fragment_execution_registry.py`

Current ULK execution projection, owned by `ulk_fragment_execution_registry.py`:

- ALU-01 Classical Propositional: `EXECUTABLE_BOUNDED`.
- ALU-02 First-Order Unification: `EXECUTABLE_BOUNDED_CANDIDATE_REBOUND` — finite first-order term unification with occurs-check, not complete FOL proving.
- ALU-03 Temporal/LTL: `EXECUTABLE_BOUNDED_CANDIDATE_REBOUND` — finite-trace Boolean temporal semantics, not infinite-trace model checking.
- ALU-04 Epistemic/Modal: `EXECUTABLE_BOUNDED_CANDIDATE_REBOUND` — finite Kripke propositional modal semantics; no dynamic/common-knowledge/probabilistic/infinite-model completeness claim.
- ALU-05 Non-Monotonic/Dung: `EXECUTABLE_BOUNDED_CANDIDATE_REBOUND` — finite Dung argumentation subset.
- ALU-06 Dependent Type: `EXECUTABLE_BOUNDED_CANDIDATE_REBOUND` — bounded dependent Pi-calculus subset, not Lean/Coq or full Calculus of Constructions.
- ALU-07 Quantum Logic: `EXECUTABLE_BOUNDED_CANDIDATE_REBOUND` — classical finite-dimensional numerical reference subset; no quantum-hardware or quantum-advantage claim.
- ALU-08 Categorical/Topos: `EXECUTABLE_BOUNDED_CANDIDATE_REBOUND` — finite small-category law + finite Heyting-algebra subset; not elementary-topos certification.

Canonical fragment ownership remains `ULK_LOGIC_KERNEL.md v2.1.0`. Execution evidence does not rewrite Canon.

## Current bounded validation evidence

Repository CI currently exercises the complete reference-runtime unittest discovery. Relevant executed lanes include:

- Core-19/P02/Truth4/rewrite regression tests;
- coordinate-field versus algebraic-tensor type firewall;
- structural-adjacency versus point-set-topology firewall;
- finite topology checks;
- finite relation algebra and Boolean closure;
- ULK fragment checker bindings;
- C01–C09 control-plane coverage registry;
- generic L00–L29 primitive contract runtime;
- adversarial primitive identity/provenance/dependency/authority tests.

Latest math type-firewall CI receipt: commit `6047daa3700859139069a1708f44cdf62729b81d`, completed successfully on 2026-09-14.

Latest primitive-contract CI receipt: commit `6e3eea239e796e7bcdd2eb2cc7dced10684804e4`, completed successfully on 2026-09-14.

`TEST_PASS != TRUTH`: these receipts establish bounded executable behavior under their declared test domains only.

## Quarantined / rejected generalizations

Not admitted as universal runtime laws:

- `Paradox(X) <-> X AND NOT X` as general paradox semantics;
- `DLogic(X) <-> X AND NOT X` as general dual-logic semantics;
- universal linear time;
- causal path implies open topological region;
- `Distinction == NonExistence` across lineages;
- missing/unknown equals false, zero, or non-existence;
- every Core-19 coordinate has a proven equation;
- coordinate/indexed-array shape alone establishes tensor semantics;
- graph adjacency/reachability establishes point-set topology, logical entailment, or causality;
- pairwise satisfiability implies global satisfiability;
- dependency invalidation proves descendants false;
- bounded fragment execution implies complete logic-fragment semantics;
- source or executable evidence implies Canon promotion.

## Revalidation triggers

Revalidate when any of the following changes:

- current `LOGIC.txt` or `Reasoning kernel.txt` revision;
- bound Drive source revision/hash/AST identity;
- canonical ULK version/status;
- `K_CANON` admission rules;
- AMOS_CORE baseline;
- P02 lineage evidence;
- coordinate-field/tensor/topology/relation contracts;
- checker identity or implementation scope;
- dependency orientation or invalidation epoch;
- test harness, tolerance, seed, or tested domain.

## Status

`CANDIDATE_SOURCE -> ADMISSIBLE_BOUNDED_PROJECTION`

`CANONICAL_ULK_OWNER = ULK_LOGIC_KERNEL.md v2.1.0`

`ALU01 -> EXECUTABLE_BOUNDED`

`ALU02..ALU08 -> EXECUTABLE_BOUNDED_CANDIDATE_REBOUND`

`NOT_PROMOTED_TO_CANON`

`SYSTEM_WIDE_EXECUTABLE_CLOSURE = NOT_ESTABLISHED`
