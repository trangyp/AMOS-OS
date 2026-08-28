---
title: SKILL — Amos Causal Closure Governor
type: skill
source: 07_SKILLS/amos-causal-closure-governor
name: amos-causal-closure-governor
description: Causal Closure Governor — causal reasoning capability. Use when causal
  analysis, counterfactual reasoning, or intervention design. Use when amos-causal-reasoning-master
  routes to this specialized capability.
parent_skill: amos-causal-reasoning-master
domain: causal
origin_architect: Trang Phan
epistemic_class: SOURCE_CLAIM
tags:
- type/skill
- canon/skill
- domain/causal-reasoning
- canon-group/tech-ai
- topic/causality
- capability/causal-reasoning
- capability/governance
- capability/closure
- capability/cosmo_brain_vault_content
- rscf/epistemic
- rscf/C-constraint
- rscf/G-relation
- rscf/S-state
- rscf/T-topology
- rscf/type-model
- sota/progressive-disclosure
- sota/anti-patterns
- amos_os
- amos-causal-closure-governor
rscf:
  state: DERIVED
  claim_class: DERIVED
  provenance: AMOS_corpus
  scope: AMOS_general
version: 1.1.0
rscf_state: SOURCE_CLAIM
hml_level: H
gmef_gates:
- L0_integrity
- L1_epistemic
- L2_provenance
- L5_scope
- L24_causal_epoch
collapse_class: reversible
qfm_gate_set: QFM_v43
law_compliance:
- L0
- L1
- L2
- L4
- L5
- L7
- L16
- L17
- L18
- L24
---







# Causal Closure Governor

## Identity

Origin architect: **Trang Phan**. Domain: causal. Parent: amos-causal-reasoning-master. Epistemic class: SOURCE_CLAIM. H/M/L: H.
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

- **causal_closure.validate_abstraction**: Validate causal abstraction: does the higher-level model preserve causal structure?
- **causal_closure.enforce_closure**: Enforce causal closure: every effect must have a sufficient cause within the system
- **causal_closure.govern_hierarchy**: Govern causal hierarchy: direct, distributed, delayed, and cascading causes
- **causal_closure.reason_counterfactual**: Reason counterfactually: what would happen under alternative interventions
- **causal_closure.manage_lifecycle**: Manage lifecycle: classify, validate, trace, assess, detect.
- **causal_closure.detect_drift**: Detect drift in evidence chains, provenance freshness, or confidence calibration.
- **causal_closure.validate_outputs**: Validate outputs against domain constraints and epistemic class.

> **Reference**: See `references/vault_domain_knowledge.md` (content_hash: fe5db79e174e18cc) for the full vault-sourced domain knowledge (5270 chars).

## Cosmo Brain Vault Content

> **Source**: `_00_Cosmo brain/trang/trang_amos_reality_architecture_master_max_detail.md` (vault canon, SOURCE_CLAIM)

### Causal Closure Principle

Causal closure states that every physical effect has a sufficient physical cause. Applied to AMOS:

**Causal closure law**: Every system state change must trace to a sufficient causal chain within the system's declared boundary.

**Closure requirements**:
- Every effect has a cause within the system boundary
- No "spooky action" -- uncaused state changes are flagged as UNKNOWN/GAP
- Causal chains must be traceable through the provenance graph
- External inputs are causes at the boundary, not violations of closure

### 6 Causal Modes

| Mode | Description | Example |
|------|-------------|---------|
| C0 Direct | A causes B directly | Function call returns value |
| C1 Distributed | Multiple causes converge | Multiple evidence sources support a claim |
| C2 Delayed | Cause precedes effect in time | Memory encoding enables later retrieval |
| C3 Cascading | Cause triggers chain | Gap detection triggers repair triggers validation |
| C4 Feedback | Effect feeds back to cause | Learning loop updates inference |
| C5 Counterfactual | What would happen without cause | Falsifier testing |

### Anti-Faking Mechanism

Causal closure governance includes anti-faking mechanisms that penalize:
- Narrative drift: claims that drift from their causal origin
- Deception gaps: missing causal links presented as complete
- Unsupported speculation: claims without causal backing

### Epistemic Boundary

Causal closure is an architectural principle, not a metaphysical claim. It does not prove determinism, physicalism, or the impossibility of emergent causation. It is a governance constraint, not a physics theorem.

## Failure Modes
- **Insufficient evidence**: If source material is insufficient, mark as UNKNOWN/GAP and fail closed — do not fabricate.
- **Scope violation**: If the query falls outside the skill's declared scope, escalate to the parent skill or steward.
- **Binding broken**: If 1:1:1 binding (skill→agent→workflow) is broken, flag routing mismatch and block execution.
- **Validation failure**: If validation gates fail, downgrade confidence, flag the gap, and escalate — do not force-fit.
- **Epistemic overreach**: If a claim exceeds the established evidence or epistemic class, retract and relabel.

## Validation Gates

- **G1 (Law of Law)**: No unresolved contradictions within the skill's scope.
- **G2 (Epistemic class)**: All claims labeled SOURCE / DERIVED / AMOS_MODEL / EMPIRICAL — never claim beyond evidence.
- **G3 (Provenance)**: Source path recorded

---
**Links:** [[07_SKILLS_MOC]]

## Related

- [[amos-causal-closure-governor_MOC]]

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
- `[[amos-causal-closure-governor_MOC]]` — skill Map of Content
- `amos-causal-reasoning-master` — parent skill
- `[[amos-causal-closure-governor-workflow]]` — corresponding workflow
- `amos-causal-closure-governor-agent` — corresponding agent
---

**Related:** [[00_HOME]] · [[AMOS_RSCF_NODES]] · [[LAW_HIERARCHY]] · [[07_SKILLS_MOC]] · [[references_MOC]]

**MOC:** [[07_SKILLS_MOC]]

**Trang Framework:** [[TRANG_FRAMEWORK_RECURSIVE_ONTOLOGY_DYNAMICS]]

---
RSCF-NODE
node_id: amos-causal-closure-governor
node_type: skill
path: 07_SKILLS/amos-causal-closure-governor/SKILL.md
RSCF-RELATIONS:
- INDEXED_BY: [[00_HOME]]
- INDEXED_BY: [[AMOS_RSCF_NODES]]
- CHILD_OF: [[07_SKILLS_MOC]]
