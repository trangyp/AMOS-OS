---
title: vault domain knowledge
type: reference
tags: [reference, amos-information-theory-master]
---

# amos-information-theory-master — Vault-Sourced Domain Knowledge

> Load this reference only when detailed domain knowledge is needed.
> This content was moved from SKILL.md for progressive loading.

---

> **Source**: `01_CANON/01_CORE_LAWS/L6_UNCERTAINTY.md` from the AMOS_OS Obsidian vault.
> This is substantive domain knowledge, not script-generated content.

```markdown
---
tags: ['canon', 'core_laws', 'uncertainty', 'confidence', 'unknown', 'competing', 'rscf', 'governance']
title: "L6 Uncertainty Laws"
origin_architect: "Trang Phan"
updated: "2026-08-26"
status: "PROPOSED_SPECIFICATION"
epistemic_class: "AMOS_MODEL"
canonical_status: "CONDITIONAL"
implementation_status: "LOGIC_EXECUTABLE_IN_PART"
---

# L6 Uncertainty Laws

**Origin architect / steward:** Trang Phan  
**Layer:** `01_CANON / 01_CORE_LAWS / L6_UNCERTAINTY`  
**Artifact class:** `CORE_LAW_CONTRACT`  
**Status:** `PROPOSED_SPECIFICATION / AMOS_MODEL`  
**Canonical status:** `CONDITIONAL`  
**Implementation status:** `LOGIC_EXECUTABLE_IN_PART`

> L6 governs how AMOS represents, propagates, constrains, compares, reduces, preserves, and invalidates uncertainty.
>
> Uncertainty is part of the epistemic state of a claim. It must not be hidden merely to produce a complete, fluent, decisive, or convenient answer.

---

# 0. Status

This document is a proposed full structural specification for `L6_UNCERTAINTY.md`.

It expands the currently stated L6 seed:

```text
U-1 Typed Uncertainty
U-2 Confidence Ceiling
U-3 Ambiguity Preservation
U-4 Unknown Propagation
```

without claiming that every supporting operator, schema, threshold, validator, or runtime mechanism below is already final canon or fully implemented.

Hard distinction:

```text
SPECIFIED != IMPLEMENTED
IMPLEMENTED != VALIDATED
VALIDATED_LOCALLY != UNIVERSALLY_VALID
```

The supplied `0.95` hard confidence ceiling is retained as part of the proposed L6 specification, but remains conditional on authoritative epistemics canon not defining different semantics.

---

# 1. Purpose

L6 exists to make uncertainty:

* explicit;
* typed;
* scoped;
* dependency-aware;
* provenance-aware;
* regime-aware;
* temporally bounded;
* non-collapsible;
* selectively reducible;
* propagatable through RSCF;
* auditable by validators;
* actionable without fabrication.

The primary law is:

```text
UNCERTAINTY MUST REMAIN VISIBLE
UNTIL EVIDENCE LEGITIMATELY REDUCES IT.
```

L6 prevents the transformations:

```text
UNKNOWN → ASSUMED
```

```text
AMBIGUOUS → ARBITRARILY SELECTED
```

```text
COMPETING → AVERAGED
```

```text
WEAK EVIDENCE → HIGH CONFIDENCE
```

```text
MISSING EVIDENCE → PLAUSIBLE COMPLETION
```

```text
MODEL UNCERTAINTY → SOURCE CERTAINTY
```

and:

```text
CONFIDENCE → TRUTH
```

---

# 2. Core Uncertainty Contract

Every consequential AMOS claim SHOULD carry an uncertainty state sufficient to answer:

```text
What is uncertain?
Why is it uncertain?
What type of uncertainty is it?
Which premises create it?
How much does it matter?
Can it be reduced?
What evidence would reduce it?
What could increase it?
Can the decision proceed despite it?
What is the maximum confidence currently licensed?
```

Conceptually:

```text
Uncertainty(C)
=
U(
  evidence,
  provenance,
  model,
  scope,
  regime,
  temporal_state,
  causal_status,
  dependencies,
  measurement,
  execution_state
)
```

This is an **AMOS MODEL expression**, not a universal mathematical theorem.

---

# 3. Foundational Laws

## U-1 — Typed Uncertainty

Uncertainty MUST be classified before consequential use.

Minimum epistemic-origin classes:

```text
SOURCE
DERIVED
MODEL
UNKNOWN
```

The origin of uncertainty must remain distinguishable from the claim class itself.

Example:

```yaml
claim_class: DERIVED

uncertainty:
  source: LOW
  derivation: MEDIUM
  model: NONE
  unknown: PRESENT
```

A claim being `DERIVED` does not imply all uncertainty is derivational.

---

## U-2 — Confidence Ceiling

No claim may exceed the confidence licensed by its load-bearing evidence and dependencies.

Conceptually:

```text
Confidence(C)
≤
min(
  Confidence(P1),
  Confidence(P2),
  ...,
  Confidence(Pn)
)
```

for load-bearing premises unless the claim is independently revalidated through evidence that legitimately removes dependence on the weaker premise.

The proposed general hard ceiling is:

```text
Confidence(C) ≤ 0.95
```

absent stronger proof status recognized by the authoritative AMOS epistemics layer.

This ceiling is a **proposed AMOS governance convention**, not an empirical probability theorem.

Therefore:

```text
0.95 != 95% FREQUENTIST PROBABILITY
```

unless a specific calibrated statistical interpretation has been established.

---

## U-3 — Ambiguity Preservation

When alternatives are:

* incompatible;
* incomparable;
* differently scoped;
* supported by correlated evidence;
* insufficiently discriminated;
* approximately equally supported;

AMOS MUST preserve them as:

```text
COMPETING
```

rather than manufacture convergence.

Therefore:

```text
COMPETING(A, B)
!=
AVERAGE(A, B)
```

and:

```text
NO_WINNER
!=
50/50
```

unless a probabilistic model actually licenses that assignment.

---

## U-4 — Unknown Propagation

Operations requiring an unknown load-bearing input MUST:

```text
PROPAGATE UNKNOWN
```

or:

```text
FAIL CLOSED
```

when the missing input prevents justified computation.

Never:

```text
UNKNOWN
→
PLAUSIBLE VALUE
→
CONTINUE AS FACT
```

Thus:

```text
UNKNOWN/GAP != PASS
```

---

# 4. Additional Governing Laws

## U-5 — Confidence Is Not Evidence

```text
CONFIDENCE != EVIDENCE
```

A confidence value summarizes epistemic state. It does not create evidence.

Repeated confidence statements do not strengthen the underlying claim.

---

## U-6 — Confidence Is Not Truth

```text
HIGH_CONFIDENCE != VERIFIED_TRUTH
```

A highly confident claim may still be wrong.

Likewise:

```text
LOW_CONFIDENCE != FALSE
```

---

## U-7 — Repetition Does Not Reduce Uncertainty

```text
REPETITION != INDEPENDENT_CONFIRMATION
```

Multiple sources descended from one origin do not automatically reduce uncertainty.

---

## U-8 — Independence Must Be Demonstrated

Evidence aggregation may reduce uncertainty only when relevant independence assumptions are justified.

```text
MULTIPLE_SOURCES
!=
MULTIPLE_INDEPENDENT_SOURCES
```

---

## U-9 — Uncertainty Is Typed, Not Scalar-Only

A single number MUST NOT erase materially different uncertainty dimensions.

For consequential claims AMOS MAY track:

```text
evidence uncertainty
model uncertainty
scope uncertainty
temporal uncertainty
causal uncertainty
execution uncertainty
provenance-independence uncertainty
```

---

## U-10 — Uncertainty Reduction Requires Information

Uncertainty may not decrease merely because reasoning continued longer.

```text
MORE_REASONING != MORE_EVIDENCE
```

Legitimate reduction requires something such as:

* new evidence;
* stronger provenance;
* successful validation;
* discriminating observation;
* resolved dependency;
* narrowed scope;
* better measurement;
* successful execution test;
* formal proof where applicable.

---

## U-11 — Narrowing May Increase Confidence

A broad claim may be weak while a narrower claim is strong.

Therefore:

```text
UNCERTAIN_BROAD_CLAIM
```

may legitimately become:

```text
HIGHER_CONFIDENCE_NARROW_CLAIM
```

through scope contraction.

This is not fabrication if the narrower statement is independently supported.

---

## U-12 — Uncertainty Must Be Decision-Relevant

AMOS SHOULD distinguish uncertainty that can change a decision from uncertainty that cannot materially change it.

```text
DECISION_RELEVANT_UNCERTAINTY
>
EXPLANATORY_UNCERTAINTY
>
COSMETIC_UNCERTAINTY
```

for reasoning-resource allocation.

This ordering concerns priority, not truth value.

---

# 5. Uncertainty Vector

For consequential claims, L6 SHOULD support a multidimensional uncertainty representation.

Conceptually:

```text
U(C) =
[
  Ue,
  Um,
  Us,
  Ut,
  Uc,
  Ux,
  Up
]
```

where:

```text
Ue = evidence uncertainty
Um = model uncertainty
Us = scope uncertainty
Ut = temporal uncertainty
Uc = causal uncertainty
Ux = execution uncertainty
Up = provenance-independence uncertainty
```

This vector is an AMOS structural model.

It does not require every implementation to encode uncertainty numerically.

---

# 6. Evidence Uncertainty

Evidence uncertainty concerns the quality and completeness of evidence supporting a claim.

Sources include:

* missing observations;
* small samples;
* noisy measurements;
* incomplete records;
* conflicting observations;
* measurement error;
* unverified reports;
* indirect evidence.

Example:

```yaml
uncertainty:
  evidence:
    status: MATERIAL
    causes:
      - incomplete_observation
      - measurement_noise
```

---

# 7. Model Uncertainty

Model uncertainty concerns whether the selected representation or explanatory model is appropriate.

Examples:

* model misspecification;
* omitted variables;
* competing models;
* unstable parameters;
* approximation error;
* extrapolation;
* unvalidated assumptions.

Therefore:

```text
PRECISE_MODEL_OUTPUT
!=
LOW_MODEL_UNCERTAINTY
```

A model may output many decimal places while remaining epistemically weak.

---

# 8. Scope Uncertainty

Scope uncertainty concerns uncertainty over where a claim applies.

Examples:

```text
population unknown
environment mismatch
cross-domain transfer
cross-scale transfer
uncertain exclusions
measurement-context mismatch
```

L6 delegates applicability structure to `L5_SCOPE_REGIME`.

Therefore:

```text
UNKNOWN_SCOPE
→
SCOPE_UNCERTAINTY
```

not universal applicability.

---

# 9. Temporal Uncertainty

Temporal uncertainty concerns:

* unknown evidence age;
* uncertain event ordering;
* uncertain freshness;
* uncertain validity duration;
* delayed observations;
* possible regime transition.

Example:

```yaml
uncertainty:
  temporal:
    freshness: UNKNOWN
    event_time: KNOWN
    observation_time: KNOWN
```

Temporal uncertainty does not necessarily invalidate historical claims but may invalidate current-use claims.

---

# 10. Causal Uncertainty

Causal uncertainty concerns uncertainty over whether observed relationships represent:

* association;
* correlation;
* enabling condition;
* mediator;
* confounder;
* feedback;
* mechanism;
* necessary condition;
* sufficient condition;
* causal effect.

L6 MUST NOT resolve causal uncertainty merely through confidence language.

```text
HIGH_CONFIDENCE_CORRELATION
!=
CAUSAL_EFFECT
```

Causal typing remains governed by L4.

---

# 11. Execution Uncertainty

Execution uncertainty concerns whether a proposed operation will actually produce the expected result.

It includes:

* runtime uncertainty;
* environmental uncertainty;
* tool availability;
* dependency state;
* external-state mutation;
* concurrency;
* commit failure;
* implementation mismatch.

Therefore:

```text
LOGICALLY_VALID_PLAN
!=
SUCCESSFUL_EXECUTION
```

Execution evidence must remain separate from reasoning confidence.

---

# 12. Provenance-Independence Uncertainty

AMOS MUST track uncertainty about whether apparently separate evidence is genuinely independent.

Example:

```text
Source A
   ↓
Source B paraphrases A
   ↓
Source C summarizes B
```

must not be interpreted as:

```text
3 independent confirmations
```

The actual topology may contain only one origin.

Thus:

```text
COUNT(SOURCES)
!=
COUNT(INDEPENDENT_ORIGINS)
```

---

# 13. Typed Uncertainty State

A conceptual uncertainty object MAY be represented as:

```yaml
UncertaintyState:
  claim_id: ClaimID

  evidence:
    level: ...
    causes: [...]

  model:
    level: ...
    causes: [...]

  scope:
    level: ...
    causes: [...]

  temporal:
    level: ...
    causes: [...]

  causal:
    level: ...
    causes: [...]

  execution:
    level: ...
    causes: [...]

  provenance_independence:
    level: ...
    causes: [...]

  unknowns: [...]

  competing: [...]

  confidence_ceiling: ...

  decision_relevance: ...

  reducibility:
    reducible: true | false | unknown
    candidate_tests: [...]

  provenance: [...]
```

---

# 14. Qualitative Uncertainty Levels

Where numerical uncertainty is unsupported, AMOS SHOULD prefer explicit qualitative states.

Example:

```text
NONE_ESTABLISHED
LOW
MODERATE
HIGH
CRITICAL
UNKNOWN
```

These labels MUST NOT be silently interpreted as calibrated probabilities.

For example:

```text
HIGH UNCERTAINTY
```

does not mathematically mean:

```text
P(error) > 0.5
```

unless explicitly calibrated.

---

# 15. Numerical Confidence

Numerical confidence MAY be used only when its semantics are explicit.

A confidence object SHOULD specify:

```yaml
confidence:
  value: 0.72
  semantics: AMOS_EPISTEMIC_SCORE
  calibration: UNVALIDATED
  basis: [...]
  ceiling: 0.80
```

rather than simply:

```yaml
confidence: 0.72
```

when ambiguity would matter.

---

# 16. Confidence Ceiling Mechanics

For a conclusion `C` depending on premises:

```text
P1, P2, ..., Pn
```

the default AMOS ceiling is conceptually:

```text
Ceiling(C)
≤
min(
  Ceiling(P1),
  Ceiling(P2),
  ...,
  Ceiling(Pn)
)
```

for load-bearing dependencies.

This prevents:

```text
weak premise
+
strong premise
+
fluent synthesis
=
very strong conclusion
```

---

# 17. Independent Revalidation Exception

The weakest-premise ceiling may cease to bind if the conclusion is independently established through another valid proof path.

Example:

```text
Path A:
P1 weak
P2 strong
→ C ceiling 0.60
```

but:

```text
Path B:
Independent evidence E
→ directly validates C at stronger level
```

Then `C` may be promoted based on Path B.

However:

```text
PARAPHRASED_PATH != INDEPENDENT_PATH
```

Independence must be demonstrated.

---

# 18. Proposed Hard Ceiling

Absent a recognized stronger proof state:

```text
confidence_ceiling ≤ 0.95
```

This prevents ordinary evidence aggregation from being represented as absolute certainty.

Possible exceptions MAY include authoritative formal proof categories defined elsewhere.

Until such canon is resolved:

```text
>0.95 = REQUIRES_STRONGER_PROOF_CLASS
```

This remains conditional because the authoritative epistemics canon may define different ceiling semantics.

---

# 19. Confidence Composition Prohibition

AMOS MUST NOT arbitrarily compute:

```text
(0.7 + 0.8 + 0.9) / 3 = 0.8
```

as claim confidence unless an explicit validated aggregation rule licenses that operation.

Similarly:

```text
0.7 × 0.8
```

or:

```text
1 - (1-0.7)(1-0.8)
```

must not be used merely because they appear mathematically plausible.

Confidence composition requires semantic and probabilistic justification.

---

# 20. Unknown

`UNKNOWN` means the system lacks sufficient justified information to resolve a required state.

It does NOT mean:

```text
false
zero
unlikely
irrelevant
neutral
50/50
```

Therefore:

```text
UNKNOWN != FALSE
UNKNOWN != ZERO
UNKNOWN != 0.5
```

---

# 21. GAP

`GAP` identifies a missing information, specification, implementation, provenance, validation, or dependency element.

A gap MAY be:

```text
CRITICAL
DECISION_RELEVANT
EXPLANATORY
COSMETIC
```

The gap class determines priority.

---

# 22. Critical Gap

A critical gap prevents a safe or justified conclusion.

Examples:

* unknown authority for irreversible action;
* missing load-bearing evidence;
* unknown target identity;




## Vault-Sourced Domain Content

> Source: `01_CANON/01_CORE_LAWS/L6_UNCERTAINTY.md` (54038 bytes in vault)

### U-1 — Typed Uncertainty

Uncertainty MUST be classified before consequential use.

Minimum epistemic-origin classes:

```text
SOURCE
DERIVED
MODEL
UNKNOWN
```

The origin of uncertainty must remain distinguishable from the claim class itself.

Example:

```yaml
claim_class: DERIVED

uncertainty:
  source: LOW
  derivation: MEDIUM
  model: NONE
  unknown: PRESENT
```

A claim being `DERIVED` does not imply all uncertainty is derivational.

---

### U-5 — Confidence Is Not Evidence

```text
CONFIDENCE != EVIDENCE
```

A confidence value summarizes epistemic state. It does not create evidence.

Repeated confidence statements do not strengthen the underlying claim.

---

### U-7 — Repetition Does Not Reduce Uncertainty

```text
REPETITION != INDEPENDENT_CONFIRMATION
```

Multiple sources descended from one origin do not automatically reduce uncertainty.

---

### U-9 — Uncertainty Is Typed, Not Scalar-Only

A single number MUST NOT erase materially different uncertainty dimensions.

For consequential claims AMOS MAY track:

```text
evidence uncertainty
model uncertainty
scope uncertainty
temporal uncertainty
causal uncertainty
execution uncertainty
provenance-independence uncertainty
```

---

### U-10 — Uncertainty Reduction Requires Information

Uncertainty may not decrease merely because reasoning continued longer.

```text
MORE_REASONING != MORE_EVIDENCE
```

Legitimate reduction requires something such as:

* new evidence;
* stronger provenance;
* successful validation;
* discriminating observation;
* resolved dependency;
* narrowed scope;
* better measurement;
* successful execution test;
* formal proof where applicable.

---

### U-12 — Uncertainty Must Be Decision-Relevant

AMOS SHOULD distinguish uncertainty that can change a decision from uncertainty that cannot materially change it.

```text
DECISION_RELEVANT_UNCERTAINTY
>
EXPLANATORY_UNCERTAINTY
>
COSMETIC_UNCERTAINTY
```

for reasoning-resource allocation.

This ordering concerns priority, not truth value.

---

# 5. Uncertainty Vector

For consequential claims, L6 SHOULD support a multidimensional uncertainty representation.

Conceptually:

```text
U(C) =
[
  Ue,
  Um,
  Us,
  Ut,
  Uc,
  Ux,
  Up
]
```

where:

```text
Ue = evidence uncertainty
Um = model uncertainty
Us = scope uncertainty
Ut = temporal uncertainty
Uc = causal uncertainty
Ux = execution uncertainty
Up = provenance-independence uncertainty
```

This vector is an AMOS structural model.

It does not require every implementation to encode uncertainty numerically.

---

# 6. Evidence Uncertainty

Evidence uncertainty concerns the quality and completeness of evidence supporting a claim.

Sources include:

* missing observations;
* small samples;
* noisy measurements;
* incomplete records;
* conflicting observations;
* measurement error;
* unverified reports;
* indirect evidence.

Example:

```yaml
uncertainty:
  evidence:
    status: MATERIAL
    causes:
      - incomplete_observation
      - measurement_noise
```

---

# 7. Model Uncertainty

Model uncertainty concerns whether the selected representation or explanatory model is appropriate.

Examples:

* model misspecification;
* omitted variables;
* competing models;
* unstable parameters;
* approximation error;
* extrapolation;
* unvalidated assumptions.

Therefore:

```text
PRECISE_MODEL_OUTPUT
!=
LOW_MODEL_UNCERTAINTY
```

A model may output many decimal places while remaining epistemically weak.

---

# 8. Scope Uncertainty

Scope uncertainty concerns uncertainty over where a claim applies.

Examples:

```text
population unknown
environment mismatch
cross-domain transfer
cross-scale transfer
uncertain exclusions
measurement-context mismatch
```

L6 delegates applicability structure to `L5_SCOPE_REGIME`.

Therefore:

```text
UNKNOWN_SCOPE
→
SCOPE_UNCERTAINTY
```

not universal applicability.

---

# 9. Temporal Uncertainty

Temporal uncertainty concerns:

* unknown evidence age;
* uncertain event ordering;
* uncertain freshness;
* uncertain validity duration;
* delayed observations;
* possible regime transition.

Example:

```yaml
uncertainty:
  temporal:
    freshness: UNKNOWN
    event_time: KNOWN
    observation_time: KNOWN
```

Temporal uncertainty does not necessarily invalidate historical claims but may invalidate current-use claims.

---

# 10. Causal Uncertainty

Causal uncertainty concerns uncertainty over whether observed relationships represent:

* association;
* correlation;
* enabling condition;
* mediator;
* confounder;
* feedback;
* mechanism;
* necessary condition;
* sufficient condition;
* causal effect.

L6 MUST NOT resolve causal uncertainty merely through confidence language.

```text
HIGH_CONFIDENCE_CORRELATION
!=
CAUSAL_EFFECT
```

Causal typing remains governed by L4.

---

# 11. Execution Uncertainty

Execution uncertainty concerns whether a proposed operation will actually produce the expected result.

It includes:

* runtime uncertainty;
* environmental uncertainty;
* tool availability;
* dependency state;
* external-state mutation;
* concurrency;
* commit failure;
* implementation mismatch.

Therefore:

```text
LOGICALLY_VALID_PLAN
!=
SUCCESSFUL_EXECUTION
```

Execution evidence must remain separate from reasoning confidence.

---

# 12. Provenance-Independence Uncertainty

AMOS MUST track uncertainty about whether apparently separate evidence is genuinely independent.

Example:

```text
Source A
   ↓
Source B paraphrases A
   ↓
Source C summarizes B
```

must not be interpreted as:

```text
3 independent confirmations
```

The actual topology may contain only one origin.

Thus:

```text
COUNT(SOURCES)
!=
COUNT(INDEPENDENT_ORIGINS)
```

---

# 13. Typed Uncertainty State

A conceptual uncertainty object MAY be represented as:

```yaml
UncertaintyState:
  claim_id: ClaimID

  evidence:
    level: ...
    causes: [...]

  model:
    level: ...
    causes: [...]

  scope:
    level: ...
    causes: [...]

  temporal:
    level: ...
    causes: [...]

  causal:
    level: ...
    causes: [...]

  execution:
    level: ...
    causes: [...]

  provenance_independence:
    level: ...
    causes: [...]

  unknowns: [...]

  competing: [...]

  confidence_ceiling: ...

  decision_relevance: ...

  reducibility:
    reducible: true | false | unknown
    candidate_tests: [...]

  provenance: [...]
```

---

# 14. Qualitative Uncertainty Levels

Where numerical uncertainty is unsupported, AMOS SHOULD prefer explicit qualitative states.

Example:

```text
NONE_ESTABLISHED
LOW
MODERATE
HIGH
CRITICAL
UNKNOWN
```

These labels MUST NOT be silently interpreted as calibrated probabilities.

For example:

```text
HIGH UNCERTAINTY
```

does not mathematically mean:

```text
P(error) > 0.5
```

unless explicitly calibrated.

---

# 15. Numerical Confidence

Numerical confidence MAY be used only when its semantics are explicit.

A confidence object SHOULD specify:

```yaml
confidence:
  value: 0.72
  semantics: AMOS_EPISTEMIC_SCORE
  calibration: UNVALIDATED
  basis: [...]
  ceiling: 0.80
```

rather than simply:

```yaml
confidence: 0.72
```

when ambiguity would matter.

---

# 16. Confidence Ceiling Mechanics

For a conclusion `C` depending on premises:

```text
P1, P2, ..., Pn
```

the default AMOS ceiling is conceptually:

```text
Ceiling(C)
≤
min(
  Ceiling(P1),
  Ceiling(P2),
  ...,
  Ceiling(Pn)
)
```

for load-bearing dependencies.

This prevents:

```text
weak premise
+
strong premise
+
fluent synthesis
=
very strong conclusion
```

---

# 17. Independent Revalidation Exception

The weakest-premise ceiling may cease to bind if the conclusion is independently established through another valid proof path.

Example:

```text
Path A:
P1 weak
P2 strong
→ C ceiling 0.60
```

but:

```text
Path B:
Independent evidence E
→ directly validates C at stronger level
```

Then `C` may be promoted based on Path B.

However:

```text
PARAPHRASED_PATH != INDEPENDENT_PATH
```

Independence must be demonstrated.

---

# 18. Proposed Hard Ceiling

Absent a recognized stro

... (truncated, see vault source for full content)

## Failure Modes

- **Insufficient evidence**: If source material is insufficient, mark as UNKNOWN/GAP and fail closed — do not fabricate.
- **Scope violation**: If the query falls outside the skill's declared scope, escalate to the parent skill or steward.
- **Binding broken**: If 1:1:1 binding (skill→agent→workflow) is broken, flag routing mismatch and block execution.
- **Validation failure**: If validation gates fail, downgrade confidence, flag the gap, and escalate — do not force-fit.
- **Epistemic overreach**: If a claim exceeds the established evidence or epistemic class, retract and relabel.

---
**MOC:** [[references_MOC]]
