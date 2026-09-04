#!/usr/bin/env python3
"""Expand 01_CANON/07_PROVENANCE and 08_SUPERSESSION placeholder files."""

import os
from pathlib import Path

CANON_DIR = Path("/Users/mac/Documents/AMOS_OS/01_CANON")

# Provenance file definitions
PROVENANCE_FILES = {
    "07_PROVENANCE/AMOS_CORE_LINEAGE_PROVENANCE.md": {
        "title": "AMOS Core Lineage Provenance",
        "id": "amos_core_lineage_provenance",
        "purpose": "The AMOS Core Lineage Provenance registry traces the lineage of AMOS Core versions from v3.0 through v4.4, recording the predecessor/successor chain, changesets, validation evidence, and promotion records for each version.",
        "content": """### 2.1 Lineage Chain

```text
v3.0 → v3.1 → v3.2 → v4.0 → v4.1 → v4.2 → v4.3 → v4.4 (current)
```

### 2.2 Version Record Fields

Each version record contains:
- `version`: semantic version identifier
- `predecessor`: previous version in the chain
- `changeset`: summary of changes from predecessor
- `validation_evidence`: references to validation receipts
- `promotion_record`: authority and date of promotion
- `supersession_status`: ACTIVE, SUPERSEDED, or DEPRECATED

### 2.3 Current Authoritative Version

$$\\text{Authoritative}(v) \\iff v = 4.4 \\wedge \\text{PromotionRecord}(v) \\text{ is valid}$$

### 2.4 Non-Promotion Rule

Any v4.5-v4.17 labels are historical consolidation labels, NOT promoted canonical successors, unless supported by explicit predecessor/successor chain, source version/hash, changeset, validation/regression evidence, authority/promotion record, and supersession lineage.""",
    },
    "07_PROVENANCE/CANON_HASH_REGISTRY.md": {
        "title": "Canon Hash Registry",
        "id": "canon_hash_registry",
        "purpose": "The Canon Hash Registry maintains cryptographic hashes of all canonical artifacts in the AMOS OS, enabling tamper detection and integrity verification.",
        "content": """### 2.1 Hash Entry

$$\\text{Entry}(a) = (\\text{artifact\\_id}, \\text{version}, \\text{hash}, \\text{timestamp}, \\text{signer})$$

### 2.2 Integrity Verification

$$\\text{Intact}(a) \\iff \\text{Hash}(\\text{Content}(a)) = \\text{RegisteredHash}(a)$$

### 2.3 Tamper Detection

$$\\neg\\text{Intact}(a) \\implies \\text{Flag}(a, \\text{TAMPERED}) \\wedge \\text{Quarantine}(a)$$

### 2.4 Hash Algorithm

All canon hashes use BLAKE3 (256-bit) for cryptographic binding.""",
    },
    "07_PROVENANCE/CANON_TO_SOURCE_MAP.md": {
        "title": "Canon to Source Map",
        "id": "canon_to_source_map",
        "purpose": "The Canon to Source Map maps each canonical artifact to its originating source(s), enabling provenance tracing from canon back to original material.",
        "content": """### 2.1 Mapping Entry

$$\\text{Map}(c) = (\\text{canon\\_id}, \\text{source\\_id}, \\text{source\\_type}, \\text{extraction\\_method})$$

### 2.2 Source Types

```text
NATIVE_CANON:     originated within AMOS corpus
EXTERNAL_RESEARCH: originated from external research (arxiv, papers)
HISTORICAL:       originated from historical/heritage sources
DERIVED:          derived from other canonical artifacts
```

### 2.3 Traceability

$$\\forall\\, c \\in \\text{Canon}, \\exists\\, s \\in \\text{Sources} : \\text{Map}(c, s)$$

Every canonical artifact must trace to at least one source.""",
    },
    "07_PROVENANCE/DERIVED_CANON_SOURCE_REGISTRY.md": {
        "title": "Derived Canon Source Registry",
        "id": "derived_canon_source_registry",
        "purpose": "The Derived Canon Source Registry records canonical artifacts that were derived from other canonical artifacts, preserving the derivation chain.",
        "content": """### 2.1 Derivation Record

$$\\text{Derived}(c) = (c, \\text{parent\\_canon}, \\text{derivation\\_method}, \\text{derivation\\_timestamp})$$

### 2.2 Derivation Chain

$$\\text{Chain}(c) = [c, \\text{parent}(c), \\text{parent}(\\text{parent}(c)), \\ldots, \\text{root}]$$

### 2.3 Derivation Integrity

$$\\text{Valid}(c) \\iff \\text{Chain}(c) \\text{ is complete} \\wedge \\text{root}(c) \\in \\text{NativeCanon}$$""",
    },
    "07_PROVENANCE/FILE_HASH_REGISTRY.md": {
        "title": "File Hash Registry",
        "id": "file_hash_registry",
        "purpose": "The File Hash Registry maintains cryptographic hashes of all files in the AMOS OS vault, enabling file integrity verification and change detection.",
        "content": """### 2.1 File Hash Entry

$$\\text{Entry}(f) = (\\text{file\\_path}, \\text{hash}, \\text{timestamp}, \\text{size})$$

### 2.2 Change Detection

$$\\text{Changed}(f) \\iff \\text{Hash}(f_{\\text{current}}) \\neq \\text{RegisteredHash}(f)$$

### 2.3 Hash Algorithm

BLAKE3 (256-bit) for all file hashes.""",
    },
    "07_PROVENANCE/FRAMEWORK_ANCESTRY_GRAPH.md": {
        "title": "Framework Ancestry Graph",
        "id": "framework_ancestry_graph",
        "purpose": "The Framework Ancestry Graph records the parent-child relationships between AMOS frameworks, showing how frameworks evolved from and depend on each other.",
        "content": """### 2.1 Graph Structure

$$G = (V, E) : V = \\text{Frameworks}, E = \\text{AncestryRelations}$$

### 2.2 Ancestry Relation

$$\\text{Ancestry}(f_1, f_2) \\iff f_2 \\text{ is derived from } f_1$$

### 2.3 Acyclicity

$$\\text{Valid}(G) \\iff \\neg\\exists\\, \\text{cycle in } G$$

The ancestry graph must be acyclic — no framework may be its own ancestor.""",
    },
    "07_PROVENANCE/FRAMEWORK_IP_LINEAGE.md": {
        "title": "Framework IP Lineage",
        "id": "framework_ip_lineage",
        "purpose": "The Framework IP Lineage records the intellectual property lineage of AMOS frameworks, establishing origin architect authority and stewardship chain.",
        "content": """### 2.1 IP Lineage Entry

$$\\text{IP}(f) = (\\text{framework}, \\text{origin\\_architect}, \\text{steward}, \\text{license}, \\text{creation\\_date})$$

### 2.2 Origin Architect Authority

$$\\text{OriginArchitect}(f) = \\text{Trang Phan}, \\forall\\, f \\in \\text{AMOS Frameworks}$$

### 2.3 Stewardship Transfer

$$\\text{Transfer}(f, s_1, s_2) \\implies \\text{Record}(f, s_1, s_2, \\text{timestamp}, \\text{authority})$$""",
    },
    "07_PROVENANCE/HERITAGE_PROVENANCE.md": {
        "title": "Heritage Provenance",
        "id": "heritage_provenance",
        "purpose": "The Heritage Provenance registry traces the lineage of heritage decision intelligence artifacts, connecting them to ancestral and civilizational sources.",
        "content": """### 2.1 Heritage Source

$$\\text{HeritageSource}(h) = (h, \\text{tradition}, \\text{generation}, \\text{source\\_independence})$$

### 2.2 Source Independence

$$\\text{Independent}(h) \\iff \\text{source\\_independence}(h) > 0.8$$

### 2.3 Heritage Preservation

Heritage provenance must preserve lineage, not erase it. Invalidated heritage is archived, not deleted.""",
    },
    "07_PROVENANCE/HERITAGE_SOURCE_REGISTRY.md": {
        "title": "Heritage Source Registry",
        "id": "heritage_source_registry",
        "purpose": "The Heritage Source Registry catalogs all sources of heritage decision intelligence, including ancestral traditions, civilizational records, and historical decision receipts.",
        "content": """### 2.1 Source Entry

$$\\text{Source}(s) = (\\text{source\\_id}, \\text{tradition}, \\text{era}, \\text{reliability}, \\text{independence})$$

### 2.2 Reliability Scoring

$$\\text{Reliable}(s) \\iff \\text{reliability}(s) > 0.7 \\wedge \\text{independence}(s) > 0.8$$

### 2.3 Cross-Validation

Heritage sources require cross-validation with at least 2 independent traditions (Rule of 2).""",
    },
    "07_PROVENANCE/IP_OWNERSHIP_REGISTRY.md": {
        "title": "IP Ownership Registry",
        "id": "ip_ownership_registry",
        "purpose": "The IP Ownership Registry records the intellectual property ownership of all AMOS OS artifacts, establishing who holds authority over each artifact.",
        "content": """### 2.1 Ownership Entry

$$\\text{Owner}(a) = (\\text{artifact}, \\text{owner}, \\text{ownership\\_type}, \\text{since})$$

### 2.2 Origin Architect Ownership

$$\\text{Owner}(a) = \\text{Trang Phan}, \\forall\\, a \\in \\text{AMOS Native Canon}$$

### 2.3 Ownership Transfer

Ownership transfer requires explicit authority, receipt, and provenance recording.""",
    },
    "07_PROVENANCE/LICENSE_REGISTRY.md": {
        "title": "License Registry",
        "id": "license_registry",
        "purpose": "The License Registry records the licensing terms for all AMOS OS artifacts, establishing usage rights and restrictions.",
        "content": """### 2.1 License Entry

$$\\text{License}(a) = (\\text{artifact}, \\text{license\\_type}, \\text{terms}, \\text{grantor})$$

### 2.2 Default License

All AMOS native canon artifacts are governed by the AMOS origin architect authority (Trang Phan).

### 2.3 External Material

External research material retains its original license and is linked as evidence, not incorporated as canon.""",
    },
    "07_PROVENANCE/NATIVE_CANON_SOURCE_REGISTRY.md": {
        "title": "Native Canon Source Registry",
        "id": "native_canon_source_registry",
        "purpose": "The Native Canon Source Registry catalogs all sources of native AMOS canon — material that originated within the AMOS corpus rather than from external sources.",
        "content": """### 2.1 Native Canon Source

$$\\text{Native}(s) \\iff \\text{origin}(s) = \\text{AMOS\\_corpus}$$

### 2.2 Source Classification

```text
NATIVE_CANON:     originated within AMOS corpus by Trang Phan
EXTERNAL_RESEARCH: originated from external research
HISTORICAL:       originated from historical/heritage sources
DERIVED:          derived from other canonical artifacts
```

### 2.3 Native Canon Integrity

Native canon sources must have complete provenance: origin architect, creation date, and lineage chain.""",
    },
    "07_PROVENANCE/NEUROSYNCAI_PROVENANCE.md": {
        "title": "NeuroSyncAI Provenance",
        "id": "neurosyncai_provenance",
        "purpose": "The NeuroSyncAI Provenance registry traces the lineage of NeuroSyncAI framework artifacts, connecting them to BCI and neuroscience research sources.",
        "content": """### 2.1 NeuroSyncAI Source

$$\\text{Source}(n) = (\\text{artifact}, \\text{research\\_source}, \\text{validation\\_status})$$

### 2.2 Research Source Types

```text
BCI_RESEARCH:     brain-computer interface research papers
NEUROSCIENCE:     neuroscience literature
CLINICAL_TRIALS:  clinical validation studies
AMOS_MODEL:       AMOS-internal model extensions
```

### 2.3 Provenance Independence

NeuroSyncAI claims require 2+ independent research sources (Rule of 2) before promotion above SOURCE_CLAIM.""",
    },
    "07_PROVENANCE/ORIGINAL_SOURCE_REGISTRY.md": {
        "title": "Original Source Registry",
        "id": "original_source_registry",
        "purpose": "The Original Source Registry catalogs the original sources from which AMOS canonical artifacts were derived, establishing the root of each provenance chain.",
        "content": """### 2.1 Original Source

$$\\text{Original}(s) \\iff \\neg\\exists\\, s' : \\text{Derived}(s, s')$$

An original source has no predecessor — it is the root of a provenance chain.

### 2.2 Root Tracing

$$\\text{Root}(a) = \\text{Original}(\\text{Chain}(a)[-1])$$

### 2.3 Root Integrity

Original sources must have declared origin architect, creation date, and ownership.""",
    },
    "07_PROVENANCE/ORIGIN_ARCHITECT_REGISTRY.md": {
        "title": "Origin Architect Registry",
        "id": "origin_architect_registry",
        "purpose": "The Origin Architect Registry records the origin architect and steward for each AMOS OS artifact, establishing authority and accountability.",
        "content": """### 2.1 Origin Architect Entry

$$\\text{Architect}(a) = (\\text{artifact}, \\text{origin\\_architect}, \\text{steward}, \\text{since})$$

### 2.2 AMOS Origin Architect

$$\\text{OriginArchitect}(a) = \\text{Trang Phan}, \\forall\\, a \\in \\text{AMOS Native}$$

### 2.3 Stewardship

The steward is responsible for maintaining the artifact's canonical status, provenance, and integrity. Stewardship transfer requires explicit recording.""",
    },
    "07_PROVENANCE/PROVENANCE_INDEPENDENCE_REGISTRY.md": {
        "title": "Provenance Independence Registry",
        "id": "provenance_independence_registry",
        "purpose": "The Provenance Independence Registry records the independence status of provenance sources, supporting Rule of 2 (R2) enforcement.",
        "content": """### 2.1 Independence Entry

$$\\text{Independence}(s_1, s_2) = (s_1, s_2, \\text{independent}, \\text{confidence}, \\text{evidence})$$

### 2.2 Independence Test

$$\\text{Independent}(s_1, s_2) \\iff \\neg\\text{SharedOrigin}(s_1, s_2) \\wedge \\neg\\text{SharedDependency}(s_1, s_2) \\wedge \\neg\\text{SharedLineage}(s_1, s_2)$$

### 2.3 Sybil Hardening

This registry supports the K_SYBIL_HARDENING kernel contract by detecting when apparent multiplicity is actually single-origin.""",
    },
    "07_PROVENANCE/PROVENANCE_ROOT_REGISTRY.md": {
        "title": "Provenance Root Registry",
        "id": "provenance_root_registry",
        "purpose": "The Provenance Root Registry identifies the root sources of all provenance chains in the AMOS OS, establishing the foundation for provenance tracing.",
        "content": """### 2.1 Root Entry

$$\\text{Root}(c) = (\\text{canon\\_id}, \\text{root\\_source}, \\text{root\\_type}, \\text{depth})$$

### 2.2 Root Types

```text
NATIVE:     root is an AMOS native source
EXTERNAL:   root is an external research source
HISTORICAL: root is a historical/heritage source
```

### 2.3 Root Integrity

Root sources must have complete provenance metadata and declared ownership.""",
    },
    "07_PROVENANCE/QLS_QCLA_PROVENANCE.md": {
        "title": "QLS/QCLA Provenance",
        "id": "qls_qcla_provenance",
        "purpose": "The QLS/QCLA Provenance registry traces the lineage of Quantum Logic Structure and Quantum Causality Layer Architecture artifacts.",
        "content": """### 2.1 QLS Source

$$\\text{Source}(q) = (\\text{artifact}, \\text{framework\\_origin}, \\text{quantum\\_analogy\\_basis})$$

### 2.2 Quantum Analogy Note

QLS/QCLA artifacts use quantum mechanics as ANALOGY/METAPHOR for reasoning, NOT as physical predictions. All QLS/QCLA claims are AMOS_MODEL.

### 2.3 Provenance Chain

QLS/QCLA provenance chains trace back to either:
- AMOS native canon (Trang Phan)
- Quantum mechanics literature (used as analogy, not as empirical basis)""",
    },
    "07_PROVENANCE/SOURCE_ANCESTRY_GRAPH.md": {
        "title": "Source Ancestry Graph",
        "id": "source_ancestry_graph",
        "purpose": "The Source Ancestry Graph records the parent-child relationships between AMOS sources, showing how sources depend on and derive from each other.",
        "content": """### 2.1 Graph Structure

$$G = (V, E) : V = \\text{Sources}, E = \\text{AncestryRelations}$$

### 2.2 Ancestry Relation

$$\\text{Ancestry}(s_1, s_2) \\iff s_2 \\text{ is derived from } s_1$$

### 2.3 Acyclicity

The source ancestry graph must be acyclic — no source may be its own ancestor.""",
    },
    "07_PROVENANCE/SOURCE_TO_CANON_MAP.md": {
        "title": "Source to Canon Map",
        "id": "source_to_canon_map",
        "purpose": "The Source to Canon Map is the reverse mapping of the Canon to Source Map, enabling lookup of all canonical artifacts derived from a given source.",
        "content": """### 2.1 Reverse Mapping

$$\\text{ReverseMap}(s) = \\{c : \\text{Map}(c, s)\\}$$

### 2.2 Impact Analysis

When a source is updated or invalidated, the reverse map identifies all canonical artifacts that depend on it.

### 2.3 Invalidation Propagation

$$\\text{Invalidated}(s) \\implies \\forall\\, c \\in \\text{ReverseMap}(s), \\text{Revalidate}(c)$$""",
    },
    "07_PROVENANCE/TRANG_ORIGIN_PROVENANCE.md": {
        "title": "Trang Origin Provenance",
        "id": "trang_origin_provenance",
        "purpose": "The Trang Origin Provenance registry establishes Trang Phan as the origin architect of the AMOS OS and the Trang Framework, recording the foundational provenance of the entire system.",
        "content": """### 2.1 Origin Declaration

$$\\text{OriginArchitect}(\\text{AMOS}) = \\text{Trang Phan}$$
$$\\text{OriginArchitect}(\\text{Trang Framework}) = \\text{Trang Phan}$$

### 2.2 Foundational Artifacts

The foundational artifacts created by the origin architect include:
- AMOS Core Laws (L0-L32)
- Trang Framework (D, R, C, M, H, Repair, Recursion, Selection, Consequence)
- 7-Part Universe Canon
- UBI (Unified Biological Intelligence)
- QLS/QCLA (Quantum Logic Structure / Quantum Causality Layer Architecture)
- TSS/TPE (The Trang System / Trang Prediction Engine)

### 2.3 Agent Invariant

Agents MUST NOT claim independent authorship of AMOS. All AMOS native canon traces to Trang Phan as origin architect.""",
    },
    "07_PROVENANCE/TSS_TPE_PROVENANCE.md": {
        "title": "TSS/TPE Provenance",
        "id": "tss_tpe_provenance",
        "purpose": "The TSS/TPE Provenance registry traces the lineage of The Trang System (TSS) and Trang Prediction Engine (TPE) artifacts.",
        "content": """### 2.1 TSS Source

$$\\text{Source}(t) = (\\text{artifact}, \\text{origin}, \\text{validation\\_status})$$

### 2.2 TSS Origin

TSS originated from Trang Phan's governance and institutional framework design.

### 2.3 TPE Origin

TPE originated from Trang Phan's foresight and prediction system design, incorporating 7-cycle evolutionary transitions and multi-horizon intervention planning.""",
    },
    "07_PROVENANCE/UBI_PROVENANCE.md": {
        "title": "UBI Provenance",
        "id": "ubi_provenance",
        "purpose": "The UBI Provenance registry traces the lineage of Unified Biological Intelligence (UBI) framework artifacts.",
        "content": """### 2.1 UBI Source

$$\\text{Source}(u) = (\\text{artifact}, \\text{domain}, \\text{research\\_basis})$$

### 2.2 UBI Domains

UBI provenance covers 4 domains:
- NBI: Neurobiological Intelligence (neuroscience literature)
- NEI: Neuroemotional Intelligence (affective neuroscience)
- SI: Somatic Intelligence (interoception research)
- BEI: Neuroelectromagnetic Intelligence (cardiac coherence research)

### 2.3 AMOS Model Boundary

All UBI artifacts are AMOS_MODEL. Biological research is used as evidence, not as empirical validation of UBI claims.""",
    },
    "07_PROVENANCE/UNIVERSE_CANON_PROVENANCE.md": {
        "title": "Universe Canon Provenance",
        "id": "universe_canon_provenance",
        "purpose": "The Universe Canon Provenance registry traces the lineage of 7-Part Universe Canon artifacts.",
        "content": """### 2.1 Universe Canon Source

$$\\text{Source}(u) = (\\text{artifact}, \\text{part}, \\text{origin})$$

### 2.2 Seven Parts

Universe Canon provenance covers all 7 parts:
- P1 Reality, P2 Flow, P3 Structure, P4 Behavior
- P5 Identity, P6 Enforcement, P7 Evolution

### 2.3 Origin

The 7-Part Universe Canon originated from Trang Phan's universe-level structural reasoning, incorporating concepts from systems theory, thermodynamics (as analogy), and information theory.""",
    },
    "07_PROVENANCE/VERSION_HASH_REGISTRY.md": {
        "title": "Version Hash Registry",
        "id": "version_hash_registry",
        "purpose": "The Version Hash Registry maintains cryptographic hashes for each version of each AMOS OS artifact, enabling version integrity verification and rollback validation.",
        "content": """### 2.1 Version Hash Entry

$$\\text{Entry}(a, v) = (\\text{artifact}, \\text{version}, \\text{hash}, \\text{timestamp}, \\text{changeset})$$

### 2.2 Version Integrity

$$\\text{Intact}(a, v) \\iff \\text{Hash}(\\text{Content}(a, v)) = \\text{RegisteredHash}(a, v)$$

### 2.3 Rollback Validation

$$\\text{RollbackValid}(a, v) \\iff \\text{Intact}(a, v) \\wedge \\text{VersionExists}(a, v)$$

### 2.4 Hash Algorithm

BLAKE3 (256-bit) for all version hashes.""",
    },
}

# Supersession file definitions
SUPERSESSION_FILES = {
    "08_SUPERSESSION/ACTIVE_VS_LEGACY_CANON.md": {
        "title": "Active vs Legacy Canon",
        "id": "active_vs_legacy_canon",
        "purpose": "The Active vs Legacy Canon registry distinguishes between currently active canonical artifacts and legacy (superseded but preserved) artifacts.",
        "content": """### 2.1 Active vs Legacy

$$\\text{Active}(a) \\iff \\text{status}(a) \\in \\{\\text{ACTIVE}, \\text{SUBSTANTIVE\\_SPECIFICATION}\\}$$
$$\\text{Legacy}(a) \\iff \\text{status}(a) = \\text{SUPERSEDED}$$

### 2.2 Supersession Rule

When artifact $a_1$ is superseded by $a_2$:
- $a_1$ status → SUPERSEDED
- $a_2$ status → ACTIVE
- $a_1$ is preserved (archived, not deleted)
- Lineage link: $a_1 \\to a_2$

### 2.3 No Silent Replacement

$$\\text{Replace}(a_1, a_2) \\implies \\text{Record}(a_1, a_2, \\text{timestamp}, \\text{authority}, \\text{reason})$$

Supersession must be explicitly recorded with authority and reason.""",
    },
    "08_SUPERSESSION/CANON_SUPERSESSION_REGISTRY.md": {
        "title": "Canon Supersession Registry",
        "id": "canon_supersession_registry",
        "purpose": "The Canon Supersession Registry records all canonical artifact supersessions, preserving the full history of what replaced what and why.",
        "content": """### 2.1 Supersession Entry

$$\\text{Supersede}(a_1, a_2) = (a_1, a_2, \\text{timestamp}, \\text{authority}, \\text{reason}, \\text{changeset})$$

### 2.2 Supersession Chain

$$\\text{Chain}(a) = [a, \\text{superseded\\_by}(a), \\text{superseded\\_by}(\\text{superseded\\_by}(a)), \\ldots]$$

### 2.3 No Erasure

Superseded artifacts are archived, never deleted. The supersession chain must be complete and traceable.""",
    },
    "08_SUPERSESSION/CORE_LAW_SUPERSESSION.md": {
        "title": "Core Law Supersession",
        "id": "core_law_supersession",
        "purpose": "The Core Law Supersession registry records supersessions of AMOS core laws (L0-L32), preserving the evolution history of the law hierarchy.",
        "content": """### 2.1 Law Supersession

$$\\text{Supersede}(L_1, L_2) \\implies \\text{Level}(L_2) \\geq \\text{Level}(L_1)$$

A law may only be superseded by a law at the same or higher level.

### 2.2 Promotion Chain

```text
PROPOSED_SPECIFICATION → CONDITIONAL → CANON_LAW
```

Each promotion requires evidence, validation receipt, and authority.

### 2.3 Historical Preservation

Superseded laws are preserved with their original content, provenance, and lineage. The supersession record links old to new.""",
    },
    "08_SUPERSESSION/DEPRECATED_CANON_REGISTRY.md": {
        "title": "Deprecated Canon Registry",
        "id": "deprecated_canon_registry",
        "purpose": "The Deprecated Canon Registry records canonical artifacts that have been deprecated — they should no longer be used but are preserved for historical reference.",
        "content": """### 2.1 Deprecation Entry

$$\\text{Deprecate}(a) = (a, \\text{timestamp}, \\text{authority}, \\text{reason}, \\text{replacement})$$

### 2.2 Deprecation vs Supersession

- Superseded: replaced by a specific newer artifact
- Deprecated: should no longer be used, may or may not have a direct replacement

### 2.3 No Erasure

Deprecated artifacts are preserved with lineage. Deprecation preserves history, it does not erase it.""",
    },
    "08_SUPERSESSION/HISTORICAL_CANON_PRESERVATION.md": {
        "title": "Historical Canon Preservation",
        "id": "historical_canon_preservation",
        "purpose": "The Historical Canon Preservation registry ensures that all historical canonical artifacts are preserved and accessible, supporting provenance tracing and rollback.",
        "content": """### 2.1 Preservation Rule

$$\\forall\\, a \\in \\text{CanonHistory}, \\text{Preserved}(a) \\iff \\text{Archived}(a) \\wedge \\text{Accessible}(a) \\wedge \\text{Lineage}(a) \\text{ is complete}$$

### 2.2 Archive Integrity

Historical artifacts must maintain:
- Original content (unchanged)
- Original provenance (complete chain)
- Supersession links (to successor if any)
- Access metadata (retrievable by id + version)

### 2.3 No Silent Deletion

No canonical artifact may be silently deleted. All removals must go through the supersession/deprecation process.""",
    },
    "08_SUPERSESSION/LINEAGE_PRESERVATION_LAW.md": {
        "title": "Lineage Preservation Law",
        "id": "lineage_preservation_law",
        "purpose": "The Lineage Preservation Law establishes the requirement that all canonical artifact lineage must be preserved across supersessions, deprecations, and version changes.",
        "content": """### 2.1 Lineage Preservation Invariant

$$\\text{Preserved}(a) \\implies \\text{Lineage}(a) \\text{ is complete} \\wedge \\text{Lineage}(a) \\text{ is traceable} \\wedge \\text{Lineage}(a) \\text{ is tamper-evident}$$

### 2.2 Lineage Completeness

$$\\text{Complete}(\\text{Lineage}(a)) \\iff \\forall\\, n \\in \\text{Lineage}(a), \\text{Source}(n) \\neq \\text{null} \\wedge \\text{Timestamp}(n) \\neq \\text{null}$$

### 2.3 No Lineage Erasure

$$\\text{Supersede}(a_1, a_2) \\implies \\text{Lineage}(a_2) \\supseteq \\text{Lineage}(a_1)$$

The successor's lineage must include the predecessor's lineage.""",
    },
    "08_SUPERSESSION/VERSION_SUPERSESSION_REGISTRY.md": {
        "title": "Version Supersession Registry",
        "id": "version_supersession_registry",
        "purpose": "The Version Supersession Registry records version-to-version supersessions within individual artifacts, tracking how each artifact has evolved over time.",
        "content": """### 2.1 Version Supersession Entry

$$\\text{VersionSupersede}(a, v_1, v_2) = (a, v_1, v_2, \\text{timestamp}, \\text{changeset}, \\text{validation})$$

### 2.2 Version Chain

$$\\text{Chain}(a) = [v_1, v_2, \\ldots, v_n] : v_{i+1} \\text{ supersedes } v_i$$

### 2.3 Version Integrity

Each version must have:
- Complete content (the artifact as it was at that version)
- Hash (for integrity verification)
- Changeset (what changed from the previous version)
- Validation status (was this version validated?)""",
    },
    "08_SUPERSESSION/SUPERSESSION_AUDIT_TRAIL.md": {
        "title": "Supersession Audit Trail",
        "id": "supersession_audit_trail",
        "purpose": "The Supersession Audit Trail records all supersession events in chronological order, providing a complete history of canonical artifact evolution.",
        "content": """### 2.1 Audit Trail Entry

$$\\text{Audit}(e) = (\\text{event\\_id}, \\text{timestamp}, \\text{event\\_type}, \\text{artifact}, \\text{actor}, \\text{details})$$

### 2.2 Event Types

```text
SUPERSEDE:     artifact was superseded by a newer version
DEPRECATE:     artifact was deprecated
PROMOTE:       artifact was promoted to a higher status
RESTORE:       superseded artifact was restored to active
ARCHIVE:       artifact was moved to archive
```

### 2.3 Trail Integrity

The audit trail must be:
- Complete (no missing events)
- Tamper-evident (hash-chained)
- Chronologically ordered
- Independently verifiable""",
    },
    "08_SUPERSESSION/SUPERSESSION_CHAIN_VALIDATOR.md": {
        "title": "Supersession Chain Validator",
        "id": "supersession_chain_validator",
        "purpose": "The Supersession Chain Validator validates the integrity and completeness of supersession chains, ensuring no gaps or inconsistencies in canonical artifact evolution.",
        "content": """### 2.1 Validation Checks

$$\\text{Valid}(\\text{Chain}(a)) \\iff \\text{Complete}(\\text{Chain}(a)) \\wedge \\text{Consistent}(\\text{Chain}(a)) \\wedge \\text{Ordered}(\\text{Chain}(a))$$

### 2.2 Completeness Check

Every link in the chain must have: predecessor, successor, timestamp, authority, and reason.

### 2.3 Consistency Check

No artifact may appear twice in the same chain. No chain may have cycles.

### 2.4 Ordering Check

Chain timestamps must be strictly monotonic — each successor's timestamp must be later than its predecessor's.""",
    },
}

TEMPLATE = '''---
title: {title}
type: {type}
source: 01_CANON/{dir}
artifact: {filename}
artifact_id: amos_01_canon_{dir_id}_{id}
origin_architect: Trang Phan
steward: Trang Phan
system: AMOS OS
plane: 01_CANON
segment: 01_CANON/{dir}
artifact_kind: {kind}
path: 01_CANON/{dir}/{filename}
tags:
  - amos-os
  - canon
  - {dir_tag}
  - rscf
  - placeholder_expanded
  - law-hierarchy{tags_extra}
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

node_id: amos_01_canon_{dir_id}_{id}

node_type: {kind}

path: 01_CANON/{dir}/{filename}

claim_class: AMOS_MODEL

rscf_state: DERIVED

canonical_status: CONDITIONAL

RSCF-RELATIONS:

- INDEXED_BY: [[00_ROOT/00_HOME|00_HOME]]

- INDEXED_BY: [[00_ROOT/AMOS_RSCF_NODES|AMOS_RSCF_NODES]]

- GOVERNED_BY: [[01_CANON/01_CORE_LAWS/LAW_HIERARCHY|LAW_HIERARCHY]]

______________________________________________________________________

**MOC:** [[01_CANON/{dir}/{moc}|{moc}]]
'''


def expand_file(filepath, content_def, dir_name, dir_id, dir_tag, kind, moc, type_name="registry"):
    filename = os.path.basename(filepath)
    title = content_def["title"]
    title_short = title.replace(" Registry", "").replace(" Provenance", "").replace(" Law", "")

    tags_extra = ""
    if "tags_extra" in content_def:
        tags_extra = "\n  - " + "\n  - ".join(content_def["tags_extra"])

    content = TEMPLATE.format(
        title=title,
        title_short=title_short,
        type=type_name,
        dir=dir_name,
        dir_id=dir_id,
        dir_tag=dir_tag,
        kind=kind,
        filename=filename,
        id=content_def["id"],
        tags_extra=tags_extra,
        purpose=content_def["purpose"],
        content=content_def["content"],
        moc=moc,
    )

    with open(filepath, "w") as f:
        f.write(content)
    return len(content)


def main():
    expanded = 0

    # Provenance files
    for rel_path, content_def in PROVENANCE_FILES.items():
        filepath = CANON_DIR / rel_path
        if filepath.exists():
            size = expand_file(str(filepath), content_def, "07_PROVENANCE", "07_provenance", "provenance", "REGISTRY", "07_PROVENANCE_MOC.md")
            print(f"Expanded {rel_path}: {size} bytes")
            expanded += 1
        else:
            print(f"WARNING: {rel_path} not found")

    # Supersession files
    for rel_path, content_def in SUPERSESSION_FILES.items():
        filepath = CANON_DIR / rel_path
        if filepath.exists():
            size = expand_file(str(filepath), content_def, "08_SUPERSESSION", "08_supersession", "supersession", "REGISTRY", "08_SUPERSESSION_MOC.md")
            print(f"Expanded {rel_path}: {size} bytes")
            expanded += 1
        else:
            print(f"WARNING: {rel_path} not found")

    print(f"\nTotal expanded: {expanded}")


if __name__ == "__main__":
    main()
