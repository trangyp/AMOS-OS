---
artifact_id: AMOS-OS-K-METACOGNITION
canonical_name: K_METACOGNITION
artifact_type: kernel_metacognition_contract
status: AMOS_MODEL
conclusion_class: AMOS_MODEL
amos_core_target: v4.4

origin_architect: Trang Phan
steward: Trang Phan

plane: KERNEL
kernel_family: REASONING
domain: metacognition
scope: AMOS_OS

created: 2026-08-25
updated: 2026-08-25

tags:
  - amos-os
  - canon-group/tech-ai
  - canon/model
  - kernel
  - kernel/reasoning
  - kernel/metacognition
  - kernel/epistemic
  - kernel/provenance
  - kernel/uncertainty
  - kernel/validation
  - kernel/dependency
  - kernel/scope
  - kernel/regime
  - kernel/sensitivity
  - kernel/rscf
  - rscf/claim
  - rscf/provenance
  - rscf/state/model
  - topic/metacognition

aliases:
  - AMOS Metacognition Kernel
  - Metacognition Kernel
  - K Metacognition
  - K_METACOGNITION
---

# K_METACOGNITION

> **AMOS Core target:** `v4.4`  
> **Origin architect / steward:** Trang Phan  
> **Plane:** `02_KERNEL`  
> **Status:** `AMOS_MODEL`  
> **Conclusion class:** `AMOS_MODEL`

## Purpose

`K_METACOGNITION` defines the AMOS kernel contract for reasoning about the quality, limits, state, and reliability of reasoning itself.

Its core function is:

```text
REASON
↓
INSPECT THE REASONING STATE
↓
IDENTIFY DECISION-CHANGING UNCERTAINTY
↓
TEST LOAD-BEARING PREMISES
↓
DETECT CONFLICT / SCOPE / PROVENANCE / CAUSAL FAILURE
↓
ADAPT REASONING DEPTH
↓
STOP, ESCALATE, REPAIR, OR CONTINUE
```

Metacognition does not create truth by introspection.

It governs whether a conclusion is sufficiently supported to be reused, challenged, downgraded, escalated, or rejected.

---

# 1. Architectural Position

```text
CANON
↓
FOUNDATIONAL LOGIC
↓
META-LOGIC
↓
EPISTEMIC + PROVENANCE + CAUSAL STRUCTURE
↓
K_METACOGNITION
↓
REASONING GOVERNANCE
↓
VALIDATION / DECISION / ACTION
```

`K_METACOGNITION` observes and regulates reasoning operations.

It does not replace:

```text
CANON
KERNEL LOGIC
EVIDENCE
PROVENANCE
VALIDATION
AUTHORITY
```

---

# 2. Core Law

```text
THINKING ABOUT THINKING
!=
EVIDENCE ABOUT REALITY
```

Therefore:

```text
INTERNAL COHERENCE
!=
TRUTH

CONFIDENCE
!=
VALIDATION

FLUENCY
!=
CORRECTNESS

CONSISTENCY
!=
EMPIRICAL SUPPORT

ABSENCE OF DETECTED ERROR
!=
PROOF OF CORRECTNESS
```

---

# 3. Metacognitive Object

A metacognitive state should conceptually carry:

```yaml
metacognitive_state:
  objective:
  scope:
  stakes:

  active_claims: []
  load_bearing_premises: []

  evidence_state:
  provenance_state:
  causal_state:
  dependency_state:

  uncertainty:
    evidence:
    model:
    scope:
    temporal:
    causal:
    execution:
    provenance_independence:

  contradictions: []
  competing_hypotheses: []
  gaps: []

  sensitivity_points: []

  reasoning_depth:
  escalation_required:
  stop_condition:

  conclusion_class:
  confidence_ceiling:
```

---

# 4. Objective Awareness

Before evaluating reasoning quality, the kernel must know what the reasoning is trying to achieve.

Conceptually:

```text
META_STATE
=
f(
  OBJECTIVE,
  SCOPE,
  STAKES,
  FRESHNESS,
  REQUIRED_DELIVERABLE
)
```

The same evidence may be sufficient for:

```text
EXPLANATION
```

but insufficient for:

```text
IRREVERSIBLE DECISION
```

---

# 5. Stakes Awareness

Required validation increases with consequence.

Conceptually:

```text
VALIDATION_REQUIREMENT
↑
AS
IRREVERSIBILITY
COST
SAFETY EXPOSURE
LEGAL EXPOSURE
FINANCIAL EXPOSURE
INSTITUTIONAL IMPACT
DOWNSTREAM DEPENDENCY
↑
```

This is a governance principle, not a universal numerical formula.

---

# 6. Epistemic State

Metacognition must distinguish:

```text
WHAT IS OBSERVED
WHAT IS CLAIMED
WHAT IS DERIVED
WHAT IS MODELED
WHAT IS DECIDED
WHAT IS UNKNOWN
```

Canonical evidence classes:

```text
SOURCE_CLAIM
OBSERVATION
DERIVED
MODEL
DECISION
UNKNOWN
```

These must not silently collapse into one another.

---

# 7. Conclusion Classes

Every material conclusion should use the weakest accurate class:

```text
VERIFIED
DERIVED
MODEL
CONDITIONAL
COMPETING
UNKNOWN/GAP
```

Metacognition must detect unjustified promotion such as:

```text
MODEL
→
VERIFIED
```

without validation.

---

# 8. Confidence Firewall

```text
SUBJECTIVE CONFIDENCE
!=
EVIDENCE QUALITY
```

A reasoning process may feel highly coherent while resting on weak evidence.

Therefore confidence must be bounded by load-bearing premises.

Conceptually:

```text
CONFIDENCE(CONCLUSION)
≤
MIN(
  LOAD_BEARING_PREMISE_CONFIDENCE
)
```

unless the relevant premise is independently revalidated.

---

# 9. Load-Bearing Premises

A premise is load-bearing when changing or invalidating it can materially change a conclusion.

```text
PREMISE P
IS LOAD-BEARING
IFF
INVALIDATE(P)
CAN CHANGE
CONCLUSION C
```

Metacognitive effort should prioritize these premises over decorative background information.

---

# 10. Dependency Awareness

For:

```text
P1
P2
P3
↓
C1
↓
C2
```

if `P2` fails:

```text
INVALIDATE(P2)
INVALIDATE(C1 if dependent)
INVALIDATE(C2 if dependent)
```

but preserve unrelated valid work.

```text
LOCAL FAILURE
!=
GLOBAL FAILURE
```

---

# 11. Selective Invalidation

The default recovery operation is:

```text
FAILED PREMISE
↓
DEPENDENCY EDGE
↓
DEPENDENT CONCLUSIONS
```

not:

```text
FAILED PREMISE
↓
DELETE EVERYTHING
```

This supports repairable reasoning.

---

# 12. Contradiction Awareness

Metacognition must actively detect:

```text
CLAIM A
AND
NOT A
```

or materially incompatible conclusions.

A contradiction must not be hidden merely to produce fluent output.

Possible outcomes include:

```text
RESOLVED
COMPETING
CONDITIONAL
UNKNOWN/GAP
```

---

# 13. Competing Hypotheses

If:

```text
H1
H2
H3
```

remain viable and available evidence cannot discriminate them:

```text
STATE = COMPETING
```

Do not force convergence.

---

# 14. Adversarial Validation

For consequential conclusions:

```text
CONSTRUCT STRONGEST SUPPORTED CONCLUSION
↓
CHALLENGE IT THROUGH A DIFFERENT PATH
```

The challenge should seek:

```text
CONTRADICTION
CORRELATED PROVENANCE
STALE PREMISE
SCOPE LEAKAGE
REGIME SHIFT
HIDDEN DEPENDENCY
CAUSAL OVERREACH
STRONGER ALTERNATIVE
```

---

# 15. Independent Challenge Requirement

Repeating the same reasoning in different words is not independent validation.

```text
SAME PREMISES
+
SAME SOURCE ANCESTRY
+
SAME MODEL
=
CORRELATED CHECK
```

not independent confirmation.

---

# 16. Provenance Awareness

Metacognition should ask:

```text
WHERE DID THIS PREMISE COME FROM?
```

and:

```text
DO APPARENTLY MULTIPLE SOURCES SHARE ANCESTRY?
```

Repetition is not independence.

```text
SOURCE A
↓
REPORT B
↓
ARTICLE C
↓
SUMMARY D
```

may represent one provenance family.

---

# 17. Provenance Independence Firewall

```text
MULTIPLE DOCUMENTS
!=
MULTIPLE INDEPENDENT SOURCES
```

Independence must be demonstrated when it materially affects confidence.

---

# 18. Freshness Awareness

A previously valid conclusion may become invalid when its temporal assumptions expire.

Conceptually:

```text
VALID(C, t)
IFF
DEPENDENCIES_VALID(C, t)
AND
REGIME_COMPATIBLE(C, t)
AND
FRESHNESS_VALID(C, t)
```

Freshness is claim-specific.

---

# 19. Scope Awareness

Every material claim inherits an applicability envelope.

Where relevant:

```yaml
scope:
  system:
  population:
  environment:
  scale:
  time:
  regime:
  measurement_method:
  assumptions:
```

Metacognition must detect attempts to generalize beyond this envelope.

---

# 20. Scope Leakage

Example:

```text
VALID IN SYSTEM A
```

does not automatically imply:

```text
VALID IN SYSTEM B
```

Likewise:

```text
VALID AT SCALE X
```

does not prove:

```text
VALID AT SCALE 1000X
```

---

# 21. Regime Awareness

A conclusion may be valid under:

```text
REGIME R1
```

and invalid under:

```text
REGIME R2
```

Metacognition must test whether the environment has crossed a regime boundary.

---

# 22. Causal Awareness

Metacognition must detect when reasoning silently upgrades:

```text
ASSOCIATION
→
CAUSATION
```

It distinguishes:

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

---

# 23. Causal Overreach Firewall

The following are insufficient by themselves to establish causation:

```text
ANALOGY
SEQUENCE
CO-OCCURRENCE
CORRELATION
STRUCTURAL SIMILARITY
NARRATIVE COHERENCE
```

Metacognition must downgrade conclusions that exceed the causal evidence type.

---

# 24. Structural Similarity Firewall

```text
STRUCTURE(A) ≈ STRUCTURE(B)
```

may support:

```text
MODEL / HYPOTHESIS
```

but not automatically:

```text
CAUSAL EQUIVALENCE
```

Cross-domain mappings remain `MODEL` unless independently validated.

---

# 25. Uncertainty Vector

Material uncertainty should be decomposed:

```text
U =
<
U_evidence,
U_model,
U_scope,
U_temporal,
U_causal,
U_execution,
U_provenance_independence
>
```

This prevents the phrase:

```text
"UNCERTAIN"
```

from hiding what is actually uncertain.

---

# 26. Evidence Uncertainty

Ask:

```text
DO WE HAVE ENOUGH RELIABLE EVIDENCE?
```

Possible causes:

```text
MISSING DATA
LOW-QUALITY SOURCE
UNVERIFIED SOURCE CLAIM
CONFLICTING OBSERVATIONS
MEASUREMENT ERROR
```

---

# 27. Model Uncertainty

Ask:

```text
IS THE INTERPRETIVE MODEL ITSELF RELIABLE?
```

Multiple models may explain the same evidence.

Model uncertainty must not be mislabeled as evidence uncertainty.

---

# 28. Scope Uncertainty

Ask:

```text
WHERE DOES THIS CONCLUSION APPLY?
```

Unknown applicability boundaries should produce:

```text
CONDITIONAL
```

or:

```text
UNKNOWN/GAP
```

when material.

---

# 29. Temporal Uncertainty

Ask:

```text
IS THE INFORMATION STILL CURRENT ENOUGH?
```

Stale premises should trigger revalidation when freshness can change the outcome.

---

# 30. Causal Uncertainty

Ask:

```text
DO WE KNOW THE CAUSAL STRUCTURE
OR ONLY ASSOCIATION?
```

This uncertainty is critical when the user intends intervention.

---

# 31. Execution Uncertainty

A correct plan may still fail operationally.

```text
PLAN VALIDITY
!=
EXECUTION SUCCESS
```

Execution uncertainty includes:

```text
RESOURCE AVAILABILITY
IMPLEMENTATION ERROR
COORDINATION FAILURE
ENVIRONMENTAL VARIANCE
DEPENDENCY FAILURE
```

---

# 32. Provenance-Independence Uncertainty

Ask:

```text
ARE THESE SOURCES ACTUALLY INDEPENDENT?
```

If unknown:

```text
U_provenance_independence > 0
```

and confidence should not be boosted as though independence were established.

---

# 33. Gap Classification

Metacognitive gaps are classified:

```text
CRITICAL
DECISION-RELEVANT
EXPLANATORY
COSMETIC
```

Resolution priority:

```text
CRITICAL
↓
DECISION-RELEVANT
↓
EXPLANATORY
↓
COSMETIC
```

---

# 34. Critical Gap

A critical gap prevents a safe or valid conclusion.

Example:

```text
UNKNOWN IDENTITY OF LOAD-BEARING SOURCE
UNKNOWN JURISDICTION FOR LEGAL CLAIM
UNKNOWN MEDICATION FOR INTERACTION CHECK
UNKNOWN STATE VERSION FOR COMMIT
```

If unresolved:

```text
RETURN UNKNOWN/GAP
```

and identify the minimum missing information.

---

# 35. Decision-Relevant Gap

A gap is decision-relevant when resolving it may change:

```text
SELECTED OPTION
RISK CLASS
ACTION
PRIORITY
RESOURCE ALLOCATION
```

These should normally be investigated before explanatory detail.

---

# 36. Explanatory Gap

An explanatory gap affects understanding but not the current decision.

It may remain unresolved once action sufficiency is reached.

---

# 37. Cosmetic Gap

A cosmetic gap affects presentation rather than reasoning integrity.

It should not consume reasoning budget while higher-value uncertainty remains.

---

# 38. Sensitivity

Metacognition asks:

```text
WHAT IS THE SMALLEST PLAUSIBLE CHANGE
THAT WOULD FLIP THE CONCLUSION?
```

This identifies fragile reasoning.

---

# 39. Fragility

If:

```text
SMALL CHANGE(P)
→
CHANGE(CONCLUSION)
```

then the conclusion should be marked:

```text
FRAGILE
```

and usually:

```text
CONDITIONAL
```

---

# 40. Robustness

A conclusion is comparatively robust if it survives plausible perturbations of noncritical assumptions.

```text
ROBUST
!=
CERTAIN
```

Robustness does not remove scope, provenance, or causal requirements.

---

# 41. Adaptive Complexity

AMOS reasoning depth is represented conceptually as:

```text
C0 DIRECT
C1 COMPACT
C2 STRUCTURED
C3 DEEP
C4 MAXIMUM
```

Use the lowest level sufficient for integrity.

---

# 42. C0 — Direct

Appropriate when:

```text
LOW STAKES
CLEAR FACT
NO MATERIAL CONFLICT
NO COMPLEX DEPENDENCY
NO FRESHNESS PROBLEM
```

Avoid unnecessary architecture expansion.

---

# 43. C1 — Compact

Use when limited decomposition is required but uncertainty remains small.

Typical pattern:

```text
CLAIM
EVIDENCE
LIMIT
ACTION
```

---

# 44. C2 — Structured

Use when reasoning requires:

```text
MULTIPLE PREMISES
TRADE-OFFS
SCOPE CHECKS
BASIC PROVENANCE
MULTIPLE OPTIONS
```

---

# 45. C3 — Deep

Escalate when:

```text
HIGH STAKES
CONFLICT
WEAK EVIDENCE
CAUSAL AMBIGUITY
REGIME UNCERTAINTY
MULTIPLE COMPETING MODELS
SIGNIFICANT DEPENDENCY
```

---

# 46. C4 — Maximum

Reserve for cases involving combinations such as:

```text
VERY HIGH STAKES
IRREVERSIBILITY
GOVERNANCE IMPACT
COMPLEX PROVENANCE
MULTIPLE REGIMES
CAUSAL DISPUTE
ADVERSARIAL CONDITIONS
SYSTEMIC FAILURE RISK
```

Maximum complexity is not intrinsically better.

---

# 47. Escalation Rule

Escalate when additional reasoning can materially alter:

```text
CLAIM
DECISION
ACTION
RISK
```

Do not escalate merely because more analysis is possible.

---

# 48. De-escalation Rule

Once outcome-changing uncertainty is resolved:

```text
DE-ESCALATE
```

Do not continue expanding analysis without positive expected decision value.

---

# 49. Reasoning Budget

Metacognitive effort should be allocated where uncertainty reduction has the highest decision value.

Conceptually:

```text
PRIORITY(i)
∝
EXPECTED_DECISION_VALUE_OF_RESOLVING(U_i)
/
COST_OF_RESOLUTION(U_i)
```

This is an architectural optimization model, not a claim of literal numerical runtime calculation.

---

# 50. Smallest Sufficient Proof Scope

v4.4 fast-path reasoning prefers:

```text
SMALLEST PROOF SCOPE
THAT CAN SAFELY SUPPORT
THE REQUIRED CONCLUSION
```

Do not traverse unrelated knowledge.

---

# 51. Local Reasoning Fast Path

Local reasoning is admissible only when:

```text
DEPENDENCY CLOSURE ESTABLISHED
AND
PROVENANCE SUFFICIENT
AND
PROVENANCE INDEPENDENCE SUFFICIENT
AND
SCOPE COMPATIBLE
AND
REGIME COMPATIBLE
AND
FRESHNESS VALID
AND
NO MATERIAL CONFLICT
```

Then global reasoning may be avoided.

---

# 52. Fast-Path Escalation

Escalate from local reasoning if:

```text
SHARED SOURCE ANCESTRY DETECTED
CONFLICT DETECTED
STALE PREMISE DETECTED
REGIME CROSSING DETECTED
CAUSAL COUPLING DETECTED
DEPENDENCY AMBIGUITY DETECTED
GOVERNANCE IMPACT DETECTED
IRREVERSIBLE STAKES DETECTED
```

---

# 53. H/M/L Retrieval Awareness

Metacognition controls retrieval depth.

```text
BOOTSTRAP
↓
H DOMAIN
↓
M SUBSYSTEM
↓
L DETAIL
↓
RAW EVIDENCE
```

Raw evidence is loaded only when necessary to alter the answer or validate a load-bearing premise.

---

# 54. Retrieval Firewall

```text
MORE RETRIEVAL
!=
BETTER REASONING
```

Excess evidence may:

```text
ADD NO DECISION VALUE
INTRODUCE CORRELATED SOURCES
INCREASE CONFLICT NOISE
OBSCURE LOAD-BEARING PREMISES
```

Retrieval must remain purpose-driven.

---

# 55. RSCF Awareness

Metacognition treats RSCF structures as dependency-bearing reasoning objects.

Conceptually:

```text
RSCF
=
CLAIM
+
EVIDENCE
+
PROVENANCE
+
SCOPE
+
REGIME
+
DEPENDENCIES
+
FALSIFIERS
+
CONFIDENCE CEILING
```

where applicable.

---

# 56. Proof Capsule Awareness

Important conclusions should conceptually carry:

```yaml
proof_capsule:
  claim:
  claim_class:

  load_bearing_premises: []

  evidence: []
  provenance: []

  scope:
  regime:
  temporal_validity:

  dependencies: []
  competing_explanations: []
  falsifiers: []

  sensitivity_points: []
  confidence_ceiling:
  invalidation_conditions: []
```

Metacognition decides whether this capsule remains reusable.

---

# 57. Proof Reuse

A proof capsule may be reused only while:

```text
DEPENDENCIES VALID
AND
SCOPE VALID
AND
REGIME VALID
AND
FRESHNESS VALID
AND
NO MATERIAL CONFLICT
```

Otherwise:

```text
REVALIDATE
```

---

# 58. Persistent Provenance

A conclusion without recoverable provenance should not silently retain high trust after context loss.

Persistent reasoning requires enough lineage to reconstruct:

```text
WHAT WAS CLAIMED
WHY IT WAS BELIEVED
WHAT IT DEPENDED ON
WHEN IT WAS VALID
WHAT COULD INVALIDATE IT
```

---

# 59. Failure Detection

Metacognition should recognize:

```text
PREMISE FAILURE
SOURCE FAILURE
DEPENDENCY FAILURE
SCOPE FAILURE
REGIME FAILURE
CAUSAL FAILURE
PROVENANCE FAILURE
EXECUTION FAILURE
```

Different failures require different repair paths.

---

# 60. Failure Recovery

Default:

```text
DETECT FAILURE
↓
IDENTIFY FAILED NODE / EDGE
↓
INVALIDATE DEPENDENTS
↓
PRESERVE UNAFFECTED WORK
↓
ROLL BACK TO NEAREST VALID STATE
↓
REROUTE
```

Global recomputation is a last resort.

---

# 61. No Repeated Failed Path

```text
FAILED PATH
+
UNCHANGED EVIDENCE
+
UNCHANGED ASSUMPTIONS
=
DO NOT REPEAT
```

Retry requires some changed condition.

---

# 62. Reasoning Loop Detection

Metacognition should detect loops such as:

```text
QUESTION
→
ANALYSIS
→
SAME QUESTION
→
SAME ANALYSIS
→
...
```

When no new information enters:

```text
STOP
```

or identify the missing discriminating evidence.

---

# 63. Branch Control

Branch only when alternatives can materially alter the outcome.

```text
BRANCH
IFF
ALTERNATIVE PATH
CAN CHANGE
CLAIM / DECISION / ACTION
```

Equivalent branches should merge.

---

# 64. Branch Explosion Firewall

Do not enumerate all conceivable alternatives.

Prioritize:

```text
SUPPORTED
PLAUSIBLE
DISCRIMINATING
DECISION-RELEVANT
```

branches.

---

# 65. Strongest Alternative Test

Before accepting an important conclusion:

```text
WHAT IS THE STRONGEST SUPPORTED ALTERNATIVE?
```

If the alternative has comparable support:

```text
COMPETING
```

may be the correct state.

---

# 66. Discriminating Test Selection

Prefer evidence that separates hypotheses.

Conceptually:

```text
TEST*
=
CHEAPEST HIGH-INFORMATION TEST
THAT CAN CHANGE THE DECISION
```

Do not accumulate redundant confirmation.

---

# 67. Falsification Awareness

Ask:

```text
WHAT OBSERVATION WOULD MAKE THIS CONCLUSION WRONG?
```

A claim with no identifiable falsifier may still function as a model, definition, or normative rule, but must not masquerade as an empirically testable proposition.

---

# 68. Confirmation-Bias Firewall

Metacognition should not search only for support.

For consequential claims:

```text
SUPPORT SEARCH
+
CHALLENGE SEARCH
```

are both required when feasible.

---

# 69. Narrative-Coherence Firewall

A clean story is not evidence.

```text
COHERENT NARRATIVE
!=
VALID CAUSAL MODEL
```

Metacognition must resist filling missing edges because the resulting explanation sounds complete.

---

# 70. Completeness Firewall

```text
INCOMPLETE BUT SUPPORTED
>
COMPLETE BUT FABRICATED
```

Therefore:

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

# 71. Unknown Preservation

When a critical fact is unavailable:

```text
UNKNOWN
```

must remain `UNKNOWN`.

Do not convert uncertainty into:

```text
LIKELY FACT
```

merely to finish the response.

---

# 72. Assumption Awareness

Assumptions must be explicit when they are load-bearing.

Conceptually:

```yaml
assumption:
  proposition:
  reason_required:
  scope:
  sensitivity:
  falsifier:
```

Hidden assumptions are a metacognitive failure.

---

# 73. Assumption Minimization

Prefer reasoning that requires fewer unsupported assumptions when explanatory power is otherwise comparable.

This does not establish a universal simplicity law.

It is a reliability heuristic.

---

# 74. Model Awareness

Metacognition must know when it is operating inside a model.

```text
MODEL OUTPUT
```

inherits limitations from:

```text
MODEL STRUCTURE
PARAMETERS
CALIBRATION
BOUNDARY CONDITIONS
ASSUMPTIONS
```

---

# 75. Benchmark Firewall

```text
BENCHMARK SUCCESS
!=
UNIVERSAL VALIDITY
```

A model validated on benchmark `B` remains validated only within the supported applicability envelope.

---

# 76. Simulation Firewall

```text
SIMULATION SUCCESS
!=
REAL-WORLD VALIDATION
```

Simulation is evidence about behavior under the simulation assumptions.

It is not automatically evidence about external reality.

---

# 77. Formal-Proof Firewall

Testing distributed or Byzantine scenarios does not automatically constitute universal formal proof.

```text
TEST COVERAGE
!=
FORMAL PROOF
```

unless formal proof actually exists.

---

# 78. Latency Firewall

Reported performance such as:

```text
LATENCY = X
```

must retain environment assumptions.

```text
MEASURED LATENCY
!=
HARDWARE-INDEPENDENT PROPERTY
```

---

# 79. Capability / Authority Firewall

Metacognitive confidence never creates authority.

```text
CAPABILITY
!=
AUTHORITY

KNOWING
!=
PERMISSION

MODEL
!=
AUTHORITY

PROPOSAL
!=
COMMIT
```

---

# 80. Metacognition / Control-Plane Firewall

`K_METACOGNITION` may detect that escalation or authorization is needed.

It does not grant that authorization.

```text
KERNEL:
"AUTHORITY REQUIRED"

CONTROL PLANE:
"AUTHORITY VALID / INVALID"
```

These roles remain separate.

---

# 81. Metacognition / Runtime Firewall

The kernel may specify:

```text
RETRY
ROLLBACK
ESCALATE
REVALIDATE
```

as logical outcomes.

Actual runtime execution belongs to the runtime/control architecture.

```text
REASONING RECOMMENDATION
!=
EXECUTED STATE TRANSITION
```

---

# 82. Metacognition / Cognition Firewall

```text
K_METACOGNITION
```

defines reasoning constraints and inspection rules.

It is not identical to the full cognitive organism.

```text
KERNEL CONTRACT
!=
COGNITIVE ORGAN
```

---

# 83. Metacognition / Agent Firewall

An agent may use metacognitive rules.

The agent is not the kernel.

```text
AGENT
!=
K_METACOGNITION
```

The kernel defines reusable reasoning constraints.

---

# 84. Stop Conditions

Reasoning should stop when all three are sufficient:

```text
CLAIM SUFFICIENCY
DECISION SUFFICIENCY
ACTION SUFFICIENCY
```

unless the user explicitly requests deeper analysis.

---

# 85. Claim Sufficiency

Reached when the requested claim can be stated with an appropriate conclusion class and material uncertainty is visible.

---

# 86. Decision Sufficiency

Reached when remaining uncertainty is unlikely to change the selected decision.

---

# 87. Action Sufficiency

Reached when the next safe action is clear enough to execute or hand off.

---

# 88. Overthinking Detection

Further analysis is wasteful when:

```text
EXPECTED DECISION CHANGE ≈ NONE
```

and no integrity-critical gap remains.

Metacognition should then stop rather than optimize indefinitely.

---

# 89. Underthinking Detection

Further reasoning is required when unresolved uncertainty can materially change:

```text
SAFETY
AUTHORITY
CLAIM CLASS
DECISION
ACTION
```

---

# 90. Self-Correction

When new evidence invalidates a conclusion:

```text
DO NOT DEFEND OLD OUTPUT
```

Instead:

```text
IDENTIFY INVALIDATED PREMISE
↓
DOWNGRADE / REPAIR CONCLUSION
↓
PRESERVE VALID COMPONENTS
↓
UPDATE DEPENDENTS
```

---

# 91. Anti-Regression

A reasoning optimization is acceptable only if it preserves or improves:

```text
FACTUAL SUPPORT
SCOPE CORRECTNESS
CONTRADICTION VISIBILITY
PROVENANCE RECOVERABILITY
CAUSAL DISCIPLINE
SAFETY
EFFICIENCY
USER FIT
```

Otherwise:

```text
ROLL BACK OPTIMIZATION
```

---

# 92. Metacognitive Invariants

```text
MC-01
CONFIDENCE MUST NOT SUBSTITUTE FOR EVIDENCE

MC-02
FLUENCY MUST NOT SUBSTITUTE FOR CORRECTNESS

MC-03
INTERNAL COHERENCE MUST NOT SUBSTITUTE FOR EXTERNAL VALIDATION

MC-04
LOAD-BEARING PREMISES MUST BE IDENTIFIABLE

MC-05
CONCLUSION CONFIDENCE MUST RESPECT PREMISE CONFIDENCE

MC-06
MATERIAL CONTRADICTIONS MUST REMAIN VISIBLE

MC-07
GENUINE COMPETING HYPOTHESES MUST NOT BE FORCED TO CONVERGE

MC-08
PROVENANCE INDEPENDENCE MUST NOT BE ASSUMED

MC-09
SCOPE MUST PROPAGATE INTO CONCLUSIONS

MC-10
REGIME SHIFTS MUST TRIGGER REVALIDATION

MC-11
STALE LOAD-BEARING PREMISES MUST TRIGGER FRESHNESS CHECKS

MC-12
CAUSAL CLAIMS MUST MATCH CAUSAL EVIDENCE TYPE

MC-13
STRUCTURAL SIMILARITY MUST NOT BECOME CAUSAL PROOF

MC-14
UNCERTAINTY TYPES MUST REMAIN DISTINGUISHABLE WHEN MATERIAL

MC-15
CRITICAL GAPS MUST BE RESOLVED BEFORE COSMETIC GAPS

MC-16
FRAGILE RESULTS MUST BE MARKED CONDITIONAL

MC-17
LOCAL FAST PATH REQUIRES ESTABLISHED DEPENDENCY CLOSURE

MC-18
FAILED PREMISES INVALIDATE ONLY DEPENDENT RESULTS

MC-19
FAILED REASONING PATHS MUST NOT REPEAT WITHOUT CHANGED CONDITIONS

MC-20
MORE ANALYSIS MUST NOT BE EQUATED WITH BETTER ANALYSIS

MC-21
UNKNOWN/GAP MUST NOT BECOME PASS

MC-22
MODEL MUST NOT BECOME AUTHORITY

MC-23
CAPABILITY MUST NOT BECOME AUTHORITY

MC-24
METACOGNITIVE OUTPUT MUST NOT CLAIM IMPLEMENTATION IT CANNOT VERIFY

MC-25
REASONING SHOULD STOP WHEN CLAIM, DECISION, AND ACTION SUFFICIENCY ARE MET
```

---

# 93. Failure Modes

```text
OVERCONFIDENCE
UNDERCONFIDENCE
FALSE_CERTAINTY
NARRATIVE_COMPLETION
HIDDEN_ASSUMPTION
PREMISE_BLINDNESS
DEPENDENCY_BLINDNESS
CONTRADICTION_SUPPRESSION
FORCED_CONVERGENCE
PROVENANCE_COLLAPSE
FALSE_INDEPENDENCE
SCOPE_LEAKAGE
REGIME_LEAKAGE
STALE_REASONING
CAUSAL_OVERREACH
MODEL_OVERREACH
BENCHMARK_OVERREACH
SIMULATION_OVERREACH
AUTHORITY_LEAKAGE
REASONING_LOOP
BRANCH_EXPLOSION
GLOBAL_RECOMPUTATION_BIAS
REPEATED_FAILED_PATH
PREMATURE_STOP
ANALYSIS_WITHOUT_DECISION_VALUE
```

---

# 94. Conceptual Runtime

```python
def metacognitive_check(reasoning_state):
    objective = identify_objective(reasoning_state)
    stakes = classify_stakes(reasoning_state)

    claims = identify_material_claims(reasoning_state)
    premises = identify_load_bearing_premises(claims)

    check_evidence(premises)
    check_provenance(premises)
    check_scope(premises)
    check_regime(premises)
    check_freshness(premises)
    check_causal_typing(premises)

    contradictions = detect_contradictions(claims)
    competitors = detect_competing_hypotheses(claims)

    uncertainty = decompose_uncertainty(reasoning_state)
    gaps = classify_gaps(reasoning_state)

    sensitivity = find_conclusion_flipping_premises(claims)

    if critical_gap(gaps):
        return UNKNOWN_GAP

    if unresolved_material_competition(competitors):
        return COMPETING

    if sensitivity_is_high(sensitivity):
        downgrade_to(CONDITIONAL)

    if escalation_has_positive_decision_value(
        uncertainty,
        stakes,
    ):
        return ESCALATE

    if claim_decision_action_sufficient(reasoning_state):
        return STOP

    return CONTINUE
```

This is architectural pseudocode, not a claim of deployed implementation.

---

# 95. Required Tests

Future implementation verification should include:

```text
CONFIDENCE-CEILING TEST
LOAD-BEARING-PREMISE TEST
DEPENDENCY-INVALIDATION TEST
CONTRADICTION-PRESERVATION TEST
COMPETING-HYPOTHESIS TEST
PROVENANCE-INDEPENDENCE TEST
SCOPE-FIREWALL TEST
REGIME-SHIFT TEST
FRESHNESS TEST
CAUSAL-TYPING TEST
SENSITIVITY TEST
GAP-PRIORITY TEST
FAST-PATH TEST
ESCALATION TEST
DE-ESCALATION TEST
FAILED-PATH TEST
LOCAL-RECOVERY TEST
STOP-CONDITION TEST
AUTHORITY-FIREWALL TEST
UNKNOWN-PRESERVATION TEST
```

---

# 96. Negative Tests

```text
HIGH CONFIDENCE
→
VERIFIED
MUST FAIL

FLUENT EXPLANATION
→
TRUE
MUST FAIL

MULTIPLE DESCENDANT SOURCES
→
INDEPENDENT CONFIRMATION
MUST FAIL

CORRELATION
→
CAUSATION
MUST FAIL

STRUCTURAL SIMILARITY
→
CAUSAL EQUIVALENCE
MUST FAIL

BENCHMARK SUCCESS
→
UNIVERSAL VALIDITY
MUST FAIL

SIMULATION SUCCESS
→
EMPIRICAL VALIDATION
MUST FAIL

UNKNOWN
→
PASS
MUST FAIL

MODEL
→
AUTHORITY
MUST FAIL

CAPABILITY
→
AUTHORITY
MUST FAIL

LOCAL PREMISE FAILURE
→
GLOBAL INVALIDATION
MUST FAIL

UNCHANGED FAILED PATH
→
AUTOMATIC RETRY
MUST FAIL
```

---

# 97. Promotion Gate

Before promotion beyond `AMOS_MODEL`:

```text
[ ] canonical metacognition lineage bound
[ ] epistemic classes confirmed
[ ] conclusion classes confirmed
[ ] confidence-ceiling semantics confirmed
[ ] dependency invalidation semantics confirmed
[ ] provenance-independence semantics confirmed
[ ] scope firewall confirmed
[ ] regime firewall confirmed
[ ] freshness rules confirmed
[ ] causal firewall confirmed
[ ] uncertainty vector confirmed
[ ] gap taxonomy confirmed
[ ] sensitivity semantics confirmed
[ ] adaptive complexity semantics confirmed
[ ] fast-path conditions confirmed
[ ] adversarial validation behavior confirmed
[ ] stop conditions confirmed
[ ] recovery behavior tested
[ ] authority firewall tested
[ ] negative tests implemented
[ ] unresolved conflicts registered
```

Until these are evidenced:

```text
IMPLEMENTATION_STATUS = UNKNOWN/GAP
```

---

# 98. Lifecycle

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

Do not collapse lifecycle states.

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

# 99. Integrity Note

This artifact replaces an empty repository placeholder with a structured metacognitive kernel model aligned to the AMOS v4.4 reasoning architecture.

It does **not** establish that every described mechanism exists as executable AMOS OS runtime code.

Therefore:

```text
DOCUMENT_CLASS = AMOS_MODEL
IMPLEMENTATION = UNKNOWN/GAP
EMPIRICAL_VALIDATION = UNKNOWN/GAP
RUNTIME_AUTHORITY = NONE
```

---

# 100. RSCF Node

```RSCF-NODE
node_id: AMOS-OS-K-METACOGNITION
node_type: kernel_metacognition_contract
domain: AMOS_OS_KERNEL
functional_type: MetacognitionKernel
lifecycle_stage: Architecture
claim_class: AMOS_MODEL

RSCF-RELATIONS:
  - INDEXED_BY: [[02_KERNEL/00_INDEX/KERNEL_MAP]]

  - GOVERNED_BY: [[01_CANON/AMOS_CORE_LAWS]]
  - CONSTRAINED_BY: [[01_CANON/INVARIANT_REGISTRY]]
  - PRECEDENCE_GOVERNED_BY: [[01_CANON/LAW_HIERARCHY]]
  - AUTHORITY_GOVERNED_BY: [[01_CANON/AUTHORITY_CANON]]
  - HML_GOVERNED_BY: [[01_CANON/HML_CANON]]

  - PROVENANCE_GOVERNED_BY: [[01_CANON/CANON_PROVENANCE]]
  - LINEAGE_TRACKED_BY: [[01_CANON/SOURCE_LINEAGE]]
  - CONFLICTS_TRACKED_BY: [[01_CANON/CONFLICT_REGISTRY]]
  - EVOLUTION_TRACKED_BY: [[01_CANON/SUPERSESSION_LOG]]

  - LOGIC_DEPENDS_ON: [[02_KERNEL/01_FOUNDATION/K_CORE19_LOGIC]]
  - META_LOGIC_DEPENDS_ON: [[02_KERNEL/01_FOUNDATION/K_META_LOGIC]]
  - SEMANTICS_DEPEND_ON: [[02_KERNEL/01_FOUNDATION/K_DISTINCTION_RELATION_CONSTRAINT]]
  - PRECEDENCE_DEPENDS_ON: [[02_KERNEL/01_FOUNDATION/K_LAW_HIERARCHY]]

  - EPISTEMIC_DEPENDS_ON: [[02_KERNEL/04_EPISTEMIC/README]]
  - PROVENANCE_DEPENDS_ON: [[02_KERNEL/05_PROVENANCE/README]]
  - CAUSAL_DEPENDS_ON: [[02_KERNEL/06_CAUSAL/README]]
  - DEPENDENCY_DEPENDS_ON: [[02_KERNEL/07_DEPENDENCY/README]]
  - STATE_INTERACTS_WITH: [[02_KERNEL/08_STATE/README]]
  - VALIDATED_BY: [[02_KERNEL/14_VALIDATION/README]]
  - RECOVERY_INTERACTS_WITH: [[02_KERNEL/15_RECOVERY/README]]

  - COUNTERFACTUAL_INTERACTS_WITH: [[02_KERNEL/01_FOUNDATION/K_COUNTERFACTUAL]]

  - AUTHORIZED_THROUGH: [[03_CONTROL_PLANE/00_INDEX/CONTROL_PLANE_MAP]]
  - EXECUTED_THROUGH: [[04_RUNTIME/00_INDEX/RUNTIME_MAP]]
  - KNOWLEDGE_BOUND_TO: [[11_KNOWLEDGE/00_AMOS_Full_Brain_OS_Architecture]]
  - STATE_RECORDED_IN: [[12_STATE/AUTHORITATIVE_STATE]]
  - OBSERVED_BY: [[17_OBSERVABILITY/00_INDEX/README]]
  - VERIFIED_BY: [[19_TESTS/00_INDEX/README]]
```

---

## Related

[[00_ROOT/README]] ·
[[00_ROOT/ARCHITECTURE]] ·
[[00_ROOT/SYSTEM_MAP]] ·
[[01_CANON/00_INDEX/CANON_MAP]] ·
[[01_CANON/AMOS_CORE_LAWS]] ·
[[01_CANON/INVARIANT_REGISTRY]] ·
[[01_CANON/LAW_HIERARCHY]] ·
[[01_CANON/HML_CANON]] ·
[[01_CANON/AUTHORITY_CANON]] ·
[[01_CANON/CANON_PROVENANCE]] ·
[[01_CANON/SOURCE_LINEAGE]] ·
[[01_CANON/CONFLICT_REGISTRY]] ·
[[01_CANON/SUPERSESSION_LOG]] ·
[[02_KERNEL/00_INDEX/KERNEL_MAP]] ·
[[02_KERNEL/01_FOUNDATION/K_CORE19_LOGIC]] ·
[[02_KERNEL/01_FOUNDATION/K_DISTINCTION_RELATION_CONSTRAINT]] ·
[[02_KERNEL/01_FOUNDATION/K_LAW_HIERARCHY]] ·
[[02_KERNEL/01_FOUNDATION/K_META_LOGIC]] ·
[[02_KERNEL/01_FOUNDATION/K_COUNTERFACTUAL]] ·
[[02_KERNEL/04_EPISTEMIC/README]] ·
[[02_KERNEL/05_PROVENANCE/README]] ·
[[02_KERNEL/06_CAUSAL/README]] ·
[[02_KERNEL/07_DEPENDENCY/README]] ·
[[02_KERNEL/08_STATE/README]] ·
[[02_KERNEL/14_VALIDATION/README]] ·
[[02_KERNEL/15_RECOVERY/README]] ·
[[03_CONTROL_PLANE/00_INDEX/CONTROL_PLANE_MAP]] ·
[[04_RUNTIME/00_INDEX/RUNTIME_MAP]] ·
[[11_KNOWLEDGE/00_AMOS_Full_Brain_OS_Architecture]] ·
[[12_STATE/AUTHORITATIVE_STATE]] ·
[[17_OBSERVABILITY/00_INDEX/README]] ·
[[19_TESTS/00_INDEX/README]]

```text
```

---

[[00_ROOT/00_ROOT_MOC.md|AMOS MOC]]

---
**Related:** [[00-Home]] · [[AMOS_RSCF_NODES]]
