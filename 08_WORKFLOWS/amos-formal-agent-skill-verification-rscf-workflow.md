---
title: amos-formal-agent-skill-verification-rscf-workflow
type: workflow
version: 3.0.0
origin_architect: Trang Phan
epistemic_class: AMOS_MODEL
---

# Workflow: Formal Agent Skill Verification

`BIND -> DECLARE -> STATIC_EFFECT_SCAN -> CONTAINMENT -> DYNAMIC_GAP -> RECEIPT -> CHALLENGE`

## Preconditions
- Bind exact Skill source/revision.
- Load an explicit effect manifest.
- Use the deterministic verifier; prose claims do not substitute for executable evidence.

## Gates
1. Validate `allowed_effects` vocabulary.
2. Scan bundled Python scripts with AST analysis.
3. Compare observed effects against the declared effect set.
4. Return `VIOLATION` for undeclared effects or parse failure.
5. Return `UNKNOWN` when reflection/dynamic behavior escapes the modeled boundary.
6. Return `CONTAINED` only for the bounded AST-visible property.
7. Preserve `CAPABILITY != AUTHORITY` and `STATIC_CONTAINMENT != FORMAL_PROGRAM_PROOF`.

## Output
Return verdict, observed/allowed effects, violations, dynamic gaps, file hashes, scope, receipt hash and unresolved falsifiers.
