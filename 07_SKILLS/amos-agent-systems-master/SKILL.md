---
schema_version: 1.0
title: SKILL — Amos Agent Systems Master
type: skill
source: 07_SKILLS/amos-agent-systems-master
name: amos-agent-systems-master
description: AMOS Agent Systems — agent fabrication, delegation, agency-consequence tensors, agent economy governance, agent-to-agent protocols. Use when agent design, delegation reasoning, or multi-agent govern. Do not use for generic tasks outside agent domain.
parent_skill: none
domain: agent
origin_architect: Trang Phan
epistemic_class: SOURCE_CANON
tags:
  - type/skill
  - type/skill
  - domain/agent-systems
  - epistemic/source_claim
  - hml/m
  - epistemic/source_canon
  - amos-os
  - agents
  - readme
  - routing-policy-validation-receipt
  - authz-engine-validation-receipt
  - agent-template
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
license: MIT
steward: Trang Phan
---

# [[AGENTS|AGENTS]] README

## Identity

Origin architect: **Trang Phan**. Domain: agent. Parent: none. Epistemic class: SOURCE_CANON. H/M/L: M.

## When to Use

AMOS Agent Systems — agent fabrication, delegation, agency-consequence tensors, agent economy governance, agent-to-agent protocols. Use for agent design, delegation reasoning, or multi-agent govern...

- When managing lifecycle operations across classify, validate, trace, assess, and detect
- When detecting drift in evidence chains, provenance freshness, or confidence calibration
- When validating outputs against domain constraints and epistemic class

## Capabilities

- **agent_systems.fabricate_agent**: Fabricate agents with proper schema: capabilities, side-effect classification, governance metadata, and content hash.
- **agent_systems.delegate_task**: Delegate tasks to subordinate agents with scope bounds, authority gates, and consequence tensor tracking.
- **agent_systems.validate_agent_composition**: Validate agent composition: MECE coverage, skill binding integrity, capability bounds, and governance metadata.
- **agent_systems.trace_agent_provenance**: Trace agent capabilities, content, and delegation chain to source skills and vault provenance.
- **agent_systems.assess_agent_claim**: Assess agent claims for epistemic class, capability scope, authority bounds, and lifecycle status.
- **agent_systems.manage_agent_lifecycle**: Manage agent lifecycle: fabricate, activate, promote, retire, and archive with provenance tracking.
- **agent_systems.detect_agent_drift**: Detect agent drift: capability creep, scope expansion, governance decay, and content hash tampering.
- **agent_systems.escalate_agent_gaps**: Escalate agent gaps: flag orphan agents, broken skill bindings, missing capabilities, trigger repair.
- **agent_systems.manage_lifecycle**: Manage lifecycle: classify, validate, trace, assess, detect.
- **agent_systems.detect_drift**: Detect drift in evidence chains, provenance freshness, or confidence calibration.
- **agent_systems.validate_outputs**: Validate outputs against domain constraints and epistemic class.

## Operations

1. **agent_systems.fabricate_agent**: Fabricate agents with proper schema: capabilities, side-effect classification, governance metadata, and content hash.
1. **agent_systems.delegate_task**: Delegate tasks to subordinate agents with scope bounds, authority gates, and consequence tensor tracking.
1. **agent_systems.validate_agent_composition**: Validate agent composition: MECE coverage, skill binding integrity, capability bounds, and governance metadata.
1. **agent_systems.trace_agent_provenance**: Trace agent capabilities, content, and delegation chain to source skills and vault provenance.
1. **agent_systems.assess_agent_claim**: Assess agent claims for epistemic class, capability scope, authority bounds, and lifecycle status.
1. **agent_systems.manage_agent_lifecycle**: Manage agent lifecycle: fabricate, activate, promote, retire, and archive with provenance tracking.
1. **agent_systems.detect_agent_drift**: Detect agent drift: capability creep, scope expansion, governance decay, and content hash tampering.
1. **agent_systems.escalate_agent_gaps**: Escalate agent gaps: flag orphan agents, broken skill bindings, missing capabilities, trigger repair.
1. **agent_systems.manage_lifecycle**: Manage lifecycle: classify, validate, trace, assess, detect.
1. **agent_systems.detect_drift**: Detect drift in evidence chains, provenance freshness, or confidence calibration.
1. **agent_systems.validate_outputs**: Validate outputs against domain constraints and epistemic class.

## Consolidated Sub-Skills (11)

This parent skill consolidates the following sub-skills. Each is a section within this domain:

## Vault-Sourced Domain Knowledge

> **Source**: `06_AGENTS/AGENTS_README.md` from the AMOS_OS Obsidian vault.
> This is substantive domain knowledge, not script-generated content.

## [[AGENTS|AGENTS]] README — part 2

## Purpose

`AGENTS README` is the package readme for the **Agents** plane segment at `06_AGENTS`.
The Agents plane governs agent specifications, capability envelopes, and delegation boundaries. Normative load-bearing content lives in the sibling contract(s); this readme orients navigation.

## Sibling artifacts

- [[06_AGENTS/AGENTS_AGENT_CONTRACT|AGENTS_AGENT_CONTRACT]]

## Contract discipline

Typed artifacts · provenance stamped · epistemic class declared · confidence ceiling · fail-closed on UNKNOWN/GAP · receipts for consequential effects · rollback basin before mutation.

## Gaps

Executable binding PARTIAL unless an executed validation receipt exists for this subsystem ([[25_COGNITIVE_MATRIX/11_VALIDATION/ROUTING_POLICY_VALIDATION_RECEIPT|ROUTING_POLICY_VALIDATION_RECEIPT]] · [[03_CONTROL_PLANE/04_AUTHORITY/AUTHZ_ENGINE_VALIDATION_RECEIPT|AUTHZ_ENGINE_VALIDATION_RECEIPT]]).

## Worked semantics

Given an operation touching `AGENTS README` within the Agents plane:

1. **Admit** — resolve the artifact by id + version; unresolved id ⇒ `UNKNOWN/GAP`, fail closed.
1. **Bind scope** — declare domain / regime / H-M-L applicability before any mutation.
1. **Check authority** — authority_ref must be epoch-valid; capability alone never authorizes.
1. **Validate preconditions** — dependency closure traversed to the smallest result-changing set.
1. **Propose** — candidate state is non-authoritative until gates pass (`PROPOSAL ≠ COMMIT`).
1. **Commit or hold** — on any failed premise: preserve unaffected state, invalidate dependent descendants only, record receipt.

## Promotion-gate checklist

- [ ] typed schema bound to this artifact
- [ ] identity + versioning implemented
- [ ] negative cases covered (missing · malformed · stale · unauthorized input)
- [ ] provenance edges persisted and validated
- [ ] rollback basin demonstrated for consequential effects
- [ ] executed validation receipt specific to this artifact
- [ ] unresolved critical gaps registered as UNKNOWN/GAP (visible)

## Cross-plane binding

- AGENT_TEMPLATE

______________________________________________________________________

**MOC:** [[07_SKILLS/amos-agent-systems-master/amos-agent-systems-master_MOC|amos-agent-systems-master_MOC]]

## Examples

- **Scenario**: When managing lifecycle operations across classify, validate, trace, assess, and detect

  - **Input**: A query matching this skill's domain (agent)
  - **Output**: Structured result with epistemic labels and provenance

- **Scenario**: When detecting drift in evidence chains, provenance freshness, or confidence calibration

  - **Input**: A query matching this skill's domain (agent)
  - **Output**: Structured result with epistemic labels and provenance

- **Scenario**: When validating outputs against domain constraints and epistemic class

  - **Input**: A query matching this skill's domain (agent)
  - **Output**: Structured result with epistemic labels and provenance

## Validation Gates

- **L0 Integrity**: All structural elements accounted for; no silent gaps
- **L1 Epistemic**: Every claim tagged with epistemic class (SOURCE_CLAIM / DERIVED / AMOS_MODEL)
- **L5 Scope**: Analysis confined to declared scope and domain
- **L7 Authority**: No autonomous action beyond authority boundary

## Anti-Patterns

- **Do not use** for tasks outside the agent domain
- **Do not use** when the query requires empirical validation that this skill cannot provide
- **Do not use** when a parent skill or higher-level orchestrator should route instead
- **Do not bypass** epistemic class labeling — every output must carry SOURCE/DERIVED/AMOS_MODEL tags
- **Do not chain** more than 3 skills without explicit orchestrator approval

## Composition

- **Parent**: `none` — routes to this skill when agent specialization is needed
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

## Do not use

- For generic agent fabrication outside the AMOS agent framework
- To claim empirical validation of multi-agent theories
- As a substitute for domain-specific agent design or delegation evidence
- Outside agent systems domain reasoning

## References

- `references/11k_agent_templates.md` — loaded on demand
- `references/11k_environment_scan_agent.md` — loaded on demand
- `references/agent_registry.md` — loaded on demand
- `references/agent_working_instructions_v2.md` — loaded on demand
- `references/ai_workforce_layer.md` — loaded on demand
- `references/architecture_guardian_agent.md` — loaded on demand
- `references/fabrication_engine.md` — loaded on demand
- `references/fabrication_engine_layer.md` — loaded on demand
- `references/os_agent_model.md` — loaded on demand
- `references/references_MOC.md` — loaded on demand
- \`\` — skill Map of Content
- `none` — parent skill
- \`\` — corresponding workflow
- `amos-agent-systems-master-agent` — corresponding agent

______________________________________________________________________

**Related:** [[00_ROOT/00_HOME|00_HOME]] · [[00_ROOT/AMOS_RSCF_NODES|AMOS_RSCF_NODES]] · [[01_CANON/01_CORE_LAWS/LAW_HIERARCHY|LAW_HIERARCHY]] · [[07_SKILLS/07_SKILLS_MOC|07_SKILLS_MOC]] · references_MOC

**MOC:** [[07_SKILLS/07_SKILLS_MOC|07_SKILLS_MOC]]

**Trang Framework:** [[11_KNOWLEDGE/TRANG_FRAMEWORK_RECURSIVE_ONTOLOGY_DYNAMICS|TRANG_FRAMEWORK_RECURSIVE_ONTOLOGY_DYNAMICS]]

______________________________________________________________________

RSCF-NODE
node_id: amos-agent-systems-master
node_type: skill
path: 07_SKILLS/amos-agent-systems-master/SKILL.md
RSCF-RELATIONS:

- INDEXED_BY: [[00_ROOT/00_HOME|00_HOME]]
- INDEXED_BY: [[00_ROOT/AMOS_RSCF_NODES|AMOS_RSCF_NODES]]
- CHILD_OF: [[07_SKILLS/07_SKILLS_MOC|07_SKILLS_MOC]]
