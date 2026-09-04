---
canon-group: meta
canon-type: framework
rscf-state: source-claim
rscf-claim: verified
rscf-provenance: AMOS_corpus
conclusion_class: AMOS_MODEL
epistemic_class: SOURCE_CLAIM
topic: Active Vs Legacy Canon
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

# Active vs Legacy Canon

## 0. Status

`ACTIVE_VS_LEGACY_CANON.md` defines the proposed AMOS OS **Active vs Legacy Canon** registry.

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

The Active vs Legacy Canon registry distinguishes between currently active canonical artifacts and legacy (superseded but preserved) artifacts.

______________________________________________________________________

## 2. Formal Definition

### 2.1 Active vs Legacy

$$\text{Active}(a) \iff \text{status}(a) \in \{\text{ACTIVE}, \text{SUBSTANTIVE\_SPECIFICATION}\}$$
$$\text{Legacy}(a) \iff \text{status}(a) = \text{SUPERSEDED}$$

### 2.2 Supersession Rule

When artifact $a_1$ is superseded by $a_2$:
- $a_1$ status → SUPERSEDED
- $a_2$ status → ACTIVE
- $a_1$ is preserved (archived, not deleted)
- Lineage link: $a_1 \to a_2$

### 2.3 No Silent Replacement

$$\text{Replace}(a_1, a_2) \implies \text{Record}(a_1, a_2, \text{timestamp}, \text{authority}, \text{reason})$$

Supersession must be explicitly recorded with authority and reason.

______________________________________________________________________

## 3. Application

This registry is used by:
- [[02_KERNEL/K_MEMORY_RETRIEVAL|K_MEMORY_RETRIEVAL]] — for provenance-aware retrieval
- [[02_KERNEL/K_MEMORY_ADMISSION|K_MEMORY_ADMISSION]] — for provenance validation at admission
- [[17_OBSERVABILITY/PROVENANCE_TRUST_FIREWALL|PROVENANCE_TRUST_FIREWALL]] — for trust boundary enforcement
- [[01_CANON/01_CORE_LAWS/L2_PROVENANCE|L2_PROVENANCE]] — for provenance law enforcement

______________________________________________________________________

## 4. Gaps

- Executable binding NOT_ESTABLISHED
- Canonical status CONDITIONAL
- Automated validation NOT_ESTABLISHED

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

node_id: amos_01_canon_08_supersession_active_vs_legacy_canon

node_type: REGISTRY

path: 01_CANON/08_SUPERSESSION/ACTIVE_VS_LEGACY_CANON.md

claim_class: AMOS_MODEL

rscf_state: DERIVED

canonical_status: CONDITIONAL

RSCF-RELATIONS:

- INDEXED_BY: [[00_ROOT/00_HOME|00_HOME]]

- INDEXED_BY: [[00_ROOT/AMOS_RSCF_NODES|AMOS_RSCF_NODES]]

- GOVERNED_BY: [[01_CANON/01_CORE_LAWS/LAW_HIERARCHY|LAW_HIERARCHY]]

______________________________________________________________________

**MOC:** [[01_CANON/08_SUPERSESSION/08_SUPERSESSION_MOC.md|08_SUPERSESSION_MOC.md]]
