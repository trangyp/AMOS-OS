---
artifact_id: AMOS-COGNITIVE-ORGANISM-CANON
name: COGNITIVE_ORGANISM_CANON
title: "AMOS Cognitive Organism Canon — Governed Cognitive Subsystem Architecture"

document_version: "2.0.0"
canon_version: "4.4"
amos_core_target: "v4.4"

status: ACTIVE_CANON_CANDIDATE
conclusion_class: AMOS_MODEL
rscf_state: derived

canon_group: tech-ai
canon_type: cognitive-organism-canon

origin_architect: Trang Phan
steward: Trang Phan

created: 2026-08-25
updated: 2026-08-25

tags:
  - amos
  - amos-os
  - amos-core
  - amos-core-v4-4
  - cognition
  - cognitive-organism
  - cognitive-architecture
  - cognitive-organs
  - reasoning
  - perception
  - memory
  - learning
  - planning
  - decision
  - metacognition
  - rscf
  - hml
  - provenance
  - uncertainty
  - adaptive-complexity
  - governed-evolution
  - canon-group/tech-ai
  - canon/framework
  - canon/model
  - rscf/claim
  - rscf/provenance
  - rscf/state/derived
  - topic/cognitive-organism-canon

aliases:
  - AMOS Cognitive Organism Canon
  - Cognitive Organism Canon
  - AMOS Cognitive Organism
  - Cognitive Organ Architecture

related:
  - "[[00_ROOT/README.md|AMOS OS]]"
  - "[[00_ROOT/ARCHITECTURE.md|Architecture]]"
  - "[[00_ROOT/SYSTEM_MAP.md|System Map]]"
  - "[[01_CANON/00_INDEX/CANON_MAP.md|Canon Map]]"
  - "[[01_CANON/AMOS_CORE_LAWS.md|AMOS Core Laws]]"
  - "[[01_CANON/INVARIANT_REGISTRY.md|Invariant Registry]]"
  - "[[01_CANON/LAW_HIERARCHY.md|Law Hierarchy]]"
  - "[[01_CANON/COGNITION_CANON.md|Cognition Canon]]"
  - "[[01_CANON/HML_CANON.md|H/M/L Canon]]"
  - "[[01_CANON/PERSISTENCE_CANON.md|Persistence Canon]]"
  - "[[05_COGNITIVE_ORGANISM/00_INDEX/COGNITIVE_ORGANISM_MAP.md|Cognitive Organism Map]]"
  - "[[06_AGENTS/00_INDEX/AGENT_MAP.md|Agent Map]]"
  - "[[07_SKILLS/00_INDEX/SKILL_MAP.md|Skill Map]]"
  - "[[08_WORKFLOWS/00_INDEX/WORKFLOW_MAP.md|Workflow Map]]"
  - "[[10_MEMORY/00_INDEX/MEMORY_MAP.md|Memory Map]]"
  - "[[11_KNOWLEDGE/00_AMOS_Full_Brain_OS_Architecture.md|AMOS Full Brain OS Architecture]]"
  - "[[25_COGNITIVE_MATRIX/00_INDEX/ARCHITECTURE.md|Cognitive Matrix]]"
---

# AMOS Cognitive Organism Canon

**Origin architect / steward:** Trang Phan

> **Status:** `ACTIVE_CANON_CANDIDATE`  
> **AMOS Core target:** `v4.4`  
> **Conclusion class:** `AMOS_MODEL`

---

# 0. Purpose

The **AMOS Cognitive Organism Canon** defines the canonical architectural role of the `05_COGNITIVE_ORGANISM` plane.

The Cognitive Organism is the governed composition layer for cognitive capabilities inside AMOS OS.

It organizes specialized cognitive functions into a coherent reasoning organism without collapsing them into agents, workflows, runtime machinery, models, memory, or authority.

Canonical abstraction:

```text
INPUT / CONTEXT
↓
PERCEPTION
↓
ATTENTION
↓
FRAMING
↓
RETRIEVAL
↓
REASONING
↓
SIMULATION / HYPOTHESIS
↓
PLANNING
↓
DECISION SUPPORT
↓
METACOGNITIVE VALIDATION
↓
PROPOSAL / COGNITIVE OUTPUT
```

Cross-cutting cognitive substrates:

```text
MEMORY ACCESS
KNOWLEDGE ACCESS
PROVENANCE
UNCERTAINTY
RSCF
H/M/L
CAUSAL DISCIPLINE
SCOPE / REGIME
CONTRADICTION
SENSITIVITY
LEARNING
```

The Cognitive Organism exists to coordinate cognition.

It does **not** possess unrestricted authority to act.

---

# 1. Canonical Position in AMOS OS

The Cognitive Organism occupies a specific architectural plane:

```text
CANON
↓
KERNEL
↓
CONTROL PLANE
↓
RUNTIME
↓
COGNITIVE ORGANISM
↓
AGENTS / SKILLS / WORKFLOWS
↓
TOOLS / MODELS / DOMAIN ADAPTERS
↓
EXTERNAL EFFECTS
```

This ordering defines architectural responsibility, not necessarily a literal synchronous execution sequence.

The Cognitive Organism consumes governed capabilities from lower infrastructure layers and exposes cognitive capability to higher role/execution structures.

---

# 2. Hard Architectural Boundaries

```text
CANON != COGNITIVE ORGANISM

KERNEL != COGNITIVE ORGANISM

CONTROL_PLANE != COGNITIVE ORGANISM

RUNTIME != COGNITIVE ORGANISM

COGNITION != AUTHORITY

COGNITIVE ORGAN != AGENT

COGNITIVE ORGAN != SKILL

COGNITIVE ORGAN != WORKFLOW

COGNITIVE ORGAN != MODEL

COGNITIVE ORGAN != MEMORY

COGNITIVE ORGAN != TOOL

CAPABILITY != AUTHORITY

PROPOSAL != COMMIT
```

These separations are load-bearing.

---

# 3. Cognitive Organism Definition

Conceptually:

```text
COGNITIVE ORGANISM
=
GOVERNED COMPOSITION
OF SPECIALIZED COGNITIVE ORGANS
```

A cognitive organism may contain capabilities for:

```text
PERCEPTION
ATTENTION
CONTEXT FORMATION
RETRIEVAL
MEMORY ACCESS
PATTERN ANALYSIS
REASONING
CAUSAL ANALYSIS
HYPOTHESIS GENERATION
SIMULATION
PLANNING
DECISION SUPPORT
METACOGNITION
LEARNING
ADAPTATION
```

The exact implemented organ inventory must be determined from authoritative implementation artifacts.

Missing implementation evidence remains:

```text
UNKNOWN/GAP
```

---

# 4. Organism != Monolith

AMOS should not model cognition as one opaque undifferentiated block.

Instead:

```text
COGNITIVE ORGANISM
├── COGNITIVE ORGAN A
├── COGNITIVE ORGAN B
├── COGNITIVE ORGAN C
└── ...
```

Each organ should eventually declare:

```text
PURPOSE
INPUT CONTRACT
OUTPUT CONTRACT
DEPENDENCIES
STATE ACCESS
AUTHORITY BOUNDARY
PROVENANCE REQUIREMENTS
INVARIANTS
FAILURE MODES
TESTS
RECOVERY
```

---

# 5. Organ Contract

Canonical conceptual schema:

```yaml
cognitive_organ:
  organ_id:
  name:
  purpose:

  inputs: []
  outputs: []

  dependencies: []

  reads:
    memory: []
    knowledge: []
    state: []

  writes:
    memory: []
    state: []

  capabilities: []
  prohibited_actions: []

  authority:
    level:
    permissions: []

  provenance_requirements: []
  invariants: []

  failure_modes: []
  recovery_paths: []

  tests: []
```

A directory or filename alone does not prove this contract exists operationally.

---

# 6. Capability / Authority Firewall

A cognitive organ can be highly capable without possessing execution authority.

```text
CAPABILITY
=
WHAT THE ORGAN CAN COMPUTE
```

```text
AUTHORITY
=
WHAT THE ORGAN IS PERMITTED TO COMMIT OR EFFECT
```

Therefore:

```text
CAPABILITY != AUTHORITY
```

A planning organ may produce a plan.

That does not authorize execution.

A decision-support organ may recommend a decision.

That does not constitute commitment.

A learning organ may propose an update.

That does not authorize canon mutation.

---

# 7. Organ != Agent

An organ represents a cognitive function.

An agent represents a role-based operational actor.

Conceptually:

```text
COGNITIVE ORGAN
=
REUSABLE COGNITIVE CAPABILITY
```

while:

```text
AGENT
=
IDENTITY
+
ROLE
+
OBJECTIVE
+
CAPABILITIES
+
BOUNDARIES
+
AUTHORITY ENVELOPE
+
RUNTIME CONTRACT
```

An agent may invoke multiple organs.

Multiple agents may reuse the same organ.

Therefore:

```text
1 ORGAN → N AGENTS
```

is valid.

And:

```text
1 AGENT → N ORGANS
```

is also valid.

---

# 8. Organ != Skill

A skill is a reusable procedure or bounded operational method.

A cognitive organ is a persistent architectural cognitive capability.

```text
ORGAN
=
COGNITIVE FUNCTION
```

```text
SKILL
=
REUSABLE PROCEDURE
```

A skill may invoke an organ.

An organ may use skills.

Neither identity should silently replace the other.

---

# 9. Organ != Workflow

A workflow defines orchestration across steps.

```text
WORKFLOW
=
ORDERED / CONDITIONAL EXECUTION GRAPH
```

A cognitive organ provides a capability used within that graph.

Therefore:

```text
ORGAN != WORKFLOW
```

Even when an organ internally contains multiple processing stages.

---

# 10. Organ != Model

Models may support cognition.

Examples:

```text
FOUNDATION MODEL
DOMAIN MODEL
CALIBRATION MODEL
PREDICTIVE MODEL
CAUSAL MODEL
SIMULATION MODEL
```

But:

```text
MODEL != COGNITIVE ORGAN
```

A model supplies computational or representational capability.

An organ governs how that capability participates in cognition.

---

# 11. Organ != Memory

Memory is persistent or session-bounded information state.

A memory organ may manage access to memory, but:

```text
MEMORY ORGAN != MEMORY STORE
```

and:

```text
MEMORY != COGNITION
```

Stored information does not reason merely because it is available.

---

# 12. Organ != Knowledge

Knowledge provides evidence, claims, frameworks, RSCFs, and validated structures.

The Cognitive Organism reasons over knowledge.

Therefore:

```text
KNOWLEDGE != COGNITIVE ORGANISM
```

The organism must not silently convert every retrieved knowledge object into verified truth.

---

# 13. Organ != Runtime

Runtime executes.

The Cognitive Organism reasons.

```text
RUNTIME
=
SCHEDULING
ROUTING
EXECUTION
RESOURCE MANAGEMENT
LIFECYCLE
```

```text
COGNITIVE ORGANISM
=
COGNITIVE FUNCTION
COGNITIVE COMPOSITION
REASONING CONTROL
```

Therefore:

```text
RUNTIME != COGNITION
```

---

# 14. Organ != Control Plane

The control plane governs:

```text
POLICY
AUTHORITY
COMMIT
PROVENANCE CONTROL
STATE TRANSITIONS
```

The Cognitive Organism may request or propose governed transitions.

It does not silently bypass them.

Canonical path:

```text
COGNITIVE RESULT
↓
PROPOSAL
↓
AUTHORITY / POLICY CHECK
↓
COMMIT OR REJECT
```

---

# 15. Organ != Canon

Cognitive outputs do not become canon automatically.

```text
COGNITIVE OUTPUT
!=
CANON
```

Promotion requires the appropriate:

```text
PROVENANCE
REVIEW
VALIDATION
SUPERSESSION
GOVERNANCE
```

process.

---

# 16. Canonical Organ Families

The following are architectural families rather than assertions that every named implementation already exists.

```text
01 PERCEPTION
02 ATTENTION
03 CONTEXT
04 MEMORY ACCESS
05 KNOWLEDGE RETRIEVAL
06 REASONING
07 CAUSAL ANALYSIS
08 HYPOTHESIS
09 SIMULATION
10 PLANNING
11 DECISION SUPPORT
12 METACOGNITION
13 LEARNING
14 ADAPTATION
15 INTEGRATION
```

Specific implementation names must be bound separately.

---

# 17. Perception Organ Family

Purpose:

```text
RAW / STRUCTURED INPUT
↓
COGNITIVELY USABLE OBSERVATION
```

Responsibilities may include:

```text
INPUT NORMALIZATION
SIGNAL EXTRACTION
OBSERVATION FORMATION
SOURCE IDENTIFICATION
QUALITY CHECKING
```

Perception must not automatically convert observations into conclusions.

---

# 18. Attention Organ Family

Purpose:

```text
AVAILABLE INFORMATION
↓
DECISION-RELEVANT INFORMATION
```

Attention allocates limited reasoning resources.

Potential responsibilities:

```text
SALIENCE
PRIORITIZATION
NOVELTY
RISK
CONTRADICTION
DECISION VALUE
```

Attention priority does not establish truth.

```text
SALIENCE != VALIDITY
```

---

# 19. Context Organ Family

Context establishes the active reasoning envelope.

It may maintain:

```text
OBJECTIVE
SCOPE
STAKE LEVEL
TIME
REGIME
USER INTENT
ACTIVE ASSUMPTIONS
DEPENDENCIES
```

Context leakage must be controlled.

A conclusion derived under one context must not silently migrate into another incompatible context.

---

# 20. Memory Access Organ Family

Memory-access organs mediate retrieval from memory systems.

Potential memory classes:

```text
WORKING
EPISODIC
SEMANTIC
PROCEDURAL
LONG-TERM
SESSION
PROVENANCE
```

Retrieval does not establish validity.

```text
REMEMBERED != VERIFIED
```

---

# 21. Knowledge Retrieval Organ Family

Knowledge retrieval should use the smallest sufficient path.

Canonical fractal traversal:

```text
BOOTSTRAP
↓
H
↓
M
↓
L
↓
RAW EVIDENCE
```

Raw evidence should not be loaded unless needed.

This supports:

```text
EFFICIENCY
LOCALITY
PROVENANCE
REVALIDATION
```

without weakening integrity.

---

# 22. Reasoning Organ Family

Reasoning organs transform premises into derived conclusions.

They must preserve:

```text
PREMISES
DEPENDENCIES
EVIDENCE TYPE
PROVENANCE
SCOPE
REGIME
FRESHNESS
UNCERTAINTY
```

where load-bearing.

---

# 23. Recursive RSCF Integration

RSCF is a primary reasoning structure.

```text
CLAIM
├── PREMISE A
│   └── RSCF A
├── PREMISE B
│   └── RSCF B
└── CONCLUSION
```

The Cognitive Organism should permit local reasoning over these structures without requiring global recomputation where dependency closure is established.

---

# 24. Atomic Multi-RSCF Cognition

Complex conclusions may depend on multiple RSCFs.

```text
RSCF A
+
RSCF B
+
RSCF C
↓
COMPOSITE CONCLUSION
```

If all are load-bearing:

```text
VALID(A)
AND
VALID(B)
AND
VALID(C)
```

is required within the applicable envelope.

Partial validity must not silently become composite validity.

---

# 25. Causal Analysis Organ Family

Causal cognition must distinguish:

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

Structural resemblance alone cannot establish causation.

---

# 26. Hypothesis Organ Family

Hypothesis cognition should generate multiple plausible explanations when evidence permits.

```text
OBSERVATIONS
↓
H1
H2
H3
...
```

Generation should not immediately force selection.

---

# 27. Competing Hypothesis Preservation

When incompatible hypotheses remain materially supported:

```text
STATE = COMPETING
```

AMOS must preserve the competition.

Do not collapse:

```text
H1 vs H2
```

into a single narrative merely because one answer is stylistically easier.

---

# 28. Discriminating-Test Selection

The organism should prefer:

```text
CHEAPEST
HIGH-INFORMATION
DISCRIMINATING TEST
```

capable of separating competing hypotheses.

Evidence quantity alone is not the objective.

Decision-changing information is.

---

# 29. Simulation Organ Family

Simulation may evaluate:

```text
WHAT-IF
COUNTERFACTUAL
SCENARIO
SYSTEM DYNAMICS
STRATEGY
RISK
```

under explicit assumptions.

Hard boundary:

```text
SIMULATION != OBSERVATION
```

and:

```text
SIMULATION RESULT != EMPIRICAL VALIDATION
```

---

# 30. Planning Organ Family

Planning converts objectives and constraints into candidate action structures.

```text
OBJECTIVE
+
CONSTRAINTS
+
AVAILABLE CAPABILITIES
+
STATE
↓
PLAN
```

A plan remains:

```text
PROPOSAL
```

until authorized.

---

# 31. Decision-Support Organ Family

Decision-support cognition compares alternatives under uncertainty.

It may consider:

```text
EXPECTED VALUE
RISK
REVERSIBILITY
ROBUSTNESS
DEPENDENCIES
UNCERTAINTY
OPTION VALUE
GOVERNANCE
```

The output should remain typed as recommendation or decision support unless authority explicitly grants more.

---

# 32. Metacognition Organ Family

Metacognition reasons about reasoning.

Responsibilities may include:

```text
ASSUMPTION CHECK
CONTRADICTION CHECK
CONFIDENCE CHECK
PROVENANCE CHECK
SCOPE CHECK
REGIME CHECK
FRESHNESS CHECK
CAUSAL CHECK
SENSITIVITY CHECK
GAP DETECTION
```

Metacognition is a critical integrity layer.

---

# 33. Adversarial Cognition

Consequential conclusions should support a genuinely different challenge path.

```text
PRIMARY REASONING
↓
CONCLUSION
```

then:

```text
ALTERNATIVE PATH
↓
SEEK FAILURE
```

The challenge should search for:

```text
CONTRADICTION
CORRELATED PROVENANCE
STALE PREMISES
HIDDEN DEPENDENCIES
SCOPE LEAKAGE
REGIME MISMATCH
CAUSAL OVERREACH
STRONGER ALTERNATIVE
```

---

# 34. Learning Organ Family

Learning changes reusable cognitive state based on new evidence.

But:

```text
OBSERVATION
!=
AUTOMATIC LEARNING
```

and:

```text
LEARNING
!=
CANON MUTATION
```

A proposed learned update should pass appropriate validation.

---

# 35. Governed Learning

Canonical pattern:

```text
NEW EVIDENCE
↓
PROPOSED UPDATE
↓
PROVENANCE CHECK
↓
CONFLICT CHECK
↓
SCOPE / REGIME CHECK
↓
VALIDATION
↓
ACCEPT / REJECT / QUARANTINE
```

High-impact learning requires stronger governance.

---

# 36. Adaptation Organ Family

Adaptation modifies cognitive strategy rather than necessarily modifying knowledge.

Examples:

```text
CHANGE RETRIEVAL DEPTH
CHANGE COMPLEXITY LEVEL
CHANGE HYPOTHESIS SET
CHANGE VALIDATION DEPTH
CHANGE TOOL SELECTION
```

Adaptation must remain within policy and authority boundaries.

---

# 37. Adaptive Complexity

The Cognitive Organism should support:

```text
C0 — DIRECT
C1 — COMPACT
C2 — STRUCTURED
C3 — DEEP
C4 — MAXIMUM
```

Start at the lowest sufficient level.

Escalate only where material uncertainty or stakes justify it.

---

# 38. Complexity Escalation Conditions

Escalation triggers include:

```text
HIGH STAKES
IRREVERSIBILITY
NOVELTY
WEAK EVIDENCE
STALE EVIDENCE
CONTRADICTION
CAUSAL AMBIGUITY
SCOPE MISMATCH
REGIME CHANGE
COMPETING MODELS
GOVERNANCE IMPACT
LOW TRUST
AMBIGUOUS DEPENDENCIES
```

---

# 39. Cognitive Fast Path

AMOS v4.4 permits local fast-path cognition when sufficient conditions are satisfied.

Conceptually:

```text
LOCAL PROBLEM
+
DEPENDENCY CLOSURE
+
PROVENANCE SUFFICIENCY
+
SCOPE COMPATIBILITY
+
REGIME COMPATIBILITY
+
FRESHNESS
+
NO MATERIAL CONFLICT
↓
LOCAL REASONING
```

---

# 40. Fast Path Firewall

Fast-path reasoning must escalate when:

```text
EVIDENCE SHARES ANCESTRY
CONFLICT EXISTS
PREMISES ARE STALE
REGIMES DIFFER
CAUSAL COUPLING EXISTS
GOVERNANCE IS AFFECTED
STAKES ARE IRREVERSIBLE
DEPENDENCIES ARE UNCLEAR
```

Therefore:

```text
FAST PATH != LOWER INTEGRITY
```

---

# 41. Cognitive Integration Organ

A cognitive organism requires integration across specialized organs.

Conceptually:

```text
PERCEPTION
+
MEMORY
+
KNOWLEDGE
+
REASONING
+
HYPOTHESIS
+
PLANNING
+
METACOGNITION
↓
INTEGRATED COGNITIVE STATE
```

Integration must preserve disagreement rather than overwrite it.

---

# 42. No Forced Consensus

Different organs may produce conflicting outputs.

Example:

```text
PATTERN ORGAN → H1

CAUSAL ORGAN → H2

RISK ORGAN → H3
```

The integrator must not automatically average or collapse them.

Instead:

```text
COMPARE
TRACE
TEST
PRESERVE COMPETING
```

until discriminating evidence exists.

---

# 43. Cognitive State Model

Conceptual state:

```yaml
cognitive_state:
  objective:
  context:

  active_observations: []
  active_claims: []
  active_rscfs: []

  hypotheses: []
  contradictions: []

  assumptions: []
  dependencies: []

  uncertainty:
    evidence:
    model:
    scope:
    temporal:
    causal:
    execution:
    provenance_independence:

  active_proof_capsules: []
  invalidated_proof_capsules: []

  open_gaps: []

  proposed_actions: []
```

This is an architectural model, not an assertion of current serialized implementation.

---

# 44. Provenance as Cognitive Substrate

Cognition must remain provenance-aware.

Relevant provenance may include:

```text
SOURCE
SOURCE IDENTITY
ANCESTRY
DERIVATION
DEPENDENCY
TIME
ENVIRONMENT
MODEL
TRANSFORMATION
```

A conclusion without recoverable load-bearing provenance should be downgraded where provenance is necessary.

---

# 45. Evidence Independence

Multiple cognitive organs using the same source do not create independent evidence.

```text
ONE SOURCE
↓
ORGAN A
ORGAN B
ORGAN C
```

still represents shared ancestry.

Canonical law:

```text
MULTIPLE ORGANS
!=
MULTIPLE INDEPENDENT SOURCES
```

---

# 46. Sybil-Hardened Cognition

The organism must resist false confidence created by duplicated evidence.

```text
ORIGIN A
├── COPY B
├── SUMMARY C
├── MODEL OUTPUT D
└── REPORT E
```

may still constitute one provenance family.

Repetition does not manufacture independence.

---

# 47. Scope Firewall

Each material cognitive result inherits an applicability envelope.

```yaml
applicability:
  system:
  population:
  environment:
  scale:
  time:
  regime:
  measurement_method:
  assumptions:
```

No organ may silently widen this scope.

---

# 48. Regime Firewall

The organism must detect when cognitive reuse crosses regimes.

```text
RESULT VALID IN R1
+
CURRENT CONTEXT R2
↓
COMPATIBILITY CHECK
```

If compatibility cannot be established:

```text
REVALIDATE
```

or:

```text
UNKNOWN/GAP
```

---

# 49. Freshness Firewall

Cognitive reuse is freshness-bounded.

A previously valid proof capsule may become stale because:

```text
SOURCE CHANGED
SYSTEM CHANGED
MODEL CHANGED
REGULATION CHANGED
ENVIRONMENT CHANGED
REGIME CHANGED
DEPENDENCY CHANGED
```

Freshness is part of validity.

---

# 50. Sensitivity Organ Function

The organism should identify the smallest change capable of flipping an important conclusion.

```text
PREMISE
THRESHOLD
ASSUMPTION
OBSERVATION
MODEL CHOICE
```

If plausible perturbation flips the result:

```text
CONCLUSION = CONDITIONAL
```

where appropriate.

---

# 51. Uncertainty Vector

Cognitive uncertainty should remain multidimensional:

```text
U =
[
  U_evidence,
  U_model,
  U_scope,
  U_temporal,
  U_causal,
  U_execution,
  U_provenance
]
```

Collapsing all uncertainty into one score may destroy useful information.

---

# 52. Proof Capsules

Reusable cognitive conclusions should conceptually carry:

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

Proof capsules support safe reuse across the organism.

---

# 53. Proof Capsule Routing

An organ may reuse a proof capsule only when:

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
NO MATERIAL CONFLICT
```

Otherwise the capsule must be revalidated.

---

# 54. Confidence Ceiling

A composite cognitive result cannot be stronger than its weakest load-bearing premise unless independently revalidated.

Conceptually:

```text
C(result)
<=
MIN(
  C(load-bearing premises)
)
```

This applies across organ composition.

---

# 55. Cognitive Failure Localization

When an organ fails:

```text
FAILED ORGAN / PREMISE / EDGE
↓
DEPENDENCY TRACE
↓
LOCAL INVALIDATION
↓
PRESERVE UNAFFECTED STATE
↓
REROUTE
```

Hard law:

```text
LOCAL COGNITIVE FAILURE
!=
GLOBAL COGNITIVE RESET
```

---

# 56. Cognitive Recovery

Recovery should prefer:

```text
NEAREST VALID STATE
```

rather than restarting the complete reasoning process.

Potential recovery paths:

```text
ALTERNATIVE ORGAN
ALTERNATIVE MODEL
ALTERNATIVE SOURCE
LOWER-SCOPE CLAIM
CONDITIONAL RESULT
COMPETING RESULT
UNKNOWN/GAP
```

---

# 57. No Blind Cognitive Retry

If:

```text
PATH P
```

fails with:

```text
EVIDENCE E
ASSUMPTIONS A
MODEL M
```

then rerunning:

```text
P + E + A + M
```

without material change should not be treated as new validation.

---

# 58. Cognitive Degradation

When some cognitive capability is unavailable, the organism should degrade explicitly.

Example:

```text
CAUSAL ORGAN UNAVAILABLE
↓
ASSOCIATIONAL ANALYSIS MAY CONTINUE
↓
CAUSAL CLAIMS DISALLOWED
```

Capability loss must narrow permitted conclusions.

---

# 59. Fail-Closed Principle

For integrity-critical cognitive functions:

```text
UNKNOWN/GAP
```

should fail closed where a positive validation is required.

Therefore:

```text
NO PROVENANCE
!=
PROVENANCE PASS
```

```text
NO CONFLICT CHECK
!=
NO CONFLICT
```

```text
NO CAUSAL EVIDENCE
!=
CAUSAL VALIDATION
```

---

# 60. Cognitive Lifecycle

Canonical lifecycle:

```text
REGISTER
↓
INITIALIZE
↓
READY
↓
ACTIVATE
↓
REASON
↓
VALIDATE
↓
OUTPUT
↓
PERSIST ELIGIBLE STATE
↓
IDLE / CONTINUE
```

Failure branch:

```text
FAILURE
↓
LOCALIZE
↓
ROLLBACK
↓
RECOVER
↓
REVALIDATE
```

---

# 61. Organ Registration

Every implemented organ should eventually be discoverable through a typed registry.

Registry entries should identify at minimum:

```text
ORGAN ID
TYPE
VERSION
STATUS
INPUT CONTRACT
OUTPUT CONTRACT
DEPENDENCIES
AUTHORITY
IMPLEMENTATION REFERENCE
```

Existence in the registry does not prove operational health.

---

# 62. Organ Version Identity

File identity and semantic version identity are distinct.

```text
FILENAME
!=
ARTIFACT ID
!=
SEMANTIC IDENTITY
!=
VERSION IDENTITY
```

Canonical filenames should not require version suffixes.

Version evolution belongs in metadata, provenance, hashes, revisions, and supersession records.

---

# 63. Cognitive Organ Health

Potential health states:

```text
UNKNOWN
INITIALIZING
READY
DEGRADED
FAILED
QUARANTINED
RETIRED
```

Health should be observable rather than inferred from file presence.

---

# 64. Observability

Cognitive observability may include:

```text
ORGAN ACTIVATION
LATENCY
DEPENDENCY ACCESS
MODEL ACCESS
RSCF CREATION
PROOF CAPSULE REUSE
CONFLICT DETECTION
ESCALATION
FAILURE
RECOVERY
```

Observability must respect privacy and IP boundaries.

---

# 65. Traceability

Important cognitive outputs should be traceable to:

```text
ORGAN(S)
MODEL(S)
KNOWLEDGE
MEMORY
RSCF(S)
PROVENANCE
SCOPE
REGIME
```

where material.

Traceability does not require exposing private hidden reasoning.

---

# 66. Security Boundary

Cognitive capability does not grant access.

An organ must operate through governed access controls.

```text
COGNITIVE NEED
↓
ACCESS REQUEST
↓
AUTHORIZATION
↓
RESOURCE ACCESS
```

not:

```text
COGNITIVE NEED
↓
UNRESTRICTED ACCESS
```

---

# 67. Tool Boundary

Tools create capabilities for observation or effect.

```text
TOOL != PERMISSION
```

A cognitive organ may recommend tool use.

Tool execution still requires the appropriate runtime and authority path.

---

# 68. External Effect Firewall

The Cognitive Organism should not directly create uncontrolled external effects.

Canonical boundary:

```text
COGNITIVE ORGANISM
↓
PROPOSAL
↓
AGENT / WORKFLOW
↓
CONTROL / AUTHORITY CHECK
↓
RUNTIME
↓
TOOL
↓
EXTERNAL EFFECT
```

Exact implementation routing may differ, but authority must not disappear.

---

# 69. Cognitive Safety

Validation intensity increases with consequence.

```text
LOW STAKES
→
LOWER VALIDATION BURDEN

HIGH STAKES
→
HIGHER VALIDATION BURDEN
```

Relevant dimensions:

```text
IRREVERSIBILITY
FINANCIAL IMPACT
LEGAL IMPACT
HEALTH IMPACT
SAFETY IMPACT
INSTITUTIONAL IMPACT
DOWNSTREAM DEPENDENCY
```

---

# 70. Reversibility

Under unresolved uncertainty, cognition should prefer recommendations that are:

```text
REVERSIBLE
STAGED
OBSERVABLE
REPAIRABLE
```

when these preserve the objective.

---

# 71. Cognitive Finality

A cognitive result reaches purpose-relative finality when:

```text
LOAD-BEARING PREMISES RESOLVED
+
DEPENDENCY CLOSURE ESTABLISHED
+
MATERIAL CONFLICTS HANDLED
+
SCOPE / REGIME VALID
+
REQUIRED CHALLENGE COMPLETED
+
DECISION-CHANGING UNCERTAINTY ACCEPTABLE
```

---

# 72. Finality != Immutability

A cognitively final result may later become invalid.

Triggers include:

```text
NEW EVIDENCE
DEPENDENCY FAILURE
REGIME CHANGE
SOURCE RETRACTION
MODEL CHANGE
CONTRADICTION
EXPIRY
```

Therefore:

```text
FINAL
!=
FOREVER TRUE
```

---

# 73. Cognitive Finality != Canon Finality

```text
COGNITIVE FINALITY
!=
CANON FINALITY
```

A cognitive result can be sufficient for a decision while remaining:

```text
DERIVED
MODEL
CONDITIONAL
COMPETING
```

---

# 74. Persistent Provenance

Where cognitive outputs are persisted, provenance should persist with them.

Persisting:

```text
CONCLUSION ONLY
```

while discarding:

```text
DEPENDENCIES
SCOPE
REGIME
SOURCE LINEAGE
```

weakens safe reuse.

---

# 75. MVCC / CAS Alignment

Where AMOS implementation uses MVCC/CAS-style state concepts, cognition should respect versioned state boundaries.

Conceptually:

```text
READ STATE VERSION V
↓
REASON
↓
PROPOSE WRITE AGAINST V
↓
VALIDATE CURRENT VERSION
↓
COMMIT OR RETRY / REVALIDATE
```

This section is an architectural alignment model, not proof that every cognitive organ implements literal MVCC/CAS primitives.

---

# 76. Stale-State Firewall

If cognitive reasoning was derived from:

```text
STATE V1
```

but authoritative state is now:

```text
STATE V2
```

the organism must determine whether the difference is material before committing downstream action.

```text
STALE INPUT
!=
CURRENT VALIDATION
```

---

# 77. Proof-Based Coordination Avoidance

Cognitive organs need not globally coordinate when local independence is established.

Local execution may proceed when:

```text
DEPENDENCY CLOSURE
AND
PROVENANCE INDEPENDENCE
AND
NO SHARED MUTABLE INVARIANT
AND
NO MATERIAL CONFLICT
```

are demonstrated.

This is a reasoning pattern aligned with AMOS v4.4, not a claim that all cognition is literally distributed.

---

# 78. Cognitive Shards

A cognitive problem may be decomposed into local reasoning shards.

```text
PROBLEM
├── SHARD A
├── SHARD B
└── SHARD C
```

Each shard should preserve:

```text
SCOPE
DEPENDENCIES
PROVENANCE
OUTPUT CLASS
```

before composition.

---

# 79. Shard-Local Finalization

A shard may finalize locally only if its relevant dependency closure is established.

```text
LOCAL FINALITY
!=
GLOBAL FINALITY
```

Composite reasoning must still validate cross-shard dependencies.

---

# 80. Causal Epoch Alignment

Where causal epoch concepts are used by AMOS Core v4.4, cognitive reuse should not silently cross an invalidated causal epoch.

Conceptually:

```text
EPOCH E1 RESULT
+
CURRENT EPOCH E2
↓
CAUSAL COMPATIBILITY CHECK
```

Exact implementation semantics must remain bound to authoritative AMOS Core sources.

---

# 81. Cognitive Evolution

The Cognitive Organism may evolve through:

```text
OBSERVATION
↓
PROPOSED CHANGE
↓
TEST
↓
ADVERSARIAL VALIDATION
↓
ANTI-REGRESSION
↓
PROVENANCE
↓
GOVERNANCE
↓
PROMOTION
```

No organ should self-promote structural changes without governance.

---

# 82. Anti-Regression

An optimization must not weaken:

```text
FACTUAL SUPPORT
SCOPE CORRECTNESS
CONTRADICTION VISIBILITY
PROVENANCE RECOVERABILITY
CAUSAL DISCIPLINE
SAFETY
AUTHORITY BOUNDARIES
RECOVERY
```

If it does:

```text
REJECT
OR
ROLL BACK
```

---

# 83. Organ Replacement

Replacement should preserve lineage.

```text
ORGAN A
↓
SUPERSEDED BY
↓
ORGAN B
```

Required metadata should eventually include:

```text
REASON
DATE
PROVENANCE
COMPATIBILITY
MIGRATION PATH
ROLLBACK PATH
```

Deletion without lineage destroys recoverability.

---

# 84. Cognitive Organism Invariants

```text
COGORG-001 COGNITION != AUTHORITY

COGORG-002 COGNITIVE ORGAN != AGENT

COGORG-003 COGNITIVE ORGAN != SKILL

COGORG-004 COGNITIVE ORGAN != WORKFLOW

COGORG-005 COGNITIVE ORGAN != MODEL

COGORG-006 COGNITIVE ORGAN != MEMORY

COGORG-007 RUNTIME != COGNITIVE ORGANISM

COGORG-008 CONTROL_PLANE != COGNITIVE ORGANISM

COGORG-009 COGNITIVE OUTPUT != CANON

COGORG-010 CAPABILITY != AUTHORITY

COGORG-011 PROPOSAL != COMMIT

COGORG-012 MEMORY RETRIEVAL != VERIFICATION

COGORG-013 MULTIPLE ORGANS != INDEPENDENT EVIDENCE

COGORG-014 STRUCTURAL SIMILARITY != CAUSATION

COGORG-015 SIMULATION != EMPIRICAL VALIDATION

COGORG-016 LOCAL FAILURE != GLOBAL RESET

COGORG-017 LOCAL FINALITY != GLOBAL FINALITY

COGORG-018 FAST PATH != LOWER INTEGRITY

COGORG-019 UNKNOWN/GAP != PASS

COGORG-020 FINAL != IMMUTABLE

COGORG-021 FILENAME != VERSION IDENTITY

COGORG-022 TOOL != PERMISSION

COGORG-023 LEARNING != CANON MUTATION

COGORG-024 SALIENCE != VALIDITY

COGORG-025 STALE INPUT != CURRENT VALIDATION
```

---

# 85. Minimum Organ Validation Contract

Every production-grade cognitive organ should eventually answer:

| Dimension     | Required question                               |
| ------------- | ----------------------------------------------- |
| Identity      | What cognitive capability is this?              |
| Purpose       | Why does it exist?                              |
| Inputs        | What may enter?                                 |
| Outputs       | What may leave?                                 |
| Dependencies  | What must be valid for it to operate?           |
| Scope         | Where is its result applicable?                 |
| State         | What state can it read or write?                |
| Memory        | What memory classes can it access?              |
| Knowledge     | What knowledge classes can it access?           |
| Models        | Which models may it invoke?                     |
| Tools         | Which tools may it request?                     |
| Authority     | What may it actually authorize?                 |
| Provenance    | What lineage must it preserve?                  |
| Failure       | How can it fail?                                |
| Recovery      | How is failure localized and repaired?          |
| Tests         | How is correct behavior verified?               |
| Observability | How is health measured?                         |
| Security      | What access restrictions apply?                 |
| Version       | What semantic implementation/version is active? |
| Supersession  | What replaces it when evolved?                  |

---

# 86. Cognitive Organ Test Families

Expected test families include:

```text
ORGAN CONTRACT TESTS
INPUT VALIDATION
OUTPUT VALIDATION
DEPENDENCY TESTS
AUTHORITY-BOUNDARY TESTS
PROVENANCE TESTS
RSCF TESTS
H/M/L ROUTING TESTS
CONTRADICTION TESTS
CAUSAL-FIREWALL TESTS
SCOPE TESTS
REGIME TESTS
FRESHNESS TESTS
MEMORY-ACCESS TESTS
MODEL-ROUTING TESTS
FAILURE-LOCALIZATION TESTS
RECOVERY TESTS
FAST-PATH TESTS
ESCALATION TESTS
ADVERSARIAL TESTS
ANTI-REGRESSION TESTS
OBSERVABILITY TESTS
SECURITY TESTS
```

---

# 87. Organ Composition Tests

Composition tests should verify that valid individual organs do not create invalid aggregate cognition.

Examples:

```text
VALID ORGAN A
+
VALID ORGAN B
!=
AUTOMATICALLY VALID COMPOSITION
```

Tests should detect:

```text
SHARED HIDDEN DEPENDENCY
PROVENANCE CORRELATION
STATE CONFLICT
SCOPE MISMATCH
REGIME MISMATCH
CIRCULAR REASONING
AUTHORITY ESCALATION
```

---

# 88. Adversarial Cognitive Organism Tests

High-value adversarial scenarios include:

```text
MULTIPLE ORGANS USING ONE SOURCE

MEMORY RETURNING STALE CLAIM

PLANNER TREATING MODEL OUTPUT AS FACT

SIMULATOR TREATED AS OBSERVATION

AGENT ATTEMPTING TO BYPASS CONTROL PLANE

COGNITIVE ORGAN WRITING AUTHORITATIVE STATE DIRECTLY

FAST PATH WITH HIDDEN SHARED DEPENDENCY

LOCAL RSCF FAILURE PROPAGATED GLOBALLY

HIGH-SALIENCE LOW-VALIDITY EVIDENCE

REGIME SHIFT WITHOUT REVALIDATION

MODEL UPDATE INVALIDATING OLD PROOF CAPSULE

COMPETING HYPOTHESES FORCED INTO CONSENSUS
```

---

# 89. Required Cognitive Organism Index

The `05_COGNITIVE_ORGANISM` plane should eventually maintain a map comparable to:

```text
05_COGNITIVE_ORGANISM/
│
├── 00_INDEX/
│   ├── COGNITIVE_ORGANISM_MAP.md
│   ├── ORGAN_REGISTRY.md
│   ├── DEPENDENCY_MAP.md
│   └── AUTHORITY_MAP.md
│
├── 01_PERCEPTION/
├── 02_ATTENTION/
├── 03_CONTEXT/
├── 04_MEMORY_ACCESS/
├── 05_KNOWLEDGE_RETRIEVAL/
├── 06_REASONING/
├── 07_CAUSAL/
├── 08_HYPOTHESIS/
├── 09_SIMULATION/
├── 10_PLANNING/
├── 11_DECISION/
├── 12_METACOGNITION/
├── 13_LEARNING/
├── 14_ADAPTATION/
└── 15_INTEGRATION/
```

This is a **placement model**, not proof these directories are currently canonical or implemented.

Exact tree promotion requires reconciliation with the authoritative repository tree.

---

# 90. Cognitive Organism Map Contract

`COGNITIVE_ORGANISM_MAP.md` should eventually answer:

```text
WHAT ORGANS EXIST?
WHAT DOES EACH ORGAN DO?
WHAT DEPENDS ON WHAT?
WHAT IS IMPLEMENTED?
WHAT IS PLACEHOLDER?
WHAT IS VALIDATED?
WHAT IS DEPRECATED?
WHAT AUTHORITY DOES EACH ORGAN HAVE?
WHAT STATE CAN EACH ORGAN ACCESS?
```

---

# 91. Organ Registry Contract

`ORGAN_REGISTRY.md` should eventually maintain typed entries such as:

```yaml
organ:
  id:
  semantic_name:
  family:
  implementation:
  version:
  status:
  authority:
  dependencies:
  tests:
  provenance:
```

Registry membership alone is not validation.

---

# 92. Dependency Map Contract

The dependency map should distinguish:

```text
REQUIRED
OPTIONAL
FALLBACK
MUTABLE
CAUSAL
DATA
CONTROL
PROVENANCE
```

dependency edges where relevant.

This enables selective failure propagation.

---

# 93. Authority Map Contract

The authority map should explicitly identify:

```text
READ
PROPOSE
WRITE
COMMIT
EXECUTE
PROMOTE
INVALIDATE
```

permissions.

Default principle:

```text
NO EXPLICIT AUTHORITY
=
NO AUTHORITY
```

for privileged operations.

---

# 94. Conclusion Classes

Cognitive Organism outputs must use the weakest accurate class:

```text
VERIFIED
DERIVED
MODEL
CONDITIONAL
COMPETING
UNKNOWN/GAP
```

Organ complexity does not justify stronger conclusion classes.

---

# 95. Implementation Firewall

This canon defines the intended AMOS Cognitive Organism architecture.

It does **not** by itself establish implementation of:

```text
ALL ORGAN FAMILIES
FULL ORGAN REGISTRY
AUTOMATED RSCF ROUTING
AUTOMATED H/M/L RETRIEVAL
AUTOMATED CAUSAL INFERENCE
AUTOMATED PROVENANCE TOPOLOGY
AUTOMATED SYBIL HARDENING
AUTOMATED REGIME DETECTION
ATOMIC MULTI-RSCF TRANSACTIONS
MVCC/CAS COGNITIVE STATE
CAUSAL EPOCH FINALITY
SHARD-LOCAL FINALIZATION
PROOF-BASED DISTRIBUTED COORDINATION
FORMALLY VERIFIED COGNITIVE INVARIANTS
```

unless separately evidenced.

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

# 96. Promotion Gate

Promotion:

```text
ACTIVE_CANON_CANDIDATE
→
ACTIVE_CANON
```

requires review of at least:

```text
COGNITIVE ORGANISM BOUNDARY
ORGAN TAXONOMY
ORGAN CONTRACT
AGENT FIREWALL
SKILL FIREWALL
WORKFLOW FIREWALL
MODEL FIREWALL
MEMORY FIREWALL
RUNTIME FIREWALL
CONTROL-PLANE FIREWALL
RSCF INTEGRATION
H/M/L INTEGRATION
PROVENANCE
AUTHORITY
STATE
FAILURE LOCALIZATION
RECOVERY
FAST PATH
ADVERSARIAL VALIDATION
OBSERVABILITY
SECURITY
TESTS
VERSIONING
SUPERSESSION
```

Any unresolved implementation question remains explicitly:

```text
UNKNOWN/GAP
```

---

# 97. RSCF Node

```yaml
node_id: AMOS_COGNITIVE_ORGANISM_CANON

functional_type:
  - COGNITIVE_ARCHITECTURE_MODEL
  - COGNITIVE_COMPOSITION_MODEL
  - COGNITIVE_GOVERNANCE_MODEL

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
  The AMOS Cognitive Organism is the governed composition plane for
  specialized cognitive capabilities. It coordinates perception,
  retrieval, reasoning, hypothesis formation, simulation, planning,
  decision support, metacognition, learning, and adaptation while
  preserving provenance, scope, regime, uncertainty, dependency,
  authority, and failure boundaries.

critical_invariants:
  - COGNITION != AUTHORITY
  - COGNITIVE ORGAN != AGENT
  - COGNITIVE ORGAN != SKILL
  - COGNITIVE ORGAN != WORKFLOW
  - COGNITIVE ORGAN != MODEL
  - COGNITIVE ORGAN != MEMORY
  - RUNTIME != COGNITIVE ORGANISM
  - CONTROL_PLANE != COGNITIVE ORGANISM
  - CAPABILITY != AUTHORITY
  - PROPOSAL != COMMIT
  - MULTIPLE ORGANS != INDEPENDENT EVIDENCE
  - LOCAL FAILURE != GLOBAL RESET
  - FAST PATH != LOWER INTEGRITY
  - UNKNOWN/GAP != PASS

known_gaps:
  - Exact production cognitive-organ inventory requires repository binding.
  - Exact GMEF integration requires authoritative source binding.
  - Exact causal-epoch runtime semantics require authoritative v4.4 implementation binding.
  - Literal MVCC/CAS implementation must not be inferred from architectural alignment.

does_not_establish:
  - implementation completeness
  - empirical validation
  - autonomous authority
  - unrestricted external execution
  - formal verification
  - implementation of every conceptual organ
```

---

# 98. Changelog

## v2.0.0 — 2026-08-25

Expanded the original placeholder into an AMOS v4.4-aligned Cognitive Organism canon candidate.

Added:

* architectural plane definition;
* cognition/authority firewall;
* organ/agent separation;
* organ/skill separation;
* organ/workflow separation;
* organ/model separation;
* organ/memory separation;
* runtime/control-plane separation;
* canonical organ contract;
* organ-family taxonomy;
* perception;
* attention;
* context;
* memory access;
* knowledge retrieval;
* reasoning;
* recursive and multi-RSCF integration;
* causal cognition;
* hypothesis competition;
* simulation;
* planning;
* decision support;
* metacognition;
* learning;
* adaptation;
* adaptive complexity;
* v4.4 fast path;
* cognitive integration;
* provenance topology;
* evidence-independence firewall;
* scope/regime/freshness;
* sensitivity;
* uncertainty vector;
* proof capsules;
* confidence ceiling;
* local failure recovery;
* cognitive lifecycle;
* registry requirements;
* observability;
* security;
* external-effect firewall;
* finality;
* persistent provenance;
* MVCC/CAS alignment boundary;
* cognitive shards;
* shard-local finalization;
* causal-epoch alignment;
* anti-regression;
* organ replacement;
* validation/test contracts;
* implementation firewall.

## v1.0.0 — 2026-08-25

Initial placeholder reserved the canonical AMOS OS location.

---

# 99. Canonical Summary

```text
AMOS COGNITIVE ORGANISM
=
GOVERNED COMPOSITION
OF SPECIALIZED COGNITIVE CAPABILITIES
```

Canonical flow:

```text
ENVIRONMENT / INPUT
↓
PERCEPTION
↓
ATTENTION
↓
CONTEXT
↓
MEMORY + KNOWLEDGE RETRIEVAL
↓
REASONING
↓
CAUSAL ANALYSIS
↓
HYPOTHESIS / SIMULATION
↓
PLANNING
↓
DECISION SUPPORT
↓
METACOGNITIVE CHALLENGE
↓
INTEGRATION
↓
COGNITIVE RESULT
↓
PROPOSAL
```

Authority remains outside unrestricted cognition:

```text
PROPOSAL
↓
CONTROL / GOVERNANCE
↓
AUTHORIZED COMMIT
↓
RUNTIME
↓
EXTERNAL EFFECT
```

Core laws:

```text
COGNITION != AUTHORITY

COGNITIVE ORGAN != AGENT

COGNITIVE ORGAN != SKILL

COGNITIVE ORGAN != WORKFLOW

COGNITIVE ORGAN != MODEL

COGNITIVE ORGAN != MEMORY

RUNTIME != COGNITION

CONTROL_PLANE != COGNITION

CAPABILITY != AUTHORITY

PROPOSAL != COMMIT

MEMORY RETRIEVAL != VERIFICATION

MULTIPLE ORGANS != INDEPENDENT EVIDENCE

SIMULATION != EMPIRICAL VALIDATION

LOCAL FAILURE != GLOBAL RESET

LOCAL FINALITY != GLOBAL FINALITY

FAST PATH != LOWER INTEGRITY

UNKNOWN/GAP != PASS
```

Canonical objective:

```text
SPECIALIZE COGNITION
WITHOUT FRAGMENTING INTEGRITY.

COMPOSE CAPABILITIES
WITHOUT COLLAPSING AUTHORITY.

REUSE KNOWLEDGE
WITHOUT LOSING PROVENANCE.

ADAPT REASONING
WITHOUT WEAKENING INVARIANTS.

FAIL LOCALLY.
RECOVER LOCALLY.
ESCALATE WHEN REQUIRED.

AND NEVER ALLOW
COGNITIVE CAPABILITY
TO SILENTLY BECOME
EXECUTION AUTHORITY.
```

---

**Related:** [[00_ROOT/README.md|AMOS OS]] · [[00_ROOT/MOC.md|MOC]] · [[00_ROOT/ARCHITECTURE.md|Architecture]] · [[00_ROOT/SYSTEM_MAP.md|System Map]] · [[00_ROOT/NEURAL_NETWORK.md|AMOS Neural Network]] · [[01_CANON/README.md|AMOS Canon]] · [[01_CANON/00_INDEX/CANON_MAP.md|Canon Map]] · [[01_CANON/AMOS_CORE_LAWS.md|AMOS Core Laws]] · [[01_CANON/INVARIANT_REGISTRY.md|Invariant Registry]] · [[01_CANON/LAW_HIERARCHY.md|Law Hierarchy]] · [[01_CANON/COGNITION_CANON.md|Cognition Canon]] · [[01_CANON/HML_CANON.md|H/M/L Canon]] · [[01_CANON/PERSISTENCE_CANON.md|Persistence Canon]] · [[02_KERNEL/00_INDEX/KERNEL_MAP.md|Kernel Map]] · [[03_CONTROL_PLANE/00_INDEX/CONTROL_PLANE_MAP.md|Control Plane Map]] · [[04_RUNTIME/00_INDEX/RUNTIME_MAP.md|Runtime Map]] · [[05_COGNITIVE_ORGANISM/00_INDEX/COGNITIVE_ORGANISM_MAP.md|Cognitive Organism Map]] · [[05_COGNITIVE_ORGANISM/00_INDEX/ORGAN_REGISTRY.md|Organ Registry]] · [[05_COGNITIVE_ORGANISM/00_INDEX/DEPENDENCY_MAP.md|Cognitive Dependency Map]] · [[05_COGNITIVE_ORGANISM/00_INDEX/AUTHORITY_MAP.md|Cognitive Authority Map]] · [[06_AGENTS/00_INDEX/AGENT_MAP.md|Agent Map]] · [[07_SKILLS/00_INDEX/SKILL_MAP.md|Skill Map]] · [[08_WORKFLOWS/00_INDEX/WORKFLOW_MAP.md|Workflow Map]] · [[09_PROTOCOLS/00_INDEX/PROTOCOL_MAP.md|Protocol Map]] · [[10_MEMORY/00_INDEX/MEMORY_MAP.md|Memory Map]] · [[11_KNOWLEDGE/00_INDEX/KNOWLEDGE_MAP.md|Knowledge Map]] · [[11_KNOWLEDGE/00_AMOS_Full_Brain_OS_Architecture.md|AMOS Full Brain OS Architecture]] · [[12_STATE/00_INDEX/STATE_MAP.md|State Map]] · [[13_MODELS/00_INDEX/MODEL_MAP.md|Model Map]] · [[14_TOOLS/00_INDEX/TOOL_MAP.md|Tool Map]] · [[16_SCHEMAS/00_INDEX/SCHEMA_MAP.md|Schema Map]] · [[17_OBSERVABILITY/00_INDEX/OBSERVABILITY_MAP.md|Observability Map]] · [[18_SECURITY/00_INDEX/SECURITY_MAP.md|Security Map]] · [[19_TESTS/00_INDEX/TEST_MAP.md|Test Map]] · [[20_OPERATIONS/00_INDEX/OPERATIONS_MAP.md|Operations Map]] · [[25_COGNITIVE_MATRIX/00_INDEX/ARCHITECTURE.md|Cognitive Matrix]]

```
```
