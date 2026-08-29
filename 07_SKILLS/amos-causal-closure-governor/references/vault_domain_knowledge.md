---
title: Vault Domain Knowledge — Amos Causal Closure Governor
type: reference
source: 07_SKILLS/amos-causal-closure-governor/references
tags:
- reference
- amos-causal-closure-governor
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
> Extracted from skill: `amos-causal-closure-governor`

## Vault-Sourced Content

### Source 1: AMOS_CORE v3.4.1 — Distributed Causal Evolution Runtime

> Path: `amos-general/A/CORE/AMOS_CORE v3.4.1 — Distributed Causal Evolution Runtime.md` | Size: 76005 chars | Match score: 10 | content_hash: c7e85dd6d3746e50

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

### Source 2: Vault Orphan-Closure Pass (2026-08-23)

> Path: `dated/2026-08-23/2026-08-23 Vault Orphan-Closure Pass.md` | Size: 2854 chars | Match score: 10 | content_hash: 44b95588c945a882

# Vault Orphan-Closure Pass (2026-08-23)

## Key findings
- The `arxiv_md/` folder (65,953 files) had NO index → bulk of orphans. Fixed with 33 batch indexes.
- 12 root files had Obsidian-illegal link chars (`#`, `[`, `]`, trailing spaces) → renamed to link-safe ASCII (no content change).
- 7PT canon notes live under `md/`, not root — validator `DEFAULT_VAULT` correctly points to `md/` and passes.

## Honest limitations
- "Reachable" ≠ "curated". The 80k dumps remain non-curated data; only the curated canon+MOC are authoritative graph. Indexes are navigational scaffolding, explicitly tagged `type: auto-index`.
- Phantom orphans are a filesystem-cache artifact of `os.walk` during concurrent renames; always verify with `find`/`ls` before claiming a regression.

---

---

### Source 3: RSCF — Resonance Scan Causal Field

> Path: `rscf/SKILL (rscf).md` | Size: 1071 chars | Match score: 10 | content_hash: 24f40a537f42f350

# RSCF — Resonance Scan Causal Field

## Purpose
RSCF (Resonance Scan Causal Field) is the AMOS proof capsule format for
evidence-grounded claims. It provides a structured way to make, audit, and
invalidate claims with dependencies, scope, freshness, competing explanations,
falsifiers, and confidence ceilings.

## Structure
- **Claim**: The assertion being made
- **Evidence**: Supporting evidence with provenance
- **Scope**: Domain and regime boundaries
- **Freshness**: Temporal validity of the evidence
- **Competing**: Alternative explanations
- **Falsifiers**: Conditions that would invalidate the claim
- **Confidence**: Upper bound on confidence level

## Usage
Use RSCF when making consequential claims, code assertions, research findings,
or decisions that require evidence-grounded conclusions.

## Links
- See also: amos-rscf-claims skill
- See also: amos-self-review-loop skill

---

---
- [[07_SKILLS_MOC]]
**MOC:** references_MOC
---

**Related:** [[00_HOME]] · [[AMOS_RSCF_NODES]] · [[LAW_HIERARCHY]] · references_MOC · [[07_SKILLS_MOC]]

**MOC:** references_MOC

**Trang Framework:** [[TRANG_FRAMEWORK_RECURSIVE_ONTOLOGY_DYNAMICS]]

---
RSCF-NODE
node_id: amos-causal-closure-governor-vault-domain-knowledge
node_type: reference
path: 07_SKILLS/amos-causal-closure-governor/references/vault_domain_knowledge.md
RSCF-RELATIONS:
- INDEXED_BY: [[00_HOME]]
- INDEXED_BY: [[AMOS_RSCF_NODES]]
- CHILD_OF: references_MOC
