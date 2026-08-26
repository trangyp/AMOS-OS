---
name: skill-naming-audit
version: 1.0.0
source: 00_ROOT/00_ROOT_NAMING_STANDARD.md
description: AMOS skill naming audit produced from .devin/skills across vault and runtime trees.
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

See `[[SKILL_RENAME_MANIFEST]]` for the full mapping.

## Next Steps
1. Review the manifest for source-protected names (e.g., `absolute-logic`, `supercurrent`, `omega` if source-defined).
2. Decide whether to keep deprecated names as redirect stubs or replace outright.
3. Approve the cosmetic/automated renames or request a source-aware pass.
