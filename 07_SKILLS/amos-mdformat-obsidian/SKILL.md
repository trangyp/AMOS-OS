---
schema_version: 1.0
name: amos-mdformat-obsidian
description: AMOS mdformat-obsidian — Obsidian vault Markdown formatting using mdformat-obsidian and related plugins. Use when formatting Obsidian-flavored Markdown files (callouts, footnotes, task lists, dollar math, wikilinks), fixing broken YAML frontmatter parsing, normalizing thematic breaks/bullet markers/code block fences, or migrating legacy tags to RSCF structural-axis taxonomy. Use whenever the user mentions mdformat, obsidian formatting, vault formatting, wikilink normalization, or frontmatter fixing — even without explicitly asking for 'mdformat'. Do not use for non-Obsidian Markdown files, semantic content rewriting, or tasks outside the AMOS_OS vault context.
license: MIT
parent_skill: amos-knowledge-research-master
domain: knowledge
epistemic_class: AMOS_MODEL
version: 1.1.0
rscf_state: DERIVED
hml_level: L
gmef_gates:
- L0_integrity
- L1_epistemic
- L5_scope
collapse_class: reversible
qfm_gate_set: QFM_v43
law_compliance:
- L0
- L1
- L5
tags:
- type/skill
- canon/skill
- domain/knowledge-research
- rscf/source_claim
- hml/m
- epistemic/source_claim
- amos_os
steward: Trang Phan
language: en
rscf:
  state: DERIVED
  claim_class: DERIVED
  provenance: AMOS_corpus
  scope: AMOS_general
---

# mdformat-obsidian Vault Formatting

## Description## Description

AMOS mdformat-obsidian — Obsidian vault Markdown formatting using mdformat-obsidian and related plugins. Use when formatting Obsidian-flavored Markdown files (callouts, footnotes, task lists, dollar math, wikilinks), fixing broken YAML frontmatter parsing, normalizing thematic breaks/bullet markers/code block fences, or migrating legacy tags to [[RSCF_CANON]] structural-axis taxonomy. Use whenever the user mentions mdformat, obsidian formatting, vault formatting, wikilink normalization, or frontmatter fixing — even without explicitly asking for 'mdformat'. Do not use for non-Obsidian Markdown files, semantic content rewriting, or tasks outside the AMOS_OS vault context.



## Identity## Identity

Origin architect: **Trang Phan**.
Skill for formatting Obsidian vault Markdown files using `mdformat-obsidian` and related plugins.

**Epistemic class**: AMOS_MODEL (tool-based formatting workflow).

## When to Use## When to Use

- Format Obsidian-flavored Markdown files (callouts, footnotes, task lists, dollar math, wikilinks)
- Fix broken YAML frontmatter parsing (4-backtick wrapping bug)
- Normalize thematic breaks, bullet markers, and code block fences
- Migrate legacy tags to RSCF structural-axis taxonomy
- Use the Obsidian vault as the reasoning brain for canonical formatting and tagging
- Run the full `amos-vault-formatting-tagging` workflow to batch-normalize frontmatter and tags
- Verify vault health via Obsidian MCP after formatting



## Validation Gates## Validation Gates

- **[[L0_INTEGRITY]] Integrity**: No content deleted during formatting — only whitespace/syntax restructured
- **[[L1_EPISTEMIC]] Epistemic**: All formatting changes tagged as DERIVED with provenance
- **[[L5_SCOPE_REGIME]] Scope**: Only vault-scoped files processed; no external files modified
- **[[L7_AUTHORITY]] Authority**: Batch vault formatting requires steward approval

## Do not use## Do not use

- For non-Obsidian Markdown files (use standard mdformat without obsidian plugin)
- To alter semantic content of canon artifacts (formatting only, never content rewriting)
- On files with 4-backtick fences wrapping inner 3-backtick blocks (these are legitimate)
- As a substitute for manual review of canon-law changes
- Outside the AMOS_OS Obsidian vault context

## Examples## Examples

**User says:** "Format all canon files in 01_CANON/ with mdformat-obsidian"
→ Run mdformat with obsidian plugin on all .md files in 01_CANON/, normalizing wikilinks, frontmatter, and thematic breaks.

**User says:** "Fix the broken YAML frontmatter in AMOS_EMOTION_CANON.md"
→ Identify the 4-backtick wrapping bug, apply mdformat-frontmatter to normalize YAML parsing.

**User says:** "Migrate legacy tags to RSCF structural-axis taxonomy"
→ Replace old flat tags with nested rscf/* taxonomy tags across vault files using mdformat-obsidian.

## Prerequisites## Prerequisites

### mdformat-obsidian Installation

The vault uses Python 3.12+ for mdformat-obsidian (requires Python >= 3.10).

```sh
# Create venv with Python 3.12
/Users/mac/.local/bin/python3.12 -m venv /tmp/mdformat_venv

# Install from local wheels (if pip hangs on resolution)
/tmp/mdformat_venv/bin/pip install --no-index --find-links=/tmp/mdformat_wheels \
  mdformat mdformat-obsidian mdformat-frontmatter mdformat-wikilink \
  mdformat-gfm mdit-py-plugins

# Or install from PyPI (if network works)
/tmp/mdformat_venv/bin/pip install mdformat mdformat-obsidian mdformat-frontmatter mdformat-wikilink
```

### Installed Plugins

- **mdformat-obsidian** — Obsidian callouts, inline footnotes, task lists, dollar math
- **mdformat-frontmatter** — YAML frontmatter preservation and formatting
- **mdformat-wikilink** — Obsidian `wikilink` preservation
- **mdformat-gfm** — GitHub Flavored Markdown tables, strikethrough

## Capabilities## Capabilities

- **format.validate**: Check if a file is properly formatted (`mdformat --check`)
- **format.file**: Format a single vault file in-place
- **format.batch**: Format multiple vault files in batch
- **format.fix_backtick_wrapping**: Fix the 4-backtick `markdown` wrapping bug that breaks frontmatter parsing
- **format.fix_thematic_breaks**: Convert mdformat's `___` thematic breaks back to `---` for Obsidian compatibility
- **tag.migrate_rscf**: Migrate legacy tags to RSCF structural-axis taxonomy
- **tag.normalize**: Normalize frontmatter tags using Obsidian MCP


## Operations## Operations

1. Execute `format.validate` — format validate with appropriate parameters and validate output.
2. Execute `format.file` — format file with appropriate parameters and validate output.
3. Execute `format.batch` — format batch with appropriate parameters and validate output.
4. Execute `format.fix_backtick_wrapping` — format fix backtick wrapping with appropriate parameters and validate output.
5. Execute `format.fix_thematic_breaks` — format fix thematic breaks with appropriate parameters and validate output.
6. Execute `tag.migrate_rscf` — tag migrate rscf with appropriate parameters and validate output.
7. Execute `tag.normalize` — tag normalize with appropriate parameters and validate output.
## Formatting Workflow## Formatting Workflow

### Step 1: Fix 4-Backtick Wrapping Bug

Some vault files have ````markdown` wrapping that encloses YAML frontmatter in a code block, breaking Obsidian's frontmatter parsing.

**Detection**:
```sh
grep -rl '^````markdown' /Users/mac/Documents/AMOS_OS/ --include='*.md'
```

**Fix for line-1 cases** (frontmatter at start of file wrapped in 4-backtick fence):
1. Remove the ````markdown` line
2. Find the matching `````` close (first 4+ backtick line after a ```text block)
3. Change it to ``` (3 backticks) to properly close the inner code block

**Fix for embedded cases** (frontmatter mid-file, wrapped in 4-backtick fence):
1. Extract the frontmatter block (--- to ---)
2. Move it to the top of the file
3. Remove the 4-backtick wrapping
4. Reassemble: frontmatter + content-before-fence + content-after-close

### Step 2: Run mdformat-obsidian

```sh
/tmp/mdformat_venv/bin/mdformat "<vault_file>"
```

This formats:
- Obsidian callouts (`> [!note]`, `> [!tip]`, etc.)
- Inline footnotes (`^[footnote]`)
- Task list markers (`[x]`, `[?]`, `[/]`, `[-]`)
- Dollar math (`$...$`, `$$...$$`)
- Wikilinks (`note`)
- YAML frontmatter
- Bullet markers (standardizes to `-`)
- Code block fences

### Step 3: Fix Thematic Breaks

mdformat converts `---` thematic breaks to `___` (underscores) or long `______...` lines to avoid ambiguity with YAML frontmatter delimiters. For Obsidian compatibility, convert them back:

```python
import re
content = open(filepath).read()
# Match lines that are only underscores (3 or more, including long underscore lines)
new_content = re.sub(r'^_{3,}$', '---', content, flags=re.MULTILINE)
open(filepath, 'w').write(new_content)
```

This is safe because frontmatter `---` delimiters are already `---` and won't match `^_+$`.

### Step 3a: Restore Stripped Wikilinks

**CRITICAL**: mdformat-wikilink strips `...` syntax from wikilinks pointing to non-existent notes, converting `NOTE_NAME` to bare `NOTE_NAME`. This is destructive and must be reversed.

**Known stripped wikilink targets** (notes that don't exist in the vault):
- `K_ATOMIC_MULTI_RSCF`
- `AMOS_FRACTAL_KNOWLEDGE_NETWORK`
- `AMOS_CORE_RUNTIME_LINEAGE`
- `PROOF_CAPSULE`

**Restoration script**:
```python
import re

STRIPPED_WIKILINKS = [
    "K_ATOMIC_MULTI_RSCF",
    "AMOS_FRACTAL_KNOWLEDGE_NETWORK",
    "AMOS_CORE_RUNTIME_LINEAGE",
    "PROOF_CAPSULE",
]

def restore_wikilinks(content):
    lines = content.split('\n')
    in_code_block = False
    result = []
    for line in lines:
        if line.lstrip().startswith('```'):
            in_code_block = not in_code_block
            result.append(line)
            continue
        for name in STRIPPED_WIKILINKS:
            line = re.sub(
                r'(?<!\[\[)(' + re.escape(name) + r')(?!\]|\w)',
                r'\1', line
            )
        result.append(line)
    return '\n'.join(result)
```

**Also restore bare ALL_CAPS names in `**Related:**` lines**:

**Tags:** #amos_os #skill #knowledge #framework #rscf #agent #authority #canon #claim #confidence #drift #epistemic #evidence
```python
def fix_related_line(line):
    if '**Related:**' not in line:
        return line
    parts = line.split(' · ')
    result = []
    for part in parts:
        content = part.strip().replace('**Related:**', '').strip()
        if content and not content.startswith('[['):
            if re.match(r'^[A-Z][A-Z0-9_]{2,}$', content) or \
               re.match(r'^AMOS_[A-Z]', content) or \
               re.match(r'^L\d+_', content):
                if '**Related:**' in part:
                    prefix = part[:part.index('**Related:**') + len('**Related:**')]
                    part = prefix + ' ' + content + ''
                else:
                    part = '' + content + ''
        result.append(part)
    return ' · '.join(result)
```

### Step 3b: Restore LaTeX \( \) Inline Math Delimiters

**CRITICAL**: mdformat strips `\(` and `\)` LaTeX inline math delimiters, converting `\(X\)` to plain `(X)`. This breaks Obsidian's math rendering.

**CRITICAL WARNING**: Do NOT restore `\(` `\)` inside `$$` display math blocks!
Inside `$$...$$` blocks, plain parentheses ARE math notation. Adding `\(` `\)` inside
`$$` blocks breaks rendering. Only restore `\(` `\)` for **inline math** outside `$$` blocks.

**Restoration patterns** (apply ONLY outside code blocks AND outside `$$` math blocks):
- `\(X\)` where X is a single capital letter: `(C)` → `\(C\)`
- `\(X_y\)` where X is capital with subscript: `(R_A)` → `\(R_A\)`
- `\(X^y\)` where X is capital with superscript: `(p^*)` → `\(p^*\)`
- `\(r_1,r_2\)` comma-separated math: `(r_1,r_2)` → `\(r_1,r_2\)`
- `\(Replay\)` capitalized words in math context: `(Replay)` → `\(Replay\)`

**Do NOT restore** (these are regular parentheses, not LaTeX):
- `ABORT(Conflict)` — function call notation
- `Preserve(Lineage)` — function call notation
- `Confidence(Receipt)` — function call notation
- `(The)`, `(This)`, `(For)` — regular prose
- ANY `(X)` inside `$$...$$` blocks — these are already math mode

**Also fix**: mdformat escapes `*` inside former LaTeX: `p^\*` → `p^*`

### Step 3c: Fix YAML Wikilink Keys

**CRITICAL**: Do NOT convert YAML keys to wikilinks. When restoring wikilinks,
only restore them in prose text, `**Related:**` lines, and RSCF-RELATIONS sections.
YAML keys like `PROOF_CAPSULE:` must remain as plain identifiers, NOT `[[L19_PROOF_CAPSULE]]:`.

**Detection**: Check inside `yaml` code blocks for `...:` patterns at line start.
**Fix**: `[[L19_PROOF_CAPSULE]]:` → `PROOF_CAPSULE:`

```python
def fix_escaped_asterisks(content):
    content = re.sub(r'\^\\\*', '^*', content)
    return content
```

### Step 3c: Fix Related Line Spacing

mdformat may remove spaces around `·` (middle dot) in `**Related:**` lines. Ensure consistent ` · ` spacing:

```python
def fix_related_spacing(line):
    if '**Related:**' not in line:
        return line
    line = re.sub(r'\]·', '] ·', line)
    line = re.sub(r'·\[', '· [', line)
    line = re.sub(r'(\w)·', r'\1 ·', line)
    line = re.sub(r'·(\w)', r'· \1', line)
    return line
```

### Step 4: Verify Frontmatter Parsing

Use the Obsidian MCP to verify frontmatter is now parsed correctly:

```
frontmatter action=get path="<vault_relative_path>"
```

If `frontmatter` returns `null`, the frontmatter is still broken.

### Step 5: Migrate Tags to RSCF Structural-Axis Taxonomy

Add RSCF structural-axis tags to the frontmatter:

| RSCF Tag | Used For |
|----------|----------|
| `rscf/D-distinction` | identity, classification, difference |
| `rscf/C-constraint` | hard limits, invariants, canon constraints |
| `rscf/G-relation` | coupling, interconnection, dependency |
| `rscf/S-state` | runtime condition, formal state |
| `rscf/T-topology` | architecture, graph structure |
| `rscf/M-memory` | persistent knowledge, historical state |
| `rscf/K-compression` | summarization, representation reduction |
| `rscf/P-repair` | correction, test repair |
| `rscf/μ-mutation` | evolution, change, version transition |
| `rscf/B-boundary` | memory boundaries, system boundaries |
| `rscf/X-cross-scale` | multi-level systems |
| `rscf/E-entropy` | drift, disorder, lacunarity |
| `rscf/type-model` | model artifact |
| `rscf/type-system` | system artifact |
| `rscf/type-process` | process artifact |
| `rscf/type-evidence` | evidence artifact |
| `rscf/type-concept` | conceptual artifact |

Use the Obsidian MCP `frontmatter` tool with `action=set` to update tags:
```
frontmatter action=set path="<path>" key=tags value=["tag1", "rscf/C-constraint", ...]
```

## Canon File Tag Mapping## Canon File Tag Mapping

For canon files in `01_CANON/03_COGNITION_CANON/`:

| Canon File | RSCF Tags |
|------------|-----------|
| AMOS_COGNITIVE_FIELD_CANON | `rscf/C-constraint`, `rscf/D-distinction`, `rscf/S-state`, `rscf/type-model` |
| AMOS_CONSCIOUSNESS_CANON | `rscf/C-constraint`, `rscf/D-distinction`, `rscf/type-concept` |
| AMOS_COGNITION_CANON | `rscf/C-constraint`, `rscf/D-distinction`, `rscf/G-relation`, `rscf/type-model` |
| AMOS_ATTENTION_CANON | `rscf/C-constraint`, `rscf/D-distinction`, `rscf/S-state`, `rscf/type-model` |
| AMOS_COGNITION_MASTER_CANON | `rscf/C-constraint`, `rscf/D-distinction`, `rscf/G-relation`, `rscf/T-topology`, `rscf/type-system` |

## Vault Health Verification## Vault Health Verification

After formatting, verify vault health using Obsidian MCP:

```
# Check frontmatter is parsed
frontmatter action=get path="<path>"

# Check note metadata (tags, headings, links)
note_inspect path="<path>"

# Check for broken wikilinks
wikilinks query=broken

# Check vault statistics
vault_info
```

## Important Notes## Important Notes

- **Always backup files before formatting**: `cp <file> /tmp/<backup>`
- **mdformat modifies files in-place**: use `--check` first to preview
- **The `___` to `---` post-processing is required** for Obsidian compatibility
- **Wikilink stripping is destructive**: mdformat-wikilink strips `[[]]` from wikilinks to non-existent notes — must restore after formatting
- **LaTeX `\( \)` stripping is destructive**: mdformat strips `\(` and `\)` delimiters — must restore after formatting
- **NEVER restore `\( \)` inside `$$` math blocks**: Inside `$$...$$`, plain `()` is already math mode. Adding `\(\)` breaks rendering.
- **NEVER convert YAML keys to wikilinks**: `PROOF_CAPSULE:` in YAML blocks must stay as-is, NOT `[[L19_PROOF_CAPSULE]]:`
- **Related line spacing**: mdformat may remove spaces around `·` — must fix after formatting
- **Frontmatter `---` delimiters are preserved** by mdformat-frontmatter plugin
- **mdformat-frontmatter sorts frontmatter keys alphabetically** and removes quotes — this is expected behavior
- **4-backtick fences are legitimate** when wrapping content with inner 3-backtick blocks (e.g., `CANON_X_KNOWLEDGE.md`) — do not "fix" these
- **Tag migration is idempotent**: once `rscf/*` tags are present and `canon-group/*` tags are absent, the file is considered migrated

## Reference## Reference

### Epistemic Boundaries

- All outputs must carry epistemic class label (SOURCE/DERIVED/AMOS_MODEL/EMPIRICAL).
- No claim beyond the declared scope.
- Never promote AMOS_MODEL to SOURCE or EMPIRICAL without external evidence.

## Provenance## Provenance

- **Origin architect**: Trang Phan

- **Origin architect**: Trang Phan

- **Skill**: amos-mdformat-obsidian
- **Source**: AMOS_OS Obsidian vault (`/Users/mac/Documents/AMOS_OS`)
- **Vault source**: `11_KNOWLEDGE/rscf/RSCF_STRUCTURAL_TAG_MIGRATION.md`
- **Tool**: [mdformat-obsidian](https://github.com/KyleKing/mdformat-obsidian) v0.3.2
- **Created**: 2026-08-28

## SOTA Data Trustworthiness (2026)## SOTA Data Trustworthiness (2026)

> **Source**: Atlan/UC Irvine 2026 study — 99% of SKILL.md files have at least one flaw; the 6th practice (data trustworthiness) is named by zero conventional guides.

### Data Trustworthiness Checks

Before applying this skill's outputs, validate:

1. **Freshness**: Is the source data current? Check `content_hash` and vault modification dates. If source is >90 days old and domain is fast-moving, flag as STALE_SOURCE.
2. **Ownership**: Is the source owned by a recognized authority? Vault canon (Trang Phan) = SOURCE_CANON. External papers = SOURCE_CLAIM. User-provided = OBSERVATION. Unattributed = UNKNOWN/GAP.
3. **Certification**: Has the source been validated? Validated sources have `content_hash` matches. Unvalidated sources require independent corroboration (2+ sources) before consolidation.
4. **Integrity**: Has the source been modified since last validation? If `content_hash` mismatches recomputed hash, flag as INTEGRITY_GAP and trigger revalidation.

### Trustworthiness Decision

- SOURCE_CANON + fresh + integrity_verified = TRUSTED (confidence ceiling: 1.0)
- SOURCE_CLAIM + fresh + integrity_verified = RELIABLE (confidence ceiling: 0.95)
- SOURCE_CLAIM + stale or integrity_unverified = CONDITIONAL (confidence ceiling: 0.7)
- UNKNOWN/GAP + any = UNTRUSTED (confidence ceiling: 0.5, require human review)

## SOTA Evaluation Contract (2026)## SOTA Evaluation Contract (2026)

> **Source**: AEVAL (arxiv 2607.16345) — deterministic, reproducible test pipeline. ACES (arxiv 2608.20614) — paired live trials with and without skill.

### Eval Contract

```yaml
eval_contract:
  skill_name: amos-mdformat-obsidian
  test_tasks:
    - id: basic_trigger
      input: "Query matching this skill's domain"
      expected: "Structured output with epistemic labels and provenance"
    - id: scope_violation
      input: "Query outside this skill's domain"
      expected: "Reject and route to parent skill"
    - id: grounding_check
      input: "Query with insufficient evidence"
      expected: "Flag as GROUNDING_GAP, downgrade confidence"
    - id: regression_osmosis
      input: "Query that should NOT trigger this skill"
      expected: "Skill does not influence output when not triggered"
  grading:
    executor_grader_separation: true
    first_attempt_grading: true
    self_correction_tracking: true
  metrics:
    - skill_lift: "improvement over baseline without skill"
    - regression_rate: "tasks that worsened with skill"
    - grounding_fidelity: "outputs grounded in actual input"
    - verification_completeness: "post-execution checks performed"
```

### Regression Test Protocol

1. Run paired trials: with-skill vs without-skill
2. Measure Skill Lift (improvement) and Regression (worsening)
3. Track 3 regression modes: osmosis, grounding displacement, verification displacement
4. If regression rate > 10%, flag skill for review
5. Executor and grader MUST be structurally separated (no self-grading bias)

## SOTA Regression Prevention (2026)

> **Source**: The Regression Tax (arxiv 2607.22520) — skills can make agents worse via 3 modes. Reliability depends more on grounding and verification than procedural skill choice.

### Mode 1: Description Osmosis Guard

A skill changes agent behavior just by being present in context, even when never invoked.

**Guard**: This skill's description is scoped to its exact trigger conditions. When not triggered, the skill MUST NOT influence agent behavior. Agents MUST NOT apply this skill's procedures to tasks outside its declared scope, even if the skill content is loaded in context.

### Mode 2: Grounding Displacement Guard

A skill's prescribed procedure overrides how the agent interprets its inputs.

**Guard**: This skill's procedure MUST NOT override input interpretation. The agent MUST ground all reasoning in the actual input data, user intent, and observed context — not in the skill's procedural assumptions. If the skill's procedure conflicts with input evidence, input evidence wins. The skill provides HOW to reason, not WHAT to reason about.

### Mode 3: Verification Displacement Guard

A skill's procedure suppresses checks the agent would otherwise perform on its outputs.

**Guard**: This skill MUST NOT suppress post-execution verification. After executing this skill's procedure, the agent MUST independently verify: (1) output matches input intent, (2) output is internally consistent, (3) output does not exceed declared scope, (4) epistemic class labels are accurate. Verification is mandatory, not optional.

## SOTA Grounding Support (2026)

> **Source**: The Regression Tax (arxiv 2607.22520) — grounding displacement is the dominant source of persistent failures. Skills over-support procedure and under-support grounding.

### Input-Grounded Reasoning

All outputs from this skill MUST be grounded in:
1. **Input data**: The actual data provided, not the skill's assumptions about what data should look like
2. **User intent**: What the user actually asked for, not what the skill assumes they want
3. **Observed context**: The real state of the world, not the skill's model of it
4. **Source evidence**: Vault sources, empirical data, or established math — not the skill's internal logic

### Grounding Checks (execute before output)

- [ ] Does the output reference actual input data, not assumed data?
- [ ] Does the output address the actual user request, not a template request?
- [ ] Does the output reflect the current state, not a stale snapshot?
- [ ] Are claims traced to source evidence with provenance?

If any check fails, downgrade confidence and flag as GROUNDING_GAP.

## References

See references/ directory for detailed sub-files. Read references/ files when deeper context is needed for this capability.
