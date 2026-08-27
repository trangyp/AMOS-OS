---
title: "Workflows — Amos Workflow Builder"
type: reference
source: 07_SKILLS/amos-workflow-builder/references
tags: [reference, amos-workflow-builder, canon/skill]
rscf:
  state: SOURCE_CLAIM
  claim_class: SOURCE_CLAIM
  provenance: AMOS_corpus
  scope: skill_reference
---


# Workflow Creation and Update Workflows

## CREATE Workflow

1. **ORIENT**: Resolve workflow name, domain, bound agent, bound skill, trigger.
2. **GAP**: Identify missing steps, gates, bindings, failure paths.
3. **SOURCE**: Bind to vault canon, existing skills, existing agents.
4. **ARCHITECT**: Design frontmatter, steps, gates, failure paths, provenance.
5. **BUILD**: Write the workflow file.
6. **INTEGRATE**: Verify 1:1:1 routing (workflow:agent:skill).
7. **CHALLENGE**: Stress-test gates, failure paths, scope, contradictions.
8. **VALIDATE**: Run G1-G10 hard gates.
9. **PACKAGE**: Prepare installable bundle.

## UPDATE Workflow

1. **ORIENT**: Identify existing workflow and required changes.
2. **GAP**: Identify missing or outdated steps, gates, bindings.
3. **SOURCE**: Re-bind to updated sources.
4. **ARCHITECT**: Update structure preserving existing bindings.
5. **BUILD**: Update the workflow file.
6. **INTEGRATE**: Verify routing still 1:1:1.
7. **CHALLENGE**: Stress-test updated sections.
8. **VALIDATE**: Run G1-G10 hard gates.
9. **PACKAGE**: Prepare updated bundle.

## AUDIT Workflow

1. **ORIENT**: Identify workflow to audit.
2. **GAP**: Check for missing steps, gates, bindings, failure paths.
3. **VALIDATE**: Run G1-G10 hard gates.
4. **REPORT**: Generate audit report with pass/fail per gate.

## REPAIR Workflow

1. **ORIENT**: Identify workflow and validation failures.
2. **GAP**: Classify each failure.
3. **SOURCE**: Re-bind to correct sources.
4. **BUILD**: Fix failures.
5. **VALIDATE**: Re-run G1-G10 hard gates.
6. **PACKAGE**: Prepare repaired bundle.

## PACKAGE Workflow

1. **VALIDATE**: Run G1-G10 hard gates.
2. **BUNDLE**: Collect workflow, agent, skill files.
3. **REPORT**: Generate validation report and provenance manifest.

---
**MOC:** [[references_MOC]]

## Related

- [[07_SKILLS_MOC]]
