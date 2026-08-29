---
title: Vault Domain Knowledge — Amos Formally Verified Migration Rscf
type: reference
source: 07_SKILLS/amos-formally-verified-migration-rscf/references
tags:
- reference
- amos-formally-verified-migration-rscf
- canon/skill
- skill
- equation-firewall
- 2026-08-22-trang-phi-framework
- 2026-08-22-devin-memory-update
- 00-home
- 2026-08-22-executable-brain-model-lineage
- amos-rscf-nodes
- law-hierarchy
- references-moc
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
> Extracted from skill: `amos-formally-verified-migration-rscf`

## Vault-Sourced Content

### Source 1: AMOS 7PT Canon Migration Engine

> Path: `engine/A/AMOS 7PT Canon Migration Engine.md` | Size: 23434 chars | Match score: 10 | content_hash: d98204ead70ee82a

"""
AMOS 7PT Canon Migration Engine
================================

Purpose
-------
Deterministically repair the seven 7PT canon notes while preserving existing
part-specific analysis and enforcing the canonical seven-question structure.

Transformation classes
----------------------
1. FLOW + ENFORCEMENT
   Ensure literal links exist for:
   - 2026-08-22 7-Part Universe Canon.md
   - 7PT_Complete_Canon_Audit_Reaudit.md

2. CONSTRAINT + STRUCTURE + TIME + ADAPTATION + TERMINATION
   Replace the legacy five-question "Canonical test" with the canonical
   seven-question test.

3. Preserve the legacy five-question material as:
       ## <Part>-specific analysis

4. Make the transformation deterministic and idempotent:
       patch(patch(x)) == patch(x)

AMOS status
-----------
MODEL / deterministic migration utility.

This script edits canon artifacts. It does NOT by itself prove that the
resulting content is canonical, empirically valid, or admitted into the
active AMOS runtime.

Authority boundary
------------------
Filesystem mutation is an execution effect. In a governed AMOS deployment,
the patch result should be treated as a candidate artifact until validation,
provenance checks, authority checks, and commit admission succeed.
"""

from __future__ import annotations

import re
from dataclasses import dataclass
from pathlib import Path
from typing import Final


# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------

VAULT: Final = Path(
    "/Users/mac/Downloads/stitch_project_cosmo/_00_Cosmo brain/md"
)

HOME_FILENAME: Final = "2026-08-22 7-Part Universe Canon.md"
REAUDIT_FILENAME: Final = "7PT_Complete_Canon_Audit_Reaudit.md"

PARTS: Final = (
    "CONSTRAINT",
    "FLOW",
    "STRUCTURE",
    "ENFORCEMENT",
    "TIME",
    "ADAPTATION",
    "TERMINATION",
)

PART_DISPLAY: Final = {
    "CONSTRAINT": "Constraint",
    "FLOW": "Flow",
    "STRUCTURE": "Structure",
    "ENFORCEMENT": "Enforcement",
    "TIME": "Time",
    "ADAPTATION": "Adaptation",
    "TERMINATION": "Termination",
}

CANONICAL_QUESTIONS: Final = (
    "Where are the constraints?",
    "What is the flow?",
    "What structure stabilizes it?",
    "How is it enforced?",
    "How does time stress it?",
    "How does it adapt without drift?",
    "What are its termination conditions?",
)

PART_OWNED_QUESTION: Final = {
    "CONSTRAINT": 0,
    "FLOW": 1,
    "STRUCTURE": 2,
    "ENFORCEMENT": 3,
    "TIME": 4,
    "ADAPTATION": 5,
    "TERMINATION": 6,
}

# Critical inverse mapping.
# The original implementation did not do this correctly.
QUESTION_OWNER: Final = {
    question_index: part
    for part, question_index in PART_OWNED_QUESTION.items()
}


# ---------------------------------------------------------------------------
# Typed result state
# ---------------------------------------------------------------------------

@dataclass(frozen=True)
class PatchR

---

### Source 2: Brain Inventory — Verified (2026-08-22, live state)

> Path: `dated/2026-08-22/2026-08-22 Brain Inventory.md` | Size: 2106 chars | Match score: 7 | content_hash: e47fc055996aab7d

# Brain Inventory — Verified (2026-08-22, live state)

> Durable map of what is in the Cosmo Brain. Counts verified by direct filesystem scan; the vault is co-edited by parallel Devin/Antigravity agents so numbers drift upward between scans.

## Corpus (verified this scan)
- **Skills**: 803 `.devin/skills/` (0 empty dirs — every skill has SKILL.md)
- **Agents**: 61 `*.md`
- **Workflows**: 48 `*.md`
- **Bridge notes**: 54 `_00_Cosmo brain/md/bridges/`
- **Kernel JSON specs**: 1,471 under `designs/_00_Cosmo brain/Kernels/` (Logic / Biology_Cognition / Governance_Risk / Tech / etc.)
- **Engine skills**: 216 (name contains "engine")
- **Kernel skills**: 146 (name contains "kernel")

## Top skill clusters (prefix)
tech 30 · training 23 · vn 23 · absolute 20 · governance 13 · sector 13 · cognitive 12 · os 11 · universe 11 · super 10 · unified 10 · risk 9

## Notable implemented modules (beyond reference specs)
- `cosmo-brain/executable_brain_model.py` — v22 executable brain (8 v1.0 layers + integration gates)
- `cosmo-brain/trang_agent/` — VERIFIED Trang ∅ Framework agent (self-tests PASS; deterministic; converges λ→0.2)

## Integrity notes
- Obsidian resolves `link` by FILENAME anywhere in vault (bridges/ make MOC links resolve).
- Engine-layer skills (19 MOC-linked) are mostly reference-only; only CodingOmegaEngineLayer has a real brain class.
- Kernel JSON specs are source blueprints; the 146 kernel *skills* are their wrappers.
- Thresholds in Trang ∅ Framework are AMOS_MODEL/UNVERIFIED (per EQUATION_FIREWALL.md), not universal.

## Links
- 2026_08_22_TRANG_PHI_FRAMEWORK
- 2026_08_22_EXECUTABLE_BRAIN_MODEL_LINEAGE
- 2026_08_22_DEVIN_MEMORY_UPDATE

---

### Source 3: RSCF Structural Tag Migration

> Path: `rscf/RSCF Structural Tag Migration.md` | Size: 22332 chars | Match score: 5 | content_hash: 863e096c9f55eae8

# RSCF Structural Tag Migration

## Overview


The migration operates on a bounded registry of Markdown files and transforms:

```text
legacy canon-group taxonomy
        ↓
RSCF structural-axis taxonomy
```

The source implementation defines migration mappings for AMOS, Cosmo Brain, formal-system, memory, canon, topology, state, compression, repair, mutation, boundary, cross-scale, entropy, and evidence-oriented notes.

The architectural purpose is:

[
\boxed{
LegacyMetadata
\rightarrow
TypedRSCFMetadata
}
]

while preserving document content outside the targeted metadata field.

---

# 1. Migration Objective

The migration replaces legacy tag structures such as:

```yaml
tags: [canon-group/..., ..., topic/...]
```

with structural tags such as:

```yaml
tags:
  - rscf/M-memory
  - rscf/S-state
  - rscf/T-topology
  - rscf/type-model
```

The migration is therefore not merely a tag rename.

It changes the metadata ontology from:

```text
broad canon-group classification
```

to:

```text
typed RSCF structural coordinates
```

---

# 2. Core Transformation

For each registered file:

[
F_i=
(
Path_i,
Pattern_i,
Replacement_i
)
]

the migration performs:

[
Content'_i
==========

Replace(
Content_i,
Pattern_i,
Replacement_i
)
]

subject to the invariant:

[
Body(Content'_i)
================

Body(Content_i)
]

except for explicitly targeted metadata cleanup.

---

# 3. Migration Registry

The migration registry is explicit rather than dynamically inferred.

Each record defines:

```text
filename
legacy tag pattern
canonical replacement tags
```

Conceptually:

```text
MIGRATIONS
   │
   ├── File A
   │     ├── match pattern
   │     └── target tags
   │
   ├── File B
   │     ├── match pattern
   │     └── target tags
   │
   └── ...
```

This preserves deterministic behavior.

---

# 4. RSCF Structural Axes

The target taxonomy includes multiple RSCF structural dimensions.

## Distinction

```text
rscf/D-distinction
```

Used when a note primarily establishes:

```text
identity
classification
difference
inventory boundaries
canonical separation
```

---

# 5. Constraint

```text
rscf/C-constraint
```

Used for:

```text
hard limits
invariants
canon constraints
structural admissibility
```

---

# 6. Relation

```text
rscf/G-relation
```

Used for:

```text
coupling
interconnection
dependency
cross-component relation
```

---

# 7. State

```text
rscf/S-state
```

Used for:

```text
runtime condition
formal state
field state
system state
dynamic configuration
```

---

# 8. Topology

```text
rscf/T-topology
```

Used for:

```text
architecture
graph structure
geometry
connectivity
spatial organization
```

---

# 9. Memory

```text
rscf/M-memory
```

Used for:

```text
persistent knowledge
historical state
lineage
memory architecture
vault persistence
```

---

# 10. Compression

```text
rscf/K-compression
```

Used for:

```text
summarization
representation reduction
bridge compression
structural abstraction
```

---

# 11. Repair

```text
rscf/P-

---
**MOC:**
```
---

**Related:** [[00_HOME]] · [[AMOS_RSCF_NODES]] · [[LAW_HIERARCHY]] · references_MOC · [[07_SKILLS_MOC]]

**MOC:** references_MOC

**Trang Framework:** [[TRANG_FRAMEWORK_RECURSIVE_ONTOLOGY_DYNAMICS]]

---
RSCF-NODE
node_id: amos-formally-verified-migration-rscf-vault-domain-knowledge
node_type: reference
path: 07_SKILLS/amos-formally-verified-migration-rscf/references/vault_domain_knowledge.md
RSCF-RELATIONS:
- INDEXED_BY: [[00_HOME]]
- INDEXED_BY: [[AMOS_RSCF_NODES]]
- CHILD_OF: references_MOC
