---
title: SKILL NAMING AUDIT
type: skill
name: skill-naming-audit
version: 1.0.0
source: 00_ROOT/00_ROOT_NAMING_STANDARD.md
description: AMOS skill naming audit produced from .devin/skills across vault and
  runtime trees.
tags:
- note
- 07-skills
- type/skill
rscf:
  state: DERIVED
  claim_class: DERIVED
  provenance: AMOS_corpus
  scope: AMOS_general
---

# AMOS Skill Naming Audit

## Scope
- Trees scanned: 2
- Total `SKILL.md` instances: 1268
- Unique names: 634
- Compliant (`OK`): 1156
- Non-compliant: 112

## Issue Summary
| Issue | Count |
|-------|------:|
| OK | 1156 |
| DECORATIVE:omega | 30 |
| DECORATIVE:super | 24 |
| DECORATIVE:full | 16 |
| DECORATIVE:absolute | 10 |
| DECORATIVE:max | 10 |
| DECORATIVE:best | 8 |
| DECORATIVE:complete | 6 |
| DECORATIVE:report | 6 |
| DECORATIVE:vomni | 6 |
| DECORATIVE:ultimate | 4 |
| DECORATIVE:new | 2 |
| DECORATIVE:infinity | 2 |
| DECORATIVE:final | 2 |
| NON_ASCII | 2 |

## Rename Manifest
112 skills have a proposed canonical name different from the current `name`.

See `` for the full mapping.

## Enhancement Pass
After the rename, a second pass ran through all `SKILL.md` files:

- Filled empty `description` frontmatter fields from body content: **451** skills.
- Updated internal references to renamed skills in redirect/consolidated notes: **358** substitutions.
- Verified `amos-19x19-family` retains its own full specification (not a redirect).

## Next Steps
1. Review the manifest for source-protected names (e.g., `absolute-logic`, `supercurrent`, `omega` if source-defined).
2. Verify runtime skill resolution in a fresh session.
3. Add any remaining canonical skills to the `07_SKILLS/` index if needed.

---
**MOC:** [[07_SKILLS/07_SKILLS_MOC|07_SKILLS_MOC]]
