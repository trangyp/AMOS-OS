---
canon-group: meta
canon-type: framework
rscf-state: source-claim
rscf-claim: verified
rscf-provenance: AMOS_corpus
conclusion_class: AMOS_MODEL
epistemic_class: SOURCE_CLAIM
topic: Vault Domain Knowledge
tags:
  - canon-group/tech-ai
  - rscf/claim
  - rscf/provenance
  - rscf/state/source-claim
  - misc
created: 2026-08-22
---
---
---

# Vault-Sourced Domain Knowledge

> Source: AMOS_OS Obsidian vault (`_00_Cosmo brain/`)
> Epistemic class: SOURCE_CLAIM
> Extracted from skill: `amos-causal-hierarchy-governor`

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
- Minimal translation layer (NL \<-> logic stubs)
  - Drift / integrity audit hooks
- Placeholders for higher layers (universe, multi-agent, compression) as stubs

This file is designed as a stable nucleus you can extend with:
\- Absolute-Human engine
\- UBI / TSS / PSI domain adapters

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

## ============================================================

## 0. META / CONFIG

## ============================================================

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

## ============================================================

## 1. CORE-19 LOGIC KERNEL

## ============================================================

class NodeType(Enum):
\# Base logical structure
ATOM = auto()
NOT = auto()
AND = auto()
OR = auto()
IMPLIES = auto()
BOTTOM = auto() # ⊥

```
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
```

@dataclass
class Formula:
"""Tree-structured formula node."""
node_type: NodeType
children: List["Formula"] = field(default_factory=list)
atom: Optional\[Tuple\[str, Tuple[Any, ...]\]\] = None # (predicate, args)

```
def __repr__(self) -> str:
    t = self.node_type
    if t == NodeType.ATOM:
        pred, args = self.atom or ("?", ())
        args_str = ", ".join(repr(a) for a in
```

______________________________________________________________________

### Source 2: RSCF — Resonance Scan Causal Field

> Path: `rscf/SKILL (rscf).md` | Size: 1071 chars | Match score: 10 | content_hash: 24f40a537f42f350

## RSCF — Resonance Scan Causal Field

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

______________________________________________________________________

______________________________________________________________________

### Source 3: AMOS_CORE v4.2 — Deterministic Causal Epoch Runtime

> Path: `amos-general/A/CORE/AMOS_CORE v4.2 — Deterministic Causal Epoch Runtime.md` | Size: 168042 chars | Match score: 8 | content_hash: ecea6a0f73169b7f

"""
AMOS_CORE v3 – Deterministic Reasoning Kernel (Clean Single-File Version)

Status:

- Executable Python module (no external dependencies beyond stdlib).
- Canon-aligned structure with:
  - Core-19 logic + rewrite system
  - Knowledge base + entailment + contradiction detection
- TSS-style system state
  - Task + engine API
- Minimal translation layer (NL \<-> logic stubs)
  - Drift / integrity audit hooks
- Placeholders for higher layers (universe, multi-agent, compression) as stubs

This file is designed as a stable nucleus you can extend with:
\- Absolute-Human engine
\- UBI / TSS / PSI domain adapters

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

## ============================================================

## 0. META / CONFIG — part 2

## ============================================================

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

## ============================================================

## 1. CORE-19 LOGIC KERNEL — part 2

## ============================================================

class NodeType(Enum):
\# Base logical structure
ATOM = auto()
NOT = auto()
AND = auto()
OR = auto()
IMPLIES = auto()
BOTTOM = auto() # ⊥

```
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
```

@dataclass
class Formula:
"""Tree-structured formula node."""
node_type: NodeType
children: List["Formula"] = field(default_factory=list)
atom: Optional\[Tuple\[str, Tuple[Any, ...]\]\] = None # (predicate, args)

```
def __repr__(self) -> str:
    t = self.node_type
    if t == NodeType.ATOM:
        pred, args = self.atom or ("?", ())
        args_str = ", ".join(repr(a) for a in
```

______________________________________________________________________

- [[07_SKILLS/07_SKILLS_MOC|07_SKILLS_MOC]]
  **MOC:** references_MOC

______________________________________________________________________

**Related:** [[00_ROOT/00_HOME|00_HOME]] · [[00_ROOT/AMOS_RSCF_NODES|AMOS_RSCF_NODES]] · [[01_CANON/01_CORE_LAWS/LAW_HIERARCHY|LAW_HIERARCHY]] · references_MOC · [[07_SKILLS/07_SKILLS_MOC|07_SKILLS_MOC]]

**MOC:** references_MOC

**Trang Framework:** [[11_KNOWLEDGE/TRANG_FRAMEWORK_RECURSIVE_ONTOLOGY_DYNAMICS|TRANG_FRAMEWORK_RECURSIVE_ONTOLOGY_DYNAMICS]]

______________________________________________________________________

RSCF-NODE
node_id: amos-causal-hierarchy-governor-vault-domain-knowledge
node_type: reference
path: 07_SKILLS/amos-causal-hierarchy-governor/references/vault_domain_knowledge.md
RSCF-RELATIONS:

- INDEXED_BY: [[00_ROOT/00_HOME|00_HOME]]
- INDEXED_BY: [[00_ROOT/AMOS_RSCF_NODES|AMOS_RSCF_NODES]]
- CHILD_OF: references_MOC
