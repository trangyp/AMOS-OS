---
origin_architect: Trang Phan
steward: Trang Phan
amos_core_target: v4.4
title: Vault Domain Knowledge — Amos Knowledge Harvest Runtime
type: reference
source: 07_SKILLS/amos-knowledge-harvest-runtime/references
tags:
  - reference
  - amos-knowledge-harvest-runtime
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
> Extracted from skill: `amos-knowledge-harvest-runtime`

## Vault-Sourced Content

### Source 1: Knowledge Harvest Runtime

> Path: `misc/K/KNOWLEDGE_HARVEST.md` | Size: 1072 chars | Match score: 19 | content_hash: fbdf562d4113ee62

## Knowledge Harvest Runtime

## Structural equation

`PermanentKnowledge = Claim + Scope + Evidence + Provenance + Constraint + FailureMode + Validity + Lineage`

## Pipeline

1. acquire/fingerprint
1. deterministic structure extraction
1. small falsifiable semantic claims
1. provenance/evidence/regime/governance validation
1. structured storage
1. retention-class-controlled cleanup
1. compact retrieval compilation

## Retrieval compiler

user_problem → AMOS_structural_decomposition → knowledge_registry_query → candidate_RSCF_retrieval → scope_filter → evidence_filter → freshness_filter → governance_filter → conflict_field_resolution → compact_context_compile → LLM_or_agent

Anti-pattern:
`vector_search -> dump_many_raw_repository_chunks -> LLM`

______________________________________________________________________

______________________________________________________________________

### Source 2: AMOS_CORE v3.5 — Epistemic Regime Lineage Runtime

> Path: `amos-general/A/CORE/AMOS_CORE v3.5 — Epistemic Regime Lineage Runtime.md` | Size: 88716 chars | Match score: 12 | content_hash: b4f8a0ccac78d131

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
## Meta-patterns
PARADOX = auto()  # Π(X)
CONV = auto()     # Λ(X)
DIVG = auto()     # Δ(X)

## Logic modes
PLOGIC = auto()   # PositiveLogic
NLOGIC = auto()   # NegativeLogic
ZLOGIC = auto()   # ZeroLogic
DLOGIC = auto()   # DualLogic
MLOGIC = auto()   # MultiLogic
METAL = auto()    # MetaLogic

## Meta-logic modes
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

### Source 3: AMOS_CORE v3.4.1 — Distributed Causal Evolution Runtime

> Path: `amos-general/A/CORE/AMOS_CORE v3.4.1 — Distributed Causal Evolution Runtime.md` | Size: 76005 chars | Match score: 12 | content_hash: c7e85dd6d3746e50

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
## Meta-patterns
PARADOX = auto()  # Π(X)
CONV = auto()     # Λ(X)
DIVG = auto()     # Δ(X)

## Logic modes
PLOGIC = auto()   # PositiveLogic
NLOGIC = auto()   # NegativeLogic
ZLOGIC = auto()   # ZeroLogic
DLOGIC = auto()   # DualLogic
MLOGIC = auto()   # MultiLogic
METAL = auto()    # MetaLogic

## Meta-logic modes
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

**MOC:** references_MOC

## Related

- [[07_SKILLS/07_SKILLS_MOC|07_SKILLS_MOC]]

______________________________________________________________________

**Related:** [[00_ROOT/00_HOME|00_HOME]] · [[00_ROOT/AMOS_RSCF_NODES|AMOS_RSCF_NODES]] · [[01_CANON/01_CORE_LAWS/LAW_HIERARCHY|LAW_HIERARCHY]] · references_MOC · [[07_SKILLS/07_SKILLS_MOC|07_SKILLS_MOC]]

**MOC:** references_MOC

**Trang Framework:** [[11_KNOWLEDGE/TRANG_FRAMEWORK_RECURSIVE_ONTOLOGY_DYNAMICS|TRANG_FRAMEWORK_RECURSIVE_ONTOLOGY_DYNAMICS]]

______________________________________________________________________

RSCF-NODE
node_id: amos-knowledge-harvest-runtime-vault-domain-knowledge
node_type: reference
path: 07_SKILLS/amos-knowledge-harvest-runtime/references/vault_domain_knowledge.md
RSCF-RELATIONS:

- INDEXED_BY: [[00_ROOT/00_HOME|00_HOME]]
- INDEXED_BY: [[00_ROOT/AMOS_RSCF_NODES|AMOS_RSCF_NODES]]
- CHILD_OF: references_MOC
