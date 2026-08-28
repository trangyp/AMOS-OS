---
title: AMOS FOREX PACKAGES MURK PRIMITIVES
tags: [amos-general, amos, general, canon/knowledge]
type: note
source: 11_KNOWLEDGE/amos-general
rscf:
  state: SOURCE_CLAIM
  claim_class: SOURCE_CLAIM
  provenance: AMOS_corpus
  scope: AMOS_architecture
---


# AMOS FOREX PACKAGES MURK PRIMITIVES

"""MURK primitive definitions.

The 19 typed primitives are represented by an ``Enum`` for strict type‑checking.
"""

from __future__ import annotations

from enum import Enum

class Primitive(str, Enum):
    EXISTENCE = "Existence"
    NON_EXISTENCE = "NonExistence"
    CAUSALITY = "Causality"
    TEMPORAL = "Temporal"
    INFORMATIONAL = "Informational"
    TOPOLOGICAL = "Topological"
    IDENTITY = "Identity"
    CONVERGENCE = "Convergence"
    DIVERGENCE = "Divergence"
    PARADOX = "Paradox"
    POSITIVE_LOGIC = "PositiveLogic"
    NEGATIVE_LOGIC = "NegativeLogic"
    ZERO_LOGIC = "ZeroLogic"
    DUAL_LOGIC = "DualLogic"
    MULTI_LOGIC = "MultiLogic"
    META_LOGIC = "MetaLogic"
    SUPRA_LOGIC = "SupraLogic"
    ANTI_LOGIC = "AntiLogic"
    NULL_LOGIC = "NullLogic"

__all__ = ["Primitive"]

---
**Related:** [[00_HOME]] · [[KNOWLEDGE_MOC]] · [[AMOS_SIMULATION_KERNEL_V0_MATH_FOUNDATIONS]] · [[SYSTEM_SCAN_AGENT]] · [[AUTOMATION_PROFILES]]

---
**MOC:** [[AMOS-GENERAL_MOC]]

---
**Trang Framework:** [[TRANG_FRAMEWORK_RECURSIVE_ONTOLOGY_DYNAMICS]]
