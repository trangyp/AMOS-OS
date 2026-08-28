---
title: Vault Domain Knowledge — Amos Narrative Integrity Governor
type: reference
source: 07_SKILLS/amos-narrative-integrity-governor/references
tags:
- reference
- amos-narrative-integrity-governor
- canon/skill
rscf:
  state: SOURCE_CLAIM
  claim_class: SOURCE_CLAIM
  provenance: AMOS_corpus
  scope: skill_reference
---


# Vault-Sourced Domain Knowledge

> Source: AMOS_OS Obsidian vault (`_00_Cosmo brain/`)
> Epistemic class: SOURCE_CLAIM
> Extracted from skill: `amos-narrative-integrity-governor`

## Vault-Sourced Content

### Source 1: AMOS Absolute Integrity Pass — 2026-08-23

> Path: `amos-general/M/md__2026-08-23 AMOS Absolute Integrity Pass.md` | Size: 3502 chars | Match score: 10

# AMOS Absolute Integrity Pass — 2026-08-23

> Epistemic class: OBSERVATION
> Conclusion label: `HIGH` — All test suites green, zero empty files, zero orphan notes, zero broken wikilinks, test counts reconciled.
> Governing law: `integrity > completeness > fluency > speed > token savings`.

## What Was Done

A comprehensive integrity pass over the entire AMOS brain to eliminate all
gaps: failing tests, empty files, orphan nodes, broken wikilinks, and
inconsistent test counts across documentation.

## Fixes Applied

### 1. Python kernel test failures (2 → 0)
- **`AMOS_GapRegistry.py:run_all_discovery`** — was returning all 6 mode keys
 (with empty lists) even when no input was provided. Tests
 `test_run_all_discovery_partial` and `test_run_all_discovery_empty` expected
 only modes with actual input to appear in the result dict. Fixed by
 initialising `results = {}` and only adding keys when input is provided.
- Python kernel tests: 2013+2 fail → **2015 pass**.

### 2. Empty files filled (3 → 0)
- `FINAL_CLEANUP_COMPLETE.md` — was 0 bytes. Filled with cleanup summary.
- `AMOS_PRODUCTION/scripts/main.py` — was 0 bytes. Filled with production
 entry point stub.
- `AMOS_CANON/__init__.py` — was 0 bytes. Added module docstring.

### 3. Test count reconciliation
| Runtime | Before (doc) | After (actual) |
|---------|-------------|----------------|
| Python kernel (pytest) | 1997 | **2015** |
| TypeScript (vitest) | 1253 | **1392** |
| Kafka Brain Buffer | 180 | 180 |
| Cognitive substrate | 271 | 271 |
| Deterministic verification | 359 | 359 |
| **Grand total** | 4060 | **4217** |

Updated in:
- `amos-deterministic-verification.md`
- `cosmo-brain/AMOS_OS_KERNEL/AGENTS.md`
- `_00_Cosmo brain/2026-08-23 AMOS TypeScript Test Expansion.md`

### 4. Integrity scans (all clean)
- **Orphan notes**: 0 (verified via `ObsidianBrain.orphan_notes()`)
- **Broken wikilinks**: 0 (all `wikilinks` resolve to existing notes)
- **TypeScript compilation**: 0 errors (`tsc --noEmit` clean)
- **Empty files (non-venv)**: 0

## Key Lessons

1. **`run_all_discovery` semantics**: When a method accepts optional inputs for
 multiple modes, only include modes that received input in the result. Empty
 lists for unused modes create false positives in tests and downstream
 consumers.

2. **Test count drift**: Test counts in documentation drift silently as tests
 are added. Reconcile counts after every test expansion session by running
 the actual suite and updating all docs that reference the count.

3. **Empty file triage**: `__init__.py` files are legitimately empty in Python
 packages — add a docstring rather than deleting. Other empty files (`.md`,
 `main.py`) indicate incomplete work and should be filled with real content.

4. **Integrity verification pipeline**: The reliable scan order is:
 (a) run all test suites, (b) `find -size 0` for empty files,
 (c) `ObsidianBrain.orphan_notes()` for orphan notes,
 (d) wikilink resolution check,

---

### Source 2: Vault Integrity Pass — 2026-08-23

> Path: `dated/2026-08-23/2026-08-23 Vault Integrity Pass.md` | Size: 3363 chars | Match score: 10

# Vault Integrity Pass — 2026-08-23

> Applied the 7-part canon lens to the vault itself: what limits, what flows, what holds, what corrects.

## CONSTRAINT (what bounded this pass)
- 83,948 md files — too large to hand-edit. Scope the authoritative cluster (canon notes + main MOCs + `.devin`), not the whole corpus.
- No fabrication: genuine gaps resolved with **pointer/anchor notes** delegating to canonical sources, never invented architecture.

## FLOW (what was done)
1. Baseline: file health (0 empty, 0 broken symlinks ), validator (7/7 canon notes pass `--strict` ).
2. Canon-cluster graph scan → 27 broken targets.
3. Classified: 24 filename-drift (resolve to real files), 3 genuine gaps (no target anywhere).
4. Repaired 24 drift links vault-wide (1,985 links across 55 files; preserved aliases).
5. Created 3 anchor notes: `AMOS Universe Structure Tree.md`, `AMOS Universe Interaction Engine.md`, `amos-audit-repair-master-workflow.md`.
6. Fixed `The Seven Cycles … (Comprehensive Edition)` alias → real `The Seven Cycles of the Trang System™ – Official M.md` (duplicate canon copies at root + `md/`).
7. Upgraded `amos-vault-integrity-audit` skill with honest methodology (vault-wide scan, fenced-code exclusion, authoritative-cluster gate).

## STRUCTURE (what holds it)
- 7 canon notes (root `_00_Cosmo brain/`), validator at `cosmo-brain/tools/` + `~/scripts/`.
- `~/scripts/canon_link_fix_map.json` — the 24-target drift→real mapping.
- Pointer/anchor notes carry `type: pointer` + `aliases:` + `source:` so future audits recognize them as intentional.

## ENFORCEMENT (what corrects errors)
- `validate_canon_notes.py --strict` — deterministic gate.
- `amos-vault-integrity-audit` skill — re-runnable; excludes code fences + placeholders so false orphans don't mask real ones.
- Git repo present at vault root → rollback basin if any future edit regresses.

## TIME / ADAPTATION / TERMINATION
- **Time:** vault-wide auto-dump orphans will keep drifting as new ingests arrive; the cluster gate keeps the *curated brain* clean regardless.
- **Adaptation:** new genuine gaps → add a pointer/anchor note, never fabricate.
- **Termination:** curated-cluster gate is GREEN (0 unresolved). Vast vault-wide dump orphans remain but are known-state + recovery-basin-protected (source data intact). Absolute "zero broken links everywhere" is not claimed — and claiming it would require corrupting real data.

## STATUS
- **Authoritative curated graph: CLEAN** (0 empty, 0 broken symlinks, 0 unresolved cluster targets, validator green).
- Vault-wide data-dump orphans: known-state, not addressed by design.

---

---

### Source 3: 2026-08-25 Quantum-Fractal-Math Consolidation & Integrity Pass

> Path: `dated/2026-08-25/2026-08-25-quantum-fractal-math-consolidation.md` | Size: 3532 chars | Match score: 7

# 2026-08-25 Quantum-Fractal-Math Consolidation & Integrity Pass

## Additional Actions

Priority stack: quantum > fractal > math. All changes additive; no existing content rewritten.

### Skills (2 empty dirs closed — real integrity gaps)

| Skill | Content | Source |
|-------|---------|--------|
| `SKILL.md` | QCLA full framework: K1–K5 claims, 4 logic types (emotion=high-speed, intuition=condensed, instinct=stored, cognition=reflective), coherence-window design, UBI integrity thresholds | `_00_Cosmo brain/Quantum Chemical Logic Architecture (QCLA).md` (Trang Phan, UBI/NeuroSyncAI, 12 Nov 2025) |
| `SKILL.md` | 7-kernel consolidation: C02 super, Engineering Math, Control Systems, Optimization, Prob/Stats, Signal Processing, Simulation + 6 governance gates | 9 vault kernel specs incl. `AMOS_Optimization_Kernel_v0_Math_Foundations.md`, `AMOS_C02_Math_Compute_SUPER.md` (32.9MB) |

Both synced to `~/.devin/skills/`.

### New workflows (3)

1. `amos-fractal-systems-master-workflow.md` — 7-phase unified pipeline: intake classification → H/M/L fractal decomposition → math kernel formulation → quantum-layer check → MURK cross-check → validation gates → storage.
2. `amos-causal-reasoning-master-workflow.md` — molecular coherence pipeline operationalizing K1–K5 with hard epistemic rules.
3. `amos-c02-math-compute-master-workflow.md` — 7-phase math pipeline with failure-mode table.

All synced to `~/.devin/workflows/`.

### New agents (2)

1. `amos-causal-reasoning-master` — 5 capabilities: coherence_window_assessment, logic_type_classification, cross_scale_determinism_trace, coherence_security_analysis, ubi_integrity_gate. Governance block with 4 irreducible limits + 0.95 confidence ceiling.
2. `amos-c02-math-compute-master` — 5 capabilities: kernel_routing, problem_formulation, method_selection_and_solve, sensitivity_and_uncertainty_report, math_governance_pass (6 hard rules).

Both registered additively in `_00_Cosmo Brain/AMOS_AGENT_REGISTRY.json` with provenance (`module_path: UNKNOWN/GAP`, real canon_spec paths verified).

## Verification

- `scripts/brain-integrity-repair.py` then `scripts/brain-consistency-audit.py`: **RESULT: OK** — skills 69 dirs / 0 missing [[SKILL]].md / 0 tiny, 0 empty core files, 0 broken MOC links, registry 137 registered ↔ 94 files, **0 unregistered**.
- Both agent JSONs parse (`json.load` OK); dependency check: all deps resolve on disk.
- `sh scripts/obsidian-health-check.sh`: all checks passed.

## Pre-existing broken deps found (not fixed — out of scope, need owner decision)

- `amos-c05-mind-behavior-master`: 9 bare-name deps that resolve only in Hermes skill space (flattened), not as .devin/skills paths
- `amos-knowledge-research-master` / `amos-causal-reasoning-master`: category-word deps ("workflows", "files", "agents") — malformed dep entries

## Lessons

- Registry repair loop (repair → audit) absorbed all new agents cleanly; keep registering

---
**MOC:** [[references_MOC]]

## Related

- [[07_SKILLS_MOC]]
---

**Related:** [[00_HOME]] · [[AMOS_RSCF_NODES]] · [[LAW_HIERARCHY]] · [[references_MOC]] · [[07_SKILLS_MOC]]

**MOC:** [[references_MOC]]

**Trang Framework:** [[TRANG_FRAMEWORK_RECURSIVE_ONTOLOGY_DYNAMICS]]

---
RSCF-NODE
node_id: amos-narrative-integrity-governor-vault-domain-knowledge
node_type: reference
path: 07_SKILLS/amos-narrative-integrity-governor/references/vault_domain_knowledge.md
RSCF-RELATIONS:
- INDEXED_BY: [[00_HOME]]
- INDEXED_BY: [[AMOS_RSCF_NODES]]
- CHILD_OF: [[references_MOC]]
