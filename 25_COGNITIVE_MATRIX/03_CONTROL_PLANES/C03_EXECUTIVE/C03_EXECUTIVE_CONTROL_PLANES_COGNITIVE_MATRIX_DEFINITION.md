---
canon-group: meta
canon-type: framework
rscf-state: source-claim
rscf-claim: conditional
rscf-provenance: AMOS_corpus
conclusion_class: AMOS_MODEL
epistemic_class: AMOS_MODEL
topic: C03 Executive Control Planes Cognitive Matrix Definition
tags:
  - canon-group/tech-ai
  - rscf/claim
  - rscf/provenance
  - amos-model
created: 2026-08-22
updated: 2026-09-14
---

# C03 — Executive

**Package:** `C03_EXECUTIVE`  
**Class:** `COGNITIVE_MATRIX_CONTROL_PLANE`  
**Origin architect / steward:** Trang Phan  
**Status:** `EXECUTABLE_BOUNDED_REFERENCE / VALIDATION_REQUIRED_BEYOND_TESTED_SCOPE`

## Scope

C03 converts an already-formed candidate set into a bounded executive proposal.
It does not originate Canon, mint C01 governance authority, or dispatch C08 effects.

Dependency boundary:

`C01_GOVERNANCE -> C03_EXECUTIVE -> C08_EXECUTION`

## Typed candidate state

For candidate `x`, C03 consumes the tuple

`x = (id, plan, goal, p, r, i, c, h, condition, provenance)`

where:

- `p` is declared priority in `{0,...,100}`;
- `r` is a non-negative ordinal risk rank;
- `i` is a non-negative ordinal irreversibility rank;
- `c` is a finite non-negative resource-cost quantity in the request's declared cost unit;
- `h in {true,false}` is the hard-constraint gate;
- `condition` is an AMOS condition state;
- provenance is non-empty and identity-preserving.

No cross-unit arithmetic is performed. Risk and irreversibility ranks are ordinal policy inputs, not empirical probabilities.

## Admissibility

A candidate may enter executive ordering only when its hard gate passes and its condition is not stale, quarantined, or falsified.
Unknown request gaps are held. Competing evidence is preserved.

## Decision relation

For each admissible candidate define the lexicographic decision vector

`d(x) = (-p(x), r(x), i(x), c(x))`.

C03 selects `x*` only when there is a unique admissible candidate whose vector is lexicographically minimal.

If multiple admissible candidates share the minimal vector, C03 returns `HOLD_COMPETING`.

This is a **definition of the bounded AMOS executive policy**, not a theorem that this ordering is universally optimal.

## Hard invariants

1. Hard constraints dominate ranking.
2. `STALE -> REVALIDATE`, not `FALSE`.
3. `COMPETING` is preserved, not averaged away.
4. `UNKNOWN/GAP != PASS`.
5. No weighted score is fabricated when units/semantics differ.
6. Exact best-vector ties do not receive arbitrary ID-based authority.
7. `SELECT_PROPOSAL != C01_AUTHORIZATION`.
8. `SELECT_PROPOSAL != C08_EXECUTION`.
9. Every selected or competing candidate preserves provenance.
10. Schema and epoch drift fail closed.

## Executable binding

Reference runtime:

`04_RUNTIME/01_REFERENCE_IMPLEMENTATION/c03_executive_runtime.py`

Adversarial tests:

`04_RUNTIME/01_REFERENCE_IMPLEMENTATION/test_c03_executive_runtime.py`

The executable binding is `AMOS_MODEL / bounded reference`. Passing tests establish only the tested implementation properties; they do not promote this policy into SOURCE_CANON or an empirical law.

## Hard boundaries

```text
CONTRACT != CANON PROMOTION
IMPLEMENTED != UNIVERSALLY VALID
SELECTED != AUTHORIZED
AUTHORIZED != EXECUTED
UNKNOWN/GAP != PASS
```

[[25_COGNITIVE_MATRIX/00_INDEX/COGNITIVE_MATRIX_MOC|COGNITIVE_MATRIX_MOC]] · [[00_ROOT/00_ROOT_MOC|00_ROOT_MOC]] · [[00_ROOT/AMOS MOC|AMOS MOC]]
