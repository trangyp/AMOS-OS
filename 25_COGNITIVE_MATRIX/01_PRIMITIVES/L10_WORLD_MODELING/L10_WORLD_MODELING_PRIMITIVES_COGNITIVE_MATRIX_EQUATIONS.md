---
canon-group: cognition
canon-type: mathematical_contract
rscf-state: derived
rscf-provenance: AMOS_corpus_plus_reality_simulation_distinction
conclusion_class: AMOS_MODEL
epistemic_class: DERIVED
topic: L10 World Modeling Primitives Cognitive Matrix Equations
created: 2026-08-22
updated: 2026-09-14
origin_architect: Trang Phan
amos_core_target: v4.4
canonical_status: CONDITIONAL
---

# L10 — Equations and Formal Relations

**Package:** `L10_WORLD_MODELING`  
**Origin architect / steward:** **Trang Phan**

## 1. Typed representation state

Let:

- `O` be object identifiers;
- `C` representation classes;
- `V` variables;
- `S` scales;
- `T` time coordinates;
- `R` regimes;
- `B` observers;
- `P` provenance identifiers;
- `Q` validation states;
- `K` consequence classes.

A world-model coordinate is an element of the typed product:

```text
X in O x C x V x S x T x R x B x P x Q x K
```

The axes are not interchangeable.

## 2. Fidelity-envelope predicate

Let a fidelity envelope be:

```text
E = (V_E, R_E, T_E, M_E)
```

where `V_E`, `R_E`, `T_E`, and `M_E` are the validated sets of variables, regimes, time coordinates, and measurement methods.

For record `x`, define:

```text
Compatible_E(x)
iff
variable(x) in V_E
AND regime(x) in R_E
AND time(x) in T_E
AND method(x) in M_E
```

This typed predicate is preferred to intersecting heterogeneous domains as though they were one set.

## 3. Reality-contact predicate

Define the externally anchorable representation classes:

```text
C_external
= {OBSERVED_REALITY, MEASURED_PROXY, DEPLOYED_OUTCOME}
```

For record `x`:

```text
RealityContact_E(x)
iff
class(x) in C_external
AND ExternalObservationPresent(x)
AND MeasurementMethodKnown(x)
AND ProvenanceRecoverable(x)
AND Compatible_E(x)
```

This is an AMOS runtime gate, not a metaphysical definition of reality.

## 4. Commensurability predicate

For model record `m` and observation record `o`:

```text
Commensurate(m,o)
iff
object(m) = object(o)
AND variable(m) = variable(o)
AND unit(m) = unit(o)
AND time(m) = time(o)
AND regime(m) = regime(o)
```

A numeric discrepancy is not computed when the coordinates are not commensurate.

## 5. Absolute discrepancy

If `Commensurate(m,o)` and both values are real-valued, define:

```text
d_abs(m,o) := |value(m) - value(o)|
```

This has the same unit as the compared variable.

No dimensionless relative error is computed unless a denominator convention and zero-domain rule are separately declared.

## 6. Tolerance classification

For caller-declared tolerance `tau >= 0`:

```text
WithinTolerance(m,o,tau)
iff
d_abs(m,o) <= tau
```

and:

```text
ExceedsTolerance(m,o,tau)
iff
d_abs(m,o) > tau
```

`tau` is context-specific policy/model input. It is not a universal physical threshold.

## 7. Conservative provenance-independence gate

Let `root(x)` be the provenance root and `generator(x)` an optional generator identity.

The bounded runtime admits candidate independence only if:

```text
root(a) != root(b)
AND
(generator(a) is UNKNOWN
 OR generator(b) is UNKNOWN
 OR generator(a) != generator(b))
```

Passing this gate is necessary only for this simple runtime and is not sufficient proof of statistical, institutional, or physical independence.

## 8. Model-reality error state

For a model-like record `m` and externally anchored record `o`, the discrepancy state is defined only when:

```text
ModelLike(m)
AND RealityContact_E(o)
AND Commensurate(m,o)
AND Numeric(value(m))
AND Numeric(value(o))
```

Otherwise the result remains `UNKNOWN/GAP` rather than inventing a distance.

## 9. Cross-scale transform contract

For state spaces `X_s` and `X_t` at source and target scales, a scale transform is a typed function:

```text
F_(s->t) : X_s -> X_t
```

Its existence does not imply invertibility.

If an inverse is not proven, do not assert:

```text
F_(t->s)(F_(s->t)(x)) = x
```

Information loss, aggregation, and observer dependence must be declared when material.

## 10. Discrepancy as evidence

Let `M` be a model hypothesis and `o` an admissible observation. A mismatch:

```text
d_abs(M,o) > tau
```

may falsify or stale a dependent model claim only when that claim actually depends on the compared variable, regime, and tolerance contract.

It does not automatically invalidate unrelated model components.

## 11. Hard mathematical boundaries

```text
MODEL STATE != OBSERVATION
SIMULATION CONSISTENCY != EXTERNAL VALIDATION
DISTINCT FILES != INDEPENDENT EVIDENCE
CROSS-SCALE MAP != ISOMORPHISM
ABSOLUTE ERROR != CAUSAL EXPLANATION
UNKNOWN != ZERO
```

RSCF-NODE

```text
node_id: l10_primitives_equations
node_type: mathematical_contract
claim_class: AMOS_MODEL
rscf_state: DERIVED
canonical_status: CONDITIONAL
```

**MOC:** [[25_COGNITIVE_MATRIX/01_PRIMITIVES/L10_WORLD_MODELING/L10_WORLD_MODELING_MOC|L10_WORLD_MODELING_MOC]]
