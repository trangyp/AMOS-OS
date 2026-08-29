---
title: Vault Domain Knowledge — Amos Boundary Scope Master
type: reference
source: 07_SKILLS/amos-boundary-scope-master/references
tags:
- reference
- amos-boundary-scope-master
- type/skill
- skill
- validation
- amos-moc
- 00-home
- amos-rscf-nodes
- law/L0-integrity
- law/L1-epistemic
- law/L2-provenance
- law/L3-dependency
- l4-causal
- l5-scope-regime
- references-moc
rscf:
  state: SOURCE_CLAIM
  claim_class: SOURCE_CLAIM
  provenance: AMOS_corpus
  scope: skill_reference
---

# amos-boundary-scope-master — Vault-Sourced Domain Knowledge

> Load this reference only when detailed domain knowledge is needed.
> This content was moved from SKILL.md for progressive loading.

---

> **Source**: `01_CANON/01_CORE_LAWS/L5_SCOPE_REGIME.md` from the AMOS_OS Obsidian vault.
> This is substantive domain knowledge, not script-generated content.

```markdown
---
tags: ['canon', 'core_laws', 'scope', 'regime', 'temporal', 'freshness', 'applicability', 'rscf', 'governance']
title: L5 Scope, Regime, and Temporal Laws
origin_architect: "Trang Phan"
status: "AMOS_MODEL"
canon_status: "PROPOSED_CANON_CONTENT"
epistemic_class: "AMOS_MODEL"
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

* population compatibility;
* environmental compatibility;
* measurement compatibility;
* mechanism stability;
* regime compatibility;
* temporal compatibility;
* scale compatibility;
* provenance;
* assumptions;
* known exclusions;
* distribution shift.

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

* policy change;
* structural break;
* market transition;
* software deployment;
* architecture change;
* model update;
* population shift;
* sensor change;
* environmental change;
* authority change;
* dependency change;
* adversarial event;
* failure or recovery state.

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

* source-defined;
* policy-defined;
* model-derived;
* event-triggered;
* unknown.

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

* a policy expands to new jurisdictions;
* software deployment reaches more users;
* an experiment moves to another population;
* a model's supported domain changes.

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
  requested_targe


## Vault-Sourced Domain Content

> Source: `01_CANON/01_CORE_LAWS/L5_SCOPE_REGIME.md` (53632 bytes in vault)

### L5-L1 — Scope Preservation

```text
Every consequential conclusion inherits the scope
of its load-bearing premises unless broader scope
is independently established.
```

### F16 — Stale Memory Reuse

Stored conclusions are reused after their validity envelope expires.

### F17 — Scope-Based Contradiction Erasure

A real contradiction is hidden by inventing different scopes.

### Test 1 — Scope Leakage

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

### Test 7 — Context Preservation

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

### Test 9 — Unknown Scope

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

### L5-I1 — Scope Required

```text
Consequential claims require explicit or explicitly UNKNOWN scope.
```

### L5-I6 — Scope Inheritance

```text
Derived claims inherit load-bearing premise scope.
```

### L5-I10 — Cross-Domain Firewall

```text
STRUCTURAL_SIMILARITY != TRANSFER_VALIDATION
```

### L5-I15 — Placeholder Boundary

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

* L0 for integrity;
* L1 for epistemic typing;
* L2 for provenance and freshness reconstruction;
* L3 for applicability propagation through dependencies;
* L4 for preserving the applicability envelope of causal conclusions.

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

* claim that every system has discrete regimes;
* impose one universal freshness threshold;
* establish universal time constants;
* prove that H/M/L mappings are empirical laws;
* guarantee transfer between populations;
* replace domain-specific external validity analysis;
* replace statistical distribution-shift analysis;
* replace temporal causal inference;
* grant authority;
* execute actions;
* convert placeholders into implementation.

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

[[AMOS MOC]]

---

**Related:** [[00_HOME]] · [[AMOS_RSCF_NODES]] · [[L0_INTEGRITY]] · [[L1_EPISTEMIC]] · [[L2_PROVENANCE]] · [[L3_DEPENDENCY]] · [[L4_CAUSAL]]

---

RSCF-NODE

node_id: l5_scope_regime

node_type: core_law

path: 01_CANON/01_CORE_LAWS/[[L5_SCOPE_REGIME]].md

RSCF-RELATIONS:

* DEPENDS_ON: [[L0_INTEGRITY]]
* DEPENDS_ON: [[L1_EPISTEMIC]]
* DEPENDS_ON: [[L2_PROVENANCE]

... (truncated, see vault source for full content)

## Failure Modes

- **Insufficient evidence**: If source material is insufficient, mark as UNKNOWN/GAP and fail closed — do not fabricate.
- **Scope violation**: If the query falls outside the skill's declared scope, escalate to the parent skill or steward.
- **Binding broken**: If 1:1:1 binding (skill→agent→workflow) is broken, flag routing mismatch and block execution.
- **Validation failure**: If validation gates fail, downgrade confidence, flag the gap, and escalate — do not force-fit.
- **Epistemic overreach**: If a claim exceeds the established evidence or epistemic class, retract and relabel.

---
**MOC:** references_MOC
