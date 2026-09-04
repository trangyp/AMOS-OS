---
schema_version: 1.0
title: SKILL — Amos Adaptive Stability Balancer
type: skill
source: 07_SKILLS/amos-adaptive-stability-balancer
name: amos-adaptive-stability-balancer
description: Balance stability-preserving operation against adaptation, scaling, exploration, mutation, and recovery in AMOS runtimes. Use when a system risks collapse from excessive load, recursion, concurrency, memory pressure, dependency degradation, operational pressure, oscillation, uncontrolled adaptation, or excessive rigidity; when deciding whether to freeze, contain, degrade gracefully, maintain, recover, cautiously adapt, scale, or resume normal operation; when resource headroom, observability, resilience, dependency health, damping, saturation, collapse thresholds, or recovery capacity matter; or when amos-os-runtime-master routes a runtime stability decision. Preserve hard safety boundaries, hardware/environment scope, H/M/L coupling, bounded resources, reversibility, provenance, regime validity, and selective recovery. Stability does not mean immobility, and adaptation is never allowed to consume th Do not use for generic load balancing, network traffic routing, or tasks outside AMOS runtime stability domain.
parent_skill: amos-os-runtime-master
domain: runtime
origin_architect: Trang Phan
epistemic_class: SOURCE_CLAIM
tags:
  - type/skill
  - type/skill
  - domain/os-runtime
  - epistemic/source_claim
  - hml/m
  - epistemic/source_claim
  - amos-os
  - law-hierarchy
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
  - L7_authority
  - L8_execution
collapse_class: reversible
qfm_gate_set: QFM_v43
law_compliance:
  - L0
  - L1
  - L2
  - L4
  - L5
  - L7
  - L8
  - L16
  - L17
  - L18
license: MIT
steward: Trang Phan
---

# AMOS Adaptive Stability Balancer

## Identity

Origin architect: **Trang Phan**. Domain: runtime. Parent: amos-os-runtime-master. Epistemic class: SOURCE_CLAIM. H/M/L: M.

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

______________________________________________________________________

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
- \*\*adapti

______________________________________________________________________

**Links:** [[07_SKILLS/07_SKILLS_MOC|07_SKILLS_MOC]]

## Operations

1. **adaptive_stabil_balancer.evaluate_influence**: Evaluate whether memory may influence a pending action through the AMOS Adaptive Stability Balancer consent, provenance, and risk gates.
1. **adaptive_stabil_balancer.validate_gates**: Validate AMOS Adaptive Stability Balancer decisions against hard partition gates, epistemic class preservation, and consent state requirements.
1. **adaptive_stabil_balancer.analyze_state**: Analyze AMOS Adaptive Stability Balancer memory state: working, episodic, semantic stores, consolidation, and retrieval graph health.
1. **adaptive_stabil_balancer.trace_provenance**: Trace AMOS Adaptive Stability Balancer memory entries to source, encoding operation, consolidation history, and field-level lineage.
1. **adaptive_stabil_balancer.assess_claim**: Assess AMOS Adaptive Stability Balancer memory claims for epistemic class, freshness, contradiction status, and confidence ceiling.
1. **adaptive_stabil_balancer.manage_lifecycle**: Manage AMOS Adaptive Stability Balancer lifecycle: encode, normalize, admit, consolidate, index, retrieve, filter, update.
1. **adaptive_stabil_balancer.detect_drift**: Detect memory drift: stale entries, broken provenance, epistemic class erosion, and context discontinuity.
1. **adaptive_stabil_balancer.escalate_gaps**: Escalate AMOS Adaptive Stability Balancer memory gaps: flag UNKNOWN/GAP entries, quarantine untrusted data, trigger memory repair.
1. **adaptive_stabil_balancer.validate_outputs**: Validate outputs against domain constraints and epistemic class.
1. **adaptive_stability.monitor_stability**: Monitor runtime stability: drift, oscillation, divergence, and regime transitions
1. **adaptive_stability.calibrate_feedback**: Calibrate feedback control loops to maintain stable operating conditions
1. **adaptive_stability.decompose_primitive**: Decompose complex operations into primitive, atomic, verifiable steps
1. **adaptive_stability.align_drift**: Align AI drift back to authorized operating envelope when deviation is detected
1. **adaptive_stability.enforce_closed_loop**: Enforce closed-loop learning: every output feeds back into the next iteration
1. **adaptive_stability.manage_lifecycle**: Manage lifecycle: classify, validate, trace, assess, detect.
1. **adaptive_stability.detect_drift**: Detect drift in evidence chains, provenance freshness, or confidence calibration.
1. \*\*adapti

## Related

- [[07_SKILLS/amos-adaptive-stability-balancer/amos-adaptive-stability-balancer_MOC|amos-adaptive-stability-balancer_MOC]]

## Examples

- **Scenario**: User query requires runtime reasoning
  - **Input**: Domain-specific question or task
  - **Output**: Capability result with confidence ceiling and gap flags

## Validation Gates

- **L0 Integrity**: All structural elements accounted for; no silent gaps
- **L1 Epistemic**: Every claim tagged with epistemic class (SOURCE_CLAIM / DERIVED / AMOS_MODEL)
- **L5 Scope**: Analysis confined to declared scope and domain
- **L7 Authority**: No autonomous action beyond authority boundary

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

## Do not use

- For generic runtime analysis outside the AMOS OS/runtime framework
- To claim empirical validation of OS or runtime theories
- As a substitute for domain-specific runtime or infrastructure evidence
- Outside runtime/OS domain reasoning

## References

- `references/references_MOC.md` — loaded on demand
- `references/stability_reference.md` — loaded on demand
- \`\` — skill Map of Content
- `amos-os-runtime-master` — parent skill
- \`\` — corresponding workflow
- `amos-adaptive-stability-balancer-agent` — corresponding agent

______________________________________________________________________

**Related:** [[00_ROOT/00_HOME|00_HOME]] · [[00_ROOT/AMOS_RSCF_NODES|AMOS_RSCF_NODES]] · [[01_CANON/01_CORE_LAWS/LAW_HIERARCHY|LAW_HIERARCHY]] · [[07_SKILLS/07_SKILLS_MOC|07_SKILLS_MOC]] · references_MOC

**MOC:** [[07_SKILLS/07_SKILLS_MOC|07_SKILLS_MOC]]

**Trang Framework:** [[11_KNOWLEDGE/TRANG_FRAMEWORK_RECURSIVE_ONTOLOGY_DYNAMICS|TRANG_FRAMEWORK_RECURSIVE_ONTOLOGY_DYNAMICS]]

______________________________________________________________________

RSCF-NODE
node_id: amos-adaptive-stability-balancer
node_type: skill
path: 07_SKILLS/amos-adaptive-stability-balancer/SKILL.md
RSCF-RELATIONS:

- INDEXED_BY: [[00_ROOT/00_HOME|00_HOME]]
- INDEXED_BY: [[00_ROOT/AMOS_RSCF_NODES|AMOS_RSCF_NODES]]
- CHILD_OF: [[07_SKILLS/07_SKILLS_MOC|07_SKILLS_MOC]]
