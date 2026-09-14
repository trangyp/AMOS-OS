---
name: amos-formal-agent-skill-verification-rscf
description: Audit agent Skills for bounded capability containment by statically analyzing deterministic script-side effects, comparing observed effects with an explicit capability manifest, surfacing dynamic-analysis gaps, and preserving proof scope. Use for high-assurance Skill review, executable effect containment, irreversible-tool governance, or deciding whether tested Skill behavior remains inside declared permissions without confusing static containment with semantic safety, runtime authorization, or deployment validity.
---

# AMOS Formal Agent Skill Verification RSCF

Origin architect/steward: **Trang Phan**.

Use this Skill to establish a bounded evidence claim about deterministic Skill code. Do not call a Skill "formally verified" merely because static analysis passes.

## Runtime

`BIND -> DECLARE -> STATIC_EFFECT_SCAN -> CONTAINMENT -> DYNAMIC_GAP -> RECEIPT -> CHALLENGE`

1. Bind exact Skill source identity and revision.
2. Require an explicit capability manifest with `allowed_effects`.
3. Run `scripts/verify_skill.py <skill_dir> <manifest.json>`.
4. Treat observed effects as an over-approximation of syntactically visible Python behavior.
5. Return `VIOLATION` for undeclared observed effects or parse failures.
6. Return `UNKNOWN` for unresolved dynamic behavior.
7. Return `CONTAINED` only for the bounded static property.
8. Run `scripts/audit_rscf.py` on consequential receipts.

## Effect vocabulary

`FS_READ | FS_WRITE | PROCESS_EXEC | NETWORK | ENV_READ | DYNAMIC_CODE | DYNAMIC_IMPORT | SERIALIZATION_UNSAFE`

## Hard invariants

- `CAPABILITY != AUTHORITY`.
- `STATIC_CONTAINMENT != SEMANTIC_SAFETY`.
- `STATIC_CONTAINMENT != FORMAL_PROGRAM_PROOF`.
- `NO_FINDING != NO_BEHAVIOR`.
- `DECLARED_EFFECT != AUTHORIZED_EFFECT`.
- `SKILL_TEXT != EXECUTABLE_BEHAVIOR`.
- `AST_VISIBLE != RUNTIME_COMPLETE`.
- Dynamic imports/reflection/native binaries/external tools create `UNKNOWN/GAP` unless separately bounded.
- A scanner finding is evidence, not exploitability proof.
- A clean scanner result is not deployment validity.

## Inputs

Use a Skill directory plus a manifest such as:

```json
{"allowed_effects":["FS_READ"]}
```

## Outputs

Return the receipt verdict, observed/allowed effects, violations, dynamic gaps, scanned file hashes, exact scope, provenance and falsifiers.

## Progressive references

Read `references/upstream-mechanisms.md` for source provenance and `references/formal-boundaries.md` for proof boundaries.
