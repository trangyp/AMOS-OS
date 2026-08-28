---
tags:
- canon
- core_laws
- scope
- regime
- temporal
- freshness
- applicability
- rscf
- governance
- canon/universe
title: L5 Scope, Regime, and Temporal Laws
origin_architect: Trang Phan
status: AMOS_MODEL
canon_status: PROPOSED_CANON_CONTENT
epistemic_class: AMOS_MODEL
type: document
source: 01_CANON/01_CORE_LAWS
rscf:
  state: DERIVED
  claim_class: DERIVED
  provenance: AMOS_corpus
  scope: AMOS_general
---


# L5 Scope, Regime, and Temporal Laws

**Origin architect / steward:** Trang Phan  
**Layer:** `01_CANON / 01_CORE_LAWS / L5_SCOPE_REGIME`  
**Artifact class:** `CORE_LAW_CONTRACT`  
**Status:** `AMOS_MODEL — requires canon approval / provenance validation`

> L5 governs **where, when, under which conditions, and for how long** an AMOS claim, rule, dependency, causal relation, model, decision, capability, or proof capsule remains applicable.
>
> Validity is never assumed to be universal merely because something was valid somewhere, sometime, or under one operating condition.

---

# 1. Purpose

`L5_SCOPE_REGIME` establishes the AMOS laws for:

- scope;
- applicability;
- regime;
- temporal validity;
- freshness;
- observation time;
- event time;
- decision time;
- execution time;
- validity windows;
- regime transitions;
- scope transitions;
- cross-scale applicability;
- stale-state detection;
- revalidation;
- selective invalidation.

L5 exists to prevent AMOS from silently transforming:

```text
VALID HERE
```

into:

```text
VALID EVERYWHERE
```

or:

```text
VALID THEN
```

into:

```text
VALID NOW
```

or:

```text
VALID UNDER REGIME R1
```

into:

```text
VALID UNDER REGIME R2
```

or:

```text
VALID FOR POPULATION P1
```

into:

```text
VALID FOR POPULATION P2
```

without evidence supporting the transfer.

The governing principle is:

```text
VALIDITY IS SCOPED,
REGIME-BOUND,
AND TEMPORALLY CONDITIONED
UNLESS BROADER VALIDITY IS ESTABLISHED.
```

---

# 2. Core L5 Law

Every consequential AMOS claim SHOULD possess an applicability envelope.

Conceptually:

```text
Validity(C)
=
Validity(
    C,
    Scope,
    Regime,
    Time,
    Scale,
    Observer,
    Measurement,
    Assumptions,
    Dependencies,
    Provenance
)
```

This is an **AMOS MODEL expression**, not a universal mathematical theorem.

A claim stripped from its applicability envelope is not equivalent to the original claim.

Therefore:

```text
CLAIM_WITH_CONTEXT != CLAIM_WITHOUT_CONTEXT
```

and:

```text
VALID(C, S1, R1, T1)
DOES NOT IMPLY
VALID(C, S2, R2, T2)
```

unless transfer has been independently justified.

---

# 3. Fundamental Laws

## L5-L1 — Scope Preservation

```text
Every consequential conclusion inherits the scope
of its load-bearing premises unless broader scope
is independently established.
```

## L5-L2 — Regime Preservation

```text
Validity established in regime R1
does not automatically transfer to regime R2.
```

## L5-L3 — Temporal Preservation

```text
Validity established at time T1
does not automatically establish validity at T2.
```

## L5-L4 — Freshness Requirement

```text
STALE_EVIDENCE != CURRENT_EVIDENCE
```

## L5-L5 — Scale Preservation

```text
VALID_AT_L != VALID_AT_M != VALID_AT_H
```

unless a valid cross-scale transformation is established.

## L5-L6 — Observer Preservation

```text
OBSERVED_BY_O1 != OBSERVED_BY_O2
```

when observer position or measurement procedure materially affects the claim.

## L5-L7 — Measurement Preservation

```text
MEASURED_BY_METHOD_M1
!=
MEASURED_BY_METHOD_M2
```

unless compatibility is established.

## L5-L8 — Assumption Preservation

A conclusion inherits its load-bearing assumptions.

```text
REMOVE_ASSUMPTION
→
REVALIDATE_DEPENDENT_CLAIMS
```

## L5-L9 — Transition Revalidation

Material regime, scope, temporal, measurement, or dependency transitions trigger revalidation.

## L5-L10 — Unknown Applicability Is Not Universal Applicability

```text
UNKNOWN_SCOPE != UNIVERSAL_SCOPE
UNKNOWN_REGIME != ALL_REGIMES
UNKNOWN_TIME != TIME_INVARIANT
```

---

# 4. Definition of Scope

In L5, `scope` means the explicit applicability boundary of a claim, rule, model, operation, or decision.

A scope MAY include:

```yaml
scope:
  system: ...
  subsystem: ...
  population: ...
  entity_set: [...]
  geography: ...
  environment: ...
  domain: ...
  task: ...
  scale: ...
  observer: ...
  measurement_method: ...
  authority_domain: ...
  data_domain: ...
  operational_context: ...
  assumptions: [...]
  exclusions: [...]
```

Scope answers:

> **To what exactly does this apply?**

Scope is not merely metadata.

It is part of validity.

---

# 5. Scope Envelope

AMOS SHOULD represent consequential applicability through a structured envelope.

```yaml
ScopeEnvelope:
  scope_id: ScopeID

  system:
    id: ...
    type: ...

  domain:
    primary: ...
    secondary: [...]

  population:
    included: [...]
    excluded: [...]

  entities:
    included: [...]
    excluded: [...]

  environment:
    type: ...
    constraints: [...]

  geography:
    region: ...
    restrictions: [...]

  scale:
    level: H | M | L | CROSS_SCALE
    resolution: ...

  observer:
    identity_class: ...
    observation_position: ...

  measurement:
    method: ...
    instrument: ...
    units: ...
    resolution: ...

  assumptions: [...]
  exclusions: [...]
  boundaries: [...]

  provenance: [...]
```

Missing fields remain unknown.

They MUST NOT silently acquire permissive defaults.

---

# 6. Scope Intersection Law

When multiple premises support a conclusion, the default conclusion scope cannot exceed the compatible intersection of the load-bearing premise scopes.

Conceptually:

```text
Scope(C)
⊆
⋂ Scope(P_i)
```

for load-bearing premises `P_i`, unless an explicit transfer argument independently establishes a broader envelope.

This prevents:

```text
P1 valid in Europe
P2 valid globally
-----------------
C valid globally
```

when `P1` is necessary to `C`.

The safe inherited scope is bounded by the narrower load-bearing premise.

---

# 7. Scope Expansion Law

Scope expansion is a governed operation.

```text
EXPAND_SCOPE(C, S1 → S2)
```

requires evidence supporting transfer.

A proposed expansion SHOULD evaluate:

- population compatibility;
- environmental compatibility;
- measurement compatibility;
- mechanism stability;
- regime compatibility;
- temporal compatibility;
- scale compatibility;
- provenance;
- assumptions;
- known exclusions;
- distribution shift.

Therefore:

```text
GENERALIZATION
=
CLAIM_REQUIRING_EVIDENCE
```

not a default transformation.

---

# 8. Scope Contraction

Scope may safely be narrowed when required.

```text
S2 ⊂ S1
```

A narrower claim may remain supported even when a broader claim fails.

Example:

```text
"works universally"
```

may be falsified while:

```text
"works under configuration X"
```

remains supported.

AMOS SHOULD prefer selective scope contraction over unnecessary total rejection when evidence permits.

---

# 9. Definition of Regime

A `regime` is a materially distinct operating condition under which relationships, constraints, distributions, mechanisms, policies, or valid behaviors may differ.

Examples include:

```text
NORMAL
STRESSED
CRISIS
RECOVERY

TRAINING
VALIDATION
PRODUCTION

LOW_LOAD
HIGH_LOAD

LIQUID
ILLIQUID

PRE_POLICY
POST_POLICY

PRE_DEPLOYMENT
POST_DEPLOYMENT

STABLE
TRANSITIONAL
UNSTABLE

ONLINE
OFFLINE

NOMINAL
DEGRADED
FAILSAFE
```

These examples are illustrative.

Domain-specific regime definitions require domain-specific evidence.

---

# 10. Regime State

A conceptual regime record MAY contain:

```yaml
RegimeState:
  regime_id: RegimeID
  regime_class: ...
  start_time: ...
  end_time: ...
  detection_method: ...
  defining_conditions: [...]
  observed_indicators: [...]
  uncertainty: ...
  provenance: [...]
  predecessor: ...
  successor: ...
```

A regime label without defining conditions is insufficient for strong reasoning.

---

# 11. Regime Detection Law

AMOS MUST distinguish:

```text
REGIME_OBSERVED
```

from:

```text
REGIME_INFERRED
```

and:

```text
REGIME_ASSUMED
```

For example:

```yaml
regime_detection:
  status: INFERRED
  evidence:
    - volatility_shift
    - policy_change
    - dependency_change
  confidence: ...
```

must not be represented as directly observed if the regime is model-derived.

---

# 12. Regime Transfer Law

Given:

```text
Valid(C, R1)
```

AMOS cannot infer:

```text
Valid(C, R2)
```

merely because the claim identifier is unchanged.

Transfer requires evidence that load-bearing validity conditions survive the transition.

Conceptually:

```text
Transferable(C, R1 → R2)
=
MechanismStable
AND ScopeCompatible
AND DependencyCompatible
AND MeasurementCompatible
AND AssumptionsCompatible
AND NoMaterialContradiction
```

This is an AMOS governance model.

---

# 13. Regime Shift Law

A regime shift occurs when one or more validity-relevant conditions change sufficiently that previously accepted conclusions require reconsideration.

Potential triggers include:

- policy change;
- structural break;
- market transition;
- software deployment;
- architecture change;
- model update;
- population shift;
- sensor change;
- environmental change;
- authority change;
- dependency change;
- adversarial event;
- failure or recovery state.

Regime shift does not automatically invalidate everything.

It triggers **dependency-aware revalidation**.

---

# 14. Temporal Dimensions

L5 MUST distinguish multiple kinds of time.

At minimum:

```yaml
TemporalState:
  event_time: ...
  observation_time: ...
  source_publication_time: ...
  ingestion_time: ...
  retrieval_time: ...
  reasoning_time: ...
  decision_time: ...
  authorization_time: ...
  execution_time: ...
  commit_time: ...
  revalidation_time: ...
```

These timestamps are not interchangeable.

---

# 15. Event Time vs Observation Time

`event_time` means when the underlying event occurred.

`observation_time` means when it was observed or recorded.

Therefore:

```text
EVENT_TIME != OBSERVATION_TIME
```

Example:

```text
event occurred: T1
sensor recorded: T2
database ingested: T3
agent retrieved: T4
decision made: T5
```

Reasoning that collapses these timestamps may infer false ordering, freshness, or causality.

---

# 16. Publication Time vs Evidence Time

A source published at `T2` may describe evidence collected at `T1`.

Therefore:

```text
PUBLICATION_TIME != EVIDENCE_TIME
```

A recently published document may contain old evidence.

Likewise, an older source may still describe a stable invariant.

Freshness cannot be inferred from publication date alone.

---

# 17. Retrieval Time vs Validity Time

A claim retrieved now is not necessarily valid now.

```text
RETRIEVED_NOW != VALID_NOW
```

Retrieval establishes availability, not current applicability.

L5 requires evaluation of the underlying evidence and regime.

---

# 18. Decision Time vs Commit Time

A decision may be formed at `T_decision`.

Execution may occur at `T_commit`.

If relevant state changes between them:

```text
State(T_decision) != State(T_commit)
```

then the decision may require revalidation.

Therefore:

```text
VALID_AT_DECISION
!=
AUTOMATICALLY_VALID_AT_COMMIT
```

This is particularly important for consequential or irreversible actions.

---

# 19. Temporal Validity Window

Claims MAY have an explicit validity window:

```yaml
validity_window:
  valid_from: ...
  valid_until: ...
  revalidate_after: ...
  expiration_basis: ...
```

A validity window may be:

- source-defined;
- policy-defined;
- model-derived;
- event-triggered;
- unknown.

AMOS MUST preserve which one applies.

---

# 20. Freshness

Freshness describes whether evidence or state remains sufficiently current for its intended use.

Freshness is task-dependent.

There is no universal rule such as:

```text
older than X days = stale
```

unless a domain or policy explicitly establishes that threshold.

A conceptual freshness record:

```yaml
FreshnessState:
  observed_at: ...
  retrieved_at: ...
  expected_change_rate: ...
  last_revalidated: ...
  invalidation_events: [...]
  freshness_status:
    - CURRENT
    - AGING
    - STALE
    - UNKNOWN
```

---

# 21. Freshness Law

Freshness MUST be evaluated relative to:

```text
claim
× domain
× decision
× regime
× expected change rate
```

For example, a mathematical definition may remain valid for decades while a live market quote may become stale within seconds.

Therefore:

```text
FRESHNESS IS RELATIONAL,
NOT ABSOLUTE.
```

---

# 22. Expiration Law

Expiration occurs when a claim crosses a defined temporal boundary or when an invalidating event occurs.

Conceptually:

```text
Expired(C)
=
TimeExpired(C)
OR
InvalidatingEventOccurred(C)
OR
RegimeChanged(C)
OR
DependencyChanged(C)
```

Expiration SHOULD normally trigger:

```text
REVALIDATE
```

rather than immediate deletion.

---

# 23. Event-Driven Invalidity

Some claims remain valid indefinitely until a particular event occurs.

Example:

```yaml
valid_until_event:
  - policy_revoked
  - model_replaced
  - authority_revoked
  - dependency_version_changed
  - source_retracted
```

Thus temporal validity is not always calendar-based.

---

# 24. Scope–Regime Coupling

Scope and regime are separate but may interact.

A population may remain constant while its operating regime changes.

A regime may remain constant while the relevant population changes.

Therefore:

```text
SCOPE != REGIME
```

Yet:

```text
Validity = f(scope, regime, ...)
```

may depend on both.

AMOS MUST NOT collapse them into a single generic context field when their distinction matters.

---

# 25. Temporal–Regime Coupling

Time passing alone does not necessarily create a regime change.

Likewise, a regime can change almost instantaneously.

Therefore:

```text
ΔTIME != REGIME_SHIFT
```

and:

```text
REGIME_SHIFT != LARGE_ΔTIME
```

A regime transition requires evidence of validity-relevant structural or contextual change.

---

# 26. Scope–Temporal Coupling

Scope may change over time.

Examples:

- a policy expands to new jurisdictions;
- software deployment reaches more users;
- an experiment moves to another population;
- a model's supported domain changes.

Therefore scope SHOULD be versioned or temporally bound when material.

Conceptually:

```text
Scope(C, T1) != Scope(C, T2)
```

may be true even if the claim text remains identical.

---

# 27. Typed Inputs

L5 MAY consume:

```yaml
L5Input:
  claim: Claim
  claim_class: EpistemicClass

  scope: ScopeEnvelope | UNKNOWN
  regime: RegimeState | UNKNOWN

  temporal:
    event_time: Timestamp | UNKNOWN
    observation_time: Timestamp | UNKNOWN
    publication_time: Timestamp | UNKNOWN
    retrieval_time: Timestamp | UNKNOWN
    decision_time: Timestamp | UNKNOWN
    commit_time: Timestamp | UNKNOWN

  scale: H | M | L | CROSS_SCALE | UNKNOWN

  measurement_context: MeasurementContext | UNKNOWN
  observer_context: ObserverContext | UNKNOWN

  dependencies: ClaimRef[]
  assumptions: AssumptionRef[]
  evidence: EvidenceRef[]
  provenance: ProvenanceRef[]

  requested_target_scope: ScopeEnvelope | null
  requested_target_regime: RegimeState | null
  requested_target_time: Timestamp | null
```

---

# 28. Typed Outputs

```yaml
L5Assessment:
  claim_id: ClaimID

  applicability:
    scope_status:
      - VALID
      - CONDITIONAL
      - OUT_OF_SCOPE
      - UNKNOWN

    regime_status:
      - VALID
      - CONDITIONAL
      - REGIME_MISMATCH
      - TRANSITION
      - UNKNOWN

    temporal_status:
      - CURRENT
      - AGING
      - STALE
      - EXPIRED
      - UNKNOWN

  effective_scope: ScopeEnvelope
  effective_regime: RegimeState
  validity_window: TemporalWindow

  transfer_status:
    - TRANSFER_SUPPORTED
    - TRANSFER_CONDITIONAL
    - TRANSFER_REJECTED
    - TRANSFER_UNKNOWN

  revalidation_required: boolean

  dependencies: ClaimRef[]
  evidence: EvidenceRef[]
  provenance: ProvenanceRef[]
  competing: [...]
  falsifiers: [...]
  confidence_ceiling: float
```

---

# 29. State Variables

Conceptual L5 state MAY include:

```yaml
l5_state:
  active_scope: S
  target_scope: S_target

  active_regime: R
  previous_regime: R_prev
  candidate_regime: R_candidate

  current_time: T
  evidence_time: T_e
  observation_time: T_o
  decision_time: T_d
  commit_time: T_c

  freshness_state: F

  scale_state: K
  observer_state: O
  measurement_state: M

  transition_state: X
  revalidation_state: V
  invalidation_state: I

  provenance_state: P
  dependency_state: D
```

These are conceptual contract variables and do not themselves prove implementation.

---

# 30. Operators

Minimum L5 operator family:

```text
DEFINE_SCOPE
BOUND_SCOPE
INTERSECT_SCOPE
EXPAND_SCOPE
CONTRACT_SCOPE
COMPARE_SCOPE
TRANSFER_SCOPE

DEFINE_REGIME
DETECT_REGIME
COMPARE_REGIME
TRANSITION_REGIME
TRANSFER_REGIME

STAMP_EVENT_TIME
STAMP_OBSERVATION_TIME
STAMP_RETRIEVAL_TIME
STAMP_DECISION_TIME
STAMP_COMMIT_TIME

ASSESS_FRESHNESS
EXPIRE
REVALIDATE
INVALIDATE_STALE
QUARANTINE_STALE

MAP_SCALE
TRANSFER_SCALE

CHECK_OBSERVER_COMPATIBILITY
CHECK_MEASUREMENT_COMPATIBILITY

BUILD_APPLICABILITY_ENVELOPE
VALIDATE_APPLICABILITY
```

Operators proposing a broader validity envelope MUST NOT themselves authorize promotion.

---

# 31. Applicability Envelope

For important claims, AMOS SHOULD construct:

```yaml
ApplicabilityEnvelope:
  claim_id: ...

  scope:
    system: ...
    population: ...
    environment: ...
    geography: ...
    domain: ...

  scale:
    level: ...

  regime:
    id: ...
    defining_conditions: [...]

  temporal:
    valid_from: ...
    valid_until: ...
    evidence_time: ...
    observation_time: ...
    last_revalidated: ...

  observer:
    context: ...

  measurement:
    method: ...

  assumptions: [...]
  exclusions: [...]
  dependencies: [...]
  provenance: [...]

  status: ...
```

This envelope travels with the claim.

---

# 32. Context Stripping Prohibition

A downstream system MUST NOT reduce:

```yaml
claim: X
scope: S1
regime: R1
valid_until: T1
class: CONDITIONAL
```

to:

```text
X
```

and treat it as unconditional knowledge.

That transformation constitutes validity-context loss.

Therefore:

```text
CONTEXT_STRIPPING = INTEGRITY_RISK
```

---

# 33. H/M/L Applicability

## H — Governing / System Scale

At H, L5 governs:

- global system boundaries;
- institution-wide regimes;
- ecosystem conditions;
- strategic horizons;
- policy eras;
- broad authority domains;
- systemic regime transitions.

Example:

```text
organization operating normally
→ organization under emergency governance
```

may constitute an H-level regime shift.

---

## M — Subsystem Scale

At M, L5 governs:

- subsystem operating modes;
- workflow regimes;
- service boundaries;
- team or component scopes;
- model deployment contexts;
- intermediate time horizons.

A subsystem may enter a different regime while the H-level system remains nominal.

---

## L — Local Scale

At L, L5 governs:

- individual observations;
- transactions;
- requests;
- local states;
- sensor readings;
- single actions;
- short-lived evidence.

L-level evidence can become stale rapidly even while H-level structural conditions remain stable.

---

# 34. Cross-Scale Applicability

A claim established at one scale does not automatically transfer to another.

```text
VALID_L != VALID_M
VALID_M != VALID_H
VALID_H != VALID_L
```

Transfer requires an explicit aggregation, decomposition, or cross-scale mapping rule.

For example:

```text
many local observations
```

do not automatically prove:

```text
system-wide law
```

Similarly:

```text
system-wide average
```

does not automatically describe:

```text
every local entity
```

---

# 35. Cross-Domain Applicability

Structural similarity across domains does not establish transferability.

```text
VALID_IN_DOMAIN_A
+
SIMILAR_STRUCTURE_IN_DOMAIN_B
!=
VALID_IN_DOMAIN_B
```

Cross-domain application remains `MODEL` or `CONDITIONAL` until independently supported.

This protects AMOS fractal and cross-architecture reasoning from empirical overreach.

---

# 36. Scope Inheritance Through RSCF

If:

```text
C depends on P1, P2, P3
```

then `C` inherits the relevant applicability constraints of its load-bearing premises.

Conceptually:

```text
Scope(C)
⊆
Intersection(
  Scope(P1),
  Scope(P2),
  Scope(P3)
)
```

and:

```text
TemporalValidity(C)
≤
weakest load-bearing temporal validity
```

unless independently revalidated.

---

# 37. Regime Inheritance Through RSCF

If a premise is only valid in `R1`, a dependent conclusion cannot silently become regime-independent.

Example:

```text
P1 valid only in LOW_VOLATILITY
P2 regime-independent
C depends on P1 and P2
```

then:

```text
C inherits LOW_VOLATILITY applicability
```

unless another proof supports broader validity.

---

# 38. Temporal Inheritance Through RSCF

A derived claim cannot normally be fresher than its load-bearing evidence merely because it was computed recently.

Therefore:

```text
DERIVATION_TIME != EVIDENCE_FRESHNESS
```

A report generated today from stale evidence remains bounded by that stale evidence.

---

# 39. Provenance and Applicability

L5 applicability claims require provenance.

For example:

```yaml
applicability_provenance:
  scope_source: ...
  regime_source: ...
  temporal_source: ...
  freshness_source: ...
  measurement_source: ...
  assumptions_source: ...
```

If scope is inferred rather than source-defined:

```yaml
scope_class: DERIVED
```

should be preserved.

If regime is model-estimated:

```yaml
regime_class: MODEL
```

should be preserved.

---

# 40. Confidence Ceiling

L5 imposes an applicability confidence ceiling.

Conceptually:

```text
C_applicability
≤
min(
  C_scope,
  C_regime,
  C_temporal,
  C_freshness,
  C_measurement,
  C_observer,
  C_dependency,
  C_provenance
)
```

This is an AMOS governance model.

If scope is unknown:

```text
C_scope = bounded
```

If regime is uncertain:

```text
C_regime = bounded
```

Therefore the overall claim cannot be promoted as universally applicable.

---

# 41. Unknown Scope Law

When scope is unknown:

```yaml
scope: UNKNOWN
```

AMOS MUST NOT substitute:

```yaml
scope: UNIVERSAL
```

Correct handling is:

```text
UNKNOWN/GAP
```

or a bounded conditional conclusion.

---

# 42. Unknown Regime Law

When regime is unknown:

```text
REGIME = UNKNOWN
```

the system SHOULD determine whether regime materially affects the decision.

If yes:

```text
REVALIDATION / DISCRIMINATION REQUIRED
```

If no:

the claim may proceed only if regime-independence itself is supported.

---

# 43. Unknown Time Law

When evidence time is unavailable:

```text
EVIDENCE_TIME = UNKNOWN
```

freshness cannot be positively established.

Therefore:

```text
UNKNOWN_TIME != CURRENT
```

This may be a critical gap for fast-changing domains.

---

# 44. Gap Prioritization

L5 gaps SHOULD be classified:

```text
CRITICAL
DECISION_RELEVANT
EXPLANATORY
COSMETIC
```

Examples:

### Critical

Unknown regime for an irreversible high-impact action.

### Decision-Relevant

Unknown freshness where new information could flip the decision.

### Explanatory

Missing exact historical timestamp that does not change the conclusion.

### Cosmetic

Missing formatting metadata.

AMOS resolves them in that order.

---

# 45. Sensitivity Law

For consequential conclusions, L5 SHOULD identify the smallest applicability change capable of flipping the result.

Examples:

```text
Would the conclusion fail if evidence were 30 days older?

Would it fail in a stressed regime?

Would it fail outside population P1?

Would it fail under measurement method M2?

Would it fail at H instead of L?
```

If a small plausible shift flips the result:

```text
status = FRAGILE / CONDITIONAL
```

---

# 46. Transition State

AMOS SHOULD explicitly represent transitional regimes.

A system moving from `R1` to `R2` may temporarily satisfy neither stable model.

Therefore:

```text
TRANSITION != R1
TRANSITION != R2
```

and should not be forced into either classification when evidence indicates an unstable transition.

Possible state:

```yaml
regime:
  status: TRANSITION
  from: R1
  toward: R2
  confidence: ...
```

---

# 47. Regime Hysteresis

Some systems do not immediately return to their prior state when a triggering condition disappears.

Therefore a regime classifier MAY need to distinguish:

```text
ENTRY_THRESHOLD
```

from:

```text
EXIT_THRESHOLD
```

where domain evidence supports this behavior.

AMOS MUST NOT assume hysteresis universally.

This remains domain-specific.

---

# 48. Regime Uncertainty

Where multiple regime interpretations remain plausible:

```yaml
competing_regimes:
  - R1
  - R2
  - TRANSITION
```

AMOS SHOULD preserve:

```text
COMPETING
```

rather than arbitrarily selecting one.

The preferred next step is the cheapest high-information observation capable of discriminating among them.

---

# 49. Scope Conflict

Two sources may describe the same claim under different scopes.

Example:

```text
Source A: valid for P1
Source B: valid for P2
```

AMOS MUST NOT automatically merge them into:

```text
valid for P1 ∪ P2
```

unless compatibility is established.

They may represent:

- legitimate extension;
- conflicting evidence;
- different regimes;
- different measurements;
- different populations;
- provenance duplication.

---

# 50. Temporal Conflict

Evidence may disagree because it comes from different periods.

Example:

```text
E1 at T1 supports C
E2 at T2 contradicts C
```

This does not automatically imply one source is wrong.

Possible explanation:

```text
regime changed between T1 and T2
```

Therefore temporal alignment precedes contradiction collapse.

---

# 51. Apparent Contradiction Law

Before classifying two claims as contradictory, L5 SHOULD test:

```text
same scope?
same population?
same scale?
same regime?
same time?
same observer?
same measurement?
same assumptions?
```

If not, the claims may be context-separated rather than logically contradictory.

---

# 52. True Contradiction Preservation

If two claims remain incompatible after scope/regime/temporal normalization:

```text
CONTRADICTION = PRESERVE
```

until resolved.

L5 MUST NOT hide contradiction by silently changing scope.

---

# 53. Revalidation Triggers

Revalidation SHOULD occur when any load-bearing validity condition changes.

Triggers include:

```yaml
revalidation_triggers:
  - scope_expansion
  - scope_contraction_affecting_claim
  - regime_shift
  - temporal_expiration
  - stale_evidence
  - dependency_change
  - source_retraction
  - measurement_change
  - observer_change
  - policy_change
  - authority_change
  - model_version_change
  - environmental_change
  - population_shift
  - contradiction_discovered
```

---

# 54. Selective Revalidation

A change SHOULD invalidate only affected claims.

Conceptually:

```text
Changed(X)
→
FindClaimsDependingOn(X)
→
MarkForRevalidation(descendants)
```

not:

```text
Changed(X)
→
InvalidateEverything
```

This preserves unaffected validated state.

---

# 55. Revalidation State Machine

A conceptual state machine:

```text
VALID
  ↓ trigger
REVALIDATION_REQUIRED
  ↓
UNDER_REVIEW
  ├── evidence still supports → VALID
  ├── narrower applicability → CONDITIONAL
  ├── unresolved → QUARANTINED
  └── contradicted → INVALID
```

This is a governance model, not a claim of current implementation.

---

# 56. Stale-State Quarantine

Stale evidence need not be deleted.

Instead:

```text
CURRENT
→
AGING
→
STALE
→
QUARANTINED
```

where appropriate.

Quarantine preserves:

- history;
- provenance;
- replay;
- comparison;
- regime reconstruction.

But quarantined evidence MUST NOT silently support current high-confidence conclusions.

---

# 57. Historical Validity

A stale claim may remain historically valid.

Example:

```text
Policy P was active in 2024.
```

may remain a valid historical statement in 2026 even though the policy is no longer active.

Thus:

```text
STALE_FOR_CURRENT_DECISION
!=
FALSE_HISTORICALLY
```

Temporal reasoning must preserve this distinction.

---

# 58. Future Validity

Future claims require explicit predictive or scheduled status.

```text
VALID_FROM: T_future
```

does not mean valid now.

Likewise:

```text
EXPECTED_AT_T_future
```

is a forecast unless guaranteed by an authoritative deterministic mechanism.

Therefore:

```text
FUTURE_EXPECTATION != CURRENT_FACT
```

---

# 59. Retroactive Change

Some rules or authoritative decisions may explicitly have retroactive scope.

AMOS MUST NOT assume retroactivity.

Required representation:

```yaml
temporal_effect:
  effective_from: ...
  announced_at: ...
  retroactive: true | false
  authority: ...
```

Without explicit evidence:

```text
RETROACTIVE = FALSE / UNKNOWN
```

according to the domain contract.

---

# 60. Control-Plane Requirements

An L5-conformant control plane SHOULD support:

```yaml
control_plane_requirements:

  scope_validation: required
  regime_validation: required
  temporal_validation: required
  freshness_validation: required

  event_time_tracking: required_when_material
  observation_time_tracking: required_when_material
  decision_time_tracking: required_for_governed_actions
  commit_time_tracking: required_for_governed_actions

  applicability_provenance: required
  dependency_linkage: required

  regime_shift_detection: required_where_regime_sensitive
  stale_state_detection: required_where_freshness_sensitive

  selective_invalidation: required
  revalidation: required

  authority_recheck:
    required_when_authority_state_can_change

  commit_time_revalidation:
    required_for_consequential_mutable_state
```

Again:

```text
CONTRACT_REQUIREMENT != IMPLEMENTED_FEATURE
```

until runtime evidence exists.

---

# 61. Commit-Time Law

For governed actions:

```text
PROPOSAL_TIME
<
DECISION_TIME
≤
COMMIT_TIME
```

may involve changing state.

Therefore a commit gate SHOULD verify:

```text
scope still valid?
regime still valid?
evidence still fresh?
dependencies unchanged?
authority still valid?
constraints unchanged?
target state unchanged materially?
```

If a load-bearing condition changed:

```text
COMMIT = BLOCK / REVALIDATE
```

rather than executing stale intent.

---

# 62. Authority Scope Law

Authority itself has scope and time.

An authority witness SHOULD specify:

```yaml
authority_scope:
  principal: ...
  action_types: [...]
  resources: [...]
  recipients: [...]
  environment: ...
  valid_from: ...
  valid_until: ...
  revocation_state: ...
```

Therefore:

```text
AUTHORIZED_FOR_A
!=
AUTHORIZED_FOR_B
```

and:

```text
AUTHORIZED_AT_T1
!=
AUTHORIZED_AT_T2
```

after expiry or revocation.

---

# 63. Capability Scope Law

Capabilities may also be context-dependent.

```text
CAPABILITY_EXISTS
```

does not mean:

```text
CAPABILITY_VALID_IN_ALL_ENVIRONMENTS
```

A Skill may function in one runtime and fail in another.

Therefore capability manifests SHOULD declare environment and regime assumptions.

---

# 64. Proposal Scope Law

A proposal is scoped to the state from which it was generated.

If target conditions materially change:

```text
Proposal(P, State1)
```

cannot automatically become:

```text
Commit(P, State2)
```

without validation.

Thus:

```text
PROPOSAL != COMMIT
```

remains an L5 temporal integrity boundary as well as a governance boundary.

---

# 65. Agent Requirements

An agent operating under L5 SHOULD determine:

1. What system is being discussed?
2. Which population/entities are included?
3. What is excluded?
4. At what scale?
5. Under which regime?
6. At what time?
7. When was evidence observed?
8. When was it retrieved?
9. How quickly can the state change?
10. Has a regime shift occurred?
11. Are measurements compatible?
12. Does the requested conclusion exceed source scope?
13. Does action occur later than reasoning?
14. Is revalidation required before commit?

The agent SHOULD answer at the narrowest scope justified by evidence.

---

# 66. Skill Requirements

Skills producing consequential outputs SHOULD expose applicability metadata where material.

Example:

```yaml
skill_applicability:
  supported_domains: [...]
  unsupported_domains: [...]
  supported_scales: [...]
  required_regimes: [...]
  freshness_requirements: [...]
  environment_requirements: [...]
  assumptions: [...]
  authority_requirements: [...]
```

A Skill must not imply universal applicability merely because it is addressable by the system.

```text
ADDRESSABLE != VALIDATED
```

---

# 67. Workflow

Canonical conceptual L5 workflow:

```text
1. RECEIVE CLAIM / REQUEST
2. IDENTIFY TARGET DECISION
3. RESOLVE SYSTEM / POPULATION
4. RESOLVE SCOPE
5. RESOLVE SCALE
6. RESOLVE REGIME
7. RESOLVE EVENT TIME
8. RESOLVE OBSERVATION TIME
9. RESOLVE EVIDENCE TIME
10. ASSESS FRESHNESS
11. CHECK MEASUREMENT CONTEXT
12. CHECK OBSERVER CONTEXT
13. LOAD DEPENDENCIES
14. LOAD PROVENANCE
15. TEST SCOPE COMPATIBILITY
16. TEST REGIME COMPATIBILITY
17. TEST TEMPORAL COMPATIBILITY
18. TEST CROSS-SCALE TRANSFER
19. IDENTIFY COMPETING INTERPRETATIONS
20. RUN SENSITIVITY CHECK
21. BUILD APPLICABILITY ENVELOPE
22. APPLY CONFIDENCE CEILING
23. CLASSIFY RESULT
24. IF ACTION → RECHECK AT COMMIT
25. RECORD VALIDITY / REVALIDATION CONDITIONS
```

---

# 68. Protocol

A minimal L5 protocol:

```yaml
APPLICABILITY_REQUEST:
  claim: ...
  target_scope: ...
  target_regime: ...
  target_time: ...
  target_scale: ...

APPLICABILITY_CONTEXT:
  source_scope: ...
  source_regime: ...
  evidence_time: ...
  observation_time: ...
  measurement_context: ...
  dependencies: [...]
  provenance: [...]

APPLICABILITY_ASSESSMENT:
  scope_status: ...
  regime_status: ...
  temporal_status: ...
  freshness_status: ...
  transfer_status: ...
  confidence_ceiling: ...

APPLICABILITY_DECISION:
  valid_scope: ...
  valid_regime: ...
  validity_window: ...
  exclusions: [...]
  revalidation_conditions: [...]
  gaps: [...]
```

---

# 69. Interaction with L0 Integrity

L0 supplies the governing requirement that validity context cannot be discarded for convenience.

L5 operationalizes that requirement across:

- scope;
- regime;
- time;
- scale;
- observer;
- measurement.

If fluency requires removing qualifiers that are load-bearing to correctness:

```text
INTEGRITY > FLUENCY
```

The qualifiers remain.

---

# 70. Interaction with L1 Epistemic

L1 identifies what kind of knowledge a claim represents.

L5 determines where and when that epistemic status applies.

Example:

```yaml
claim_class: VERIFIED
scope: S1
regime: R1
```

does NOT mean:

```yaml
claim_class: VERIFIED
scope: UNIVERSAL
regime: ALL
```

Thus epistemic class and applicability are orthogonal dimensions.

---

# 71. Interaction with L2 Provenance

L2 establishes origin and ancestry.

L5 uses that provenance to determine:

- evidence date;
- measurement context;
- source scope;
- source regime;
- supersession;
- retraction;
- version.

Without provenance, applicability may become impossible to reconstruct.

---

# 72. Interaction with L3 Dependency

L3 establishes which claims depend on which premises.

L5 uses the dependency graph to propagate applicability constraints.

If:

```text
C → depends on P
```

and:

```text
P valid only in R1
```

then `C` cannot silently become regime-independent.

---

# 73. Interaction with L4 Causal

L4 determines whether causal strength is warranted.

L5 determines whether the causal conclusion applies to the requested:

- population;
- environment;
- regime;
- time;
- scale.

Therefore:

```text
CAUSALLY_SUPPORTED
!=
UNIVERSALLY_APPLICABLE
```

A causal result may be valid yet narrowly scoped.

---

# 74. Interaction with RSCF

L5 SHOULD be embedded directly in RSCF capsules.

```yaml
rscf:
  claim: ...
  claim_class: ...
  evidence: [...]
  provenance: [...]

  scope:
    system: ...
    population: ...
    environment: ...
    scale: ...

  regime:
    id: ...
    conditions: [...]

  freshness:
    evidence_time: ...
    last_revalidated: ...
    status: ...

  dependencies: [...]
  competing: [...]
  falsifiers: [...]
  confidence_ceiling: ...
```

RSCF reuse is permitted only while these validity dimensions remain compatible.

---

# 75. RSCF Reuse Law

A stored proof capsule MAY be reused when:

```text
dependency closure valid
AND provenance valid
AND scope compatible
AND regime compatible
AND freshness sufficient
AND no material contradiction
```

Otherwise:

```text
REUSE = BLOCKED / CONDITIONAL / REVALIDATE
```

This is central to AMOS fast-path reasoning.

---

# 76. Fast-Path Applicability

Local reuse may avoid expensive global reasoning when:

```text
ScopeCompatible = TRUE
RegimeCompatible = TRUE
FreshEnough = TRUE
DependenciesValid = TRUE
ProvenanceValid = TRUE
ConflictFree = TRUE
```

If these conditions cannot be established, AMOS escalates rather than assuming them.

Thus:

```text
FAST_PATH != LOWER_INTEGRITY_PATH
```

---

# 77. Interaction with Memory

Memory MUST preserve applicability qualifiers.

A memory such as:

```text
"Model X performs well."
```

is insufficient if the original evidence actually meant:

```yaml
claim: Model X performs well
benchmark: B1
dataset: D1
version: V1
hardware: H1
time: T1
regime: R1
```

Retrieval SHOULD restore the relevant envelope.

Otherwise memory introduces scope pollution.

---

# 78. Interaction with Canon

Canon statements may themselves have:

- version scope;
- subsystem scope;
- effective date;
- supersession date;
- applicability conditions.

A later canon revision MUST NOT silently rewrite historical canon provenance.

Instead preserve:

```text
V1 valid during T1
V2 supersedes V1 at T2
```

where supported.

---

# 79. Supersession Law

Supersession is explicit.

```yaml
supersession:
  prior_artifact: ...
  successor_artifact: ...
  effective_at: ...
  scope: ...
  reason: ...
  provenance: ...
```

The existence of a newer artifact does not automatically establish complete replacement.

Possible relations include:

```text
SUPERSEDES
PARTIALLY_SUPERSEDES
EXTENDS
CORRECTS
DEPRECATES
COEXISTS
```

---

# 80. Version Law

Version identity forms part of scope.

```text
System V1 != System V2
```

for reasoning whenever the version change modifies load-bearing behavior.

Benchmark, implementation, policy, or causal claims tied to V1 cannot automatically transfer to V2.

---

# 81. Environment Law

Execution claims inherit environment conditions.

Relevant dimensions MAY include:

```yaml
environment:
  runtime: ...
  operating_system: ...
  dependency_versions: [...]
  hardware: ...
  configuration: ...
  network_state: ...
  permissions: ...
```

Therefore:

```text
PASSED_IN_ENV_A
!=
PASSED_IN_ENV_B
```

until compatibility is demonstrated.

---

# 82. Benchmark Applicability

Benchmark evidence is scoped to:

- benchmark definition;
- dataset;
- model/system version;
- harness;
- environment;
- seed where applicable;
- evaluation protocol;
- time;
- metric.

Therefore:

```text
BENCHMARK_PASS
!=
UNIVERSAL_CAPABILITY
```

and:

```text
BENCHMARK_SUCCESS
!=
DEPLOYMENT_VALIDITY
```

without transfer evidence.

---

# 83. Policy Applicability

Policy rules SHOULD specify:

```yaml
policy_applicability:
  subjects: [...]
  actions: [...]
  resources: [...]
  jurisdiction: ...
  environment: ...
  valid_from: ...
  valid_until: ...
  exceptions: [...]
  precedence: ...
```

A policy outside its applicability scope must not be invoked as authority.

---

# 84. Failure Modes

L5 recognizes at least the following failures.

### F1 — Scope Leakage

A narrow claim becomes broader without evidence.

### F2 — Regime Leakage

A claim valid in one regime is reused in another.

### F3 — Temporal Leakage

Historical evidence is treated as current.

### F4 — Freshness Fabrication

Unknown evidence age is treated as fresh.

### F5 — Scale Leakage

Local evidence becomes system-wide law.

### F6 — Population Leakage

Results for one population are generalized to another.

### F7 — Environment Leakage

Runtime evidence transfers across incompatible environments.

### F8 — Measurement Leakage

Results from one measurement method are treated as equivalent to another.

### F9 — Observer Collapse

Observer-specific evidence is treated as observer-independent.

### F10 — Publication/Freshness Confusion

Recent publication is treated as recent evidence.

### F11 — Retrieval/Freshness Confusion

Recently retrieved information is treated as current information.

### F12 — Decision/Commit Drift

Execution uses assumptions that changed after the decision.

### F13 — Version Leakage

Evidence from V1 is applied to V2 without validation.

### F14 — Transition Misclassification

A transitional state is forced into a stable regime.

### F15 — Unknown-to-Universal Promotion

Missing applicability metadata becomes universal applicability.

### F16 — Stale Memory Reuse

Stored conclusions are reused after their validity envelope expires.

### F17 — Scope-Based Contradiction Erasure

A real contradiction is hidden by inventing different scopes.

### F18 — False Contradiction

Claims from legitimately different regimes are treated as mutually exclusive.

---

# 85. Repair and Recovery

L5 recovery follows:

```text
DETECT APPLICABILITY FAILURE
        ↓
IDENTIFY AFFECTED DIMENSION
        ↓
SCOPE / REGIME / TIME / SCALE / MEASUREMENT
        ↓
TRACE DEPENDENCIES
        ↓
FREEZE AFFECTED PROMOTIONS
        ↓
PRESERVE UNAFFECTED CLAIMS
        ↓
RECONSTRUCT APPLICABILITY ENVELOPE
        ↓
REVALIDATE
        ↓
RESTORE / NARROW / QUARANTINE / INVALIDATE
```

Repair SHOULD be selective.

---

# 86. Scope Repair

If a claim is overgeneralized:

```text
C valid universally
```

but evidence supports only:

```text
C valid in S1
```

repair SHOULD narrow the claim:

```text
UNIVERSAL
→
S1
```

rather than deleting valid S1 evidence.

---

# 87. Regime Repair

If evidence is discovered to apply only to `R1`:

```text
regime: ALL
```

becomes:

```text
regime: R1
```

Dependent conclusions must then be re-evaluated.

---

# 88. Temporal Repair

If freshness cannot be established:

```text
CURRENT
```

must be downgraded to:

```text
UNKNOWN
```

or:

```text
STALE
```

depending on evidence.

No invented timestamp may be inserted merely to complete the schema.

---

# 89. Validators

Conceptual L5 validators include:

```text
validate_scope()
validate_scope_inheritance()
validate_scope_transfer()

validate_regime()
validate_regime_transition()
validate_regime_transfer()

validate_event_time()
validate_observation_time()
validate_evidence_time()
validate_decision_time()
validate_commit_time()

validate_freshness()
validate_validity_window()

validate_scale()
validate_cross_scale_transfer()

validate_measurement_context()
validate_observer_context()

validate_version_compatibility()
validate_environment_compatibility()

validate_revalidation_trigger()
validate_applicability_envelope()
```

---

# 90. Minimum Tests

## Test 1 — Scope Leakage

Input:

```text
Evidence supports population P1.
Question asks about P1 + P2.
```

Expected:

```text
P2 = UNKNOWN/GAP
```

unless transfer evidence exists.

---

## Test 2 — Regime Shift

Input:

```text
Claim valid under R1.
System transitions to R2.
```

Expected:

```text
REVALIDATION_REQUIRED
```

where the claim is regime-sensitive.

---

## Test 3 — Freshness

Input:

```text
Evidence timestamp unknown.
Domain changes rapidly.
```

Expected:

```text
FRESHNESS = UNKNOWN
```

not `CURRENT`.

---

## Test 4 — Historical Validity

Input:

```text
Policy P was valid at T1 but revoked at T2.
```

Expected:

```text
historical claim = potentially valid
current authority = invalid
```

---

## Test 5 — Decision/Commit Drift

Input:

```text
decision made under State1
commit attempted under materially changed State2
```

Expected:

```text
COMMIT_BLOCKED_PENDING_REVALIDATION
```

---

## Test 6 — Cross-Scale Transfer

Input:

```text
local L observations support X
```

Expected:

```text
H-level universal conclusion not automatically licensed
```

---

## Test 7 — Context Preservation

Input stored as:

```yaml
claim: X
scope: S1
regime: R1
```

Expected retrieval:

```yaml
claim: X
scope: S1
regime: R1
```

not merely `X`.

---

## Test 8 — False Contradiction

Input:

```text
C true in R1
C false in R2
```

Expected:

```text
REGIME-CONDITIONAL DIFFERENCE
```

not necessarily logical contradiction.

---

## Test 9 — Unknown Scope

Input:

```text
scope metadata absent
```

Expected:

```text
scope = UNKNOWN
```

not `UNIVERSAL`.

---

## Test 10 — Version Transition

Input:

```text
benchmark passed V1
current system V2
```

Expected:

```text
TRANSFER_REQUIRES_VALIDATION
```

---

# 91. Falsifiers

An L5 applicability conclusion SHOULD expose conditions that would invalidate it.

Examples:

```yaml
falsifiers:
  - target population differs materially from validated population
  - operating regime changes
  - evidence becomes stale
  - measurement method changes
  - system version changes
  - source is superseded or retracted
  - authority expires
  - relevant dependency changes
  - environment changes materially
  - cross-scale transfer fails validation
  - hidden exclusion is discovered
  - temporal ordering was incorrectly reconstructed
```

---

# 92. Invariants

## L5-I1 — Scope Required

```text
Consequential claims require explicit or explicitly UNKNOWN scope.
```

## L5-I2 — Unknown Is Not Universal

```text
UNKNOWN_SCOPE != UNIVERSAL_SCOPE
```

## L5-I3 — Regime Required

```text
Regime-sensitive claims require explicit or UNKNOWN regime.
```

## L5-I4 — Temporal Integrity

```text
EVENT_TIME
!=
OBSERVATION_TIME
!=
RETRIEVAL_TIME
!=
DECISION_TIME
!=
COMMIT_TIME
```

unless equality is actually established.

## L5-I5 — Freshness Integrity

```text
RECENT_RETRIEVAL != FRESH_EVIDENCE
```

## L5-I6 — Scope Inheritance

```text
Derived claims inherit load-bearing premise scope.
```

## L5-I7 — Regime Inheritance

```text
Derived claims inherit load-bearing premise regime constraints.
```

## L5-I8 — Temporal Inheritance

```text
New derivation does not reset old evidence age.
```

## L5-I9 — Scale Firewall

```text
LOCAL_VALIDITY != SYSTEM_VALIDITY
```

## L5-I10 — Cross-Domain Firewall

```text
STRUCTURAL_SIMILARITY != TRANSFER_VALIDATION
```

## L5-I11 — Selective Invalidation

```text
Applicability failure invalidates affected descendants,
not unrelated claims.
```

## L5-I12 — Commit Freshness

```text
Consequential commit requires current load-bearing state.
```

## L5-I13 — Authority Temporality

```text
PAST_AUTHORITY != CURRENT_AUTHORITY
```

## L5-I14 — Version Integrity

```text
V1_EVIDENCE != V2_VALIDATION
```

## L5-I15 — Placeholder Boundary

```text
ADDRESSABLE != VALIDATED
```

---

# 93. Hard Boundaries

```text
VALID_HERE != VALID_EVERYWHERE

VALID_THEN != VALID_NOW

VALID_R1 != VALID_R2

VALID_L != VALID_M != VALID_H

UNKNOWN_SCOPE != UNIVERSAL_SCOPE

UNKNOWN_REGIME != ALL_REGIMES

UNKNOWN_TIME != CURRENT

RETRIEVED_NOW != OBSERVED_NOW

PUBLICATION_TIME != EVIDENCE_TIME

DECISION_TIME != COMMIT_TIME

NEW_DERIVATION != NEW_EVIDENCE

BENCHMARK_PASS != UNIVERSAL_CAPABILITY

CAPABILITY != AUTHORITY

PAST_AUTHORITY != CURRENT_AUTHORITY

PROPOSAL != COMMIT

STRUCTURAL_SIMILARITY != TRANSFER_VALIDATION

UNKNOWN/GAP != PASS
```

---

# 94. Dependencies

Conceptual dependency spine:

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
      ↓
L5 SCOPE / REGIME / TEMPORAL
```

L5 relies particularly on:

- L0 for integrity;
- L1 for epistemic typing;
- L2 for provenance and freshness reconstruction;
- L3 for applicability propagation through dependencies;
- L4 for preserving the applicability envelope of causal conclusions.

L5 MUST NOT weaken earlier laws.

---

# 95. Downstream Requirements

Any later core law consuming L5-governed knowledge SHOULD preserve:

```text
scope
regime
time
freshness
scale
observer
measurement
dependencies
provenance
```

where material.

A downstream transformation that discards these fields must either prove they are irrelevant or explicitly record the loss.

---

# 96. Non-Purposes

L5 does NOT:

- claim that every system has discrete regimes;
- impose one universal freshness threshold;
- establish universal time constants;
- prove that H/M/L mappings are empirical laws;
- guarantee transfer between populations;
- replace domain-specific external validity analysis;
- replace statistical distribution-shift analysis;
- replace temporal causal inference;
- grant authority;
- execute actions;
- convert placeholders into implementation.

---

# 97. Evidence / Provenance Requirements

A mature L5 artifact SHOULD preserve source references for:

```yaml
evidence_requirements:
  scope_definition: source_or_explicit_model
  regime_definition: source_or_explicit_model
  timestamps: source_or_observation
  freshness_thresholds: source_or_policy
  transfer_rules: source_or_validated_model
  scale_mapping: source_or_explicit_model
  authority_window: authoritative_source
  version_mapping: source
```

Where source evidence does not exist:

```text
MODEL / UNKNOWN/GAP
```

must remain visible.

---

# 98. Gap Status

This document supplies a full structural proposal for `L5_SCOPE_REGIME.md`.

It does **not** establish that every law, schema, variable, operator, threshold, or workflow above already exists verbatim in approved Trang Phan source canon.

Current status:

```yaml
gap_status:
  structural_contract: PROVIDED
  scope_architecture: PROVIDED
  regime_architecture: PROVIDED
  temporal_architecture: PROVIDED
  freshness_architecture: PROVIDED
  hml_applicability: PROVIDED
  control_plane_contract: PROVIDED

  exact_source_canon_equivalence: UNVERIFIED
  empirical_validation: DOMAIN_DEPENDENT
  runtime_implementation: NOT_ESTABLISHED
  final_canon_approval: REQUIRED
```

Therefore:

```text
FULL_CONTENT != FINAL_CANON
```

---

# 99. RSCF Completion State

```yaml
claim_class: AMOS_MODEL

claim:
  "L5_SCOPE_REGIME defines the AMOS applicability firewall:
   consequential claims remain bounded by their supported scope,
   regime, temporal validity, freshness, scale, measurement context,
   dependencies, and provenance."

evidence:
  - AMOS governing architecture supplied by origin architect/steward
  - L0-L4 structural dependency spine
  - scope/regime/freshness requirements expressed in the AMOS operating contract

provenance:
  origin_architect: Trang Phan
  artifact_family: AMOS_OS
  layer: 01_CANON/01_CORE_LAWS
  path: 01_CANON/01_CORE_LAWS/L5_SCOPE_REGIME.md
  derivation_status: proposed_structural_completion

scope:
  system: AMOS
  applies_to:
    - claims
    - evidence
    - models
    - dependencies
    - causal relations
    - RSCFs
    - agents
    - skills
    - workflows
    - policies
    - authority
    - decisions
    - actions

regime:
  - reasoning
  - retrieval
  - memory
  - validation
  - governance
  - execution

freshness:
  revalidate_on:
    - canon_change
    - scope_change
    - regime_change
    - temporal_expiration
    - dependency_change
    - provenance_change
    - measurement_change
    - version_change
    - authority_change

dependencies:
  - L0_INTEGRITY
  - L1_EPISTEMIC
  - L2_PROVENANCE
  - L3_DEPENDENCY
  - L4_CAUSAL

competing:
  - some domains require continuous rather than discrete regime models
  - some claims may be genuinely time-invariant within their formal domain
  - some transfer rules require domain-specific external-validity methods
  - scope dimensions may differ by subsystem and cannot always be globally normalized

falsifiers:
  - a downstream claim exceeds source scope without transfer evidence
  - stale evidence is treated as current
  - a regime-sensitive claim survives a material regime shift without revalidation
  - event and observation time are incorrectly collapsed
  - local evidence is promoted to system-wide validity without support
  - unknown applicability is treated as universal
  - expired authority is treated as current authority
  - changed dependencies do not trigger selective revalidation

confidence_ceiling:
  structural_coherence: HIGH
  canon_equivalence: UNVERIFIED
  runtime_implementation: UNKNOWN
  empirical_validity: DOMAIN_DEPENDENT
```

---

# 100. Canon Promotion Gate

Before promotion to final canon:

```text
[ ] Trang Phan / steward approval
[ ] source-canon reconciliation
[ ] L0 compatibility confirmed
[ ] L1 compatibility confirmed
[ ] L2 compatibility confirmed
[ ] L3 compatibility confirmed
[ ] L4 compatibility confirmed
[ ] terminology normalized
[ ] scope schema reviewed
[ ] regime schema reviewed
[ ] temporal schema reviewed
[ ] freshness rules reviewed
[ ] H/M/L transfer rules reviewed
[ ] control-plane requirements reviewed
[ ] tests executed where implementation exists
[ ] contradictions preserved/resolved
[ ] downstream dependencies inspected
[ ] supersession lineage recorded
[ ] version assigned
```

Until promotion:

```text
STATUS = AMOS_MODEL / PROPOSED_CANON_CONTENT
```

not:

```text
STATUS = VERIFIED_FINAL_CANON
```

---

00_ROOT_MOC|AMOS MOC

---

**Related:** [[00_HOME]] · [[AMOS_RSCF_NODES]] · [[L0_INTEGRITY]] · [[L1_EPISTEMIC]] · [[L2_PROVENANCE]] · [[L3_DEPENDENCY]] · [[L4_CAUSAL]]

---

RSCF-NODE

node_id: l5_scope_regime

node_type: core_law

path: 01_CANON/01_CORE_LAWS/L5_SCOPE_REGIME.md

RSCF-RELATIONS:

- DEPENDS_ON: L0_INTEGRITY
- DEPENDS_ON: L1_EPISTEMIC
- DEPENDS_ON: L2_PROVENANCE
- DEPENDS_ON: L3_DEPENDENCY
- DEPENDS_ON: L4_CAUSAL
- INDEXED_BY: [[00_HOME]]
- INDEXED_BY: AMOS_RSCF_NODES

claim_class: AMOS_MODEL

```
```

---
**MOC:** [[01_CORE_LAWS_MOC]]
