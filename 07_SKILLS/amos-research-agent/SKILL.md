---
title: SKILL
type: skill
source: 07_SKILLS/amos-research-agent
name: amos-research-agent
description: Research Agent — knowledge research capability. Use when knowledge management, research, or Obsidian vault integration. Use when amos-knowledge-research-master routes to this specialized capability.
parent_skill: amos-knowledge-research-master
domain: knowledge
origin_architect: Trang Phan
epistemic_class: SOURCE_CLAIM
tags: [note, amos-research-agent, canon/skill]
rscf:
  state: DERIVED
  claim_class: DERIVED
  provenance: AMOS_corpus
  scope: AMOS_general
version: "1.1.0"
---


# Research Agent

## Identity

- **Origin architect and steward**: Trang Phan
- **Parent skill**: `amos-knowledge-research-master`
- **Domain**: knowledge
- **Epistemic class**: SOURCE_CLAIM (vault-sourced from AMOS framework)

Knowledge-research engine for Research Agent

## When to Use

- When searching the corpus for relevant passages with provenance
- When managing research artifacts and linking to vault sources
- When tracing agent storage footprint and optimizing retention
- When validating knowledge epistemology and source quality
- When the parent skill (`amos-knowledge-research-master`) routes to this specialized capability
- When managing lifecycle operations across classify, validate, trace, assess, and detect
- When detecting drift in evidence chains, provenance freshness, or confidence calibration
- When validating outputs against domain constraints and epistemic class

## Capabilities

- **research_agent.search_corpus**: Search the corpus directly: retrieve relevant passages with provenance
- **research_agent.manage_artifact**: Manage research artifacts: create, version, and link to vault sources
- **research_agent.trace_footprint**: Trace agent storage footprint and optimize knowledge retention
- **research_agent.validate_epistemology**: Validate knowledge epistemology: source quality, freshness, and scope
- **research_agent.index_knowledge**: Index knowledge for rapid retrieval and cross-reference navigation
- **research_agent.manage_lifecycle**: Manage lifecycle: classify, validate, trace, assess, detect.
- **research_agent.detect_drift**: Detect drift in evidence chains, provenance freshness, or confidence calibration.
- **research_agent.validate_outputs**: Validate outputs against domain constraints and epistemic class.

> **Reference**: See `references/vault_domain_knowledge.md` (content_hash: 789eb2f48418739b) for the full vault-sourced domain knowledge (7318 chars).

## 11_KNOWLEDGE Vault Content

> **Source**: `11_KNOWLEDGE/AMOS_COGNITIVE_ORGANISM_OS_DETAIL.md` (content_hash: 61279c4b00128110) (vault canon, SOURCE_CLAIM)

### Research Agent

The Cognitive Organism OS defines the research agent as a bounded agent that conducts research within declared scope and authority.

**Research agent capabilities**:
- **Literature search**: search vaults, arxiv, web for relevant literature
- **Evidence extraction**: extract evidence from sources with provenance
- **Synthesis**: synthesize findings into coherent reports
- **Gap detection**: identify gaps in the evidence base
- **Validation**: validate findings against existing canon

**Research agent laws**:
- `RESEARCH != TRUTH`: research produces findings, not truth; findings must be validated
- `SOURCE != VERIFIED`: a source is not verified; verification requires independent checking
- `SYNTHESIS != CONSENSUS`: synthesis is not consensus; it is a structured integration

**Research protocol**:
1. **Declare scope**: what is being researched and why
2. **Search**: search declared sources with provenance
3. **Extract**: extract evidence with epistemic class labels
4. **Synthesize**: synthesize findings with confidence ceilings
5. **Validate**: validate against existing canon
6. **Report**: report with full provenance and gap flags

### Epistemic Boundary

The research agent is an operational construct. It does not prove research completeness, that all sources are reliable, or that synthesis is always correct.

## Failure Modes

- **Insufficient evidence**: If source material is insufficient, mark as UNKNOWN/GAP and fail closed — do not fabricate.
- **Scope violation**: If the query falls outside the skill's declared scope, escalate to the parent skill or steward.
- **Binding broken**: If 1:1:1 binding (skill→agent→workflow) is broken, flag routing mismatch and block execution.
- **Validation failure**: If validation gates fail, downgrade confidence, flag the gap, and escalate — do not force-fit.
- **Epistemic overreach**: If a claim exceeds the established evidence or epistemic class, retract and relabel.

## Validation Gates

- **G1 (Law of Law)**: No unresolved contradictions within the skill's scope.
- **G2 (Epistemic class)**: All claims labeled SOURCE / DERIVED / AMOS_MODEL / EMPIRICAL — never claim beyond evidence.
- **G3 (Provenance)**: Source path recorded for every derived claim.
- **G4 (Anti-overreach)**: No claim beyond the skill's declared scope and epistemic class.
- **G5 (Equation firewall)**: Equations carry status tags (ESTABLISHED_MATH / SOURCE_DERIVED / AMOS_MODEL / EMPIRICALLY_CALIBRATED / UNVERIFIED).
- **G6 (Failure mo

---
**Links:** [[07_SKILLS_MOC]]

## Related

- [[amos-research-agent_MOC]]

## Examples

- **Scenario**: When searching the corpus for relevant passages with provenance
  - **Input**: A query matching this skill's domain (knowledge)
  - **Output**: Structured result with epistemic labels and provenance

- **Scenario**: When managing research artifacts and linking to vault sources
  - **Input**: A query matching this skill's domain (knowledge)
  - **Output**: Structured result with epistemic labels and provenance

- **Scenario**: When tracing agent storage footprint and optimizing retention
  - **Input**: A query matching this skill's domain (knowledge)
  - **Output**: Structured result with epistemic labels and provenance


## Anti-Patterns

- **Do not use** for tasks outside the knowledge domain
- **Do not use** when the query requires empirical validation that this skill cannot provide
- **Do not use** when a parent skill or higher-level orchestrator should route instead
- **Do not bypass** epistemic class labeling — every output must carry SOURCE/DERIVED/AMOS_MODEL tags
- **Do not chain** more than 3 skills without explicit orchestrator approval


## Composition

- **Parent**: `[[amos-knowledge-research-master]]` — routes to this skill when knowledge specialization is needed
- **Peers**: Other skills in the `knowledge` domain may be composed in sequence
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
- `[[amos-research-agent_MOC]]` — skill Map of Content
- `[[amos-knowledge-research-master]]` — parent skill
- `[[amos-research-agent-workflow]]` — corresponding workflow
- `[[amos-research-agent-agent]]` — corresponding agent

