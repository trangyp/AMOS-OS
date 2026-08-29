---
title: Vault Domain Knowledge — Amos Causal Abstraction Validity Rscf Engine
type: reference
source: 07_SKILLS/amos-causal-abstraction-validity-rscf-engine/references
tags:
- reference
- amos-causal-abstraction-validity-rscf-engine
- canon/skill
- 07-skills-moc
- references-moc
- 00-home
- amos-rscf-nodes
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
> Extracted from skill: `amos-causal-abstraction-validity-rscf-engine`

## Vault-Sourced Content

### Source 1: RSCF — Resonance Scan Causal Field

> Path: `rscf/SKILL (rscf).md` | Size: 1071 chars | Match score: 12 | content_hash: 24f40a537f42f350

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

### Source 2: AMOS_CORE v3.4.1 — Distributed Causal Evolution Runtime

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

### Source 3: AMOS_Analogy_Abstraction_Kernel_v0_Meta_Cognition4_2

> Path: `kernel/A/AMOS_Analogy_Abstraction_Kernel_v0_Meta_Cognition4_2.md` | Size: 6602 chars | Match score: 10 | content_hash: d1803bc2e3f226a6

{
  "kernel_id": "Analogy_Abstraction_Kernel",
  "version": "1.0.0",
  "source": "md/Core/AMOS_Analogy_Abstraction_Kernel_v0.md (category: meta_cognition, from AMOS_Omni_KERNEL.json)",
  "description": "Kernel for analogy and abstraction — mapping structural similarities across domains, extracting abstract patterns from concrete instances, and using analogical reasoning while avoiding false analogies.",
  "group": "Kernels.Meta_Cognition",
  "category": "Meta_Cognition",
  "priority": 9,
  "required": true,
  "domains": ["analogy", "abstraction", "pattern_matching", "cross_domain", "metaphor", "structural_similarity"],
  "depends_on": ["Meta_Logic_Kernel", "Meta_Ontology_Kernel", "Cognitive_Compression_Kernel"],
  "meta": {
    "role": "Analogy and Abstraction Kernel",
    "creator": "Trang Phan (Origin Architect)",
    "status": "defined",
    "binding_rules": ["Law_of_Law", "Rule_of_2", "Rule_of_4", "Absolute_Integrity"],
    "omni_category": "meta_cognition",
    "position": 5
  },
  "purpose": "Enable analogical reasoning across domains by identifying structural similarities, extracting abstract patterns, and using analogies productively while detecting and avoiding false or misleading analogies.",
  "analogy_structure": {
    "source_domain": "The domain being mapped FROM (already understood)",
    "target_domain": "The domain being mapped TO (being understood via analogy)",
    "mapper": "What maps between source and target; the structural correspondence",
    "alignment": "Which elements of source correspond to which elements of target",
    "inferences": "What can be inferred about target based on source knowledge"
  },
  "valid_analogy_criteria": {
    "structural_similarity": "The mapping must preserve structural relationships, not just surface features",
    "relevant_properties_mapped": "Properties relevant to the reasoning task must be mappable between domains",
    "no_critical_differences_ignored": "Known critical differences between domains must be acknowledged, not hidden",
    "bounded_scope": "The analogy has a defined scope; it does not claim to explain everything about the target",
    "productive": "The analogy generates useful inferences, not just decorative similarity"
  },
  "false_analogy_detection": {
    "surface_only": "Mapping based on superficial similarity (name, appearance) without structural correspondence",
    "ignoring_critical_differences": "Hidden or ignored differences that break the mapping for the current purpose",
    "over_extension": "Pushing the analogy beyond its valid scope to draw conclusions it doesn't support",
    "category_error_in_mapping": "Mapping entities from different ontological categories as if they're equivalent",
    "false_precision": "Treating the analogy as more precise than it is; using it as proof rather than illustration"
  },
  "rules": {
    "analogy_illustrates_not_proves": "An analogy can illustrate a structural point but cannot serve as proof. Always distinguish illustratio

---
- [[07_SKILLS_MOC]]
**MOC:** references_MOC
---

**Related:** [[00_HOME]] · [[AMOS_RSCF_NODES]] · [[LAW_HIERARCHY]] · references_MOC · [[07_SKILLS_MOC]]

**MOC:** references_MOC

**Trang Framework:** [[TRANG_FRAMEWORK_RECURSIVE_ONTOLOGY_DYNAMICS]]

---
RSCF-NODE
node_id: amos-causal-abstraction-validity-rscf-engine-vault-domain-knowledge
node_type: reference
path: 07_SKILLS/amos-causal-abstraction-validity-rscf-engine/references/vault_domain_knowledge.md
RSCF-RELATIONS:
- INDEXED_BY: [[00_HOME]]
- INDEXED_BY: [[AMOS_RSCF_NODES]]
- CHILD_OF: references_MOC
