---
title: SKILL
type: skill
source: 07_SKILLS/amos-causal-reasoning-master
name: amos-causal-reasoning-master
description: AMOS Causal Reasoning — causal closure, causal hierarchy, counterfactual reasoning, intervention analysis. 4 causal modes (Direct, Distributed, Delayed, Cascading), 6 causal gates. Use for causal a...
parent_skill: none
domain: causal
origin_architect: Trang Phan
epistemic_class: SOURCE_CANON
tags: [note, amos-causal-reasoning-master, canon/skill]
rscf:
  state: DERIVED
  claim_class: DERIVED
  provenance: AMOS_corpus
  scope: AMOS_general
version: "1.1.0"
---


# K CAUSAL HIERARCHY

## Identity

Origin architect and steward: **Trang Phan**.

This is a **parent skill** that consolidates 3 sub-skills into a single domain master.
Following the skill-organizer best practice: fewer, richer skills beat many overlapping ones.
A parent skill with clearly labeled sections is better than 3 separate shallow skills.

**Epistemic class**: SOURCE_CLAIM (vault-sourced from `02_KERNEL/03_CAUSAL/K_CAUSAL_HIERARCHY.md`).

## When to Use

- When determining whether a relationship is causal vs correlational vs associational
- When performing counterfactual reasoning or intervention analysis
- When classifying causal modes: Direct, Distributed, Delayed, Cascading
- When evaluating causal evidence strength against the causal hierarchy
- When applying the causal firewall to prevent causal overreach
- When a child skill routes a causal analysis or counterfactual task to this master

- When managing lifecycle operations across classify, validate, trace, assess, and detect
- When detecting drift in evidence chains, provenance freshness, or confidence calibration
- When validating outputs against domain constraints and epistemic class

## Capabilities

- **causal_reason.analyze_causal**: Analyze AMOS Causal Reasoning causal hierarchy: observation, intervention, counterfactual, and causal closure.
- **causal_reason.validate_causal**: Validate AMOS Causal Reasoning causal claims for identification, confounder control, and causal gate compliance.
- **causal_reason.apply_intervention**: Apply AMOS Causal Reasoning causal intervention analysis: do-calculus, effect estimation, and counterfactual mapping.
- **causal_reason.trace_causal_provenance**: Trace AMOS Causal Reasoning causal findings to observational data, intervention records, and counterfactual models.
- **causal_reason.assess_causal_claim**: Assess AMOS Causal Reasoning causal claims for identification type, evidence strength, and mechanism vs correlation.
- **causal_reason.manage_causal_lifecycle**: Manage AMOS Causal Reasoning causal lifecycle: observe, hypothesize, test, intervene, validate, and finalize.
- **causal_reason.detect_causal_drift**: Detect causal drift: confounder emergence, regime change, causal chain break, and effect decay.
- **causal_reason.escalate_causal_gaps**: Escalate AMOS Causal Reasoning causal gaps: flag unconfirmed causality, require discriminating test, trigger analysis.
- **causal_reason.manage_lifecycle**: Manage lifecycle: classify, validate, trace, assess, detect.
- **causal_reason.detect_drift**: Detect drift in evidence chains, provenance freshness, or confidence calibration.
- **causal_reason.validate_outputs**: Validate outputs against domain constraints and epistemic class.

## Vault-Sourced Domain Knowledge

> **Sources**: `_00_Cosmo brain/misc/CA/causal.md` (content_hash: 6035054c7197da54), `_00_Cosmo brain/misc/CA/CAUSAL_FIREWALL.md` (content_hash: f71dae4c4d3e7ba6) (vault canon, SOURCE_CLAIM)

### Causal Evidence Hierarchy

| Level | Class | Evidence Required |
|-------|-------|-------------------|
| 0 | descriptive | observation only |
| 1 | association | co-occurrence |
| 2 | correlation | statistical correlation |
| 3 | enabling condition | enabling factor identified |
| 4 | mediator/confounder | mediation or confounding analysis |
| 5 | mechanism | mechanistic understanding |
| 6 | intervention effect | controlled intervention |

### Causal Firewall Rules

1. A stronger causal class requires stronger evidence.
2. Sequence, co-occurrence, analogy, structural resemblance, and predictive success do not by themselves establish mechanism or intervention effect.
3. For causal counterfactuals: identify intervention variable, hold background conditions explicit, separate observed from hypothetical states, mark unidentifiable counterfactuals UNKNOWN.

### Causal Relation Types

- `association` — co-occurrence without direction
- `correlation` — statistical correlation without causation
- `enabling_condition` — necessary but not sufficient
- `mediator` — intermediate variable in causal chain
- `confounder` — common cause of both variables
- `feedback` — bidirectional causal loop
- `necessary_condition` — must be present for effect
- `sufficient_condition` — alone can produce effect
- `mechanism` — explains how cause produces effect
- `intervention_effect` — confirmed by controlled intervention

### 4 Causal Modes

- **Direct**: A → B (immediate, single-step)
- **Distributed**: A → {B1, B2, ...} (fan-out, parallel)
- **Delayed**: A →[Δt]→ B (time-lagged)
- **Cascading**: A → B → C → ... (chain reactio
- [[AGENT_TEMPLATE]]

---
**MOC:** [[amos-causal-reasoning-master_MOC]]

## Examples

- **Scenario**: When determining whether a relationship is causal vs correlational vs associational
  - **Input**: A query matching this skill's domain (causal)
  - **Output**: Structured result with epistemic labels and provenance

- **Scenario**: When performing counterfactual reasoning or intervention analysis
  - **Input**: A query matching this skill's domain (causal)
  - **Output**: Structured result with epistemic labels and provenance

- **Scenario**: When classifying causal modes: Direct, Distributed, Delayed, Cascading
  - **Input**: A query matching this skill's domain (causal)
  - **Output**: Structured result with epistemic labels and provenance


## Anti-Patterns

- **Do not use** for tasks outside the causal domain
- **Do not use** when the query requires empirical validation that this skill cannot provide
- **Do not use** when a parent skill or higher-level orchestrator should route instead
- **Do not bypass** epistemic class labeling — every output must carry SOURCE/DERIVED/AMOS_MODEL tags
- **Do not chain** more than 3 skills without explicit orchestrator approval


## Composition

- **Parent**: `[[none]]` — routes to this skill when causal specialization is needed
- **Peers**: Other skills in the `causal` domain may be composed in sequence
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


## References

- `references/counterfactual_reasoning_kernel.md` — loaded on demand
- `references/references_MOC.md` — loaded on demand
- `references/sensitivity_falsifiers.md` — loaded on demand
- `references/vault_domain_knowledge.md` — loaded on demand
- `[[amos-causal-reasoning-master_MOC]]` — skill Map of Content
- `[[none]]` — parent skill
- `[[amos-causal-reasoning-master-workflow]]` — corresponding workflow
- `[[amos-causal-reasoning-master-agent]]` — corresponding agent

