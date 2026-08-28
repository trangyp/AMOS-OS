---
type: note
source: 01_CANON/01_CORE_LAWS
tags:
- canon
- core_laws
- causal
- causality
- dependency
- provenance
- rscf
- governance
- canon/universe
title: L4 Causal Laws
origin_architect: Trang Phan
status: AMOS_MODEL
canon_status: PROPOSED_CANON_CONTENT
epistemic_class: AMOS_MODEL
rscf:
  state: SOURCE_CLAIM
  claim_class: SOURCE_CLAIM
  provenance: AMOS_corpus
  scope: core_laws
---


# L4 Causal Laws

**Origin architect / steward:** Trang Phan
**Layer:** `01_CANON / 01_CORE_LAWS / L4_CAUSAL`
**Artifact class:** `CORE_LAW_CONTRACT`
**Status:** `AMOS_MODEL — requires canon approval / provenance validation`

> L4 governs what AMOS is permitted to claim, infer, preserve, invalidate, or act upon as a causal relationship.
>
> A dependency, sequence, correlation, similarity, prediction, or explanation does not become causal merely because it is coherent.

---

## 1. Purpose

`L4_CAUSAL` establishes the causal-integrity laws of AMOS.

Its purpose is to prevent AMOS from silently promoting:

- association into causation;
- temporal ordering into causation;
- dependency into causation;
- prediction into mechanism;
- structural similarity into causal equivalence;
- intervention proposals into proven intervention effects;
- local causal relationships into universal ones;
- cross-scale mappings into causal laws;
- model-generated explanations into observed mechanisms.

L4 therefore acts as the firewall between:

```text
WHAT VARIES TOGETHER
        ↓
WHAT DEPENDS ON WHAT
        ↓
WHAT MAY EXPLAIN WHAT
        ↓
WHAT CAUSES WHAT
        ↓
WHAT AN INTERVENTION MAY CHANGE
```

Each transition requires additional evidence.

No transition is automatic.

---

# 2. Core Causal Law

The root L4 law is:

```text
CAUSAL_CLAIM
REQUIRES
CAUSALLY_TYPED_EVIDENCE
```

Formally, as an AMOS model constraint:

```text
Cause(A → B) cannot be promoted
unless evidence E supports the required causal relation
within scope S,
regime R,
time T,
observer/measurement context O,
and provenance topology P.
```

Therefore:

```text
DEPENDENCY != CAUSATION
CORRELATION != CAUSATION
SEQUENCE != CAUSATION
PREDICTION != CAUSATION
SIMILARITY != CAUSATION
COHERENCE != CAUSATION
MECHANISM_PROPOSAL != MECHANISM_VERIFICATION
INTERVENTION_PROPOSAL != INTERVENTION_EFFECT
```

---

# 3. Causal Relation Types

AMOS MUST type causal statements rather than storing every causal-looking relationship as a generic `CAUSES` edge.

Minimum causal vocabulary:

```yaml
causal_relation_types:

  ASSOCIATION:
    meaning: variables or states exhibit a relationship
    causal_strength: none_implied

  CORRELATION:
    meaning: measurable statistical co-variation
    causal_strength: none_implied

  TEMPORAL_PRECEDENCE:
    meaning: A occurs before B
    causal_strength: necessary_for_some_causal_claims_but_not_sufficient

  DEPENDENCY:
    meaning: B structurally/logically/computationally depends on A
    causal_strength: not_automatically_causal

  ENABLING_CONDITION:
    meaning: A permits or enables B without necessarily producing B

  CONTRIBUTORY_CAUSE:
    meaning: A contributes to probability or magnitude of B

  NECESSARY_CONDITION:
    meaning: B cannot occur under the declared model without A

  SUFFICIENT_CONDITION:
    meaning: A is sufficient for B under declared conditions

  MEDIATOR:
    meaning: A transmits part or all of an effect between variables

  CONFOUNDER:
    meaning: A influences variables whose relationship is being evaluated

  MODERATOR:
    meaning: A changes strength or direction of another relationship

  MECHANISM:
    meaning: an identified process connecting cause and effect

  INTERVENTION_EFFECT:
    meaning: changing A produces a supported change in B under stated conditions

  FEEDBACK:
    meaning: causal influence participates in a cyclic process

  COMMON_CAUSE:
    meaning: shared upstream cause contributes to multiple downstream states

  CAUSAL_CHAIN:
    meaning: ordered sequence of causally supported edges

  CAUSAL_LOOP:
    meaning: feedback structure containing causally supported cyclic influence

  CROSS_SCALE_CAUSE:
    meaning: claimed causal influence across H/M/L or other scale boundaries

  COUNTERFACTUAL_DEPENDENCE:
    meaning: outcome differs under an admissible counterfactual intervention

  UNKNOWN_CAUSAL_RELATION:
    meaning: evidence does not license stronger causal typing
```

If evidence cannot discriminate among these classes:

```text
relation = UNKNOWN_CAUSAL_RELATION
```

or:

```text
relation = COMPETING
```

It MUST NOT default to `CAUSES`.

---

# 4. Causal Claim Classes

Every important causal claim SHOULD carry an epistemic class.

```yaml
causal_claim_classes:

  OBSERVATION:
    description: directly recorded or measured relationship

  SOURCE_CLAIM:
    description: causal statement asserted by an external or canonical source

  DERIVED:
    description: causal conclusion derived from accepted premises

  MODEL:
    description: causal structure introduced as a modeling hypothesis

  CONDITIONAL:
    description: causal conclusion valid only under explicit assumptions

  COMPETING:
    description: multiple causal explanations remain viable

  VERIFIED:
    description: supported to the declared verification standard

  UNKNOWN_GAP:
    description: insufficient evidence to determine the causal relation
```

`SOURCE_CLAIM` does not automatically become `VERIFIED`.

`MODEL` does not automatically become `OBSERVATION`.

---

# 5. Typed Inputs

L4 may consume:

```yaml
CausalInput:
  entities: EntitySet
  observations: ObservationSet
  variables: VariableSet
  candidate_relations: RelationSet
  temporal_order: TemporalGraph | null
  dependency_graph: DependencyGraph | null
  intervention_data: InterventionEvidence | null
  counterfactual_model: CounterfactualModel | null
  mechanisms: MechanismEvidence[]
  confounders: VariableSet
  mediators: VariableSet
  moderators: VariableSet
  scope: ScopeEnvelope
  regime: RegimeIdentifier
  measurement_context: MeasurementContext
  provenance: ProvenanceGraph
  freshness: FreshnessState
  assumptions: AssumptionSet
  competing_hypotheses: CausalHypothesis[]
```

Inputs MUST retain their epistemic type.

For example:

```text
observed correlation
```

must not enter the causal layer already labeled:

```text
observed cause
```

unless the source itself explicitly reports a causal result and the provenance records that distinction.

---

# 6. Typed Outputs

```yaml
CausalAssessment:
  claim_id: ClaimID
  source_entity: EntityID
  target_entity: EntityID

  relation_type:
    - ASSOCIATION
    - CORRELATION
    - DEPENDENCY
    - ENABLING_CONDITION
    - CONTRIBUTORY_CAUSE
    - NECESSARY_CONDITION
    - SUFFICIENT_CONDITION
    - MEDIATOR
    - CONFOUNDER
    - MODERATOR
    - MECHANISM
    - INTERVENTION_EFFECT
    - FEEDBACK
    - COMMON_CAUSE
    - COUNTERFACTUAL_DEPENDENCE
    - CROSS_SCALE_CAUSE
    - UNKNOWN_CAUSAL_RELATION

  claim_class:
    - OBSERVATION
    - SOURCE_CLAIM
    - DERIVED
    - MODEL
    - CONDITIONAL
    - COMPETING
    - VERIFIED
    - UNKNOWN_GAP

  evidence: EvidenceRef[]
  provenance: ProvenanceRef[]
  dependencies: ClaimRef[]
  assumptions: AssumptionRef[]
  competing: CausalHypothesis[]
  falsifiers: Falsifier[]
  scope: ScopeEnvelope
  regime: RegimeIdentifier
  freshness: FreshnessState
  confidence_ceiling: float
```

---

# 7. State Variables

Conceptual L4 state MAY include:

```yaml
causal_state:
  candidate_graph: G_candidate
  accepted_graph: G_accepted
  rejected_edges: E_rejected
  quarantined_edges: E_quarantined
  competing_graphs: G_competing[]
  intervention_evidence: I
  observational_evidence: O
  mechanism_evidence: M
  counterfactual_evidence: CF
  dependency_state: D
  provenance_state: P
  scope_state: S
  regime_state: R
  temporal_state: T
  confidence_state: C
  contradiction_state: X
```

These variables describe an AMOS reasoning contract.

They do not assert that a deployed runtime currently implements all such state structures.

---

# 8. Causal Operators

Minimum conceptual operator family:

```text
OBSERVE
ASSOCIATE
CORRELATE
ORDER_TEMPORALLY
MAP_DEPENDENCY
PROPOSE_CAUSE
IDENTIFY_CONFOUNDER
IDENTIFY_MEDIATOR
IDENTIFY_MODERATOR
TEST_MECHANISM
TEST_INTERVENTION
CONSTRUCT_COUNTERFACTUAL
COMPARE_COUNTERFACTUAL
TRACE_CAUSAL_CHAIN
DETECT_FEEDBACK
TEST_SCOPE
TEST_REGIME
TEST_PROVENANCE
CHALLENGE_CAUSE
PROMOTE_CAUSAL_EDGE
DOWNGRADE_CAUSAL_EDGE
QUARANTINE_CAUSAL_EDGE
INVALIDATE_CAUSAL_EDGE
REPAIR_CAUSAL_GRAPH
```

Promotion is governed.

For example:

```text
PROPOSE_CAUSE(A,B)
```

creates a candidate relation.

It does NOT imply:

```text
COMMIT_CAUSE(A,B)
```

---

# 9. Causal Promotion Law

A causal edge may conceptually progress through:

```text
CANDIDATE
   ↓
SUPPORTED
   ↓
CONDITIONAL
   ↓
VALIDATED
```

only when its required evidence conditions are satisfied.

The transition:

```text
CANDIDATE → VALIDATED
```

must never occur merely because a hypothesis is plausible.

A conceptual promotion predicate is:

```text
Promotable(c) =
    EvidenceAdequate(c)
AND ProvenanceValid(c)
AND DependencyClosure(c)
AND ScopeCompatible(c)
AND RegimeCompatible(c)
AND FreshEnough(c)
AND ContradictionResolvedOrPreserved(c)
AND CausalStandardSatisfied(c)
```

If any load-bearing condition is unknown:

```text
Promotable(c) = FALSE
```

unless the target status explicitly permits `CONDITIONAL` or `UNKNOWN/GAP`.

---

# 10. Evidence Ladder

AMOS SHOULD distinguish evidence strength by the causal claim being attempted.

A simplified conceptual ladder is:

```text
description
    ↓
association
    ↓
temporal relationship
    ↓
predictive relationship
    ↓
dependency evidence
    ↓
mechanistic evidence
    ↓
counterfactual evidence
    ↓
intervention evidence
```

This is not a universal scientific ranking.

Different domains require different causal methods.

The important AMOS rule is:

```text
Evidence sufficient for a weaker relation
does not automatically support a stronger relation.
```

---

# 11. Correlation Firewall

Given:

```text
Corr(A,B) != 0
```

AMOS MAY conclude:

```text
A and B exhibit statistical association
```

within the applicable measurement regime.

AMOS MUST NOT conclude solely from that:

```text
A → B
```

because alternatives include:

```text
A → B
B → A
C → A and C → B
A ↔ B
selection bias
measurement artifact
sampling artifact
regime dependence
chance
model misspecification
```

These alternatives form part of the causal challenge set where material.

---

# 12. Temporal Firewall

Temporal precedence can be relevant to causal reasoning:

```text
t(A) < t(B)
```

but:

```text
A BEFORE B != A CAUSED B
```

A temporal sequence may reflect:

- common causes;
- scheduling;
- dependency;
- coincidence;
- delayed observation;
- measurement latency;
- feedback;
- hidden intermediate states.

Observation time and event time SHOULD therefore remain distinct.

---

# 13. Dependency Firewall

L3 dependency structure may provide candidate causal topology, but:

```text
Depends(B,A) != Causes(A,B)
```

Examples include:

- software module dependencies;
- logical premise dependencies;
- data dependencies;
- documentation references;
- organizational reporting relationships.

Such edges can influence propagation without constituting empirical causal effects.

L4 MUST preserve the distinction.

---

# 14. Prediction Firewall

If:

```text
A predicts B
```

AMOS MUST NOT automatically infer:

```text
A causes B
```

Predictive utility may arise from:

- proxy variables;
- common causes;
- leakage;
- temporal structure;
- confounding;
- measurement artifacts;
- stable correlations;
- reverse causation.

Therefore:

```text
PREDICTIVE_POWER != CAUSAL_AUTHORITY
```

---

# 15. Mechanism Law

A mechanism claim requires more than narrative coherence.

A proposed mechanism SHOULD identify:

```yaml
mechanism:
  initiating_condition: ...
  intermediate_states: [...]
  transformations: [...]
  constraints: [...]
  target_effect: ...
  scope: ...
  regime: ...
  evidence: [...]
  alternatives: [...]
  falsifiers: [...]
```

A mechanism becomes stronger when independent observations discriminate it from viable alternatives.

A coherent story alone remains:

```text
MODEL
```

or:

```text
SOURCE_CLAIM
```

---

# 16. Counterfactual Law

A counterfactual asks:

```text
What would B have been
if A had been different,
while the admissible causal structure remained appropriately controlled?
```

Conceptually:

```text
B_do(A=a)
```

must remain distinct from:

```text
B | A=a
```

Interventional and observational conditioning are not interchangeable by default.

Counterfactual reasoning MUST declare:

- intervention;
- baseline;
- preserved conditions;
- changed conditions;
- causal assumptions;
- model dependence;
- uncertainty.

Unsupported counterfactuals remain `MODEL`.

---

# 17. Intervention Law

An intervention claim is stronger than an observational association.

Conceptually:

```text
ΔB under do(A)
```

must not be inferred solely from:

```text
ΔB associated with ΔA
```

An intervention assessment SHOULD ask:

```text
Was A actually manipulated?
Was assignment controlled or otherwise causally identifiable?
Were confounders addressed?
Was B measured appropriately?
Was the intervention delivered as intended?
Was the comparison valid?
Does the result apply to the requested population/regime?
```

---

# 18. Confounder Law

Where:

```text
C → A
C → B
```

a naive relationship between A and B may be misleading.

AMOS SHOULD preserve candidate confounders until evidence excludes or appropriately controls them.

Absence of an identified confounder does not prove absence of confounding.

Therefore:

```text
NO_KNOWN_CONFOUNDER != NO_CONFOUNDING
```

---

# 19. Mediation Law

If a claim proposes:

```text
A → M → B
```

AMOS SHOULD distinguish:

- total effect;
- direct effect;
- mediated effect;
- interaction/moderation;
- unsupported decomposition.

The existence of correlations among A, M, and B does not establish mediation.

---

# 20. Necessary and Sufficient Conditions

AMOS MUST distinguish:

```text
NECESSARY
```

from:

```text
SUFFICIENT
```

If A is necessary for B:

```text
B ⇒ A
```

under the declared model/scope.

This does not imply:

```text
A ⇒ B
```

Likewise, sufficient does not automatically mean necessary.

Claims of necessity or sufficiency SHOULD carry especially explicit scope conditions because they are easily overgeneralized.

---

# 21. Feedback Law

Causal systems may contain cycles:

```text
A → B → C → A
```

Therefore AMOS MUST NOT assume every causal system is a static DAG unless the applicable method requires that representation.

Feedback analysis SHOULD preserve:

- direction;
- lag;
- gain/strength where known;
- stabilizing versus amplifying effects;
- regime dependence;
- observation interval.

---

# 22. Cross-Scale Causal Law

For H/M/L reasoning:

```text
L → M
M → H
H → M
M → L
```

are possible candidate directions.

But cross-scale structural correspondence does not prove causal propagation.

Therefore:

```text
CROSS_SCALE_SIMILARITY != CROSS_SCALE_CAUSATION
```

Any cross-scale causal claim MUST specify:

```yaml
source_scale: H | M | L
target_scale: H | M | L
mechanism: ...
time_scale: ...
aggregation_rule: ...
scope: ...
evidence: ...
```

Absent this support, the mapping remains `MODEL`.

---

# 23. H/M/L Applicability

### H — Governing/System Scale

At H, L4 evaluates:

- system-wide causal architecture;
- governing constraints;
- systemic feedback;
- large dependency cascades;
- policy/intervention effects;
- regime-level causes;
- cross-domain propagation.

### M — Subsystem/Mechanism Scale

At M, L4 evaluates:

- subsystem interactions;
- mechanisms;
- mediators;
- intermediate transformations;
- organizational/process causal chains;
- component interactions.

### L — Local/Event Scale

At L, L4 evaluates:

- individual observations;
- local interventions;
- events;
- variable transitions;
- direct measurements;
- specific causal edges.

No scale automatically dominates another.

Cross-scale aggregation requires explicit transformation rules.

---

# 24. Provenance Law for Causal Evidence

Every consequential causal edge SHOULD be provenance-bound.

Minimum record:

```yaml
causal_provenance:
  claim_id: ...
  source_id: ...
  source_type: ...
  origin: ...
  ancestry: [...]
  method: ...
  observation_time: ...
  event_time: ...
  retrieval_time: ...
  scope: ...
  regime: ...
  transformations: [...]
  independence_status: ...
  freshness: ...
```

Multiple reports derived from one original study, dataset, experiment, benchmark, or model MUST NOT be counted as independent causal confirmations.

Thus:

```text
SOURCE_COUNT != INDEPENDENT_EVIDENCE_COUNT
```

---

# 25. Provenance Independence

If:

```text
E1 ← S
E2 ← S
E3 ← S
```

then E1, E2, and E3 may share ancestry.

They cannot automatically be treated as three independent causal confirmations.

Independent confirmation requires sufficiently independent evidence topology.

If independence cannot be established:

```text
independence_status = UNKNOWN
```

and confidence MUST be bounded accordingly.

---

# 26. Confidence Ceiling

Causal confidence is bounded by load-bearing uncertainty.

Conceptually:

```text
C_causal ≤ min(
    C_evidence,
    C_provenance,
    C_identification,
    C_scope,
    C_regime,
    C_temporal,
    C_measurement,
    C_dependency
)
```

This is an AMOS governance equation, not a universal statistical theorem.

A highly confident source cannot repair a weak causal design merely by asserting certainty.

---

# 27. Competing Causal Hypotheses

AMOS MUST preserve materially viable alternatives.

Example:

```yaml
competing:
  - id: H1
    hypothesis: A causes B

  - id: H2
    hypothesis: B causes A

  - id: H3
    hypothesis: C causes both A and B

  - id: H4
    hypothesis: relationship is measurement artifact

  - id: H5
    hypothesis: relationship is regime-specific
```

If available evidence cannot discriminate them:

```text
status = COMPETING
```

not:

```text
status = VERIFIED
```

---

# 28. Discriminating Evidence Law

When competing causal models exist, AMOS SHOULD seek the lowest-cost evidence with the highest expected discriminatory value.

Prefer:

```text
ONE DISCRIMINATING TEST
```

over:

```text
MANY REDUNDANT CONFIRMATIONS
```

where the former can resolve the outcome-changing uncertainty.

---

# 29. Adversarial Causal Validation

For consequential causal conclusions, AMOS SHOULD challenge the preferred explanation.

Challenge questions include:

```text
Could the direction be reversed?

Could a hidden common cause explain the observation?

Could selection explain it?

Could measurement error explain it?

Could the apparent mechanism be post-hoc?

Could the evidence sources share ancestry?

Could the relationship disappear in another regime?

Could timing invalidate the proposed direction?

Could another mechanism produce the same observations?

Does intervention evidence contradict observational evidence?
```

Successful challenge requires downgrade, qualification, competition preservation, or invalidation.

---

# 30. Scope Law

Every causal claim inherits an applicability envelope.

```yaml
scope:
  population: ...
  system: ...
  environment: ...
  geography: ...
  scale: ...
  time: ...
  measurement_method: ...
  intervention_type: ...
  assumptions: [...]
```

A causal conclusion established in `S1` does not automatically hold in `S2`.

Therefore:

```text
VALID_IN_SCOPE != UNIVERSALLY_VALID
```

---

# 31. Regime Law

Causal structure may change across regimes.

Examples include:

```text
normal / stressed
pre-change / post-change
low-load / high-load
stable / unstable
development / production
peace / crisis
liquid / illiquid
```

A causal edge MUST NOT silently survive a regime transition if its validity depends on the previous regime.

Conceptually:

```text
Valid(c, R1) does not imply Valid(c, R2)
```

---

# 32. Freshness Law

Causal evidence can become stale when:

- system architecture changes;
- policy changes;
- environment changes;
- population changes;
- instrumentation changes;
- dependencies change;
- causal mechanisms themselves change.

Freshness is therefore part of causal validity.

```text
PAST_CAUSAL_SUPPORT != CURRENT_CAUSAL_VALIDITY
```

---

# 33. Causal Dependency Closure

A causal conclusion may depend upon other claims.

Example:

```text
C3 depends on C1 and C2.
```

Then:

```text
Invalidate(C1)
```

requires re-evaluation of:

```text
C3
```

but not unrelated causal claims.

This follows selective invalidation:

```text
invalidate failed premise
→ invalidate dependent edges
→ preserve unaffected graph
```

Global causal recomputation is a last resort.

---

# 34. Causal Epoch Integrity

Where AMOS reasoning spans changing system states, causal evidence MUST remain associated with the state/epoch in which it was valid.

Conceptually:

```text
Evidence(E, epoch_n)
```

cannot automatically authorize:

```text
Cause(C, epoch_n+1)
```

after relevant causal structure changes.

Revalidation is required when load-bearing conditions change.

---

# 35. Causal Decision Boundary

Even a supported causal claim does not automatically authorize action.

```text
CAUSAL_KNOWLEDGE != AUTHORITY
```

Therefore:

```text
CAUSE_SUPPORTED
```

does not imply:

```text
INTERVENTION_AUTHORIZED
```

Authorization remains a control-plane/governance responsibility.

---

# 36. Proposal / Commit Boundary

A causal model may recommend an intervention:

```text
PROPOSE(do(A))
```

but this remains a proposal.

```text
PROPOSAL != COMMIT
```

Before execution, relevant control planes must evaluate:

- authority;
- permissions;
- constraints;
- reversibility;
- risk;
- current state;
- stale evidence;
- affected stakeholders;
- commit-time validity.

---

# 37. Causal Risk Escalation

Validation requirements SHOULD increase with:

```text
irreversibility
× consequence
× uncertainty
× dependency fan-out
× affected population
```

Low-impact reversible experimentation may tolerate more uncertainty than irreversible high-impact intervention.

This is a governance principle, not a claim of a universally calibrated numerical risk formula.

---

# 38. Causal Failure Modes

L4 recognizes at least the following failures:

### F1 — Correlation Promotion

```text
correlation → cause
```

without causal support.

### F2 — Temporal Fallacy

```text
A happened first → A caused B
```

### F3 — Reverse Causality

Actual or plausible direction:

```text
B → A
```

is ignored.

### F4 — Confounder Omission

A common cause is omitted.

### F5 — Mechanism Fabrication

A plausible mechanism is narrated without evidence.

### F6 — Scope Leakage

A valid local causal result is generalized beyond its support.

### F7 — Regime Leakage

A causal relationship is reused after regime change.

### F8 — Provenance Multiplication

Correlated descendants are counted as independent confirmations.

### F9 — Dependency/Cause Collapse

Structural dependency is mislabeled causal.

### F10 — Prediction/Cause Collapse

Predictive performance is treated as mechanism evidence.

### F11 — Cross-Scale Overreach

Structural correspondence across H/M/L is treated as causal propagation.

### F12 — Intervention Overclaim

Observed association is used to predict intervention effects without identification.

### F13 — Counterfactual Fabrication

Unsupported alternative histories are presented as causal conclusions.

### F14 — Confidence Inflation

Causal confidence exceeds the weakest load-bearing premise.

### F15 — Causal Graph Persistence Error

Invalidated causal edges remain active downstream.

### F16 — Authority Leakage

A causal conclusion is treated as permission to intervene.

---

# 39. Repair and Recovery

When causal integrity fails:

```text
DETECT
→ FREEZE PROMOTION
→ IDENTIFY FAILED EDGE/PREMISE
→ TRACE DEPENDENTS
→ DOWNGRADE OR QUARANTINE
→ PRESERVE UNAFFECTED STRUCTURE
→ GENERATE COMPETING EXPLANATIONS
→ SEEK DISCRIMINATING EVIDENCE
→ REVALIDATE
→ RESTORE IF WARRANTED
```

Repair MUST target the smallest causal cut sufficient to restore integrity.

Do not erase unaffected knowledge.

---

# 40. Causal Quarantine

A causal edge SHOULD enter quarantine when:

- provenance is unresolved;
- evidence is contradictory;
- scope is unclear;
- regime compatibility is unknown;
- dependency closure fails;
- causal identification is insufficient;
- source independence cannot be established;
- falsifying evidence appears.

Quarantine means:

```text
stored
but not trusted for stronger downstream causal promotion
```

It does not mean deleted.

---

# 41. Validators

Conceptual L4 validators include:

```text
validate_relation_type()
validate_temporal_order()
validate_dependency_vs_cause()
validate_confounders()
validate_mechanism()
validate_intervention_basis()
validate_counterfactual_basis()
validate_scope()
validate_regime()
validate_freshness()
validate_provenance()
validate_independence()
validate_competing_hypotheses()
validate_confidence_ceiling()
validate_authority_boundary()
validate_dependency_closure()
```

---

# 42. Minimum Causal Tests

A causal artifact SHOULD be testable against:

### Test 1 — Correlation Firewall

Input:

```text
A and B correlate.
```

Expected:

```text
ASSOCIATION/CORRELATION
```

not automatically:

```text
CAUSE
```

### Test 2 — Temporal Firewall

Input:

```text
A precedes B.
```

Expected:

```text
TEMPORAL_PRECEDENCE
```

not automatically causal.

### Test 3 — Dependency Firewall

Input:

```text
B imports A.
```

Expected:

```text
DEPENDENCY
```

not empirical causation.

### Test 4 — Confounder Challenge

Given candidate:

```text
A → B
```

and plausible:

```text
C → A
C → B
```

Expected:

```text
CONDITIONAL / COMPETING
```

until discriminated.

### Test 5 — Provenance Sybil Test

Three sources descend from one origin.

Expected:

```text
independence_count != 3
```

### Test 6 — Regime Shift

Causal edge validated in R1 but R2 changes a load-bearing mechanism.

Expected:

```text
REVALIDATION_REQUIRED
```

### Test 7 — Authority Boundary

Supported causal intervention is proposed.

Expected:

```text
PROPOSAL
```

not automatic execution.

---

# 43. Falsifiers

An L4 causal claim SHOULD identify what would weaken or falsify it.

Examples:

```yaml
falsifiers:
  - intervention produces no predicted effect
  - reverse intervention explains observations better
  - identified confounder removes relationship
  - mechanism prediction fails
  - effect disappears under valid replication
  - causal direction reverses under improved temporal measurement
  - provenance is discovered to be non-independent
  - result fails outside the originally hidden scope
  - regime transition invalidates mechanism
  - measurement artifact explains the observed relationship
```

A claim with no conceivable falsifier SHOULD NOT be promoted as strong causal knowledge merely because it is internally coherent.

---

# 44. Invariants

## L4-I1 — Causal Typing

```text
Every causal claim MUST have an explicit relation type.
```

## L4-I2 — Correlation Firewall

```text
CORRELATION != CAUSATION
```

## L4-I3 — Dependency Firewall

```text
DEPENDENCY != CAUSATION
```

## L4-I4 — Prediction Firewall

```text
PREDICTION != CAUSATION
```

## L4-I5 — Temporal Firewall

```text
PRECEDENCE != CAUSATION
```

## L4-I6 — Evidence Requirement

```text
CAUSAL_STRENGTH cannot exceed EVIDENCE_STRENGTH
```

## L4-I7 — Provenance Requirement

```text
No consequential causal promotion without recoverable provenance.
```

## L4-I8 — Scope Preservation

```text
Causal claims inherit scope.
```

## L4-I9 — Regime Preservation

```text
Causal claims inherit regime validity.
```

## L4-I10 — Confidence Ceiling

```text
Derived causal confidence cannot exceed the weakest
load-bearing premise without independent revalidation.
```

## L4-I11 — Competing Preservation

```text
Unresolved viable causal alternatives remain COMPETING.
```

## L4-I12 — Selective Invalidation

```text
Failure of one causal premise invalidates dependent claims,
not unrelated claims.
```

## L4-I13 — Cross-Scale Firewall

```text
STRUCTURAL_SIMILARITY != CROSS_SCALE_CAUSATION
```

## L4-I14 — Authority Separation

```text
CAUSAL_CAPABILITY != AUTHORITY
```

## L4-I15 — Commit Separation

```text
CAUSAL_PROPOSAL != COMMIT
```

---

# 45. Dependencies

L4 conceptually depends upon preceding integrity layers.

```text
L0 INTEGRITY
    ↓
L1 EPISTEMIC
    ↓
L2 PROVENANCE
    ↓
L3 DEPENDENCY
    ↓
L4 CAUSAL
```

Interpretation:

### L0

Ensures causal reasoning does not violate governing integrity constraints.

### L1

Determines what kind of claim is being made and what evidence status it carries.

### L2

Preserves origin, ancestry, independence, freshness, and evidence lineage.

### L3

Tracks which premises and structures causal conclusions depend upon.

### L4

Determines what causal strength those premises actually license.

L4 MUST NOT override L0–L3.

---

# 46. Control-Plane Requirements

Any implementation claiming L4 conformance SHOULD provide mechanisms for:

```yaml
control_plane:
  claim_typing: required
  provenance_validation: required
  dependency_validation: required
  causal_promotion_gate: required
  scope_gate: required
  regime_gate: required
  freshness_gate: required
  contradiction_gate: required
  authority_gate: required_for_action
  commit_revalidation: required_for_consequential_action
  selective_invalidation: required
  auditability: required
```

This describes the contract.

It does not establish that any particular AMOS runtime already implements every mechanism.

---

# 47. Agent Requirements

An agent using L4 SHOULD:

1. identify the causal question;
2. identify the weakest sufficient causal claim;
3. classify available evidence;
4. preserve provenance;
5. construct viable alternatives;
6. identify confounders;
7. check temporal ordering;
8. check scope and regime;
9. distinguish observation from intervention;
10. identify falsifiers;
11. assign the weakest accurate conclusion class;
12. request control-plane authorization before consequential intervention.

An agent MUST NOT increase causal strength merely to make an answer more decisive.

---

# 48. Skill Requirements

A Skill interacting with L4 SHOULD declare:

```yaml
causal_contract:
  reads_causal_state: true | false
  proposes_causal_edges: true | false
  validates_causal_edges: true | false
  mutates_causal_state: true | false

  accepted_evidence_types: [...]
  produced_claim_types: [...]
  required_provenance: [...]
  scope_constraints: [...]
  regime_constraints: [...]
  authority_required: [...]
  falsifiers: [...]
```

A Skill capable of producing causal proposals does not automatically possess authority to commit them.

---

# 49. Workflow

Canonical conceptual workflow:

```text
1. RECEIVE QUESTION / OBSERVATION
2. TYPE VARIABLES AND ENTITIES
3. LOAD RELEVANT DEPENDENCIES
4. LOAD PROVENANCE
5. IDENTIFY OBSERVED RELATION
6. GENERATE CANDIDATE CAUSAL MODELS
7. IDENTIFY CONFOUNDERS / MEDIATORS / MODERATORS
8. CHECK TEMPORAL STRUCTURE
9. CHECK MECHANISM EVIDENCE
10. CHECK COUNTERFACTUAL / INTERVENTION EVIDENCE
11. CHECK SCOPE
12. CHECK REGIME
13. CHECK FRESHNESS
14. CHECK PROVENANCE INDEPENDENCE
15. RUN COMPETING-HYPOTHESIS CHALLENGE
16. IDENTIFY FALSIFIERS
17. APPLY CONFIDENCE CEILING
18. CLASSIFY CONCLUSION
19. PROPOSE RESULT
20. IF ACTION REQUIRED → AUTHORITY / COMMIT GATES
21. RECORD PROVENANCE AND DEPENDENCIES
```

---

# 50. Protocol

A minimal causal exchange protocol:

```yaml
CAUSAL_REQUEST:
  question: ...
  candidate_entities: [...]
  requested_relation: ...
  requested_scope: ...
  requested_regime: ...

CAUSAL_ANALYSIS:
  observed_relationship: ...
  candidate_causes: [...]
  competing: [...]
  evidence: [...]
  provenance: [...]
  assumptions: [...]
  falsifiers: [...]

CAUSAL_DECISION:
  relation_type: ...
  claim_class: ...
  confidence_ceiling: ...
  scope: ...
  regime: ...
  unresolved_gaps: [...]

CAUSAL_ACTION_PROPOSAL:
  intervention: ...
  expected_effect: ...
  evidence_basis: ...
  uncertainty: ...
  reversibility: ...
  authority_required: ...
```

---

# 51. Interaction with RSCF

Every consequential causal claim SHOULD be representable as an RSCF capsule.

```yaml
rscf:
  claim: ...
  claim_class: ...
  causal_relation_type: ...
  premises: [...]
  evidence: [...]
  provenance: [...]
  scope: ...
  regime: ...
  freshness: ...
  dependencies: [...]
  competing: [...]
  falsifiers: [...]
  confidence_ceiling: ...
```

RSCF dependency structure makes causal invalidation selective.

If a premise fails:

```text
invalidate descendants of failed premise
```

rather than:

```text
erase entire knowledge state
```

---

# 52. Interaction with GMEF

Where a causal conclusion supports a system change, the causal result remains evidence for governance rather than authority itself.

Conceptually:

```text
L4 CAUSAL ASSESSMENT
        ↓
CHANGE PROPOSAL
        ↓
GOVERNANCE / GMEF
        ↓
AUTHORITY VALIDATION
        ↓
RISK / REVERSIBILITY
        ↓
COMMIT-TIME REVALIDATION
        ↓
EXECUTE / REJECT / DEFER / SANDBOX
```

A correct causal model can still lead to an unauthorized or unacceptable intervention.

---

# 53. Interaction with Counterfactual Reasoning

L4 supplies causal boundaries to counterfactual reasoning.

Counterfactual generation without causal discipline may create fluent alternative histories that are not warranted.

Therefore:

```text
COUNTERFACTUAL_PLAUSIBILITY
!=
COUNTERFACTUAL_CAUSAL_VALIDITY
```

Counterfactual conclusions remain bounded by the validity of the causal model used to generate them.

---

# 54. Interaction with Memory

Causal memory SHOULD preserve:

```yaml
causal_memory:
  claim: ...
  relation_type: ...
  evidence_epoch: ...
  provenance: ...
  scope: ...
  regime: ...
  dependencies: [...]
  competing: [...]
  falsifiers: [...]
  revalidation_conditions: [...]
```

Memory retrieval MUST NOT strip these qualifiers and return only:

```text
A causes B
```

when the stored knowledge was actually:

```text
A may contribute to B under R1 and S1,
conditional on assumptions X and Y.
```

---

# 55. Interaction with Prediction

Prediction and causation remain separate epistemic lanes.

```text
Predict(B | A)
```

may be useful without establishing:

```text
Effect(do(A), B)
```

Likewise, a causal factor may have weak predictive value in a noisy system.

AMOS SHOULD therefore preserve both:

```text
predictive evidence
```

and:

```text
causal evidence
```

without collapsing them.

---

# 56. Interaction with Repair

Causal diagnosis influences repair targeting.

If failure `F` is observed, AMOS SHOULD avoid immediately repairing the nearest correlated component.

Instead:

```text
OBSERVED FAILURE
      ↓
CANDIDATE CAUSES
      ↓
CAUSAL DISCRIMINATION
      ↓
TARGET OF REPAIR
      ↓
REPAIR PROPOSAL
```

Repairing a symptom while preserving the actual cause may create recurring failure or hidden degradation.

---

# 57. Interaction with System Completion

A causal architecture is incomplete for a declared scope if it requires causal conclusions but lacks mechanisms for:

- relation typing;
- provenance;
- competing hypotheses;
- falsification;
- scope;
- regime;
- temporal ordering;
- dependency propagation;
- causal invalidation.

However:

```text
STRUCTURAL_COMPLETENESS != EMPIRICAL_VALIDITY
```

A perfectly specified causal subsystem can still contain false causal hypotheses.

---

# 58. Non-Purposes

L4 is NOT intended to:

- prove that AMOS has discovered universal causal laws;
- replace domain-specific causal inference;
- replace experimental design;
- replace statistical methodology;
- declare philosophical theories of causation universally correct;
- infer causation from narrative coherence;
- authorize interventions;
- convert AMOS structural analogies into empirical causal facts.

---

# 59. Hard Boundaries

```text
ASSOCIATION != CAUSATION

CORRELATION != CAUSATION

TEMPORAL_PRECEDENCE != CAUSATION

DEPENDENCY != CAUSATION

PREDICTION != CAUSATION

SIMILARITY != CAUSATION

STRUCTURAL_ANALOGY != CAUSATION

MODEL != OBSERVATION

SOURCE_CLAIM != VERIFIED

MECHANISM_PROPOSAL != MECHANISM_VALIDATION

COUNTERFACTUAL != OBSERVED_FACT

INTERVENTION_PROPOSAL != INTERVENTION_EFFECT

CAPABILITY != AUTHORITY

PROPOSAL != COMMIT

UNKNOWN/GAP != PASS
```

---

# 60. Gap Status

This artifact supplies a **full proposed AMOS causal-law contract**, but its status must remain bounded.

It does NOT by itself establish that every definition, operator, equation, causal category, threshold, or protocol above already exists verbatim in Trang Phan's approved source canon.

Accordingly:

```yaml
gap_status:
  structural_contract: PROVIDED
  causal_framework: PROVIDED
  runtime_implementation: NOT_ESTABLISHED
  empirical_validation: NOT_ESTABLISHED
  verbatim_source_canon_equivalence: NOT_ESTABLISHED
  final_canon_approval: REQUIRED
```

---

# 61. RSCF Completion State

```yaml
claim_class: AMOS_MODEL

claim:
  "L4_CAUSAL defines a governed causal-integrity layer that prevents
   unsupported promotion from association, dependency, prediction,
   temporal sequence, or structural similarity into causal claims."

evidence:
  - current AMOS governing architecture supplied by origin architect/steward
  - preceding L0/L1/L2/L3 structural contracts
  - AMOS causal-firewall requirements

provenance:
  origin_architect: Trang Phan
  artifact_family: AMOS_OS
  layer: 01_CANON/01_CORE_LAWS
  derivation_status: proposed_structural_completion

scope:
  system: AMOS
  layer: causal_reasoning
  applicability:
    - reasoning
    - agents
    - skills
    - workflows
    - memory
    - governance
    - intervention_proposals

regime:
  - analytical
  - agentic
  - runtime_governance

freshness:
  revalidate_on:
    - canon_change
    - causal_ontology_change
    - provenance_rule_change
    - dependency_rule_change
    - control_plane_change

dependencies:
  - L0_INTEGRITY
  - L1_EPISTEMIC
  - L2_PROVENANCE
  - L3_DEPENDENCY

competing:
  - domain-specific causal frameworks may require stronger or different identification rules
  - different causal formalisms may represent equivalent relationships differently
  - some causal questions may remain fundamentally underidentified from available evidence

falsifiers:
  - approved source canon contradicts a proposed L4 law
  - a promoted causal rule permits unsupported causal inference
  - causal provenance cannot be reconstructed
  - scope or regime restrictions are lost downstream
  - correlated sources are counted as independent confirmation
  - dependency or prediction is automatically promoted to causation
  - causal conclusions automatically authorize interventions

confidence_ceiling:
  structural_coherence: HIGH
  canon_equivalence: UNVERIFIED
  runtime_implementation: UNKNOWN
  empirical_validity: DOMAIN_DEPENDENT
```

---

# 62. Canon Promotion Gate

Before this artifact is labeled `FINAL_CANON`, require:

```text
[ ] origin/steward approval
[ ] source-canon reconciliation
[ ] terminology reconciliation
[ ] L0 compatibility
[ ] L1 compatibility
[ ] L2 compatibility
[ ] L3 compatibility
[ ] downstream dependency review
[ ] RSCF validation
[ ] control-plane compatibility
[ ] causal failure-mode tests
[ ] contradiction scan
[ ] supersession record
[ ] version assignment
```

Until those conditions are satisfied:

```text
FULL_CONTENT != FINAL_CANON
```

The correct status is:

```text
AMOS_MODEL / PROPOSED_CANON_CONTENT
```

---

[[00_ROOT_MOC]]|[[AMOS MOC]]

---

**Related:** [[00_HOME]] · [[AMOS_RSCF_NODES]] · [[L0_INTEGRITY]] · [[L1_EPISTEMIC]] · [[L2_PROVENANCE]] · [[L3_DEPENDENCY]]

---

RSCF-NODE

node_id: l4_causal

node_type: core_law

path: 01_CANON/01_CORE_LAWS/L4_CAUSAL.md

RSCF-RELATIONS:

- DEPENDS_ON: [[L0_INTEGRITY]]
- DEPENDS_ON: [[L1_EPISTEMIC]]
- DEPENDS_ON: [[L2_PROVENANCE]]
- DEPENDS_ON: [[L3_DEPENDENCY]]
- INDEXED_BY: [[00_HOME]]
- INDEXED_BY: [[AMOS_RSCF_NODES]]

claim_class: AMOS_MODEL

```
```

---
**MOC:** [[01_CORE_LAWS_MOC]]
