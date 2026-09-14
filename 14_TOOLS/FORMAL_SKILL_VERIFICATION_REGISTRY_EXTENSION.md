# Formal Skill Verification Registry Extension

Candidate T1 registry binding pending master-registry consolidation:

| Tool ID | Entry File | Tier | Capability Mask |
| --- | --- | --- | --- |
| `amos-skill-capability-containment` | `14_TOOLS/SKILL_CAPABILITY_CONTAINMENT_VERIFIER.md` | T1 | `SKILL_STATIC_EFFECT_SCAN | SKILL_EFFECT_MANIFEST_VALIDATE | SKILL_CAPABILITY_CONTAINMENT_CHECK | SKILL_DYNAMIC_GAP_AUDIT | SKILL_CONTAINMENT_RECEIPT_VALIDATE` |

This extension does not grant deployment or execution authority. It exists so the branch has an explicit registry candidate without silently rewriting the master registry before exact-head contract validation.
