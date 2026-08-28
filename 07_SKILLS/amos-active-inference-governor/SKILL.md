---
schema_version: 1.0
title: SKILL — Amos Active Inference Governor
type: skill
source: 07_SKILLS/amos-active-inference-governor
name: amos-active-inference-governor
description: Govern active-inference-style perception-belief-action loops inside AMOS
  by separating observations, latent-state beliefs, uncertainty, preferences or goals,
  candidate actions, expected consequences, prediction error, evidence updates, authority,
  and actual effects. Use when an AMOS agent must decide whether to update beliefs,
  gather information, act, continue observing, or stop; when prediction-error minimization
  could conflict with truth, safety, authority, or user intent; when perception and
  action form a feedback loop; or when amos-c05-mind-behavior-master routes a cognition/behavior
  task requiring bounded active inference. Treat active inference as an AMOS_MODEL
  unless independently grounded in established domain theory; never use it to claim
  consciousness, neuroscience proof, free-energy-theory validation, or autonomous
  authority. Do not use for consciousness claims, neuroscience proof, free-energy-theory
  validation, or autonomous authority beyond declared scope.
parent_skill: amos-c05-mind-behavior-master
domain: mind_behavior
origin_architect: Trang Phan
epistemic_class: AMOS_MODEL
tags:
- type/skill
- canon/skill
- domain/mind-behavior
- rscf/source_claim
- hml/m
- epistemic/amos_model
- amos_os
- 00-home
- amos-rscf-nodes
- law-hierarchy
- 07-skills-moc
- references-moc
- trang-framework-recursive-ontology-dynamics
- skill
rscf:
  state: DERIVED
  claim_class: DERIVED
  provenance: AMOS_corpus
  scope: AMOS_general
version: 1.1.0
rscf_state: SOURCE_CLAIM
hml_level: M
gmef_gates:
- L0_integrity
- L1_epistemic
- L2_provenance
- L5_scope
collapse_class: reversible
qfm_gate_set: QFM_v43
law_compliance:
- L0
- L1
- L2
- L4
- L5
- L16
- L17
license: MIT
steward: Trang Phan
---

# AMOS Active Inference Governor

## Identity

Origin architect: **Trang Phan**. Domain: mind_behavior. Parent: amos-c05-mind-behavior-master. Epistemic class: AMOS_MODEL. H/M/L: M.
## When to Use
- When an AMOS agent must decide whether to update beliefs, gather information, act, continue observing, or stop
- When prediction-error minimization could conflict with truth, safety, authority, or user intent
- When perception and action form a feedback loop requiring governed selection
- When `amos-c05-mind-behavior-master` routes a cognition/behavior task requiring bounded active inference
- When multiple competing hypotheses must be preserved under uncertainty rather than collapsed prematurely
- When an action's predicted benefit must be checked against authority, safety, and constraint gates before execution
- When managing lifecycle operations across classify, validate, trace, assess, and detect
- When detecting drift in evidence chains, provenance freshness, or confidence calibration
- When validating outputs against domain constraints and epistemic class

## Capabilities

- **aig.run_governed_loop**: Execute the 10-step governed perception-belief-action loop (OBSERVE -> INFER -> COMPARE -> GENERATE -> GOVERN -> SELECT -> ACT_OR_OBSERVE -> MEASURE -> UPDATE -> STOP_OR_CONTINUE) with every transition bounded by evidence, uncertainty, authority, safety, and scope.
- **aig.evaluate_governance_pass**: Evaluate whether a candidate action passes the governance gate: ConstraintPass AND AuthorityPass AND SafetyPass AND PolicyPass AND ScopePass AND EvidencePass AND ReversibilityPass. Reject actions that fail any gate regardless of predicted benefit.
- **aig.preserve_competing_hypotheses**: Preserve at least one competing explanation when evidence is weak, stakes are high, interpretations imply different actions, or provenance is correlated. Maintain COMPETING status until discriminating evidence appears.
- **aig.enforce_epistemic_firewall**: Enforce the active-inference epistemic firewall: ACTIVE_INFERENCE_MODEL != BIOLOGICAL_PROOF, PREDICTION_ERROR != OBJECTIVE_ERROR, BELIEF_UPDATE != TRUTH, PREFERRED_STATE != AUTHORIZED_STATE, ACTION_SELECTION != ACTION_AUTHORITY, SYSTEM_HOMEOSTASIS != CONSCIOUSNESS.
- **aig.detect_failure_modes**: Detect active-inference failure modes including MODEL_CAPTURE, PREDICTION_LOCK, CONFIRMATION_LOOP, PROXY_OPTIMIZATION, BELIEF_OVERCONFIDENCE, ACTION_BIAS, GOAL_DRIFT, AUTHORITY_DRIFT, SELF_CONFIRMING_ACTION, REWARD_HACKING, and ENDLESS_LOOP.
- **aig.select_smallest_sufficient_action**: Select the smallest sufficient admissible action considering expected usefulness, uncertainty reduction, risk, reversibility, cost, authority, and downstream dependencies. Prefer reversible information-gathering actions under uncertainty. NO_ACTION is a valid governed outcome.
- **aig.manage_lifecycle**: Manage lifecycle: classify, validate, trace, assess, detect.
- **aig.detect_drift**: Detect drift in evidence chains, provenance freshness, or confidence calibration.
- **aig.validate_outputs**: Validate outputs against domain constraints and epistemic class.


# Epistemic Firewall

Use:

`SOURCE_CLAIM | OBSERVATION | AMOS_MODEL | DERIVED | DOMAIN_EMPIRICAL | CONDITIONAL | COMPETING | UNKNOWN/GAP`

Maintain:

```text
ACTIVE_INFERENCE_MODEL != BIOLOGICAL_PROOF
PREDICTION_ERROR != OBJECTIVE_ERROR
BELIEF_UPDA

---
**Links:** 

## Related

- 
```

## Examples

- **Scenario**: When an AMOS agent must decide whether to update beliefs, gather information, act, continue observing, or stop
  - **Input**: A query matching this skill's domain (mind_behavior)
  - **Output**: Structured result with epistemic labels and provenance

- **Scenario**: When prediction-error minimization could conflict with truth, safety, authority, or user intent
  - **Input**: A query matching this skill's domain (mind_behavior)
  - **Output**: Structured result with epistemic labels and provenance

- **Scenario**: When perception and action form a feedback loop requiring governed selection
  - **Input**: A query matching this skill's domain (mind_behavior)
  - **Output**: Structured result with epistemic labels and provenance


## Validation Gates

- **L0 Integrity**: All structural elements accounted for; no silent gaps
- **L1 Epistemic**: Every claim tagged with epistemic class (SOURCE_CLAIM / DERIVED / AMOS_MODEL)
- **L5 Scope**: Analysis confined to declared scope and domain
- **L7 Authority**: No autonomous action beyond authority boundary

## Anti-Patterns

- **Do not use** for tasks outside the mind_behavior domain
- **Do not use** when the query requires empirical validation that this skill cannot provide
- **Do not use** when a parent skill or higher-level orchestrator should route instead
- **Do not bypass** epistemic class labeling — every output must carry SOURCE/DERIVED/AMOS_MODEL tags
- **Do not chain** more than 3 skills without explicit orchestrator approval


## Composition

- **Parent**: `amos-c05-mind-behavior-master` — routes to this skill when mind_behavior specialization is needed
- **Peers**: Other skills in the `mind_behavior` domain may be composed in sequence
- **Orchestrator**: The parent skill or `AMOS_HOME` orchestrates routing
- **Workflow**: Each skill has a corresponding workflow in `08_WORKFLOWS/`
- **Agent**: Each skill has a corresponding agent in `06_AGENTS/`


## Evaluation

### Success Criteria

- Output includes epistemic class label (SOURCE/DERIVED/AMOS_MODEL/EMPIRICAL)
- Output includes provenance reference to source evidence
- Output includes confidence ceiling (capped at 0.95 for DERIVED, 1.0 for SOURCE_CANON)
- Output includes gap flags for unresolved unknowns
- Output does not exceed declared scope

### Failure Modes

- **Overreach**: Output claims validity beyond its epistemic class
- **Scope creep**: Output addresses questions outside the declared domain
- **Provenance loss**: Output cannot trace back to source evidence
- **Confidence inflation**: Output confidence exceeds the weakest-premise ceiling


## Error Handling

- **On scope violation**: Reject the query and route back to parent skill
- **On missing evidence**: Flag as GAP and reduce confidence ceiling to 0.5
- **On contradiction**: Flag as CRITICAL_GAP and halt until resolved
- **On provenance loss**: Mark output as UNKNOWN and require human review
- **On drift**: Trigger drift alignment via `amos-ai-drift-alignment-governor`


## Do not use

- For generic analysis outside the mind_behavior framework
- To claim empirical validation without domain-specific evidence
- As a substitute for domain-specific evidence
- Outside mind_behavior domain reasoning

## References

- `references/pragmatic_action.md` — loaded on demand
- `references/references_MOC.md` — loaded on demand
- `` — skill Map of Content
- `amos-c05-mind-behavior-master` — parent skill
- `` — corresponding workflow
- `amos-active-inference-governor-agent` — corresponding agent
---

**Related:** [[00_HOME]] · [[AMOS_RSCF_NODES]] · [[LAW_HIERARCHY]] · [[07_SKILLS_MOC]] · [[references_MOC]]

**MOC:** [[07_SKILLS_MOC]]

**Trang Framework:** [[TRANG_FRAMEWORK_RECURSIVE_ONTOLOGY_DYNAMICS]]

---
RSCF-NODE
node_id: amos-active-inference-governor
node_type: skill
path: 07_SKILLS/amos-active-inference-governor/[[SKILL]].md
RSCF-RELATIONS:
- INDEXED_BY: [[00_HOME]]
- INDEXED_BY: [[AMOS_RSCF_NODES]]
- CHILD_OF: [[07_SKILLS_MOC]]
