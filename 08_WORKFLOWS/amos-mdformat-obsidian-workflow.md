---
Type: Workflow
Skill: amos-mdformat-obsidian
Agent: amos-mdformat-obsidian-agent
Trigger: When Obsidian vault Markdown formatting, frontmatter fixing, tag migration, or wikilink normalization is needed within the knowledge domain
Version: 1.1.0
title: AMOS mdformat-obsidian
tags:
- type/workflow
- domain/cross-domain
- amos_os
---

# Workflow: AMOS mdformat-obsidian

## Preconditions

- The `amos-mdformat-obsidian` skill exists and is loaded.
- The `amos-mdformat-obsidian-agent` agent is available and has valid content_hash.
- The target files are within the AMOS OS Obsidian vault scope.
- Epistemic class labeling is enabled (SOURCE / DERIVED / AMOS_MODEL / EMPIRICAL).
- Git is available for reversibility verification.

## Steps

1. **Intake**: Identify the formatting task and confirm it matches the mdformat-obsidian scope.
   - Classify the query: single file, directory, or full vault
   - Identify specific formatting issues: frontmatter, callouts, wikilinks, tags, math
   - Confirm target paths are within vault scope
2. **Skill Invocation**: Load the `amos-mdformat-obsidian` skill.
   - Read the skill content and validation gates
   - Identify which formatting capabilities are most relevant
3. **Application**: Apply the mdformat-obsidian capability.
   - Tag every output with its epistemic status (SOURCE / DERIVED / AMOS_MODEL)
   - Record provenance for every formatting change
   - Preserve all content — only restructure whitespace and syntax
4. **Validation**: Check results against validation gates.
   - Verify all formatted files parse as valid Markdown
   - Confirm all wikilinks still resolve
   - Confirm all frontmatter fields are preserved
   - Diff against original to confirm only formatting changes
5. **Finalization**: Produce formatting report and commit.
   - Generate summary of changes (files formatted, tags migrated, frontmatter fixed)
   - Tag output with epistemic class and provenance
   - Ensure git reversibility is maintained

## Operations

1. **Intake**: Identify the formatting task and confirm it matches the mdformat-obsidian scope. - Classify the query: single file, directory, or full vault - Identify specific formatting issues: frontmatter, callouts, wikilinks, tags, math...
2. **Skill Invocation**: Load the `amos-mdformat-obsidian` skill. - Read the skill content and validation gates - Identify which formatting capabilities are most relevant
3. **Application**: Apply the mdformat-obsidian capability. - Tag every output with its epistemic status (SOURCE / DERIVED / AMOS_MODEL) - Record provenance for every formatting change - Preserve all content — only restructure whitespace an...
4. **Validation**: Check results against validation gates. - Verify all formatted files parse as valid Markdown - Confirm all wikilinks still resolve - Confirm all frontmatter fields are preserved - Diff against original to confirm only for...
5. **Finalization**: Produce formatting report and commit. - Generate summary of changes (files formatted, tags migrated, frontmatter fixed) - Tag output with epistemic class and provenance - Ensure git reversibility is maintained

## Validation Gates

- [ ] Epistemic class labeled (SOURCE/DERIVED/AMOS_MODEL/EMPIRICAL)
- [ ] Provenance recorded
- [ ] Scope respected (no claim beyond declared scope)
- [ ] Confidence ceiling enforced (weakest load-bearing premise)
- [ ] Gaps classified (CRITICAL/DECISION_RELEVANT/EXPLANATORY/COSMETIC)
## Error Recovery

- **Parse error**: Skip file, log error, continue with remaining files
- **Frontmatter error**: Preserve original frontmatter, flag for manual review
- **Wikilink break**: Revert file immediately, escalate to user
- **Max retries**: 3 per file before skipping

## Failure Paths

- If validation gate fails: revert changes via git, report failure with diagnostics
- If scope violation: stop immediately, escalate to user
- If irreversibility detected: abort, preserve original state

## AMOS Canon Workflow Governance

### GMEF Gate Sequence (L18)
- L0_integrity: No content deleted during formatting
- L1_epistemic: All changes tagged with epistemic class
- L5_scope: Only vault-scoped files processed

### H/M/L Rigor Assignment (L16)
- H-level: Full vault batch formatting (requires steward approval)
- M-level: Directory-level formatting
- L-level: Single file formatting

### RSCF Propagation (L17)
- All formatting changes recorded as DERIVED
- Provenance: original file path + formatting rule applied

## Error Handling

- **Scope violation**: Reject and route to parent skill.
- **Contradiction**: Flag CRITICAL_GAP and halt; do not fabricate canon.
- **Provenance loss**: Mark output as UNKNOWN and request human review.
- **Drift**: Trigger drift alignment governor before re-execution.

## Composition

- Can be invoked by parent skills for domain-specific operations.
- Can delegate to `amos-audit-repair-master` for gap escalation.
- No delegation to non-AMOS skills.

## Provenance

- **Origin architect**: Trang Phan
- **Steward**: Trang Phan
- **Epistemic class**: AMOS_MODEL
- **RSCF state**: SOURCE_CLAIM
