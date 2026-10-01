---
title: "AMOS OS Skills — Repository Contract"
type: skill-registry-guide
source: 07_SKILLS
origin_architect: Trang Phan
steward: Trang Phan
status: ACTIVE_GUIDANCE
epistemic_class: AMOS_MODEL
---

# AMOS OS Skills — Repository Contract

## 1. Scope

`07_SKILLS/` is the repository-native AMOS Skill surface.

This guide defines how **new and actively migrated** Skills should be represented, validated, sourced, and composed. It does not claim that every historical Skill already satisfies the current portable format.

```text
SKILL_DECLARED != SKILL_IMPLEMENTED
SKILL_IMPLEMENTED != SKILL_VALIDATED
SKILL_AVAILABLE != SKILL_AUTHORIZED
SOURCE_CLAIM != VERIFIED
LEGACY != INVALID
```

## 2. Repository ownership

Create and edit active AMOS Skills under:

```text
07_SKILLS/<skill-name>/
```

Host-specific mirrors such as `.devin/skills`, `.claude/skills`, editor caches, or user-home Skill directories may exist in particular deployments. They are projections/copies unless a separate governed deployment contract explicitly says otherwise.

Do not assume a host-specific directory exists merely because an older document references it.

## 3. Portable `SKILL.md` entrypoint

For a new or substantially migrated Skill, use only the portable discovery fields in frontmatter:

```yaml
---
name: amos-example-skill
description: What this capability owns and the concrete situations that should trigger it.
---
```

Keep other AMOS metadata in the body or an appropriate machine-readable companion artifact instead of expanding discovery frontmatter indefinitely.

The description is a trigger contract, not a slogan. There is no repository rule requiring an arbitrary fixed character count.

## 4. Skill bundle structure

Preferred bundle:

```text
amos-example-skill/
├── SKILL.md
├── references/       optional, progressively loaded evidence/canon/workflows
├── scripts/          optional deterministic validators/transforms
├── assets/           optional output-consumed assets
└── agents/           optional host-specific projection/config
```

`SKILL.md` should stay operational. Large canon extracts, vault dumps, examples, or raw research belong in targeted references.

## 5. Required semantic content

The body should make material items explicit:

- purpose;
- non-purpose;
- trigger boundary;
- typed inputs;
- typed outputs;
- runtime sequence;
- epistemic/source boundary;
- provenance requirements;
- scope/regime limits;
- failure behavior;
- composition/parent-child boundary;
- validation requirements.

Do not add empty headings merely to satisfy a template.

## 6. Progressive loading

Default:

```text
metadata
-> SKILL.md
-> targeted reference
-> raw evidence only when required
```

This keeps discovery cheap while preserving recoverability.

## 7. Scripts

Use Skill-local or repository-level scripts when deterministic execution is stronger than prose for:

- schema validation;
- package structure checks;
- deterministic transformation;
- benchmark/test harnesses;
- repository scanning.

Every newly introduced deterministic script should have representative positive and negative tests.

## 8. External GitHub Skills and agents

External repositories are reference evidence, not AMOS canon or automatic dependencies.

Use:

- `07_SKILLS/amos-github-agent-skill-integrator/SKILL.md` for governed transfer;
- `11_KNOWLEDGE/EXTERNAL_AGENT_SOURCE_REGISTRY.json` for immutable source pins;
- `06_AGENT_SYSTEMS/GITHUB_AGENT_SKILL_INTEROP.md` for resource/protocol mapping.

Do not bulk-copy public Skill collections into active AMOS.

## 9. Legacy migration

Many historical Skills use extended AMOS frontmatter or older generated structures. Migration is incremental:

```text
TOUCH CAPABILITY
-> INSPECT CURRENT SEMANTICS
-> PRESERVE UNIQUE VALUE
-> SPLIT LARGE REFERENCES IF NEEDED
-> MOVE TO PORTABLE DISCOVERY METADATA
-> VALIDATE
-> REVIEW
```

Do not mass-rewrite hundreds of files only for formatting. A migration must preserve trigger semantics, provenance, dependencies, and unique knowledge.

The repository validator reports untouched legacy schemas as migration warnings unless `--strict-legacy` is explicitly requested.

## 10. Duplicate and overlap rule

Before creating a Skill, classify:

```text
NEW_CAPABILITY
EXISTING_THIN_SKILL
DUPLICATE
OVERLAP
ALIAS
SUPERSEDING_UPDATE
UNKNOWN
```

Naming differences do not justify duplicate capability ownership.

When overlap exists, strengthen the canonical owner or define a precise boundary before creating another Skill.

## 11. AMOS 7-Part mapping

Constraint / Flow / Structure / Enforcement / Time / Adaptation / Termination remains an AMOS persistence-analysis axis where relevant.

It is not a mandatory decorative section for every Skill. Include 7-Part mapping when it changes routing, completeness reasoning, or validation. Do not claim that the entire Skill inventory is MECE merely from labels or counts.

## 12. Validation

Current repository gate:

```bash
python3 scripts/validate_agent_skill_surface.py --summary
```

For GitHub-derived capability work also run:

```bash
python3 scripts/validate_external_agent_sources.py
python3 scripts/validate_workflow_references.py
python3 -m unittest discover -s scripts/tests -p 'test_*.py' -v
```

Use `--strict-legacy` only in a scoped migration change intended to repair the resulting legacy findings.

## 13. Authority

A Skill may describe how to perform a capability. It may not self-grant invocation, tool, commit, merge, release, or production authority.

```text
SkillCapability
  + ResolvedTaskScope
  + FreshAuthority
  + ValidDependencies
  -> EligibleInvocation
```

This is a structural AMOS decision rule, not an empirical equation.

## 14. Indexing

Use `07_SKILLS/07_SKILLS_MOC.md` and generated/validated indexes when available. Historical inventory counts are observations tied to their source snapshot and must not be presented as current truth without a current scan.
