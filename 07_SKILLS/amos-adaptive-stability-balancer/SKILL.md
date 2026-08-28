---
title: "SKILL — Amos Adaptive Stability Balancer"
type: skill
source: 07_SKILLS/amos-adaptive-stability-balancer
name: amos-adaptive-stability-balancer
description: Balance stability-preserving operation against adaptation, scaling, exploration, mutation, and recovery in AMOS runtimes. Use when a system risks collapse from excessive load, recursion, concurrency, memory pressure, dependency degradation, operational pressure, oscillation, uncontrolled adaptation, or excessive rigidity; when deciding whether to freeze, contain, degrade gracefully, maintain, recover, cautiously adapt, scale, or resume normal operation; when resource headroom, observability, resilience, dependency health, damping, saturation, collapse thresholds, or recovery capacity matter; or when amos-os-runtime-master routes a runtime stability decision. Preserve hard safety boundaries, hardware/environment scope, H/M/L coupling, bounded resources, reversibility, provenance, regime validity, and selective recovery. Stability does not mean immobility, and adaptation is never allowed to consume the reserves required for survival.
parent_skill: amos-os-runtime-master
domain: runtime
origin_architect: Trang Phan
epistemic_class: SOURCE_CLAIM
tags: [note, amos-adaptive-stability-balancer, canon/skill]
rscf:
  state: DERIVED
  claim_class: DERIVED
  provenance: AMOS_corpus
  scope: AMOS_general
version: "1.1.0"
---


# AMOS Adaptive Stability Balancer

## Identity

**Origin architect and steward:** Trang Phan

## When to Use

Use this skill when balancing system stability against adaptive change, detecting stability regime transitions (STABLE/ADAPTIVE/STRAINED/DEGRADED/RECOVERY/SAFE_MODE/CRITICAL/COLLAPSE_RISK/UNKNOWN), or governing resource/reserve/environment/stability/adaptation integrity across the AMOS runtime.

**Parent skill:** `amos-os-runtime-master`

**Domain:** runtime / stability / resilience / adaptive control

**Primary epistemic status:** `SOURCE_CLAIM` for vault-defined runtime structures and constraints; `AMOS_MODEL` for new synthesis or control equations introduced by this Skill.

The Adaptive Stability Balancer governs the tension between:

```text
STABILITY
↔
ADAPTATION
```

Its central question is:

> Given the current load, reserves, dependency health, resource pressure, uncertainty, observability, recovery capacity, regime, and proposed change, should the system preserve, contain, recover, adapt, scale, degrade, freeze, or stop?

The Skill exists because both extremes can fail:

```text
TOO_STABLE
→ rigidity
→ inability to adapt
→ accumulating mismatch
→ eventual fragility

TOO_ADAPTIVE
→ churn
→ resource depletion
→ instability
→ cascading failure
```

The target is not maximum stability or maximum adaptation.

The target is:

```text
VIABLE_ADAPTIVE_STABILITY
```

within current constraints.

---

## Capabilities

- **adaptive_stabil_balancer.evaluate_influence**: Evaluate whether memory may influence a pending action through the AMOS Adaptive Stability Balancer consent, provenance, and risk gates.
- **adaptive_stabil_balancer.validate_gates**: Validate AMOS Adaptive Stability Balancer decisions against hard partition gates, epistemic class preservation, and consent state requirements.
- **adaptive_stabil_balancer.analyze_state**: Analyze AMOS Adaptive Stability Balancer memory state: working, episodic, semantic stores, consolidation, and retrieval graph health.
- **adaptive_stabil_balancer.trace_provenance**: Trace AMOS Adaptive Stability Balancer memory entries to source, encoding operation, consolidation history, and field-level lineage.
- **adaptive_stabil_balancer.assess_claim**: Assess AMOS Adaptive Stability Balancer memory claims for epistemic class, freshness, contradiction status, and confidence ceiling.
- **adaptive_stabil_balancer.manage_lifecycle**: Manage AMOS Adaptive Stability Balancer lifecycle: encode, normalize, admit, consolidate, index, retrieve, filter, update.
- **adaptive_stabil_balancer.detect_drift**: Detect memory drift: stale entries, broken provenance, epistemic class erosion, and context discontinuity.
- **adaptive_stabil_balancer.escalate_gaps**: Escalate AMOS Adaptive Stability Balancer memory gaps: flag UNKNOWN/GAP entries, quarantine untrusted data, trigger memory repair.
- **adaptive_stabil_balancer.validate_outputs**: Validate outputs against domain constraints and epistemic class.
- **adaptive_stability.monitor_stability**: Monitor runtime stability: drift, oscillation, divergence, and regime transitions
- **adaptive_stability.calibrate_feedback**: Calibrate feedback control loops to maintain stable operating conditions
- **adaptive_stability.decompose_primitive**: Decompose complex operations into primitive, atomic, verifiable steps
- **adaptive_stability.align_drift**: Align AI drift back to authorized operating envelope when deviation is detected
- **adaptive_stability.enforce_closed_loop**: Enforce closed-loop learning: every output feeds back into the next iteration
- **adaptive_stability.manage_lifecycle**: Manage lifecycle: classify, validate, trace, assess, detect.
- **adaptive_stability.detect_drift**: Detect drift in evidence chains, provenance freshness, or confidence calibration.
- **adapti

---
**Links:** [[07_SKILLS_MOC]]

## Related

- [[amos-adaptive-stability-balancer_MOC]]

## Examples

- **Scenario**: User query requires runtime reasoning
  - **Input**: Domain-specific question or task
  - **Output**: Capability result with confidence ceiling and gap flags


## Anti-Patterns

- **Do not use** for tasks outside the runtime domain
- **Do not use** when the query requires empirical validation that this skill cannot provide
- **Do not use** when a parent skill or higher-level orchestrator should route instead
- **Do not bypass** epistemic class labeling — every output must carry SOURCE/DERIVED/AMOS_MODEL tags
- **Do not chain** more than 3 skills without explicit orchestrator approval


## Composition

- **Parent**: `amos-os-runtime-master` — routes to this skill when runtime specialization is needed
- **Peers**: Other skills in the `runtime` domain may be composed in sequence
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

- `references/references_MOC.md` — loaded on demand
- `references/stability_reference.md` — loaded on demand
- `[[amos-adaptive-stability-balancer_MOC]]` — skill Map of Content
- `amos-os-runtime-master` — parent skill
- `[[amos-adaptive-stability-balancer-workflow]]` — corresponding workflow
- `amos-adaptive-stability-balancer-agent` — corresponding agent
---

**Related:** [[00_HOME]] · [[AMOS_RSCF_NODES]] · [[LAW_HIERARCHY]] · [[07_SKILLS_MOC]] · [[references_MOC]]

**MOC:** [[07_SKILLS_MOC]]

**Trang Framework:** [[TRANG_FRAMEWORK_RECURSIVE_ONTOLOGY_DYNAMICS]]

---
RSCF-NODE
node_id: amos-adaptive-stability-balancer
node_type: skill
path: 07_SKILLS/amos-adaptive-stability-balancer/SKILL.md
RSCF-RELATIONS:
- INDEXED_BY: [[00_HOME]]
- INDEXED_BY: [[AMOS_RSCF_NODES]]
- CHILD_OF: [[07_SKILLS_MOC]]
