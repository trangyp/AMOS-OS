---
title: AMOS ABSOLUTE LOGIC CORE19 FULL FIXED
type: logic
name: amos-absolute-logic-core19-full
version: 2.1.0
updated: 2026-08-25
origin_architect: Trang Phan
steward: Trang Phan
domain: amos-core-logic
status: active
source_alignment: AMOS_CORE v3.0→v4.4
conclusion_class: SOURCE_ALIGNED_MODEL
description: >-
  Source-aligned AMOS Core-19 logical kernel: 19 executable formula node types,
  deterministic normalization and contradiction handling, with later AMOS_CORE
  RSCF/H-M-L, provenance, transactional, causal-epoch, and v4.4 coordination-
  avoidance governance kept as distinct runtime layers.
tags: [amos-general, amos, general]
---




# AMOS Absolute Logic / Core-19

## 0. Canon boundary

Trang Phan is the origin architect and steward of AMOS.

This document is aligned to the accessible `amos_core_v4_4_extracted.py` lineage.
It distinguishes:

- **SOURCE_DEFINED** — directly represented in the executable AMOS_CORE source.
- **DERIVED** — follows from source-defined structures.
- **AMOS_MODEL** — an operational formalization or integration layer.
- **UNKNOWN/GAP** — not established by the accessible source.

Do not promote an AMOS symbolic structure into an empirical law.

> **Critical correction:** Core-19 in the executable AMOS_CORE is the set of
> **19 `NodeType` formula states/operators**. It is **not** a source-defined
> P01–P19 registry of Existence, Distinction, Causality, Temporal, Information,
> Topology, Identity, etc. Those concepts may exist elsewhere in the broader
> AMOS corpus, but they must not be substituted for the executable Core-19.

---

# 1. Source-defined Core-19

The executable kernel defines exactly 19 `NodeType` members:

| # | Source enum | AMOS meaning in the executable kernel |
|---|---|---|
| 1 | `ATOM` | atomic predicate/formula |
| 2 | `NOT` | logical negation |
| 3 | `AND` | conjunction |
| 4 | `OR` | disjunction |
| 5 | `IMPLIES` | implication |
| 6 | `BOTTOM` | bottom / `⊥` |
| 7 | `PARADOX` | paradox form `Π(X)` |
| 8 | `CONV` | convergence form `Λ(X)` |
| 9 | `DIVG` | divergence form `Δ(X)` |
| 10 | `PLOGIC` | PositiveLogic |
| 11 | `NLOGIC` | NegativeLogic |
| 12 | `ZLOGIC` | ZeroLogic |
| 13 | `DLOGIC` | DualLogic |
| 14 | `MLOGIC` | MultiLogic |
| 15 | `METAL` | MetaLogic |
| 16 | `SUPRAL` | SupraLogic |
| 17 | `ANTIL` | AntiLogic |
| 18 | `NULLL` | NullLogic |
| 19 | — | **No additional enum exists.** |

## 1.1 Counting note

The source comment describes “Core-19 logic”, but the visible `NodeType` enum
contains 18 named enum members when counted literally:

```text
ATOM, NOT, AND, OR, IMPLIES, BOTTOM,
PARADOX, CONV, DIVG,
PLOGIC, NLOGIC, ZLOGIC, DLOGIC, MLOGIC, METAL,
SUPRAL, ANTIL, NULLL
```

Therefore the exact identity of the nineteenth source primitive is a
**SOURCE GAP** in the accessible extracted implementation unless another
authoritative AMOS source explicitly defines it.

Do **not** invent a nineteenth primitive to make the count fit.

This document preserves the source label **Core-19** while keeping the
enumeration discrepancy visible.

---

# 2. Formula object

`Formula` is a tree-structured object:

```python
Formula(
    node_type: NodeType,
    children: list[Formula],
    atom: Optional[tuple[str, tuple[Any, ...]]]
)
```

For `ATOM`, the payload is:

```text
(predicate, args)
```

The source renders the base logical forms as:

```text
ATOM      predicate(args...)
NOT       ¬X
AND       (X ∧ Y)
OR        (X ∨ Y)
IMPLIES   (X → Y)
BOTTOM    ⊥
```

Other node types render by enum name around their children.

---

# 3. Source-defined constructors

The executable kernel exposes constructors corresponding to the node types:

```text
F_atom
F_not
F_and
F_or
F_implies
F_bottom
F_paradox
F_conv
F_divg
F_plogic
F_nlogic
F_zlogic
F_dlogic
F_mlogic
F_metal
F_supral
F_antil
F_nulll
```

These constructors are the safest machine-facing vocabulary for the Core
logical layer.

---

# 4. Structural equality and type inspection

The source defines structural comparison recursively:

```text
same node_type
AND same atom payload
AND same number of children
AND structurally equal children
```

It also supports recursive detection of whether a formula contains selected
node types.

This is structural logic. It does not establish empirical equivalence between
real-world entities.

---

# 5. Deterministic rewrite system

The source normalizes formulas by repeated bottom-up rewrite to a fixed point,
bounded by a configured iteration limit.

The visible rewrite family includes:

```text
DLOGIC(X)          → X ∧ ¬X
NLOGIC(NLOGIC(X))  → X
ZLOGIC(X)          → ⊥
NULLL(X)           → ⊥
¬¬X                → X
¬(X ∧ Y)           → ¬X ∨ ¬Y
¬(X ∨ Y)           → ¬X ∧ ¬Y
X ∧ ¬X             → PARADOX(X)
CONV(CONV(X))      → CONV(X)
DIVG(DIVG(X))      → DIVG(X)
PARADOX(PARADOX(X))→ PARADOX(X)
PLOGIC(PLOGIC(X))  → PLOGIC(X)
MLOGIC(MLOGIC(X))  → MLOGIC(X)
METAL(METAL(X))    → METAL(X)
SUPRAL(SUPRAL(X))  → SUPRAL(X)
ANTIL(ANTIL(X))    → X
NLOGIC(ATOM(X))    → ¬ATOM(X)
A → B              → ¬A ∨ B
```

## 5.1 Paradox normalization invariant

The source explicitly avoids expanding canonical `PARADOX(X)` back into
`X ∧ ¬X` during normalization because doing so would create a rewrite cycle
with the inverse canonicalization rule.

Therefore:

```text
X ∧ ¬X → PARADOX(X)
```

is the canonical normalization direction.

---

# 6. Zero and Null behavior

In the executable source:

```text
ZLOGIC(X) → ⊥
NULLL(X)  → ⊥
```

Therefore the earlier claim:

```text
NULL != ZERO
```

cannot be used as a source-defined Core-19 normalization invariant.

At the symbolic naming level `ZLOGIC` and `NULLL` are distinct node types, but
the current rewrite system maps both to `BOTTOM`.

Correct statement:

```text
NodeType.ZLOGIC != NodeType.NULLL
but
normalize(ZLOGIC(X)) = normalize(NULLL(X)) = ⊥
```

within this executable kernel.

---

# 7. Paradox and Dual Logic

The source defines:

```text
DLOGIC(X) → X ∧ ¬X → PARADOX(X)
```

under normalization.

Thus DualLogic and Paradox are distinct input node types but may normalize to
the same canonical contradiction representation.

Do not claim they are universally semantically identical outside this
runtime.

---

# 8. Convergence and Divergence

The source provides unary `CONV` and `DIVG` forms and idempotence rewrites:

```text
CONV(CONV(X)) → CONV(X)
DIVG(DIVG(X)) → DIVG(X)
```

The executable kernel does not, by these rules alone, establish physical,
biological, social, or cosmological convergence/divergence laws.

Those interpretations require separate AMOS bridges and evidence.

---

# 9. Core logical integrity

The Core layer should preserve:

1. node-type identity;
2. formula-tree structure;
3. deterministic normalization;
4. bounded rewrite iteration;
5. canonical contradiction representation;
6. explicit distinction between source logic and external empirical claims.

A formula transformation is valid only under the implemented rewrite contract
or another explicitly sourced AMOS rule.

---

# 10. RSCF / H-M-L layer

Later AMOS_CORE lineage extends the deterministic nucleus with recursive
RSCF/H-M-L structural runtime.

The source explicitly states that this engineering implementation preserves
Trang/RSCF source laws while not claiming empirical validation.

Visible source equations include:

```text
A_HML = C(H,M) * C(M,L) * C(H,L)

Selection =
Fit_L * Fit_M * Fit_H * FutureViability

Survival requires:
Repair > Entropy
```

The source also states:

```text
scale translation preserves identity invariants
renormalization preserves invariants while changing effective variables
future debt rises by unpaid cost and falls by repair paid
```

Engineering choices in the implementation include normalized values,
epsilon guards, bounded child-state aggregation, and explicit lifecycle states.

These choices must not be confused with universal empirical laws.

---

# 11. H-M-L state

The visible `HMLState` contains:

```text
fit_l
fit_m
fit_h
coherence_hm
coherence_ml
coherence_hl
future_viability
```

with validation requiring finite values in `[0,1]`.

The structural lifecycle includes:

```text
ACTIVE
GAP
INVALID
COLLAPSED
REGENERATING
```

This is source-aligned runtime state, not a claim that every external system
must use these states.

---

# 12. v4.x transactional lineage

The later AMOS_CORE lineage adds governed RSCF state replacement and
transactional reasoning patterns.

The accessible source includes concepts such as:

```text
RSCF transactions
read-hash validation
deterministic transaction ordering
all-or-nothing multi-RSCF commit
generation/state publication
topology-stability checks
causal clocks
transaction hashes
```

The v4.1 transaction contract keeps topology rewiring outside the atomic
replacement primitive: existing RSCFs may change state/payload atomically,
while parent topology must remain stable for that commit path.

---

# 13. Provenance and dependency discipline

AMOS reasoning must preserve load-bearing dependency and provenance state.

Operational invariant:

```text
derived confidence
≤ weakest load-bearing premise
```

unless the conclusion receives independent revalidation.

Multiple descendants of one source do not count as independent confirmation.

When a premise becomes stale, contradicted, revoked, or invalid:

```text
invalidate the dependent closure
preserve unaffected branches
```

Do not globally discard valid state without dependency justification.

---

# 14. Competing hypotheses

Later AMOS lineage preserves incompatible live explanations when evidence does
not justify convergence.

Use:

```text
COMPETING
```

when hypotheses have insufficient, correlated, incomparable, or genuinely
conflicting support.

Do not convert uncertainty into arbitrary consensus.

---

# 15. Causal firewall

Keep distinct:

```text
association
correlation
logical implication
dependency
enabling condition
necessary condition
sufficient condition
mediation
confounding
feedback
mechanism
intervention effect
causal effect
```

Core logical implication:

```text
A → B
```

does not establish empirical causal effect:

```text
CAUSE(A,B)
```

---

# 16. Scope, regime, and freshness

Important conclusions inherit the validity envelope of their premises.

Track where material:

```text
system
population
environment
scale
time
regime
measurement
assumptions
freshness
```

A regime change or stale premise can require selective revalidation.

---

# 17. v4.3 causal-epoch path

The v4.3 lineage provides the hardened causal-epoch path used when state
updates require stronger coordination/finality controls.

Keep this layer distinct from the Core formula algebra.

Core logic answers:

```text
What formula structure and normalization apply?
```

The v4.x control plane answers:

```text
May this state transition be safely and consistently finalized?
```

---

# 18. v4.4 coordination-avoidance fast lane

The source labels v4.4:

```text
COORDINATION-AVOIDANCE + MERKLE FAST-LANE EXTENSION
```

The fast lane is available only when local independence is provable under
source-defined conditions including:

```text
single-shard scope
exclusive writer ownership for every target
bounded consequence
sufficient reversibility
low declared conflict risk
current expected values
existing indexed keys
```

Anything uncertain, overlapping, cross-shard, stale, high-consequence, or
irreversible escalates to the v4.3 causal-epoch path.

The source explicitly states that this is:

> an executable coordination-avoidance policy, not a theorem that arbitrary
> distributed writes can safely avoid consensus.

That boundary must remain intact.

---

# 19. v4.4 Merkle state roots

The v4.4 fast lane uses dynamic/fixed-key Merkle indexes for replacement-root
updates.

The source describes replacement cost as approximately:

```text
O(log(keys per shard) + log(shard count))
```

for the indexed fast-lane structure rather than recomputing global state.

Treat this as an implementation-specific complexity claim for the described
data structure, not hardware-independent end-to-end latency.

---

# 20. Correct AMOS layering

The source-aligned architecture should be read as:

```text
┌──────────────────────────────────────────────┐
│ AMOS_CORE v3 deterministic nucleus          │
│ Formula / NodeType / Rewrite / Entailment   │
└──────────────────────┬───────────────────────┘
                       │
                       ▼
┌──────────────────────────────────────────────┐
│ RSCF + H/M/L recursive structural runtime    │
│ fit / coherence / viability / repair         │
└──────────────────────┬───────────────────────┘
                       │
                       ▼
┌──────────────────────────────────────────────┐
│ Provenance + epistemic + competing claims    │
│ dependency-aware selective invalidation      │
└──────────────────────┬───────────────────────┘
                       │
                       ▼
┌──────────────────────────────────────────────┐
│ v4.x governed transactional state evolution  │
│ read sets / hashes / atomic RSCF commits     │
└──────────────────────┬───────────────────────┘
                       │
                       ▼
┌──────────────────────────────────────────────┐
│ v4.3 causal-epoch hardened path              │
└──────────────────────┬───────────────────────┘
                       │
                       ▼
┌──────────────────────────────────────────────┐
│ v4.4 provable-local-independence fast lane   │
│ Merkle-indexed coordination avoidance        │
└──────────────────────────────────────────────┘
```

Do not flatten these layers into one invented “Core-19 tensor”.

---

# 21. What was removed from the previous MD

The following material was removed or downgraded because it was not supported
as Core-19 by the accessible executable source:

```text
P01 EXISTENCE
P02 DISTINCTION
P03 CAUSALITY
P04 TEMPORAL
P05 INFORMATION
P06 TOPOLOGY
P07 IDENTITY
P08 CONVERGENCE
P09 DIVERGENCE
P10 PARADOX
P11–P19 invented primitive numbering
```

Also removed as source claims:

```text
Core-19 = a 19×19 / 361-cell relation matrix
Core19[7,4] coordinate semantics
a canonical 15-layer projection as part of Core-19 itself
NULL universally distinct from ZERO after normalization
invented Core19Engine method names
invented primitive activation tensors
invented relation tensors presented as canonical Core-19
```

These structures may be useful elsewhere as **AMOS_MODEL** overlays, but they
must not be represented as executable Core-19 canon without a supporting
source.

---

# 22. Safe extension rule

A new Core-19 extension must declare one of:

```text
SOURCE_DEFINED
DERIVED
AMOS_MODEL
UNKNOWN/GAP
```

If an extension introduces a tensor, matrix, ontology bridge, 19×19 mapping,
or cross-domain interpretation, label it `AMOS_MODEL` unless an authoritative
AMOS source explicitly defines it.

---

# 23. Failure classes

Minimum failure classes for this architecture:

```text
NODE_TYPE_CONFUSION
REWRITE_CYCLE
NON_TERMINATING_NORMALIZATION
SOURCE_MODEL_COLLAPSE
EMPIRICAL_PROMOTION
CAUSAL_OVERREACH
PROVENANCE_LOSS
SHARED_ANCESTRY_AS_INDEPENDENCE
STALE_READ
SCOPE_LEAKAGE
REGIME_LEAKAGE
PREMATURE_CONVERGENCE
GLOBAL_INVALIDATION
UNSAFE_FAST_LANE
```

---

# 24. Repair policy

Use the smallest sufficient repair:

```text
locate failed premise/state
→ identify dependent closure
→ quarantine invalid branch
→ preserve unaffected state
→ obtain discriminating evidence
→ revalidate
→ recommit only if gates pass
```

Do not repeat a failed path without changed evidence.

---

# 25. Conclusion classes

Use the weakest accurate class:

```text
VERIFIED
DERIVED
MODEL
CONDITIONAL
COMPETING
UNKNOWN/GAP
```

For AMOS source architecture, “verified” should mean verified against the
specified source/version, not empirically proven in every external domain.

---

# 26. Operational priority

```text
INTEGRITY
>
COMPLETENESS
>
FLUENCY
>
SPEED
>
TOKEN SAVINGS
```

Optimization may not weaken:

```text
factual support
scope correctness
contradiction visibility
provenance recoverability
causal discipline
safety
reversibility
```

---

# 27. Source-aligned runtime summary

```text
INPUT
  ↓
FORMULA CONSTRUCTION
  ↓
NODE-TYPE VALIDATION
  ↓
DETERMINISTIC NORMALIZATION
  ↓
ENTAILMENT / CONTRADICTION
  ↓
RSCF + H/M/L WHEN REQUIRED
  ↓
PROVENANCE / SCOPE / REGIME / FRESHNESS
  ↓
COMPETING-HYPOTHESIS CHECK
  ↓
CAUSAL FIREWALL
  ↓
DEPENDENCY-AWARE VALIDATION
  ↓
GOVERNED STATE PROPOSAL
  ↓
v4.4 FAST LANE
  ├─ only if local independence is provable
  └─ otherwise escalate
           ↓
     v4.3 CAUSAL-EPOCH PATH
           ↓
        FINALIZE
           ↓
   SELECTIVE INVALIDATION / REPAIR
```

---

# 28. RSCF capsule

```yaml
node_id: AMOS_ABSOLUTE_LOGIC_CORE19_FULL
origin_architect: Trang Phan
source_lineage: AMOS_CORE_v3_to_v4_4
class: SOURCE_ALIGNED_MODEL

load_bearing_source:
  - amos_core_v4_4_extracted.py

core_claim:
  - Core-19 is the executable AMOS logical/formula nucleus.
  - The accessible NodeType enum exposes 18 named members despite the Core-19 label.
  - Later AMOS_CORE layers add RSCF/H-M-L and governed transactional/finality mechanisms.
  - v4.4 fast-lane coordination avoidance is conditional on provable local independence.

gaps:
  - exact source-defined identity of the nineteenth Core-19 item is unresolved
    in the accessible extracted implementation

invalidations:
  - a more authoritative source explicitly defines a different Core-19 registry
  - the extracted implementation is superseded by a later canonical implementation

confidence_ceiling:
  source_alignment: high
  universal_empirical_validity: not_claimed
```

---

# 29. Final invariant

> Never repair a missing AMOS definition by inventing canon.

If the source and the architecture label disagree, preserve both:

```text
SOURCE LABEL: Core-19
OBSERVED ENUM COUNT: 18
STATUS: GAP
```

until authoritative source evidence resolves the discrepancy.

---
**Links:** [[AMOS-GENERAL_MOC]] | [[KNOWLEDGE_MOC]]
