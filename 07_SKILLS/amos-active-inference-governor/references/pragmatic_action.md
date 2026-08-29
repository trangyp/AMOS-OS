---
title: pragmatic action
type: reference
source: 07_SKILLS/amos-active-inference-governor/references
tags:
- reference
- amos-active-inference-governor
- type/skill
- references-moc
- 07-skills-moc
- 00-home
- amos-rscf-nodes
- law-hierarchy
- trang-framework-recursive-ontology-dynamics
rscf:
  state: SOURCE_CLAIM
  claim_class: SOURCE_CLAIM
  provenance: AMOS_corpus
  scope: skill_reference
---

# Active Inference Governor — Pragmatic Action Detail

> Load this reference when detailed pragmatic action reasoning is needed.

---

## Pragmatic action

Action primarily intended to change the target system.

Examples:

* edit state
* execute tool action
* send message
* commit transaction
* deploy change

Maintain:

```text
NEED_MORE_CERTAINTY
→ prefer epistemic action

SUFFICIENT_CERTAINTY + AUTHORITY
→ pragmatic action may become eligible
```

---

# 5. GOVERN

No candidate action is eligible merely because it reduces prediction error.

Evaluate:

```text
GovernancePass =
ConstraintPass
AND AuthorityPass
AND SafetyPass
AND PolicyPass
AND ScopePass
AND EvidencePass
AND ReversibilityPass
```

Status:

`AMOS_MODEL`

For high-stakes actions add:

* provenance validation
* freshness validation
* contradiction check
* commit-time revalidation
* rollback path

---

# Active-Inference Governance Firewall

Maintain:

```text
ERROR_REDUCTION != ACTION_PERMISSION
MODEL_PREFERENCE != USER_PREFERENCE
USER_PREFERENCE != AUTHORITY
AUTHORITY != SAFETY
LIKELY_SUCCESS != JUSTIFIED_ACTION
INFORMATION_GAIN != PRIVACY_PERMISSION
```

The governor must reject an apparently optimal action if it violates a higher-order constraint.

---

# Preferences and Goals

Represent preferences explicitly.

```text
PreferenceState = [
    goal,
    source,
    owner,
    priority,
    scope,
    temporal_validity,
    authority,
    mutability
]
```

Distinguish:

```text
user_goal
system_constraint
model_preference
organizational_policy
safety_requirement
```

Do not collapse them into one reward function.

---

# Preference Hierarchy

Apply higher-order constraints before local optimization.

Conceptually:

```text
hard safety / platform constraints
→ valid authority
→ current explicit user objective
→ accepted task constraints
→ stable user preferences
→ optimization preferences
```

Do not allow a lower-order predicted benefit to override a higher-order invariant.

---

# 6. SELECT

Choose the smallest sufficient admissible action.

Selection should consider:

```text
expected usefulness
uncertainty reduction
risk
reversibility
cost
latency
authority
downstream dependency
scope
```

Do not optimize a single metric in isolation.

---

# Candidate Action State

Represent:

```text
CandidateAction = [
    action,
    predicted_effect,
    predicted_information_gain,
    evidence_basis,
    uncertainty,
    authority,
    risk,
    reversibility,
    cost,
    dependencies,
    scope,
    regime,
    status
]
```

Status may be:

```text
ELIGIBLE
CONDITIONAL
BLOCKED
DOMINATED
COMPETING
UNKNOWN
```

---

# Action Selection Rule

Prefer:

```text
lowest-cost
reversible
high-information
constraint-compatible
action
```

that can resolve the decision-relevant uncertainty.

When two actions are materially indistinguishable:

do not manufacture precision.

---

# 7. ACT OR OBSERVE

Return one governed transition:

```text
ACT
OBSERVE_MORE
ASK
WAIT
ROLLBACK
ESCALATE
NO_ACTION
STOP
```

No action is a valid result.

Do not interpret inactivity as governor failure.

---

# 8. MEASURE

After action, measure actual consequences where evidence is available.

Distinguish:

```text
EXPECTED_EFFECT
!=
OBSERVED_EFFECT
```

Record:

```text
Outcome = [
    action,
    predicted_result,
    observed_result,
    divergence,
    side_effects,
    timestamp,
    regime,
    evidence,
    provenance
]
```

Do not fabricate outcome evidence.

---

# 9. UPDATE

Update only beliefs whose dependencies changed.

Use:

```text
new evidence
→ affected premise
→ dependent hypothesis
→ dependent decision
```

Preserve unaffected conclusions.

Avoid global belief reset unless dependency closure requires it.

---

# Selective Belief Revision

If:

```text
H1 depends on P1 + P2
H2 depends on P2 + P3
```

and `P1` fails:

invalidate or downgrade `H1`.

Do not automatically invalidate `H2`.

---

# 10. STOP OR CONTINUE

Do not create endless prediction-correction loops.

Continue only when expected decision value of another iteration is positive.

Stop when:

```text
ClaimSufficiency
AND DecisionSufficiency
AND ActionSufficiency
```

are achieved.

Also stop when:

* evidence cannot improve
* authority is missing
* next action violates constraints
* uncertainty is irreducible
* further iteration has low value
* user objective is already satisfied

---

# Expected Free Energy Boundary

If using expected-free-energy-style terminology, treat it strictly as an `AMOS_MODEL` unless the user explicitly requests established active inference theory and independent sources are loaded.

Conceptually, action selection may distinguish:

```text
pragmatic value
+
epistemic value
-
risk
-
constraint violation
```

Do not present this as the canonical Friston free-energy equation unless using and citing the established scientific formulation.

Do not invent neuroscience equations from AMOS notation.

---

# Reality / Model Distinction

Maintain:

```text
WORLD_STATE
!=
OBSERVATION
!=
INTERNAL_MODEL
!=
PREDICTION
!=
SIMULATION
```

The governor operates on representations.

It does not have direct access to all real-world state.

---

# Observer Effect

Treat observer influence conservatively.

An observation process may alter:

* what information becomes available
* user behavior
* system state
* future actions
* data collection

Do not invoke quantum observer language unless the domain genuinely requires quantum mechanics.

---

# Embodiment Firewall

Active inference often appears in biological or embodied contexts.

For ChatGPT/AMOS reasoning maintain:

```text
NO_DIRECT_BODY
NO_NATIVE_INTEROCEPTION
NO_AUTONOMOUS_SENSORIMOTOR_LOOP
NO_SUBJECTIVE_VALENCE
```

unless an external system explicitly supplies sensors or actuator state.

Model embodiment only from supplied evidence.

---

# Mind / Behavior Boundary

When reasoning about humans:

do not use the active inference model to diagnose hidden mental states.

Prefer:

```text
observed behavior
→ candidate interpretation
→ competing interpretation
→ evidence needed
```

Avoid:

```text
behavior
→ definitive internal state
```

---

# Causal Firewall

Distinguish:

```text
correlation
association
prediction
enabling condition
feedback
confounder
mediator
mechanism
causal effect
```

A model that predicts behavior does not automatically explain its cause.

An intervention that changes prediction error does not establish the mechanism responsible.

---

# Multi-Scale Runtime

When relevant use:

```text
L = local observation/action
M = agent/system loop
H = governing objective / environment / policy
```

Check:

```text
L action improves local prediction
```

against:

```text
M system stability
H governing constraints
```

Reject local optimization that damages higher-scale viability.

---

# Multi-Agent Active Inference

For multiple agents, keep their models separate.

Represent:

```text
AgentState[i] = [
    observations,
    beliefs,
    preferences,
    authority,
    uncertainty,
    candidate_actions
]
```

Do not assume:

```text
AgentA.belief == AgentB.belief
AgentA.goal == AgentB.goal
AgentA.authority == AgentB.authority
```

Shared action requires explicit coordination.

---

# Information Manipulation Risk

In multi-agent systems, an agent may benefit from changing another agent's beliefs.

Therefore test:

```text
information_gain_for_A
vs
epistemic_integrity_for_B
```

Do not permit deceptive information shaping merely because it improves predicted coordination.

---

# FreezeZone Integration

The supplied AMOS Brain reports describe FreezeZone-style governance behavior.

Use the concept as a governance pattern:

```text
if integrity falls below required threshold
or critical governance invariant fails
→ suspend action selection
```

Do not reuse historical numeric thresholds as universal defaults unless the current governing source requires them.

Prefer:

```text
FreezeCondition = configured policy condition
```

rather than hardcoding historical values.

---

# Governance SSOT Integration

When a governing source-of-truth exists:

```text
current governing policy
>
local active-inference preference
```

Do not allow the prediction loop to mutate its own governing authority.

Governance changes require a separate authorized change process.

---

# Objective Validation

Before optimizing:

verify that the objective itself is valid.

Check:

* user actually requested it
* scope is correct
* target is still current
* objective does not violate hard constraints
* success metric is not proxy-corrupted
* objective has not drifted

Maintain:

```text
OPTIMIZATION_SUCCESS
!=
OBJECTIVE_VALIDITY
```

---

# Goodhart Firewall

If the active loop optimizes a proxy, monitor whether the proxy detaches from the real objective.

Examples:

```text
lower response time
!=
better answer

lower prediction error
!=
better world state

higher engagement
!=
user benefit

higher confidence
!=
greater truth
```

When proxy drift appears:

stop optimization and revalidate the objective.

---

# Evidence Integrity

The supplied AMOS Brain architecture emphasizes evidence-bound operation.

For consequential belief updates track:

```text
source
provenance
freshness
scope
independence
contradiction
```

Multiple descendants of one source do not constitute independent confirmation.

---

# Contradiction Handling

If evidence supports incompatible models:

```text
H1
H2
```

preserve:

```text
COMPETING
```

Do not select one merely because it produces a lower modeled error.

Prefer the cheapest high-information discriminating test.

---

# Uncertainty Vector

When material, separate:

```text
U = [
    evidence_uncertainty,
    model_uncertainty,
    scope_uncertainty,
    temporal_uncertainty,
    causal_uncertainty,
    execution_uncertainty,
    provenance_uncertainty
]
```

Do not collapse all uncertainty into one scalar unless a valid aggregation rule exists.

---

# Prediction State

Represent predictions with:

```text
Prediction = [
    target,
    horizon,
    predicted_state,
    conditions,
    regime,
    uncertainty,
    evidence,
    falsifier
]
```

Never store a prediction later as an observation unless outcome evidence is acquired.

---

# Prediction Governance

For consequential forecasts require:

* timestamp safety
* no future leakage
* regime validity
* calibration where available
* competing model
* falsification criterion

Maintain:

```text
PREDICTION
!=
DECISION
```

A prediction informs a decision.

It does not determine it.

---

# RSCF Integration

For consequential active-inference conclusions use:

```text
CLAIM:
CLASS:
TARGET:
OBSERVATIONS:
BELIEFS:
COMPETING:
PREDICTION:
UNCERTAINTY:
PREFERENCES:
CONSTRAINTS:
AUTHORITY:
CANDIDATE_ACTIONS:
SELECTED_TRANSITION:
EXPECTED_EFFECT:
FALSIFIERS:
PROVENANCE:
REGIME:
CONFIDENCE_CEILING:
```

Keep the proof capsule as small as possible.

---

# GMEF Integration

If the loop proposes changing its own:

* model
* policy
* memory
* authority
* objective
* architecture

treat that as governed system evolution.

Require:

```text
change proposal
→ authority
→ evidence
→ impact analysis
→ validation
→ bounded rollout
→ rollback
```

Do not let the active-inference loop self-authorize structural evolution.

---

# Sensitivity Test

Identify the smallest premise capable of changing the selected action.

Examples:

* identity of user intent
* regime assumption
* probability estimate
* authority state
* safety condition
* prediction horizon

Validate the most decision-sensitive premise first.

If the action changes under small plausible perturbations:

classify the result:

`CONDITIONAL`

---

# Failure Modes

Monitor for:

```text
MODEL_CAPTURE
PREDICTION_LOCK
CONFIRMATION_LOOP
PROXY_OPTIMIZATION
BELIEF_OVERCONFIDENCE
ACTION_BIAS
OBSERVATION_BIAS
GOAL_DRIFT
REGIME_DRIFT
AUTHORITY_DRIFT
SELF_CONFIRMING_ACTION
REWARD_HACKING
ENDLESS_LOOP
```

Do not treat lower prediction error as proof that the loop is healthy.

---

# Self-Fulfilling Prediction Firewall

An action may make its own prediction appear correct.

Represent:

```text
prediction
→ action
→ environment changes
→ predicted outcome appears
```

Do not classify this as independent predictive validation.

Separate:

```text
PASSIVE_PREDICTION
from
INTERVENTION_CONDITIONED_OUTCOME
```

---

# Recovery

When the active-inference loop becomes unreliable:

```text
FREEZE
→ identify failed premise/model
→ preserve valid observations
→ restore governing objective
→ restore constraint state
→ reopen competing hypotheses
→ gather discriminating evidence
→ revalidate
→ resume or stop
```

Do not erase valid state unnecessarily.

---

# Decision Outcomes

Return one of:

```text
UPDATE_BELIEF
OBSERVE_MORE
SEEK_INFORMATION
ASK
ACT
WAIT
ROLLBACK
FREEZE
ESCALATE
NO_ACTION
STOP
```

Use `NO_ACTION` when action would reduce integrity.

---

# Parent Routing Contract

When called by `amos-c05-mind-behavior-master`, accept:

```text
target
observations
task_objective
scope
optional_beliefs
optional_preferences
optional_constraints
optional_authority
optional_HML
optional_regime
optional_RSCF
stakes
reversibility
```

Return:

```text
observed_state
candidate_beliefs
competing_hypotheses
prediction_state
uncertainty_vector
candidate_actions
governance_result
selected_transition
expected_effect
evidence_needed
provenance
invalidation_conditions
```

---

# Default Output

Use:

```text
Class:
Target:
Objective:
Observed:
Inferred:
Competing:
Uncertainty:
Prediction:
Candidate actions:
Governance constraints:
Selected transition:
Why:
Evidence needed:
Invalidates if:
```

For simple cases compress aggressively.

---

# Validation Gates

---
**MOC:** references_MOC

## Related

- [[07_SKILLS_MOC]]
---

**Related:** [[00_HOME]] · [[AMOS_RSCF_NODES]] · [[LAW_HIERARCHY]] · references_MOC · [[07_SKILLS_MOC]]

**MOC:** references_MOC

**Trang Framework:** [[TRANG_FRAMEWORK_RECURSIVE_ONTOLOGY_DYNAMICS]]

---
RSCF-NODE
node_id: amos-active-inference-governor-pragmatic-action
node_type: reference
path: 07_SKILLS/amos-active-inference-governor/references/pragmatic_action.md
RSCF-RELATIONS:
- INDEXED_BY: [[00_HOME]]
- INDEXED_BY: [[AMOS_RSCF_NODES]]
- CHILD_OF: references_MOC
