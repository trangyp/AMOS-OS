---
title: Vault Domain Knowledge — Amos Causal Reasoning Master
type: reference
source: 07_SKILLS/amos-causal-reasoning-master/references
tags:
- reference
- amos-causal-reasoning-master
- type/skill
- skill
- k-counterfactual
- law-hierarchy
- trang-framework-recursive-ontology-dynamics
rscf:
  state: SOURCE_CLAIM
  claim_class: SOURCE_CLAIM
  provenance: AMOS_corpus
  scope: skill_reference
---

# amos-causal-reasoning-master — Vault-Sourced Domain Knowledge

> Load this reference only when detailed domain knowledge is needed.
> This content was moved from SKILL.md for progressive loading.

---

> **Source**: `02_KERNEL/03_CAUSAL/K_CAUSAL_HIERARCHY.md` from the AMOS_OS Obsidian vault.
> This is substantive domain knowledge, not script-generated content.

# K CAUSAL HIERARCHY

> **AMOS Core target:** `v4.4`
> **Origin architect / steward:** Trang Phan
> **Plane:** `02_KERNEL`
> **Status:** `AMOS_MODEL`
> **Conclusion class:** `AMOS_MODEL`

## Purpose

`K_CAUSAL_HIERARCHY` defines the AMOS kernel contract for distinguishing levels and types of causal knowledge.

Its central purpose is to prevent weaker evidence from being silently promoted into stronger causal claims.

The governing rule is:

```text
OBSERVATION
!=
ASSOCIATION
!=
CORRELATION
!=
TEMPORAL ORDER
!=
DEPENDENCY
!=
MECHANISM
!=
INTERVENTIONAL EFFECT
!=
COUNTERFACTUAL EFFECT
```

A claim may move upward in the causal hierarchy only when evidence appropriate to the stronger causal class is available.

Structural similarity, sequence, repetition, authority, model confidence, or fluent explanation cannot substitute for causal evidence.

---

# 1. Core Law

For evidence state `E` and causal claim `C`:

```text
LICENSE(E, C)
```

must hold before `C` can be accepted at its claimed causal level.

Therefore:

```text
CAUSAL CLAIM STRENGTH
<=
CAUSAL LICENSE OF LOAD-BEARING EVIDENCE
```

A stronger conclusion cannot be derived merely because it is compatible with weaker evidence.

---

# 2. Causal Firewall

AMOS distinguishes at minimum:

```text
OBSERVATION
ASSOCIATION
CORRELATION
TEMPORAL PRECEDENCE
STRUCTURAL DEPENDENCY
ENABLING CONDITION
MECHANISM
MEDIATION
CONFOUNDING
NECESSARY CONDITION
SUFFICIENT CONDITION
CAUSAL CONTRIBUTION
INTERVENTIONAL EFFECT
COUNTERFACTUAL EFFECT
FEEDBACK
```

These relations are not interchangeable.

---

# 3. Base Hierarchy

A useful conceptual hierarchy is:

```text
L0  OBSERVATION
↓
L1  ASSOCIATION
↓
L2  CORRELATION
↓
L3  TEMPORAL / STRUCTURAL DEPENDENCY
↓
L4  CAUSAL CANDIDATE
↓
L5  MECHANISM-SUPPORTED RELATION
↓
L6  INTERVENTIONAL CAUSAL EFFECT
↓
L7  COUNTERFACTUAL CAUSAL EFFECT
```

This hierarchy represents increasing causal commitment.

It is not a claim that every causal problem follows a single linear ladder.

Some causal relation types are orthogonal and require separate typing.

---

# 4. L0 — Observation

An observation records what was measured, reported, or detected.

Example:

```text
X = 7
Y = 12
```

or:

```text
EVENT A OCCURRED
EVENT B OCCURRED
```

Observation alone licenses no causal relation.

```text
OBSERVED(X)
+
OBSERVED(Y)

↛

X CAUSES Y
```

---

# 5. L1 — Association

Association means variables or events appear related under a defined measurement context.

```text
ASSOC(X, Y | S, R, T)
```

where:

```text
S = scope
R = regime
T = temporal context
```

Association may motivate causal investigation.

It does not establish causation.

---

# 6. L2 — Correlation

Correlation is a typed statistical relationship.

Conceptually:

```text
CORR(X, Y) != 0
```

may support:

```text
X and Y covary
```

but does not alone support:

```text
X → Y
```

because alternatives include:

```text
Y → X
Z → X AND Z → Y
SELECTION BIAS
MEASUREMENT BIAS
FEEDBACK
CHANCE
MODEL MISSPECIFICATION
```

---

# 7. Correlation Firewall

```text
CORRELATION
!=
CAUSATION
```

remains a hard invariant.

Likewise:

```text
HIGH CORRELATION
!=
STRONG CAUSAL PROOF
```

and:

```text
REPEATED CORRELATION
!=
INDEPENDENT CAUSAL CONFIRMATION
```

when the observations share provenance or confounding structure.

---

# 8. L3 — Temporal Precedence

Suppose:

```text
X occurs before Y
```

This may satisfy one condition needed by some causal hypotheses.

It does not establish:

```text
X → Y
```

Therefore:

```text
BEFORE(X, Y)
!=
CAUSES(X, Y)
```

Temporal precedence is evidence about ordering, not sufficient causal evidence.

---

# 9. Structural Dependency

A structural dependency means one component depends on another according to a system model.

```text
A DEPENDS_ON B
```

does not necessarily mean:

```text
B CAUSES A
```

in the empirical causal sense.

Examples include:

```text
software dependency
logical dependency
schema dependency
authority dependency
derivation dependency
execution dependency
```

These must remain typed.

---

# 10. Dependency Firewall

```text
DEPENDENCY
!=
CAUSATION
```

A dependency edge may become part of a causal model only when the semantics of the edge justify causal interpretation.

---

# 11. L4 — Causal Candidate

A causal candidate is a hypothesis such as:

```text
H1: X → Y
```

supported enough to investigate but not yet licensed as a validated causal conclusion.

Candidate state should preserve alternatives:

```text
H1: X → Y
H2: Y → X
H3: Z → {X, Y}
H4: X ↔ Y
H5: ASSOCIATION WITHOUT CAUSAL EFFECT
```

Until discriminating evidence exists:

```text
STATE = COMPETING
```

where appropriate.

---

# 12. L5 — Mechanism-Supported Relation

A mechanism describes a plausible process through which one state influences another.

```text
X
↓
M
↓
Y
```

A mechanism may substantially strengthen a causal hypothesis.

But:

```text
PLAUSIBLE MECHANISM
!=
DEMONSTRATED CAUSAL EFFECT
```

A mechanism can be real while its effect is negligible, context-dependent, blocked, or dominated by other pathways.

---

# 13. Mechanism Typing

A mechanism claim should identify:

```yaml
mechanism:
  source:
  target:
  mediator:
  conditions:
  scope:
  regime:
  evidence:
  competing_mechanisms:
  falsifiers:
```

Mechanisms without explicit conditions risk scope leakage.

---

# 14. Enabling Condition

An enabling condition makes an outcome or mechanism possible.

```text
E ENABLES Y
```

does not imply:

```text
E IS SUFFICIENT FOR Y
```

or:

```text
E IS THE PRIMARY CAUSE OF Y
```

Therefore:

```text
ENABLING
!=
SUFFICIENT
```

---

# 15. Necessary Condition

`X` is necessary for `Y` under scope `S` when:

```text
¬X → ¬Y
```

within the defined applicability envelope.

This does not mean:

```text
X → Y
```

Therefore:

```text
NECESSARY
!=
SUFFICIENT
```

---

# 16. Sufficient Condition

`X` is sufficient for `Y` under conditions `C` when:

```text
X ∧ C → Y
```

within the relevant scope and regime.

Sufficiency must not be generalized beyond those conditions.

---

# 17. Necessary and Sufficient

When both are established:

```text
X ↔ Y
```

may represent a necessary-and-sufficient relation under explicit conditions.

This is a strong claim.

It requires correspondingly strong evidence.

---

# 18. Causal Contribution

Many real systems have multiple contributing causes.

```text
X contributes to Y
```

is weaker than:

```text
X is necessary for Y
```

or:

```text
X is sufficient for Y
```

AMOS should preserve this distinction rather than forcing binary causation.

---

# 19. Mediation

Mediation represents an intermediate causal path:

```text
X → M → Y
```

where `M` transmits some or all of the causal influence of `X` on `Y`.

A mediation claim requires evidence distinguishing:

```text
DIRECT EFFECT
INDIRECT EFFECT
TOTAL EFFECT
```

when those distinctions are material.

---

# 20. Mediation Firewall

Observing:

```text
X associated with M
M associated with Y
```

does not alone prove:

```text
X → M → Y
```

The path remains a model until appropriately validated.

---

# 21. Confounding

A confounder `Z` may produce:

```text
Z → X
Z → Y
```

creating an apparent relation:

```text
X ↔ Y
```

without the proposed direct causal relation.

Therefore every consequential causal claim should consider material confounding alternatives.

---

# 22. Hidden Confounding

Unknown or unmeasured variables may remain possible.

Therefore:

```text
NO KNOWN CONFOUNDER
!=
NO CONFOUNDER EXISTS
```

Confidence must respect the evidence available.

---

# 23. Selection Effects

Selection may induce misleading associations.

Conceptually:

```text
X → S ← Y
```

Conditioning on `S` can create an apparent relation between `X` and `Y`.

AMOS causal reasoning must therefore distinguish:

```text
OBSERVED ASSOCIATION
```

from:

```text
ASSOCIATION AFTER SELECTION
```

when selection is material.

---

# 24. Collider Structure

A collider:

```text
X → Z ← Y
```

requires special treatment.

Conditioning on `Z` can create dependence between otherwise independent causes.

Therefore:

```text
CONDITIONING
```

is not automatically harmless.

---

# 25. Common Cause

A common cause structure:

```text
Z
├──→ X
└──→ Y
```

is a primary competing explanation for apparent `X → Y` relations.

Causal analysis should explicitly test it when plausible.

---

# 26. Common Effect

A common effect structure:

```text
X ──→ Z
Y ──→ Z
```

must not be confused with:

```text
X → Y
```

or:

```text
Y → X
```

---

# 27. Chain

A causal chain:

```text
X → M → Y
```

may support transitive causal influence under appropriate conditions.

But:

```text
X → M
M → Y
```

does not automatically imply a simple invariant effect of `X` on `Y`.

Intervention semantics, blockers, nonlinearities, regimes, and feedback may matter.

---

# 28. Fork

A causal fork:

```text
X ← Z → Y
```

represents common-cause structure.

This must remain distinguishable from:

```text
X → Y
```

---

# 29. Feedback

Feedback occurs when causal influence participates in a loop.

Conceptually:

```text
X → Y
↑   ↓
└── Z
```

or:

```text
X ↔ Y
```

over time.

Feedback requires temporal or state indexing to avoid treating cyclic influence as an instantaneous contradiction.

---

# 30. Feedback Firewall

```text
FEEDBACK
!=
SIMPLE BIDIRECTIONAL CORRELATION
```

A feedback claim requires evidence that reciprocal causal influence actually occurs.

---

# 31. Positive Feedback

Positive feedback amplifies change.

Conceptually:

```text
ΔX
→
ΔY
→
further ΔX
```

The label `positive` refers to amplification structure, not desirability.

---

# 32. Negative Feedback

Negative feedback counteracts deviation.

```text
ΔX
→
response
→
reduce ΔX
```

Again:

```text
NEGATIVE
!=
BAD
```

It describes causal control structure.

---

# 33. Direct Cause

A direct causal edge:

```text
X → Y
```

means the modeled causal relationship is not represented as mediated by another variable in the relevant model.

But directness is model-relative.

A more detailed model may reveal mediators.

Therefore:

```text
DIRECT
```

must inherit the model's granularity and scope.

---

# 34. Indirect Cause

An indirect effect occurs through one or more mediators:

```text
X → M1 → M2 → Y
```

The path should remain explicit when it matters to intervention or explanation.

---

# 35. Total Causal Effect

Conceptually:

```text
TOTAL_EFFECT
=
DIRECT_EFFECT
+
INDIRECT_EFFECTS
```

where the mathematical decomposition is valid for the model used.

AMOS must not assume additive decomposition universally.

---

# 36. L6 — Interventional Effect

An interventional causal claim concerns what changes when an intervention changes `X`.

Conceptually:

```text
P(Y | do(X=x1))
!=
P(Y | do(X=x0))
```

supports a causal effect under the relevant assumptions.

This is stronger than observational association.

---

# 37. Intervention Firewall

```text
P(Y | X)
```

is not generally equivalent to:

```text
P(Y | do(X))
```

Therefore observational prediction and causal intervention must remain distinct.

---

# 38. Intervention Scope

An intervention effect inherits:

```text
POPULATION
ENVIRONMENT
TIME
REGIME
INTERVENTION TYPE
MEASUREMENT METHOD
ASSUMPTIONS
```

An intervention validated in one envelope must not silently generalize to another.

---

# 39. Natural vs Artificial Intervention

Different interventions on nominally the same variable may produce different effects.

Therefore:

```text
SET X
```

is insufficiently precise when intervention mechanism matters.

The intervention should be typed where necessary.

---

# 40. L7 — Counterfactual Effect

Counterfactual reasoning concerns alternative outcomes for the same modeled unit or state under different interventions.

Conceptually:

```text
Y_x
```

versus:

```text
Y_x'
```

The counterfactual level makes stronger assumptions than ordinary association.

---

# 41. Counterfactual Firewall

```text
OBSERVED Y AFTER X
```

does not directly reveal:

```text
WHAT Y WOULD HAVE BEEN
WITHOUT X
```

The missing counterfactual must be inferred through an appropriately justified model or design.

---

# 42. Relationship to [[K_COUNTERFACTUAL]]

`K_COUNTERFACTUAL` governs the logical construction and evaluation of counterfactual branches.

`K_CAUSAL_HIERARCHY` determines what causal strength those branches can support.

```text
COUNTERFACTUAL BRANCH
!=
COUNTERFACTUAL PROOF
```

---

# 43. Causal Direction

Given association:

```text
X — Y
```

possible directions include:

```text
X → Y
Y → X
X ← Z → Y
X ↔ Y
NO CAUSAL EDGE
```

AMOS must not select direction from association alone unless additional evidence licenses it.

---

# 44. Causal Graph

A causal model may be represented as:

```text
G = (V, E)
```

where:

```text
V = typed variables / states
E = typed causal edges
```

Each causal edge should carry sufficient metadata to identify its epistemic status.

---

# 45. Typed Causal Edge

Recommended conceptual representation:

```yaml
causal_edge:
  source:
  target:

  relation_type:
  direction:

  conclusion_class:

  evidence: []
  provenance: []

  scope:
  regime:
  temporal_validity:

  assumptions: []
  confounders: []
  mediators: []

  falsifiers: []
  invalidation_conditions: []

  confidence_ceiling:
```

---

# 46. Relation Types

Recommended relation vocabulary:

```text
ASSOCIATED_WITH
CORRELATED_WITH
PRECEDES
DEPENDS_ON
ENABLES
INHIBITS
CONTRIBUTES_TO
MEDIATES
CONFOUNDS
NECESSARY_FOR
SUFFICIENT_FOR
CAUSES
DIRECTLY_CAUSES
INDIRECTLY_CAUSES
MODERATES
FEEDBACKS_WITH
```

Do not collapse these into a generic `RELATED_TO` when causal semantics matter.

---

# 47. Epistemic Classes

Causal claims retain AMOS conclusion classes:

```text
VERIFIED
DERIVED
MODEL
CONDITIONAL
COMPETING
UNKNOWN/GAP
```

A causal relation represented in a model is not automatically `VERIFIED`.

---

# 48. Source Claims

A document may assert:

```text
X causes Y
```

Without independent validation, AMOS records:

```text
SOURCE_CLAIM:
"source asserts X causes Y"
```

not automatically:

```text
VERIFIED:
X causes Y
```

---

# 49. Evidence Typing

Relevant evidence classes include:

```text
SOURCE_CLAIM
OBSERVATION
DERIVED
MODEL
DECISION
UNKNOWN
```

The evidence type determines what causal inference it can support.

---

# 50. Evidence Strength Firewall

A useful constraint is:

```text
CAUSAL CONCLUSION
<=
WEAKEST LOAD-BEARING CAUSAL PREMISE
```

unless the weak premise has been independently revalidated or replaced.

---

# 51. Provenance Independence

Suppose three claims all descend from one source:

```text
SOURCE A
├── REPORT B
├── REPORT C
└── REPORT D
```

Then:

```text
B + C + D
```

do not constitute three independent causal confirmations.

---

# 52. Provenance Topology

Causal validation should preserve:

```text
SOURCE IDENTITY
ANCESTRY
DEPENDENCY
CORRELATION RISK
FRESHNESS
REGIME
```

when these can affect causal confidence.

---

# 53. Causal Sybil Hardening

Repeated claims can create false apparent confirmation


## Vault-Sourced Domain Content

> Source: `11_KNOWLEDGE/TRANG_FRAMEWORK_RECURSIVE_ONTOLOGY_DYNAMICS.md` (53649 bytes in vault)

### Research Capsule

- **Conclusion class:** `MODEL`
- **Evidence class:** `SOURCE_CLAIM`
- **Canonical status:** `NON_CANONICAL`
- **Validation status:** `UNVALIDATED`
- **Primary question:** Can the Trang Framework be developed from a meta-ontology into computable recursive survival dynamics?
- **Primary comparison domains:** quantum theory, QFT, classical emergence, thermodynamics, complex systems, biology, cognition, and civilization.
- **Load-bearing proposals:** boundary, persistence, identity, memory, repair, HML translation, emergence, scale transition, causal propagation, recursive stabilization, and survival.
- **Critical gaps:** measurable operators, formal proof, dimensional consistency, simulation, predictive falsifiability, experimental protocols, and mapping to established physics.
- **Promotion gate:** no proposition moves into `01_CANON` solely because it is internally coherent or mathematically expressed.

---

### 5. Measurement And Collapse As A Proposed Boundary Model

A simplified quantum description may be represented schematically as:

```text
state evolves
→ interaction / measurement occurs
→ an outcome is recorded
```

The Trang Framework proposes investigating whether measurement can be modeled using:

```text
possibility constraints
→ boundary locking
→ stable recorded state
```

Proposed schematic:

```text
Collapse_Model
=
Constraint
× BoundaryLocking
× RecursiveStabilization
```

This is not asserted as an established physical account of wavefunction collapse.

**Class:** `MODEL`

---

### 13. Temporal Memory Operator

Introduce:

```text
τ = memory depth
```

Proposed memory equation:

```text
K(t+1)
=
αK(t)
+
βExperience(t)
-
γDecay(t)
```

where:

```text
α = memory retention
β = new learning contribution
γ = memory degradation
```

A simplified learning condition is proposed as:

```text
β > γ
```

and a degradation condition as:

```text
γ > β
```

These relations require normalization, units, and domain-specific interpretation before simulation.

---

### 24. Information Model

Proposed:

```text
Information_Model
=
Difference
× FutureImpact
× MemoryIntegration
```

Conceptually:

> Information is a difference capable of changing future system state.

This is a framework-specific modeling definition and should be compared with established information-theoretic definitions rather than treated as equivalent to them.

---

### 28. Tensor Relation Formalism — 𝕋

Introduce:

```text
𝕋(i,j,k,t,s)
```

as a proposed multidimensional relational representation encoding, where defined:

- relation;
- direction;
- magnitude;
- time;
- scale.

Proposed integrity metric:

```text
I
=
Consistency(𝕋)
× Persistence(𝕋)
× Repairability(𝕋)
```

The tensor's mathematical type, index semantics, transformation rules, and metric structure remain open requirements.

---

### 31. Causal Graph Operator — ⊕

Introduce:

```text
⊕(A→B)
```

to represent a proposed causal constraint relationship in which intervention or state change in `A` alters the accessible state space of `B`.

Conceptually:

```text
CausalInfluence
≈ StateSpaceConstraintPropagation
```

AMOS causal discipline requires distinguishing association, mechanism, intervention, mediation, confounding, enabling conditions, necessity, sufficiency, and feedback. This operator alone does not prove causation.

---

### 58. Agency And Repair Authority

Proposed:

```text
Agency
=
Perception
× OptionSpace
× Permission
× Energy
× ConsequenceTracking
```

Awareness without repair authority may have limited corrective value. Conversely, action authority without validation or consequence tracking can increase risk.

---

### 59. Owned Memory

Proposed:

```text
OwnedMemory
=
SelfRelevance
× ContinuityImpact
× Integration
× FutureBehaviorChange
```

The framework distinguishes stored data, accessible memory, and memory integrated into a system's persistent self-model.

---

### 67. Internal Privacy

Proposed:

```text
PrivateState
=
InternalState
-
ReportableState
-
ExternallyWritableState
```

This expression is conceptual rather than set-theoretically complete.

For advanced AI architecture, a governance proposal is that privileged core state should not be writable by an untrusted language/interface layer without authorization and validation.

---

# Part VI — Observer, Classicality, and Physics Mapping

### 74. Formal Language Layer

Distinguish:

```text
Entity      = modeled system
State       = configuration of an entity
Operator    = transformation
Metric      = measurement function
Threshold   = decision / transition boundary
Transition  = state change
Failure     = defined loss mode
Recovery    = restoration process
Inheritance = transfer of persistent information
Observer    = system participating in measurement
```

---

# Part VII — Closure Requirements

### 75. Near-Closure Architecture

Absolute completeness is not claimed.

A maximally closed recursive research framework would require at least the following interacting layers:

### 75.10 Cognitive Layer

- predictive modeling;
- symbolic compression;
- recursive self-modeling;
- counterfactual simulation;
- correction authority.

### 75.12 Meta-Law Layer

- falsifiability;
- self-audit;
- contradiction detection;
- repair operators;
- scope boundaries.

The source model is strongest as a conceptual architecture for cross-scale recursion and survival and remains weakest where exact state-space, dynamics, geometry, and physics-facing mathematical derivation are required.

---

### 83. Information–Energy Relationship

Proposed conceptual distinction:

```text
Information
=
DifferenceCapableOfChangingFutureStates
```

```text
Energy
=
CapacityForPhysicalStateTransition
```

Proposed relationship:

```text
No usable information processing without physical energetic implementation.
No usable energy gradient without distinguishable physical states.
```

This does not establish literal information-energy equivalence. Established results such as Landauer's principle must be treated according to their actual scope.

---

### 84. Law Emergence

Proposed:

```text
Law_Model
=
StableRecursiveInvariant
that persists across transformation space
```

Proposed physical-law interpretation:

```text
PhysicalLaw_Model
=
StableConstraint / invariant
within viable state space
```

This is a philosophical/modeling proposal, not an empirically established origin theory for physical laws.

---

### 86. Computational Boundary

The framework proposes investigating whether finite/local update constraints can help model:

- causality;
- locality;
- latency;
- horizons;
- decoherence;
- observational limits.

No implication should be made that these phenomena are thereby derived. Each requires separate formal proof and empirical mapping.

---

### 88. Semantic Causality

Living and social systems may respond to interpreted symbols, rules, goals, and shared meanings.

Examples include:

- money;
- law;
- language;
- religion;
- identity;
- mathematics.

Proposed:

```text
Meaning_Model
=
ConstraintEncodedThroughSharedSymbolicMemory
```

AMOS causal discipline requires tracing the physical, informational, institutional, and behavioral mechanisms by which symbolic meaning changes outcomes. Meaning must not be treated as an unexplained fundamental force.

---

### 91. Self-Modifying Law Engine

The framework proposes investigating whether effective laws can change across scale or regime.

Introduce:

```text
MetaLaw_Model
=
RulesConstrainingEffectiveLawEvolution
```

This does not imply fundamental physical laws actually evolve. Fundamental-law change and effective-law change must remain distinct hypotheses.

---

### 97. Epistemic Horizon

Even if all preceding layers were formalized, unresolved questions may remain, including:

- why there is existence rather than nothing;
- why particular invariants obtain;
- whether mathematics is discovered, constructed, or both;
- whether consciousness is fundamental, emergent, or differently constituted;
- whether p

... (truncated, see vault source for full content)

## Failure Modes

- **Insufficient evidence**: If source material is insufficient, mark as UNKNOWN/GAP and fail closed — do not fabricate.
- **Scope violation**: If the query falls outside the skill's declared scope, escalate to the parent skill or steward.
- **Binding broken**: If 1:1:1 binding (skill→agent→workflow) is broken, flag routing mismatch and block execution.
- **Validation failure**: If validation gates fail, downgrade confidence, flag the gap, and escalate — do not force-fit.
- **Epistemic overreach**: If a claim exceeds the established evidence or epistemic class, retract and relabel.

---
**MOC:** references_MOC

## Related

- [[07_SKILLS_MOC]]
---

**Related:** [[00_HOME]] · [[AMOS_RSCF_NODES]] · [[LAW_HIERARCHY]] · references_MOC · [[07_SKILLS_MOC]]

**MOC:** references_MOC

**Trang Framework:** [[TRANG_FRAMEWORK_RECURSIVE_ONTOLOGY_DYNAMICS]]

---
RSCF-NODE
node_id: amos-causal-reasoning-master-vault-domain-knowledge
node_type: reference
path: 07_SKILLS/amos-causal-reasoning-master/references/vault_domain_knowledge.md
RSCF-RELATIONS:
- INDEXED_BY: [[00_HOME]]
- INDEXED_BY: [[AMOS_RSCF_NODES]]
- CHILD_OF: references_MOC

