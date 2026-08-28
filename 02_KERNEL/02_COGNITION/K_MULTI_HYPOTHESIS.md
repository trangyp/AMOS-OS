---
title: K MULTI HYPOTHESIS
type: hypothesis
source: 02_KERNEL/02_COGNITION
artifact_id: AMOS-OS-K-MULTI-HYPOTHESIS
canonical_name: K_MULTI_HYPOTHESIS
artifact_type: kernel_multi_hypothesis_contract
status: AMOS_MODEL
conclusion_class: AMOS_MODEL
amos_core_target: v4.4
origin_architect: Trang Phan
steward: Trang Phan
plane: KERNEL
kernel_family: REASONING
domain: multi-hypothesis-reasoning
scope: AMOS_OS
created: 2026-08-25
updated: 2026-08-25
tags:
- amos-os
- kernel
- core
- canon-group/tech-ai
- canon/model
- kernel/reasoning
- kernel/multi-hypothesis
- kernel/competing-hypotheses
- kernel/epistemic
- kernel/provenance
- kernel/evidence-topology
- kernel/dependency
- kernel/causal
- kernel/counterfactual
- kernel/metacognition
- kernel/scope
- kernel/regime
- kernel/freshness
- kernel/sensitivity
- kernel/validation
- kernel/rscf
- rscf/claim
- rscf/provenance
- rscf/state/model
- topic/multi-hypothesis
- topic/competing-hypotheses
- topic/discriminating-evidence
- readme
- architecture
- system-map
- placement-rules
- canon-map
- amos-core-laws
- invariant-registry
- law-hierarchy
- hml-canon
- authority-canon
- canon-provenance
- source-lineage
- source-registry
- conflict-registry
- supersession-log
- kernel-map
- k-core19-logic
- k-distinction-relation-constraint
- k-law-hierarchy
- k-meta-logic
- k-counterfactual
- k-metacognition
- control-plane-map
- runtime-map
- authoritative-state
- 00-root-moc
- amos-moc
- 00-home
- amos-rscf-nodes
- 02-cognition-moc
aliases:
- AMOS Multi Hypothesis Kernel - Multi Hypothesis Kernel - K Multi Hypothesis - K_MULTI_HYPOTH
---

# K_MULTI_HYPOTHESIS
> **AMOS Core target:** `v4.4`
> **Origin architect / steward:** Trang Phan
> **Plane:** `02_KERNEL`
> **Status:** `AMOS_MODEL`
> **Conclusion class:** `AMOS_MODEL`
## Purpose
`K_MULTI_HYPOTHESIS` defines the AMOS kernel contract for maintaining, comparing, challenging, discriminating, updating, and resolving multiple plausible explanations or predictions without forcing premature convergence.
Its core function is:
```text
QUESTION / OBSERVATION / ANOMALY
↓
GENERATE OR RETRIEVE MATERIAL HYPOTHESES
↓
KEEP HYPOTHESES DISTINCT
↓
MAP EVIDENCE + PROVENANCE + DEPENDENCIES
↓
TEST SCOPE / REGIME / FRESHNESS
↓
SEEK CONTRADICTING + DISCRIMINATING EVIDENCE
↓
UPDATE RELATIVE SUPPORT
↓
RESOLVE
OR
PRESERVE COMPETING
OR
RETURN UNKNOWN/GAP
```
The kernel exists to prevent:
```text
FIRST PLAUSIBLE EXPLANATION
→
UNJUSTIFIED CONCLUSION
```
and:
```text
MOST REPEATED EXPLANATION
→
FALSE CONSENSUS
```
rscf:
  state: DERIVED
  claim_class: DERIVED
  provenance: AMOS_corpus
  scope: AMOS_general
---


# 1. Architectural Position

```text
01_CANON
↓
02_KERNEL
   ├── K_CORE19_LOGIC
   ├── K_DISTINCTION_RELATION_CONSTRAINT
   ├── K_LAW_HIERARCHY
   ├── K_META_LOGIC
   ├── K_COUNTERFACTUAL
   ├── K_METACOGNITION
   └── K_MULTI_HYPOTHESIS
↓
EPISTEMIC / PROVENANCE / CAUSAL / DEPENDENCY / VALIDATION
↓
03_CONTROL_PLANE
↓
04_RUNTIME
```

`K_MULTI_HYPOTHESIS` does not replace causal, provenance, epistemic, or validation kernels.

It coordinates their outputs around competing explanatory states.

---

# 2. Core Law

```text
PLAUSIBLE
!=
VERIFIED
```

and:

```text
ONE SUPPORTED HYPOTHESIS
!=
ONLY POSSIBLE HYPOTHESIS
```

and:

```text
MULTIPLE SOURCES
!=
MULTIPLE INDEPENDENT CONFIRMATIONS
```

When material alternatives remain viable:

```text
PRESERVE COMPETING
```

---

# 3. Hard Boundary

```text
HYPOTHESIS != FACT
HYPOTHESIS != OBSERVATION
HYPOTHESIS != MODEL TRUTH
SUPPORT != VERIFICATION
POPULARITY != EVIDENCE
REPETITION != INDEPENDENCE
SOURCE COUNT != INDEPENDENT ROOT COUNT
BEST CURRENT HYPOTHESIS != CERTAINTY
NO ALTERNATIVE FOUND != NO ALTERNATIVE EXISTS
CONSISTENCY != CORRECTNESS
COHERENCE != CAUSATION
COMPETING != FAILURE
UNKNOWN/GAP != PASS
```

---

# 4. Hypothesis Object

A material hypothesis should conceptually carry:

```yaml
hypothesis:
  hypothesis_id:
  statement:

  hypothesis_type:
  conclusion_class:

  scope:
  regime:
  temporal_validity:

  assumptions: []

  supporting_evidence: []
  contradicting_evidence: []
  neutral_evidence: []

  provenance_roots: []
  dependency_refs: []

  predicted_observations: []
  counterfactual_predictions: []

  falsifiers: []
  discriminating_tests: []

  confidence_ceiling:
  status:
```

---

# 5. Hypothesis Types

AMOS may distinguish:

```text
EXPLANATORY
CAUSAL
MECHANISTIC
PREDICTIVE
STRUCTURAL
COUNTERFACTUAL
DIAGNOSTIC
FAILURE
BEHAVIORAL
STATE
PROVENANCE
AUTHORITY
REGIME
IMPLEMENTATION
```

Hypothesis type determines which evidence can legitimately discriminate it.

---

# 6. Hypothesis Identity

Each hypothesis must have stable identity.

```text
H1 != H2
```

whenever their propositions differ materially.

Different wording does not necessarily mean different hypotheses.

```text
DIFFERENT WORDING
!=
DIFFERENT SEMANTIC HYPOTHESIS
```

Likewise:

```text
SAME LABEL
!=
SAME HYPOTHESIS
```

if assumptions or scope differ.

---

# 7. Semantic Normalization

Before counting hypotheses, normalize:

```text
TERMS
DEFINITIONS
UNITS
SCOPE
REGIME
TIME
ASSUMPTIONS
CAUSAL DIRECTION
```

Two statements that appear different may be semantically equivalent.

Example:

```text
H1:
X increases Y under R1.

H2:
Within regime R1, Y rises when X rises.
```

may normalize to one proposition.

Do not manufacture diversity from paraphrases.

---

# 8. Hypothesis Distinction Firewall

Conversely, apparently similar claims may differ materially.

```text
H1:
X correlates with Y.

H2:
X causes Y.
```

These are not equivalent.

```text
CORRELATION HYPOTHESIS
!=
CAUSAL HYPOTHESIS
```

---

# 9. Initial Hypothesis Set

The initial hypothesis set should include every materially supported explanation that can change the answer.

Conceptually:

```text
H =
{
  H1,
  H2,
  ...
  Hn
}
```

Do not expand into arbitrary possibilities with no support or decision value.

---

# 10. Completeness Boundary

The kernel seeks:

```text
MATERIAL HYPOTHESIS COVERAGE
```

not:

```text
ALL LOGICALLY POSSIBLE STORIES
```

A hypothesis should enter the active set when it is:

```text
PLAUSIBLE ENOUGH
AND
MATERIALLY DISTINCT
AND
CAPABLE OF CHANGING THE OUTCOME
```

---

# 11. Null Hypothesis

Where appropriate, preserve a null or minimal explanation.

Examples:

```text
NO MATERIAL EFFECT
NO CAUSAL LINK
RANDOM VARIATION
MEASUREMENT ARTIFACT
NO SYSTEM CHANGE
```

The null hypothesis should not be privileged automatically.

It is simply another explicitly modeled alternative where relevant.

---

# 12. Unknown Hypothesis Class

If evidence indicates:

```text
CURRENT HYPOTHESES
DO NOT EXPLAIN OBSERVATIONS
```

AMOS should permit:

```text
H_UNKNOWN
```

rather than forcing one known hypothesis to absorb unexplained evidence.

---

# 13. Open-World Firewall

```text
H1 REJECTED
H2 REJECTED
```

does not necessarily imply:

```text
H3 TRUE
```

unless the hypothesis set is demonstrably exhaustive for the relevant proposition.

In many real-world domains:

```text
HYPOTHESIS SET
=
OPEN WORLD
```

Therefore:

```text
REJECT ALL KNOWN
→
UNKNOWN/GAP
```

may be the correct outcome.

---

# 14. Evidence Partition

For each hypothesis, evidence should be classified as:

```text
SUPPORTING
CONTRADICTING
NEUTRAL
AMBIGUOUS
SHARED
DISCRIMINATING
FALSIFYING
```

Do not treat every relevant source as support.

---

# 15. Evidence Typing

Evidence topology distinguishes:

```text
SOURCE_CLAIM
OBSERVATION
DERIVED
MODEL
DECISION
UNKNOWN
```

A hypothesis supported only by model outputs has a different epistemic basis from one supported by independent observations.

---

# 16. Provenance Topology

Each evidence item should preserve ancestry.

Example:

```text
ROOT_A
├── SOURCE_B
│   └── REPORT_D
└── SOURCE_C
    └── REPORT_E
```

`B`, `C`, `D`, and `E` may represent one upstream origin.

Therefore:

```text
DOCUMENT COUNT
!=
INDEPENDENT EVIDENCE COUNT
```

---

# 17. Sybil Hardening

A hypothesis supported by:

```text
ARTICLE_1
ARTICLE_2
ARTICLE_3
AGENT_SUMMARY_1
AGENT_SUMMARY_2
```

may still have only:

```text
ONE INDEPENDENT ROOT
```

if all descend from one origin.

Repetition must not inflate hypothesis support.

---

# 18. Independence States

Recommended evidence-independence states:

```text
INDEPENDENT
PARTIALLY_INDEPENDENT
CORRELATED
SHARED_ANCESTRY
UNKNOWN
```

Canonical rule:

```text
UNKNOWN
!=
INDEPENDENT
```

---

# 19. Evidence Correlation

Evidence may be correlated through:

```text
SAME DATASET
SAME SOURCE
SAME MODEL
SAME AUTHORS
SAME EXPERIMENT
SAME PIPELINE
SAME API
SAME AGENT CONTEXT
SAME TRANSFORMATION
```

Correlation risk should remain visible.

---

# 20. Hypothesis Support Structure

Conceptually:

```yaml
support_state:
  hypothesis_id:

  supporting_roots: []
  contradicting_roots: []

  independent_support_count:
  correlated_support_count:

  evidence_quality:
  provenance_quality:
  scope_fit:
  regime_fit:
  freshness:

  unresolved_conflicts: []

  conclusion_class:
```

No universal scalar score is required.

---

# 21. No Naive Vote Counting

Invalid reasoning:

```text
H1 = 10 sources
H2 = 2 sources

THEREFORE
H1 wins 10:2
```

unless those sources are independent and otherwise comparable.

Correct analysis must inspect:

```text
PROVENANCE ROOTS
QUALITY
SCOPE
REGIME
EVIDENCE TYPE
FRESHNESS
```

---

# 22. No Authority-by-Majority

```text
MOST PEOPLE SAY H1
```

is not itself proof.

Popularity may be relevant as an observation of belief distribution, but:

```text
POPULAR BELIEF
!=
EXTERNAL TRUTH
```

---

# 23. Scope Firewall

Each hypothesis has an applicability envelope.

```yaml
scope:
  system:
  population:
  environment:
  scale:
  time:
  measurement_method:
  assumptions:
```

Two hypotheses may both be correct in different scopes.

---

# 24. Scope Partition

Example:

```text
H1 valid for population P1
H2 valid for population P2
```

The correct resolution may be:

```text
BOTH CONDITIONAL
```

rather than selecting one globally.

---

# 25. Regime Firewall

A hypothesis may dominate in one regime and fail in another.

```text
R1 → H1
R2 → H2
```

This can be a valid partition.

Do not force:

```text
H1 OR H2
```

when the real structure is:

```text
H1 GIVEN R1
H2 GIVEN R2
```

---

# 26. Regime Shift Detection

When observations once supporting `H1` stop fitting:

```text
DO NOT IMMEDIATELY CONCLUDE
H1 WAS ALWAYS WRONG
```

Check whether:

```text
REGIME CHANGED
```

A previously valid model may become stale without being historically invalid.

---

# 27. Temporal Hypotheses

Hypotheses may differ only by time.

Example:

```text
H1:
System state changed before T.

H2:
System state changed after T.
```

Temporal discrimination may resolve the conflict without rejecting the underlying mechanism.

---

# 28. Freshness

Evidence supporting a current hypothesis must be current enough for the domain.

```text
OLD SUPPORT
```

may remain historically valid but stale for current decision-making.

Freshness is typed and claim-specific.

---

# 29. Causal Hypotheses

Causal hypotheses require stronger discipline.

Possible alternatives for observed association:

```text
H1:
X → Y

H2:
Y → X

H3:
Z → X AND Y

H4:
X ↔ Y FEEDBACK

H5:
MEASUREMENT ARTIFACT

H6:
NO STABLE CAUSAL RELATION
```

AMOS should preserve plausible alternatives until discrimination is possible.

---

# 30. Causal Firewall

The following cannot independently resolve causal competition:

```text
SEQUENCE
CO-OCCURRENCE
CORRELATION
STRUCTURAL SIMILARITY
ANALOGY
NARRATIVE COHERENCE
```

Causal hypotheses require appropriately typed evidence.

---

# 31. Mechanism Hypotheses

For the same observed effect:

```text
H1:
MECHANISM A

H2:
MECHANISM B

H3:
A + B INTERACTION
```

all may remain live even if the outcome itself is well established.

Thus:

```text
OUTCOME VERIFIED
!=
MECHANISM VERIFIED
```

---

# 32. Counterfactual Integration

Each causal hypothesis may generate different counterfactual predictions.

```text
H1 → CF1
H2 → CF2
H3 → CF3
```

A discriminating intervention should ideally yield different expected outcomes across hypotheses.

---

# 33. Prediction Table

Conceptually:

| Observation/Test | H1 predicts | H2 predicts | H3 predicts |
| ---------------- | ----------- | ----------- | ----------- |
| `T1`             | `A`         | `B`         | `A`         |
| `T2`             | `X`         | `X`         | `Y`         |
| `T3`             | `M`         | `N`         | `P`         |

`T3` has more discriminating value if predictions diverge strongly.

---

# 34. Discriminating Evidence

Evidence is discriminating when:

```text
P(E | H1)
```

and:

```text
P(E | H2)
```

differ materially.

This notation is conceptual and does not require every implementation to use Bayesian probability.

---

# 35. Cheap High-Information Test

Preferred next step:

```text
TEST*
=
LOWEST COST
TEST
WITH
HIGHEST EXPECTED DECISION-RELEVANT DISCRIMINATION
```

Avoid redundant evidence that every surviving hypothesis already predicts.

---

# 36. Redundant Evidence

If:

```text
H1 predicts A
H2 predicts A
H3 predicts A
```

observing `A` may have low discrimination value.

It may validate shared premises without ranking the competing hypotheses.

---

# 37. Falsifiers

Each hypothesis should identify observations capable of weakening it.

```yaml
hypothesis:
  id: H1
  falsifiers:
    - F1
    - F2
```

A hypothesis without a meaningful falsifier may remain a model or interpretive frame rather than a strongly empirical claim.

---

# 38. Strong Falsification

If hypothesis `H1` entails:

```text
H1 → A
```

and high-quality observation gives:

```text
NOT A
```

then `H1` may be invalidated or downgraded, subject to checking auxiliary assumptions.

---

# 39. Auxiliary Assumption Firewall

Failure of a prediction may arise from:

```text
HYPOTHESIS FAILURE
OR
AUXILIARY ASSUMPTION FAILURE
OR
MEASUREMENT FAILURE
OR
REGIME MISMATCH
```

Therefore one failed prediction does not always uniquely identify the failed premise.

---

# 40. Assumption Map

Hypotheses should expose material assumptions.

```text
H1
├── A1
├── A2
└── A3
```

If `A2` is fragile, confidence in `H1` must reflect that dependence.

---

# 41. Common Assumption Risk

Suppose:

```text
H1 depends on A
H2 depends on A
H3 depends on A
```

Then evidence validating `A` supports all three.

It does not discriminate among them.

Likewise, failure of `A` may invalidate all three.

---

# 42. Dependency Graph

Conceptually:

```text
            P_SHARED
           /   |    \
         H1    H2    H3

P_H1 ───→ H1
P_H2 ───→ H2
P_H3 ───→ H3
```

Metacognitive and validation layers should target `P_H1/P_H2/P_H3` when seeking discrimination.

---

# 43. Hypothesis Confidence Ceiling

For hypothesis `H`:

```text
CONFIDENCE(H)
<=
WEAKEST LOAD-BEARING PREMISE
```

unless that premise is independently revalidated or bypassed.

---

# 44. No Probability Fabrication

If the evidence does not justify numerical probabilities:

```text
DO NOT INVENT
H1 = 70%
H2 = 20%
H3 = 10%
```

Use qualitative states such as:

```text
STRONGER SUPPORT
WEAKER SUPPORT
COMPARABLE SUPPORT
INCOMPARABLE
COMPETING
UNKNOWN
```

---

# 45. Relative Support States

Recommended states:

```text
DOMINANT
STRONGLY_SUPPORTED
SUPPORTED
PLAUSIBLE
WEAK
CHALLENGED
FALSIFIED_FOR_SCOPE
COMPETING
UNKNOWN
```

These describe comparative evidence state, not universal truth.

---

# 46. Dominant Hypothesis

`DOMINANT` means:

```text
BEST SUPPORTED AMONG ACTIVE HYPOTHESES
```

not:

```text
VERIFIED TRUE
```

A dominant hypothesis remains vulnerable to:

```text
NEW EVIDENCE
NEW HYPOTHESIS
PROVENANCE FAILURE
SCOPE SHIFT
REGIME SHIFT
```

---

# 47. Comparable Support

If two hypotheses have materially comparable evidence:

```text
H1 ≈ H2
```

the correct state is:

```text
COMPETING
```

unless a decision rule explicitly permits provisional action.

---

# 48. Incomparable Support

Evidence may be strong but incomparable.

Example:

```text
H1 supported by controlled experiment
H2 supported by field observation in different regime
```

Do not force these into a single scalar without a justified comparison model.

---

# 49. Conflict Registry Integration

Material unresolved hypothesis conflicts should bind to:

```text
CONFLICT_REGISTRY
```

Conceptually:

```text
H1
↘
 CONFLICT_ID
↗
H2
```

The hypothesis kernel manages competition.

The conflict registry preserves the incompatibility as a governed artifact.

---

# 50. Source Registry Integration

Every load-bearing evidence source should resolve through:

```text
SOURCE_REGISTRY
```

where applicable.

This enables:

```text
SOURCE IDENTITY
VERSION
FRESHNESS
PROVENANCE
INDEPENDENCE
DEPENDENCY
```

checks.

---

# 51. Source Lineage Integration

`SOURCE_LINEAGE` determines ancestry relationships.

This is essential for detecting false independent support.

---

# 52. RSCF Integration

Each hypothesis may be represented as an RSCF.

Conceptually:

```text
RSCF_H1
RSCF_H2
RSCF_H3
```

Each carries:

```text
CLAIM
PREMISES
EVIDENCE
PROVENANCE
SCOPE
REGIME
FALSIFIERS
DEPENDENCIES
CONFIDENCE CEILING
```

---

# 53. Multi-RSCF Competition

The kernel may reason over:

```text
RSCF_SET =
{
  H1,
  H2,
  ...
  Hn
}
```

A change to shared evidence may require atomic re-evaluation of several hypothesis states.

---

# 54. Atomic Hypothesis Update

If a new observation changes relative support across multiple hypotheses:

```text
E_NEW
↓
H1 downgrade
H2 upgrade
H3 invalidate
```

the resulting hypothesis set should remain internally coherent.

A partially updated set can misrepresent relative support.

---

# 55. Multi-Hypothesis State

Conceptually:

```yaml
hypothesis_set:
  set_id:
  question:

  hypotheses: []

  shared_evidence: []
  discriminating_evidence: []

  shared_dependencies: []
  conflicts: []

  scope:
  regime:
  freshness:

  current_state:
  preferred_discriminator:

  unresolved_gaps: []
```

---

# 56. Hypothesis Set States

Recommended set states:

```text
OPEN
COMPETING
PARTIALLY_DISCRIMINATED
DOMINANT_HYPOTHESIS
RESOLVED_FOR_SCOPE
ALL_REJECTED
UNKNOWN/GAP
```

---

# 57. OPEN

`OPEN` means:

```text
hypothesis construction or evidence binding remains incomplete
```

Do not interpret it as epistemic failure.

---

# 58. COMPETING

`COMPETING` means:

```text
two or more incompatible hypotheses remain materially viable
```

This is a legitimate stable state.

---

# 59. PARTIALLY_DISCRIMINATED

Example:

```text
H1 rejected
H2 viable
H3 viable
```

The competition narrows but is not resolved.

---

# 60. DOMINANT_HYPOTHESIS

Use when one hypothesis has substantially stronger support but meaningful alternatives remain.

The output should still expose those alternatives where decision-relevant.

---

# 61. RESOLVED_FOR_SCOPE

Resolution must be scoped.

```text
RESOLVED
FOR
SCOPE S
REGIME R
TIME T
```

does not imply universal resolution.

---

# 62. ALL_REJECTED

If all active hypotheses are invalidated:

```text
STATE = ALL_REJECTED
```

Then:

```text
GENERATE / RETRIEVE NEW HYPOTHESIS
OR
RETURN UNKNOWN/GAP
```

Do not resurrect the least-bad rejected hypothesis merely to fill the gap.

---

# 63. Hypothesis Generation

New hypotheses may originate from:

```text
OBSERVATION
ANOMALY
MECHANISM
COUNTERFACTUAL
MODEL
EXTERNAL SOURCE
FAILURE ANALYSIS
DOMAIN THEORY
```

Generated hypotheses enter as:

```text
MODEL / SOURCE_CLAIM / UNKNOWN
```

according to origin.

Generation is not validation.

---

# 64. Novel Hypothesis Firewall

A newly generated explanation must not gain confidence merely because it is elegant, novel, or internally coherent.

```text
NOVELTY != EVIDENCE
ELEGANCE != EVIDENCE
COMPLEXITY != EVIDENCE
SIMPLICITY != TRUTH
```

---

# 65. Parsimony

When hypotheses explain the evidence equally well and have otherwise comparable support, lower unsupported assumption burden may be preferable as a heuristic.

But:

```text
PARSIMONY
!=
PROOF
```

A more complex hypothesis may be correct.

---

# 66. Explanatory Coverage

A hypothesis may explain more observations than another.

Conceptually:

```text
COVERAGE(H)
=
SUPPORTED OBSERVATIONS EXPLAINED BY H
```

But high coverage alone does not establish causation, independence, or predictive validity.

---

# 67. Contradiction Burden

A hypothesis should record evidence it fails to explain.

```text
UNEXPLAINED OBSERVATIONS
```

must not be hidden merely because the hypothesis explains many other facts.

---

# 68. Exception Burden

A hypothesis requiring many unvalidated exceptions may be fragile.

However:

```text
MORE EXCEPTIONS
!=
AUTOMATICALLY FALSE
```

Some domains are genuinely heterogeneous.

---

# 69. Predictive Discrimination

Where possible, prefer hypotheses making different testable predictions.

```text
H1 → P1
H2 → P2
```

with:

```text
P1 != P2
```

creates a higher-information test opportunity.

---

# 70. Retrodiction Firewall

A hypothesis explaining already-known observations may have weaker discriminating value than one making successful novel predictions.

But:

```text
NOVEL PREDICTION
```

still requires correct measurement, scope, and provenance.

---

# 71. Counterfactual Discrimination

For causal hypotheses:

```text
H1:
do(X) → Y1

H2:
do(X) → Y2
```

an intervention capable of distinguishing `Y1` from `Y2` has high causal decision value.

---

# 72. Sensitivity Analysis

Ask:

```text
WHAT IS THE SMALLEST PREMISE
THAT CHANGES WHICH HYPOTHESIS IS PREFERRED?
```

This identifies the load-bearing discriminator.

---

# 73. Ranking Fragility

If a small plausible change reverses:

```text
H1 > H2
```

into:

```text
H2 > H1
```

then hypothesis ranking is fragile.

Represent:

```text
COMPETING / CONDITIONAL
```

rather than falsely stable ranking.

---

# 74. Robust Dominance

A dominant hypothesis is more robust when it remains preferred under plausible variation of:

```text
NONCRITICAL ASSUMPTIONS
EVIDENCE WEIGHT
SCOPE EDGE CONDITIONS
MODEL PARAMETERS
```

Robust dominance still remains scope-bounded.

---

# 75. Metacognitive Challenge

Before accepting a dominant hypothesis, ask:

```text
WHAT WOULD HAVE TO BE TRUE
FOR THE STRONGEST ALTERNATIVE TO WIN?
```

Then inspect those premises.

This prevents premature lock-in.

---

# 76. Hypothesis Lock-In Firewall

Once a hypothesis becomes preferred, later evidence must still be allowed to challenge it.

```text
CURRENT WINNER
!=
PERMANENT WINNER
```

Avoid interpretation of all later evidence through one locked model.

---

# 77. Confirmation Bias Firewall

For a preferred hypothesis:

```text
SEARCH SUPPORT
```

must be paired where material with:

```text
SEARCH CONTRADICTION
```

and:

```text
SEARCH STRONGER ALTERNATIVE
```

---

# 78. Search Allocation

Evidence gathering should prioritize:

```text
LOAD-BEARING DIFFERENCES
```

between hypotheses.

Do not spend effort collecting facts that all hypotheses already explain.

---

# 79. Information-Value Rule

Conceptually:

```text
VALUE(E)
=
EXPECTED CHANGE IN
CLAIM / DECISION / ACTION
FROM OBSERVING E
```

High-information evidence deserves priority.

---

# 80. Adaptive Complexity

Reasoning depth:

```text
C0 DIRECT
C1 COMPACT
C2 STRUCTURED
C3 DEEP
C4 MAXIMUM
```

should escalate as hypothesis competition becomes more consequential.

---

# 81. Escalation Conditions

Escalate when:

```text
MULTIPLE VIABLE HYPOTHESES
HIGH STAKES
IRREVERSIBLE DECISION
CONFLICTING EVIDENCE
CAUSAL AMBIGUITY
UNKNOWN PROVENANCE INDEPENDENCE
REGIME UNCERTAINTY
STALE EVIDENCE
AMBIGUOUS DEPENDENCIES
GOVERNANCE IMPACT
```

---

# 82. Fast Path

A multi-hypothesis fast path is admissible when:

```text
ONE HYPOTHESIS DOMINATES
AND
MATERIAL ALTERNATIVES HAVE BEEN CHECKED
AND
PROVENANCE INDEPENDENCE IS SUFFICIENT
AND
SCOPE / REGIME / FRESHNESS ARE VALID
AND
NO MATERIAL CONFLICT REMAINS
```

Then local resolution may be sufficient.

---

# 83. Fast-Path Firewall

```text
NO ALTERNATIVE FOUND QUICKLY
!=
NO MATERIAL ALTERNATIVE
```

Fast path cannot skip hypothesis challenge when stakes or ambiguity require it.

---

# 84. H/M/L Retrieval

Hypothesis reasoning should retrieve evidence recursively:

```text
H DOMAIN
↓
M SUBSYSTEM
↓
L MECHANISM / DETAIL
↓
RAW EVIDENCE
```

Only traverse branches capable of changing hypothesis ranking.

---

# 85. Raw Evidence Rule

Raw evidence should be loaded when needed to resolve:

```text
SOURCE AMBIGUITY
EXACT WORDING
CONTRADICTION
PROVENANCE
SCOPE
REGIME
MEASUREMENT
DISCRIMINATING PREDICTION
```

Do not load exhaustive raw evidence by default.

---

# 86. Hypothesis Invalidation

A hypothesis may be invalidated when:

```text
LOAD-BEARING PREMISE FAILS
FALSIFIER TRIGGERS
SCOPE FAILS
REGIME FAILS
CAUSAL MECHANISM FAILS
PREDICTION FAILS
PROVENANCE BASIS FAILS
```

Invalidation must be scoped.

---

# 87. Partial Invalidation

A hypothesis may fail in one scope and survive in another.

Example:

```text
H1 valid for S1
H1 invalid for S2
```

Correct state:

```text
H1 = CONDITIONAL / SCOPED
```

not globally false.

---

# 88. Hypothesis Recovery

A previously rejected hypothesis may re-enter if:

```text
NEW EVIDENCE
NEW REGIME
CORRECTED PROVENANCE
REVISED ASSUMPTION
MEASUREMENT ERROR DISCOVERED
```

changes the load-bearing state.

Historical invalidation should remain traceable.

---

# 89. No Identical Retry

A failed hypothesis path should not simply be reconsidered without changed evidence.

```text
REJECTED H1
+
NO NEW EVIDENCE
+
NO NEW ASSUMPTION
=
DO NOT RE-RUN SAME PATH
```

---

# 90. Decision Use

Hypothesis competition may inform action even before epistemic resolution.

Example:

```text
H1 → action A safest
H2 → action A also safest
```

Then action may be robust despite unresolved explanation.

This is:

```text
DECISION SUFFICIENCY
WITHOUT
EXPLANATORY SUFFICIENCY
```

---

# 91. Decision-Robust Hypothesis Sets

If all viable hypotheses recommend the same reversible action:

```text
ACTION ROBUST
```

may be stronger than any individual explanatory hypothesis.

But the unresolved hypothesis conflict must remain visible.

---

# 92. Divergent Action Sets

If:

```text
H1 → ACTION A
H2 → ACTION B
```

and actions are materially different, discrimination has high decision value.

Escalate evidence gathering before irreversible action where feasible.

---

# 93. Governance Boundary

`K_MULTI_HYPOTHESIS` may determine:

```text
EPISTEMICALLY PREFERRED
```

but not:

```text
AUTHORIZED
```

Canonical law:

```text
BEST-SUPPORTED HYPOTHESIS
!=
AUTHORITY
```

---

# 94. Runtime Boundary

Runtime may execute tests, queries, simulations, or workflows generated from the hypothesis kernel.

But:

```text
KERNEL PROPOSAL
!=
RUNTIME ACTION
```

Execution requires proper authority and tool paths.

---

# 95. Agent Boundary

Multiple agents generating the same hypothesis do not create independent evidence.

```text
AGENT_A → H1
AGENT_B → H1
```

If both use the same source ancestry:

```text
NOT TWO INDEPENDENT CONFIRMATIONS
```

---

# 96. Model Boundary

Multiple models agreeing may still share:

```text
TRAINING DATA
ARCHITECTURAL BIASES
UPSTREAM SOURCES
PROMPT ASSUMPTIONS
```

Model agreement must not automatically be treated as independent empirical confirmation.

---

# 97. Simulation Boundary

Simulation may discriminate hypotheses only relative to the simulation's assumptions.

```text
SIMULATION SUPPORTS H1
```

does not automatically mean:

```text
REAL WORLD VERIFIES H1
```

---

# 98. Formal Proof Boundary

If a hypothesis concerns a formally defined system, formal proof may resolve it within that formal system.

But:

```text
FORMAL MODEL PROOF
!=
EXTERNAL SYSTEM VALIDATION
```

unless model correspondence is independently established.

---

# 99. Multi-Hypothesis Uncertainty Vector

Conceptually:

```text
U_H =
<
U_hypothesis_set,
U_evidence,
U_provenance,
U_independence,
U_scope,
U_regime,
U_temporal,
U_causal,
U_model,
U_discrimination
>
```

Different dimensions require different remedies.

---

# 100. Hypothesis-Set Gap Types

```text
CRITICAL
DECISION-RELEVANT
EXPLANATORY
COSMETIC
```

Examples:

```text
UNKNOWN SOURCE ROOT
→ potentially CRITICAL

UNKNOWN CAUSAL DIRECTION
→ potentially DECISION-RELEVANT

UNKNOWN MINOR MECHANISM
→ EXPLANATORY

MISSING LABEL
→ COSMETIC
```

depending on objective.

---

# 101. Stop Conditions

Multi-hypothesis reasoning may stop when:

```text
CLAIM SUFFICIENCY
AND
DECISION SUFFICIENCY
AND
ACTION SUFFICIENCY
```

are met.

Full explanatory convergence is not always necessary.

---

# 102. Resolution Proof Capsule

A hypothesis resolution should conceptually carry:

```yaml
resolution:
  question:

  winning_hypothesis:
  competing_hypotheses: []

  load_bearing_discriminators: []

  supporting_evidence: []
  contradicting_evidence: []

  provenance_roots: []
  independence_state:

  scope:
  regime:
  temporal_validity:

  falsifiers: []
  invalidation_conditions: []

  confidence_ceiling:
  conclusion_class:
```

---

# 103. Resolution Reuse

A resolution may be reused only while:

```text
DEPENDENCIES VALID
PROVENANCE VALID
SCOPE VALID
REGIME VALID
FRESHNESS VALID
NO NEW MATERIAL HYPOTHESIS
NO NEW MATERIAL CONFLICT
```

Otherwise re-open.

---

# 104. Reopening Condition

A resolved set should reopen when:

```text
NEW EVIDENCE APPEARS
NEW HYPOTHESIS APPEARS
PROVENANCE INDEPENDENCE FAILS
SOURCE IS INVALIDATED
REGIME SHIFTS
SCOPE CHANGES
FALSIFIER TRIGGERS
LOAD-BEARING ASSUMPTION FAILS
```

---

# 105. Multi-Hypothesis Invariants

```text
MH-01
HYPOTHESES MUST REMAIN SEMANTICALLY DISTINCT

MH-02
PARAPHRASES MUST NOT BE COUNTED AS SEPARATE HYPOTHESES

MH-03
PLAUSIBILITY MUST NOT BECOME VERIFICATION

MH-04
ONE SUPPORTED HYPOTHESIS MUST NOT ERASE MATERIAL ALTERNATIVES

MH-05
SOURCE COUNT MUST NOT SUBSTITUTE FOR PROVENANCE INDEPENDENCE

MH-06
MULTIPLE DESCENDANTS MUST NOT BECOME MULTIPLE ROOTS

MH-07
EVIDENCE MUST REMAIN TYPED

MH-08
SHARED EVIDENCE MUST NOT BE MISLABELED AS DISCRIMINATING

MH-09
SCOPE DIFFERENCES MUST NOT BE FORCED INTO GLOBAL CONFLICT

MH-10
REGIME DIFFERENCES MUST NOT BE FORCED INTO GLOBAL CONFLICT

MH-11
CAUSAL HYPOTHESES REQUIRE CAUSALLY APPROPRIATE EVIDENCE

MH-12
CORRELATION MUST NOT SELECT A CAUSAL HYPOTHESIS BY ITSELF

MH-13
STRUCTURAL SIMILARITY MUST NOT SELECT A CAUSAL HYPOTHESIS BY ITSELF

MH-14
COMPETING HYPOTHESES MUST REMAIN COMPETING UNTIL DISCRIMINATED

MH-15
UNKNOWN ALTERNATIVES MUST REMAIN POSSIBLE IN OPEN-WORLD DOMAINS

MH-16
ALL KNOWN HYPOTHESES REJECTED MUST NOT FORCE A WINNER

MH-17
CONFIDENCE MUST RESPECT LOAD-BEARING PREMISES

MH-18
DOMINANT MUST NOT BE EQUATED WITH VERIFIED

MH-19
HYPOTHESIS INVALIDATION MUST BE SCOPE-AWARE

MH-20
FAILED HYPOTHESIS PATHS MUST NOT REPEAT WITHOUT CHANGED EVIDENCE

MH-21
DISCRIMINATING EVIDENCE SHOULD BE PREFERRED OVER REDUNDANT EVIDENCE

MH-22
DECISION ROBUSTNESS MUST REMAIN DISTINCT FROM EXPLANATORY CERTAINTY

MH-23
BEST-SUPPORTED HYPOTHESIS MUST NOT BECOME AUTHORITY

MH-24
UNKNOWN/GAP MUST NOT BECOME FORCED CONVERGENCE

MH-25
RESOLUTION MUST REMAIN REOPENABLE WHEN INVALIDATION CONDITIONS FIRE
```

---

# 106. Failure Modes

```text
FIRST_HYPOTHESIS_LOCK_IN
PARAPHRASE_DUPLICATION
HYPOTHESIS_COLLAPSE
FALSE_EXHAUSTIVENESS
SOURCE_COUNT_BIAS
PROVENANCE_SYBIL
FALSE_INDEPENDENCE
CONFIRMATION_BIAS
CONTRADICTION_SUPPRESSION
FORCED_CONVERGENCE
NAIVE_MAJORITY_RULE
SCOPE_COLLAPSE
REGIME_COLLAPSE
STALE_EVIDENCE_REUSE
CAUSAL_OVERREACH
MODEL_AGREEMENT_OVERREACH
SIMULATION_OVERREACH
NULL_HYPOTHESIS_PRIVILEGE
DOMINANCE_AS_VERIFICATION
OPEN_WORLD_CLOSURE
REDUNDANT_EVIDENCE_ACCUMULATION
BRANCH_EXPLOSION
HYPOTHESIS_RESURRECTION_WITHOUT_NEW_EVIDENCE
AUTHORITY_LEAKAGE
```

---

# 107. Conceptual Evaluation Algorithm

```python
def evaluate_hypothesis_set(hypothesis_set, context):
    hypotheses = normalize_hypotheses(
        hypothesis_set.hypotheses
    )

    hypotheses = remove_semantic_duplicates(
        hypotheses
    )

    for hypothesis in hypotheses:
        bind_evidence(hypothesis)
        resolve_provenance(hypothesis)
        check_scope(hypothesis, context)
        check_regime(hypothesis, context)
        check_freshness(hypothesis, context)
        map_dependencies(hypothesis)
        identify_falsifiers(hypothesis)

    detect_shared_ancestry(hypotheses)
    detect_material_conflicts(hypotheses)

    viable = [
        h for h in hypotheses
        if not falsified_for_scope(h)
    ]

    if not viable:
        return UNKNOWN_GAP

    if len(viable) == 1:
        return validate_single_remaining_hypothesis(
            viable[0]
        )

    discriminator = select_high_information_test(
        viable
    )

    if discriminator is None:
        return COMPETING

    return {
        "state": "COMPETING",
        "hypotheses": viable,
        "preferred_discriminator": discriminator,
    }
```

This is architectural pseudocode, not a claim of deployed implementation.

---

# 108. Hypothesis Update Algorithm

Conceptually:

```text
NEW EVIDENCE
↓
IDENTIFY SOURCE + PROVENANCE
↓
CLASSIFY EVIDENCE TYPE
↓
MAP TO HYPOTHESES
↓
UPDATE SUPPORT / CONTRADICTION EDGES
↓
CHECK SHARED ANCESTRY
↓
CHECK SCOPE / REGIME / FRESHNESS
↓
RECOMPUTE ONLY AFFECTED HYPOTHESES
↓
UPDATE SET STATE
```

This preserves local reasoning and selective invalidation.

---

# 109. Current Lifecycle

```text
PLACEHOLDER
↓
AMOS_MODEL
↓
SOURCE_BOUND
↓
IMPLEMENTED
↓
TESTED
↓
VALIDATED
↓
AUTHORIZED
```

These are separate states.

```text
DOCUMENTED
!=
IMPLEMENTED

IMPLEMENTED
!=
TESTED

TESTED
!=
VALIDATED

VALIDATED
!=
AUTHORIZED
```

---

# 110. Promotion Gate

Before promotion beyond `AMOS_MODEL`:

```text
[ ] canonical multi-hypothesis lineage bound
[ ] hypothesis identity semantics confirmed
[ ] hypothesis-set semantics confirmed
[ ] evidence typing confirmed
[ ] provenance topology integration confirmed
[ ] source independence rules confirmed
[ ] scope partition semantics confirmed
[ ] regime partition semantics confirmed
[ ] freshness behavior confirmed
[ ] causal-hypothesis behavior confirmed
[ ] counterfactual integration confirmed
[ ] falsifier semantics confirmed
[ ] discriminating-test semantics confirmed
[ ] sensitivity semantics confirmed
[ ] open-world handling confirmed
[ ] atomic multi-RSCF update behavior confirmed
[ ] selective invalidation tested
[ ] resolution reopening tested
[ ] negative tests implemented
[ ] unresolved conflicts registered
```

Until these are evidenced:

```text
IMPLEMENTATION_STATUS = UNKNOWN/GAP
```

---

# 111. Required Tests

Future verification should include:

```text
SEMANTIC-DUPLICATE HYPOTHESIS TEST
FIRST-HYPOTHESIS LOCK-IN TEST
MULTIPLE-INDEPENDENT-HYPOTHESIS TEST
SHARED-PROVENANCE TEST
FALSE-INDEPENDENCE TEST
SOURCE-COUNT BIAS TEST
SCOPE-PARTITION TEST
REGIME-PARTITION TEST
FRESHNESS TEST
NULL-HYPOTHESIS TEST
CAUSAL-COMPETITION TEST
COUNTERFACTUAL-DISCRIMINATION TEST
SHARED-EVIDENCE TEST
DISCRIMINATING-EVIDENCE TEST
FALSIFIER TEST
OPEN-WORLD TEST
ALL-HYPOTHESES-REJECTED TEST
SENSITIVITY TEST
DOMINANCE-FRAGILITY TEST
SELECTIVE-INVALIDATION TEST
RESOLUTION-REOPENING TEST
AUTHORITY-FIREWALL TEST
```

---

# 112. Negative Tests

```text
FIRST PLAUSIBLE HYPOTHESIS
→
WINNER
MUST FAIL

TEN COPIES SUPPORT H1
ONE INDEPENDENT SOURCE SUPPORTS H2
→
10:1 INDEPENDENT SUPPORT
MUST FAIL

H1 VALID IN R1
H2 VALID IN R2
→
DIRECT GLOBAL CONTRADICTION
MUST FAIL

CORRELATION
→
SELECT H1 CAUSAL
MUST FAIL

ALL KNOWN HYPOTHESES REJECTED
→
LEAST BAD HYPOTHESIS TRUE
MUST FAIL

DOMINANT HYPOTHESIS
→
VERIFIED
MUST FAIL

MULTIPLE AGENTS AGREE
→
INDEPENDENT CONFIRMATION
MUST FAIL

SIMULATION SUPPORT
→
REAL-WORLD VERIFICATION
MUST FAIL

NO ALTERNATIVE FOUND
→
NO ALTERNATIVE EXISTS
MUST FAIL

COMPETING
→
FORCED CONVERGENCE
MUST FAIL

MODEL
→
AUTHORITY
MUST FAIL
```

---

# 113. Integrity Note

This artifact replaces an empty repository placeholder with a structured AMOS v4.4-aligned multi-hypothesis reasoning contract.

Its load-bearing architecture is consistent with the AMOS lineage principles of:

```text
COMPETING HYPOTHESES
PROVENANCE TOPOLOGY
SYBIL HARDENING
EPISTEMIC REGIMES
CAUSAL FIREWALLS
RSCF DEPENDENCY
H/M/L RETRIEVAL
ADVERSARIAL VALIDATION
SENSITIVITY
SELECTIVE INVALIDATION
SMALLEST SUFFICIENT PROOF
```

However, this document does **not** independently prove that an exact historical executable kernel under the name `K_MULTI_HYPOTHESIS` already existed with this complete specification.

Therefore:

```text
DOCUMENT_CLASS = AMOS_MODEL
IMPLEMENTATION = UNKNOWN/GAP
EMPIRICAL_VALIDATION = UNKNOWN/GAP
RUNTIME_AUTHORITY = NONE
```

until canonical source lineage, implementation evidence, tests, and governance promotion establish stronger status.

---

# 114. RSCF Node

```RSCF-NODE
node_id: AMOS-OS-K-MULTI-HYPOTHESIS
node_type: kernel_multi_hypothesis_contract
domain: AMOS_OS_KERNEL
functional_type: MultiHypothesisKernel
lifecycle_stage: Architecture
claim_class: AMOS_MODEL

RSCF-RELATIONS:
  - INDEXED_BY: KERNEL_MAP

  - GOVERNED_BY: AMOS_CORE_LAWS
  - CONSTRAINED_BY: INVARIANT_REGISTRY
  - PRECEDENCE_GOVERNED_BY: LAW_HIERARCHY
  - AUTHORITY_GOVERNED_BY: AUTHORITY_CANON
  - HML_GOVERNED_BY: HML_CANON

  - PROVENANCE_GOVERNED_BY: CANON_PROVENANCE
  - LINEAGE_TRACKED_BY: SOURCE_LINEAGE
  - SOURCES_REGISTERED_BY: SOURCE_REGISTRY
  - CONFLICTS_TRACKED_BY: CONFLICT_REGISTRY
  - EVOLUTION_TRACKED_BY: SUPERSESSION_LOG

  - LOGIC_DEPENDS_ON: K_CORE19_LOGIC
  - META_LOGIC_DEPENDS_ON: K_META_LOGIC
  - SEMANTICS_DEPEND_ON: K_DISTINCTION_RELATION_CONSTRAINT
  - PRECEDENCE_DEPENDS_ON: K_LAW_HIERARCHY

  - COUNTERFACTUAL_INTERACTS_WITH: K_COUNTERFACTUAL
  - METACOGNITION_INTERACTS_WITH: K_METACOGNITION

  - EPISTEMIC_DEPENDS_ON: README
  - PROVENANCE_DEPENDS_ON: README
  - CAUSAL_DEPENDS_ON: README
  - DEPENDENCY_DEPENDS_ON: README
  - STATE_INTERACTS_WITH: README
  - ATOMICITY_INTERACTS_WITH: README
  - VALIDATED_BY: README
  - RECOVERY_INTERACTS_WITH: README

  - AUTHORIZED_THROUGH: CONTROL_PLANE_MAP
  - EXECUTED_THROUGH: RUNTIME_MAP
  - KNOWLEDGE_BOUND_TO: 11_KNOWLEDGE/00_AMOS_Full_Brain_OS_Architecture
  - STATE_RECORDED_IN: AUTHORITATIVE_STATE
  - OBSERVED_BY: README
  - VERIFIED_BY: README
```

---

# 115. Canonical Summary

```text
OBSERVATION / QUESTION
↓
IDENTIFY MATERIAL HYPOTHESES
↓
NORMALIZE SEMANTICS
↓
REMOVE DUPLICATE PARAPHRASES
↓
BIND EVIDENCE
↓
BIND PROVENANCE
↓
CHECK INDEPENDENCE
↓
CHECK SCOPE
↓
CHECK REGIME
↓
CHECK FRESHNESS
↓
MAP SUPPORT + CONTRADICTION
↓
MAP SHARED ASSUMPTIONS
↓
GENERATE PREDICTIONS / FALSIFIERS
↓
SEEK CHEAPEST HIGH-INFORMATION DISCRIMINATOR
↓
ADVERSARIALLY CHALLENGE CURRENT WINNER
↓
RESOLVE FOR SCOPE
OR
PRESERVE COMPETING
OR
UNKNOWN/GAP
```

Core laws:

```text
HYPOTHESIS != FACT

PLAUSIBLE != VERIFIED

DOMINANT != VERIFIED

REPETITION != INDEPENDENCE

DOCUMENT COUNT != INDEPENDENT ROOT COUNT

AGENT AGREEMENT != INDEPENDENT CONFIRMATION

MODEL AGREEMENT != EMPIRICAL CONFIRMATION

SHARED EVIDENCE != DISCRIMINATING EVIDENCE

SCOPE DIFFERENCE != GLOBAL CONTRADICTION

REGIME DIFFERENCE != GLOBAL CONTRADICTION

CORRELATION != CAUSATION

STRUCTURAL SIMILARITY != CAUSATION

NO ALTERNATIVE FOUND != NO ALTERNATIVE EXISTS

ALL KNOWN HYPOTHESES REJECTED != REMAINING HYPOTHESIS TRUE

COMPETING != FAILURE

UNKNOWN/GAP != PASS

BEST-SUPPORTED HYPOTHESIS != AUTHORITY

RESOLUTION MUST REMAIN REOPENABLE
```

Canonical objective:

```text
DO NOT FALL IN LOVE WITH THE FIRST EXPLANATION.

DO NOT COUNT COPIES AS CONFIRMATION.

DO NOT COUNT AGENTS AS INDEPENDENT SOURCES
WHEN THEY SHARE ANCESTRY.

DO NOT FORCE ONE HYPOTHESIS
WHEN MULTIPLE REMAIN VIABLE.

KEEP CLAIM,
EVIDENCE,
SOURCE,
PROVENANCE,
SCOPE,
REGIME,
AND CAUSAL TYPE
DISTINCT.

ASK WHICH OBSERVATION
WOULD MOST CHEAPLY
SEPARATE THE SURVIVING HYPOTHESES.

CHALLENGE THE CURRENT WINNER
WITH THE STRONGEST SUPPORTED ALTERNATIVE.

RESOLVE ONLY
TO THE SCOPE SUPPORTED BY EVIDENCE.

WHEN EVIDENCE CANNOT DISCRIMINATE:

COMPETING.

WHEN THE ACTIVE HYPOTHESIS SET
IS INSUFFICIENT:

UNKNOWN/GAP.
```

## Related

[[README]] ·
[[ARCHITECTURE]] ·
[[SYSTEM_MAP]] ·
[[PLACEMENT_RULES]] ·
[[CANON_MAP]] ·
[[AMOS_CORE_LAWS]] ·
[[INVARIANT_REGISTRY]] ·
[[LAW_HIERARCHY]] ·
[[HML_CANON]] ·
[[AUTHORITY_CANON]] ·
[[CANON_PROVENANCE]] ·
[[SOURCE_LINEAGE]] ·
[[SOURCE_REGISTRY]] ·
[[CONFLICT_REGISTRY]] ·
[[SUPERSESSION_LOG]] ·
[[README]] ·
[[KERNEL_MAP]] ·
[[K_CORE19_LOGIC]] ·
[[K_DISTINCTION_RELATION_CONSTRAINT]] ·
[[K_LAW_HIERARCHY]] ·
[[K_META_LOGIC]] ·
[[K_COUNTERFACTUAL]] ·
[[K_METACOGNITION]] ·
[[README]] ·
[[README]] ·
[[README]] ·
[[README]] ·
[[README]] ·
[[README]] ·
[[README]] ·
[[README]] ·
[[CONTROL_PLANE_MAP]] ·
[[RUNTIME_MAP]] ·
11_KNOWLEDGE/00_AMOS_Full_Brain_OS_Architecture ·
[[AUTHORITATIVE_STATE]] ·
[[README]] ·
[[README]]

```text
```

---

[[00_ROOT_MOC]]|[[AMOS MOC]]

---
**Related:** [[00_HOME]] · [[AMOS_RSCF_NODES]]

---
**MOC:** [[02_COGNITION_MOC]]
