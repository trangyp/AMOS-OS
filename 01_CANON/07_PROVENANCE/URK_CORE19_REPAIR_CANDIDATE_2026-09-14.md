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

This record admits source material into the **candidate** layer only. It does not promote any candidate source to canonical status.

Canonical precedence remains governed by the existing canon process. Freshness, filename, apparent completeness, successful bounded tests, or a runtime binding are insufficient by themselves for canon promotion.

Origin architect / steward: **Trang Phan**.

## Source inputs

### C1 — Reasoning kernel

- Source collection: Google Drive `_00_AMOS_CANON:`
- File: `Reasoning kernel.txt`
- Drive file ID: `1Pbd9Tj03FDzgmV09vkVVZv5Ml2uak1-f`
- Current observed revision ID: `0B_FlOTCuYcaFUlU1NDFRalVkY0NOVzg1Wk9CMGd0WEpjYWNNPQ`
- Observed modified time: `2026-09-14T06:31:43.759Z`
- Declared source status: `ACTIVE_REPAIR_SPEC / AMOS_MODEL`
- Declared target: `AMOS_CORE v4.4`

### C2 — LOGIC compatibility registry

- Source collection: Google Drive `_00_AMOS_CANON:`
- File: `LOGIC.txt`
- Drive file ID: `1t4ePB_idXl3alYpZHzgc9jm_0tJjsz6w`
- Current observed revision ID: `0B_FlOTCuYcaFZlcxL1RGUW1BUCs4TEFmVVFlZWZXMzBlUWtvPQ`
- Observed modified time: `2026-09-14T06:31:35.546Z`
- Declared source status: `ACTIVE_REPAIR_SPEC / AMOS_MODEL`
- Declared target: `AMOS_CORE v4.4`

### C3 — URK mathematical substrate candidate v1.1

- Source collection: Google Drive `_00_AMOS_CANON:`
- File: `AMOS_URK_MATHEMATICAL_SUBSTRATE_CANDIDATE_v1.1.json`
- Drive file ID: `1cEomX8WidF_nQurE2f7tJ8zMlAdfxc2V`
- SHA-256 of ingested raw file: `0ee4aea0cda88388e1bf5d116ed34d95dd87d90a61c2b210fc3c8ff0c55c9d59`
- Declared source status: `PROPOSED_ARCHITECTURE / ACTIVE_CANON_CANDIDATE / NOT_CANON`
- Declared target: `AMOS_CORE v4.4`
- Bounded validation receipt: `AMOS_URK_MATH_V1_1_VALIDATION_RECEIPT_2026-09-14.json`
- Receipt Drive file ID: `1f2ue6Szb1B7YGq_L_DOHRQ-vzdOo3InG`
- Receipt raw SHA-256: `f55fb040dcf1eb34f077bf3e6158da3bc2c90a8def10ea02f1693354545efbbb`

### C4 — ULK ALU-02 executable profile candidate

- Source collection: Google Drive `_00_AMOS_CANON:`
- File: `ULK_ALU02_FIRST_ORDER_UNIFICATION_EXECUTABLE_PROFILE_V1_CANDIDATE.json`
- Drive file ID: `12j8wV7m1nwbRN65N_pnhk_Gd8DXthIz0`
- Raw SHA-256: `b29829139c8db4dc12e3dce4850a3491eb869e77fd30f40e8ea9c5c434ad7ac0`
- Canonical semantic owner remains: `ULK_LOGIC_KERNEL.md v2.1.0`
- Candidate scope: finite first-order **term unification** over variables, constants, and function terms with occurs-check.
- Candidate status: `PARTIAL_EXECUTABLE_EVIDENCE_CANDIDATE / NOT_CANON`

### C5 — ALU-02 executable checker and receipt

- Checker: `amos_ulk_alu02_unification_reference_checker_v1.py`
- Drive file ID: `1O_z3t-O7Np_mrpmoem3rBFsIf4DE6dln`
- Checker SHA-256: `002a4c72adf0afaa7ad1b33792008ea6a525ca43b69ae4eff301c1b06a135275`
- Receipt: `AMOS_ULK_ALU02_UNIFICATION_VALIDATION_RECEIPT_2026-09-14.json`
- Receipt Drive file ID: `1-5b0ygR2PDjQrPi-AdefC6_6EbBexOeU`
- Receipt raw SHA-256: `7e280159e636e50ea46c4e67a3e52fc57c5958a5168ed521992ae8d4259d9489`
- Receipt status: bounded executed evidence only; not formal completeness proof, Canon promotion, or effect authority.

## Candidate objects admitted for bounded runtime projection

The following objects are admitted as candidate/derived runtime inputs because their semantics can be typed and tested without claiming universal empirical or canonical truth:

1. **Namespace separation**
   - `URK_MATH != ULK_LOGIC`.
   - canonical ULK 8 logic-engine ALUs, ULMK 8 atomic units, Core-19 semantic positions, and executable AST/rewrite rules remain separate objects.

2. **P02 conflict preservation**
   - historical candidate: `NonExistence`.
   - recovered candidate: `Distinction`.
   - cross-lineage state: `COMPETING`.
   - a local use requires explicit namespace/version binding.

3. **Four-valued evidence state**
   - state represented as `(supports_true, supports_false)` over booleans.
   - neither, true-only, false-only, and both remain distinct states.
   - negation swaps the support channels.
   - information join accumulates support coordinate-wise.

4. **Core-19 matrix boundary**
   - 19 semantic positions define `19 * 19 = 361` pair coordinates.
   - coordinate existence does not establish a semantic law or equation at every coordinate.
   - `UNBOUND` remains a valid state.

5. **Typed tensor boundary**
   - invalid standard-math use of `[19,19,"1E∞"]` is rejected.
   - runtime projection uses explicit typed row, column, scale, context, regime, and observer axes where required.

6. **Topology/causality firewall**
   - relation, adjacency, path, correlation, temporal order, prediction, and graph reachability do not by themselves establish causation.

7. **Finite relation algebra**
   - URK-E1 finite relation ↔ Boolean adjacency encoding is admitted as established finite mathematics.
   - URK-E2 Boolean-semiring matrix composition is admitted for finite relation composition.
   - URK-E3 finite reflexive-transitive closure is admitted with containment, reflexivity, transitivity, and idempotence properties.
   - reachability is not silently upgraded to logical entailment or causal effect.

8. **Core-19 rewrite-order repair**
   - `NLOGIC(NLOGIC(x))` must be recognized before recursive child normalization.
   - bounded invariants include normalization idempotence and double-NLOGIC involution for the implemented unary fragment.

9. **Logic-fragment execution status**
   - ALU-01 classical propositional: bounded executable evidence exists.
   - ALU-02 first-order/unification: bounded **term-unification** candidate is rebound to an exact checker hash; this does not establish a complete first-order theorem prover.
   - ALU-07 quantum logic: canonical bounded claim retained but exact repository checker/receipt remains `REBIND_PENDING` on this surface.
   - ALU-03, ALU-04, ALU-05, ALU-06, and ALU-08 remain specification-only unless separately rebound.

10. **Promotion gate**
   - source resolved;
   - semantics typed;
   - assumptions bound;
   - equations checked;
   - counterexamples checked;
   - implementation receipt available where implementation is claimed;
   - canon authority present for Canon promotion.

## Quarantined / rejected generalizations

These are not admitted as universal runtime laws:

- `Paradox(X) <-> X AND NOT X` as general paradox semantics.
- `DLogic(X) <-> X AND NOT X` as general dual-logic semantics.
- universal linear time.
- causal path implies open topological region.
- Distinction equals NonExistence across lineages.
- missing/unknown equals false, zero, or non-existence.
- every Core-19 pair coordinate has a proven equation.
- `1E∞` as a standard mathematical tensor dimension/cardinality.
- pairwise satisfiability implies global satisfiability.
- graph reachability implies logical entailment.
- graph reachability implies causation.
- term unification implies full FOL theorem-prover completeness.
- architecture/source claims imply implementation.
- executable candidate evidence implies Canon promotion.

## Executable projection

Current repository projection is materialized on `trangyp/AMOS-OS` mainline.

Runtime components:
- `04_RUNTIME/01_REFERENCE_IMPLEMENTATION/core19_runtime.py`
- `04_RUNTIME/01_REFERENCE_IMPLEMENTATION/core19_tensor_topology.py`
- `04_RUNTIME/01_REFERENCE_IMPLEMENTATION/urk_relation_algebra.py`
- `04_RUNTIME/01_REFERENCE_IMPLEMENTATION/amos_ulk_alu02_unification_reference_checker_v1.py`
- `04_RUNTIME/01_REFERENCE_IMPLEMENTATION/ulk_fragment_execution_registry.py`
- `04_RUNTIME/01_REFERENCE_IMPLEMENTATION/internet_algorithm_registry.py`

Bounded verifiers:
- `04_RUNTIME/01_REFERENCE_IMPLEMENTATION/test_core19_runtime.py`
- `04_RUNTIME/01_REFERENCE_IMPLEMENTATION/test_core19_tensor_topology.py`
- `04_RUNTIME/01_REFERENCE_IMPLEMENTATION/test_urk_math_alu02_algorithms.py`

Observed bounded verification:
- Python compilation: PASS for the newly rebound URK/ALU-02/algorithm modules.
- Consolidated URK-E1..E3 / ALU-02 / algorithm-ingress suite: 12 PASS, 0 FAIL.
- ALU-02 source checker hash exactly matches the source receipt.
- ALU-02 receipt cases reproduced and extended with 3,000 seeded symmetry/idempotence fuzz pairs.
- URK-E1 encode/decode round trips checked over randomized finite relations.
- URK-E2 Boolean matrix composition cross-checked against direct set relation composition over randomized finite relations.
- URK-E3 closure checked over randomized finite directed relations for containment, reflexivity, transitivity, and idempotence.
- Earlier Core-19 repair evidence remains bounded to its own test domains.

The AMOS math-audit harness still intentionally surfaces its known global T2 probability-labeling counterexample. That pre-existing audit finding is not suppressed or misattributed to URK-E1..E3.

## Revalidation triggers

Revalidate this candidate projection if any of the following changes:

- any bound Drive source revision or raw hash;
- `K_CANON` admission rules;
- canonical ULK version/status;
- AMOS_CORE baseline;
- P02 source lineage evidence;
- ALU-02 checker identity, term ABI, occurs-check semantics, or receipt;
- exact quantum checker/receipt identity;
- runtime normalizer semantics;
- tensor/topology/relation-algebra type contracts;
- test harness or random seed/domain.

## Status

`CANDIDATE_SOURCE -> ADMISSIBLE_BOUNDED_PROJECTION`

`ALU02_TERM_UNIFICATION -> EXECUTABLE_BOUNDED_CANDIDATE_REBOUND`

`NOT_PROMOTED_TO_CANON`

`SYSTEM_WIDE_EXECUTABLE_CLOSURE = NOT_ESTABLISHED`
