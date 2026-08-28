````markdown
---
title: "EPISTEMIC_REGIMES Classification Law"
aliases:
  - "EPISTEMIC_REGIMES"
  - "Epistemic Regimes"
  - "Epistemic Regimes Classification"
  - "Epistemic Classification Law"
type: core_law
source: 01_CANON/01_CORE_LAWS
tags:
  - core_law
  - epistemic
  - epistemic_regimes
  - classification
  - knowledge_class
  - source_claim
  - observation
  - derived
  - model
  - provenance
  - evidence
  - scope
  - regime
  - confidence
  - rscf
  - core_laws
  - canon
  - canon/universe

rscf:
  state: SOURCE_CLAIM
  claim_class: AMOS_MODEL
  provenance: AMOS_corpus
  scope: core_laws
  node_id: epistemic_regimes
  node_type: core_law
---

# EPISTEMIC_REGIMES Classification Law

> [!abstract]
> Governs the four discrete knowledge classes:
>
> **SOURCE_CLAIM · OBSERVATION · DERIVED · MODEL**
>
> The law exists to prevent claims with materially different epistemic
> origins from being silently treated as equivalent.

---

# 0. Status

```yaml
status:
  node_id: epistemic_regimes
  node_type: core_law
  state: SOURCE_CLAIM
  claim_class: AMOS_MODEL
  provenance: AMOS_corpus
  scope: core_laws

  governing_classes:
    - SOURCE_CLAIM
    - OBSERVATION
    - DERIVED
    - MODEL

  canonical_function:
    - epistemic_classification
    - provenance_preservation
    - inference_boundary_control
    - evidence_typing
    - model_boundary_control
````

The supplied source establishes four discrete knowledge classes:

```text
SOURCE_CLAIM
OBSERVATION
DERIVED
MODEL
```

These four classes form the classification surface of this law.

They must not be silently collapsed into one generic category such as
"knowledge", "fact", "evidence", or "truth".

---

# 1. Core Law

Every material knowledge object governed by this classification law
must be represented according to the epistemic origin that actually
supports it.

Canonical class set:

$$
K_{class}
\in
\{
SOURCE\_CLAIM,\;
OBSERVATION,\;
DERIVED,\;
MODEL
\}
$$

Normalized classifier:

$$
Classify(K)
\rightarrow
\{
SOURCE\_CLAIM,\;
OBSERVATION,\;
DERIVED,\;
MODEL
\}
$$

This mathematical notation is a normalized representation of the
supplied four-class statement.

It does not add a fifth source-defined class.

---

# 2. Classification Principle

The classification question is not:

> "How convincing does this statement sound?"

It is:

> "What kind of epistemic object is this, given how it was obtained?"

Therefore:

```text
CLASS
!= RHETORICAL CONFIDENCE
```

and:

```text
CLASS
!= POPULARITY
```

and:

```text
CLASS
!= AUTHORITY
```

and:

```text
CLASS
!= TRUTH VALUE
```

The class records epistemic origin/type.

It does not by itself certify correctness.

---

# 3. The Four Classes

```text
                 EPISTEMIC_REGIMES
                        |
        +---------------+---------------+
        |               |               |
        v               v               v
 SOURCE_CLAIM      OBSERVATION       DERIVED
                                        |
                                        |
                                        v
                                      MODEL
```

The diagram shows the four governed categories only.

It does **not** imply a canonical hierarchy between them.

The classes are distinct types, not automatically ranks.

---

# 4. SOURCE_CLAIM

## 4.1 Definition

`SOURCE_CLAIM` identifies a proposition whose immediate epistemic basis
is that a source asserts, records, reports, specifies, or declares it.

Normalized form:

$$
SOURCE\_CLAIM(S,C)
$$

means:

```text
Source S claims C
```

It does not automatically mean:

```text
C is independently verified
```

---

# 5. SOURCE_CLAIM Core Boundary

The canonical integrity distinction is:

```text
SOURCE S SAYS X
```

versus:

```text
X IS VERIFIED
```

These are not equivalent.

Therefore:

$$
SOURCE\_CLAIM(X)
\nRightarrow
VERIFIED(X)
$$

A source may be:

* accurate;
* inaccurate;
* incomplete;
* stale;
* scoped;
* ambiguous;
* internally inconsistent;
* downstream of another source;
* authoritative within one domain but not another.

Classification preserves this distinction.

---

# 6. SOURCE_CLAIM Examples

```yaml
examples:

  - statement: "The specification says the system uses protocol X."
    class: SOURCE_CLAIM

  - statement: "The README reports 21/21 tests passing."
    class: SOURCE_CLAIM

  - statement: "The architecture document labels this component validated."
    class: SOURCE_CLAIM

  - statement: "The paper reports a 94% benchmark result."
    class: SOURCE_CLAIM

  - statement: "The vendor documentation lists a latency of 20 ms."
    class: SOURCE_CLAIM
```

Unless the relevant underlying evidence is independently inspected,
these remain claims about what a source reports.

---

# 7. Source Authority Does Not Change Class

A source may be highly authoritative.

That does not transform the source relationship itself.

Example:

```text
AUTHORITATIVE SOURCE
        |
        v
      CLAIM X
```

The epistemic object:

```text
"Authoritative source states X"
```

is still source-grounded.

Authority can affect trust assessment.

It does not erase provenance.

---

# 8. Multiple Sources

Suppose:

```text
SOURCE A ---> CLAIM X
SOURCE B ---> CLAIM X
SOURCE C ---> CLAIM X
```

This may increase support only if their evidentiary relationships are
relevant and sufficiently independent.

If instead:

```text
             ORIGINAL SOURCE
             /      |      \
            v       v       v
         SOURCE A SOURCE B SOURCE C
             \      |      /
                    X
```

then three repetitions do not necessarily represent three independent
confirmations.

Therefore:

```text
SOURCE COUNT
!=
INDEPENDENT PROVENANCE COUNT
```

---

# 9. SOURCE_CLAIM Provenance Requirement

A useful source claim should preserve enough provenance to answer:

```text
WHO OR WHAT MADE THE CLAIM?
WHERE?
WHEN?
UNDER WHAT SCOPE?
UNDER WHAT REGIME?
FROM WHAT UPSTREAM SOURCE?
```

Conceptual representation:

```yaml
source_claim:
  claim: C
  source_identity: S
  source_location: optional
  source_time: optional
  source_version: optional
  source_ancestry: optional
  scope: optional
  regime: optional
  freshness: optional
```

The exact schema is not established by the terse source law.

This is an integration model.

---

# 10. OBSERVATION

## 10.1 Definition

`OBSERVATION` identifies a directly recorded measurement, inspection,
event, state, or result produced through an observation process.

Normalized form:

$$
OBSERVATION(O)
$$

where \(O\) is tied to an observation context.

An observation should preserve its measurement conditions where those
conditions can change interpretation.

---

# 11. Observation Boundary

An observation is not interpretation.

```text
OBSERVED:
temperature sensor returned 80°C
```

is distinct from:

```text
INTERPRETED:
the system is overheating
```

The first may be an observation.

The second requires additional reasoning, thresholds, or model
assumptions.

Therefore:

```text
OBSERVATION
!= INTERPRETATION
```

---

# 12. Observation Does Not Guarantee Accuracy

A direct observation may still be affected by:

* measurement error;
* calibration error;
* instrumentation failure;
* sampling bias;
* logging defects;
* contamination;
* environmental mismatch;
* observer error;
* corrupted state;
* incomplete capture.

Therefore:

$$
OBSERVATION(X)
\nRightarrow
INFALLIBLE(X)
$$

The class describes how the information was obtained.

It does not guarantee perfect measurement.

---

# 13. Observation Context

An observation without context may be unusable.

Conceptually:

```yaml
observation:
  value: O
  measurement_method: M
  environment: E
  time: T
  scope: S
  instrument: optional
  calibration: optional
  uncertainty: optional
```

For example:

```text
Latency = 20 ms
```

without:

```text
hardware
network
workload
sample size
percentile
runtime version
measurement method
```

does not license universal latency claims.

---

# 14. Observation Examples

```yaml
examples:

  - statement: "The measured response time in this run was 42 ms."
    class: OBSERVATION

  - statement: "The test execution returned PASS."
    class: OBSERVATION

  - statement: "The inspected file contains 1,578 lines."
    class: OBSERVATION

  - statement: "The current registry value is version 17."
    class: OBSERVATION
```

provided the values were actually inspected or measured.

If merely reported by another document:

```text
SOURCE_CLAIM
```

may instead be the correct class.

---

# 15. Source Claim vs Observation

Critical distinction:

```text
DOCUMENT SAYS:
"21 tests passed"
```

Classification:

```text
SOURCE_CLAIM
```

If the test suite is actually executed and the runtime result is
directly captured:

```text
21 passed
```

Classification:

```text
OBSERVATION
```

The textual proposition may look identical.

Its epistemic class differs because its provenance differs.

---

# 16. OBSERVATION Scope

Observation inherits its observation envelope.

If:

```text
OBSERVATION O
```

was produced under:

```text
Environment = E1
Time = T1
Version = V1
Population = P1
```

then:

```text
O applies universally
```

does not follow.

Therefore:

$$
Observation(E_1)
\nRightarrow
Universal(E)
$$

without an appropriate generalization argument.

---

# 17. DERIVED

## 17.1 Definition

`DERIVED` identifies a conclusion obtained from one or more premises
through an explicit or reconstructable inference.

Normalized:

$$
P_1,P_2,\ldots,P_n
\vdash
D
$$

where:

```text
D = DERIVED
```

The epistemic status of D depends on:

* its premises;
* inference validity;
* dependency closure;
* scope compatibility;
* regime compatibility;
* freshness;
* provenance topology where relevant.

---

# 18. Derived Claim Dependency Law

A derived claim must preserve its dependency relationship.

Conceptually:

```text
P1 ----\
P2 -----\
P3 ------> DERIVATION ---> D
P4 -----/
```

If a load-bearing premise fails:

```text
P2 -> INVALID
```

then every dependent conclusion requiring P2 must be reconsidered.

Preferred invalidation:

```text
P2
 |
 +--> D1
 |     |
 |     +--> D3
 |
 +--> D2
```

Invalidate:

```text
D1
D2
D3
```

where dependent.

Do not invalidate unrelated claims.

---

# 19. Weakest Load-Bearing Premise

Derived confidence cannot silently exceed the weakest load-bearing
premise unless independent revalidation changes the support structure.

Normalized integrity rule:

$$
Confidence(D)
\leq
\min_{P_i \in LB(D)}
Confidence(P_i)
$$

where:

$$
LB(D)
=
\text{load-bearing premises of }D
$$

unless D obtains additional independent support.

---

# 20. Derived Does Not Mean Certain

A conclusion can be logically derived from uncertain premises.

Example:

```text
P1 = CONDITIONAL
P2 = SOURCE_CLAIM
P3 = OBSERVATION
```

Then a downstream result cannot be promoted merely because the
reasoning is internally coherent.

```text
VALID INFERENCE
+
UNCERTAIN PREMISE
=
UNCERTAINTY PRESERVED
```

---

# 21. Derived Claim Examples

```yaml
examples:

  - premises:
      - "Observed state version is 17."
      - "Transaction expected state version 16."
    conclusion:
      - "The expected-state check mismatches."
    class: DERIVED

  - premises:
      - "Source A and Source B share the same upstream origin."
    conclusion:
      - "Their agreement does not establish two independent confirmations."
    class: DERIVED

  - premises:
      - "Claim C depends on premise P."
      - "P has been invalidated."
    conclusion:
      - "C requires invalidation or revalidation."
    class: DERIVED
```

---

# 22. Derivation Trace

A high-integrity derived claim should be able to expose a compact
dependency trace without requiring hidden chain-of-thought.

For example:

```yaml
derived_claim:
  claim: D
  premises:
    - P1
    - P2
  inference_rule: R
  dependencies:
    - P1
    - P2
  scope: S
  regime: E
  confidence_ceiling: C
```

This preserves proof structure without requiring private reasoning
transcripts.

---

# 23. DERIVED vs OBSERVATION

```text
OBSERVATION:
"The transaction returned conflict."
```

versus:

```text
DERIVED:
"The conflict occurred because expected state differed from current
state."
```

The second statement adds explanatory inference.

Unless the mechanism is directly established, it must not inherit the
observation class merely because it explains an observation.

---

# 24. DERIVED vs SOURCE_CLAIM

Suppose a source says:

```text
A causes B.
```

Recording:

```text
"Source S claims A causes B."
```

is:

```text
SOURCE_CLAIM
```

Independently reasoning from evidence to:

```text
A causes B
```

would be:

```text
DERIVED
```

but only if the evidence licenses causal inference.

The same sentence can therefore have different epistemic classes
depending on how it is supported.

---

# 25. MODEL

## 25.1 Definition

`MODEL` identifies a representational, explanatory, predictive,
architectural, analogical, or hypothetical structure used to organize
or reason about a domain without asserting that the structure itself
has been independently established as empirical reality.

Normalized:

$$
M : X \rightarrow Y
$$

or more generally:

$$
MODEL
=
Representation(domain,\ assumptions,\ structure)
$$

A model can be useful without being universally true.

---

# 26. Model Boundary

The essential firewall is:

```text
MODEL
!= VERIFIED REALITY
```

and:

```text
STRUCTURAL SIMILARITY
!= CAUSATION
```

and:

```text
ARCHITECTURAL ANALOGY
!= LITERAL IMPLEMENTATION
```

A model may describe:

* expected behavior;
* desired architecture;
* explanatory structure;
* conceptual mapping;
* simulation;
* hypothetical mechanism;
* abstraction;
* analogy.

These must remain distinguishable from observations.

---

# 27. MODEL Examples

```yaml
examples:

  - statement: >
      Treat the reasoning system as an MVCC-style transaction engine.
    class: MODEL

  - statement: >
      Adaptive optionality can be represented as a function of repair
      capacity relative to degradation.
    class: MODEL

  - statement: >
      The architecture can be decomposed into D/M/E/R primitives.
    class: MODEL

  - statement: >
      A causal epoch can be modeled as a monotonic lineage boundary.
    class: MODEL
```

unless stronger canon or empirical evidence establishes another class.

---

# 28. Model Predictions

A model can generate predictions.

```text
MODEL M
   |
   v
PREDICTION P
   |
   v
TEST
   |
   +--> OBSERVATION O
```

Agreement between P and O may support M.

But:

```text
one successful prediction
```

does not automatically establish:

```text
universal model validity
```

The applicability envelope remains material.

---

# 29. Model Validation

Model validation is itself evidence-dependent.

Possible pattern:

```text
MODEL
  |
  +--> prediction P1
  +--> prediction P2
  +--> prediction P3
          |
          v
      observations
```

The model may gain support if predictions survive meaningful tests.

However:

```text
SUPPORTED MODEL
!= UNIVERSAL LAW
```

unless the evidence justifies that stronger conclusion.

---

# 30. Model Falsifiers

A useful model should expose conditions capable of defeating it.

Conceptually:

```yaml
model:
  claim: M
  assumptions:
    - A1
    - A2
  predictions:
    - P1
  falsifiers:
    - F1
    - F2
```

A model without any possible invalidation condition risks becoming
unfalsifiable narrative rather than decision-useful structure.

---

# 31. Four-Class Comparison

| Class          | Immediate Basis               | Core Question                                     | Does Class Imply Truth? |
| -------------- | ----------------------------- | ------------------------------------------------- | ----------------------- |
| `SOURCE_CLAIM` | source assertion              | Who/what says this?                               | No                      |
| `OBSERVATION`  | direct measurement/inspection | What was observed?                                | No                      |
| `DERIVED`      | inference from premises       | What follows from these premises?                 | No                      |
| `MODEL`        | representational structure    | What framework represents/explains/predicts this? | No                      |

No class automatically means:

```text
TRUE
```

The classes encode epistemic type.

---

# 32. Classes Are Not Confidence Levels

Incorrect:

```text
SOURCE_CLAIM = low confidence
OBSERVATION = medium confidence
DERIVED = high confidence
MODEL = speculative
```

This mapping is not valid.

A high-quality source claim can have substantial support.

A corrupted observation can be weak.

A mathematically sound derivation can be strong.

A mature model can be highly predictive.

Class and confidence must therefore remain separate variables.

---

# 33. Classification vs Conclusion Class

The four epistemic regimes should not be silently conflated with
conclusion states such as:

```text
VERIFIED
CONDITIONAL
COMPETING
UNKNOWN/GAP
```

These answer different questions.

Conceptually:

```text
EPISTEMIC CLASS:
What kind of knowledge object is this?

CONCLUSION STATUS:
How strongly may we currently conclude it?
```

A claim can therefore conceptually be:

```yaml
epistemic_class: MODEL
conclusion_status: CONDITIONAL
```

or:

```yaml
epistemic_class: OBSERVATION
conclusion_status: VERIFIED
```

if the surrounding canon defines and supports that status.

---

# 34. Classification vs RSCF State

Likewise:

```text
SOURCE_CLAIM
```

can appear both as an epistemic classification term and as an RSCF
state in corpus metadata.

Those uses must not be assumed semantically identical without the
governing RSCF schema.

This node's supplied RSCF metadata states:

```yaml
state: SOURCE_CLAIM
claim_class: AMOS_MODEL
```

That means the node itself is represented as a corpus source claim whose
claim class is AMOS_MODEL.

It does not automatically promote every proposition inside the node to
empirical fact.

---

# 35. Classification Function

Normalized classifier:

```text
INPUT: knowledge object K

1. Is K presently grounded as a report/assertion by a source?
   -> SOURCE_CLAIM

2. Is K a directly inspected/measured result?
   -> OBSERVATION

3. Is K inferred from premises?
   -> DERIVED

4. Is K a representational/explanatory/predictive architecture?
   -> MODEL
```

This is a practical classification heuristic.

The terse supplied law defines the classes but does not provide a
complete executable classifier.

---

# 36. Mixed Claims

A sentence can contain multiple epistemic objects.

Example:

> "The paper reports a 10% improvement, proving the architecture is
> universally superior."

Decomposition:

```text
C1:
"The paper reports a 10% improvement."
-> SOURCE_CLAIM

C2:
"The architecture is universally superior."
-> DERIVED or MODEL-level conclusion depending on intended meaning
```

C2 does not inherit C1's support automatically.

Composite claims should therefore be decomposed when their components
have different epistemic classes.

---

# 37. Atomic Classification

For composite proposition:

$$
C = C_1 \land C_2 \land C_3
$$

classify the meaningful atomic claims separately when their epistemic
origins differ.

Do not force:

```text
Class(C1) = Class(C2) = Class(C3)
```

merely because they occur in one sentence or document.

---

# 38. Provenance Preservation

Every classification should preserve enough provenance to reconstruct
why the class was assigned.

Conceptual topology:

```text
SOURCE
  |
  v
SOURCE_CLAIM
  |
  +--> DERIVED CLAIM
  |        |
  |        v
  |      MODEL
  |
  +--> later OBSERVATION
```

The existence of a downstream node does not erase upstream ancestry.

---

# 39. Provenance Topology

A knowledge graph should distinguish:

```text
DIRECT SOURCE
```

from:

```text
DESCENDANT OF SOURCE
```

Example:

```text
SOURCE A
   |
   v
CLAIM B
   |
   v
SUMMARY C
   |
   v
REPORT D
```

B, C, and D must not be counted as three independent confirmations of
the underlying proposition merely because they occupy separate nodes.

---

# 40. Sybil Hardening

Epistemic classification must resist artificial multiplication of
evidence.

```text
ONE ORIGIN
   |
   +--> COPY 1
   +--> COPY 2
   +--> COPY 3
   +--> COPY 4
```

does not become:

```text
FOUR INDEPENDENT SOURCES
```

Therefore:

$$
Multiplicity
\nRightarrow
Independence
$$

Provenance ancestry matters.

---

# 41. Scope Inheritance

Every material epistemic object should preserve its applicability
envelope.

Relevant dimensions may include:

```yaml
scope_envelope:
  system: optional
  population: optional
  environment: optional
  scale: optional
  time: optional
  regime: optional
  measurement_method: optional
  assumptions: optional
```

A derived claim cannot silently widen beyond its premises.

---

# 42. Scope Rule

If:

$$
Scope(P)=S
$$

and D depends solely on P, then absent a validated generalization:

$$
Scope(D)
\subseteq S
$$

or remains bounded by S.

Therefore:

```text
LOCAL EVIDENCE
!= UNIVERSAL EVIDENCE
```

---

# 43. Regime Firewall

Epistemic classification and epistemic regime are related but distinct.

This node classifies knowledge objects as:

```text
SOURCE_CLAIM
OBSERVATION
DERIVED
MODEL
```

[[L21_EPISTEMIC_REGIME]] governs regime-level applicability.

Examples of regimes may include:

```text
simulation
empirical
canonical
speculative
```

where established by the relevant law.

A class must not silently cross regimes.

---

# 44. Cross-Regime Promotion

Suppose:

```text
MODEL validated in SIMULATION
```

That does not automatically become:

```text
EMPIRICALLY VERIFIED MODEL
```

Similarly:

```text
CANONICAL SPECIFICATION
```

does not automatically become:

```text
OBSERVED RUNTIME IMPLEMENTATION
```

A bridge requires appropriate evidence.

---

# 45. Canon vs Empirical Reality

A canonical law may establish:

```text
AMOS requires X
```

within the corpus.

That is different from establishing:

```text
Every deployed system physically implements X
```

Therefore:

```text
CANONICAL REQUIREMENT
!= EMPIRICAL IMPLEMENTATION PROOF
```

This firewall is especially important for architectural language.

---

# 46. Freshness

Epistemic class alone does not establish current validity.

An observation from time \(t_0\):

```text
OBSERVATION @ t0
```

can become stale relative to a decision at \(t_1\).

Likewise:

```text
SOURCE_CLAIM @ version 1
```

may no longer represent version 2.

Thus:

```text
CLASSIFICATION
!= FRESHNESS
```

---

# 47. Freshness Axes

Where decision-relevant, freshness may require checking:

```text
temporal
environmental
regime
provenance
scope
model
source
```

as governed by the relevant epistemic-regime canon.

A claim can remain correctly classified while becoming stale.

Example:

```yaml
class: OBSERVATION
classification_valid: true
freshness: STALE
```

---

# 48. Causal Firewall

None of the four classes automatically licenses causal inference.

```text
SOURCE_CLAIM:
"A causes B"
```

does not establish causality.

```text
OBSERVATION:
"A occurred before B"
```

does not establish causality.

```text
DERIVED:
"A and B correlate"
```

does not establish causality.

```text
MODEL:
"A mechanistically causes B"
```

does not establish causality unless appropriately validated.

Therefore:

```text
SEQUENCE
!= CAUSE

CORRELATION
!= CAUSE

ANALOGY
!= CAUSE

MODEL MECHANISM
!= VERIFIED CAUSAL EFFECT
```

---

# 49. Evidence Typing for Causality

Causal conclusions should distinguish:

```text
association
correlation
mechanism
enabling condition
necessary condition
sufficient condition
mediation
confounding
feedback
causal effect
```

A generic "related to" observation must not silently become a causal
claim.

Epistemic classification preserves the upstream evidence type needed
to detect such overreach.

---

# 50. Classification Preservation Through Derivation

Suppose:

```text
S1 = SOURCE_CLAIM
O1 = OBSERVATION
```

and:

```text
D1 = derive(S1, O1)
```

Then:

```text
Class(D1) = DERIVED
```

while its provenance still records:

```text
depends_on:
  - S1
  - O1
```

The derived class does not erase the classes of its premises.

---

# 51. Model Built from Derived Claims

Similarly:

```text
S1 -> SOURCE_CLAIM
O1 -> OBSERVATION
D1 -> DERIVED
```

may support:

```text
M1 -> MODEL
```

Topology:

```text
SOURCE_CLAIM ----\
                  \
OBSERVATION --------> DERIVED ----> MODEL
```

The model should preserve this dependency structure.

---

# 52. Model Does Not Retroactively Reclassify Evidence

If model M explains observation O:

```text
O ---> M
```

O remains an observation.

It does not become:

```text
MODEL
```

merely because a model incorporates it.

Likewise, a source claim used by a model remains source-derived in
provenance.

---

# 53. Observation Does Not Retroactively Verify Model

Suppose:

```text
MODEL M predicts O
```

and O is observed.

This may increase support for M.

But:

```text
OBSERVED PREDICTION
```

does not necessarily imply:

```text
MODEL VERIFIED UNIVERSALLY
```

Alternative models may predict the same observation.

Competing explanations must remain visible.

---

# 54. Competing Models

Suppose:

```text
MODEL M1 ---> predicts O
MODEL M2 ---> predicts O
```

and:

```text
OBSERVATION O
```

Then O does not discriminate between M1 and M2.

Correct state:

```text
COMPETING
```

if neither has stronger discriminating evidence.

Do not force convergence.

---

# 55. Discriminating Evidence

When models compete, prefer evidence capable of separating them.

```text
M1 predicts X
M2 predicts NOT X
```

Then observation of X has greater discrimination value than another
observation both models already predict.

Therefore:

```text
HIGH-INFORMATION TEST
>
REDUNDANT CONFIRMATION
```

when decision value is the objective.

---

# 56. UNKNOWN and GAP

The supplied four-class law governs:

```text
SOURCE_CLAIM
OBSERVATION
DERIVED
MODEL
```

It does not explicitly add `UNKNOWN` as a fifth knowledge class.

However, absence of sufficient information must not be forced into one
of the four classes.

Use the relevant gap canon:

[[L27_GAP]]

and:

[[L28_CRITICAL_GAP]]

when classification or support cannot be established.

Therefore:

```text
INSUFFICIENT EVIDENCE
!= MODEL
```

and:

```text
MISSING SOURCE
!= SOURCE_CLAIM
```

and:

```text
NO OBSERVATION
!= OBSERVATION
```

---

# 57. Classification Gap

If the epistemic origin cannot be determined:

```yaml
classification:
  class: UNKNOWN
  reason: provenance_missing
```

may be used as an operational gap representation if supported by the
broader AMOS classification system.

It should not be presented as a fifth canonical class established by
this node.

The four source-established classes remain unchanged.

---

# 58. Gap Priority

Material gaps should be resolved according to decision impact.

```text
CRITICAL
    |
    v
DECISION-RELEVANT
    |
    v
EXPLANATORY
    |
    v
COSMETIC
```

A classification uncertainty is critical when the decision would be
unsafe or invalid under one plausible classification but acceptable
under another.

---

# 59. Classification Conflict

Two validators may disagree:

```text
Validator A -> OBSERVATION
Validator B -> SOURCE_CLAIM
```

Do not resolve by majority vote alone.

Inspect provenance.

Example:

```text
Value came from document report
```

supports:

```text
SOURCE_CLAIM
```

whereas:

```text
Value was directly measured during this execution
```

supports:

```text
OBSERVATION
```

The conflict is resolved by epistemic origin, not label preference.

---

# 60. Misclassification: Source Claim as Observation

Invalid promotion:

```text
README:
"All tests pass."
        |
        v
OBSERVATION
```

Correct without execution evidence:

```text
README:
"All tests pass."
        |
        v
SOURCE_CLAIM
```

The source's confidence does not change this.

---

# 61. Misclassification: Model as Observation

Invalid:

```text
Architecture predicts state X
        |
        v
"X was observed"
```

A prediction is not an observation.

Correct:

```text
MODEL
  |
  v
PREDICTION X
```

until an observation process actually measures X.

---

# 62. Misclassification: Observation as Causal Proof

Invalid:

```text
A observed before B
        |
        v
A CAUSED B
```

Sequence is insufficient.

Correct:

```text
OBSERVATION:
A preceded B
```

plus additional causal evidence if a causal conclusion is required.

---

# 63. Misclassification: Derived as Source Claim

If AMOS infers:

```text
D from P1 + P2
```

D is not a source claim merely because P1 and P2 came from documents.

Correct topology:

```text
SOURCE_CLAIM P1
SOURCE_CLAIM P2
       |
       v
DERIVED D
```

This preserves the inference edge.

---

# 64. Misclassification: Source Claim as Model

A source can itself state a model.

Then two layers exist:

```text
SOURCE S
  |
  v
"S proposes MODEL M"
```

At the outer provenance layer:

```text
SOURCE_CLAIM
```

The embedded object may be:

```text
MODEL
```

Both types should be preserved rather than collapsed.

---

# 65. Nested Epistemic Typing

A useful representation can distinguish:

```yaml
claim:
  text: "Source S proposes architecture M."

  outer_class:
    type: SOURCE_CLAIM

  embedded_object:
    type: MODEL
    id: M
```

Likewise:

```yaml
claim:
  text: "Source S reports observation O."

  outer_class: SOURCE_CLAIM
  embedded_object: OBSERVATION
```

until O is independently observed.

---

# 66. Epistemic Object Identity

A knowledge object should retain stable identity across reclassification
events.

Example:

```text
C1 @ t0:
SOURCE_CLAIM
```

Later independent measurement may produce:

```text
O1 @ t1:
OBSERVATION
```

supporting the same proposition.

Preferred:

```text
C1 SOURCE_CLAIM ----\
                     +--> proposition P
O1 OBSERVATION ------/
```

rather than silently rewriting C1 as an observation.

This preserves causal and provenance history.

---

# 67. No Silent Epistemic Promotion

Never silently transform:

```text
SOURCE_CLAIM
   ->
OBSERVATION
```

or:

```text
MODEL
   ->
VERIFIED REALITY
```

or:

```text
DERIVED
   ->
DIRECT EVIDENCE
```

Promotion requires a new evidentiary event and explicit lineage.

---

# 68. No Silent Epistemic Demotion

Likewise, contradictory later evidence should not erase historical
classification.

If an observation is later discovered to be corrupted:

```text
O1 @ E1 = OBSERVATION
```

preserve the historical record and add:

```text
O1 INVALIDATED @ E2
```

rather than pretending O1 never existed.

This aligns with causal lineage discipline.

---

# 69. Epoch-Aware Classification

Conceptually:

```yaml
epistemic_record:
  claim_id: C
  class: OBSERVATION
  epoch: e_k
  validity:
    from: e_k
    until: e_n
```

If later evidence invalidates C:

```text
e_n:
SUPERSEDE / INVALIDATE
```

not:

```text
rewrite e_k silently
```

The exact epoch schema belongs to the relevant causal-epoch law.

---

# 70. Replayability Boundary

A classification decision may be replayable if the classification
inputs and rules are preserved.

Conceptually:

```text
root inputs
    +
provenance
    +
classification rule
    +
versions
        |
        v
replay classification
```

But:

```text
REPLAYABILITY
!= CORRECTNESS
```

A deterministically replayed misclassification remains a
misclassification.

---

# 71. Atomic Reasoning Boundary

When multiple epistemic objects jointly support one decision:

```text
SOURCE_CLAIM S1
OBSERVATION O1
DERIVED D1
MODEL M1
```

their classes should remain intact inside the reasoning transaction.

Atomic reasoning must not flatten them into:

```text
EVIDENCE = TRUE
```

Instead:

```text
transaction
  |
  +--> S1 : SOURCE_CLAIM
  +--> O1 : OBSERVATION
  +--> D1 : DERIVED
  +--> M1 : MODEL
```

Each contributes according to its actual role.

---

# 72. RSCF Integration

Each RSCF capsule can carry epistemic typing.

Conceptually:

```yaml
rscf:
  claim: C
  epistemic_class: DERIVED
  premises:
    - P1
    - P2
  provenance:
    - S1
  scope: S
  regime: R
  freshness: F
  falsifiers:
    - X
  confidence_ceiling: Cmax
```

The exact RSCF schema remains governed by:

[[L17_RSCF]]

---

# 73. RSCF Classification Invariant

For any material RSCF claim:

```text
RSCF CLAIM
    |
    v
EPISTEMIC CLASS
```

should remain traceable to its epistemic origin.

If the origin cannot be established:

```text
CLASSIFICATION GAP
```

should remain visible.

Do not choose the most flattering class.

---

# 74. Classification and Validation

Validation asks whether the object satisfies relevant checks.

Classification asks what type of epistemic object it is.

Thus:

```text
CLASSIFICATION
!= VALIDATION
```

Example:

```yaml
object:
  class: SOURCE_CLAIM
  validation:
    source_identity: PASS
    freshness: PASS
    independent_confirmation: NOT_ESTABLISHED
```

The source claim can be well-validated *as a source claim* without its
embedded proposition being independently verified.

---

# 75. Classification and Verification

Important distinction:

```text
VERIFY("Source S says X")
```

may succeed.

That verifies:

```text
S says X
```

It does not necessarily verify:

```text
X
```

This distinction is fundamental to provenance-aware reasoning.

---

# 76. Classification and Contradiction

Suppose:

```text
SOURCE A claims X
SOURCE B claims NOT X
```

Correct representation:

```text
S1 = SOURCE_CLAIM(X)
S2 = SOURCE_CLAIM(NOT X)
```

Do not choose one merely to eliminate contradiction.

State:

```text
COMPETING SOURCE CLAIMS
```

until discriminating evidence exists.

---

# 77. Observation Conflict

Suppose:

```text
OBSERVATION O1 -> X
OBSERVATION O2 -> NOT X
```

Possible causes include:

* measurement error;
* different environments;
* different times;
* regime shift;
* different populations;
* instrumentation differences;
* genuine state change.

Therefore:

```text
CONTRADICTORY OBSERVATIONS
```

should trigger scope/provenance/freshness analysis rather than forced
averaging.

---

# 78. Derived Conflict

Suppose two derivations produce:

```text
D1 -> X
D2 -> NOT X
```

Inspect:

```text
premises
inference rules
scope
regime
freshness
provenance
hidden assumptions
```

The conflict may arise because the derivations are valid under
different applicability envelopes.

---

# 79. Model Conflict

Competing models should remain:

```text
MODEL M1
MODEL M2
MODEL M3
```

until evidence discriminates.

Model plurality is not itself a defect.

Premature convergence is.

---

# 80. Evidence Topology

A complete epistemic topology may resemble:

```text
SOURCE A ------------------------+
                                 |
                                 v
                         SOURCE_CLAIM S1
                                 |
                                 |
OBSERVATION O1 ------------------+
                                 |
                                 v
                            DERIVED D1
                              /      \
                             /        \
                            v          v
                        MODEL M1    MODEL M2
```

This structure preserves:

* origin;
* dependency;
* competing interpretations;
* inference boundaries.

---

# 81. Provenance Independence Test

Before treating multiple claims as independent support, ask:

```text
Do they share:
- source ancestry?
- dataset ancestry?
- model ancestry?
- measurement pipeline?
- benchmark?
- runtime?
- authoring chain?
- common assumptions?
```

If yes, correlation risk must remain visible.

Independence must be demonstrated rather than assumed.

---

# 82. Source Repetition Rule

If ten documents repeat the same unsupported claim from one origin:

$$
IndependentEvidence \neq 10
$$

Potentially:

$$
IndependentOrigin = 1
$$

depending on actual ancestry.

Therefore:

```text
REPETITION
!= VALIDATION
```

---

# 83. Benchmark Boundary

A benchmark result may begin as:

```text
SOURCE_CLAIM
```

if merely reported.

It may become:

```text
OBSERVATION
```

for a directly executed benchmark run.

Any general conclusion such as:

```text
system is universally superior
```

is:

```text
DERIVED
```

and must respect benchmark scope.

---

# 84. Runtime Claim Boundary

Statement:

```text
"The architecture uses atomic CAS."
```

If present only in documentation:

```text
SOURCE_CLAIM
```

If implementation code is inspected:

```text
OBSERVATION
```

may describe what the inspected code contains.

Claim:

```text
"The deployed runtime always behaves atomically."
```

requires additional evidence.

Code inspection alone does not universally establish runtime behavior.

---

# 85. Implementation Boundary

A canonical architecture can say:

```text
SYSTEM MUST DO X
```

Classification:

```text
SOURCE_CLAIM
```

about the canonical requirement.

An implementation test can observe:

```text
SYSTEM DID X IN TEST T
```

Classification:

```text
OBSERVATION
```

General conclusion:

```text
SYSTEM WILL ALWAYS DO X
```

is a stronger derived/model claim requiring appropriate support.

---

# 86. Test-Pass Boundary

If documentation says:

```text
21/21 tests pass
```

without test execution evidence loaded:

```text
SOURCE_CLAIM
```

If the test suite is executed and produces:

```text
21 passed
```

then that run result is:

```text
OBSERVATION
```

But:

```text
21/21 tests passed
```

does not imply:

```text
implementation is universally correct
```

That would exceed the observation's scope.

---

# 87. Formal Proof Boundary

If a source states:

```text
"This property is formally proven."
```

that statement is initially:

```text
SOURCE_CLAIM
```

unless the proof artifact is inspected.

Inspection can establish:

```text
OBSERVATION:
a proof artifact exists with structure X
```

Whether the proof is valid may require formal validation.

Do not equate a proof claim with a verified theorem without the
necessary evidence.

---

# 88. Simulation Boundary

A simulation produces observations **within the simulation regime**.

For example:

```text
OBSERVATION:
all simulation branches remained stable
```

does not directly establish:

```text
real-world system is stable
```

without an explicit bridge.

The observation class remains valid while its regime remains bounded.

---

# 89. Structural Similarity Boundary

Suppose model A and system B share structure.

This can support:

```text
MODEL:
A is a useful analogy for B
```

It does not establish:

```text
A causes B
```

or:

```text
B literally implements A
```

Structural similarity remains model-level unless independently
validated.

---

# 90. Classification Decision Tree

```text
KNOWLEDGE OBJECT K
       |
       v
Was K obtained as a source assertion/report?
       |
      YES
       |
       v
 SOURCE_CLAIM

Otherwise:
       |
       v
Was K directly measured/inspected/recorded?
       |
      YES
       |
       v
  OBSERVATION

Otherwise:
       |
       v
Was K inferred from explicit premises?
       |
      YES
       |
       v
    DERIVED

Otherwise:
       |
       v
Is K a representational/explanatory/predictive structure?
       |
      YES
       |
       v
     MODEL

Otherwise:
       |
       v
CLASSIFICATION GAP
```

Mixed objects should be decomposed rather than forced through one
branch.

---

# 91. Minimal Classification Record

```yaml
epistemic_record:
  id: K1
  statement: "..."
  class: SOURCE_CLAIM

  provenance:
    source: "..."

  scope:
    system: "..."
    regime: "..."

  freshness:
    observed_at: "..."

  dependencies: []

  confidence_ceiling: source_supported
```

This is an illustrative schema, not a source-established mandatory
serialization format.

---

# 92. Full Classification Record

```yaml
epistemic_record:

  id: K1

  statement:
    text: "..."

  classification:
    class: DERIVED
    classifier_version: optional

  provenance:
    direct_sources: []
    source_ancestry: []
    independence_status: UNKNOWN

  premises:
    - P1
    - P2

  dependencies:
    - P1
    - P2

  applicability:
    system: null
    population: null
    environment: null
    scale: null
    time: null
    regime: null
    measurement_method: null
    assumptions: []

  freshness:
    temporal: null
    environmental: null
    regime: null
    provenance: null
    scope: null
    model: null
    source: null

  uncertainty:
    evidence: null
    model: null
    scope: null
    temporal: null
    causal: null
    provenance_independence: null

  competing:
    - null

  falsifiers:
    - null

  confidence_ceiling:
    value: null

  validation:
    status: null
```

Again, this is a model-level integration schema.

---

# 93. Classification State Machine

```text
UNCLASSIFIED
     |
     v
PROVENANCE_INSPECTION
     |
     +-------------------------------+
     |              |                |
     v              v                v
SOURCE_CLAIM   OBSERVATION        DERIVED
                                      |
                                      |
                                      v
                                    MODEL
```

This simplified state machine is not intended to imply that every model
must originate from a derived claim.

All four classes may be assigned directly based on epistemic origin.

---

# 94. Reclassification Event

When new evidence changes the appropriate representation, preserve
lineage.

```text
K@e1
SOURCE_CLAIM
    |
    | new direct measurement
    v
O@e2
OBSERVATION
```

Do not mutate history into:

```text
K@e1 was always OBSERVATION
```

Instead create explicit new evidence.

---

# 95. Classification Promotion Gate

A stronger epistemic representation requires stronger evidence.

Example:

```text
SOURCE_CLAIM
```

cannot be treated as directly observed merely because:

```text
source is trusted
```

Required:

```text
direct observation evidence
```

Likewise:

```text
MODEL
```

cannot be treated as empirically established merely because:

```text
model is elegant
```

---

# 96. Classification Preservation During Compression

Summarization must preserve epistemic class.

Invalid compression:

```text
Original:
"The report claims the system passed all tests."

Summary:
"The system passed all tests."
```

The summary removed the source-claim boundary.

Correct:

```text
"The report says the system passed all tests."
```

unless independent observation exists.

---

# 97. Classification Preservation During Retrieval

Retrieval must not strip epistemic metadata.

If a stored node says:

```yaml
claim_class: AMOS_MODEL
state: SOURCE_CLAIM
```

retrieval should not present its content as independently verified
empirical fact merely because it is in canon.

Canonical location and empirical verification are separate properties.

---

# 98. Classification Preservation During Synthesis

Suppose synthesis uses:

```text
SOURCE_CLAIM S
OBSERVATION O
MODEL M
```

Output should distinguish:

```text
Source reports S.
Observed O.
Under model M, this suggests D.
```

rather than:

```text
S, O, and M are all facts.
```

Synthesis must not flatten epistemic topology.

---

# 99. Classification Preservation During Citation

Citation proves or supports:

```text
where a statement came from
```

It does not automatically prove:

```text
the cited statement is true
```

Therefore:

```text
CITED
!= VERIFIED
```

Citation is provenance infrastructure.

Verification requires appropriate evidence.

---

# 100. Classification Preservation During Consensus

If multiple agents agree:

```text
Agent 1 -> X
Agent 2 -> X
Agent 3 -> X
```

their agreement does not determine epistemic class.

If all three repeat one source:

```text
SOURCE_CLAIM
```

remains the relevant origin.

If all three use the same model:

```text
MODEL CORRELATION
```

may remain.

Consensus does not create independent evidence.

---

# 101. Classification Preservation During Recovery

Recovery must preserve the original epistemic identity of restored
objects.

Rollback should not convert:

```text
MODEL
```

into:

```text
OBSERVATION
```

or:

```text
SOURCE_CLAIM
```

into:

```text
DERIVED
```

unless an explicit new epistemic event justifies the change.

---

# 102. Classification Preservation Across Epochs

Historical record:

```text
e1:
C1 = SOURCE_CLAIM

e2:
O1 = OBSERVATION supporting C1

e3:
D1 = DERIVED from C1 + O1
```

Preferred lineage:

```text
C1@e1 ----\
           \
O1@e2 ------> D1@e3
```

not:

```text
rewrite C1@e1 as DERIVED
```

Each epistemic event remains typed.

---

# 103. Classification Preservation Across Shards

If shard A stores:

```text
C = SOURCE_CLAIM
```

and shard B stores the same proposition as:

```text
C = OBSERVATION
```

the merge process must inspect why.

Possible explanation:

```text
Shard A knows only a report.
Shard B directly measured it.
```

Both records may be valid with different provenance.

A merge must not discard this distinction.

---

# 104. Classification and Atomic Multi-RSCF

An atomic transaction may contain:

```yaml
transaction:
  capsules:

    - id: R1
      epistemic_class: SOURCE_CLAIM

    - id: R2
      epistemic_class: OBSERVATION

    - id: R3
      epistemic_class: DERIVED

    - id: R4
      epistemic_class: MODEL
```

Atomic commit preserves transaction consistency.

It does not normalize all capsules to one epistemic class.

---

# 105. Classification and Confidence Ceiling

Conceptually:

```text
SOURCE_CLAIM
     |
     v
DERIVED D1
     |
     v
MODEL M1
```

If the source claim is the only load-bearing support, confidence in
downstream D1 and M1 cannot silently exceed it.

Additional independent observations may alter the ceiling.

---

# 106. Classification and Adversarial Validation

For consequential conclusions, challenge classification itself.

Ask:

```text
Is this really an observation,
or only a source report?

Is this really derived,
or is an assumption hidden?

Is this really a model,
or is it being presented as implementation?

Are these sources actually independent?

Has scope been widened?

Has regime changed?

Is the evidence stale?

Has correlation been mistaken for causation?
```

A classification that fails this challenge should be downgraded,
conditioned, or marked as a gap.

---

# 107. Sensitivity Test

Identify the smallest classification change that could flip the
decision.

Example:

```text
Decision relies on K being OBSERVATION.
```

But provenance review shows K is only:

```text
SOURCE_CLAIM.
```

If that changes the decision:

```text
classification is decision-critical
```

and should be resolved before lower-value background work.

---

# 108. Classification Error Severity

```yaml
severity:

  critical:
    example: >
      Treating an unsupported source claim as verified observation in a
      safety-critical decision.

  decision_relevant:
    example: >
      Treating correlated source reports as independent confirmation.

  explanatory:
    example: >
      Failing to distinguish two model variants when decision outcome
      is unchanged.

  cosmetic:
    example: >
      Non-semantic label formatting differences.
```

Integrity effort should scale with consequence.

---

# 109. Anti-Fabrication Rule

If evidence does not establish the epistemic origin:

```text
DO NOT GUESS.
```

Return:

```text
UNKNOWN / GAP
```

under the appropriate gap law.

Fluent prose cannot substitute for provenance.

---

# 110. Anti-Pattern Register

## ER-AP1 — Source-to-Fact Collapse

```text
SOURCE_CLAIM -> FACT
```

without independent support.

## ER-AP2 — Observation-to-General-Law Collapse

```text
ONE OBSERVATION -> UNIVERSAL CLAIM
```

without generalization evidence.

## ER-AP3 — Derivation Without Premises

```text
DERIVED
```

with no recoverable support.

## ER-AP4 — Model Reification

```text
MODEL -> REALITY
```

without validation.

## ER-AP5 — Provenance Multiplication

One source copied many times counted as independent evidence.

## ER-AP6 — Scope Leakage

Evidence from one population/environment generalized silently.

## ER-AP7 — Regime Leakage

Simulation or canon treated as empirical runtime observation.

## ER-AP8 — Causal Overreach

Correlation, sequence, or analogy promoted to causal effect.

## ER-AP9 — Confidence Inflation

Downstream confidence exceeds weak load-bearing premise.

## ER-AP10 — Silent Reclassification

Historical epistemic class rewritten without lineage.

---

# 111. Classification Decision Matrix

| Evidence Situation                        | Classification                                                     |
| ----------------------------------------- | ------------------------------------------------------------------ |
| A document asserts X                      | `SOURCE_CLAIM`                                                     |
| A person reports X                        | `SOURCE_CLAIM`                                                     |
| A README reports test success             | `SOURCE_CLAIM`                                                     |
| A test is directly executed and returns X | `OBSERVATION`                                                      |
| A sensor directly records X               | `OBSERVATION`                                                      |
| File inspection finds X                   | `OBSERVATION`                                                      |
| X follows from P1 and P2                  | `DERIVED`                                                          |
| X is an inferred explanation              | `DERIVED`                                                          |
| X is an architectural abstraction         | `MODEL`                                                            |
| X is a predictive framework               | `MODEL`                                                            |
| Epistemic origin unavailable              | `GAP`, not forced class                                            |
| Source reports an observation             | outer `SOURCE_CLAIM`; embedded observation remains source-reported |
| Source proposes a model                   | outer `SOURCE_CLAIM`; embedded object `MODEL`                      |

---

# 112. Epistemic Integrity Checks

```yaml
checks:

  classification_present:
    required: true

  provenance_recoverable:
    required: true_for_material_claims

  scope_visible:
    required: when_material

  regime_visible:
    required: when_material

  freshness_checked:
    required: when_decision_relevant

  dependency_trace:
    required: for_material_derived_claims

  model_assumptions:
    required: when_material

  provenance_independence:
    required: when_independent_confirmation_is_claimed

  causal_type:
    required: for_causal_conclusions

  gap_visibility:
    required: true
```

This checklist is a derived operationalization of the classification
law and surrounding AMOS integrity rules.

---

# 113. Classification Validator

Illustrative pseudocode:

```python
def classify_epistemic_object(obj):
    if obj.provenance.is_source_report:
        return "SOURCE_CLAIM"

    if obj.provenance.is_direct_observation:
        return "OBSERVATION"

    if obj.has_explicit_derivation:
        return "DERIVED"

    if obj.is_model_representation:
        return "MODEL"

    return "GAP"
```

This is not a canonical executable implementation.

Real classification can require decomposition of mixed claims.

---

# 114. Composite Validator

```python
def classify_composite(statement):
    atoms = decompose_into_material_claims(statement)

    results = []

    for atom in atoms:
        results.append({
            "claim": atom,
            "class": classify_epistemic_object(atom)
        })

    return results
```

Purpose:

```text
prevent one sentence
from forcing one epistemic class
onto heterogeneous claims
```

Again, illustrative only.

---

# 115. Provenance-Aware Validator

```python
def validate_source_independence(claims):
    ancestry = trace_source_ancestry(claims)

    if shared_load_bearing_origin(ancestry):
        return "CORRELATED"

    if independence_demonstrated(ancestry):
        return "INDEPENDENT"

    return "UNKNOWN"
```

This preserves the rule:

```text
independence must be demonstrated,
not assumed
```

---

# 116. Confidence Propagation

Illustrative:

```python
def confidence_ceiling(derived_claim):
    premises = load_bearing_premises(derived_claim)

    return min(
        premise.confidence
        for premise in premises
    )
```

unless an independent support path revalidates the conclusion.

The exact numerical confidence system is not established by this node.

---

# 117. Proof Capsule

```yaml
proof_capsule:

  claim:
    text: >
      EPISTEMIC_REGIMES governs four discrete knowledge classes:
      SOURCE_CLAIM, OBSERVATION, DERIVED, and MODEL.
    class: SOURCE_CLAIM

  source_basis:
    - >
      The supplied core-law text explicitly identifies those four
      classes.

  load_bearing_premises:

    - id: P1
      statement: >
        EPISTEMIC_REGIMES is identified as a core_law.
      provenance: supplied_node

    - id: P2
      statement: >
        The law explicitly governs four discrete knowledge classes.
      provenance: supplied_node

    - id: P3
      statement: >
        The named classes are SOURCE_CLAIM, OBSERVATION, DERIVED,
        and MODEL.
      provenance: supplied_node

  normalized_conclusion:
    statement: >
      Material knowledge objects should preserve which of the four
      epistemic origins/types supports them rather than silently
      collapsing those types.
    class: DERIVED

  scope:
    - core_laws
    - epistemic_classification

  dependencies:
    - L17_RSCF
    - L21_EPISTEMIC_REGIME
    - L1_EPISTEMIC
    - L5_SCOPE_REGIME
    - SCOPE_REGIME_FIREWALL
    - L27_GAP
    - L28_CRITICAL_GAP

  competing:
    - >
      Exact semantics of each class may be further constrained by
      authoritative dedicated canon not supplied in this terse node.

  falsifiers:
    - >
      Authoritative canon defines a different epistemic class set.
    - >
      Authoritative canon establishes materially different semantics
      for one or more of the four labels.
    - >
      This node is superseded by a later canonical classification law.

  confidence_ceiling:
    four_class_set: SOURCE_SUPPORTED
    expanded_semantics: MODEL_DERIVED_UNLESS_CORROBORATED
```

---

# 118. Source-Established Claims

The supplied node directly establishes:

```yaml
source_established:

  title:
    value: EPISTEMIC_REGIMES Classification Law

  type:
    value: core_law

  source:
    value: 01_CANON/01_CORE_LAWS

  tags:
    - core_law
    - epistemic_regimes
    - classification

  governing_statement:
    value: >
      Governs the four discrete knowledge classes:
      SOURCE_CLAIM, OBSERVATION, DERIVED, and MODEL.

  path:
    value: 01_CANON/01_CORE_LAWS/EPISTEMIC_REGIMES.md

  node:
    node_id: epistemic_regimes
    node_type: core_law

  relations:
    indexed_by:
      - 00_HOME
      - AMOS_RSCF_NODES
    child_of:
      - LAW_HIERARCHY

  related:
    - 00_HOME
    - AMOS_RSCF_NODES
    - LAW_HIERARCHY
    - L17_RSCF
    - L21_EPISTEMIC_REGIME
    - L22_ATOMIC_REASONING
    - L1_EPISTEMIC
    - L5_SCOPE_REGIME
    - SCOPE_REGIME_FIREWALL
    - L27_GAP
    - L28_CRITICAL_GAP

  moc:
    - 01_CORE_LAWS_MOC

  trang_framework:
    - TRANG_FRAMEWORK_RECURSIVE_ONTOLOGY_DYNAMICS
```

---

# 119. Not Established by This Node

The supplied terse node does **not** independently establish:

```yaml
not_established:

  - a numerical confidence scale

  - a probability mapping for the four classes

  - an ordering from weakest to strongest class

  - that OBSERVATION is always more trustworthy than SOURCE_CLAIM

  - that DERIVED is always stronger than OBSERVATION

  - that MODEL means false or speculative

  - a fifth canonical UNKNOWN class

  - automatic epistemic promotion rules

  - exact RSCF serialization schema

  - exact classifier implementation

  - exact provenance graph schema

  - exact freshness thresholds

  - exact source-independence algorithm

  - exact causal-validation protocol

  - literal runtime implementation

  - formal proof that the four classes are universally exhaustive
    outside their declared AMOS scope
```

These must not be invented as source canon.

---

# 120. Gap Register

```yaml
gaps:

  - id: ER-G001
    class: DECISION_RELEVANT
    issue: >
      Exact authoritative definitions of SOURCE_CLAIM, OBSERVATION,
      DERIVED, and MODEL are not included in the supplied terse node.
    status: OPEN

  - id: ER-G002
    class: DECISION_RELEVANT
    issue: >
      Exact classification algorithm for mixed or nested claims is not
      specified.
    status: OPEN

  - id: ER-G003
    class: DECISION_RELEVANT
    issue: >
      Exact relationship between epistemic class and RSCF state is not
      fully specified by this node.
    status: OPEN

  - id: ER-G004
    class: DECISION_RELEVANT
    issue: >
      Exact promotion/reclassification protocol is not supplied.
    status: OPEN

  - id: ER-G005
    class: EXPLANATORY
    issue: >
      Exact persistence schema for provenance ancestry is not supplied.
    status: OPEN

  - id: ER-G006
    class: EXPLANATORY
    issue: >
      Exact validation criteria for observation quality are not
      supplied.
    status: OPEN

  - id: ER-G007
    class: EXPLANATORY
    issue: >
      Exact validation criteria for model support are not supplied.
    status: OPEN

  - id: ER-G008
    class: DECISION_RELEVANT
    issue: >
      Relationship between the four-class system and additional
      conclusion classes such as VERIFIED, CONDITIONAL, COMPETING,
      and UNKNOWN/GAP requires the governing classification canon.
    status: OPEN
```

---

# 121. Falsifiers

```yaml
falsifiers:

  - id: ER-F001
    condition: >
      Authoritative epistemic canon defines a different discrete
      knowledge-class set.

  - id: ER-F002
    condition: >
      Authoritative canon explicitly merges two or more of
      SOURCE_CLAIM, OBSERVATION, DERIVED, and MODEL.

  - id: ER-F003
    condition: >
      Authoritative canon establishes these labels as confidence levels
      rather than epistemic classes.

  - id: ER-F004
    condition: >
      A later canonical node explicitly supersedes
      EPISTEMIC_REGIMES.md.

  - id: ER-F005
    condition: >
      Authoritative RSCF canon establishes incompatible semantics for
      these classification labels.
```

---

# 122. Dependency Graph

```text
                         [[L1_EPISTEMIC]]
                                |
                                v
                    [[EPISTEMIC_REGIMES]]
                       /      |       \
                      /       |        \
                     v        v         v
              [[L17_RSCF]]  [[L21_EPISTEMIC_REGIME]]
                     |               |
                     |               v
                     |       [[L5_SCOPE_REGIME]]
                     |               |
                     |               v
                     |    [[SCOPE_REGIME_FIREWALL]]
                     |
                     +----------------------+
                                            |
                                            v
                                      [[L27_GAP]]
                                            |
                                            v
                                  [[L28_CRITICAL_GAP]]
```

This graph represents architectural relationships suggested by the
supplied related-node list.

It does not assert undocumented dependency direction as source fact.

---

# 123. Epistemic Classification Architecture

```text
RAW INPUT
   |
   v
PROVENANCE IDENTIFICATION
   |
   v
CLAIM DECOMPOSITION
   |
   v
+---------------------------------------------+
|                                             |
| SOURCE REPORT? ---------> SOURCE_CLAIM      |
|                                             |
| DIRECT MEASUREMENT? ----> OBSERVATION       |
|                                             |
| INFERENCE? -------------> DERIVED           |
|                                             |
| REPRESENTATION? --------> MODEL             |
|                                             |
+---------------------------------------------+
   |
   v
SCOPE / REGIME
   |
   v
FRESHNESS
   |
   v
DEPENDENCY + PROVENANCE TOPOLOGY
   |
   v
CONFIDENCE CEILING
   |
   v
GAP / CONTRADICTION CHECK
   |
   v
RSCF
```

---

# 124. Classification Operational Contract

```yaml
operational_contract:

  input:
    - knowledge_object

  required_operations:
    - identify_provenance
    - decompose_material_claims_when_needed
    - assign_epistemic_class
    - preserve_source_ancestry
    - preserve_dependencies
    - preserve_scope
    - preserve_regime
    - evaluate_freshness_when_material
    - expose_classification_gaps

  prohibited_operations:
    - source_claim_to_fact_without_evidence
    - model_to_reality_without_validation
    - observation_to_universal_claim_without_generalization
    - derived_claim_without_premise_trace
    - provenance_count_inflation
    - silent_scope_expansion
    - silent_regime_crossing
    - silent_reclassification

  output:
    - typed_epistemic_object
```

---

# 125. Epistemic Classification Receipt

Illustrative receipt:

```yaml
epistemic_classification_receipt:

  receipt_id: ER-RECEIPT-001

  object_id: K1

  statement:
    text: "The source reports that all tests pass."

  classification:
    class: SOURCE_CLAIM

  reason:
    immediate_basis: source_report

  provenance:
    source_id: S1
    ancestry_status: UNKNOWN

  scope:
    corpus: AMOS

  regime:
    value: canonical_source

  validation:
    source_present: PASS
    direct_execution_observed: false
    independent_confirmation: NOT_ESTABLISHED

  confidence_ceiling:
    value: source_supported

  gaps:
    - independent_runtime_validation
```

This receipt schema is illustrative, not source-defined.

---

# 126. Classification Invariants

```text
ER-I1
EVERY MATERIAL CLAIM MUST PRESERVE ITS EPISTEMIC ORIGIN.

ER-I2
SOURCE_CLAIM MUST NOT SILENTLY BECOME OBSERVATION.

ER-I3
OBSERVATION MUST NOT SILENTLY BECOME UNIVERSAL TRUTH.

ER-I4
DERIVED CLAIMS MUST PRESERVE LOAD-BEARING PREMISES.

ER-I5
MODEL MUST NOT SILENTLY BECOME VERIFIED REALITY.

ER-I6
EPISTEMIC CLASS MUST NOT BE CONFUSED WITH CONFIDENCE.

ER-I7
EPISTEMIC CLASS MUST NOT BE CONFUSED WITH TRUTH VALUE.

ER-I8
PROVENANCE MULTIPLICITY MUST NOT BE CONFUSED WITH INDEPENDENCE.

ER-I9
SCOPE MUST NOT SILENTLY EXPAND.

ER-I10
REGIME MUST NOT SILENTLY CHANGE.

ER-I11
FRESHNESS MUST BE CHECKED WHEN IT CAN CHANGE THE DECISION.

ER-I12
STRUCTURAL SIMILARITY MUST NOT BE USED AS CAUSAL PROOF.

ER-I13
CONTRADICTIONS MUST REMAIN VISIBLE UNTIL DISCRIMINATING EVIDENCE EXISTS.

ER-I14
MISSING CLASSIFICATION EVIDENCE MUST REMAIN A GAP.

ER-I15
CLASSIFICATION HISTORY MUST PRESERVE PROVENANCE AND LINEAGE.
```

---

# 127. Compact Canon Contract

```text
EPISTEMIC_REGIMES
GOVERNS FOUR DISCRETE KNOWLEDGE CLASSES:

SOURCE_CLAIM
OBSERVATION
DERIVED
MODEL

SOURCE_CLAIM:
A SOURCE ASSERTS OR REPORTS THE PROPOSITION.

OBSERVATION:
THE PROPOSITION IS GROUNDED IN DIRECT MEASUREMENT,
INSPECTION, OR RECORDED OBSERVATION.

DERIVED:
THE PROPOSITION IS INFERRED FROM PREMISES.

MODEL:
THE PROPOSITION IS PART OF A REPRESENTATIONAL,
EXPLANATORY, PREDICTIVE, OR ARCHITECTURAL MODEL.

THE FOUR CLASSES ARE TYPES,
NOT AUTOMATIC CONFIDENCE RANKS.

SOURCE_CLAIM
DOES NOT MEAN VERIFIED.

OBSERVATION
DOES NOT MEAN INFALLIBLE.

DERIVED
DOES NOT MEAN CERTAIN.

MODEL
DOES NOT MEAN REALITY.

REPETITION
DOES NOT CREATE INDEPENDENCE.

STRUCTURAL SIMILARITY
DOES NOT CREATE CAUSATION.

CLASSIFICATION
DOES NOT REMOVE SCOPE,
REGIME,
FRESHNESS,
PROVENANCE,
DEPENDENCIES,
OR FALSIFIERS.

WHEN CLASSIFICATION CANNOT BE ESTABLISHED:
PRESERVE THE GAP.
```

---

# 128. RSCF Contract

```yaml
RSCF-CONTRACT:

  node_id: epistemic_regimes

  node_type: core_law

  H:
    name: EPISTEMIC_REGIMES Classification Law

    governing_statement: >
      Governs the four discrete knowledge classes:
      SOURCE_CLAIM, OBSERVATION, DERIVED, and MODEL.

  M:
    classes:
      - SOURCE_CLAIM
      - OBSERVATION
      - DERIVED
      - MODEL

    related_laws:
      - L17_RSCF
      - L21_EPISTEMIC_REGIME
      - L22_ATOMIC_REASONING
      - L1_EPISTEMIC
      - L5_SCOPE_REGIME
      - SCOPE_REGIME_FIREWALL
      - L27_GAP
      - L28_CRITICAL_GAP

  L:
    mechanics:
      - preserve_epistemic_origin
      - preserve_provenance
      - preserve_dependencies
      - preserve_scope
      - preserve_regime
      - prevent_silent_promotion
      - prevent_model_reification
      - prevent_provenance_inflation
      - expose_gaps

  state: SOURCE_CLAIM

  claim_class: AMOS_MODEL

  provenance: AMOS_corpus

  scope:
    - core_laws
    - epistemic_classification

  confidence_ceiling:
    four_class_statement: SOURCE_SUPPORTED
    expanded_semantics: MODEL_DERIVED
```

---

# 129. RSCF-NODE

```yaml
RSCF-NODE:

  node_id: epistemic_regimes

  node_type: core_law

  title: EPISTEMIC_REGIMES Classification Law

  path:
    01_CANON/01_CORE_LAWS/EPISTEMIC_REGIMES.md

  state: SOURCE_CLAIM

  claim_class: AMOS_MODEL

  provenance:
    origin: AMOS_corpus

  scope:
    - core_laws

  governs:
    epistemic_classes:
      - SOURCE_CLAIM
      - OBSERVATION
      - DERIVED
      - MODEL

  related:
    - L17_RSCF
    - L21_EPISTEMIC_REGIME
    - L22_ATOMIC_REASONING
    - L1_EPISTEMIC
    - L5_SCOPE_REGIME
    - SCOPE_REGIME_FIREWALL
    - L27_GAP
    - L28_CRITICAL_GAP
```

---

# 130. RSCF-RELATIONS

```yaml
RSCF-RELATIONS:

  - INDEXED_BY: [[00_HOME]]

  - INDEXED_BY: [[AMOS_RSCF_NODES]]

  - CHILD_OF: [[LAW_HIERARCHY]]

  - RELATED_TO: [[L17_RSCF]]

  - RELATED_TO: [[L21_EPISTEMIC_REGIME]]

  - RELATED_TO: [[L22_ATOMIC_REASONING]]

  - RELATED_TO: [[L1_EPISTEMIC]]

  - RELATED_TO: [[L5_SCOPE_REGIME]]

  - RELATED_TO: [[SCOPE_REGIME_FIREWALL]]

  - RELATED_TO: [[L27_GAP]]

  - RELATED_TO: [[L28_CRITICAL_GAP]]

  - INDEXED_BY: [[01_CORE_LAWS_MOC]]

  - FRAMEWORK_CONTEXT:
      [[TRANG_FRAMEWORK_RECURSIVE_ONTOLOGY_DYNAMICS]]
```

---

# 131. Supersession / Compatibility Rule

This node defines the four-class classification surface supplied here.

If another epistemic law defines:

* regime semantics;
* RSCF state semantics;
* conclusion status;
* gap semantics;
* verification semantics;

those should be treated as complementary dimensions unless
authoritative canon explicitly establishes supersession.

In particular:

```text
EPISTEMIC_REGIMES
```

should not be silently merged with:

```text
L21_EPISTEMIC_REGIME
```

because:

```text
knowledge class
```

and:

```text
applicability regime
```

are distinct concepts.

Likewise, older atomic-reasoning semantics should not redefine this
four-class set without explicit canonical authority.

---

# 132. Canon Boundary

> [!important] Canon Boundary
> The supplied source directly establishes one central proposition:
>
> **EPISTEMIC_REGIMES governs four discrete knowledge classes:
> SOURCE_CLAIM, OBSERVATION, DERIVED, and MODEL.**
>
> It also supplies the node identity, path, related nodes, MOC, and
> initial RSCF relations.
>
> The detailed definitions, equations, schemas, validators, state
> machines, confidence propagation rules, provenance topology, and
> operational examples in this expanded node are normalized
> architectural elaborations unless independently established by
> authoritative AMOS canon.
>
> They must therefore not be mistaken for missing source text that was
> actually present in the terse supplied node.

---

# 133. Final Integrity Rule

```text
EPISTEMIC_REGIMES
CLASSIFIES KNOWLEDGE INTO FOUR DISCRETE CLASSES:

SOURCE_CLAIM
OBSERVATION
DERIVED
MODEL.

THE CLASS MUST FOLLOW
THE ACTUAL EPISTEMIC ORIGIN.

A SOURCE CLAIM
IS A CLAIM ATTRIBUTED TO A SOURCE.

AN OBSERVATION
IS A DIRECTLY OBSERVED OR MEASURED RECORD
WITH ITS APPLICABILITY ENVELOPE PRESERVED.

A DERIVED CLAIM
IS A CONCLUSION DEPENDENT ON PREMISES
AND AN INFERENCE PATH.

A MODEL
IS A REPRESENTATIONAL,
EXPLANATORY,
PREDICTIVE,
ARCHITECTURAL,
OR HYPOTHETICAL STRUCTURE.

SOURCE AUTHORITY
DOES NOT ERASE SOURCE PROVENANCE.

OBSERVATION
DOES NOT GUARANTEE INFALLIBILITY.

VALID DERIVATION
DOES NOT REPAIR AN INVALID PREMISE.

MODEL ELEGANCE
DOES NOT PROVE EMPIRICAL REALITY.

REPETITION
DOES NOT CREATE INDEPENDENT CONFIRMATION.

STRUCTURAL SIMILARITY
DOES NOT ESTABLISH CAUSATION.

SIMULATION
DOES NOT SILENTLY BECOME EMPIRICAL REALITY.

CANONICAL REQUIREMENT
DOES NOT SILENTLY BECOME RUNTIME OBSERVATION.

EPISTEMIC CLASS
DOES NOT SILENTLY WIDEN SCOPE.

EPISTEMIC CLASS
DOES NOT OVERRIDE REGIME.

EPISTEMIC CLASS
DOES NOT OVERRIDE FRESHNESS.

EPISTEMIC CLASS
DOES NOT BY ITSELF DEFINE CONFIDENCE.

DOWNSTREAM CONFIDENCE
MUST NOT EXCEED ITS WEAKEST
LOAD-BEARING PREMISE
WITHOUT INDEPENDENT REVALIDATION.

CONTRADICTIONS REMAIN VISIBLE.

COMPETING MODELS REMAIN COMPETING
UNTIL DISCRIMINATING EVIDENCE EXISTS.

WHEN THE EPISTEMIC ORIGIN
CANNOT BE ESTABLISHED:

DO NOT FABRICATE A CLASSIFICATION.

PRESERVE THE GAP.

INTEGRITY
>
COMPLETENESS
>
FLUENCY.
```

---

## Related

[[00_HOME]] ·
[[AMOS_RSCF_NODES]] ·
[[LAW_HIERARCHY]] ·
[[L17_RSCF]] ·
[[L21_EPISTEMIC_REGIME]] ·
[[L22_ATOMIC_REASONING]] ·
[[L1_EPISTEMIC]] ·
[[L5_SCOPE_REGIME]] ·
[[SCOPE_REGIME_FIREWALL]] ·
[[L27_GAP]] ·
[[L28_CRITICAL_GAP]]

---

**MOC:** [[01_CORE_LAWS_MOC]]

---

**Trang Framework:** [[TRANG_FRAMEWORK_RECURSIVE_ONTOLOGY_DYNAMICS]]

---

00_ROOT_MOC|AMOS MOC

```
```
