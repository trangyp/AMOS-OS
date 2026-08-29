---
title: Vault Domain Knowledge — Amos Core19 Logic Kernel
type: reference
source: 07_SKILLS/amos-core19-logic-kernel/references
tags:
- reference
- amos-core19-logic-kernel
- canon/skill
- cosmo-brain-moc
- integration
- 2026-08-22-executable-code-internals
- 2026-08-22-devin-memory-update
- references-moc
- 2026-08-22-amos-go-board-19x19-runtime-methods
- 00-home
- amos-rscf-nodes
- law-hierarchy
- 07-skills-moc
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
> Extracted from skill: `amos-core19-logic-kernel`

## Vault-Sourced Content

### Source 1: AMOS TypeScript Type-Guards + Safety-Filter + Meta-Logic Test Expansion

> Path: `dated/2026-08-23/2026-08-23 AMOS TypeScript Type-Guards Safety-Filter Meta-Logic Tests.md` | Size: 4137 chars | Match score: 10 | content_hash: 3313748e31e61066

# AMOS TypeScript Type-Guards + Safety-Filter + Meta-Logic Test Expansion

> Epistemic class: OBSERVATION
> Conclusion label: `VERIFIED` — Added 4 new TypeScript test files (119 tests):
> type-guards (39), safety-filter (37), meta-logic (39), meta-logic-bug (4).
> TypeScript: 1195 → 1253 (+58 net). Total: 3400 → 3458.
> Governing law: `integrity > completeness > fluency > speed > token savings`.

## What was done

Added 4 new TypeScript test files covering type guards, safety filter,
meta-logic reasoning, and a meta-logic word-boundary bug regression.

## New Test Files

### 1. `tests/unit/type-guards.test.ts` (39 tests)

Tests `core/type-guards.ts` (100 lines):
- `isRecord`, `isString`, `isNumber`, `isBoolean`, `isNumberArray`, `isStringArray`
- `asString`, `asBoolean`, `asNumber`, `asNumberOrNull`, `asRecord`,
  `asStringArray`, `asNumberArray`
- Tests type narrowing, safe coercion, null handling, edge cases

### 2. `tests/unit/safety-filter.test.ts` (37 tests)

Tests `core/reasoning/safety-filter.ts` (205 lines):
- `filterOutput` — clean output passes, diagnostic language replaced
- `SAFETY_FILTER_VERSION`, `SAFE_EXPLANATIONS`
- `SafetyFilterInput` type, `OutputType` handling
- Tests filtering of diagnostic language, safe replacement explanations

### 3. `tests/unit/meta-logic.test.ts` (39 tests)

Tests `core/reasoning/meta-logic.ts` (407 lines):
- `META_LOGIC_VERSION`, `LOGIC_MODE_PROPERTIES`, `OPERATIONAL_MODES`
- `CURRENT_OPERATIONAL_MODE`, `isRiskScoreAcceptable`
- `canWriteExternally`, `canDeleteExternally`
- `applyLawOfLaw`, `applyRuleOf2`, `applyRuleOf4`, `applySignalFidelity`
- `reason` function with `ReasoningInput` type

### 4. `tests/unit/meta-logic-bug.test.ts` (4 tests)

Regression test for `applyLawOfLaw` word-boundary bug:
- Bug: substring match on 'not' caused false positives ("notable", "note")
- Negation check only inspected the claim, not the evidence
- Tests that "notable" is NOT flagged as a contradiction
- Tests that "note" is NOT flagged as a contradiction

## Test Results

| Suite | Before | After |
|-------|--------|-------|
| TypeScript (vitest) | 1195 (73 files) | 1253 (74 files, +58) |
| Python kernel (pytest) | 1934 | 1934 |
| Cognitive substrate | 271 | 271 |
| **Total** | **3400** | **3458** |

## Cross-Runtime Status

| Runtime | Tests | Status |
|---------|-------|--------|
| Python (AMOS OS Kernel) | 1934 passed | Green |
| Cognitive Substrate | 271 passed | Green |
| TypeScript (Cosmo Brain) | 1253 passed (74 files) | Green |
| **Total** | **3458** | **All green** |

## Grand Total (with deterministic verification)

| Runtime | Tests |
|---------|-------|
| Python kernel (pytest) | 1934 |
| Cognitive substrate (self-tests + pytest) | 271 |
| TypeScript (vitest) | 1253 |
| Deterministic verification | 359 |
| **Grand total** | **3817** |

## Key Source Modules

- `core/type-guards.ts` (100 lines) — runtime type guards and safe coercions
- `core/reasoning/safety-filter.ts` (205 lines) — diagnostic language filt

---

### Source 2: 2026-08-22 Tests Logic Bridge Registry

> Path: `dated/2026-08-22/2026-08-22 Tests Logic Bridge Registry.md` | Size: 1985 chars | Match score: 10 | content_hash: 1a1e9ec54c6d2dc1

# 2026-08-22 Tests Logic Bridge Registry

## Summary
Deep code-level inspection of 5 AMOS brain Python files:
1. `AMOS_INTEGRATION_TEST_DASHBOARD.py` — 22 modules, 1355 checks, 515 integration tests, ALL PASSING
2. `AMOS_LOGIC_OPERATIONAL_MODES.py` — 12 logic modes with algebraic properties, 3 operational modes
3. `AMOS_V5_UNIFIED_BRIDGE.py` — 29-field ImprovementCandidate, 6 non-compensatory refusal conditions
4. `AMOS_V22_INTEGRATION.py` — RSCF v22 with 9 constants (15 layers, 12 types, 13 relations)
5. `AMOS_MASTER_REGISTRY.py` — 677 skills across 10 UTC canonical parts, 66 evolution skills

## Key Findings
- ALL 1355 module checks and 515 integration tests pass (100%)
- 12 logic modes: positive, negative, zero, dual, multi, meta, supra, anti, null, convergence, divergence, paradox
- 3 operational modes: SAFE_INTROSPECTION_ONLY (risk 0.3), EXTERNAL_WRITE_LOW_RISK (0.6), EXPERIMENTAL_BUILD (0.9)
- 6 non-compensatory refusal conditions: constitution change, judge change, self-authorize, failure memory erasure, propagation expansion, reward hacking
- RSCF v22: 15 layers (D,B,T,G,C,S,M,E,μ,Σ,P,O,K,X,Z), 12 types, 13 relation dimensions, 9 collapse states
- 677 skills in master registry across 10 UTC parts (P1_META: 82, P7_APPLIED_OS: 212, P5_SOCIAL: 127)

## Links
- [[COSMO_BRAIN_MOC]]
- executable brain model
- AMOS INTEGRATION TEST DASHBOARD
- 2026_08_22_EXECUTABLE_CODE_INTERNALS — companion inspection of core brain Python files
- 2026_08_22_DEVIN_MEMORY_UPDATE — V22 RSCF Formal Layer verification
- 2026_08_22_AMOS_GO_BOARD_19X19_RUNTIME_METHODS — Go board integration tests

---

### Source 3: AMOS_CORE v3.1 — Logic Fixed

> Path: `amos-general/A/CORE/AMOS_CORE v3.1 — Logic Fixed.md` | Size: 984806 chars | Match score: 8 | content_hash: 592ae42b6ccbd649

"""
AMOS_CORE v3 – Deterministic Reasoning Kernel (Clean Single-File Version)

Status:
- Executable Python module (no external dependencies beyond stdlib).
- Canon-aligned structure with:
    - Core-19 logic + rewrite system
    - Knowledge base + entailment + contradiction detection
- TSS-style system state
    - Task + engine API
- Minimal translation layer (NL <-> logic stubs)
    - Drift / integrity audit hooks
- Placeholders for higher layers (universe, multi-agent, compression) as stubs

This file is designed as a stable nucleus you can extend with:
    - Absolute-Human engine
    - UBI / TSS / PSI domain adapters
- Full multi-agent + universe simulation
while remaining syntactically valid and runnable as-is.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum, auto
from typing import Any, Dict, List, Optional, Tuple, Callable
import itertools
import math
import uuid
import time


# ============================================================
# 0. META / CONFIG
# ============================================================

AMOS_VERSION = "3.0.0-clean"

@dataclass
class CanonProfile:
    """Global canon configuration flags."""
    law_of_law: bool = True
    rule_of_two: bool = True
    rule_of_four: bool = True
    seven_cycle: bool = True
    noise_signal_enforced: bool = True
    causal_compression: bool = True
    identity_cognition_separation: bool = True
    structural_integrity_required: bool = True


@dataclass
class AmosConfig:
    """Engine configuration hooks."""
    canon: CanonProfile = field(default_factory=CanonProfile)
    max_normalize_iters: int = 128
    max_backward_depth: int = 16
    max_learned_rules: int = 2048
    log_debug: bool = False


GLOBAL_CONFIG = AmosConfig()


# ============================================================
# 1. CORE-19 LOGIC KERNEL
# ============================================================

class NodeType(Enum):
    # Base logical structure
    ATOM = auto()
    NOT = auto()
    AND = auto()
    OR = auto()
    IMPLIES = auto()
    BOTTOM = auto()   # ⊥

    # Meta-patterns
    PARADOX = auto()  # Π(X)
    CONV = auto()     # Λ(X)
    DIVG = auto()     # Δ(X)

    # Logic modes
    PLOGIC = auto()   # PositiveLogic
    NLOGIC = auto()   # NegativeLogic
    ZLOGIC = auto()   # ZeroLogic
    DLOGIC = auto()   # DualLogic
    MLOGIC = auto()   # MultiLogic
    METAL = auto()    # MetaLogic

    # Meta-logic modes
    SUPRAL = auto()   # SupraLogic
    ANTIL = auto()    # AntiLogic
    NULLL = auto()    # NullLogic


@dataclass
class Formula:
    """Tree-structured formula node."""
    node_type: NodeType
    children: List["Formula"] = field(default_factory=list)
    atom: Optional[Tuple[str, Tuple[Any, ...]]] = None  # (predicate, args)

    def __repr__(self) -> str:
        t = self.node_type
        if t == NodeType.ATOM:
            pred, args = self.atom or ("?", ())
            args_str = ", ".join(repr(a) for a in

---
**MOC:** references_MOC
---

**Related:** [[00_HOME]] · [[AMOS_RSCF_NODES]] · [[LAW_HIERARCHY]] · references_MOC · [[07_SKILLS_MOC]]

**MOC:** references_MOC

**Trang Framework:** [[TRANG_FRAMEWORK_RECURSIVE_ONTOLOGY_DYNAMICS]]

---
RSCF-NODE
node_id: amos-core19-logic-kernel-vault-domain-knowledge
node_type: reference
path: 07_SKILLS/amos-core19-logic-kernel/references/vault_domain_knowledge.md
RSCF-RELATIONS:
- INDEXED_BY: [[00_HOME]]
- INDEXED_BY: [[AMOS_RSCF_NODES]]
- CHILD_OF: references_MOC
