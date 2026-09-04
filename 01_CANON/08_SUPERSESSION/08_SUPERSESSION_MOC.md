---
title: 08 Supersession MOC
type: moc
source: 01_CANON/08_SUPERSESSION
tags:
  - 08-supersession
  - canon/universe
  - amos-core-version-lineage
  - amos-framework-supersession
  - heritage-supersession
  - supersession-log
  - trang-framework-supersession
  - ubi-supersession
  - universe-canon-supersession
moc: true
rscf:
  state: DERIVED
  claim_class: DERIVED
  provenance: AMOS_corpus
  scope: AMOS_general
---

# 08 Supersession — Map of Content

**Path:** `01_CANON/08_SUPERSESSION`
**Files:** 12 | **Subdirectories:** 1

## Purpose

This MOC indexes the supersession layer of the AMOS canon — the governed
record of which canonical definitions, frameworks, and lineage claims have
been replaced, deprecated, or merged into successor artifacts. Supersession
is the mechanism by which the vault distinguishes `LATEST` from
`AUTHORITATIVE` and `DOCUMENTED` from `IMPLEMENTED`. Without this layer the
vault would accumulate competing definitions with no resolution path,
violating the MECE separation between active and legacy canon.

## MECE Domain

**Canon dimension — Authority Precedence / Lineage Supersession.**

The MECE architecture separates functional ownership, physical storage,
authority precedence, runtime call order, and evidence/validation status.
This MOC owns the **authority-precedence** slice for the canon: it records
predecessor→successor chains, conflict registries, and deprecation logs so
that every canonical claim can be traced to its current authoritative
source or explicitly marked as superseded.

## Files

- [[01_CANON/08_SUPERSESSION/ACTIVE_VS_LEGACY_CANON|ACTIVE_VS_LEGACY_CANON]] — criteria distinguishing active canon from legacy canon
- [[01_CANON/08_SUPERSESSION/AMOS_CORE_VERSION_LINEAGE|AMOS_CORE_VERSION_LINEAGE]] — version chain for AMOS_CORE releases
- [[01_CANON/08_SUPERSESSION/AMOS_FRAMEWORK_SUPERSESSION|AMOS_FRAMEWORK_SUPERSESSION]] — supersession record for the AMOS framework
- [[01_CANON/08_SUPERSESSION/CANON_SUPERSESSION_CONTRACT|CANON_SUPERSESSION_CONTRACT]] — contract governing how canon items are superseded
- [[01_CANON/08_SUPERSESSION/COMPETING_DEFINITION_REGISTRY|COMPETING_DEFINITION_REGISTRY]] — registry of competing definitions awaiting resolution
- [[01_CANON/08_SUPERSESSION/CONFLICT_REGISTRY|CONFLICT_REGISTRY]] — log of detected conflicts between canonical claims
- [[01_CANON/08_SUPERSESSION/HERITAGE_SUPERSESSION|HERITAGE_SUPERSESSION]] — supersession record for heritage-lineage artifacts
- [[01_CANON/08_SUPERSESSION/SUPERSESSION_CANON_README|SUPERSESSION_CANON_README]] — README for the supersession canon subdomain
- [[01_CANON/08_SUPERSESSION/SUPERSESSION_LOG|SUPERSESSION_LOG]] — chronological log of all supersession events
- [[01_CANON/08_SUPERSESSION/TRANG_FRAMEWORK_SUPERSESSION|TRANG_FRAMEWORK_SUPERSESSION]] — supersession record for the Trang framework
- [[01_CANON/08_SUPERSESSION/UBI_SUPERSESSION|UBI_SUPERSESSION]] — supersession record for UBI framework artifacts
- [[01_CANON/08_SUPERSESSION/UNIVERSE_CANON_SUPERSESSION|UNIVERSE_CANON_SUPERSESSION]] — supersession record for universe-canon artifacts

## Subdirectories

- [[01_CANON/00_INDEX/00_INDEX_MOC|00_INDEX_MOC]] — 00_INDEX

## Supersession Protocol

- Supersession is the governed process by which a newer canonical version replaces an older one, requiring explicit predecessor/successor linkage, validation evidence, and authority records.
- No supersession may occur without a recorded [[01_CANON/08_SUPERSESSION/SUPERSESSION_LOG|SUPERSESSION_LOG]] entry containing the old version, new version, changeset, and validation status.
- Supersession is irreversible once committed — the superseded version is archived but never deleted, preserving full rollback capability.

## Version Lineage (v3.0 → v4.4)

- **v3.0:** Original canonical baseline establishing core laws, RSCF framework, and universe canon.
- **v3.x–v4.3:** Incremental supersessions adding cognition canon, infrastructure canon, and variable registry expansions — see [[01_CANON/08_SUPERSESSION/AMOS_CORE_VERSION_LINEAGE|AMOS_CORE_VERSION_LINEAGE]].
- **v4.4:** Current authoritative canonical version — all vault artifacts target v4.4 unless explicitly marked otherwise.
- Any `v4.5`–`v4.17` labels in historical records are consolidation labels, not promoted canonical successors, unless supported by full supersession evidence chain.

## Supersession Criteria

- **Validation Gate:** The successor must pass all validation stages defined in the active control-plane contract — see [[03_CONTROL_PLANE/03_CONTROL_PLANE_MOC|03_CONTROL_PLANE_MOC]].
- **Conflict Resolution:** Competing definitions must be resolved or explicitly registered before supersession — see [[01_CANON/08_SUPERSESSION/CONFLICT_REGISTRY|CONFLICT_REGISTRY]].
- **Provenance Chain:** The successor must carry a complete provenance chain from the predecessor, including authority witness and commit-time freshness.
- **Archive-First:** The predecessor is archived to [[24_ARCHIVE/24_ARCHIVE_MOC|24_ARCHIVE]] before the successor is activated.

## Archive-First Principle

- No canonical artifact is ever deleted — superseded versions are moved to archive with full metadata and remain queryable.
- The archive preserves the exact state of the superseded artifact, including its RSCF block, tags, and cross-references.
- Rollback to a superseded version requires a new supersession event, not a direct mutation of the archive.

## Relationships

- **Parent canon:** [[01_CANON/01_CANON_MOC|01_CANON_MOC]]
- **Canon contract:** [[01_CANON/08_SUPERSESSION/CANON_SUPERSESSION_CONTRACT|CANON_SUPERSESSION_CONTRACT]]
- **Version lineage:** [[01_CANON/08_SUPERSESSION/AMOS_CORE_VERSION_LINEAGE|AMOS_CORE_VERSION_LINEAGE]]
- **Conflict tracking:** [[01_CANON/08_SUPERSESSION/CONFLICT_REGISTRY|CONFLICT_REGISTRY]]
- **Control plane:** [[03_CONTROL_PLANE/03_CONTROL_PLANE_MOC|03_CONTROL_PLANE_MOC]]
- **Archive:** [[24_ARCHIVE/24_ARCHIVE_MOC|24_ARCHIVE]]
- **Root navigation:** [[00_ROOT/00_ROOT_MOC|00_ROOT_MOC]]

## Epistemic Boundary

Supersession records are **DERIVED** claims about canon lineage, not
empirical proof that a successor has been deployed or executed. A
supersession log entry establishes documentary precedence only.
`SUPERSEDED != REMOVED`; legacy artifacts remain in the vault for audit
and rollback. Post-v4.4 canonical labels require governed successor
evidence before promotion.

______________________________________________________________________

**Parent:** [[01_CANON/01_CANON_MOC|01_CANON_MOC]]
