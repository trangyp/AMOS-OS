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

Canonical precedence remains governed by `K_CANON`. Freshness, filename, apparent completeness, successful bounded tests, or a runtime binding are insufficient by themselves for canon promotion.

Origin architect / steward: **Trang Phan**.

## Source inputs

### C1 — Reasoning kernel

- Source collection: Google Drive `_00_AMOS_CANON:`
- File: `Reasoning kernel.txt`
- Drive file ID: `1Pbd9Tj03FDzgmV09vkVVZv5Ml2uak1-f`
- Observed revision ID: `0B_FlOTCuYcaFUlU1NDFRalVkY0NOVzg1Wk9CMGd0WEpjYWNNPQ`
- Observed modified time: `2026-09-14T06:31:43.759Z`
- Declared source status: `ACTIVE_REPAIR_SPEC / AMOS_MODEL`
- Target: `AMOS_CORE v4.4`

### C2 — LOGIC compatibility registry

- File: `LOGIC.txt`
- Drive file ID: `1t4ePB_idXl3alYpZHzgc9jm_0tJjsz6w`
- Observed revision ID: `0B_FlOTCuYcaFZlcxL1RGUW1BUCs4TEFmVVFlZWZXMzBlUWtvPQ`
- Observed modified time: `2026-09-14T06:31:35.546Z`
- Declared source status: `ACTIVE_REPAIR_SPEC / AMOS_MODEL`
- Target: `AMOS_CORE v4.4`

### C3 — URK mathematical substrate candidate v1.1

- File: `AMOS_URK_MATHEMATICAL_SUBSTRATE_CANDIDATE_v1.1.json`
- Drive file ID: `1cEomX8WidF_nQurE2f7tJ8zMlAdfxc2V`
- Raw SHA-256: `0ee4aea0cda88388e1bf5d116ed34d95dd87d90a61c2b210fc3c8ff0c55c9d59`
- Status: `PROPOSED_ARCHITECTURE / ACTIVE_CANON_CANDIDATE / NOT_CANON`
- Validation receipt: `AMOS_URK_MATH_V1_1_VALIDATION_RECEIPT_2026-09-14.json`
- Receipt Drive file ID: `1f2ue6Szb1B7YGq_L_DOHRQ-vzdOo3InG`
- Receipt raw SHA-256: `f55fb040dcf1eb34f077bf3e6158da3bc2c90a8def10ea02f1693354545efbbb`

### C4 — ULK ALU-02 executable profile candidate

- File: `ULK_ALU02_FIRST_ORDER_UNIFICATION_EXECUTABLE_PROFILE_V1_CANDIDATE.json`
- Drive file ID: `12j8wV7m1nwbRN65N_pnhk_Gd8DXthIz0`
- Raw SHA-256: `b29829139c8db4dc12e3dce4850a3491eb869e77fd30f40e8ea9c5c434ad7ac0`
- Canonical semantic owner remains `ULK_LOGIC_KERNEL.md v2.1.0`.
- Candidate scope: finite first-order **term unification** with occurs-check.
- Status: `PARTIAL_EXECUTABLE_EVIDENCE_CANDIDATE / NOT_CANON`.

### C5 — ALU-02 checker and receipt

- Checker: `amos_ulk_alu02_unification_reference_checker_v1.py`
- Drive file ID: `1O_z3t-O7Np_mrpmoem3rBFsIf4DE6dln`
- Checker SHA-256: `002a4c72adf0afaa7ad1b33792008ea6a525ca43b69ae4eff301c1b06a135275`
- Receipt: `AMOS_ULK_ALU02_UNIFICATION_VALIDATION_RECEIPT_2026-09-14.json`
- Receipt Drive file ID: `1-5b0ygR2PDjQrPi-AdefC6_6EbBexOeU`
- Receipt raw SHA-256: `7e280159e636e50ea46c4e67a3e52fc57c5958a5168ed521992ae8d4259d9489`

### C6 — current unified brain source for ALU-03 and ALU-07

- File: `unified_brain.py`
- Drive file ID: `1oDrxdqfF-1HFxwDbW5ooSfsfYfJm05iQ`
- Current observed revision ID: `0B_FlOTCuYcaFdVpKNEFLOTNHcFM3Q01GVGx4TmpVTTBHVytrPQ`
- Current revision modified time: `2026-09-14T07:20:40.501Z`
- Current raw SHA-256: `c04cbe63b3a8d3b67095c17bcfb1c471ccb9841d78412aa086f44fcb35b14d8e`
- ALU-03 callable AST SHA-256: `9eecefbdc60faa0fe70ff758400174130ac536fc92debe7d85f22d55759c7f9f`
- ALU-07 callable AST bundle SHA-256: `754402e1a342f4eee7d4bf6c19c155a0ff6257cab82bcaf1f1e3bedbcec98410`
- Status: executable source evidence for bounded projection only; not Canon promotion.

### C7 — ALU-04 finite Kripke checker

- Checker: `amos_ulk_alu04_finite_kripke_checker_v1.py`
- Current checker SHA-256: `869d095013dabdfdce089e1f4065350417b5e77722c26738d6beded0ec87eac0`.
- Scope: finite worlds/agents; propositional atoms; `NOT/AND/OR/IMPLIES/BOX/DIAMOND`.
- Fail-closed repair: malformed formulas and undeclared agents are rejected; a declared agent with zero successors retains standard vacuous-BOX semantics.
- Status: `EXECUTABLE_BOUNDED_CANDIDATE_REBOUND / NOT_CANON`.

### C8 — ALU-05 finite Dung checker

- Checker: `amos_ulk_alu05_dung_checker_v1.py`
- Current checker SHA-256: `8e613729ca3a0ef9d24a8bafba432ab9b358fe3c2b4a8ac945ee7b1660ed658c`.
- Scope: finite Dung argumentation; conflict freedom, defence, characteristic function, grounded extension, admissibility, explicitly bounded preferred-extension enumeration.
- Fail-closed repair: unknown argument-set members, unknown arguments, and invalid enumeration bounds are rejected.
- Status: `EXECUTABLE_BOUNDED_CANDIDATE_REBOUND / NOT_CANON`.

## Stale whole-file receipt repair

The recursive mutation queue carried an earlier **whole-file** `unified_brain.py` hash for ALU-07. The Drive file subsequently changed, so that monolithic hash no longer identifies the current source.

Fail-closed disposition:

```text
STALE_WHOLE_FILE_RECEIPT != CURRENT_CHECKER_IDENTITY
```

The repair therefore does **not** silently accept the old receipt. Current ALU-03 and ALU-07 execution bindings use:

1. exact Drive file identity;
2. exact current revision identity;
3. current whole-file SHA for source-state provenance;
4. normalized callable-AST hashes for fragment-level semantic identity;
5. independent current execution tests.

For standalone ALU-02/04/05 checkers, exact checker SHA-256 is the implementation identity. Any checker change invalidates the old hash binding and requires revalidation/rebinding.

## Candidate objects admitted for bounded runtime projection

1. **Namespace separation**
   - `URK_MATH != ULK_LOGIC`.
   - canonical ULK ALUs, ULMK atomic units, Core-19 semantic coordinates, and executable AST/runtime surfaces remain distinct.

2. **P02 conflict preservation**
   - historical `NonExistence` and recovered `Distinction` remain `COMPETING` across source lineages.
   - namespace/version binding is required for local use.

3. **Four-valued evidence state**
   - `(supports_true, supports_false)` preserves neither/true-only/false-only/both.

4. **Core-19 matrix boundary**
   - 19 semantic positions give 361 pair coordinates.
   - coordinate existence does not prove 361 equations.
   - `UNBOUND` remains valid.

5. **Typed tensor boundary**
   - row, column, scale, context, regime, and observer axes remain typed and non-interchangeable.
   - `1E∞` is not admitted as a standard tensor dimension.

6. **Topology/causality firewall**
   - relation, adjacency, temporal order, prediction, reachability, and specialization preorder do not by themselves establish causation.
   - finite topology validation binds open-set semantics exactly for finite carriers before any topology-derived relation is used.

7. **Finite relation algebra**
   - URK-E1 finite relation/Boolean-adjacency encoding.
   - URK-E2 Boolean-semiring composition for finite relations.
   - URK-E3 finite reflexive-transitive closure with containment, reflexivity, transitivity, and idempotence checks.
   - reachability is not logical entailment or causation.

8. **Core-19 rewrite repair**
   - `NLOGIC(NLOGIC(x))` is resolved before child descent in the implemented unary fragment.

9. **Logic-fragment execution status**
   - ALU-01: `EXECUTABLE_BOUNDED` for the bound classical propositional subset.
   - ALU-02: `EXECUTABLE_BOUNDED_CANDIDATE_REBOUND` for finite first-order **term unification**, not full FOL proof search.
   - ALU-03: `EXECUTABLE_BOUNDED_CANDIDATE_REBOUND` for finite-trace Boolean temporal semantics over `ATOM/NOT/AND/OR/IMPLIES/X/F/G/U`; not infinite-trace model checking, CTL, or timed logic.
   - ALU-04: `EXECUTABLE_BOUNDED_CANDIDATE_REBOUND` for finite Kripke propositional modal/epistemic semantics; not dynamic/common-knowledge/probabilistic/infinite-model closure.
   - ALU-05: `EXECUTABLE_BOUNDED_CANDIDATE_REBOUND` for finite Dung argumentation; preferred-extension enumeration remains explicitly bounded.
   - ALU-07: `EXECUTABLE_BOUNDED_CANDIDATE_REBOUND` for the current classical finite-dimensional numerical reference checker over its explicitly enumerated operator surface; not quantum hardware, quantum advantage, or universal quantum-logic completion.
   - ALU-06 and ALU-08 remain `SPECIFICATION_ONLY` until separately rebound.

10. **Promotion gate**
   - evidence eligibility and Canon authority remain separate.
   - executable evidence cannot mint Canon authority.

## Quarantined / rejected generalizations

Not admitted as universal runtime laws:

- `Paradox(X) <-> X AND NOT X` as general paradox semantics;
- `DLogic(X) <-> X AND NOT X` as general dual-logic semantics;
- universal linear time;
- causal path implies open topological region;
- `Distinction == NonExistence` across lineages;
- missing/unknown equals false, zero, or non-existence;
- every Core-19 coordinate has a proven equation;
- pairwise satisfiability implies global satisfiability;
- graph reachability implies logical entailment or causation;
- term unification implies complete FOL theorem proving;
- finite-trace temporal evaluation implies infinite-trace LTL model checking;
- finite Kripke evaluation implies complete epistemic logic;
- finite Dung evaluation implies all non-monotonic reasoning;
- a classical finite-dimensional numerical checker implies quantum hardware execution or quantum advantage;
- source or executable evidence implies Canon promotion.

## Executable projection

Current repository runtime components include:

- `core19_runtime.py`
- `core19_tensor_topology.py`
- `finite_topology_runtime.py`
- `urk_relation_algebra.py`
- `amos_ulk_alu02_unification_reference_checker_v1.py`
- `amos_ulk_alu03_finite_trace_ltl_checker_v1.py`
- `amos_ulk_alu04_finite_kripke_checker_v1.py`
- `amos_ulk_alu05_dung_checker_v1.py`
- `amos_ulk_alu07_reference_checker_current.py`
- `ulk_fragment_execution_registry.py`
- `internet_algorithm_registry.py`

Bounded verifiers include:

- `test_core19_runtime.py`
- `test_core19_tensor_topology.py`
- `test_finite_topology_runtime.py`
- `test_urk_math_alu02_algorithms.py`
- `test_alu03_alu07_rebind.py`
- `test_ulk_alu04_alu05.py`

Observed current verification includes:

- ALU-02 exact checker hash matches its source receipt; receipt cases plus 3,000 seeded symmetry/idempotence fuzz pairs pass.
- ALU-03 named cases plus 2,000 seeded randomized formulas match an independent finite-trace evaluator.
- ALU-04 and ALU-05 exact checker hashes are bound to the current repaired implementations; malformed/unknown inputs fail closed in the tested scope.
- ALU-07 all bound operator surfaces pass its current positive/negative numerical tests within the declared bounded scope.
- URK-E1..E3 randomized finite-relation checks pass within their finite domain.
- Current-main reconciliation locally reconstructed 38 focused functional tests across Core-19, six-axis tensor storage, finite topology, ALU-04, and ALU-05 with 38 PASS / 0 FAIL.

The global AMOS math-audit harness still intentionally exposes its historical T2 probability-labeling counterexample. That finding remains visible and is not misattributed to the current URK/ALU projections.

## Revalidation triggers

Revalidate when any of the following changes:

- bound Drive source revision or raw hash;
- ALU-02/04/05 checker hash or executable ABI;
- `unified_brain.py` current revision when ALU-03 or ALU-07 is bound to it;
- ALU-03 or ALU-07 callable AST hash;
- canonical ULK version/status;
- `K_CANON` admission rules;
- AMOS_CORE baseline;
- P02 lineage evidence;
- tensor/topology/relation-algebra contracts;
- test harness, numerical tolerance, random seed, or test domain.

## Status

`CANDIDATE_SOURCE -> ADMISSIBLE_BOUNDED_PROJECTION`

`ALU02_TERM_UNIFICATION -> EXECUTABLE_BOUNDED_CANDIDATE_REBOUND`

`ALU03_FINITE_TRACE_LTL -> EXECUTABLE_BOUNDED_CANDIDATE_REBOUND`

`ALU04_FINITE_KRIPKE -> EXECUTABLE_BOUNDED_CANDIDATE_REBOUND`

`ALU05_FINITE_DUNG -> EXECUTABLE_BOUNDED_CANDIDATE_REBOUND`

`ALU07_FINITE_DIMENSIONAL_REFERENCE -> EXECUTABLE_BOUNDED_CANDIDATE_REBOUND`

`NOT_PROMOTED_TO_CANON`

`SYSTEM_WIDE_EXECUTABLE_CLOSURE = NOT_ESTABLISHED`
