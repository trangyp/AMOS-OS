---
title: URK / Core-19 Repair Overlay — 2026-09-14
origin_architect: Trang Phan
type: kernel_repair_overlay
status: ACTIVE_REPAIR_OVERLAY
conclusion_class: AMOS_MODEL
canonical_status: NOT_CANON_PROMOTION
amos_core_target: v4.4
created: 2026-09-14
---

# URK / Core-19 Repair Overlay — 2026-09-14

## Purpose

This overlay prevents stale or over-broad claims in historical Core-19/MURK artifacts from being consumed as current verified mathematics or executable semantics.

It preserves the historical files and their provenance. It does not rewrite history and it does not promote this overlay to Canon.

Origin architect / steward: **Trang Phan**.

## Applicability

This overlay applies when a runtime, agent, Skill, or human reader encounters a Core-19/MURK artifact that contains any of the following patterns without an explicit newer binding:

- a globally fixed `P02 = NonExistence` or `P02 = Distinction`;
- universal linear-time assumptions;
- 19×19 coordinate existence treated as complete semantic algebra;
- `[19, 19, 1E∞]` treated as standard tensor shape/cardinality;
- arbitrary topology/adjacency interpreted as causation;
- `Paradox(X) = X AND NOT X` as universal paradox semantics;
- `DualLogic(X) = X AND NOT X` as universal dual-logic semantics;
- `NLOGIC` normalization implemented only bottom-up;
- all eight ULK fragments described as locally executable without exact receipts.

## Current bounded repair semantics

### 1. Source/namespace separation

```text
URK_MATH != ULK_LOGIC
ULK_8_ALUS != ULMK_8_ATOMIC_UNITS
CORE19_SEMANTIC_19 != CORE19_EXECUTABLE_AST
SOURCE_CANON != IMPLEMENTATION_RECEIPT
```

These are distinction invariants, not arithmetic equations.

### 2. Core-19 coordinate space

Let `C` be the finite set of 19 Core-19 semantic positions.

The pair-coordinate set is the Cartesian product

```text
C × C
```

and therefore has cardinality

```text
|C × C| = |C|^2 = 19^2 = 361.
```

This establishes 361 coordinates only. It does not establish 361 laws, equations, or executable interactions.

### 3. P02 lineage

Cross-lineage P02 status is `COMPETING`.

Known candidates:

```text
historical lineage -> NonExistence
recovered lineage  -> Distinction
```

A local binding requires both namespace and version. No global winner is inferred from file freshness.

### 4. Four-valued evidence state

For bounded truth-status bookkeeping define

```text
V = {0,1} × {0,1}
```

where a state is `(t, f)` with `t` indicating support for truth and `f` support for falsity.

Negation is

```text
neg(t, f) = (f, t).
```

Hence

```text
neg(neg(v)) = v
```

for every `v` in `V`.

The information-order join is

```text
(t1, f1) join (t2, f2)
  = (t1 OR t2, f1 OR f2).
```

This supports distinct neither/true-only/false-only/both states without asserting that all AMOS non-classical logics reduce to this four-valued model.

### 5. Typed tensor repair

A valid runtime tensor interface uses explicit typed index sets. For example:

```text
T : Core19 × Core19 × Scale × Context × Regime -> Value.
```

`Scale`, `Context`, `Regime`, and `Value` must be supplied by the active model. The expression `1E∞` is retained only as historical source notation where provenance requires it; it is not a standard mathematical axis size.

### 6. Topology firewall

A relation edge or topological adjacency is not a causal edge by default.

Causal interpretation requires a separately typed causal semantic relation plus domain assumptions and evidence. No universal `path -> open set -> cause` implication is admitted by this overlay.

### 7. Rewrite precedence

For the implemented bounded unary fragment:

```text
NLOGIC(NLOGIC(x)) -> x
```

must be recognized **before** recursive child normalization.

Then strict subterms may be normalized. This preserves the intended bounded invariant

```text
Normalize(NLOGIC(NLOGIC(x))) = Normalize(x).
```

The implementation also checks

```text
Normalize(Normalize(x)) = Normalize(x)
```

for the implemented fragment.

### 8. Logic-fragment execution status

Current repair-surface status:

```text
ClassicalPropositional -> EXECUTABLE_BOUNDED
QuantumLogic           -> CANONICAL_BOUNDED_CLAIM_REBIND_PENDING
other canonical ULK fragments -> SPECIFICATION_ONLY here
```

This is an implementation-status statement, not a judgment about the conceptual importance of a fragment.

## Supersession scope

This overlay supersedes only the **active interpretation** of the listed stale claims for governed runtime use. It does not delete, rename, or erase the historical source artifacts.

In particular, `02_KERNEL/ABSOLUTE_LOGIC_KERNEL_19x19.md` remains preserved as a historical/source artifact, but the following statements in it must not be consumed as current verified mathematics without explicit revalidation:

- fixed cross-lineage P02;
- time is universally linear;
- complete 19×19 interaction semantics;
- `1E∞` tensor dimension;
- universal meta-logic priority claims;
- universal paradox/dual-logic contradiction semantics.

## Runtime binding

Executable bounded projection:

- `04_RUNTIME/01_REFERENCE_IMPLEMENTATION/core19_runtime.py`

Verifier:

- `04_RUNTIME/01_REFERENCE_IMPLEMENTATION/test_core19_runtime.py`

Candidate provenance:

- `01_CANON/07_PROVENANCE/URK_CORE19_REPAIR_CANDIDATE_2026-09-14.md`

## Promotion boundary

This overlay remains `AMOS_MODEL / ACTIVE_REPAIR_OVERLAY` until the canon authority separately resolves admission. Runtime success cannot self-promote a source or rule into Canon.
