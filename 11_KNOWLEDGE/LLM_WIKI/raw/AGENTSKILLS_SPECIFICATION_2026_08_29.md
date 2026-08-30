---
date: 2026-08-29
epistemic_class: OBSERVATION
provenance: https://agentskills.io/specification, not independently verified
rscf:
  claim_class: DERIVED
  provenance: https://agentskills.io/specification
  scope: AMOS_knowledge
  state: SOURCE_CLAIM
source: https://agentskills.io/specification
title: Agent Skills Specification — Raw Capture
---

# Agent Skills Specification — Raw Capture

Source: `https://agentskills.io/specification`

## Format Specification

An Agent Skill is a directory containing at minimum a `SKILL.md` file.

### Directory Structure

```text
skill-name/
├── SKILL.md          # Required: metadata + instructions
├── scripts/          # Optional: executable scripts
├── references/       # Optional: reference documentation
└── assets/           # Optional: templates and static assets
```

### Frontmatter Fields

`SKILL.md` requires YAML frontmatter:

- `name`: Lowercase, hyphen-separated identifier matching the directory name.
- `description`: 1-2 sentence summary of what the skill does and when to activate it.
- `license`: Optional SPDX license identifier.
- `version`: Semantic version string.

### Progressive Disclosure Protocol

1. **Discovery**: Agent inspects available skill names and descriptions.
2. **Activation**: Agent views `SKILL.md` when intent matches description.
3. **Execution**: Agent follows instructions and executes bundled scripts as required.
