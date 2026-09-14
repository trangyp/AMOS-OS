---
title: AMOS Skill Capability Containment Verifier
type: tool
tier: T1
origin_architect: Trang Phan
epistemic_class: AMOS_MODEL
---

# AMOS Skill Capability Containment Verifier

Local deterministic verifier for bounded script-side effect containment.

## Operations

- `SKILL_STATIC_EFFECT_SCAN`
- `SKILL_EFFECT_MANIFEST_VALIDATE`
- `SKILL_CAPABILITY_CONTAINMENT_CHECK`
- `SKILL_DYNAMIC_GAP_AUDIT`
- `SKILL_CONTAINMENT_RECEIPT_VALIDATE`

Implementation:
`07_SKILLS/amos-formal-agent-skill-verification-rscf/scripts/verify_skill.py`

Effect vocabulary:
`FS_READ | FS_WRITE | PROCESS_EXEC | NETWORK | ENV_READ | DYNAMIC_CODE | DYNAMIC_IMPORT | SERIALIZATION_UNSAFE`

## Boundaries

- `CAPABILITY != AUTHORITY`
- `STATIC_CONTAINMENT != SEMANTIC_SAFETY`
- `STATIC_CONTAINMENT != FORMAL_PROGRAM_PROOF`
- `NO_FINDING != NO_BEHAVIOR`
- `AST_VISIBLE != RUNTIME_COMPLETE`
- Networked external scanners, hosted analyzers, package registries and runtime sandboxes remain separate T3/T2 operations.
