---
canon-group: cognition
canon-type: mathematical_contract
rscf-state: derived
rscf-provenance: AMOS_corpus_plus_2026_09_14_URK_repair
conclusion_class: AMOS_MODEL
epistemic_class: DERIVED
topic: L09 Inference Primitives Cognitive Matrix Equations
created: 2026-08-22
updated: 2026-09-14
origin_architect: Trang Phan
amos_core_target: v4.4
canonical_status: CONDITIONAL
---

# L09 — Equations and Formal Relations

**Package:** `L09_INFERENCE`  
**Origin architect / steward:** **Trang Phan**

## 1. Type registry

Let:

- `C` be the finite Core-19 semantic-coordinate set.
- `K` be the set of admissible contexts.
- `R` be the set of admissible regimes.
- `S` be the set of scale indices.
- `V` be the value codomain selected by a bound model.
- `E` be the set of typed semantic interaction objects.
- `Q = (q_1,...,q_n)` be a finite list of classical propositional formulas when the bounded classical fragment is selected.

No equation below upgrades an `AMOS_MODEL` into an empirical law.

## 2. Finite coordinate identity

**ESTABLISHED_MATH / finite counting**

```text
|C| = 19
|C x C| = 19 * 19 = 361
```

This establishes 361 pair coordinates only. It does not establish 361 semantic laws.

## 3. Partial semantic interaction map

**AMOS_MODEL / typed definition**

```text
SemanticMap : C x C x K x R partial-> E
```

Equivalently, a coordinate can return no bound semantic object.

```text
SemanticMap(c_i, c_j, k, r) = UNBOUND
```

is a valid state and must not be coerced into `false`, `0`, or an invented rule.

## 4. Four-valued evidence state

**DEFINITION / AMOS_MODEL representation**

Let the evidence state be:

```text
T4 = {0,1} x {0,1}
```

where the first component records support-for-true and the second support-for-false.

Negation is defined by channel exchange:

```text
neg4(a,b) := (b,a)
```

Therefore:

```text
neg4(neg4(x)) = x
```

for every `x in T4`.

The information-order join is defined componentwise:

```text
join4((a,b),(c,d)) := (a OR c, b OR d)
```

and the information order is:

```text
(a,b) <=_info (c,d)
iff
(a <= c) AND (b <= d)
```

with Boolean order `0 <= 1`.

## 5. Repaired unary normalization

**AMOS_MODEL with executed bounded evidence**

Let `N` be the repaired normalizer over the bounded grammar:

```text
Expr ::= ATOM | NOT(Expr) | NLOGIC(Expr)
```

The double-NLOGIC rule is applied before recursive child normalization. The required invariants are:

```text
N(NLOGIC(NLOGIC(x))) = N(x)
```

and:

```text
N(N(x)) = N(x)
```

The staged repair has executable regression/property evidence for this bounded grammar. These equations are not claims about every future ULK fragment.

## 6. Global consistency

**DEFINITION / bounded classical fragment**

For a finite premise list `Q`:

```text
GloballyConsistent(Q)
:= SAT(q_1 AND ... AND q_n)
```

Pairwise compatibility is:

```text
PairwiseCompatible(Q)
:= for every i < j, SAT(q_i AND q_j)
```

The implication:

```text
PairwiseCompatible(Q) -> GloballyConsistent(Q)
```

is false in general.

Executed counterexample:

```text
Q = {A, B, NOT(A AND B)}
```

Every pair is satisfiable while the conjunction of all three formulas is not.

## 7. Bounded classical entailment

**ESTABLISHED_LOGICAL_EQUIVALENCE within the declared propositional semantics**

For premise set `P` and conclusion `q`:

```text
P entails q
iff
NOT SAT((AND P) AND NOT(q))
```

L09 uses this equivalence only when the selected fragment has `EXECUTABLE_BOUNDED` status and the atom bound is satisfied.

`entails` here is formal entailment. It is not empirical truth and does not establish causation.

## 8. RSCF confidence ceiling

**AMOS_MODEL / conjunctive necessary-premise rule**

For a conclusion `C0` whose declared necessary premises are `P_1,...,P_n`, with confidence values in `[0,1]`:

```text
Conf(C0) <= min_i Conf(P_i)
```

This is a confidence ceiling for this dependency structure. It is not a universal Bayesian aggregation formula.

If any required confidence is unknown, the executable L09 reference leaves the derived ceiling unknown rather than inventing a number.

## 9. URK tensor coordinate contract

**AMOS_MODEL / typed representation**

```text
URKTensor : C x C x S x K x R -> V
```

The row, column, scale, context, and regime axes are typed and non-interchangeable.

The earlier notation `[19,19,"1E∞"]` is not used as a standard mathematical tensor shape.

## 10. Logic-fragment implementation map

**DERIVED runtime-status function**

```text
Impl(ClassicalPropositional)
= EXECUTABLE_BOUNDED

Impl(QuantumLogic)
= CANONICAL_BOUNDED_CLAIM_REBIND_PENDING

Impl(f)
= SPECIFICATION_ONLY
```

for the other six canonical ULK fragments in this repair surface.

This status map is versioned runtime evidence, not a claim about all AMOS artifacts everywhere.

## 11. Source-scoped rewrite warning

Historical executable snapshots contain rewrites such as `PARADOX(X)` or `DLOGIC(X)` to a classical contradiction form. These remain `SOURCE_DEFINED` behavior for those snapshots.

They are not admitted here as universal definitions of Paradox or DualLogic.

## 12. Hard mathematical boundaries

```text
361 COORDINATES != 361 PROVEN EQUATIONS
PARTIAL MAP != TOTAL ALGEBRA
FORMAL ENTAILMENT != CAUSATION
SOURCE REWRITE != UNIVERSAL SEMANTICS
MODEL EQUATION != EMPIRICAL LAW
UNKNOWN != ZERO
```

RSCF-NODE

```text
node_id: l09_primitives_equations
node_type: mathematical_contract
claim_class: AMOS_MODEL
rscf_state: DERIVED
canonical_status: CONDITIONAL
```

**MOC:** [[25_COGNITIVE_MATRIX/01_PRIMITIVES/L09_INFERENCE/L09_INFERENCE_MOC|L09_INFERENCE_MOC]]
