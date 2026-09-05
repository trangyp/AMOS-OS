---
canon-group: meta
canon-type: framework
rscf-state: source-claim
rscf-claim: verified
rscf-provenance: AMOS_corpus
conclusion_class: AMOS_MODEL
epistemic_class: SOURCE_CLAIM
topic: Competing Definition Registry
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

# Competing Definition Registry

## 0. Status

`COMPETING_DEFINITION_REGISTRY.md` defines the proposed AMOS OS **Competing Definition** registry.

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

The Competing Definition Registry records cases where multiple definitions exist for the same AMOS concept, tracking the competing definitions and their resolution status.

______________________________________________________________________

## 2. Formal Definition

### 2.1 Competing Definition Entry

$$\text{Competing}(c) = (c, \text{definition}_1, \text{definition}_2, \ldots, \text{resolution\_status})$$

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
- Provenance recording for the resolution decision

______________________________________________________________________

## 3. Application

This registry is used by:
- [[02_KERNEL/05_MEMORY/K_MEMORY_RETRIEVAL|K_MEMORY_RETRIEVAL]]]] — for supersession-aware retrieval
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

node_id: amos_01_canon_08_supersession_competing_definition_registry

node_type: REGISTRY

path: 01_CANON/08_SUPERSESSION/COMPETING_DEFINITION_REGISTRY.md

claim_class: AMOS_MODEL

rscf_state: DERIVED

canonical_status: CONDITIONAL

RSCF-RELATIONS:

- INDEXED_BY: [[00_ROOT/00_HOME|00_HOME]]

- INDEXED_BY: [[00_ROOT/AMOS_RSCF_NODES|AMOS_RSCF_NODES]]

- GOVERNED_BY: [[01_CANON/01_CORE_LAWS/LAW_HIERARCHY|LAW_HIERARCHY]]

______________________________________________________________________

**MOC:** [[01_CANON/08_SUPERSESSION/08_SUPERSESSION_MOC|08_SUPERSESSION_MOC]]
