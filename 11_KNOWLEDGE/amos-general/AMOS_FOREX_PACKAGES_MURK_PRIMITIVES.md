---
title: AMOS FOREX PACKAGES MURK PRIMITIVES
tags: [amos-general]
type: note
source: 11_KNOWLEDGE/amos-general
---


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
**Related:** [[docs/moc/00-Home]] · [[docs/moc/06-Knowledge-Base-MOC]] · [[AMOS_SIMULATION_KERNEL_V0_MATH_FOUNDATIONS]] · [[SYSTEM_SCAN_AGENT]] · [[AUTOMATION_PROFILES]]

---
**MOC:** [[AMOS-GENERAL_MOC]]
