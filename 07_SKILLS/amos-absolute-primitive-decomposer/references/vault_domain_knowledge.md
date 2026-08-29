---
title: Vault Domain Knowledge — Amos Absolute Primitive Decomposer
type: reference
source: 07_SKILLS/amos-absolute-primitive-decomposer/references
tags:
- reference
- amos-absolute-primitive-decomposer
- type/skill
- law-hierarchy
- trang-framework-recursive-ontology-dynamics
rscf:
  state: SOURCE_CLAIM
  claim_class: SOURCE_CLAIM
  provenance: AMOS_corpus
  scope: skill_reference
---

# Vault-Sourced Domain Knowledge

> Source: AMOS_OS Obsidian vault (`_00_Cosmo brain/`)
> Epistemic class: SOURCE_CLAIM
> Extracted from skill: `amos-absolute-primitive-decomposer`

## Vault-Sourced Content

### Source 1: AMOS Absolute Logic-DB v1.0

> Path: `amos-general/A/Absolute/AMOS Absolute Logic DB v1.0.md` | Size: 4421 chars | Match score: 12

# AMOS Absolute Logic-DB v1.0

## Overview
Complete integrated 19-primitive Absolute Logic-DB with Pre/Absolute/Post states, 19×19 interaction matrix rules, tensor definition, and SQL schema. 0-gap structure.

## Tri-Domain Model

### PreAbsolute (Pre-logical)
States: PrePotential, PreNull, PreBoundary
- Primitive count: 0, Logic count: 0

### Absolute (Logical — active)
Layer: AbsoluteLogicLayer | Variable scale: 1E∞ | Primitive total: 19 | Logic layers: 1

### PostAbsolute (Post-collapse states)
States: DissolutionState, DriftlessState, TerminalQuietState
- Primitive count: 0, Logic count: 0

## 19 Primitives

| ID | Primitive | Category |
|----|-----------|----------|
| 1 | Existence | Pattern |
| 2 | NonExistence | Pattern |
| 3 | Causality | Pattern |
| 4 | Temporal | Pattern |
| 5 | Informational | Pattern |
| 6 | Topological | Pattern |
| 7 | Identity | Pattern |
| 8 | Convergence | MetaPattern |
| 9 | Divergence | MetaPattern |
| 10 | Paradox | MetaPattern |
| 11 | PositiveLogic | Logic |
| 12 | NegativeLogic | Logic |
| 13 | ZeroLogic | Logic |
| 14 | DualLogic | Logic |
| 15 | MultiLogic | Logic |
| 16 | MetaLogic | Logic |
| 17 | SupraLogic | MetaLogic |
| 18 | AntiLogic | MetaLogic |
| 19 | NullLogic | MetaLogic |

## 3 Logic Categories

| Category | Primitives |
|----------|-----------|
| Pattern | Existence, NonExistence, Causality, Temporal, Informational, Topological, Identity |
| MetaPattern | Convergence, Divergence, Paradox |
| Logic | PositiveLogic, NegativeLogic, ZeroLogic, DualLogic, MultiLogic, MetaLogic |
| MetaLogic | SupraLogic, AntiLogic, NullLogic |

## Interaction Rules (Category Matrix)

| Row | Col | Rule |
|-----|-----|------|
| Pattern | Pattern | pattern_interaction(row.key, col.key) |
| Pattern | MetaPattern | apply_meta_pattern(col.key, row.key) |
| Pattern | Logic | logic_applied_to_pattern(col.key, row.key) |
| Pattern | MetaLogic | meta_logic_applied_to_pattern(col.key, row.key) |
| MetaPattern | * | meta_pattern_effect(row.key, col.key) |
| Logic | * | logic_relation(row.key, col.key) |
| MetaLogic | * | meta_logic_transform(row.key, col.key) |

## AbsoluteLogicTensor

```
Shape: [19, 19, 1E∞]
Indices: i=row_idx (1..19), j=col_idx (1..19), k=resolution_idx (0..1E∞-1)
Definition: T[i][j][k] = Eval(interaction_rules(primitives[i], primitives[j]), k)
```

## Collapse Rules

### PreToAbsolute
```
Inputs: PrePotential, PreNull, PreBoundary
Output: AbsoluteLogicLayer
Condition: (PreBoundary == 1) AND (PrePotential != 0 OR PreNull != 0)
```

### AbsoluteToPost

| Rule | Condition | Effect |
|------|-----------|--------|
| DissolutionRule | Paradox + AntiLogic → max | Post = DissolutionState |
| DriftlessRule | dC/dt → 0 AND dL/dE → 0 | Post = DriftlessState |
| TerminalQuietRule | NullLogic = 1 AND all other logic → 0 | Post = TerminalQuietState |

## SQL Schema
```sql
CREATE TABLE primitives (
  id INT PRIMARY KEY,
  key VARCHAR(64),
  category VARCHAR(32),
  description TEXT
);

CREATE TABLE logic_interactions (

---

### Source 2: AMOS Absolute Integrity Pass — 2026-08-23

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
- `amos-deterministic-verification.md` (path may vary)
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

### Source 3: AMOS Absolute Logic Model

> Path: `logic/Absolute_Logic_Model.md` | Size: 1949 chars | Match score: 9

# AMOS Absolute Logic Model

> **Core Engine**: Absolute Logic
> **Skill Mapping**: `amos-absolute-logic-layer`

## Conceptual Framework

The Absolute Logic model is the formal, immutable logic database dictating the non-negotiable rules of interaction between foundational concepts or "primitives." It sits below domain-specific laws (like physics or economics) as pure, abstract relational rules.

### Key Components

#### 1. The 19-Primitive Absolute Logic DB
Defines 19 irreducible foundational primitives (e.g., State, Transition, Boundary, Force, Capacity).
- Every complex concept in other engines must eventually map back to one or more of these primitives.

#### 2. The 19x19 Interaction Matrix
Maps the deterministic outcome when any two primitives interact.
- Example: *Boundary* interacting with *Force* dictates specific yielding, repelling, or threshold-breaking rules.

#### 3. Logic Collapse Rules
Defines specific violation states where reasoning fails structurally:
- **Dissolution**: Loss of bounded identity.
- **Driftless**: Infinite looping without state transition.
- **TerminalQuiet**: Complete cessation of interaction potential.

## Integration & Output
This model is invoked by the `amos-canon-integration-layer` and the `amos-reasoning-kernel-layer` when evaluating the absolute lowest-level validity of a claim. If an argument violates the 19x19 interaction matrix, it is deemed logically collapsed and must be rejected, regardless of domain-specific context.

---

---
**MOC:**

## Related

-
```

---

**Related:** [[amos-absolute-primitive-decomposer_MOC]]
---

**Related:** [[00_HOME]] · [[AMOS_RSCF_NODES]] · [[LAW_HIERARCHY]] · references_MOC · [[07_SKILLS_MOC]]

**MOC:** references_MOC

**Trang Framework:** [[TRANG_FRAMEWORK_RECURSIVE_ONTOLOGY_DYNAMICS]]

---
RSCF-NODE
node_id: amos-absolute-primitive-decomposer-vault-domain-knowledge
node_type: reference
path: 07_SKILLS/amos-absolute-primitive-decomposer/references/vault_domain_knowledge.md
RSCF-RELATIONS:
- INDEXED_BY: [[00_HOME]]
- INDEXED_BY: [[AMOS_RSCF_NODES]]
- CHILD_OF: references_MOC
