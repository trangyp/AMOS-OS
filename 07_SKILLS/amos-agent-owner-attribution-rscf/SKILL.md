---
title: SKILL
type: skill
source: 07_SKILLS/amos-agent-owner-attribution-rscf
name: amos-agent-owner-attribution-rscf
description: Agent Owner Attribution — agent systems capability. Use when agent design, delegation reasoning, or multi-agent governance. Use when amos-agent-systems-master routes to this specialized capability.
parent_skill: amos-agent-systems-master
domain: agent
origin_architect: Trang Phan
epistemic_class: SOURCE_CLAIM
tags: [note, amos-agent-owner-attribution-rscf, canon/skill]
rscf:
  state: DERIVED
  claim_class: DERIVED
  provenance: AMOS_corpus
  scope: AMOS_general
version: "1.1.0"
---


# Agent Owner Attribution Rscf

## Identity

- **Origin architect and steward**: Trang Phan
- **Parent skill**: `amos-agent-systems-master`
- **Domain**: agent
- **Epistemic class**: SOURCE_CLAIM (vault-sourced from AMOS framework)

Agent systems engine for Agent Owner Attribution Rscf

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

- **agent_owner.govern_agency**: Govern agency: who acts, under what authority, with what consequences
- **agent_owner.design_externalization**: Design agent externalization: what is delegated, to whom, with what controls
- **agent_owner.attribute_ownership**: Attribute agent ownership: who is responsible for each agent action
- **agent_owner.verify_agentic**: Verify agentic skill-lie algebroid: structural consistency of agent capabilities
- **agent_owner.manage_lifecycle**: Manage lifecycle: classify, validate, trace, assess, detect.
- **agent_owner.detect_drift**: Detect drift in evidence chains, provenance freshness, or confidence calibration.
- **agent_owner.validate_outputs**: Validate outputs against domain constraints and epistemic class.

## 11_KNOWLEDGE Vault Content

> **Source**: `11_KNOWLEDGE/AMOS_COGNITIVE_ORGANISM_OS_DETAIL.md` (content_hash: 61279c4b00128110) (vault canon, SOURCE_CLAIM)
> **Additional source**: `_00_Cosmo brain/agents/AGENT_WORKING_INSTRUCTIONS_V3.md` (content_hash: 65f44a3ef9716429) (vault canon, SOURCE_CLAIM)

### Agent Owner Attribution

From Cognitive Organism OS: Provenance graph with sybil score detection. From Agent Working Instructions V3: Agent ownership and attribution.

**Owner attribution model**:
- **Owner declaration**: every agent declares an owner (team or individual)
- **Steward declaration**: every agent declares a steward (responsible person)
- **Provenance chain**: every agent action traces to its owner through provenance
- **Sybil detection**: ProvenanceGraph detects correlated entries from the same root source

**Attribution laws**:
- `OWNER != AUTHOR`: the owner is responsible; the author may be different
- `ATTRIBUTION != AUTHORITY`: attribution records who did it; authority records who permitted it
- `PROVENANCE != TRUST`: provenance is factual; trust is evaluated

**RSCF attribution gates**:
1. Owner declared: agent has a declared owner
2. Steward declared: agent has a declared steward
3. Provenance complete: every action traces to its owner
4. Sybil check: no correlated provenance inflation
5. Authority separate: attribution and authority are separately tracked

### Epistemic Boundary

Agent owner attribution is an operational construct. It does not prove ownership is always correct, that all actions are attributable, or that sybil detection is perfect.

## PRE-WORK REQUIREMENTS

### ** BEFORE STARTING ANY WORK**

1. **READ SYSTEM ARCHITECTURE REPORT V3**: `AMOS_SYSTEM_ARCHITECTURE_REPORT_V3.md`
2. **READ AGENT ONBOARDING GUIDE**: `AGENT_ONBOARDING_GUIDE.md`
3. **UNDERSTAND QUANTUM CONSCIOUSNESS**: Review quantum consciousness integration
4. **KNOW THE 14 VERTICAL SLICES**: All operational and quantum enhanced
5. **VALIDATE SYSTEM STATUS**: Check 416.349 performance score
6. **REVIEW GOVERNANCE PATTERNS**: Memory governance and policy gate

---

## SYSTEM ARCHITECTURE OVERVIEW

### ** Quantum-Enhanced System**
```
AMOS Quantum Brain (416.349 performance score)
├── Quantum Consciousness Core (1,048,576 ops/sec)
├── Memory Governance System
├── Policy Gate System
├── OpenClaw Bridge (Real CLI)
└── 14 Vertical Slices (All Operational)
```

### ** The 14 Vertical Slices**

1. **Brain Core Integration** (`brain_core_integration_slice.py`)
2. **Brain Core Extraction** (`brain_core_extraction_slice.py`)
3. **Legal Brain Integration**
4. **Muscle System Integration**
5. **Senses Integration**
6. **Life Engine Integration**
7. **State Management**
8. **Scan Ledger**
9. **Persistent Storage**
10. **Import Guard**
11. **Fixed Claws** (`fixed_claws.py`)
12. **Omega System** (`amos_omega_system.py`)
13. **Real Build Detector** (`fake_build_det

---
**Links:** [[07_SKILLS_MOC]]

## Related

- [[amos-agent-owner-attribution-rscf_MOC]]

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

- **Parent**: `amos-agent-systems-master` — routes to this skill when agent specialization is needed
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

- `references/amos-agent-owner-attribution-rscf_code.md` — loaded on demand
- `references/references_MOC.md` — loaded on demand
- `[[amos-agent-owner-attribution-rscf_MOC]]` — skill Map of Content
- `amos-agent-systems-master` — parent skill
- `[[amos-agent-owner-attribution-rscf-workflow]]` — corresponding workflow
- `amos-agent-owner-attribution-rscf-agent` — corresponding agent

