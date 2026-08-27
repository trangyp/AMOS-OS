---
title: 2026 08 25 QUANTUM V070 APPROVED INDEX SYNC
tags: [dated, dated/2026-08-25]
type: document
source: 11_KNOWLEDGE/dated
---


# Quantum v0.7.0 Full Integration — Session Note (2026-08-25)

## What was done

### 1. Approved Knowledge Index synced to v0.7.0
- Regenerated `cosmo-brain/knowledge/approved/index.ts` via `generate_approved_knowledge_ts.py`
- Now **94 entries total**: 22 foundational (ak-001..022, acoustic/wellness/safety/privacy/reasoning/go-board/semantic-matrix) + 72 quantum-physics (q-am-*, including new q-am-qec-006/007/008 ZNE/PEC/QLDPC)
- Evidence levels: established (all 3 new entries)

### 2. Root-cause fixes found during sync
1. **Generator missing exports**: `generate_approved_knowledge_ts.py` never emitted `APPROVED_KNOWLEDGE` const or `getApprovedKnowledge()` function that tests and downstream code import → added both (backwards-compatible aliases).
2. **Foundational entries dropped**: the generator overwrote the pre-quantum ak-* entries. Fixed by preserving them from a static part-file `knowledge/approved/foundational_ak_entries.ts.part` that the generator inlines before quantum entries.
3. **Bridge empty-source bug**: `_build_source()` returned `""` when provenance existed but all fields were empty → now falls back to `AMOS Quantum Library, {entry.id}`.
4. **Test category list stale**: `tests/unit/knowledge.test.ts` validCategories lacked `"quantum-physics"` → added.

### 3. Verification results (live runs, this session)
| Gate | Result |
|---|---|
| Quantum loader integration | ✓ Integration OK — axioms 64 / bounds 70 / invariants 42 / FMs 45 |
| Library parse | 72/72 unique entries, version 0.7.0 |
| TS suite | **1142/1142 passed (72 files)** |

## Commits
- `5e36e46` — Quantum v0.7.0 cycle + skills/workflows/agents
- `aad3623` — Restore clobbered skills
- `5e8f26a` — Approved index sync to v0.7.0 + generator/bridge/test fixes

## Lessons
- Auto-generators must preserve non-generated content (foundational entries were silently lost on regeneration).
- Always run the consumer tests after regenerating an index — the export-contract drift was invisible until vitest ran.
- Background consolidation processes remain active: check `wc -c` on newly written skills before trusting writes.

---
**Related:** [[docs/moc/00-Home]] · [[docs/moc/06-Knowledge-Base-MOC]] · [[2026-08-25-qfm-pass15-corpus-depth]] · [[2026-08-25-qfm-pass5-zero-empty]] · [[2026-08-25-qfm-pass4-runtime-sync]]

---
**MOC:** [[DATED_MOC]]
