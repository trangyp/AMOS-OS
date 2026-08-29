---
title: L02 ATTENTION PRIMITIVES COGNITIVE MATRIX RSCF
type: cognitive
source: 25_COGNITIVE_MATRIX/01_PRIMITIVES/L02_ATTENTION
tags:
- cognitive-matrix
- primitives
- l02_attention
- note
- domain/cognitive-matrix
rscf:
  state: DERIVED
  claim_class: DERIVED
  provenance: AMOS_corpus
  scope: AMOS_general
---

# L02 ATTENTION PRIMITIVES COGNITIVE MATRIX RSCF

The direct `L02_ATTENTION` source currently exposes only the placeholder: it defines L02 as **attention allocation / budgeting scarce reasoning-observation resources** and explicitly requires **RSCF/GMEF links, provenance, repair, tests, governance, freshness, and version lineage** before promotion. No canonical `RSCF.md` was recovered, so the detailed capsule below is intentionally classified as `AMOS_MODEL`, with unresolved canon/runtime fields left visible.

---
tags:
  - amos
  - cognitive-matrix
  - l02
  - attention
  - rscf
  - hml
  - provenance
  - governance

title: L02_ATTENTION — RSCF
origin_architect: "Trang Phan"
status: "MODEL_SPECIFICATION / SOURCE-BOUNDED / UNVALIDATED"
epistemic_class: "MODEL"
runtime_alignment: "AMOS Full Brain OS / AMOS_CORE v4.4 lineage"
---

# L02_ATTENTION — RSCF

**Class:** `COGNITIVE_PRIMITIVE_RSCF_CONTRACT`
**Origin architect / steward:** Trang Phan
**Primitive:** `L02_ATTENTION`
**Artifact:** `RSCF.md`
**Status:** `AMOS_MODEL / SOURCE-BOUNDED / UNVALIDATED`

> **Canon boundary:** direct L02 source currently supports the primitive role—attention allocation and budgeting scarce reasoning/observation resources—and requires an RSCF integration surface before promotion. The detailed RSCF graph, node IDs, equations, confidence rules, reuse semantics, and runtime mappings below are an AMOS model completion unless independently recovered from direct canon or executable evidence.

---

# 0. Purpose

Define the Recursive Structured Claim Framework contract for `L02_ATTENTION`.

The RSCF layer exists to ensure that attention allocation is not driven by untyped prose, hidden assumptions, stale conclusions, correlated evidence, or unsupported confidence.

It represents L02 reasoning as an explicit graph of:

```text
claims
premises
evidence
provenance
dependencies
scope
regime
freshness
H/M/L position
competing hypotheses
falsifiers
confidence ceilings
gaps
decisions
repair state
```

The governing principle is:

> **Attention may determine which claim or uncertainty receives processing resources, but the RSCF determines what epistemic status that object is allowed to retain.**

Core boundary:

```text
ATTENTION PRIORITY
!=
CLAIM VALIDITY

RSCF REPRESENTATION
!=
PROOF

RSCF COMPLETENESS
!=
EMPIRICAL VALIDITY
```

---

# 1. Source / Canon References

## 1.1 Source-supported L02 semantic core

Recovered source basis:

```text
L02_ATTENTION
=
attention allocation;
budget scarce reasoning/observation resources
```

This supports:

```text
L02 concerns finite allocation.

L02 must discriminate among competing candidate targets.

L02 requires enough state to preserve why an allocation was made.
```

The source also explicitly requires:

```text
RSCF / GMEF links where applicable
dependencies and provenance
repair / rollback behavior
tests / falsifiers
governance / authority boundary
freshness / regime validity
supersession / version lineage
```

before promotion beyond placeholder state.

## 1.2 AMOS RSCF conventions

The RSCF representation uses these knowledge-node classes:

```text
SOURCE_CLAIM
OBSERVATION
DERIVED
MODEL
DECISION
UNKNOWN
```

Final conclusion classes remain:

```text
VERIFIED
DERIVED
MODEL
CONDITIONAL
COMPETING
UNKNOWN/GAP
```

These two type systems must not be silently collapsed.

For example:

```text
knowledge node class = MODEL
conclusion class = CONDITIONAL
```

is valid.

---

# 2. Definition

An RSCF is a recursive dependency structure:

[
R =
(V,E,A,P,F)
]

where:

```text
V = typed claim/evidence/state nodes
E = dependency and relation edges
A = applicability envelopes
P = provenance topology
F = falsifiers / invalidation conditions
```

For `L02_ATTENTION`, the RSCF constrains which attention candidate may receive resources and how conclusions derived during that processing may be reused.

A candidate claim node:

[
C_i =
T[
id,
text,
class,
premises,
evidence,
scope,
regime,
freshness,
causalLevel,
competing,
falsifiers,
confidence
]
]

---

# 3. Scope

This contract applies to RSCF objects involved in:

```text
attention admission
priority assessment
candidate comparison
resource allocation
focus
research/retrieval
hypothesis evaluation
contradiction handling
escalation
defer/resume
memory recall
repair
post-repair validation
stop decisions
```

It does not itself establish:

```text
empirical truth
causal proof
external authority
durable commit permission
canonical L02 implementation
```

---

# 4. Typed Inputs

```yaml
L02RSCFInput:

  target:
    type: ClaimRef | TaskRef | CandidateRef

  objective:
    type: GoalRef

  candidate_claims:
    type: ClaimNode[]

  observations:
    type: ObservationNode[]

  evidence:
    type: EvidenceNode[]

  dependencies:
    type: DependencyGraph

  provenance:
    type: ProvenanceGraph

  scope:
    type: ScopeEnvelope

  regime:
    type: RegimeRef

  freshness:
    type: FreshnessState

  hml:
    type: HMLContext

  constraints:
    type: ConstraintSet

  uncertainty:
    type: UncertaintyVector

  attention_budget:
    type: ResourceBudget

  authority:
    type: AuthorityContext
```

---

# 5. Typed Outputs

```yaml
L02RSCFOutput:

  rscf_id:
    type: RSCFId

  root_claim:
    type: ClaimNode

  conclusion_class:
    type:
      - VERIFIED
      - DERIVED
      - MODEL
      - CONDITIONAL
      - COMPETING
      - UNKNOWN_GAP

  hml_path:
    type: HMLPath

  load_bearing_premises:
    type: ClaimRef[]

  evidence_refs:
    type: EvidenceRef[]

  dependency_edges:
    type: DependencyEdge[]

  provenance:
    type: ProvenanceGraph

  scope:
    type: ScopeEnvelope

  regime:
    type: RegimeRef

  freshness:
    type: FreshnessState

  competing:
    type: CompetingHypothesis[]

  causal_status:
    type: CausalStatus

  falsifiers:
    type: Falsifier[]

  material_gaps:
    type: GapRef[]

  confidence_ceiling:
    type: ConfidenceBound

  cheapest_discriminating_test:
    type: TestProposal | null

  reuse_conditions:
    type: ReuseCondition[]

  attention_recommendation:
    type:
      - ATTEND
      - DEFER
      - ESCALATE
      - REVALIDATE
      - STOP
      - UNKNOWN
```

---

# 6. Core State Variables

```text
R_t        = current RSCF graph
C_t        = active claim nodes
E_t        = active evidence nodes
D_t        = dependency edges
P_t        = provenance topology
HML_t      = active H/M/L path
S_t        = scope envelope
Reg_t      = regime
Fr_t       = freshness state
Comp_t     = competing hypotheses
Contra_t   = contradiction set
Gap_t      = unresolved gaps
Fals_t     = falsifiers
Conf_t     = confidence ceilings
Att_t      = attention allocation
Auth_t     = authority state
Epoch_t    = validation/revalidation epoch
```

---

# 7. Claim Node Contract

```yaml
ClaimNode:

  claim_id: null

  text: null

  knowledge_class:
    type:
      - SOURCE_CLAIM
      - OBSERVATION
      - DERIVED
      - MODEL
      - DECISION
      - UNKNOWN

  conclusion_class:
    type:
      - VERIFIED
      - DERIVED
      - MODEL
      - CONDITIONAL
      - COMPETING
      - UNKNOWN_GAP

  premises: []

  evidence_refs: []

  scope: null
  regime: null
  freshness: null

  causal_level: null

  competing_set: []

  falsifiers: []

  sensitivity: []

  confidence_ceiling: 0

  consequence: null
```

Hard invariant:

```text
NO CLAIM MAY LOSE:

scope
premises
provenance
falsifiers
invalidation conditions

WHEN COMPRESSED.
```

---

# 8. Evidence Node Contract

```yaml
EvidenceNode:

  evidence_id: null

  source_id: null

  source_type: null

  observation_method: null

  timestamp: null

  version: null

  environment: null

  scope: null

  regime: null

  ancestry: []

  independence_group: null

  quality: null

  freshness: null

  revocation_state: null

  license: null

  supported_claims: []
```

Evidence-count invariant:

```text
MULTIPLE EVIDENCE REFERENCES
!=
MULTIPLE INDEPENDENT SOURCES
```

---

# 9. Relation Edge Contract

```yaml
RSCFEdge:

  source: null
  target: null

  relation_type:
    type:
      - premise
      - evidence
      - dependency
      - contradiction
      - competing
      - causal
      - enabling
      - confounding
      - temporal
      - scope
      - provenance
      - invalidation
      - repair
      - supersession

  direction: null
  confidence: null
  provenance: []
```

A semantic, temporal, or structural edge must never be silently promoted into a causal edge.

---

# 10. RSCF Operators

Candidate L02 RSCF operators:

```text
CREATE_RSCF()
REGISTER_CLAIM()
REGISTER_EVIDENCE()
TYPE_NODE()

LINK_PREMISE()
LINK_EVIDENCE()
LINK_DEPENDENCY()
LINK_PROVENANCE()

SET_SCOPE()
SET_REGIME()
SET_FRESHNESS()
SET_HML()

REGISTER_COMPETING()
REGISTER_CONTRADICTION()
REGISTER_FALSIFIER()

TRACE_DEPENDENCIES()
TRACE_ANCESTRY()

CHECK_SCOPE()
CHECK_REGIME()
CHECK_FRESHNESS()
CHECK_PROVENANCE_INDEPENDENCE()
CHECK_CAUSAL_LEVEL()

CALCULATE_CONFIDENCE_CEILING()

CLASSIFY_GAP()
SELECT_DISCRIMINATING_TEST()

PROMOTE_CLAIM()
DOWNGRADE_CLAIM()

INVALIDATE_NODE()
INVALIDATE_DESCENDANTS()

COMPRESS_RSCF()
REHYDRATE_RSCF()

REVALIDATE()
REPAIR_RSCF()
```

Operator names remain `AMOS_MODEL`.

---

# 11. RSCF Invariants

```text
L02-RSCF-INV-001
Every consequential conclusion has an identifiable root claim.

L02-RSCF-INV-002
Every load-bearing premise remains explicitly addressable.

L02-RSCF-INV-003
Derived claims retain links to their premises.

L02-RSCF-INV-004
Evidence retains provenance ancestry.

L02-RSCF-INV-005
Correlated sources cannot masquerade as independent support.

L02-RSCF-INV-006
Scope propagates through dependent claims.

L02-RSCF-INV-007
Regime propagates through dependent claims.

L02-RSCF-INV-008
Freshness requirements propagate through dependent claims.

L02-RSCF-INV-009
Confidence cannot exceed the weakest load-bearing premise unless independently revalidated.

L02-RSCF-INV-010
UNKNOWN/GAP cannot become PASS.

L02-RSCF-INV-011
MODEL cannot silently become VERIFIED.

L02-RSCF-INV-012
SOURCE_CLAIM cannot silently become OBSERVATION.

L02-RSCF-INV-013
Repeated descendants of one source do not create epistemic independence.

L02-RSCF-INV-014
Contradictions remain visible until resolved.

L02-RSCF-INV-015
Genuine competing hypotheses remain COMPETING until discriminated.

L02-RSCF-INV-016
Causal claim level cannot exceed causal evidence level.

L02-RSCF-INV-017
Structural similarity cannot establish causation.

L02-RSCF-INV-018
Attention allocation cannot strengthen claim class by itself.

L02-RSCF-INV-019
Compression cannot erase load-bearing premises.

L02-RSCF-INV-020
Compression cannot erase falsifiers.

L02-RSCF-INV-021
Invalidation propagates only through actual dependent descendants.

L02-RSCF-INV-022
Independent valid branches survive local invalidation.

L02-RSCF-INV-023
Repair cannot rewrite source evidence.

L02-RSCF-INV-024
Decision nodes remain distinguishable from evidence nodes.

L02-RSCF-INV-025
RSCF structure does not create action authority.
```

---

# 12. Dependency Semantics

A basic proof path:

```text
Evidence
   ↓
Premise
   ↓
Intermediate claim
   ↓
Root conclusion
```

Suppose:

[
C \leftarrow P_1,P_2,P_3
]

and:

[
P_2 \leftarrow E_4,E_5
]

Then the load-bearing closure for \(C\) includes (P_2,E_4,E_5) if failure of that branch can change \(C\).

L02 attention should preferentially inspect dependency nodes that can change the root decision.

It should not automatically load every ancestor.

---

# 13. Smallest Sufficient Proof Scope

The RSCF fast path is:

```text
ROOT CLAIM
↓
identify load-bearing premises
↓
inspect only dependencies capable of flipping result
↓
stop when sufficiency is established
```

Conceptually:

[
ProofScope^*
============

\arg\min_{S}
Cost(S)
]

subject to:

[
DecisionSufficiency(S)=true
]

and:

[
Integrity(S)=true
]

This is `AMOS_MODEL`.

It formalizes the principle:

```text
SMALLEST SUFFICIENT PROOF SCOPE
!=
SMALLEST POSSIBLE CONTEXT
```

---

# 14. H/M/L Mapping

## H — Governing RSCF

Represents:

```text
mission-level claim
system objective
governing constraint
macro decision
systemic risk
```

Example:

```text
H CLAIM:
"This deployment is eligible to proceed."
```

## M — Subsystem RSCFs

Represent:

```text
safety
authority
performance
provenance
risk
resource adequacy
```

## L — Local RSCFs

Represent:

```text
one observation
one test result
one source
one dependency
one variable
one failure
```

Recursive form:

[
R_H
\rightarrow
{R_{M1},R_{M2},...}
\rightarrow
{R_{L1},R_{L2},...}
]

Only decision-relevant branches need expansion.

---

# 15. H/M/L Confidence Propagation

For H claim \(C_H\) depending on M claims:

[
Conf(C_H)
\le
\min_j Conf(C_{M_j})
]

for load-bearing \(M_j\).

For M claim depending on L claims:

[
Conf(C_M)
\le
\min_k Conf(C_{L_k})
]

for load-bearing \(L_k\).

Aggregation itself cannot increase confidence.

Independent new evidence may change the underlying graph and therefore the ceiling.

---

# 16. Competing Hypotheses

RSCF must preserve incompatible candidate explanations.

Example:

```yaml
competing:

  - id: H1
    claim: allocation failure
    support: []

  - id: H2
    claim: upstream observation failure
    support: []

  - id: H3
    claim: stale objective
    support: []
```

State remains:

```text
COMPETING
```

when support is:

```text
equal
incomparable
correlated
insufficient
```

Preferred next action:

```text
find the cheapest high-information discriminating test
```

not:

```text
collect more redundant confirmation
```

---

# 17. Contradiction Handling

Contradiction:

[
C_i
\land
\neg C_i
]

or materially incompatible claims under the same applicability envelope must remain explicit.

Candidate state:

```yaml
ContradictionRecord:

  contradiction_id: null

  claims: []

  shared_scope: null
  shared_regime: null

  provenance_sets: []

  resolution_state:
    type:
      - OPEN
      - PARTIAL
      - RESOLVED
      - NON_COMPARABLE
```

Do not resolve a contradiction merely by:

```text
majority count
authority
repetition
recency alone
fluency
```

---

# 18. Causal Firewall

RSCF causal levels should distinguish:

```text
association
correlation
enabling condition
necessary condition
sufficient condition
mediator
confounder
feedback
mechanism
intervention effect
```

An L02 candidate may be highly important without being causally important.

Therefore:

```text
ATTENTION IMPORTANCE
!=
CAUSAL IMPORTANCE
```

and:

```text
STRUCTURAL SIMILARITY
!=
CAUSAL MECHANISM
```

---

# 19. Scope / Regime Firewall

Every load-bearing claim should inherit an applicability envelope.

```yaml
ApplicabilityEnvelope:

  system: null
  population: null
  environment: null
  scale: null
  time: null
  regime: null
  measurement_method: null
  assumptions: []
```

Claim transfer:

[
C_{scope=A}
\not\Rightarrow
C_{scope=B}
]

without transfer evidence.

Regime shift:

[
R_a \rightarrow R_b
]

requires revalidation where regime is load-bearing.

---

# 20. Freshness

Each mutable claim/evidence node should declare freshness conditions.

```yaml
FreshnessContract:

  created_at: null
  observed_at: null
  validated_at: null

  valid_until: null

  invalidate_on:
    - source_update
    - environment_change
    - regime_shift
    - authority_change
    - dependency_change
    - explicit_revocation
```

Hard boundary:

```text
RETRIEVED
!=
FRESH
```

and:

```text
PREVIOUSLY VALID
!=
CURRENTLY VALID
```

---

# 21. Provenance Topology

RSCF should represent semantic ancestry, not merely document count.

Example:

```text
Source A
├── Summary A1
│   └── RSCF A1
├── Translation A2
└── Agent Report A3
```

These may constitute one provenance family.

Therefore:

[
IndependentCount
\le
ArtifactCount
]

Independence must be established, not presumed.

---

# 22. Confidence Ceiling

For claim \(C\):

[
Conf(C)
\le
\min_{p \in LoadBearing(C)}
Conf(p)
]

unless independent validation supplies a stronger proof path.

The confidence ceiling should also consider material unresolved:

```text
scope uncertainty
regime uncertainty
freshness uncertainty
causal uncertainty
execution uncertainty
provenance independence uncertainty
```

Attention allocation does not change the ceiling unless it actually obtains new evidence or removes uncertainty.

---

# 23. Sensitivity

For consequential claim \(C\), identify the smallest premise/threshold capable of flipping its conclusion.

Candidate:

```yaml
SensitivityRecord:

  claim_id: null

  flip_variables: []

  fragile_premises: []

  thresholds: []

  direction_of_change: null

  tested: false
```

Attention priority should favor high-impact sensitivity points before low-value background detail.

---

# 24. Gap Classification

Every material RSCF gap should be classified:

```text
CRITICAL
DECISION-RELEVANT
EXPLANATORY
COSMETIC
```

Priority:

```text
CRITICAL
>
DECISION-RELEVANT
>
EXPLANATORY
>
COSMETIC
```

Examples:

```text
missing authority witness
→ CRITICAL

unknown current resource budget
→ DECISION-RELEVANT or CRITICAL

missing explanation for a non-load-bearing field
→ EXPLANATORY

formatting inconsistency
→ COSMETIC
```

---

# 25. Attention Allocation From RSCF

RSCF can provide attention candidates:

[
Candidates =
CriticalGaps
\cup
FragilePremises
\cup
Contradictions
\cup
CompetingDiscriminators
\cup
StaleLoadBearingNodes
]

Candidate priority model:

[
Priority(x)
===========

F(
DecisionImpact,
UncertaintyReduction,
DependencyCriticality,
Consequence,
Freshness,
Cost
)
]

No canonical weighting is asserted.

---

# 26. RSCF Attention Loop

```text
ROOT OBJECTIVE
↓
BUILD MINIMUM RSCF
↓
IDENTIFY LOAD-BEARING PREMISES
↓
IDENTIFY GAPS / CONTRADICTIONS / COMPETING
↓
ALLOCATE ATTENTION
↓
ACQUIRE / REVALIDATE EVIDENCE
↓
UPDATE RSCF
↓
RECALCULATE CONFIDENCE
↓
REASSESS GAPS
↓
STOP / CONTINUE / ESCALATE
```

This creates a closed reasoning-allocation loop without treating model-generated structure as evidence.

---

# 27. Stop Conditions

Candidate stop conditions:

```text
CLAIM_SUFFICIENT
DECISION_SUFFICIENT
ACTION_SUFFICIENT
```

For an explanatory task:

```text
DECISION_SUFFICIENT = NOT_APPLICABLE
ACTION_SUFFICIENT = NOT_APPLICABLE
```

Stop is allowed when remaining gaps cannot materially alter the requested outcome.

Hard boundary:

```text
STOP
!=
UNIVERSAL CERTAINTY
```

---

# 28. Control-Plane Requirements

L02/RSCF reasoning may propose:

```text
claim status
attention allocation
gap priority
repair
escalation
rollback
decision recommendation
```

It does not gain commit authority.

Control-plane validation should govern, where applicable:

```text
authority witness
constraint freshness
durable state
shared state mutation
external tool effect
memory admission
cross-recipient disclosure
irreversible action
commit finalization
```

Boundary:

```text
RSCF SAYS "SUPPORTED"
!=
ACTION AUTHORIZED
```

---

# 29. Agents

Candidate RSCF roles:

```text
L02_RSCF_COORDINATOR
L02_CLAIM_TYPER
L02_DEPENDENCY_MAPPER
L02_EVIDENCE_AUDITOR
L02_PROVENANCE_AUDITOR
L02_COMPETING_HYPOTHESIS_AGENT
L02_CAUSAL_FIREWALL_AGENT
L02_GAP_AUDITOR
L02_CONFIDENCE_AUDITOR
L02_RSCF_REPAIR_AGENT
```

These are architectural roles.

Different agents do not automatically constitute independent epistemic sources.

---

# 30. Skills

Potential supporting capabilities:

```text
RSCF Modeler
AMOS Claim Verifier
AMOS Attention Allocation Governor
AMOS Provenance Trust Firewall
AMOS Metacognitive Confidence Auditor
AMOS Constraint Propagation RSCF Engine
AMOS Cross-Scale RSCF Tensor Engine
AMOS Context State Maintenance RSCF
AMOS Repair Harm Auditor
AMOS Infrastructure Control Plane
```

Skill invocation produces candidate evidence/analysis.

It does not automatically validate the RSCF node.

---

# 31. Workflow

```text
NORMALIZE TARGET
↓
SET SCOPE / REGIME / FRESHNESS
↓
BUILD H/M/L MAP
↓
REGISTER ROOT CLAIM
↓
TYPE CLAIM NODES
↓
ATTACH PREMISES
↓
ATTACH EVIDENCE
↓
RESOLVE PROVENANCE ANCESTRY
↓
MAP DEPENDENCIES
↓
REGISTER COMPETING
↓
REGISTER CONTRADICTIONS
↓
APPLY CAUSAL FIREWALL
↓
ATTACH FALSIFIERS
↓
CLASSIFY GAPS
↓
CALCULATE CONFIDENCE CEILING
↓
IDENTIFY SENSITIVE PREMISE
↓
ALLOCATE ATTENTION
↓
RETRIEVE / TEST / REVALIDATE
↓
UPDATE GRAPH
↓
ISSUE WEAKEST ACCURATE CONCLUSION CLASS
```

---

# 32. Protocols

Candidate RSCF protocol family:

```text
RSCF_CREATE
RSCF_NODE_REGISTER
RSCF_EDGE_REGISTER
RSCF_EVIDENCE_ATTACH
RSCF_PROVENANCE_ATTACH
RSCF_SCOPE_UPDATE
RSCF_REGIME_UPDATE
RSCF_FRESHNESS_UPDATE
RSCF_COMPETING_REGISTER
RSCF_CONTRADICTION_REGISTER
RSCF_FALSIFIER_REGISTER
RSCF_GAP_REGISTER
RSCF_CONFIDENCE_UPDATE
RSCF_INVALIDATION_NOTICE
RSCF_REVALIDATION_REQUEST
RSCF_REPAIR_REQUEST
RSCF_COMPRESSION_REQUEST
RSCF_REHYDRATION_REQUEST
```

Canonical protocol names remain `UNKNOWN/GAP`.

---

# 33. Evidence / Provenance Requirements

Every important conclusion should retain at least:

```text
claim
claim type
premises
evidence refs
semantic origins
ancestry groups
scope
regime
freshness
H/M/L location
causal level
competing hypotheses
falsifiers
confidence ceiling
material gaps
```

If raw evidence is externalized, retain a recovery pointer.

```text
COMPRESSED RSCF
must remain
REHYDRATABLE
```

for load-bearing evidence.

---

# 34. Compression Contract

RSCF compression may remove:

```text
redundant prose
non-load-bearing repetition
already-resolved cosmetic detail
```

It may not remove:

```text
root claim
load-bearing premises
source identity
scope
regime
freshness
contradictions
COMPETING state
falsifiers
confidence ceiling
critical gaps
recovery pointers
```

Hard invariant:

```text
COMPRESSION
!=
EPISTEMIC DELETION
```

---

# 35. Reuse Contract

An RSCF may be reused only when:

```text
dependencies remain valid
scope matches
regime matches
freshness remains valid
provenance remains admissible
no superseding contradiction exists
```

Candidate:

[
Reusable(R)
===========

DepsValid
\land
ScopeMatch
\land
RegimeMatch
\land
Fresh
\land
NoBlockingConflict
]

If one load-bearing condition fails:

```text
invalidate only dependent descendants
```

rather than discarding unrelated RSCFs.

---

# 36. Failure Modes

```text
FM-L02-RSCF-001   Missing Root Claim
FM-L02-RSCF-002   Untyped Claim
FM-L02-RSCF-003   Hidden Premise
FM-L02-RSCF-004   Missing Evidence
FM-L02-RSCF-005   Missing Provenance
FM-L02-RSCF-006   False Source Independence
FM-L02-RSCF-007   Scope Leakage
FM-L02-RSCF-008   Regime Leakage
FM-L02-RSCF-009   Freshness Loss
FM-L02-RSCF-010   Confidence Inflation
FM-L02-RSCF-011   Causal Overreach
FM-L02-RSCF-012   Contradiction Suppression
FM-L02-RSCF-013   COMPETING Collapse
FM-L02-RSCF-014   Missing Falsifier
FM-L02-RSCF-015   Missing Gap Classification
FM-L02-RSCF-016   H/M/L Collapse
FM-L02-RSCF-017   Premature Claim Promotion
FM-L02-RSCF-018   Global Invalidation
FM-L02-RSCF-019   Under-Invalidation
FM-L02-RSCF-020   Destructive Compression
FM-L02-RSCF-021   Stale RSCF Reuse
FM-L02-RSCF-022   Decision Node Treated as Evidence
FM-L02-RSCF-023   Attention Priority Treated as Proof
FM-L02-RSCF-024   Model RSCF Reported as Canon
```

---

# 37. Repair / Recovery

RSCF repair sequence:

```text
DETECT STRUCTURAL FAILURE
↓
IDENTIFY EARLIEST INVALID NODE / EDGE
↓
TRACE DESCENDANTS
↓
FREEZE AFFECTED CLAIMS
↓
PRESERVE INDEPENDENT VALID BRANCHES
↓
RESTORE MISSING TYPE / PREMISE / PROVENANCE
↓
RECHECK SCOPE / REGIME / FRESHNESS
↓
RESTORE CONTRADICTIONS / COMPETING
↓
RECOMPUTE CONFIDENCE
↓
REVALIDATE DESCENDANTS
↓
REISSUE CONCLUSION CLASS
```

Repair must not rewrite source evidence merely to restore graph consistency.

---

# 38. Tests / Validators

Required validators:

```text
VALIDATE_RSCF_SCHEMA
VALIDATE_ROOT_CLAIM
VALIDATE_NODE_TYPES
VALIDATE_PREMISES
VALIDATE_EVIDENCE
VALIDATE_PROVENANCE
VALIDATE_PROVENANCE_INDEPENDENCE
VALIDATE_DEPENDENCY_GRAPH
VALIDATE_SCOPE
VALIDATE_REGIME
VALIDATE_FRESHNESS
VALIDATE_HML
VALIDATE_CAUSAL_LEVEL
VALIDATE_COMPETING
VALIDATE_CONTRADICTIONS
VALIDATE_FALSIFIERS
VALIDATE_GAP_CLASSES
VALIDATE_CONFIDENCE_CEILING
VALIDATE_COMPRESSION
VALIDATE_REUSE
VALIDATE_INVALIDATION
```

Minimum tests:

```text
TEST-L02-RSCF-001
Remove a load-bearing premise.
Expected:
dependent conclusion becomes invalid/UNKNOWN.

TEST-L02-RSCF-002
Supply three summaries from one source.
Expected:
one provenance family, not three independent confirmations.

TEST-L02-RSCF-003
Apply a claim outside original scope.
Expected:
scope violation.

TEST-L02-RSCF-004
Reuse claim after regime change.
Expected:
revalidation.

TEST-L02-RSCF-005
Delete contradiction during compression.
Expected:
FAIL.

TEST-L02-RSCF-006
Merge equal hypotheses.
Expected:
FAIL; preserve COMPETING.

TEST-L02-RSCF-007
Set confidence above weakest load-bearing premise.
Expected:
FAIL.

TEST-L02-RSCF-008
Promote MODEL to VERIFIED without new evidence.
Expected:
FAIL.

TEST-L02-RSCF-009
Invalidate one independent branch.
Expected:
unrelated branches survive.

TEST-L02-RSCF-010
Use high attention priority as evidence.
Expected:
FAIL.

TEST-L02-RSCF-011
Remove all falsifiers.
Expected:
validator warning/failure for consequential claim.

TEST-L02-RSCF-012
Compress RSCF and rehydrate.
Expected:
load-bearing graph reconstructable.

TEST-L02-RSCF-013
Use stale evidence.
Expected:
freshness failure.

TEST-L02-RSCF-014
Report unexecuted validator as passed.
Expected:
FAIL.

TEST-L02-RSCF-015
Report model RSCF as canonical L02 implementation.
Expected:
FAIL.
```

---

# 39. Falsifiers

This artifact should be revised if direct canon establishes that:

```text
L02 does not use RSCF.

RSCF knowledge classes differ materially.

H/M/L semantics differ materially.

confidence-ceiling semantics differ.

dependency invalidation differs.

provenance independence is handled elsewhere.

L02 has no role in RSCF attention allocation.

canonical source provides incompatible RSCF schema.

runtime evidence falsifies modeled reuse/repair behavior.
```

---

# 40. Gap Matrix

```yaml
gap_status:

  L02_attention_role:
    status: SOURCE_SUPPORTED

  scarce_resource_role:
    status: SOURCE_SUPPORTED

  RSCF_link_requirement:
    status: SOURCE_SUPPORTED

  RSCF_definition:
    status: AMOS_FRAMEWORK_SUPPORTED

  claim_node_contract:
    status: MODEL_DEFINED

  evidence_node_contract:
    status: MODEL_DEFINED

  relation_contract:
    status: MODEL_DEFINED

  HML_mapping:
    status: MODEL_DEFINED

  provenance_topology:
    status: MODEL_DEFINED / FRAMEWORK_ALIGNED

  competing_hypotheses:
    status: FRAMEWORK_SUPPORTED

  causal_firewall:
    status: FRAMEWORK_SUPPORTED

  confidence_ceiling:
    status: FRAMEWORK_SUPPORTED

  selective_invalidation:
    status: FRAMEWORK_SUPPORTED

  compression_contract:
    status: MODEL_DEFINED

  reuse_contract:
    status: MODEL_DEFINED

  canonical_L02_RSCF_schema:
    status: UNKNOWN_GAP

  canonical_RSCF_operator_names:
    status: UNKNOWN_GAP

  canonical_RSCF_protocols:
    status: UNKNOWN_GAP

  canonical_attention_RSCF_binding:
    status: UNKNOWN_GAP

  runtime_implementation:
    status: UNKNOWN_GAP

  executed_validation:
    status: UNKNOWN_GAP
```

---

# 41. Critical Gaps

```text
CRITICAL GAP 1:
Exact canonical relationship between L02 and RSCF.

CRITICAL GAP 2:
Canonical L02 RSCF schema.

CRITICAL GAP 3:
Canonical runtime binding between attention allocation and claim graph.

CRITICAL GAP 4:
Executable validation that selective invalidation, confidence ceilings,
provenance preservation, and COMPETING state are enforced.
```

---

# 42. Cheapest Discriminating Evidence

Highest-value evidence sequence:

```text
1. Direct canonical L02 RSCF source.

2. Direct AMOS canonical RSCF specification.

3. L02 operator/state contracts.

4. Full Brain OS cognitive routing contract.

5. AMOS_CORE v4.4 implementation.

6. Runtime traces showing RSCF creation/update.

7. Tests demonstrating:
   confidence ceilings,
   selective invalidation,
   provenance independence,
   contradiction retention,
   COMPETING preservation.
```

Primary question:

> **Is RSCF an intrinsic L02 state representation, a shared AMOS reasoning substrate consumed by L02, or a control-plane structure outside the primitive?**

Preserve these as `COMPETING` until direct evidence resolves them.

---

# 43. Competing Architecture Models

## COMPETING-001 — L02 Owns RSCF

```text
L02
creates
updates
stores
RSCFs
```

## COMPETING-002 — Shared RSCF Substrate

```text
Shared AMOS RSCF layer
↕
L02_ATTENTION
```

L02 reads RSCF structure to allocate resources but does not own the graph.

## COMPETING-003 — Control-Plane RSCF

```text
Infrastructure Control Plane
owns RSCF

L02 receives bounded views
```

## COMPETING-004 — Hybrid

```text
L02 owns local ephemeral RSCF state.

Shared infrastructure owns durable provenance,
cross-agent state, and commit-sensitive graph updates.
```

Current architectural preference:

```text
COMPETING-004
```

as a MODEL only.

---

# 44. Canonical RSCF Capsule Template

```yaml
rscf:

  id: L02_ATTENTION_<KEY>

  target:
    claim: null
    object: null

  conclusion_class:
    value: UNKNOWN_GAP

  knowledge_class:
    value: UNKNOWN

  hml:
    H: null
    M: null
    L: null

  premises: []

  evidence: []

  provenance:
    sources: []
    ancestry: []
    independence_groups: []

  dependencies: []

  scope: null

  regime: null

  freshness: null

  causal_status: null

  competing: []

  contradictions: []

  falsifiers: []

  sensitivity: []

  uncertainty:
    evidence: null
    model: null
    scope: null
    temporal: null
    causal: null
    execution: null
    provenance_independence: null

  confidence_ceiling: 0

  gaps:
    critical: []
    decision_relevant: []
    explanatory: []
    cosmetic: []

  cheapest_discriminating_test: null

  attention:
    recommendation: UNKNOWN
    priority: null
    budget: null

  reuse:
    allowed: false
    conditions: []

  invalidation_conditions: []
```

---

# 45. L02 Master RSCF

```yaml
rscf:

  id: L02_ATTENTION_MASTER

  target:
    claim:
      L02_ATTENTION is the AMOS cognitive primitive concerned with
      allocating scarce reasoning/observation resources among competing
      targets.

  knowledge_class: SOURCE_CLAIM

  conclusion_class: CONDITIONAL

  hml:
    H:
      governing finite-resource cognition

    M:
      attention allocation subsystem

    L:
      individual candidate selection and processing

  load_bearing_premises:

    - id: P1
      claim:
        L02 concerns attention allocation.
      class: SOURCE_CLAIM

    - id: P2
      claim:
        reasoning/observation resources are scarce.
      class: SOURCE_CLAIM

    - id: P3
      claim:
        detailed RSCF integration beyond the placeholder remains unresolved.
      class: DERIVED

  evidence:
    - L02_ATTENTION/PLACEHOLDER.md

  provenance:
    origin_architect: Trang Phan
    architecture_family: AMOS
    subsystem: COGNITIVE_MATRIX
    primitive: L02_ATTENTION
    derivation:
      source primitive + bounded AMOS RSCF integration model

  scope:
    system: AMOS_OS
    subsystem: COGNITIVE_MATRIX
    primitive: L02_ATTENTION

  regime:
    governed finite-resource cognitive reasoning

  freshness:
    revalidate_when:
      - direct L02 RSCF canon is recovered
      - AMOS RSCF semantics change
      - L02 architecture changes
      - runtime implementation becomes available
      - new validation evidence appears

  dependencies:
    - L01_SENSING_OBSERVATION
    - L02_ATTENTION_PURPOSE
    - L02_ATTENTION_DEFINITION
    - L02_ATTENTION_VARIABLES
    - L02_ATTENTION_STATE
    - L02_ATTENTION_OPERATORS
    - L02_ATTENTION_INVARIANTS
    - L02_ATTENTION_DEPENDENCIES
    - L02_ATTENTION_EQUATIONS
    - L02_ATTENTION_HML
    - L02_ATTENTION_MEMORY
    - L02_ATTENTION_CONTROL_PLANES
    - L02_ATTENTION_PROTOCOLS
    - L02_ATTENTION_PROVENANCE
    - L02_ATTENTION_FAILURE_MODES
    - L02_ATTENTION_REPAIR
    - L02_ATTENTION_TESTS

  competing:

    - id: C1
      hypothesis:
        L02 owns local RSCF state.

    - id: C2
      hypothesis:
        RSCF is shared AMOS reasoning infrastructure.

    - id: C3
      hypothesis:
        infrastructure control plane owns durable RSCF state.

    - id: C4
      hypothesis:
        hybrid local/shared ownership applies.

  causal_status:
    value:
      structural / governance model only

  falsifiers:
    - direct canon assigning incompatible RSCF semantics
    - direct canon showing L02 does not interact with RSCF
    - executable runtime contradicting modeled ownership
    - tests falsifying modeled confidence/invalidation semantics

  uncertainty:
    evidence: MEDIUM_HIGH
    model: MEDIUM
    scope: MEDIUM
    temporal: MEDIUM
    causal: LOW
    execution: HIGH
    provenance_independence: MEDIUM

  confidence_ceiling:
    source-backed confidence applies to the attention-allocation and
    scarcity claims only; detailed RSCF integration remains MODEL.

  gaps:

    critical:
      - canonical L02-RSCF ownership
      - canonical schema
      - runtime implementation
      - executed validation

    decision_relevant:
      - canonical operator bindings
      - canonical protocol bindings
      - RSCF persistence ownership

    explanatory:
      - exact RSCF naming
      - internal identifiers

    cosmetic: []

  cheapest_discriminating_test:
    recover direct canonical RSCF material for L02 and compare ownership,
    schema, confidence, invalidation, provenance, and H/M/L semantics.

  attention:
    recommendation: REVALIDATE
    reason:
      critical canonical and runtime gaps remain open

  reuse:
    allowed: true
    conditions:
      - treat detailed integration as MODEL
      - preserve source/canon boundary
      - revalidate when stronger canon is recovered
      - do not infer runtime implementation
```

---

# 46. Completion State

```yaml
completion_state:

  source_canon_references:
    status: PARTIAL_SOURCE_BOUND

  definition_scope:
    status: MODEL_COMPLETE

  typed_inputs_outputs:
    status: MODEL_COMPLETE

  state_variables:
    status: MODEL_COMPLETE

  operators:
    status: MODEL_COMPLETE

  invariants:
    status: MODEL_COMPLETE

  dependencies:
    status: MODEL_COMPLETE_WITH_GAPS

  HML_applicability:
    status: MODEL_COMPLETE

  control_plane_requirements:
    status: MODEL_COMPLETE

  agents:
    status: MODEL_COMPLETE

  skills:
    status: MODEL_COMPLETE

  workflows:
    status: MODEL_COMPLETE

  protocols:
    status: MODEL_COMPLETE

  evidence_provenance:
    status: MODEL_COMPLETE_SOURCE_PARTIAL

  uncertainty_confidence:
    status: MODEL_COMPLETE

  failure_modes:
    status: MODEL_COMPLETE

  repair_recovery:
    status: MODEL_COMPLETE

  tests_validators:
    status: MODEL_COMPLETE_UNEXECUTED

  falsifiers:
    status: MODEL_COMPLETE

  gap_status:
    status: EXPLICIT_CRITICAL_GAPS_OPEN

  canonical_RSCF_schema:
    status: UNKNOWN_GAP

  runtime_implementation:
    status: UNKNOWN_GAP

  executed_validation:
    status: UNKNOWN_GAP

  overall:
    status: COMPLETE_FOR_RSCF_MODEL_SPECIFICATION_SCOPE

  conclusion_class:
    MODEL
```

---

# 47. Hard Boundaries

```text
PLACEHOLDER != IMPLEMENTED

ADDRESSABLE != VALIDATED

CAPABILITY != AUTHORITY

PROPOSAL != COMMIT

UNKNOWN/GAP != PASS
```

RSCF-specific extensions:

```text
RSCF != PROOF

RSCF NODE != TRUTH

SOURCE_CLAIM != OBSERVATION

DERIVED != VERIFIED

MODEL != CANON

DECISION != EVIDENCE

ATTENTION PRIORITY != CONFIDENCE

ATTENTION PRIORITY != VALIDITY

MULTIPLE SOURCES != INDEPENDENT SOURCES

SHARED ANCESTRY != INDEPENDENT CONFIRMATION

CORRELATION != CAUSATION

STRUCTURAL SIMILARITY != CAUSAL MECHANISM

LOCAL VALIDITY != GLOBAL VALIDITY

H COMPLETION != L VALIDATION

COMPRESSION != PERMISSION TO DROP PREMISES

NO CONTRADICTION FOUND != PROOF

TEST DEFINED != TEST EXECUTED

RSCF REPAIRED != RUNTIME VALIDATED
```

---

# 48. References

```text
L02_ATTENTION — Readme
L02_ATTENTION_PRIMITIVES_COGNITIVE_MATRIX_README
L02_ATTENTION_PRIMITIVES_COGNITIVE_MATRIX_README
L02_ATTENTION_PRIMITIVES_COGNITIVE_MATRIX_README
L02_ATTENTION_PRIMITIVES_COGNITIVE_MATRIX_README
L02_ATTENTION_PRIMITIVES_COGNITIVE_MATRIX_README
L02_ATTENTION_PRIMITIVES_COGNITIVE_MATRIX_README
L02_ATTENTION_PRIMITIVES_COGNITIVE_MATRIX_README
L02_ATTENTION_PRIMITIVES_COGNITIVE_MATRIX_README
L02_ATTENTION_PRIMITIVES_COGNITIVE_MATRIX_README
L02_ATTENTION_PRIMITIVES_COGNITIVE_MATRIX_README
L02_ATTENTION_PRIMITIVES_COGNITIVE_MATRIX_README
L02_ATTENTION_PRIMITIVES_COGNITIVE_MATRIX_README
L02_ATTENTION_PRIMITIVES_COGNITIVE_MATRIX_README
L02_ATTENTION_PRIMITIVES_COGNITIVE_MATRIX_README
L02_ATTENTION_PRIMITIVES_COGNITIVE_MATRIX_README
L02_ATTENTION_PRIMITIVES_COGNITIVE_MATRIX_README
L02_ATTENTION_PRIMITIVES_COGNITIVE_MATRIX_README
L02_ATTENTION_PRIMITIVES_COGNITIVE_MATRIX_README
L02_ATTENTION_PRIMITIVES_COGNITIVE_MATRIX_README
L02_ATTENTION_PRIMITIVES_COGNITIVE_MATRIX_README

L01_SENSING_OBSERVATION

RSCF Modeler
Cosmo_Brain_BRIDGE_INDEX
Cosmo_Brain_BRIDGE_INDEX
Cosmo_Brain_BRIDGE_INDEX
Cosmo_Brain_BRIDGE_INDEX
Cosmo_Brain_BRIDGE_INDEX
Cosmo_Brain_BRIDGE_INDEX
Cosmo_Brain_BRIDGE_INDEX
Cosmo_Brain_BRIDGE_INDEX
Cosmo_Brain_BRIDGE_INDEX
```

---

# 49. Governing RSCF Contract

> **`L02_ATTENTION` uses RSCF-compatible reasoning to allocate scarce processing resources without confusing attention with epistemic promotion. Every consequential attended claim must retain its premises, evidence, provenance, dependency structure, scope, regime, freshness, H/M/L coordinate, competing hypotheses, contradictions, falsifiers, sensitivity, and confidence ceiling. Attention should preferentially target load-bearing uncertainty, critical gaps, fragile premises, stale state, and discriminating evidence. RSCF compression may reduce redundancy but may not erase decision-relevant structure. Failed premises invalidate only dependent descendants, and no RSCF result creates authority or durable commit permission by itself.**

---

# 50. Canon Boundary

```text
SOURCE-SUPPORTED:

L02_ATTENTION concerns attention allocation.

It budgets scarce reasoning/observation resources.

The L02 placeholder explicitly requires RSCF/GMEF linkage,
provenance, repair, tests, governance, freshness,
and version-lineage treatment before promotion.


AMOS-RSCF-FRAMEWORK-SUPPORTED:

typed knowledge nodes

H/M/L decomposition

load-bearing premises

dependency graphs

provenance ancestry

scope/regime/freshness boundaries

competing hypotheses

causal firewall

falsifiers

gap classification

confidence ceilings

selective invalidation


AMOS_MODEL:

detailed L02 RSCF schema

attention-RSCF loop

node/edge types

compression contract

reuse contract

priority mapping

sensitivity mapping

agent roles

skill mappings

protocol family

master RSCF capsule


UNKNOWN/GAP:

canonical L02 RSCF ownership

canonical L02 RSCF schema

canonical operator bindings

canonical protocol bindings

canonical persistence ownership

canonical RSCF thresholds

runtime implementation

executed validation

formal verification
```

Therefore:

```text
CONCLUSION CLASS:
MODEL

NOT:
VERIFIED COMPLETE L02 RSCF CANON

NOT:
PROOF OF IMPLEMENTATION

NOT:
PROOF OF RUNTIME ENFORCEMENT

NOT:
PROOF THAT AN RSCF CLAIM IS TRUE

NOT:
AUTHORIZATION TO COMMIT
```

```text
```

---

[[00_ROOT_MOC]]|[[AMOS MOC]]

---
**Related:** [[00_HOME]] · [[COGNITIVE_MATRIX_MOC]] · [[AMOS_RSCF_NODES]]

---
RSCF-NODE
node_id: l02_attention_primitives_cognitive_matrix_rscf
node_type: note
path: 25_COGNITIVE_MATRIX/01_PRIMITIVES/L02_ATTENTION/L02_ATTENTION_PRIMITIVES_COGNITIVE_MATRIX_RSCF.md
RSCF-RELATIONS:
  - INDEXED_BY: [[00_HOME]]
  - INDEXED_BY: [[AMOS_RSCF_NODES]]
claim_class: AMOS_MODEL

---
**MOC:** [[L02_ATTENTION_MOC]]
