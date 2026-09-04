#!/usr/bin/env python3
"""Expand 01_CANON/08_SUPERSESSION placeholder files with substantive content."""

import os
from pathlib import Path

DIR = Path("/Users/mac/Documents/AMOS_OS/01_CANON/08_SUPERSESSION")

SUPERSESSION_FILES = {
    "AMOS_CORE_VERSION_LINEAGE.md": {
        "title": "AMOS Core Version Lineage",
        "id": "amos_core_version_lineage",
        "purpose": "The AMOS Core Version Lineage registry records the complete version history of AMOS Core, from v3.0 through v4.4, preserving the predecessor/successor chain, changesets, and promotion records.",
        "content": """### 2.1 Version Chain

```text
v3.0 → v3.1 → v3.2 → v4.0 → v4.1 → v4.2 → v4.3 → v4.4 (current authoritative)
```

### 2.2 Version Record

Each version record contains:
- `version`: semantic version
- `predecessor`: previous version
- `successor`: next version (or null if current)
- `changeset`: summary of changes
- `promotion_authority`: who authorized the promotion
- `promotion_date`: when promoted
- `validation_receipts`: references to validation evidence
- `status`: ACTIVE, SUPERSEDED, or DEPRECATED

### 2.3 Authoritative Version

$$\\text{Authoritative}(v) \\iff v = 4.4 \\wedge \\text{PromotionRecord}(v) \\text{ is valid}$$

### 2.4 Non-Promotion Rule

Versions v4.5-v4.17 are historical consolidation labels, NOT promoted canonical successors. A version is canonical only if it has:
- Explicit predecessor/successor chain
- Source version and hash
- Changeset documentation
- Validation/regression evidence
- Authority/promotion record
- Supersession lineage""",
    },
    "AMOS_FRAMEWORK_SUPERSESSION.md": {
        "title": "AMOS Framework Supersession",
        "id": "amos_framework_supersession",
        "purpose": "The AMOS Framework Supersession registry records supersessions of AMOS frameworks, tracking how frameworks evolve and replace each other over time.",
        "content": """### 2.1 Framework Supersession Entry

$$\\text{Supersede}(f_1, f_2) = (f_1, f_2, \\text{timestamp}, \\text{authority}, \\text{reason}, \\text{changeset})$$

### 2.2 Supersession Chain

$$\\text{Chain}(f) = [f, \\text{superseded\\_by}(f), \\ldots, \\text{current}(f)]$$

### 2.3 No Silent Replacement

$$\\text{Replace}(f_1, f_2) \\implies \\text{Record}(f_1, f_2, \\text{timestamp}, \\text{authority}, \\text{reason})$$

Framework supersession must be explicitly recorded with authority and reason. The superseded framework is archived, not deleted.""",
    },
    "COMPETING_DEFINITION_REGISTRY.md": {
        "title": "Competing Definition Registry",
        "id": "competing_definition_registry",
        "purpose": "The Competing Definition Registry records cases where multiple definitions exist for the same AMOS concept, tracking the competing definitions and their resolution status.",
        "content": """### 2.1 Competing Definition Entry

$$\\text{Competing}(c) = (c, \\text{definition}_1, \\text{definition}_2, \\ldots, \\text{resolution\\_status})$$

### 2.2 Resolution Status

```text
UNRESOLVED:    no canonical definition chosen yet
RESOLVED:      one definition promoted to canonical, others archived
PARTIAL:       some aspects resolved, others remain competing
DEPRECATED:    all competing definitions deprecated
```

### 2.3 No Silent Resolution

Competing definitions must not be silently resolved. Resolution requires:
- Explicit authority
- Evidence supporting the chosen definition
- Archival of non-chosen definitions
- Provenance recording for the resolution decision""",
    },
    "HERITAGE_SUPERSESSION.md": {
        "title": "Heritage Supersession",
        "id": "heritage_supersession",
        "purpose": "The Heritage Supersession registry records supersessions of heritage decision intelligence artifacts, preserving the evolution of ancestral wisdom frameworks.",
        "content": """### 2.1 Heritage Supersession Entry

$$\\text{Supersede}(h_1, h_2) = (h_1, h_2, \\text{timestamp}, \\text{authority}, \\text{tradition}, \\text{reason})$$

### 2.2 Preservation Rule

Heritage supersession preserves lineage, not erases it. Superseded heritage artifacts are archived with full provenance.

### 2.3 Cross-Tradition Validation

Heritage supersession across traditions requires 2+ independent tradition sources (Rule of 2) before promotion.""",
    },
    "TRANG_FRAMEWORK_SUPERSESSION.md": {
        "title": "Trang Framework Supersession",
        "id": "trang_framework_supersession",
        "purpose": "The Trang Framework Supersession registry records supersessions within the Trang Framework, tracking how the recursive ontology dynamics evolve.",
        "content": """### 2.1 Trang Supersession Entry

$$\\text{Supersede}(t_1, t_2) = (t_1, t_2, \\text{timestamp}, \\text{authority}, \\text{cascade\\_level}, \\text{reason})$$

### 2.2 Cascade-Level Preservation

Trang Framework supersessions preserve the cascade-level structure. A supersession at level $L_i$ does not affect levels $L_{i-1}$ or $L_{i+1}$.

### 2.3 Origin Architect Authority

All Trang Framework supersessions require origin architect (Trang Phan) authority or explicit delegated authority.""",
    },
    "UBI_SUPERSESSION.md": {
        "title": "UBI Supersession",
        "id": "ubi_supersession",
        "purpose": "The UBI Supersession registry records supersessions within the Unified Biological Intelligence framework, tracking how the 4-domain biological model evolves.",
        "content": """### 2.1 UBI Supersession Entry

$$\\text{Supersede}(u_1, u_2) = (u_1, u_2, \\text{timestamp}, \\text{authority}, \\text{domain}, \\text{reason})$$

### 2.2 Domain Independence

UBI supersessions in one domain (NBI, NEI, SI, BEI) do not automatically supersede other domains. Each domain's supersession is independent.

### 2.3 Non-Compensatory Preservation

The non-compensatory rule (min(NBI, NEI, SI, BEI)) is preserved across supersessions. No supersession may weaken the non-compensatory property.""",
    },
    "UNIVERSE_CANON_SUPERSESSION.md": {
        "title": "Universe Canon Supersession",
        "id": "universe_canon_supersession",
        "purpose": "The Universe Canon Supersession registry records supersessions within the 7-Part Universe Canon, tracking how universe-level structural reasoning evolves.",
        "content": """### 2.1 Universe Canon Supersession Entry

$$\\text{Supersede}(u_1, u_2) = (u_1, u_2, \\text{timestamp}, \\text{authority}, \\text{part}, \\text{reason})$$

### 2.2 Part Independence

Universe Canon supersessions in one part (P1-P7) do not automatically supersede other parts. Each part's supersession is independent.

### 2.3 Viability Preservation

The universe viability invariant ($\\prod_{i=1}^{7} \\text{PartHealth}(P_i)$) is preserved across supersessions. No supersession may reduce overall universe viability.""",
    },
}

TEMPLATE = '''---
title: {title}
type: registry
source: 01_CANON/08_SUPERSESSION
artifact: {filename}
artifact_id: amos_01_canon_08_supersession_{id}
origin_architect: Trang Phan
steward: Trang Phan
system: AMOS OS
plane: 01_CANON
segment: 01_CANON/08_SUPERSESSION
artifact_kind: REGISTRY
path: 01_CANON/08_SUPERSESSION/{filename}
tags:
  - amos-os
  - canon
  - supersession
  - rscf
  - placeholder_expanded
  - law-hierarchy
version: 1.0.0
updated: '2026-09-04'
status: SUBSTANTIVE_SPECIFICATION
epistemic_class: AMOS_MODEL
canonical_status: CONDITIONAL
implementation_status: NOT_ESTABLISHED
validation_status: NOT_ESTABLISHED
executable_binding: NOT_ESTABLISHED
ingestion_action: ADD_ONLY
rscf:
  state: DERIVED
  claim_class: DERIVED
  provenance: AMOS_corpus
  scope: AMOS_general
  regime: canon
  confidence_ceiling: source_supported
  provenance_independence: NOT_ESTABLISHED
---

# {title}

## 0. Status

`{filename}` defines the proposed AMOS OS **{title_short}** registry.

This artifact replaces a structural placeholder with substantive content.

```text
PLACEHOLDER != IMPLEMENTED
ADDRESSABLE != VALIDATED
DOCUMENTED != ENFORCED
MODEL != OBSERVATION
SOURCE_CLAIM != VERIFIED
CANON_CANDIDATE != CANONICAL
CAPABILITY != AUTHORITY
UNKNOWN/GAP != PASS
```

Origin architect / steward: **Trang Phan**

______________________________________________________________________

## 1. Purpose

{purpose}

______________________________________________________________________

## 2. Formal Definition

{content}

______________________________________________________________________

## 3. Application

This registry is used by:
- [[02_KERNEL/K_MEMORY_RETRIEVAL|K_MEMORY_RETRIEVAL]] — for supersession-aware retrieval
- [[01_CANON/07_PROVENANCE/CANON_PROVENANCE|CANON_PROVENANCE]] — for provenance chain validation
- [[01_CANON/08_SUPERSESSION/ACTIVE_VS_LEGACY_CANON|ACTIVE_VS_LEGACY_CANON]] — for active/legacy classification
- [[01_CANON/01_CORE_LAWS/LAW_HIERARCHY|LAW_HIERARCHY]] — for law hierarchy enforcement

______________________________________________________________________

## 4. Gaps

- Executable binding NOT_ESTABLISHED
- Canonical status CONDITIONAL
- Automated supersession validation NOT_ESTABLISHED

______________________________________________________________________

## 5. Ingestion Rule

```yaml
AMOS_CANON_INGESTION_RULE:
  existing_file:
    preserve: true
    overwrite: false
  uncertainty:
    action:
      - MARK_GAP_OR_COMPETING
      - NEVER_INVENT_CANON
```

______________________________________________________________________

[[00_ROOT/00_ROOT_MOC|00_ROOT_MOC]] · [[00_ROOT/AMOS MOC|AMOS MOC]]

______________________________________________________________________

**Related:** [[00_ROOT/00_HOME|00_HOME]] · [[00_ROOT/AMOS_RSCF_NODES|AMOS_RSCF_NODES]]

______________________________________________________________________

RSCF-NODE

node_id: amos_01_canon_08_supersession_{id}

node_type: REGISTRY

path: 01_CANON/08_SUPERSESSION/{filename}

claim_class: AMOS_MODEL

rscf_state: DERIVED

canonical_status: CONDITIONAL

RSCF-RELATIONS:

- INDEXED_BY: [[00_ROOT/00_HOME|00_HOME]]

- INDEXED_BY: [[00_ROOT/AMOS_RSCF_NODES|AMOS_RSCF_NODES]]

- GOVERNED_BY: [[01_CANON/01_CORE_LAWS/LAW_HIERARCHY|LAW_HIERARCHY]]

______________________________________________________________________

**MOC:** [[01_CANON/08_SUPERSESSION/08_SUPERSESSION_MOC|08_SUPERSESSION_MOC]]
'''


def expand_file(filepath, content_def):
    filename = os.path.basename(filepath)
    title = content_def["title"]
    title_short = title.replace(" Supersession", "").replace(" Lineage", "").replace(" Registry", "")

    content = TEMPLATE.format(
        title=title,
        title_short=title_short,
        filename=filename,
        id=content_def["id"],
        purpose=content_def["purpose"],
        content=content_def["content"],
    )

    with open(filepath, "w") as f:
        f.write(content)
    return len(content)


def main():
    expanded = 0
    for filename, content_def in SUPERSESSION_FILES.items():
        filepath = DIR / filename
        if filepath.exists():
            size = expand_file(str(filepath), content_def)
            print(f"Expanded {filename}: {size} bytes")
            expanded += 1
        else:
            print(f"WARNING: {filename} not found")
    print(f"\nTotal expanded: {expanded}")


if __name__ == "__main__":
    main()
