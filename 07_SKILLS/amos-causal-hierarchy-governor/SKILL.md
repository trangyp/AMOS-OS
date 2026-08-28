---
title: "SKILL — Amos Causal Hierarchy Governor"
type: skill
source: 07_SKILLS/amos-causal-hierarchy-governor
name: amos-causal-hierarchy-governor
description: Causal Hierarchy Governor — causal reasoning capability. Use when causal analysis, counterfactual reasoning, or intervention design. Use when amos-causal-reasoning-master routes to this specialized capability.
parent_skill: amos-causal-reasoning-master
domain: causal
origin_architect: Trang Phan
epistemic_class: SOURCE_CLAIM
tags: [note, amos-causal-hierarchy-governor, canon/skill]
rscf:
  state: DERIVED
  claim_class: DERIVED
  provenance: AMOS_corpus
  scope: AMOS_general
version: "1.1.0"
---


# Causal Hierarchy Governor

## Identity

- **Origin architect and steward**: Trang Phan
- **Parent skill**: `amos-causal-reasoning-master`
- **Domain**: causal
- **Epistemic class**: SOURCE_CLAIM (vault-sourced from AMOS framework)

Causal reasoning engine for Causal Hierarchy Governor

## When to Use

- When validating causal abstraction across model levels
- When enforcing causal closure: every effect has a sufficient cause
- When governing causal hierarchy: direct, distributed, delayed, cascading
- When reasoning counterfactually about alternative interventions
- When the parent skill (`amos-causal-reasoning-master`) routes to this specialized capability
- When managing lifecycle operations across classify, validate, trace, assess, and detect
- When detecting drift in evidence chains, provenance freshness, or confidence calibration
- When validating outputs against domain constraints and epistemic class

## Capabilities

- **causal_hierarchy.validate_abstraction**: Validate causal abstraction: does the higher-level model preserve causal structure?
- **causal_hierarchy.enforce_closure**: Enforce causal closure: every effect must have a sufficient cause within the system
- **causal_hierarchy.govern_hierarchy**: Govern causal hierarchy: direct, distributed, delayed, and cascading causes
- **causal_hierarchy.reason_counterfactual**: Reason counterfactually: what would happen under alternative interventions
- **causal_hierarchy.manage_lifecycle**: Manage lifecycle: classify, validate, trace, assess, detect.
- **causal_hierarchy.detect_drift**: Detect drift in evidence chains, provenance freshness, or confidence calibration.
- **causal_hierarchy.validate_outputs**: Validate outputs against domain constraints and epistemic class.

> **Reference**: See `references/vault_domain_knowledge.md` (content_hash: bb37fb0ccd2e02eb) for the full vault-sourced domain knowledge (7512 chars).

## 11_KNOWLEDGE Vault Content

> **Source**: `_00_Cosmo brain/amos-general/A/Vortical/AMOS_Vortical_Persistence_Deep_RSCF_Architecture.md` (content_hash: f9b18a9e22c3fb1d) (vault canon, SOURCE_CLAIM)
> **Additional source**: `_00_Cosmo brain/quantum/Quantum Causality Layer Architecture™ (QCLA) – Off.md` (content_hash: c2c419978ef0d79e) (vault canon, SOURCE_CLAIM)

### Causal Hierarchy Governor

From Cosmo Brain Vortical Persistence RSCF Architecture: Causal hierarchy governor with epistemic partition. From QCLA: Quantum causality layer architecture.

**Vortical persistence model**:
- **Persistence**: continued preservation of system identity under flow/disturbance/dissipation/regime change
- **Dissolution**: when load-bearing identity invariants fail
- **Causal hierarchy**: multiple levels of causal reasoning with epistemic partition

**Epistemic partition for causal claims**:
- SOURCE_CLAIM: source-declared causal claim
- DOMAIN_EMPIRICAL: empirically validated causal claim
- AMOS_MODEL: AMOS model causal claim
- DERIVED: derived causal claim
- COMPETING: competing causal hypothesis
- UNKNOWN/GAP: unknown causal relationship
- DECISION: decision-relevant causal claim

**Causal hierarchy levels**:
- **L1 Direct causation**: A directly causes B (no intermediaries)
- **L2 Distributed causation**: multiple causes contribute to an effect
- **L3 Delayed causation**: cause and effect are separated in time
- **L4 Cascading causation**: cause propagates through a chain of effects

**H/M/L mapping**: causal claims checked at H (whole system), M (subsystem), L (local event) levels

**Governance laws**:
- `DIRECT != DISTRIBUTED`: direct causation is not distributed causation
- `CAUSE != CORRELATION`: causal claims require causal evidence
- `PERSISTENCE != PERMANENCE`: persistence is continued preservation; it is not permanence

### Epistemic Boundary

Causal hierarchy governance is an epistemic construct. It does not prove causation, that the hierarchy is complete, or that causal levels are always correctly classified.

## Failure Modes

- **Insufficient evidence**: If source material is insufficient, mark as UNKNOWN/GAP and fail closed — do not fabricate.
- **Scope violation**: If the query falls outside the skill's declared scope, escalate to the parent skill or steward.
- **Binding broken**: If 1:1:1 binding (skill→agent→workflow) is broken, flag routing mismatch and block execution.
- **Validation failure**: If validation gates fail, downgrade confidence, flag the gap, and escalate — do not force-fit.
- **Epistemic overreach**: If a claim exceeds the established evidence or epistemic class, retract and re

---
**Links:** [[07_SKILLS_MOC]]

## Related

- [[amos-causal-hierarchy-governor_MOC]]

## Examples

- **Scenario**: When validating causal abstraction across model levels
  - **Input**: A query matching this skill's domain (causal)
  - **Output**: Structured result with epistemic labels and provenance

- **Scenario**: When enforcing causal closure: every effect has a sufficient cause
  - **Input**: A query matching this skill's domain (causal)
  - **Output**: Structured result with epistemic labels and provenance

- **Scenario**: When governing causal hierarchy: direct, distributed, delayed, cascading
  - **Input**: A query matching this skill's domain (causal)
  - **Output**: Structured result with epistemic labels and provenance


## Anti-Patterns

- **Do not use** for tasks outside the causal domain
- **Do not use** when the query requires empirical validation that this skill cannot provide
- **Do not use** when a parent skill or higher-level orchestrator should route instead
- **Do not bypass** epistemic class labeling — every output must carry SOURCE/DERIVED/AMOS_MODEL tags
- **Do not chain** more than 3 skills without explicit orchestrator approval


## Composition

- **Parent**: `amos-causal-reasoning-master` — routes to this skill when causal specialization is needed
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

- `references/references_MOC.md` — loaded on demand
- `references/vault_domain_knowledge.md` — loaded on demand
- `[[amos-causal-hierarchy-governor_MOC]]` — skill Map of Content
- `amos-causal-reasoning-master` — parent skill
- `[[amos-causal-hierarchy-governor-workflow]]` — corresponding workflow
- `amos-causal-hierarchy-governor-agent` — corresponding agent
---

**Related:** [[00_HOME]] · [[AMOS_RSCF_NODES]] · [[LAW_HIERARCHY]] · [[07_SKILLS_MOC]] · [[references_MOC]]

**MOC:** [[07_SKILLS_MOC]]

**Trang Framework:** [[TRANG_FRAMEWORK_RECURSIVE_ONTOLOGY_DYNAMICS]]

---
RSCF-NODE
node_id: amos-causal-hierarchy-governor
node_type: skill
path: 07_SKILLS/amos-causal-hierarchy-governor/SKILL.md
RSCF-RELATIONS:
- INDEXED_BY: [[00_HOME]]
- INDEXED_BY: [[AMOS_RSCF_NODES]]
- CHILD_OF: [[07_SKILLS_MOC]]
