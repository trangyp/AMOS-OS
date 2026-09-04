---
origin_architect: Trang Phan
steward: Trang Phan
amos_core_target: v4.4
title: Vault Ingest 2026-08-30
type: synthesis
source: 11_KNOWLEDGE/LLM_WIKI
tags:
  - ingest
  - vault
  - llm-wiki
  - canon/knowledge
  - karpathy-llm-wiki-summary
  - vault-reformat
rscf:
  state: DERIVED
  claim_class: DERIVED
  provenance: AMOS_corpus
  scope: AMOS_general
---

# Vault Ingest 2026-08-30

Vault-wide reformat of all Markdown notes to the LLM-wiki convention. Single deterministic, content-preserving pass over 7,062 source files.

## Summary

- **Command**: `python3 scripts/ingest_wiki_reformat.py` (rerunnable; `--dry-run` is read-only, verified idempotent)
- **Scan**: 7,062 `.md` files (vault excludes hidden dirs, `node_modules`, `LLM_WIKI/raw/`, live `copilot/` logs)
- **Modified**: 787 files tracked in git, 0 files where content meaning changed
- **Backup**: tar of all 7,132 `.md` files (124 MB) taken before the pass
- **Fence-aware**: all edits skip inside fenced code blocks; unbalanced fences were closed with a matching closer

## Fixes applied

| Fix                                         | Count  | Note                                                                   |
| ------------------------------------------- | ------ | ---------------------------------------------------------------------- |
| `*`/`+` bullet → `-`                        | 25,539 | column-0 and indented, outside code fences                             |
| Excess blank-line runs collapsed            | 1,679  | 3+ blank lines → 2                                                     |
| `___` horizontal rule → `---`               | 1,171  | outside code fences                                                    |
| Missing trailing newline added              | 85     |                                                                        |
| Unclosed code fence closed                  | 84     | opener length ≥ closer run kept intact (4-backtick wrappers preserved) |
| `title:` added to frontmatter               | 23     | inserted as first key; YAML `tags:`-first regression fixed and re-run  |
| Glued duplicate headings split (`## A## A`) | 17     |                                                                        |
| Minimal frontmatter added                   | 10     | files with no frontmatter at all                                       |
| Embedded frontmatter unwrapped              | 3      | body restored; inner dangling fences closed                            |

Deliberately **not** applied: `#heading` tag lines (tag clouds, not headings) and `* * *` marker runs (valid horizontal rules).

## Files touched by directory

| Directory                                                                                                 | Files |
| --------------------------------------------------------------------------------------------------------- | ----- |
| 07_SKILLS                                                                                                 | 232   |
| 25_COGNITIVE_MATRIX                                                                                       | 138   |
| 11_KNOWLEDGE                                                                                              | 129   |
| 01_CANON                                                                                                  | 84    |
| 00_ROOT                                                                                                   | 48    |
| 05_COGNITIVE_ORGANISM                                                                                     | 43    |
| 03_CONTROL_PLANE                                                                                          | 31    |
| 08_WORKFLOWS                                                                                              | 26    |
| 13_MODELS                                                                                                 | 18    |
| 02_KERNEL                                                                                                 | 13    |
| 16_SCHEMAS                                                                                                | 8     |
| 24_ARCHIVE                                                                                                | 8     |
| 12_STATE                                                                                                  | 2     |
| 21_DOMAINS                                                                                                | 1     |
| .github                                                                                                   | 1     |
| loose root files (CLAUDE.md, skill-catalog.md, amos-skill-registry-gateway.md, skill-registry-catalog.md) | 4     |

## Special cases

- `HERITAGE_MODEL_REGISTRY.md` / `NEUROSYNCAI_MODEL_REGISTRY.md`: real top frontmatter + 4-backtick-wrapped payload — **not** unwrapped (would duplicate a broken frontmatter); title added only.
- `13_MODELS/04_DOMAIN/TSS_MODEL_REGISTRY.md`, `11_KNOWLEDGE/trang/Constraint-Centered Intelligence: Full Reformatted Map.md`, `11_KNOWLEDGE/trang/TRANG_L_M_H_DINH_NGHIA_VA_PHUONG_TRINH.md`: embedded frontmatter unwrapped with body preserved.
- arxiv `0801.4950v1_Turmoil_in_Orion__The_Nearest_Massive_Protostar.md`: unquoted asterisk-heavy title breakage fixed via quoting.
- 6 `copilot/skills/...` reference files: excluded (skill-owned docs).

## Follow-up fixes (same day)

- `25_COGNITIVE_MATRIX/UBI_X_FULL_BRAIN.md`: mangled leading block repaired — proper frontmatter (title/type/source/tags/rscf), 6 `*` bullets → `-`, RSCF-NODE + MOC footer added to match all sibling plane files. YAML now parses; vault-wide bad-YAML count is **0**.
- Re-swept every remaining `* `/`+ ` line and underscore run:
  - `07_SKILLS/amos-forex-unified-os-updated/references/vault_domain_knowledge.md` line 270: 70-underscore divider sits inside a broken JSON-excerpt fence (source was truncated in original vault content; noted in an inline HTML comment). Left untouched — content-level extraction damage, not formatting.
  - `11_KNOWLEDGE/_arxiv_md/2007/0710.5942_..._BG.md` line 718: lone `_` is a mangled LaTeX subscript from markitdown conversion — content-level, left.
  - Tab-indented `\t____...` divider in `TRANG_REALITY_ARCHITECTURE.md` renders inside an indented code diagram — intentional ASCII, left.
  - Single `_` lines in both NAMING_STANDARD files are inside code fences (allowed-character examples) — intentional, left.

## Remaining known issues

- **None at the formatting level.** Vault-wide scan: 0 unclosed fences, 0 bad YAML, 0 stray bullets.

## Verification

- Re-run reports `0 files would be modified` (idempotent)
- Strict fence scan: **0** unclosed fences across all 7,081 scanned files
- YAML scan: only the pre-existing `UBI_X_FULL_BRAIN.md` fails to parse

______________________________________________________________________

```RSCF-NODE
node_id: vault_ingest_2026_08_30
node_type: synthesis
path: 11_KNOWLEDGE/LLM_WIKI/wiki/VAULT_INGEST_2026_08_30.md
RSCF-RELATIONS:
  - INDEXED_BY: [[11_KNOWLEDGE/LLM_WIKI/wiki/LLM_WIKI_INDEX|LLM_WIKI_INDEX]]
  - RELATED_TO: [[11_KNOWLEDGE/LLM_WIKI/wiki/LLM_WIKI_LOG|LLM_WIKI_LOG]]
  - RELATED_TO: [[11_KNOWLEDGE/LLM_WIKI/wiki/llm_wiki_pattern|llm_wiki_pattern]]
  - RELATED_TO: [[00_ROOT/AMOS_LLM_WIKI|AMOS_LLM_WIKI]]
claim_class: AMOS_MODEL
```

______________________________________________________________________

**MOC:** [[11_KNOWLEDGE/LLM_WIKI/LLM_WIKI_MOC|LLM_WIKI_MOC]]
