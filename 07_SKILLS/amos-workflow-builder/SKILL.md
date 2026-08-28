---
title: SKILL — Amos Workflow Builder
type: skill
source: 07_SKILLS/amos-workflow-builder
name: amos-workflow-builder
description: Build, update, audit, and package advanced AMOS/COSMO/Trang ChatGPT Workflows from capability
  gaps, existing skills, agent bindings, engine/runtime specifications, or operational sequences. Use
  when creating a new AMOS-aligned Workflow, strengthening a thin workflow, converting an AMOS engine/spec
  into an operational workflow, checking agent-skill-workflow routing, separating operational steps from
  validation gates, adding RSCF/HML/provenance/governance controls, validating step ordering and gate
  enforcement, or preparing a complete installable workflow bundle. This is the AMOS-specialized Workflow
  factory; do not use it as a generic replacement for ordinary non-AMOS workflow creation.
parent_skill: none
domain: workflow
origin_architect: Trang Phan
epistemic_class: SOURCE_CANON
tags:
- type/skill
- canon/skill
- domain/os-runtime
- rscf/source_claim
- hml/m
- epistemic/source_canon
- amos_os
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
---

# AMOS Workflow Builder

## Identity

Origin architect: **Trang Phan**. Domain: workflow. Parent: none. Epistemic class: SOURCE_CANON. H/M/L: M.
## When to Use

Use this skill when creating, updating, auditing, or packaging AMOS-aligned Workflows. Covers workflow step sequencing, validation gate enforcement (G1-G10), failure path specification, 1:1:1 binding (workflow→agent→skill), RSCF/HML/provenance/governance controls, trigger definition, and provenance recording. Use when converting engine specs into operational workflows or strengthening thin workflows.

Operate as the AMOS-specialized factory for creating, upgrading, auditing, and packaging Workflows belonging to the AMOS / COSMO / Trang architecture family.

Treat this Skill as a build-and-governance layer, not as proof that source frameworks are empirically true.

Use the weakest accurate epistemic class:

`SOURCE_CANON | SOURCE_CLAIM | OBSERVATION | DERIVED | AMOS_MODEL | DOMAIN_EMPIRICAL | VERIFIED | CONDITIONAL | COMPETING | UNKNOWN/GAP`
- When managing lifecycle operations across classify, validate, trace, assess, and detect
- When detecting drift in evidence chains, provenance freshness, or confidence calibration
- When validating outputs against domain constraints and epistemic class

## Capabilities

- **workflow.design**: Design a governed workflow graph from objective, steps, contracts, dependencies, gates, authority, retries, compensation, and rollback.
- **workflow.validate_topology**: Validate workflow topology, gates, contracts, authority boundaries, and cycles
- **workflow.analyze**: Analyze workflow topology, critical path, fan-out, fan-in, risk concentration, authority surface, failure propagation, and repair targets.
- **workflow.manage_lifecycle**: Manage workflow lifecycle: plan execution frontier, stage step execution under authority, checkpoint, recover from valid checkpoints, compensate completed durable steps after partial failure, and package validated workflow definitions.
- **workflow.detect_drift**: Detect workflow scope, dependency, authority, schema, environment, provenance, and confidence drift.
- **workflow.trace_workflow_provenance**: Trace workflow provenance to skills, agents, and vault sources
- **workflow.assess_workflow_claim**: Assess workflow claims: gate enforcement, step ordering, and promotion readiness
- **workflow.escalate_gaps**: Classify workflow gaps and escalate blocking unknowns.
 Core Objective

Create Workflows that are:

- triggerable
- source-faithful
- operational rather than descriptive
- compact at the entrypoint
- progressively loadable
- provenance-preserving
- scope/regime bounded
- contradiction-visible
- composable with parent/child AMOS Workflows
- explicit about AMOS_MODEL versus empirical claims
- testable and package-ready
- agent-bound (every workflow binds to exactly one agent)
- skill-bound (every workflow binds to exactly one skill)
- gate-enforced (every step has a validation gate)

Never convert a large vault dump directly into a workflow unless every step is required at runtime.
- **workflow.validate_outputs**: Validate outputs against domain constraints and epistemic class.

## Runtime

Apply:

`ORIENT -> GAP -> SOURCE -> ARCHITECT -> BUILD -> INTEGRATE -> CHALLENGE -> VALIDATE -> PACKAGE`

Load:

- `references/workflows.md` (content_hash: 96d94a2d2c10f977) for creation/update workflows
- `references/validation.md` (content_hash: f2ff778a23622064) for hard gates
- `references/integration.md` (content_hash: b0910ef0e01ce315) for AMOS routing, agent/skill binding, RSCF, H/M/L, and provenance contracts

Use the smallest sufficient proof and build scope.

## ORIENT

Resolve:

- requested Workflow name or capability
- CREATE, UPDATE, AUDIT, REPAIR, or PACKAGE
- intended parent Workflow
- domain
- bound agent (1:1)
- bound skill (1:1)
- expected trigger
- expected inputs
- expected outputs
- required validation gates
- authoritative source corpus
- whether empirical validation is part of the Workflow's purpose
- whether scripts/resources/assets materially improve reliability

Do not ask again for information already available from the request, source bundle, repository,

---
**Links:** [[07_SKILLS_MOC]]

## Related

- [[amos-workflow-builder_MOC]]

## Examples

- **Scenario**: When managing lifecycle operations across classify, validate, trace, assess, and detect
  - **Input**: A query matching this skill's domain (workflow)
  - **Output**: Structured result with epistemic labels and provenance

- **Scenario**: When detecting drift in evidence chains, provenance freshness, or confidence calibration
  - **Input**: A query matching this skill's domain (workflow)
  - **Output**: Structured result with epistemic labels and provenance

- **Scenario**: When validating outputs against domain constraints and epistemic class
  - **Input**: A query matching this skill's domain (workflow)
  - **Output**: Structured result with epistemic labels and provenance


## Anti-Patterns

- **Do not use** for tasks outside the workflow domain
- **Do not use** when the query requires empirical validation that this skill cannot provide
- **Do not use** when a parent skill or higher-level orchestrator should route instead
- **Do not bypass** epistemic class labeling — every output must carry SOURCE/DERIVED/AMOS_MODEL tags
- **Do not chain** more than 3 skills without explicit orchestrator approval


## Composition

- **Parent**: `none` — routes to this skill when workflow specialization is needed
- **Peers**: Other skills in the `workflow` domain may be composed in sequence
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

- `references/integration.md` — loaded on demand
- `references/references_MOC.md` — loaded on demand
- `references/validation.md` — loaded on demand
- `references/workflows.md` — loaded on demand
- `[[amos-workflow-builder_MOC]]` — skill Map of Content
- `none` — parent skill
- `[[amos-workflow-builder-workflow]]` — corresponding workflow
- `amos-workflow-builder-agent` — corresponding agent
---

**Related:** [[00_HOME]] · [[AMOS_RSCF_NODES]] · [[LAW_HIERARCHY]] · [[07_SKILLS_MOC]] · [[references_MOC]]

**MOC:** [[07_SKILLS_MOC]]

**Trang Framework:** [[TRANG_FRAMEWORK_RECURSIVE_ONTOLOGY_DYNAMICS]]

---
RSCF-NODE
node_id: amos-workflow-builder
node_type: skill
path: 07_SKILLS/amos-workflow-builder/SKILL.md
RSCF-RELATIONS:
- INDEXED_BY: [[00_HOME]]
- INDEXED_BY: [[AMOS_RSCF_NODES]]
- CHILD_OF: [[07_SKILLS_MOC]]
