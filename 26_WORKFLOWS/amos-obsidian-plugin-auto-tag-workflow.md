---
canon-group: meta
canon-type: framework
rscf-state: source-claim
rscf-claim: verified
rscf-provenance: AMOS_corpus
conclusion_class: AMOS_MODEL
epistemic_class: SOURCE_CLAIM
topic: Amos Obsidian Plugin Auto Tag Workflow
tags:
  - canon-group/tech-ai
  - rscf/claim
  - rscf/provenance
  - rscf/state/source-claim
  - misc
created: 2026-08-22
---
---
---

# Obsidian Plugin Auto Tag

## Preconditions

- Skill `obsidian-plugin-auto-tag` is loaded and available.
- Input falls within the declared domain scope.
- User request matches the trigger conditions above.

## Steps

1. **Route** — Confirm the request is tag generation, normalization, or frontmatter reconciliation for the Obsidian vault.
1. **Load** — Load the `obsidian-plugin-auto-tag` skill and target note/folder scope.
1. **Generate** — Call `auto_tag.generate_tags` with note content and optional selection.
1. **Preview** — Call `auto_tag.preview` to surface candidates with source provenance.
1. **Validate scope** — Call `auto_tag.validate_scope` to filter candidates against canon/knowledge scope.
1. **Detect language** — Call `auto_tag.detect_language` for localized tag candidates.
1. **Normalize** — Call `auto_tag.normalize_format` for the selected target format (kebab-case, snake_case, etc.).
1. **Apply** — Call `auto_tag.update_frontmatter` to insert tags and `auto_tag.fix_formatting` to clean fence/whitespace issues.
1. **Reconcile** — For bulk jobs, call `auto_tag.reconcile_tags` across the folder and produce a diff.
1. **Finalize** — Record a validation receipt and emit the result with provenance.

## Operations

1. **Route** — Confirm the request is tag generation, normalization, or frontmatter reconciliation for the Obsidian vault.
1. **Load** — Load the `obsidian-plugin-auto-tag` skill and target note/folder scope.
1. **Generate** — Call `auto_tag.generate_tags` with note content and optional selection.
1. **Preview** — Call `auto_tag.preview` to surface candidates with source provenance.
1. **Validate scope** — Call `auto_tag.validate_scope` to filter candidates against canon/knowledge scope.
1. **Detect language** — Call `auto_tag.detect_language` for localized tag candidates.
1. **Normalize** — Call `auto_tag.normalize_format` for the selected target format (kebab-case, snake_case, etc.).
1. **Apply** — Call `auto_tag.update_frontmatter` to insert tags and `auto_tag.fix_formatting` to clean fence/whitespace issues.
1. **Reconcile** — For bulk jobs, call `auto_tag.reconcile_tags` across the folder and produce a diff.
1. **Finalize** — Record a validation receipt and emit the result with provenance.

## Validation Gates

- [ ] Tags generated with source provenance
- [ ] Scope validated against canon/knowledge boundaries
- [ ] Language detected and tags localized
- [ ] Format normalized (kebab-case/snake_case/camelCase/PascalCase)
- [ ] Frontmatter updated with valid YAML
- [ ] Formatting co-fixed (fences, whitespace)
- [ ] Epistemic class labeled
- [ ] Confidence ceiling enforced

## Error Handling

- **Scope violation**: Reject and route to parent skill.
- **Contradiction**: Flag CRITICAL_GAP and halt; do not fabricate canon.
- **Provenance loss**: Mark output as UNKNOWN and request human review.
- **Drift**: Trigger drift alignment governor before re-execution.

## Composition

- Can be invoked by parent master skill for domain-specific audits.
- Can delegate to `amos-audit-repair-master` for gap escalation.
- No delegation to non-AMOS skills.

## Provenance

- **Origin architect**: Trang Phan
- **Steward**: Trang Phan
- **Epistemic class**: AMOS_MODEL
- **RSCF state**: SOURCE_CLAIM
