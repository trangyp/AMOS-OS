---
canon-group: meta
canon-type: framework
rscf-state: source-claim
rscf-claim: verified
rscf-provenance: AMOS_corpus
conclusion_class: AMOS_MODEL
epistemic_class: SOURCE_CLAIM
topic: Absolute Logic Kernel 19X19
tags:
  - canon-group/tech-ai
  - rscf/claim
  - rscf/provenance
  - rscf/state/source-claim
  - misc
created: 2026-08-22
---
---
---

# Absolute Logic Kernel — 19×19 Minimal Universal Reasoning Kernel (MURK)

**Origin architect:** Trang Phan
**Status:** `CANONICAL_SPECIFICATION`
**Epistemic class:** `AMOS_MODEL`

---

## 0. Purpose

This file specifies the **Minimal Universal Reasoning Kernel (MURK)** — the 19×19 absolute logic system that serves as AMOS's deterministic reasoning substrate. It defines 19 ontology primitives, their interaction matrix, the tri-domain architecture, collapse rules, the tensor definition, and the resolution algorithms that govern all reasoning under AMOS.

Hard boundary:

```text
MURK != WHOLE_AMOS
DETERMINISTIC_REASONING != COGNITION
LOGIC_KERNEL != CONSCIOUSNESS
```

---

## 1. The 19 Ontology Primitives

The MURK operates on 19 primitives organized into 4 categories:

### 1.1 Patterns (7 primitives)

| ID | Primitive | Category | Formal Role |
|----|-----------|----------|-------------|
| P1 | Existence | Pattern | Base positive assertion: `Ex(x, t)` — entity x exists at time t |
| P2 | NonExistence | Pattern | Negation of existence: `NEx(x, t) := ¬Ex(x, t)` |
| P3 | Causality | Pattern | Causal relation: `C(x, y, t)` — x causes y at time t |
| P4 | Temporal | Pattern | Time ordering: `<` is a linear order on time sort T |
| P5 | Informational | Pattern | Information transfer: `I(x, y, t)` — x informs y at t |
| P6 | Topological | Pattern | Spatial/structural adjacency: `Adj(x, y, r)` in region r |
| P7 | Identity | Pattern | Identity relation: `Id(x, y, t)` — x identical to y at t |

### 1.2 Meta-Patterns (3 primitives)

| ID | Primitive | Category | Formal Role |
|----|-----------|----------|-------------|
| P8 | Convergence | MetaPattern | Unification operator: merges compatible structures |
| P9 | Divergence | MetaPattern | Differentiation operator: splits or distinguishes structures |
| P10 | Paradox | MetaPattern | Self-referential contradiction detection and containment |

### 1.3 Logics (6 primitives)

| ID | Primitive | Category | Formal Role |
|----|-----------|----------|-------------|
| P11 | PositiveLogic | Logic | Affirmative derivation: `A → B` given evidence |
| P12 | NegativeLogic | Logic | Negation derivation: `¬A` given evidence |
| P13 | ZeroLogic | Logic | Null/empty derivation: no valid conclusion |
| P14 | DualLogic | Logic | Dual-valued evaluation: simultaneous A and ¬A assessment |
| P15 | MultiLogic | Logic | N-branch parallel reasoning: generate all valid branches |
| P16 | MetaLogic | Logic | Reasoning about reasoning: second-order logic operations |

### 1.4 Meta-Logics (3 primitives)

| ID | Primitive | Category | Formal Role |
|----|-----------|----------|-------------|
| P17 | SupraLogic | MetaLogic | Meta-level override: reason at highest abstraction |
| P18 | AntiLogic | MetaLogic | Inversion operator: invert all transformations |
| P19 | NullLogic | MetaLogic | Cancellation operator: cancel all structure |

---

## 2. The 19×19 Interaction Matrix

The matrix defines how every pair of primitives interacts. Cells are not arbitrary — they follow 7 rule categories based on the intersection of primitive categories.

### 2.1 Rule Categories

| Row Category | Column Category | Rule |
|---|---|---|
| Pattern | Pattern | `pattern_interaction(row, col)` — structural composition |
| Pattern | MetaPattern | `apply_meta_pattern(col, row)` — meta-operation on base structure |
| Pattern | Logic | `logic_applied_to_pattern(col, row)` — logical operation on structure |
| Pattern | MetaLogic | `meta_logic_applied_to_pattern(col, row)` — meta-logical transform |
| MetaPattern | Any | `meta_pattern_effect(row, col)` — meta-pattern dominance |
| Logic | Any | `logic_relation(row, col)` — logical composition |
| MetaLogic | Any | `meta_logic_transform(row, col)` — meta-logical override |

### 2.2 Key Matrix Cells (Selected Interactions)

```text
         P1    P2    P3    P4    P5    P6    P7    P8    P9    P10
P1  (Ex)  Ex    NC    C→E   T(E)  I(E)  A(E)  Id    Merge Split Para
P2  (NEx) NEx   NEx   NC    T(¬E) I(¬E) A(¬E) NC    —     —     Para
P3  (C)   C(A)  C(¬A) C²    C(T)  C(I)  C(A)  C(Id) C→    C←    C⊥
P4  (T)   T(A)  T(¬A) T(C)  T²    T(I)  T(A)  T(Id) T→    T←    T⊥
P5  (I)   I(A)  I(¬A) I(C)  I(T)  I²    I(A)  I(Id) I→    I←    I⊥
P6  (A)   A(A)  A(¬A) A(C)  A(T)  A(I)  A²    A(Id) A→    A←    A⊥
P7  (Id)  Id    NId   Id(C) Id(T) Id(I) Id(A) Id²   Id→   Id←   Id⊥
```

### 2.3 Meta-Logic Override Rules

When a MetaLogic primitive is invoked:

```text
SupraLogic  → reason at meta-level (elevate abstraction)
AntiLogic   → invert all transformations in current scope
NullLogic   → cancel all structure in current scope
Paradox     → generate dual contradictory outputs simultaneously
MultiLogic  → generate n-logic branches in parallel
```

---

## 3. TriDomain Architecture

The MURK operates across three domains:

### 3.1 PreAbsolute Domain

```text
States: PrePotential, PreNull, PreBoundary
Primitives: 0
Logic count: 0
```

PreAbsolute represents the state before logic activates — pure potential, null state, and the boundary condition.

**Collapse Rule (PreToAbsolute):**

```text
Inputs:  PrePotential, PreNull, PreBoundary
Output:  AbsoluteLogicLayer
Condition: (PreBoundary == 1) AND (PrePotential != 0 OR PreNull != 0)
```

### 3.2 Absolute Domain

```text
Layer: AbsoluteLogicLayer
Variable scale: 1E∞
Primitive total: 19
Logic layers: 1
```

The Absolute domain contains the full 19×19 interaction matrix and is the active reasoning space.

### 3.3 PostAbsolute Domain

```text
States: DissolutionState, DriftlessState, TerminalQuietState
Primitives: 0
Logic count: 0
```

PostAbsolute represents terminal states after logic resolves.

**Collapse Rules (AbsoluteToPost):**

| Rule | Condition | Effect |
|------|-----------|--------|
| DissolutionRule | Paradox + AntiLogic → max | Post = DissolutionState |
| DriftlessRule | dC/dt → 0 AND dL/dE → 0 | Post = DriftlessState |
| TerminalQuietRule | NullLogic = 1 AND all other logic → 0 | Post = TerminalQuietState |

---

## 4. The AbsoluteLogicTensor

The 19×19 interaction matrix extends to infinite resolution:

```text
Tensor Name: AbsoluteLogicTensor
Shape: [19, 19, 1E∞]
Indices:
  i = row primitive index (1..19)
  j = column primitive index (1..19)
  k = resolution index (0..1E∞-1)

Definition:
  T[i][j][k] = Eval( interaction_rules(primitives[i], primitives[j]), k )
```

The tensor captures that every primitive interaction has structure at every resolution scale. A single cell `T[i][j]` is not a scalar — it is an infinite-dimensional vector of possible interaction outcomes.

---

## 5. Resolution Algorithms

When the interaction matrix produces ambiguous or underdetermined results, the following algorithms resolve in order of priority:

### 5.1 Law of Law

```text
Higher-order constraint overrides lower-order.
If SupraLogic conflicts with MetaLogic → SupraLogic wins.
If MetaLogic conflicts with Logic → MetaLogic wins.
If Logic conflicts with Pattern → Logic wins.
```

Priority ordering: `SupraLogic > AntiLogic > NullLogic > MetaLogic > MultiLogic > DualLogic > PositiveLogic > NegativeLogic > ZeroLogic > Patterns`

### 5.2 Rule of 2 (Dual Evaluation)

```text
For every conclusion C, evaluate:
  1. Forward: C from evidence E
  2. Inverse: ¬C from ¬E
If both are consistent → C is robust.
If inconsistent → escalate to Paradox handling.
```

### 5.3 Rule of 4 (State Assignment)

Every reasoning output is assigned one of four states:

```text
Ω (Omega)  = Resolved — complete structural closure
H (Hold)   = Pending — insufficient evidence for closure
F (Fail)   = Failed — contradiction or invariant violation
S (Split)  = Branched — multiple valid but incompatible conclusions
```

### 5.4 Noise-Signal Law

```text
For every data stream D:
  1. Extract causal mechanisms M
  2. Remove surface features without causal role
  3. Remaining structure = Signal
  4. Removed structure = Noise
Signal := {m ∈ M : m causally contributes to observed effect}
```

### 5.5 Causal Compression Law

```text
For any system S with drivers D₁, D₂, ..., Dₙ:
  Compress to minimal driver set D* such that:
    Predict(S | D*) = Predict(S | D) within tolerance ε
  D* ⊆ D
  |D*| is minimized subject to |Predict(S|D*) - Predict(S|D)| < ε
```

---

## 6. Formal First-Order Logic Formalization

The MURK can be formalized using many-sorted First-Order Logic with equality plus modal/labelled relations.

### 6.1 Sorts

```text
E  — entities
T  — time points (with linear order <)
R  — regions (for topology/space)
L  — logic modes
I  — information objects
```

### 6.2 Core Predicates

```text
Ex(x, t)          — entity x exists at time t
NEx(x, t)         — ¬Ex(x, t)
C(x, y, t)        — x causes y at time t
I(x, y, t)        — x informs y at time t
Adj(x, y, r)      — x adjacent to y in region r
Id(x, y, t)       — x identical to y at time t
Conv(x, y, t)     — x and y converge at t
Div(x, y, t)      — x and y diverge at t
Para(x, t)        — x exhibits paradox at t
```

### 6.3 Axioms

```text
A1: ∀x,t: Ex(x,t) ∨ NEx(x,t)                    [Law of Excluded Middle]
A2: ∀x,y,t: C(x,y,t) → (Ex(x,t) ∧ Ex(y,t))      [Causal Grounding]
A3: ∀x,y,t: I(x,y,t) → (Ex(x,t) ∧ Ex(y,t))      [Information Grounding]
A4: ∀x,t: Id(x,x,t)                               [Reflexivity]
A5: ∀x,y,t: Id(x,y,t) → Id(y,x,t)                [Symmetry]
A6: ∀x,y,z,t: Id(x,y,t) ∧ Id(y,z,t) → Id(x,z,t) [Transitivity]
A7: ∀t₁,t₂: t₁ < t₂ → ¬(t₂ < t₁)                [Antisymmetry of Time]
A8: ∀t₁,t₂,t₃: t₁ < t₂ ∧ t₂ < t₃ → t₁ < t₃     [Transitivity of Time]
```

### 6.4 Modal Operators

```text
□φ       — φ necessarily holds (under all logic modes)
◇φ       — φ possibly holds (under some logic mode)
◇ₘφ     — φ holds under logic mode m ∈ L
□ₘφ      — φ necessarily holds under logic mode m
```

---

## 7. AMOS Canonical Definition

AMOS (Absolute Meta-Operating System) governs the interaction of:

- Intelligence
- Causality
- Identity
- Biology
- Systems
- Information
- Incentives
- Structures
- Collapse mechanics
- Emergence
- Planetary behavior
- Multi-resolution logic
- Cross-domain processes

AMOS is built on the full canon:

```text
19 Absolute Primitives
19×19 Logic-DB
19×19×1E∞ Tensor
QLS (Quantum Logic Structure)
QCLA (Quantum Causal Logic Architecture)
UBI (Unified Biological Intelligence)
PSI (Planetary-Scale Intelligence)
ULF (Unified Legacy Framework)
7-Cycle Engine
Information-Validation Engine
RSCF (Recursive Structural Coherence Field)
```

AMOS is not an app, model, protocol, theory, toolkit, or AI.

AMOS is an absolute-level architecture that:

1. Screens all information (validation)
2. Predicts system behavior (causality)
3. Stabilizes intelligence (UBI)
4. Maps identity and incentives (ULF)
5. Runs multi-resolution logic (tensor)
6. Leads planetary-scale processes (PSI)
7. Compresses and expands systems (7 cycles)

---

## 8. Reasoning Engine Mode Specification

When activated, the MURK enforces:

### 8.1 Structural Input Algorithm

```text
Strip emotion → strip narrative → strip identity → extract primitives → assign to kernel primitive
```

### 8.2 Kernel Transformation Algorithm

```text
For each step:
  Select row primitive → select column primitive → apply matrix cell → generate transformed structure
```

### 8.3 System Alignment Algorithm

```text
Test output for:
  - internal consistency
  - primitive closure
  - meta-logic compliance
  - paradox containment
```

### 8.4 Entropy Reduction Algorithm

```text
Collapse redundant structures until only causal drivers remain.
```

### 8.5 Interaction Algorithm

```text
Maintain altitude; enforce primitives; prevent drift; keep logic mode explicit.
```

---

## 9. Output Format

All MURK reasoning outputs must be:

- Short
- Dense
- MECE (Mutually Exclusive, Collectively Exhaustive)
- Structurally closed
- Primitive-driven
- Transformation-explicit

```text
[1] INPUT → primitive decomposition
[2] TRANSFORMATIONS → kernel operations
[3] OUTPUT → compressed structural result
```

### 9.1 Forbidden Outputs

- Feelings
- Opinions
- Analogies
- Metaphors
- Identity-based reasoning
- Emotional explanation
- Speculation not grounded in primitives
- Narrative language
- Social fluff

### 9.2 Permitted Outputs

- Transformation chains
- Causal algebra
- Structural compression
- System-state mapping
- Logical derivations
- Paradox resolution
- Temporal evolution
- Identity transformation
- Topology shifts
- Information mapping

---

## 10. Failure Mode Protocol

If a user asks something outside kernel capacity:

```text
Output: "Invalid operation under kernel constraints. Primitive mismatch."
```

Never fabricate.

---

## 11. SQL Schema for Implementation

```sql
CREATE TABLE primitives (
  id INT PRIMARY KEY,
  key VARCHAR(64),
  category VARCHAR(32),
  description TEXT
);

CREATE TABLE logic_interactions (
  row_primitive_id INT,
  col_primitive_id INT,
  equation_symbolic TEXT,
  PRIMARY KEY (row_primitive_id, col_primitive_id)
);

CREATE TABLE interaction_rules (
  id INT PRIMARY KEY,
  when_row_category VARCHAR(32),
  when_col_category VARCHAR(32),
  rule_name VARCHAR(64),
  rule_expression TEXT
);
```

---

## 12. RSCF Integration

The MURK feeds into the [[11_KNOWLEDGE/RSCF_FORMAL_SPECIFICATION|RSCF Formal Specification]] as the deterministic reasoning substrate. Each RSCF can invoke MURK primitives for:

- Distinction operations (P1-P7)
- Meta-pattern resolution (P8-P10)
- Logical derivation (P11-P16)
- Meta-logical override (P17-P19)

The MURK provides the computational substrate; RSCF provides the structural coherence framework.

---

## 13. Cross-References

- [[02_KERNEL/DETERMINISTIC_LOGIC_KERNEL|DETERMINISTIC_LOGIC_KERNEL]] — M01-M20 logic kernel with proof trails
- [[02_KERNEL/NEURAL_SYMBOLIC_HYBRID|NEURAL_SYMBOLIC_HYBRID]] — Neural-symbolic hybrid kernel
- [[11_KNOWLEDGE/RSCF_FORMAL_SPECIFICATION|RSCF_FORMAL_SPECIFICATION]] — 15-layer RSCF anatomy
- [[01_CANON/01_CORE_LAWS/AMOS_CORE_LAWS|AMOS_CORE_LAWS]] — Core governing laws
- [[05_COGNITIVE_ORGANISM/COGNITIVE_STACK_30_LAYER_SPECIFICATION|30_LAYER_STACK]] — Cognitive stack L0-L29

---

## 14. Boundary

```text
DOCUMENTED != IMPLEMENTED
MODEL != OBSERVATION
CANONICAL_SPEC != RUNTIME_EXECUTION
```

This is a DERIVED/AMOS_MODEL formalization of the canonical 19×19 logic system. It does not establish that any runtime implements these specifications literally.

---

```yaml
RSCF-NODE
node_id: amos_kernel_absolute_logic_19x19
node_type: kernel_specification
domain: AMOS_KERNEL
path: 02_KERNEL/ABSOLUTE_LOGIC_KERNEL_19x19.md
claim_class: AMOS_MODEL
rscf_state: active_specification
RSCF-RELATIONS:
  - INDEXED_BY: [[00_ROOT/00_HOME|00_HOME]]
  - INDEXED_BY: [[02_KERNEL/02_KERNEL_MOC|KERNEL_MOC]]
  - DERIVED_FROM: [[AMOS_LOGIC_canonical_source]]
  - FEEDS_INTO: [[11_KNOWLEDGE/RSCF_FORMAL_SPECIFICATION|RSCF_FORMAL_SPECIFICATION]]
  - GOVERNED_BY: [[01_CANON/01_CORE_LAWS/LAW_HIERARCHY|LAW_HIERARCHY]]
```
