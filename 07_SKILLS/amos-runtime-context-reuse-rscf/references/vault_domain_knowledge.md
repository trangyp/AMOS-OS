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
> Extracted from skill: `amos-runtime-context-reuse-rscf`

## Vault-Sourced Content

### Source 1: AMOS Core Runtime Modules

> Path: `dated/2026-08-22/2026-08-22 AMOS Core Runtime Modules.md` | Size: 3079 chars | Match score: 12

## AMOS Core Runtime Modules

> Epistic class: OBSERVATION
> Conclusion label: `VERIFIED` — 109 tests pass across 6 core module families.
> Governing law: `integrity > completeness > fluency > speed > token savings`.

## Overview

The AMOS OS Kernel has 6 core module families that implement the cognitive
runtime. These are the foundational layers beneath the governance modules.

## Module Families

### 1. Proof (`amos/proof/`)

- **ProofChecker**: 4 gates — scope/regime, confidence ceiling, causal evidence, falsifier
- **HypothesisField**: unresolved competing claims, dominance, discrimination
- **RSCF**: compile_claim, confidence_ceiling, selective_invalidate (cascade)
- **Tests**: 22 (test_proof_modules.py)

### 2. Memory (`amos/memory/`)

- **ContextBudgetGovernor**: utility-weighted context selection (6 factors)
- **MemoryImmuneSystem**: REVOKED/PROVENANCE_CYCLE/PATHOLOGICAL detection
- **MemoryManager**: tiered admission (hot/warm/cold) with provenance
- **OrientationCache**: stale-aware key-value cache
- **Tests**: 21 (test_memory_modules.py)

### 3. Graph (`amos/graph/`)

- **CausalGraph**: 7 causal levels (descriptive→intervention_effect)
- **DependencyGraph**: load-bearing descendant traversal, independence
- **ProvenanceGraph**: roots, components, sybil score
- **Tests**: 28 (test_graph_modules.py)

### 4. Runtime (`amos/runtime/`)

- **Planner**: closure, topo, build — skill dependency planning
- **Router**: tensor, complexity (C0-C4), budget
- **Selector**: complexity-aware skill selection
- **SelfAudit**: ProofChecker on all claims
- **Finalizer**: gate summary + competing check
- **Scheduler**: replay-ledger-integrated execution
- **Tests**: 17 (test_runtime_modules.py)

### 5. ABI (`amos/abi/`)

- **ModelRegistry**: discover model manifests from JSON
- **SkillRegistry**: discover skill manifests from JSON
- **ToolRegistry**: discover tool manifests from JSON
- **Tests**: 11 (test_abi_registries.py)

### 6. Replay (`amos/replay/`)

- **EventBus**: publish/subscribe with store persistence
- **Ledger**: SHA-256 hashed replay entries
- **Tests**: ~10 (test_replay_modules.py)

## Test Results

| Test File               |    Tests |
| ----------------------- | -------: |
| test_proof_modules.py   |       22 |
| test_memory_modules.py  |       21 |
| test_graph_modules.py   |       28 |
| test_runtime_modules.py |       17 |
| test_abi_registries.py  |       11 |
| test_replay_modules.py  |      ~10 |
| **Total**               | **~109** |

## Full Suite

- Python: 1934 tests pass (all modules with full test coverage)
- TypeScript: 1191 tests pass
- **Total: 3701 verified tests** across all runtimes

## Links

- [[11_KNOWLEDGE/COSMO_BRAIN_MOC|COSMO_BRAIN_MOC]]
- 2026_08_22_AMOS_ALL_249_GAPS_CLOSED
- 2026_08_22_TYPESCRIPT_DATA_QUALITY_GOVERNANCE

______________________________________________________________________

### Source 2: AMOS_CORE v3.5 — Epistemic Regime Lineage Runtime

> Path: `amos-general/A/CORE/AMOS_CORE v3.5 — Epistemic Regime Lineage Runtime.md` | Size: 88716 chars | Match score: 10

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

### Source 3: AMOS_CORE v3.4.1 — Distributed Causal Evolution Runtime

> Path: `amos-general/A/CORE/AMOS_CORE v3.4.1 — Distributed Causal Evolution Runtime.md` | Size: 76005 chars | Match score: 10

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

## **MOC:** references_MOC

**Related:** [[00_ROOT/00_HOME|00_HOME]] · [[00_ROOT/AMOS_RSCF_NODES|AMOS_RSCF_NODES]] · [[01_CANON/01_CORE_LAWS/LAW_HIERARCHY|LAW_HIERARCHY]] · references_MOC · [[07_SKILLS/07_SKILLS_MOC|07_SKILLS_MOC]]

**MOC:** references_MOC

**Trang Framework:** [[11_KNOWLEDGE/TRANG_FRAMEWORK_RECURSIVE_ONTOLOGY_DYNAMICS|TRANG_FRAMEWORK_RECURSIVE_ONTOLOGY_DYNAMICS]]

______________________________________________________________________

RSCF-NODE
node_id: amos-runtime-context-reuse-rscf-vault-domain-knowledge
node_type: reference
path: 07_SKILLS/amos-runtime-context-reuse-rscf/references/vault_domain_knowledge.md
RSCF-RELATIONS:

- INDEXED_BY: [[00_ROOT/00_HOME|00_HOME]]
- INDEXED_BY: [[00_ROOT/AMOS_RSCF_NODES|AMOS_RSCF_NODES]]
- CHILD_OF: references_MOC
