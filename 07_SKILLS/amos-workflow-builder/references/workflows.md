---
origin_architect: Trang Phan
steward: Trang Phan
amos_core_target: v4.4
title: Workflows — Amos Workflow Builder
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

# Workflow Creation and Update Workflows

## CREATE Workflow

1. **ORIENT**: Resolve workflow name, domain, bound agent, bound skill, trigger.
1. **GAP**: Identify missing steps, gates, bindings, failure paths.
1. **SOURCE**: Bind to vault canon, existing skills, existing agents.
1. **ARCHITECT**: Design frontmatter, steps, gates, failure paths, provenance.
1. **BUILD**: Write the workflow file.
1. **INTEGRATE**: Verify 1:1:1 routing (workflow:agent:skill).
1. **CHALLENGE**: Stress-test gates, failure paths, scope, contradictions.
1. **VALIDATE**: Run G1-G10 hard gates.
1. **PACKAGE**: Prepare installable bundle.

## UPDATE Workflow

1. **ORIENT**: Identify existing workflow and required changes.
1. **GAP**: Identify missing or outdated steps, gates, bindings.
1. **SOURCE**: Re-bind to updated sources.
1. **ARCHITECT**: Update structure preserving existing bindings.
1. **BUILD**: Update the workflow file.
1. **INTEGRATE**: Verify routing still 1:1:1.
1. **CHALLENGE**: Stress-test updated sections.
1. **VALIDATE**: Run G1-G10 hard gates.
1. **PACKAGE**: Prepare updated bundle.

## AUDIT Workflow

1. **ORIENT**: Identify workflow to audit.
1. **GAP**: Check for missing steps, gates, bindings, failure paths.
1. **VALIDATE**: Run G1-G10 hard gates.
1. **REPORT**: Generate audit report with pass/fail per gate.

## REPAIR Workflow

1. **ORIENT**: Identify workflow and validation failures.
1. **GAP**: Classify each failure.
1. **SOURCE**: Re-bind to correct sources.
1. **BUILD**: Fix failures.
1. **VALIDATE**: Re-run G1-G10 hard gates.
1. **PACKAGE**: Prepare repaired bundle.

## PACKAGE Workflow

1. **VALIDATE**: Run G1-G10 hard gates.
1. **BUNDLE**: Collect workflow, agent, skill files.
1. **REPORT**: Generate validation report and provenance manifest.

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
node_id: amos-workflow-builder-workflows
node_type: reference
path: 07_SKILLS/amos-workflow-builder/references/workflows.md
RSCF-RELATIONS:

- INDEXED_BY: [[00_ROOT/00_HOME|00_HOME]]
- INDEXED_BY: [[00_ROOT/AMOS_RSCF_NODES|AMOS_RSCF_NODES]]
- CHILD_OF: references_MOC
