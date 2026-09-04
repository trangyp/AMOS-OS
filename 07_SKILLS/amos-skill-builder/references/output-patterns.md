---
origin_architect: Trang Phan
steward: Trang Phan
amos_core_target: v4.4
title: output patterns
type: reference
source: 07_SKILLS/amos-skill-builder/references
tags:
  - reference
  - amos-skill-builder
  - type/skill
  - law-hierarchy
  - trang-framework-recursive-ontology-dynamics
rscf:
  state: SOURCE_CLAIM
  claim_class: EMPIRICAL
  provenance: AMOS_corpus
  scope: skill_reference
---

# Skill Builder — Output Patterns Reference

## Standard Skill Output Patterns

### Pattern 1: Capability Execution

```json
{
  "status": "DERIVED|SOURCE|AMOS_MODEL|EMPIRICAL",
  "capability": "<domain>.<verb>",
  "summary": "<one-line summary>",
  "data": { ... },
  "provenance": {
    "source": "<vault file path>",
    "epistemic_class": "SOURCE|DERIVED|AMOS_MODEL|EMPIRICAL",
    "confidence_ceiling": 0.95
  },
  "gates_passed": ["G1", "G2", ...],
  "gates_failed": []
}
```

### Pattern 2: Validation Report

```json
{
  "valid": true|false,
  "issues": ["<issue description>"],
  "gates": {
    "G1_frontmatter": "pass|fail",
    "G2_description": "pass|fail",
    ...
  }
}
```

### Pattern 3: Gap Escalation

```json
{
  "status": "UNKNOWN",
  "gap_type": "missing_evidence|missing_source|contradiction|out_of_scope",
  "summary": "<what is missing>",
  "escalation_target": "<parent skill or steward>",
  "blocking": true
}
```

### Pattern 4: Skill Package

```
<skill_name>/
├── SKILL.md              # main content with frontmatter
├── references/           # supporting reference docs
│   ├── validation.md
│   ├── workflows.md
│   └── integration.md
└── scripts/              # optional helper scripts
```

### Output Rules

- Every output includes epistemic class label
- Every derived output includes provenance path
- Confidence never exceeds the H/M/L ceiling
- On failure: fail closed, flag gap, escalate — never fabricate

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
node_id: amos-skill-builder-output-patterns
node_type: reference
path: 07_SKILLS/amos-skill-builder/references/output-patterns.md
RSCF-RELATIONS:

- INDEXED_BY: [[00_ROOT/00_HOME|00_HOME]]
- INDEXED_BY: [[00_ROOT/AMOS_RSCF_NODES|AMOS_RSCF_NODES]]
- CHILD_OF: references_MOC
