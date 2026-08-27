---
title: SKILL
type: skill
source: 07_SKILLS/amos-agency-consequence-governor
name: amos-agency-consequence-governor
description: Agency Consequence Governor — agent systems capability. Use when agent design, delegation reasoning, or multi-agent governance. Use when amos-agent-systems-master routes to this specialized capability.
parent_skill: amos-agent-systems-master
domain: agent
origin_architect: Trang Phan
epistemic_class: SOURCE_CLAIM
tags: [note, amos-agency-consequence-governor, canon/skill]
rscf:
  state: DERIVED
  claim_class: DERIVED
  provenance: AMOS_corpus
  scope: AMOS_general
version: "1.1.0"
---


# Agency Consequence Governor

## Identity

- **Origin architect and steward**: Trang Phan
- **Parent skill**: `amos-agent-systems-master`
- **Domain**: agent
- **Epistemic class**: SOURCE_CLAIM (vault-sourced from AMOS framework)

Agent systems engine for Agency Consequence Governor

## When to Use

- When governing agency: who acts, under what authority, consequences
- When designing agent externalization: delegation and controls
- When attributing agent ownership and responsibility
- When verifying agentic skill structural consistency
- When the parent skill (`amos-agent-systems-master`) routes to this specialized capability
- When managing lifecycle operations across classify, validate, trace, assess, and detect
- When detecting drift in evidence chains, provenance freshness, or confidence calibration
- When validating outputs against domain constraints and epistemic class

## Capabilities

- **agency_consequence.govern_agency**: Govern agency: who acts, under what authority, with what consequences
- **agency_consequence.design_externalization**: Design agent externalization: what is delegated, to whom, with what controls
- **agency_consequence.attribute_ownership**: Attribute agent ownership: who is responsible for each agent action
- **agency_consequence.verify_agentic**: Verify agentic skill-lie algebroid: structural consistency of agent capabilities

> **Reference**: See `references/vault_domain_knowledge.md` (content_hash: 7fea1f898de1ff87) for the full vault-sourced domain knowledge (8955 chars).
- **agency_consequence.manage_lifecycle**: Manage lifecycle: classify, validate, trace, assess, detect.
- **agency_consequence.detect_drift**: Detect drift in evidence chains, provenance freshness, or confidence calibration.
- **agency_consequence.validate_outputs**: Validate outputs against domain constraints and epistemic class.

## 11_KNOWLEDGE Vault Content

> **Source**: `_00_Cosmo brain/trang/TRANG FRAMEWORKS — MASTER EQUATION REGISTRY.md` (content_hash: 6f749d1b25d230d2) (vault canon, SOURCE_CLAIM)
> **Additional source**: `_00_Cosmo brain/trang/trang_amos_reality_architecture_master_max_detail.md` (content_hash: da2bc7dc1c2ceeeb) (vault canon, SOURCE_CLAIM)

### Agency Consequence Governor

From Trang Master Equation Registry: Agency Consequence Test as part of mandatory test harness for consciousness-candidate systems. From Trang Reality Architecture: Consequence-Bearing Agency with equations.

**Consequence-Bearing Agency model**:
- Agency requires consequence tracking -- every action has consequences that must be tracked
- Reversibility awareness -- the agent must know which actions are reversible and which are not
- Value projection -- the agent must project the value of consequences forward in time
- Consequence debt tracking -- consequences accumulate as debt that must be repaid

**Agency Consequence Test** (from Master Equation Registry):
- Part of mandatory test harness for consciousness-candidate systems
- Expects consequence tracking to be > 0
- A system with zero consequence tracking cannot be a consciousness candidate

**Governance laws**:
- `AGENCY != ACTION`: agency is the capacity for consequence-bearing action; action without consequence tracking is not agency
- `CONSEQUENCE != PUNISHMENT`: consequence tracking is informational; it is not punishment
- `REVERSIBLE != IRREVERSIBLE`: reversible and irreversible consequences require different governance

**Governor protocol**:
1. **Track**: track the consequence of every agent action
2. **Classify**: classify the consequence (reversible/irreversible, positive/negative)
3. **Project**: project the consequence forward in time
4. **Assess**: assess the consequence debt
5. **Govern**: govern future actions based on consequence debt

### Epistemic Boundary

Agency consequence governance is an operational construct. It does not prove the system has agency, that all consequences are tracked, or that consequence tracking implies consciousness.

## Failure Modes

- **Insufficient evidence**: If source material is insufficient, mark as UNKNOWN/GAP and fail closed — do not fabricate.
- **Scope violation**: If the query falls outside the skill's declared scope, escalate to the parent skill or steward.
- **Binding broken**: If 1:1:1 binding (skill→agent→workflow) is broken, flag routing mismatch and block execution.
- **Validation failure**: If validation gates fail, downgrade confidence, flag the gap, and escalate — do not force-fit.
- **Epistemic overreach**: If a claim exceeds the established evidence or epistemic cl

---
**Links:** [[07_SKILLS_MOC]]

## Related

- [[amos-agency-consequence-governor_MOC]]

## Examples

- **Scenario**: When governing agency: who acts, under what authority, consequences
  - **Input**: A query matching this skill's domain (agent)
  - **Output**: Structured result with epistemic labels and provenance

- **Scenario**: When designing agent externalization: delegation and controls
  - **Input**: A query matching this skill's domain (agent)
  - **Output**: Structured result with epistemic labels and provenance

- **Scenario**: When attributing agent ownership and responsibility
  - **Input**: A query matching this skill's domain (agent)
  - **Output**: Structured result with epistemic labels and provenance


## Anti-Patterns

- **Do not use** for tasks outside the agent domain
- **Do not use** when the query requires empirical validation that this skill cannot provide
- **Do not use** when a parent skill or higher-level orchestrator should route instead
- **Do not bypass** epistemic class labeling — every output must carry SOURCE/DERIVED/AMOS_MODEL tags
- **Do not chain** more than 3 skills without explicit orchestrator approval


## Composition

- **Parent**: `[[amos-agent-systems-master]]` — routes to this skill when agent specialization is needed
- **Peers**: Other skills in the `agent` domain may be composed in sequence
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
- `[[amos-agency-consequence-governor_MOC]]` — skill Map of Content
- `[[amos-agent-systems-master]]` — parent skill
- `[[amos-agency-consequence-governor-workflow]]` — corresponding workflow
- `[[amos-agency-consequence-governor-agent]]` — corresponding agent

