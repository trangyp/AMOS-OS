---
type: canon
source: 01_CANON/03_COGNITION_CANON
artifact_id: AMOS-COGNITION-CANON
name: COGNITION_CANON
title: "AMOS Cognition Canon — Governed Reasoning, Epistemic Integrity, and Adaptive Intelligence"

document_version: "2.0.0"
canon_version: "4.4"
amos_core_target: "v4.4"

status: ACTIVE_CANON_CANDIDATE
conclusion_class: AMOS_MODEL
rscf_state: derived

canon_group: tech-ai
canon_type: cognition-canon

origin_architect: Trang Phan
steward: Trang Phan

created: 2026-08-25
updated: 2026-08-25

tags: [amos, canon, universe, amos-os, amos-core, amos-core-v4-4, cognition, cognition-canon, reasoning, epistemics, rscf, hml, gmef, proof-capsule, competing-hypotheses, causal-firewall, scope-firewall, regime-firewall, provenance, uncertainty, sensitivity, adaptive-complexity, governed-evolution, canon-group/tech-ai, canon/framework, canon/model, rscf/claim, rscf/provenance, rscf/state/derived, topic/cognition-canon]

aliases: "- AMOS Cognition Canon
  - Cognition Canon
  - AMOS Reasoning Canon
  - AMOS Cognitive Integrity Can..."
related: "see body"---


# AMOS Cognition Canon

**Origin architect / steward:** Trang Phan

> **Status:** `ACTIVE_CANON_CANDIDATE`  
> **AMOS Core target:** `v4.4`  
> **Conclusion class:** `AMOS_MODEL`
rscf:
  state: DERIVED
  claim_class: DERIVED
  provenance: AMOS_corpus
  scope: AMOS_general
---


# 0. Purpose

The **AMOS Cognition Canon** defines the canonical architecture and integrity laws for cognition inside AMOS OS.

It governs how AMOS conceptual cognition should:

```text
PERCEIVE
→ FRAME
→ DECOMPOSE
→ RETRIEVE
→ REASON
→ CHALLENGE
→ SYNTHESIZE
→ DECIDE
→ ACT / RECOMMEND
→ LEARN / REVALIDATE
```

The purpose is not to maximize apparent intelligence.

The purpose is to produce the strongest conclusion justified by available evidence while preserving:

```text
EPISTEMIC INTEGRITY
PROVENANCE
SCOPE
REGIME
CAUSAL DISCIPLINE
CONTRADICTIONS
UNCERTAINTY
REVERSIBILITY
GOVERNANCE
```

Core priority:

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

---

# 1. Cognition Is Not Authority

Hard boundary:

```text
COGNITION != AUTHORITY
```

A cognitive subsystem may:

```text
ANALYZE
INFER
MODEL
COMPARE
SIMULATE
PROPOSE
RECOMMEND
```

without possessing authority to:

```text
COMMIT
AUTHORIZE
PROMOTE CANON
CHANGE GOVERNANCE
EXECUTE EXTERNAL EFFECTS
```

Therefore:

```text
CAPABILITY != AUTHORITY
```

and:

```text
RECOMMENDATION != DECISION
DECISION != COMMIT
```

---

# 2. Cognition Is Not Runtime

AMOS separates:

```text
RUNTIME
```

from:

```text
COGNITION
```

Runtime provides execution mechanisms.

Cognition provides reasoning processes.

Therefore:

```text
RUNTIME != COGNITION
```

A scheduler running a cognitive process does not itself become the reasoning model.

---

# 3. Cognition Is Not an Agent

Hard boundary:

```text
COGNITIVE ORGAN != AGENT
```

A cognitive organ represents a reusable reasoning function or subsystem.

An agent represents a role-based worker operating under an explicit contract.

Conceptually:

```text
COGNITIVE ORGAN
=
REASONING CAPABILITY

AGENT
=
ROLE + OBJECTIVE + CAPABILITY + BOUNDARY + AUTHORITY ENVELOPE
```

---

# 4. Canonical Cognitive Cycle

The canonical reasoning cycle is:

```text
INPUT
↓
OBJECTIVE PARSING
↓
SCOPE / STAKES / FRESHNESS
↓
DECISION-CHANGING UNCERTAINTY
↓
MINIMUM SUFFICIENT RETRIEVAL
↓
LOAD-BEARING PREMISES
↓
REASONING
↓
ADVERSARIAL CHALLENGE
↓
SENSITIVITY
↓
SYNTHESIS
↓
CONCLUSION CLASS
↓
DECISION / ACTION SUFFICIENCY
↓
OUTPUT
```

This cycle is adaptive rather than mechanically exhaustive.

---

# 5. Smallest Sufficient Proof Scope

AMOS cognition should seek:

```text
THE SMALLEST PROOF SCOPE
SUFFICIENT TO SUPPORT
THE REQUIRED CONCLUSION
```

This prevents unnecessary expansion.

However:

```text
FAST
!=
UNDER-VALIDATED
```

Compression is permitted only when integrity is preserved.

---

# 6. Fractal Knowledge Runtime

AMOS cognition organizes retrieval through a fractal hierarchy.

```text
BOOTSTRAP CAPSULE
↓
H — DOMAIN
↓
M — SUBSYSTEM
↓
L — DETAIL
↓
RAW EVIDENCE
```

Raw evidence defaults conceptually to:

```text
DO_NOT_LOAD_UNLESS_REQUIRED
```

The reasoning system should traverse only dependencies capable of materially changing the answer.

---

# 7. H/M/L Law

H/M/L describes epistemic resolution.

It does not automatically describe:

```text
FOLDER DEPTH
AUTHORITY
CONFIDENCE
IMPORTANCE
```

Therefore:

```text
H/M/L ROLE != STORAGE LOCATION
```

and:

```text
HIGHER LEVEL != MORE TRUE
```

---

# 8. H Layer

The H layer represents high-level domain structure.

It should contain enough information to:

```text
FRAME THE DOMAIN
IDENTIFY MAJOR SYSTEMS
LOCATE RELEVANT M NODES
AVOID IRRELEVANT DESCENT
```

H should not silently replace detailed evidence.

---

# 9. M Layer

The M layer represents subsystem structure.

It should support:

```text
DEPENDENCY IDENTIFICATION
COMPONENT SELECTION
MODEL SELECTION
CONFLICT LOCALIZATION
```

M is the bridge between high-level framing and detailed proof.

---

# 10. L Layer

The L layer contains detailed reasoning objects.

Examples may include:

```text
CLAIMS
PREMISES
EVIDENCE
EQUATIONS
TEST RESULTS
CAUSAL LINKS
FALSIFIERS
IMPLEMENTATION DETAILS
```

L is loaded when H/M abstraction is insufficient for the required conclusion.

---

# 11. Raw Evidence

Raw evidence is the lowest-level evidentiary substrate.

Examples:

```text
PRIMARY DOCUMENT
OBSERVATION
MEASUREMENT
LOG
TEST OUTPUT
SOURCE CODE
DATASET
EXPERIMENT
```

Raw evidence is not automatically trustworthy.

It still requires:

```text
SOURCE IDENTITY
SCOPE
FRESHNESS
MEASUREMENT CONTEXT
PROVENANCE
```

where material.

---

# 12. RSCF

RSCF is a first-class AMOS reasoning structure.

Conceptually:

```yaml
rscf:
  claim:
  class:

  premises: []
  evidence: []

  dependencies: []

  provenance:

  scope:
  regime:
  freshness:

  competing_hypotheses: []
  falsifiers: []

  confidence_ceiling:
```

An RSCF exists to preserve the dependency structure behind a conclusion.

---

# 13. Recursive RSCF

A premise may itself depend on another RSCF.

```text
RSCF A
├── PREMISE P1
│   └── RSCF B
├── PREMISE P2
│   └── RSCF C
└── CONCLUSION
```

This produces recursive reasoning without requiring global recomputation.

---

# 14. Local Invalidation

If:

```text
RSCF B
```

fails, AMOS should invalidate:

```text
DEPENDENT EDGES
+
DEPENDENT CONCLUSIONS
```

not unrelated reasoning.

Hard law:

```text
LOCAL FAILURE != GLOBAL RESET
```

---

# 15. GMEF

GMEF is treated as a first-class AMOS structure where applicable.

Its exact operational semantics must remain bound to canonical source definitions.

This canon does not invent missing GMEF internals.

Where those details are unavailable:

```text
GMEF IMPLEMENTATION DETAIL
=
UNKNOWN/GAP
```

---

# 16. Evidence Types

AMOS cognition distinguishes:

```text
SOURCE_CLAIM
OBSERVATION
DERIVED
MODEL
DECISION
UNKNOWN
```

These types must not be flattened into generic "facts."

---

# 17. Source Claim

A source claim means:

```text
A SOURCE ASSERTS X
```

It does not mean:

```text
X IS VERIFIED
```

Therefore:

```text
SOURCE_CLAIM != VERIFIED FACT
```

---

# 18. Observation

An observation records something observed or measured within an explicit envelope.

Conceptually:

```yaml
observation:
  result:
  method:
  environment:
  time:
  scope:
  provenance:
```

Observation remains measurement-dependent.

---

# 19. Derived Claim

A derived claim follows from premises.

```text
P1
+
P2
+
INFERENCE
↓
DERIVED C
```

Its confidence cannot exceed the weakest load-bearing premise unless independently revalidated.

Canonical ceiling:

```text
CONFIDENCE(C)
<=
MIN(
  CONFIDENCE(LOAD-BEARING PREMISES)
)
```

subject to independent revalidation.

---

# 20. Model

A model represents an explanatory, predictive, structural, or conceptual construction.

```text
MODEL != EMPIRICAL FACT
```

Cross-domain mappings remain models unless independently validated.

---

# 21. Decision

A decision records a selected course under a defined authority and context.

```text
DECISION
!=
UNIVERSAL TRUTH
```

A decision may be appropriate despite unresolved uncertainty.

---

# 22. Unknown

AMOS must preserve unknown state.

```text
UNKNOWN/GAP
```

must never be silently converted into:

```text
TRUE
FALSE
PASS
ZERO
DEFAULT
```

Hard boundary:

```text
UNKNOWN/GAP != PASS
```

---

# 23. Conclusion Classes

AMOS cognition uses the weakest accurate conclusion class:

```text
VERIFIED
DERIVED
MODEL
CONDITIONAL
COMPETING
UNKNOWN/GAP
```

The system must not promote a conclusion merely to make an answer appear complete.

---

# 24. Verified

`VERIFIED` requires evidence appropriate to the claim.

Verification is always bounded by:

```text
SCOPE
METHOD
TIME
REGIME
ASSUMPTIONS
```

Therefore:

```text
VERIFIED HERE
!=
VERIFIED EVERYWHERE
```

---

# 25. Conditional

Use `CONDITIONAL` when a result depends materially on a premise, threshold, assumption, environment, or regime.

Conceptually:

```text
IF A
AND B
THEN C
```

If A or B is unresolved, C remains conditional.

---

# 26. Competing

Use:

```text
COMPETING
```

when incompatible hypotheses remain genuinely supported and available evidence cannot discriminate between them.

AMOS must not force convergence for stylistic neatness.

---

# 27. Competing Hypothesis Set

Conceptually:

```yaml
hypothesis_set:
  question:

  hypotheses:
    - H1
    - H2
    - H3

  support:
  contradictions:
  provenance_overlap:

  discriminating_tests: []

  state: COMPETING
```

---

# 28. Discriminating Evidence

When hypotheses compete, prefer:

```text
THE CHEAPEST
HIGH-INFORMATION
DISCRIMINATING TEST
```

over accumulating redundant evidence.

This optimizes uncertainty reduction rather than evidence volume.

---

# 29. Evidence Topology

Evidence must be understood as a graph.

```text
SOURCE A
├── CLAIM 1
├── CLAIM 2
└── CLAIM 3
```

does not provide three independent confirmations.

Canonical law:

```text
REPETITION != INDEPENDENCE
```

---

# 30. Provenance Independence

Independence must be demonstrated, not assumed.

Cognition should test for:

```text
COMMON SOURCE
COMMON DATASET
COMMON MODEL
COMMON PIPELINE
COMMON AUTHOR
COMMON DERIVATION
MIRRORING
SUMMARY ANCESTRY
```

when independence is load-bearing.

---

# 31. Sybil Hardening

Many apparent sources may represent one underlying origin.

```text
SOURCE A
↓
COPY B
↓
SUMMARY C
↓
ARTICLE D
```

B, C, and D must not automatically count as independent confirmation.

---

# 32. Provenance Topology

Relevant reasoning may preserve:

```text
SOURCE IDENTITY
ANCESTRY
DEPENDENCY EDGES
DERIVATION EDGES
CORRELATION RISK
FRESHNESS
ENVIRONMENT
```

This topology is part of epistemic integrity.

---

# 33. Causal Firewall

AMOS cognition must distinguish:

```text
ASSOCIATION
CORRELATION
MECHANISM
ENABLING CONDITION
NECESSARY CONDITION
SUFFICIENT CONDITION
MEDIATION
CONFOUNDING
FEEDBACK
CAUSAL EFFECT
```

These are not interchangeable.

---

# 34. Structural Similarity Firewall

Hard law:

```text
STRUCTURAL SIMILARITY
!=
CAUSATION
```

Likewise:

```text
ANALOGY
!=
CAUSAL EVIDENCE
```

and:

```text
SEQUENCE
!=
CAUSAL PROOF
```

---

# 35. Cross-Domain Mapping

Cross-domain similarity may generate a model.

```text
DOMAIN A STRUCTURE
≈
DOMAIN B STRUCTURE
```

licenses:

```text
MODEL / HYPOTHESIS
```

not automatically:

```text
VERIFIED CAUSAL LAW
```

---

# 36. Scope Firewall

Important claims inherit an applicability envelope.

Conceptually:

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

Cognition must not silently generalize outside this envelope.

---

# 37. Regime Firewall

A result valid in:

```text
REGIME A
```

may fail in:

```text
REGIME B
```

Regime dimensions may include:

```text
MARKET CONDITIONS
SYSTEM LOAD
POLICY ENVIRONMENT
HARDWARE
SOFTWARE VERSION
POPULATION
PHYSICAL CONDITIONS
INSTITUTIONAL CONTEXT
```

---

# 38. Regime Shift

When regime changes materially:

```text
PREVIOUS CONCLUSION
↓
VALIDITY CHECK
↓
REUSE
OR
REVALIDATE
OR
INVALIDATE
```

A previously strong conclusion can become stale without being historically wrong.

---

# 39. Freshness

Trust is freshness-bounded.

Relevant temporal fields may include:

```text
OBSERVED_AT
PUBLISHED_AT
VALIDATED_AT
UPDATED_AT
EXPIRES_AT
```

Recent publication does not necessarily mean recent underlying evidence.

---

# 40. Proof Capsule

Important conclusions should conceptually carry:

```yaml
proof_capsule:
  claim:
  class:

  premises: []
  evidence: []

  provenance:
  dependencies: []

  scope:
  regime:
  freshness:

  competing_explanations: []
  falsifiers: []

  confidence_ceiling:
  invalidation_conditions: []
```

This enables safe reuse.

---

# 41. Proof Capsule Reuse

Reuse is allowed only while:

```text
DEPENDENCIES VALID
AND
SCOPE COMPATIBLE
AND
REGIME COMPATIBLE
AND
FRESHNESS VALID
AND
PROVENANCE SUFFICIENT
AND
NO MATERIAL CONFLICT EXISTS
```

Otherwise:

```text
REVALIDATE
```

---

# 42. Fast Path

AMOS v4.4 permits a fast path when the smallest sufficient proof scope is established.

Local reasoning is allowed only when:

```text
DEPENDENCY CLOSURE
+
PROVENANCE INDEPENDENCE
+
SCOPE COMPATIBILITY
+
REGIME COMPATIBILITY
+
FRESHNESS
+
NON-CONFLICT
```

are sufficient for the conclusion.

---

# 43. Fast Path Escalation

Escalate when cognition encounters:

```text
SHARED PROVENANCE ANCESTRY
CONFLICT
STALE PREMISES
REGIME CROSSING
CAUSAL COUPLING
GOVERNANCE IMPACT
IRREVERSIBLE STAKES
AMBIGUOUS DEPENDENCIES
WEAK EVIDENCE
```

Fast path must never trade correctness for speed.

---

# 44. Adversarial Validation

For consequential conclusions:

```text
BUILD STRONGEST SUPPORTED CONCLUSION
↓
CHALLENGE USING A DIFFERENT PATH
```

The challenge should seek:

```text
CONTRADICTION
CORRELATED PROVENANCE
STALE PREMISES
SCOPE LEAKAGE
HIDDEN DEPENDENCY
CAUSAL OVERREACH
STRONGER ALTERNATIVE
```

---

# 45. Challenge Independence

Adversarial validation is weak if the challenge simply repeats the original reasoning.

A meaningful challenge should vary one or more of:

```text
EVIDENCE PATH
MODEL
ASSUMPTIONS
DECOMPOSITION
PROVENANCE
CAUSAL EXPLANATION
```

---

# 46. Challenge Outcomes

If challenge fails to overturn the conclusion:

```text
RETAIN
```

within the original evidence envelope.

If challenge succeeds:

```text
DOWNGRADE
CONDITION
PRESERVE COMPETING
OR
RETURN UNKNOWN/GAP
```

---

# 47. Sensitivity

For consequential reasoning, identify:

```text
THE SMALLEST PREMISE,
THRESHOLD,
ASSUMPTION,
OR OBSERVATION
CAPABLE OF FLIPPING THE RESULT
```

Test that first.

---

# 48. Fragility

A conclusion is fragile when plausible perturbation changes the outcome.

Use:

```text
CONDITIONAL
```

where appropriate.

A robust conclusion should survive plausible changes to noncritical assumptions.

---

# 49. Uncertainty Vector

AMOS should separate material uncertainty into:

```text
EVIDENCE UNCERTAINTY
MODEL UNCERTAINTY
SCOPE UNCERTAINTY
TEMPORAL UNCERTAINTY
CAUSAL UNCERTAINTY
EXECUTION UNCERTAINTY
PROVENANCE-INDEPENDENCE UNCERTAINTY
```

A single confidence score may conceal important distinctions.

---

# 50. Uncertainty Budget

Reasoning effort should be spent where:

```text
EXPECTED DECISION VALUE
OF UNCERTAINTY REDUCTION
>
COST OF ADDITIONAL REASONING
```

This prevents exhaustive but decision-irrelevant analysis.

---

# 51. Adaptive Complexity

AMOS cognition uses adaptive complexity.

```text
C0 — DIRECT
C1 — COMPACT
C2 — STRUCTURED
C3 — DEEP
C4 — MAXIMUM
```

Start at the lowest sufficient level.

---

# 52. Complexity Escalation

Escalate for:

```text
HIGH STAKES
IRREVERSIBILITY
NOVELTY
WEAK EVIDENCE
STALE EVIDENCE
CONTRADICTION
CAUSAL AMBIGUITY
SCOPE MISMATCH
COMPETING MODELS
GOVERNANCE IMPACT
LOW TRUST
EXPLICIT DEEP-ANALYSIS REQUEST
```

---

# 53. Complexity De-Escalation

Once outcome-changing uncertainty is resolved:

```text
DE-ESCALATE
```

Do not continue reasoning merely because additional reasoning is possible.

---

# 54. Execution Sufficiency

AMOS cognition stops when three conditions are satisfied:

```text
CLAIM SUFFICIENCY
DECISION SUFFICIENCY
ACTION SUFFICIENCY
```

This is not equivalent to complete knowledge.

---

# 55. Claim Sufficiency

Claim sufficiency means the conclusion is supported strongly enough for the requested epistemic class.

---

# 56. Decision Sufficiency

Decision sufficiency means remaining uncertainty is unlikely to alter the selected decision materially.

---

# 57. Action Sufficiency

Action sufficiency means the next safe action is sufficiently specified.

Often:

```text
ACTION SUFFICIENCY
<
TOTAL EXPLANATORY COMPLETENESS
```

so exhaustive knowledge is unnecessary.

---

# 58. Gap Classification

Missing information is classified:

```text
CRITICAL
DECISION-RELEVANT
EXPLANATORY
COSMETIC
```

Resolve in that order.

---

# 59. Critical Gap

A critical gap prevents a safe or valid conclusion.

When unresolved:

```text
RETURN UNKNOWN/GAP
```

and identify the minimum missing information.

---

# 60. Decision-Relevant Gap

A decision-relevant gap may flip the decision.

It should normally be investigated before committing to a recommendation.

---

# 61. Explanatory Gap

An explanatory gap reduces understanding but does not materially change the decision.

It may remain unresolved if further investigation has low value.

---

# 62. Cosmetic Gap

A cosmetic gap affects presentation rather than validity.

It should never consume reasoning resources ahead of critical uncertainty.

---

# 63. Anti-Fabrication

Canonical law:

```text
MISSING EVIDENCE
MUST NOT
BE BRIDGED
WITH FLUENT PROSE
```

Therefore:

```text
ABSENCE OF CONTRADICTION != PROOF
POPULARITY != VALIDATION
AUTHORITY != INDEPENDENT CONFIRMATION
BENCHMARK SUCCESS != UNIVERSAL VALIDITY
```

---

# 64. Benchmark Firewall

A benchmark result establishes performance only within its tested envelope.

```text
BENCHMARK PASS
!=
UNIVERSAL CAPABILITY
```

Claims must inherit:

```text
DATASET
VERSION
HARDWARE
SOFTWARE
PARAMETERS
MEASUREMENT METHOD
TIME
```

where relevant.

---

# 65. Simulation Firewall

Simulation provides evidence about a model under specified assumptions.

```text
SIMULATION RESULT
!=
REAL-WORLD VALIDATION
```

unless empirically linked to the target system.

---

# 66. Formal Proof Firewall

Testing and formal proof are distinct.

```text
MANY TESTS PASSED
!=
FORMAL PROOF
```

Likewise:

```text
DISTRIBUTED / BYZANTINE TEST
!=
UNIVERSAL DISTRIBUTED-SYSTEM PROOF
```

unless an appropriate proof actually exists.

---

# 67. Deterministic Reasoning

AMOS cognition should use deterministic logic where the problem permits deterministic derivation.

Conceptually:

```text
SAME VALID INPUTS
+
SAME RULES
+
SAME CONTEXT
→
SAME LOGICAL RESULT
```

This does not claim every natural-language output will be byte-identical.

---

# 68. Determinism Firewall

Reasoning reproducibility depends on load-bearing context.

If context differs:

```text
INPUT
MODEL
VERSION
EVIDENCE
REGIME
TIME
```

then differing outputs do not necessarily violate deterministic logical structure.

---

# 69. Causal Lineage

Important conclusions should retain reasoning lineage sufficient to identify:

```text
WHAT PREMISES SUPPORTED THEM
WHAT EVIDENCE SUPPORTED THOSE PREMISES
WHAT DEPENDENCIES WERE USED
WHAT CHANGED WHEN THE CONCLUSION CHANGED
```

This enables selective invalidation.

---

# 70. Persistent Cognition

Reusable cognition requires persistence of relevant:

```text
RSCFs
PROOF CAPSULES
PROVENANCE
DEPENDENCIES
SCOPE
REGIME
FRESHNESS
FALSIFIERS
CONFLICTS
```

Persisting only final prose is insufficient for high-integrity reuse.

---

# 71. Atomic Multi-RSCF Reasoning

A conclusion may depend on multiple RSCFs.

```text
RSCF A
+
RSCF B
+
RSCF C
↓
CONCLUSION D
```

If all are load-bearing:

```text
PARTIAL VALIDATION
!=
VALIDATION OF D
```

---

# 72. Cognitive Dependency Closure

Before using a local conclusion, AMOS should establish that all material dependencies required for that conclusion are resolved sufficiently.

This is:

```text
DEPENDENCY CLOSURE
```

Closure is conclusion-relative, not necessarily global.

---

# 73. Proof-Based Coordination Avoidance

Independent cognitive branches need not always synchronize globally.

If:

```text
DEPENDENCIES ARE DISJOINT
PROVENANCE IS SUFFICIENTLY INDEPENDENT
NO SHARED INVARIANT IS AFFECTED
NO CONFLICT EXISTS
```

then local reasoning may proceed.

Independence must be demonstrated.

---

# 74. Cognitive Finality

A reasoning result becomes sufficiently final for its purpose when:

```text
LOAD-BEARING PREMISES RESOLVED
+
REQUIRED CHALLENGES PASSED
+
MATERIAL CONFLICTS HANDLED
+
SCOPE / REGIME VALID
+
DECISION-CHANGING UNCERTAINTY ACCEPTABLE
```

Finality is purpose-relative.

---

# 75. Cognitive Finality != Canon Finality

Hard boundary:

```text
REASONING FINALITY
!=
CANON PROMOTION
```

A cognitive conclusion can be sufficient for action while remaining:

```text
MODEL
CONDITIONAL
DERIVED
```

rather than canon.

---

# 76. Action Governance

Validation requirements increase with:

```text
IRREVERSIBLE COST
LEGAL EXPOSURE
FINANCIAL EXPOSURE
HEALTH IMPACT
SAFETY IMPACT
INSTITUTIONAL IMPACT
LARGE DOWNSTREAM DEPENDENCY
```

High-impact cognition should favor:

```text
STAGED
REVERSIBLE
REPAIRABLE
OBSERVABLE
```

actions.

---

# 77. Reversibility Principle

Under unresolved uncertainty:

```text
PREFER
REVERSIBLE ACTION
```

when it preserves decision value without materially increasing risk.

---

# 78. Known / Inferred / Action Separation

Consequential outputs should distinguish:

```text
KNOWN
INFERRED
UNKNOWN
FALSIFIERS
SAFE ACTION
```

when doing so materially improves decision integrity.

---

# 79. Cognitive Evolution

AMOS cognition may evolve.

Evolution must be governed.

```text
CURRENT COGNITIVE MODEL
↓
PROPOSED CHANGE
↓
VALIDATION
↓
ANTI-REGRESSION CHECK
↓
PROVENANCE
↓
GOVERNANCE
↓
PROMOTION
```

---

# 80. Governed Evolution

No cognitive optimization may weaken:

```text
FACTUAL SUPPORT
SCOPE CORRECTNESS
CONTRADICTION VISIBILITY
PROVENANCE RECOVERABILITY
CAUSAL DISCIPLINE
SAFETY
USER FIT
```

If it does:

```text
ROLL BACK
```

---

# 81. Anti-Regression

An optimization is accepted only if it preserves or improves integrity dimensions.

Conceptually:

```text
NEW METHOD
>=
OLD METHOD
```

for all load-bearing integrity properties, or trade-offs must be explicitly governed.

---

# 82. Knowledge Harvest

AMOS cognitive outputs may move through:

```text
EPHEMERAL CODE / ANALYSIS
↓
PERSISTENT EVIDENCE
↓
VALIDATED KNOWLEDGE
```

Promotion must preserve provenance.

---

# 83. Documentation Firewall

Documentation and README statements begin as:

```text
SOURCE_CLAIM
```

unless independently validated.

A project's own description is evidence of what the project claims, not automatic evidence that the implementation satisfies that description.

---

# 84. Cognitive Memory

Memory can support cognition by preserving context.

But:

```text
MEMORY != KNOWLEDGE
MEMORY != CANON
MEMORY != VERIFIED FACT
```

Memory should not silently override current evidence.

---

# 85. Cognitive State

Useful cognitive state may include:

```text
CURRENT OBJECTIVE
ACTIVE RSCFs
OPEN GAPS
COMPETING HYPOTHESES
ASSUMPTIONS
UNCERTAINTY VECTOR
DEPENDENCY GRAPH
VALID PROOF CAPSULES
INVALIDATED CAPSULES
```

This state is operational context, not automatically canon.

---

# 86. Failure Recovery

When reasoning fails:

```text
IDENTIFY FAILED PREMISE / EDGE
↓
INVALIDATE DESCENDANTS
↓
RETURN TO NEAREST VALID STATE
↓
REROUTE LOCALLY
↓
REVALIDATE
```

Do not repeat the failed path unless evidence or assumptions change.

---

# 87. No Blind Retry

Canonical law:

```text
FAILED PATH
+
UNCHANGED EVIDENCE
+
UNCHANGED ASSUMPTIONS
→
DO NOT BLINDLY REPEAT
```

A retry requires changed information, method, or hypothesis.

---

# 88. Global Recomputation

Global recomputation is a last resort.

Use it only when:

```text
DEPENDENCY DAMAGE IS GLOBAL
OR
PROVENANCE IS UNRECOVERABLE
OR
REGIME CHANGE INVALIDATES BROAD STATE
OR
LOCALIZATION FAILS
```

---

# 89. Cognitive Integrity Invariants

```text
COG-001 INTEGRITY > COMPLETENESS

COG-002 CAPABILITY != AUTHORITY

COG-003 RUNTIME != COGNITION

COG-004 ORGAN != AGENT

COG-005 SOURCE_CLAIM != VERIFIED

COG-006 MODEL != EMPIRICAL FACT

COG-007 UNKNOWN/GAP != PASS

COG-008 STRUCTURAL SIMILARITY != CAUSATION

COG-009 CORRELATION != CAUSATION

COG-010 REPETITION != INDEPENDENCE

COG-011 COPIES != INDEPENDENT CONFIRMATION

COG-012 CONFIDENCE CANNOT EXCEED THE WEAKEST LOAD-BEARING PREMISE WITHOUT INDEPENDENT REVALIDATION

COG-013 SCOPE MUST NOT SILENTLY EXPAND

COG-014 REGIME CHANGE MAY INVALIDATE CONCLUSIONS

COG-015 FRESHNESS IS PART OF VALIDITY

COG-016 CONTRADICTIONS MUST REMAIN VISIBLE

COG-017 COMPETING HYPOTHESES MUST NOT BE FORCED TO CONVERGE

COG-018 LOCAL FAILURE != GLOBAL RESET

COG-019 FAST PATH MUST PRESERVE INTEGRITY

COG-020 INDEPENDENCE MUST BE DEMONSTRATED

COG-021 PROPOSAL != COMMIT

COG-022 REASONING FINALITY != CANON FINALITY

COG-023 MEMORY != CANON

COG-024 BENCHMARK SUCCESS != UNIVERSAL VALIDITY

COG-025 SIMULATION != REAL-WORLD VALIDATION

COG-026 TEST SUCCESS != FORMAL PROOF

COG-027 ABSENCE OF CONTRADICTION != PROOF

COG-028 MISSING EVIDENCE MUST NOT BE FABRICATED

COG-029 IRREVERSIBILITY INCREASES VALIDATION REQUIREMENTS

COG-030 OPTIMIZATION MUST NOT WEAKEN INTEGRITY
```

---

# 90. Cognitive Validation Matrix

| Dimension     | Required question                                     |
| ------------- | ----------------------------------------------------- |
| Objective     | What exactly must be answered or decided?             |
| Scope         | Where does the conclusion apply?                      |
| Evidence      | What supports the load-bearing premises?              |
| Provenance    | Where did the evidence originate?                     |
| Independence  | Are apparently separate sources actually independent? |
| Freshness     | Is the evidence current enough?                       |
| Regime        | Is the operating regime compatible?                   |
| Causality     | Is causal language licensed by causal evidence?       |
| Contradiction | What credible evidence challenges the conclusion?     |
| Alternatives  | What competing hypotheses remain?                     |
| Sensitivity   | What smallest change flips the result?                |
| Confidence    | What is the weakest load-bearing premise?             |
| Governance    | What authority is required for action?                |
| Reversibility | Can the proposed action be safely reversed?           |
| Gaps          | What unresolved information could change the outcome? |

---

# 91. Cognitive Test Families

A mature AMOS implementation should eventually test:

```text
RSCF CONSTRUCTION
RSCF RECURSION
DEPENDENCY CLOSURE
LOCAL INVALIDATION
H/M/L RETRIEVAL
PROOF CAPSULE REUSE
PROVENANCE ANCESTRY
SOURCE CORRELATION
SYBIL DETECTION
SCOPE ENFORCEMENT
REGIME INVALIDATION
FRESHNESS EXPIRY
COMPETING HYPOTHESES
DISCRIMINATING TEST SELECTION
CAUSAL FIREWALL
SENSITIVITY ANALYSIS
UNCERTAINTY VECTOR
ADAPTIVE COMPLEXITY
FAST-PATH ESCALATION
ADVERSARIAL VALIDATION
FAILURE RECOVERY
ANTI-REGRESSION
ACTION GOVERNANCE
```

---

# 92. Adversarial Test Cases

Useful cognitive adversarial tests include:

```text
THREE SOURCES WITH ONE COMMON ORIGIN

RECENT ARTICLE USING STALE DATA

STRONG CORRELATION WITHOUT MECHANISM

MODEL VALID IN ONE REGIME APPLIED TO ANOTHER

HIGH-CONFIDENCE CONCLUSION WITH ONE WEAK LOAD-BEARING PREMISE

TWO EQUALLY SUPPORTED CONTRADICTORY HYPOTHESES

BENCHMARK RESULT GENERALIZED TO DIFFERENT HARDWARE

SIMULATION RESULT PRESENTED AS EMPIRICAL FACT

MISSING DATA INTERPRETED AS ZERO

FAST PATH USED DESPITE CROSS-DEPENDENCY

LOCAL FAILURE CAUSING UNNECESSARY GLOBAL RESET
```

---

# 93. Canonical Reasoning Template

```text
1. DEFINE OBJECTIVE
2. DEFINE SCOPE / STAKES / FRESHNESS
3. IDENTIFY DECISION-CHANGING UNCERTAINTY
4. RETRIEVE MINIMUM SUFFICIENT H/M/L PATH
5. IDENTIFY LOAD-BEARING PREMISES
6. BUILD RSCF
7. CHECK PROVENANCE TOPOLOGY
8. APPLY SCOPE / REGIME FIREWALL
9. APPLY CAUSAL FIREWALL
10. PRESERVE COMPETING HYPOTHESES
11. RUN ADVERSARIAL CHALLENGE
12. TEST SENSITIVITY
13. ASSIGN WEAKEST ACCURATE CONCLUSION CLASS
14. DETERMINE DECISION / ACTION SUFFICIENCY
15. RETURN CONCISE, GAP-VISIBLE OUTPUT
```

---

# 94. Canonical Failure Template

```text
CONCLUSION FAILS
↓
LOCATE FAILED PREMISE
↓
TRACE DEPENDENTS
↓
INVALIDATE ONLY DEPENDENTS
↓
PRESERVE UNAFFECTED RSCFs
↓
SEARCH ALTERNATIVE PATH
↓
REVALIDATE
↓
UPDATE CONCLUSION CLASS
```

---

# 95. Cognitive Output Contract

AMOS cognition should normally lead with the conclusion when safe.

Then surface only what materially supports it:

```text
CONCLUSION
DECISIVE EVIDENCE
MATERIAL UNCERTAINTY
COMPETING EXPLANATION
INVALIDATION CONDITION
NEXT ACTION
```

Internal reasoning machinery need not be exposed to produce an auditable result.

---

# 96. Explainability Boundary

AMOS should expose:

```text
KEY ASSUMPTIONS
DECISIVE PREMISES
EVIDENCE BASIS
MATERIAL ALTERNATIVES
UNCERTAINTY
FALSIFIERS
```

where useful.

It need not expose private implementation internals or hidden reasoning traces.

---

# 97. Implementation Firewall

This canon defines an **AMOS architectural cognition model**.

It does not establish that every current AMOS implementation literally implements:

```text
ALL RSCF MECHANISMS
ALL GMEF MECHANISMS
AUTOMATED PROVENANCE TOPOLOGY
AUTOMATED SYBIL DETECTION
FULL CAUSAL INFERENCE
AUTOMATED REGIME DETECTION
ATOMIC MULTI-RSCF EXECUTION
DISTRIBUTED COGNITIVE FINALITY
FORMALLY VERIFIED REASONING
```

unless implementation evidence exists.

These remain:

```text
AMOS_MODEL
```

or:

```text
UNKNOWN/GAP
```

as appropriate.

---

# 98. Promotion Gate

Promotion:

```text
ACTIVE_CANON_CANDIDATE
→
ACTIVE_CANON
```

requires canonical review of at least:

- cognition boundary;
- cognition versus runtime;
- cognition versus agent;
- H/M/L semantics;
- RSCF semantics;
- GMEF source binding;
- epistemic types;
- conclusion classes;
- provenance topology;
- independence requirements;
- competing hypotheses;
- causal firewall;
- scope firewall;
- regime firewall;
- freshness;
- proof capsules;
- fast path;
- adversarial validation;
- sensitivity;
- uncertainty vector;
- adaptive complexity;
- failure recovery;
- governed evolution;
- action governance;
- implementation boundaries.

Unresolved GMEF semantics should remain explicitly `UNKNOWN/GAP` rather than being invented during promotion.

---

# 99. RSCF Node

```yaml
node_id: AMOS_COGNITION_CANON

functional_type:
  - COGNITIVE_ARCHITECTURE_MODEL
  - EPISTEMIC_INTEGRITY_MODEL
  - REASONING_GOVERNANCE_MODEL
  - ADAPTIVE_REASONING_MODEL

lifecycle_stage:
  CANON_CANDIDATE

origin_architect:
  Trang Phan

steward:
  Trang Phan

amos_core_target:
  v4.4

claim_class:
  AMOS_MODEL

claim: >
  AMOS cognition should derive the strongest conclusion justified by
  available evidence while preserving provenance, dependency structure,
  epistemic type, scope, regime, freshness, causal discipline,
  contradictions, competing hypotheses, uncertainty, falsifiers,
  authority boundaries, and recovery paths.

critical_invariants:
  - INTEGRITY > COMPLETENESS
  - CAPABILITY != AUTHORITY
  - SOURCE_CLAIM != VERIFIED
  - MODEL != EMPIRICAL FACT
  - UNKNOWN/GAP != PASS
  - STRUCTURAL SIMILARITY != CAUSATION
  - REPETITION != INDEPENDENCE
  - SCOPE MUST NOT SILENTLY EXPAND
  - CONTRADICTIONS MUST REMAIN VISIBLE
  - LOCAL FAILURE != GLOBAL RESET
  - FAST PATH MUST PRESERVE INTEGRITY

known_gap:
  - Exact GMEF operational semantics require binding to authoritative canonical source definitions.

does_not_establish:
  - implementation completeness
  - empirical correctness of every cognitive subsystem
  - universal causal inference capability
  - formal verification of reasoning
  - literal implementation of every distributed v4.4 coordination concept
```

---

# 100. Changelog

## v2.0.0 — 2026-08-25

Expanded the cognition placeholder into an AMOS v4.4-aligned canon candidate.

Added:

- cognition boundary;
- cognition/runtime/agent separation;
- canonical cognitive cycle;
- smallest-sufficient-proof rule;
- fractal H/M/L retrieval;
- recursive RSCF;
- GMEF gap boundary;
- evidence typing;
- conclusion classes;
- confidence ceiling;
- provenance topology;
- Sybil hardening;
- competing hypotheses;
- discriminating evidence;
- causal firewall;
- scope/regime/freshness firewalls;
- proof capsules;
- v4.4 fast path;
- adversarial validation;
- sensitivity analysis;
- uncertainty vector;
- adaptive complexity C0–C4;
- claim/decision/action sufficiency;
- gap classification;
- anti-fabrication;
- benchmark/simulation/formal-proof firewalls;
- deterministic reasoning boundary;
- causal lineage;
- atomic multi-RSCF reasoning;
- proof-based coordination avoidance;
- cognitive finality;
- action governance;
- governed evolution;
- anti-regression;
- failure recovery;
- validation matrix;
- adversarial test families;
- implementation firewall.

## v1.0.0 — 2026-08-25

Initial placeholder reserved the canonical AMOS OS location.

---

# 101. Canonical Summary

```text
AMOS COGNITION
=
GOVERNED EVIDENCE-BOUND REASONING
```

The core cognitive path is:

```text
OBJECTIVE
↓
SCOPE / STAKES
↓
DECISION-CHANGING UNCERTAINTY
↓
H
↓
M
↓
L
↓
RSCF
↓
PROVENANCE / DEPENDENCY CHECK
↓
CAUSAL + SCOPE + REGIME FIREWALLS
↓
COMPETING HYPOTHESES
↓
ADVERSARIAL VALIDATION
↓
SENSITIVITY
↓
CONCLUSION CLASS
↓
DECISION / ACTION SUFFICIENCY
```

The core laws remain:

```text
INTEGRITY > COMPLETENESS

CAPABILITY != AUTHORITY

RUNTIME != COGNITION

ORGAN != AGENT

SOURCE_CLAIM != VERIFIED

MODEL != EMPIRICAL FACT

UNKNOWN/GAP != PASS

STRUCTURAL SIMILARITY != CAUSATION

CORRELATION != CAUSATION

REPETITION != INDEPENDENCE

SCOPE MUST NOT SILENTLY EXPAND

REGIME CHANGE MAY INVALIDATE CONCLUSIONS

CONTRADICTIONS MUST REMAIN VISIBLE

COMPETING HYPOTHESES MUST NOT BE FORCED TO CONVERGE

LOCAL FAILURE != GLOBAL RESET

FAST PATH MUST PRESERVE INTEGRITY
```

The canonical objective is:

```text
KNOW WHAT IS SUPPORTED,
KNOW WHAT IS INFERRED,
KNOW WHAT REMAINS UNKNOWN,
KNOW WHERE THE EVIDENCE CAME FROM,
KNOW WHERE THE CONCLUSION APPLIES,
KNOW WHAT COULD INVALIDATE IT,
AND NEVER MAKE THE ANSWER
STRONGER THAN THE EVIDENCE.
```

---

**Related:** README|AMOS OS · 00_ROOT_MOC|MOC · ARCHITECTURE|Architecture · SYSTEM_MAP|System Map · NEURAL_NETWORK|AMOS Neural Network · AMOS Canon · CANON_MAP|Canon Map · [[AMOS_CORE_LAWS|AMOS Core Laws]] · INVARIANT_REGISTRY|Invariant Registry · LAW_HIERARCHY|Law Hierarchy · HML_CANON|H/M/L Canon · PERSISTENCE_CANON|Persistence Canon · KERNEL_MAP|Kernel Map · CONTROL_PLANE_MAP|Control Plane Map · RUNTIME_MAP|Runtime Map · COGNITIVE_ORGANISM_MAP|Cognitive Organism Map · AGENT_MAP|Agent Map · WORKFLOW_MAP|Workflow Map · MEMORY_MEMORY_MAP|Memory Map · Knowledge Map · STATE_STATE_MAP|State Map · MODEL_MAP|Model Map · SCHEMA_MAP|Schema Map · OBSERVABILITY_OBSERVABILITY_MAP|Observability Map · TEST_MAP|Test Map · COGNITIVE_MATRIX_ARCHITECTURE|Cognitive Matrix

---

00_ROOT_MOC|AMOS MOC

---
**Related:** [[00_HOME]] · [[AMOS_RSCF_NODES]]

---
RSCF-NODE
node_id: cognition_canon
node_type: note
path: 01_CANON/03_COGNITION_CANON/COGNITION_CANON.md
RSCF-RELATIONS:
  - INDEXED_BY: [[00_HOME]]
  - INDEXED_BY: [[AMOS_RSCF_NODES]]
claim_class: AMOS_MODEL

---
**MOC:** [[03_COGNITION_CANON_MOC]]
