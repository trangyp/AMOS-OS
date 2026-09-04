---
origin_architect: Trang Phan
steward: Trang Phan
amos_core_target: v4.4
title: integration — References — Amos Workflow Builder
type: reference
source: 07_SKILLS/amos-workflow-builder/references
tags:
  - reference
  - amos-workflow-builder
  - type/skill
  - law-hierarchy
  - trang-framework-recursive-ontology-dynamics
rscf:
  state: SOURCE_CLAIM
  claim_class: SOURCE_CLAIM
  provenance: AMOS_corpus
  scope: skill_reference
---

# Workflow Builder Integration Contracts

## 1:1:1 Routing Law

Every workflow must bind to exactly:

- 1 agent (via frontmatter `Agent` field)
- 1 skill (via frontmatter `Skill` field)

The bound agent must bind to the same skill (via `depends_on_skills`).

This forms a 1:1:1 triad: workflow ↔ agent ↔ skill.

Violations:

- Workflow with no agent binding → orphan workflow
- Workflow with no skill binding → unbound workflow
- Agent's skill != workflow's skill → routing mismatch
- Multiple workflows for one agent → routing conflict (unless redirects)

## AMOS Routing

Workflows live in `.devin/workflows/`.
Agents live in `.devin/agents/`.
Skills live in `.devin/skills/`.

Routing path: trigger → workflow → agent → skill → execution

## RSCF Contracts

Every workflow must carry:

- **R**equest: the trigger condition
- **S**ource: the bound skill and agent
- **C**laim: the workflow's epistemic class
- **F**reshness: the version and last-update timestamp

## H/M/L Coupling

Workflows declare coupling level:

- **H (High)**: workflow directly modifies system state
- **M (Medium)**: workflow produces derived artifacts
- **L (Low)**: workflow is read-only analysis

## Provenance Contracts

Every workflow must record:

- source skill path
- source agent path
- source canon path (if applicable)
- content hash
- epistemic class
- creation/update timestamp

## Parent/Child Workflow Composition

Parent workflows may reference child workflows via:

- step action referencing child workflow name
- gate delegation to child workflow's gates

Constraints:

- parent scope must contain child scope
- parent gates must be stronger than child gates
- parent failure paths must cover child failure paths
- no circular references

## Agent Capability Mapping

Each workflow step should map to an agent capability:

- step action → agent capability name
- step gate → agent capability validation

This ensures the workflow is executable by the bound agent.

______________________________________________________________________

**MOC:** references_MOC

## Related

- [[07_SKILLS/07_SKILLS_MOC|07_SKILLS_MOC]]

______________________________________________________________________

**Related:** [[00_ROOT/00_HOME|00_HOME]] · [[00_ROOT/AMOS_RSCF_NODES|AMOS_RSCF_NODES]] · [[01_CANON/01_CORE_LAWS/LAW_HIERARCHY|LAW_HIERARCHY]] · references_MOC · [[07_SKILLS/07_SKILLS_MOC|07_SKILLS_MOC]]

**MOC:** references_MOC

**Trang Framework:** [[11_KNOWLEDGE/TRANG_FRAMEWORK_RECURSIVE_ONTOLOGY_DYNAMICS|TRANG_FRAMEWORK_RECURSIVE_ONTOLOGY_DYNAMICS]]

______________________________________________________________________

RSCF-NODE
node_id: amos-workflow-builder-integration
node_type: reference
path: 07_SKILLS/amos-workflow-builder/references/integration.md
RSCF-RELATIONS:

- INDEXED_BY: [[00_ROOT/00_HOME|00_HOME]]
- INDEXED_BY: [[00_ROOT/AMOS_RSCF_NODES|AMOS_RSCF_NODES]]
- CHILD_OF: references_MOC
