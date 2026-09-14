---
title: URK / Core-19 Repair Candidate Provenance — 2026-09-14
origin_architect: Trang Phan
type: candidate_canon_provenance
status: ACTIVE_REPAIR_SPEC
conclusion_class: AMOS_MODEL
canonical_status: NOT_PROMOTED
amos_core_target: v4.4
created: 2026-09-14
---

# URK / Core-19 Repair Candidate Provenance — 2026-09-14

## Authority boundary

This record admits source material into the **candidate** layer only. It does not promote either source to canonical status.

Canonical precedence remains governed by the existing canon process. Freshness, filename, apparent completeness, or successful bounded tests are insufficient by themselves for canon promotion.

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
   - runtime projection uses explicit typed row, column, scale, context, and regime axes.

6. **Topology/causality firewall**
   - relation, adjacency, path, correlation, temporal order, and prediction do not by themselves establish causation.

7. **Core-19 rewrite-order repair**
   - `NLOGIC(NLOGIC(x))` must be recognized before recursive child normalization.
   - bounded invariants include normalization idempotence and double-NLOGIC involution for the implemented unary fragment.

8. **Logic-fragment execution status**
   - classical propositional: bounded executable evidence exists.
   - quantum logic: canonical bounded claim retained but exact local checker/receipt is `REBIND_PENDING`.
   - remaining canonical ULK fragments are specification-only on this repair surface unless separately rebound.

9. **Promotion gate**
   - source resolved;
   - semantics typed;
   - assumptions bound;
   - equations checked;
   - counterexamples checked;
   - implementation receipt available where implementation is claimed;
   - canon authority present.

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
- architecture/source claims imply implementation.

## Executable projection

Repository branch: `amos/urk-core19-repair-20260914`

Runtime projection:
- `04_RUNTIME/01_REFERENCE_IMPLEMENTATION/core19_runtime.py`

Bounded verifier:
- `04_RUNTIME/01_REFERENCE_IMPLEMENTATION/test_core19_runtime.py`

Observed local verification before repository staging:
- Python compile: PASS.
- Unit/property tests: 12 PASS, 0 FAIL.
- Random unary trees: 50,000 seeded cases, 0 observed idempotence failures, 0 observed double-NLOGIC involution failures.
- AMOS math audit: 110 equation-like records scanned across changed runtime/test files; no hard failure attributable to those changed files.

## Revalidation triggers

Revalidate this candidate projection if any of the following changes:

- either Drive source revision;
- `K_CANON` admission rules;
- canonical ULK version/status;
- AMOS_CORE baseline;
- P02 source lineage evidence;
- exact quantum checker/receipt identity;
- runtime normalizer semantics;
- tensor/topology type contracts;
- test harness or random seed/domain.

## Status

`CANDIDATE_SOURCE -> ADMISSIBLE_BOUNDED_PROJECTION`

`NOT_PROMOTED_TO_CANON`

`SYSTEM_WIDE_EXECUTABLE_CLOSURE = NOT_ESTABLISHED`
