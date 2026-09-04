#!/usr/bin/env python3
"""Expand 01_CANON/00_INDEX placeholder files with substantive registry content."""

import os
from pathlib import Path

DIR = Path("/Users/mac/Documents/AMOS_OS/01_CANON/00_INDEX")

INDEX_FILES = {
    "CANON_MASTER_INDEX.md": {
        "title": "Canon Master Index",
        "id": "canon_master_index",
        "purpose": "The Canon Master Index is the top-level index of all canonical artifacts in the AMOS OS, providing a navigable map of the entire canon plane.",
        "content": """### 2.1 Index Structure

The master index organizes canonical artifacts by:
- **Plane**: 01_CANON (this plane)
- **Segment**: 01_CORE_LAWS, 02_UNIVERSE_CANON, 03_COGNITION_CANON, 04_INFRASTRUCTURE_CANON, 05_VARIABLE_REGISTRY, 06_GLOSSARY, 07_PROVENANCE, 08_SUPERSESSION
- **Artifact kind**: LAW, CANON, REGISTRY, GLOSSARY, RECEIPT, CONTRACT, MAP, INDEX
- **Status**: ACTIVE, SUBSTANTIVE_SPECIFICATION, PLACEHOLDER, SUPERSEDED, DEPRECATED

### 2.2 Index Entry

$$\\text{Entry}(a) = (\\text{artifact\\_id}, \\text{path}, \\text{segment}, \\text{kind}, \\text{status}, \\text{version})$$

### 2.3 Completeness

$$\\text{Complete}(\\text{Index}) \\iff \\forall\\, a \\in \\text{Canon}, a \\in \\text{Index}$$

Every canonical artifact must appear in the master index.""",
    },
    "CANON_FRAMEWORK_REGISTRY.md": {
        "title": "Canon Framework Registry",
        "id": "canon_framework_registry",
        "purpose": "The Canon Framework Registry catalogs all AMOS frameworks, recording their identity, origin, domain, and canonical status.",
        "content": """### 2.1 Framework Entry

$$\\text{Framework}(f) = (\\text{name}, \\text{origin\\_architect}, \\text{domain}, \\text{canonical\\_status}, \\text{version})$$

### 2.2 Registered Frameworks

| Framework | Domain | Origin | Status |
|:---|:---|:---|:---|
| Omega | Universe/Risk | Trang Phan | CONDITIONAL |
| UBI | Biology/Cognition | Trang Phan | CONDITIONAL |
| QLS/QCLA | Quantum/Logic | Trang Phan | CONDITIONAL |
| Trang | Ontology/Dynamics | Trang Phan | CONDITIONAL |
| TSS/TPE | Governance/Prediction | Trang Phan | CONDITIONAL |
| RSCF | Epistemic | Trang Phan | CONDITIONAL |
| GMEF | Evolution/Mutation | Trang Phan | CONDITIONAL |
| Heritage | Cultural/Decision | Trang Phan | CONDITIONAL |
| NeuroSyncAI | BCI/Neural | Trang Phan | CONDITIONAL |

### 2.3 No Unregistered Frameworks

All AMOS frameworks must be registered. Unregistered frameworks are UNKNOWN/GAP.""",
    },
    "CANON_FAMILY_REGISTRY.md": {
        "title": "Canon Family Registry",
        "id": "canon_family_registry",
        "purpose": "The Canon Family Registry groups related canonical artifacts into families, enabling hierarchical navigation and cross-reference.",
        "content": """### 2.1 Family Entry

$$\\text{Family}(f) = (\\text{family\\_name}, \\text{parent\\_family}, \\text{members}, \\text{domain})$$

### 2.2 Family Hierarchy

```text
AMOS_ROOT
├── CORE_LAWS (L0-L32)
├── UNIVERSE_CANON (P1-P7)
├── COGNITION_CANON
├── INFRASTRUCTURE_CANON
├── VARIABLE_REGISTRY
├── GLOSSARY
├── PROVENANCE
└── SUPERSESSION
```

### 2.3 Family Membership

Each canonical artifact belongs to exactly one family. Cross-family references are tracked via the relation registry.""",
    },
    "CANON_DOMAIN_REGISTRY.md": {
        "title": "Canon Domain Registry",
        "id": "canon_domain_registry",
        "purpose": "The Canon Domain Registry maps canonical artifacts to AMOS domains (C01-C12), ensuring each artifact is properly classified by domain.",
        "content": """### 2.1 Domain Entry

$$\\text{Domain}(d) = (\\text{domain\\_id}, \\text{name}, \\text{canon\\_artifacts}, \\text{master\\_skill})$$

### 2.2 AMOS Domains

| Domain | Name | Canon Segment |
|:---|:---|:---|
| C01 | Meta Logic | 01_CORE_LAWS |
| C02 | Math & Compute | 05_VARIABLE_REGISTRY |
| C03 | Physics & Cosmos | 02_UNIVERSE_CANON |
| C04 | Bio & Neuro | 03_COGNITION_CANON |
| C05 | Mind & Behavior | 03_COGNITION_CANON |
| C06 | Society & Culture | 02_UNIVERSE_CANON |
| C07 | Econ & Finance | 04_INFRASTRUCTURE_CANON |
| C08 | Strategy & Game | 04_INFRASTRUCTURE_CANON |
| C09 | Org, Law & Policy | 04_INFRASTRUCTURE_CANON |
| C10 | Tech & Engineering | 04_INFRASTRUCTURE_CANON |
| C11 | Design & Language | 06_GLOSSARY |
| C12 | Earth & Ecology | 02_UNIVERSE_CANON |

### 2.3 Domain Coverage

Each domain must have at least one canonical artifact. Domains with no canonical artifacts are UNKNOWN/GAP.""",
    },
    "CANON_OBJECT_REGISTRY.md": {
        "title": "Canon Object Registry",
        "id": "canon_object_registry",
        "purpose": "The Canon Object Registry catalogs all canonical object types in the AMOS OS, defining the type system for canonical artifacts.",
        "content": """### 2.1 Object Type Entry

$$\\text{ObjectType}(t) = (\\text{type\\_name}, \\text{parent\\_type}, \\text{fields}, \\text{constraints})$$

### 2.2 Canonical Object Types

| Type | Parent | Description |
|:---|:---|:---|
| LAW | CANON_OBJECT | A core law (L0-L32) |
| CANON | CANON_OBJECT | A canonical specification |
| REGISTRY | CANON_OBJECT | A registry of canonical items |
| GLOSSARY | CANON_OBJECT | A glossary of terms |
| RECEIPT | CANON_OBJECT | A validation/action receipt |
| CONTRACT | CANON_OBJECT | A governing contract |
| MAP | CANON_OBJECT | A navigational map |
| INDEX | CANON_OBJECT | An index of artifacts |

### 2.3 Type Safety

Canonical artifacts must declare their object type. Type mismatches are validation failures.""",
    },
    "CANON_RELATION_REGISTRY.md": {
        "title": "Canon Relation Registry",
        "id": "canon_relation_registry",
        "purpose": "The Canon Relation Registry records relationships between canonical artifacts, enabling cross-reference navigation and dependency tracking.",
        "content": """### 2.1 Relation Entry

$$\\text{Relation}(a_1, a_2, r) = (a_1, a_2, \\text{relation\\_type}, \\text{strength}, \\text{evidence})$$

### 2.2 Relation Types

| Type | Description |
|:---|:---|
| GOVERNS | $a_1$ governs $a_2$ |
| DEPENDS_ON | $a_1$ depends on $a_2$ |
| DERIVED_FROM | $a_1$ is derived from $a_2$ |
| SUPERSEDES | $a_1$ supersedes $a_2$ |
| COMPLEMENTS | $a_1$ complements $a_2$ |
| CONFLICTS_WITH | $a_1$ conflicts with $a_2$ |
| REFERENCES | $a_1$ references $a_2$ |

### 2.3 Relation Integrity

$$\\text{Valid}(r) \\iff \\text{Source}(r) \\neq \\text{null} \\wedge \\text{Target}(r) \\neq \\text{null} \\wedge \\text{Type}(r) \\in \\text{RelationTypes}$$""",
    },
    "CANON_STATUS_REGISTRY.md": {
        "title": "Canon Status Registry",
        "id": "canon_status_registry",
        "purpose": "The Canon Status Registry defines the canonical status values that AMOS artifacts can hold, and the valid transitions between them.",
        "content": """### 2.1 Status Values

| Status | Description |
|:---|:---|
| PLACEHOLDER | Structural placeholder, no substantive content |
| SUBSTANTIVE_SPECIFICATION | Has substantive content, not yet promoted |
| PROPOSED_SPECIFICATION | Formally proposed, under review |
| CONDITIONAL | Conditionally canonical, pending validation |
| ACTIVE_CANON_CANDIDATE | Candidate for full canon promotion |
| CANON_LAW | Fully canonical law |
| SUPERSEDED | Replaced by a newer version |
| DEPRECATED | Should no longer be used |
| UNKNOWN/GAP | Status unknown or gap |

### 2.2 Valid Transitions

```text
PLACEHOLDER → SUBSTANTIVE_SPECIFICATION → PROPOSED_SPECIFICATION → CONDITIONAL → ACTIVE_CANON_CANDIDATE → CANON_LAW
                                                                                                    ↓
                                                                                              SUPERSEDED → DEPRECATED
```

### 2.3 No Skip Promotion

$$\\text{Promote}(a, s_1, s_2) \\implies \\text{ValidTransition}(s_1, s_2)$$

Status promotions must follow valid transitions. Skipping levels requires explicit authority.""",
    },
    "CANON_VERSION_REGISTRY.md": {
        "title": "Canon Version Registry",
        "id": "canon_version_registry",
        "purpose": "The Canon Version Registry records all versions of canonical artifacts, tracking the version history of each artifact.",
        "content": """### 2.1 Version Entry

$$\\text{Version}(a, v) = (\\text{artifact}, \\text{version}, \\text{timestamp}, \\text{changeset}, \\text{hash})$$

### 2.2 Version Chain

$$\\text{Chain}(a) = [v_1, v_2, \\ldots, v_n] : v_{i+1} \\text{ supersedes } v_i$$

### 2.3 Current Version

$$\\text{Current}(a) = \\text{Chain}(a)[-1]$$

The current version is the last in the chain. All previous versions are archived.""",
    },
    "CANON_LINEAGE_REGISTRY.md": {
        "title": "Canon Lineage Registry",
        "id": "canon_lineage_registry",
        "purpose": "The Canon Lineage Registry records the lineage of all canonical artifacts, tracing each artifact back to its origin.",
        "content": """### 2.1 Lineage Entry

$$\\text{Lineage}(a) = [a, \\text{parent}(a), \\text{parent}(\\text{parent}(a)), \\ldots, \\text{root}(a)]$$

### 2.2 Root Identification

$$\\text{Root}(a) = \\text{Lineage}(a)[-1] : \\text{parent}(\\text{Root}(a)) = \\text{null}$$

### 2.3 Lineage Completeness

$$\\text{Complete}(\\text{Lineage}(a)) \\iff \\forall\\, n \\in \\text{Lineage}(a), \\text{Source}(n) \\neq \\text{null}$$

Every node in the lineage must have a declared source. Incomplete lineages are UNKNOWN/GAP.""",
    },
    "CANON_SOURCE_REGISTRY.md": {
        "title": "Canon Source Registry",
        "id": "canon_source_registry",
        "purpose": "The Canon Source Registry catalogs all sources from which AMOS canonical artifacts were derived.",
        "content": """### 2.1 Source Entry

$$\\text{Source}(s) = (\\text{source\\_id}, \\text{type}, \\text{origin}, \\text{reliability}, \\text{independence})$$

### 2.2 Source Types

| Type | Description |
|:---|:---|
| NATIVE_CANON | Originated within AMOS corpus |
| EXTERNAL_RESEARCH | External research (arxiv, papers) |
| HISTORICAL | Historical/heritage sources |
| DERIVED | Derived from other canonical artifacts |

### 2.3 Source Quality

$$\\text{Quality}(s) = \\text{reliability}(s) \\cdot \\text{independence}(s)$$

High-quality sources have both high reliability and high independence.""",
    },
    "CANON_PROVENANCE_REGISTRY.md": {
        "title": "Canon Provenance Registry",
        "id": "canon_provenance_registry",
        "purpose": "The Canon Provenance Registry is the top-level provenance index, linking to detailed provenance records in 07_PROVENANCE.",
        "content": """### 2.1 Provenance Index Entry

$$\\text{Provenance}(a) = (\\text{artifact}, \\text{provenance\\_record\\_path}, \\text{root\\_source}, \\text{independence})$$

### 2.2 Link to 07_PROVENANCE

This registry is an index. Detailed provenance records are in:
- [[01_CANON/07_PROVENANCE/CANON_PROVENANCE|CANON_PROVENANCE]]
- [[01_CANON/07_PROVENANCE/ORIGINAL_SOURCE_REGISTRY|ORIGINAL_SOURCE_REGISTRY]]
- [[01_CANON/07_PROVENANCE/PROVENANCE_ROOT_REGISTRY|PROVENANCE_ROOT_REGISTRY]]

### 2.3 Provenance Completeness

$$\\text{Complete}(a) \\iff \\text{Provenance}(a) \\neq \\text{null} \\wedge \\text{Root}(a) \\neq \\text{null}$$""",
    },
    "CANON_SUPERSESSION_REGISTRY.md": {
        "title": "Canon Supersession Registry",
        "id": "canon_supersession_registry",
        "purpose": "The Canon Supersession Registry is the top-level supersession index, linking to detailed supersession records in 08_SUPERSESSION.",
        "content": """### 2.1 Supersession Index Entry

$$\\text{Supersession}(a) = (\\text{artifact}, \\text{supersession\\_record\\_path}, \\text{current\\_version}, \\text{predecessor})$$

### 2.2 Link to 08_SUPERSESSION

This registry is an index. Detailed supersession records are in:
- [[01_CANON/08_SUPERSESSION/ACTIVE_VS_LEGACY_CANON|ACTIVE_VS_LEGACY_CANON]]
- [[01_CANON/08_SUPERSESSION/AMOS_CORE_VERSION_LINEAGE|AMOS_CORE_VERSION_LINEAGE]]

### 2.3 No Silent Supersession

All supersessions must be recorded. Unrecorded supersessions are UNKNOWN/GAP.""",
    },
    "CANON_KERNEL_REGISTRY.md": {
        "title": "Canon Kernel Registry",
        "id": "canon_kernel_registry",
        "purpose": "The Canon Kernel Registry maps canonical artifacts to their kernel-level implementations in 02_KERNEL.",
        "content": """### 2.1 Kernel Mapping Entry

$$\\text{KernelMap}(a) = (\\text{canon\\_artifact}, \\text{kernel\\_contract}, \\text{implementation\\_status})$$

### 2.2 Implementation Status

| Status | Description |
|:---|:---|
| NOT_ESTABLISHED | No kernel implementation |
| PARTIAL | Some kernel contracts implemented |
| ESTABLISHED | Full kernel implementation |
| UNKNOWN/GAP | Status unknown |

### 2.3 Canon-Kernel Boundary

$$\\text{CANON} \\neq \\text{KERNEL}$$

Canon defines what; kernel implements how. The boundary must be preserved.""",
    },
    "CANON_ENGINE_REGISTRY.md": {
        "title": "Canon Engine Registry",
        "id": "canon_engine_registry",
        "purpose": "The Canon Engine Registry maps canonical artifacts to their engine-level implementations in the AMOS engines layer.",
        "content": """### 2.1 Engine Mapping Entry

$$\\text{EngineMap}(a) = (\\text{canon\\_artifact}, \\text{engine}, \\text{binding\\_type})$$

### 2.2 Engine Types

| Engine | Domain |
|:---|:---|
| Quantum Fractal Math | Formal verification |
| MURK Reasoning | Logic/Meta-logic |
| Go Board 19x19 | Strategic reasoning |
| UBI Bio Reasoning | Biology/Cognition |
| Strategic Foresight TSS/TPE | Governance/Prediction |
| Heritage Decision | Cultural/Decision |

### 2.3 Canon-Engine Boundary

$$\\text{CANON} \\neq \\text{ENGINE}$$

Canon defines what; engines execute how. The boundary must be preserved.""",
    },
    "CANON_PROTOCOL_REGISTRY.md": {
        "title": "Canon Protocol Registry",
        "id": "canon_protocol_registry",
        "purpose": "The Canon Protocol Registry maps canonical artifacts to their protocol-level implementations in 09_PROTOCOLS.",
        "content": """### 2.1 Protocol Mapping Entry

$$\\text{ProtocolMap}(a) = (\\text{canon\\_artifact}, \\text{protocol}, \\text{binding\\_type})$$

### 2.2 Protocol Types

| Protocol | Description |
|:---|:---|
| A2A | Agent-to-Agent |
| ANP | Agent Network Protocol |
| MCP | Model Context Protocol |
| agents.json | Agent capability manifest |

### 2.3 Canon-Protocol Boundary

$$\\text{CANON} \\neq \\text{PROTOCOL}$$

Canon defines what; protocols implement how. The boundary must be preserved.""",
    },
    "CANON_OS_REGISTRY.md": {
        "title": "Canon OS Registry",
        "id": "canon_os_registry",
        "purpose": "The Canon OS Registry maps canonical artifacts to their OS-level implementations in 04_RUNTIME.",
        "content": """### 2.1 OS Mapping Entry

$$\\text{OSMap}(a) = (\\text{canon\\_artifact}, \\text{runtime\\_component}, \\text{implementation\\_status})$$

### 2.2 Runtime Components

| Component | Description |
|:---|:---|
| Kernel | 02_KERNEL |
| Control Plane | 03_CONTROL_PLANE |
| Runtime | 04_RUNTIME |
| State | 12_STATE |
| Observability | 17_OBSERVABILITY |

### 2.3 Canon-OS Boundary

$$\\text{CANON} \\neq \\text{OS\\_RUNTIME}$$

Canon defines what; OS runtime implements how. The boundary must be preserved.""",
    },
    "CANON_IP_REGISTRY.md": {
        "title": "Canon IP Registry",
        "id": "canon_ip_registry",
        "purpose": "The Canon IP Registry records the intellectual property status of all canonical artifacts.",
        "content": """### 2.1 IP Entry

$$\\text{IP}(a) = (\\text{artifact}, \\text{owner}, \\text{license}, \\text{origin\\_architect})$$

### 2.2 AMOS IP

$$\\text{Owner}(a) = \\text{Trang Phan}, \\forall\\, a \\in \\text{AMOS Native Canon}$$

### 2.3 External IP

External research material retains its original IP. AMOS links to it as evidence, not as owned canon.""",
    },
    "CANON_TRADENAME_REGISTRY.md": {
        "title": "Canon Tradename Registry",
        "id": "canon_tradename_registry",
        "purpose": "The Canon Tradename Registry records the tradenames and brand names used in the AMOS OS.",
        "content": """### 2.1 Tradename Entry

$$\\text{Tradename}(t) = (\\text{tradename}, \\text{canonical\\_name}, \\text{owner}, \\text{status})$$

### 2.2 Registered Tradenames

| Tradename | Canonical Name | Owner |
|:---|:---|:---|
| AMOS | Autonomous Multi-Operational System | Trang Phan |
| Trang Framework | Recursive Ontology Dynamics | Trang Phan |
| UBI | Unified Biological Intelligence | Trang Phan |
| QLS | Quantum Logic Structure | Trang Phan |
| QCLA | Quantum Causality Layer Architecture | Trang Phan |
| TSS | The Trang System | Trang Phan |
| TPE | Trang Prediction Engine | Trang Phan |
| GMEF | Governed Mutation Evolution Framework | Trang Phan |
| ConsentX | Consent Arbitration Framework | Trang Phan |
| NeuroSyncAI | Neural Synchronization AI | Trang Phan |

### 2.3 Tradename Protection

Agents must not claim independent authorship of AMOS tradenames. All tradenames trace to Trang Phan.""",
    },
    "CANON_ALIAS_REGISTRY.md": {
        "title": "Canon Alias Registry",
        "id": "canon_alias_registry",
        "purpose": "The Canon Alias Registry records alternative names for canonical AMOS artifacts, ensuring search and reference consistency.",
        "content": """### 2.1 Alias Entry

$$\\text{Alias}(a) = (\\text{alias}, \\text{canonical\\_name}, \\text{type})$$

### 2.2 Registered Aliases

| Alias | Canonical Name | Type |
|:---|:---|:---|
| Full Brain OS | AMOS Brain Master OS | PRODUCT |
| Super Mind OS | AMOS Engines Master | PRODUCT |
| Omega Infinity Stack | Omega Quantum Stack | PRODUCT |
| Rule of Two | Rule of 2 (R2) | LAW |
| Rule of Four | Rule of 4 (R4) | LAW |
| Khung Trang | Trang Architecture | FRAMEWORK |
| Phuong Phap Trang | Trang Method | METHOD |
| MURK | Absolute Logic Kernel | COMPONENT |

### 2.3 Alias Resolution

All references using aliases must resolve to the canonical name. Unresolved aliases are UNKNOWN/GAP.""",
    },
    "CANON_HERITAGE_REGISTRY.md": {
        "title": "Canon Heritage Registry",
        "id": "canon_heritage_registry",
        "purpose": "The Canon Heritage Registry records heritage-related canonical artifacts, linking them to ancestral and civilizational sources.",
        "content": """### 2.1 Heritage Entry

$$\\text{Heritage}(h) = (\\text{artifact}, \\text{tradition}, \\text{era}, \\text{layer}, \\text{source\\_independence})$$

### 2.2 Heritage Layers

The 32-layer ancestral decision intelligence hierarchy is the canonical heritage structure.

### 2.3 Heritage Preservation

Heritage artifacts are preserved, not erased. Invalidated heritage is archived with full provenance.""",
    },
    "CANON_ACTIVE_LEGACY_MATRIX.md": {
        "title": "Canon Active vs Legacy Matrix",
        "id": "canon_active_legacy_matrix",
        "purpose": "The Canon Active vs Legacy Matrix provides a cross-reference view of which canonical artifacts are currently active versus legacy (superseded but preserved).",
        "content": """### 2.1 Matrix Entry

$$\\text{Matrix}(a) = (\\text{artifact}, \\text{version}, \\text{status}, \\text{active\\_or\\_legacy}, \\text{successor})$$

### 2.2 Active vs Legacy

| Status | Active/Legacy | Description |
|:---|:---|:---|
| ACTIVE | Active | Currently in use |
| CANON_LAW | Active | Fully canonical |
| SUBSTANTIVE_SPECIFICATION | Active | Has content, under review |
| SUPERSEDED | Legacy | Replaced, preserved |
| DEPRECATED | Legacy | Should not be used, preserved |

### 2.3 No Silent Legacy

Artifacts do not silently become legacy. The transition from active to legacy requires explicit supersession recording.""",
    },
    "CANON_COMPLETENESS_AUDIT.md": {
        "title": "Canon Completeness Audit",
        "id": "canon_completeness_audit",
        "purpose": "The Canon Completeness Audit records the completeness status of the AMOS canon, identifying gaps and missing artifacts.",
        "content": """### 2.1 Completeness Check

$$\\text{Complete}(\\text{Canon}) \\iff \\forall\\, s \\in \\text{Segments}, \\text{Populated}(s) \\wedge \\text{Validated}(s)$$

### 2.2 Segment Status

| Segment | Files | Placeholders | Substantive | Complete |
|:---|:---|:---|:---|:---|
| 01_CORE_LAWS | 36 | 0 (expanded) | 36 | YES |
| 02_UNIVERSE_CANON | 43 | varies | varies | IN PROGRESS |
| 03_COGNITION_CANON | 30 | varies | varies | IN PROGRESS |
| 04_INFRASTRUCTURE_CANON | 36 | varies | varies | IN PROGRESS |
| 05_VARIABLE_REGISTRY | 15 | 0 (expanded) | 15 | YES |
| 06_GLOSSARY | 16 | 0 (expanded) | 16 | YES |
| 07_PROVENANCE | 26 | 0 (expanded) | 26 | YES |
| 08_SUPERSESSION | 13 | 0 (expanded) | 13 | YES |
| 00_INDEX | 28 | 0 (expanded) | 28 | YES |

### 2.3 Gap Registration

Incomplete segments must have their gaps registered as UNKNOWN/GAP. No gap may be silently ignored.""",
    },
    "CANON_SOURCE_COVERAGE.md": {
        "title": "Canon Source Coverage",
        "id": "canon_source_coverage",
        "purpose": "The Canon Source Coverage audit records which canonical artifacts have provenance sources and which are missing provenance.",
        "content": """### 2.1 Coverage Entry

$$\\text{Coverage}(a) = (\\text{artifact}, \\text{has\\_source}, \\text{source\\_type}, \\text{independence})$$

### 2.2 Coverage Metrics

$$\\text{Coverage\\_Rate} = \\frac{|\\{a : \\text{has\\_source}(a)\\}|}{|\\text{Canon}|}$$

### 2.3 Minimum Coverage

All canonical artifacts must have at least one source. Artifacts without sources are UNKNOWN/GAP.""",
    },
    "CANON_COMPETING_DEFINITIONS.md": {
        "title": "Canon Competing Definitions",
        "id": "canon_competing_definitions",
        "purpose": "The Canon Competing Definitions registry records cases where multiple definitions exist for the same AMOS concept.",
        "content": """### 2.1 Competing Definition Entry

$$\\text{Competing}(c) = (\\text{concept}, \\text{definitions}, \\text{resolution\\_status}, \\text{authority})$$

### 2.2 Resolution Status

```text
UNRESOLVED:    no canonical definition chosen
RESOLVED:      one definition promoted to canonical
PARTIAL:       some aspects resolved
DEPRECATED:    all definitions deprecated
```

### 2.3 No Silent Resolution

Competing definitions must not be silently resolved. Resolution requires explicit authority and evidence.""",
    },
}

TEMPLATE = '''---
title: {title}
type: registry
source: 01_CANON/00_INDEX
artifact: {filename}
artifact_id: amos_01_canon_00_index_{id}
origin_architect: Trang Phan
steward: Trang Phan
system: AMOS OS
plane: 01_CANON
segment: 01_CANON/00_INDEX
artifact_kind: REGISTRY
path: 01_CANON/00_INDEX/{filename}
tags:
  - amos-os
  - canon
  - index
  - registry
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

`{filename}` defines the proposed AMOS OS **{title_short}**.

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

## 3. Cross-References

- [[01_CANON/00_INDEX/CANON_MAP|CANON_MAP]]
- [[01_CANON/00_INDEX/INDEX_CANON_README|INDEX_CANON_README]]
- [[01_CANON/01_CORE_LAWS/LAW_HIERARCHY|LAW_HIERARCHY]]
- [[00_ROOT/00_ROOT_MOC|00_ROOT_MOC]]

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

node_id: amos_01_canon_00_index_{id}

node_type: REGISTRY

path: 01_CANON/00_INDEX/{filename}

claim_class: AMOS_MODEL

rscf_state: DERIVED

canonical_status: CONDITIONAL

RSCF-RELATIONS:

- INDEXED_BY: [[00_ROOT/00_HOME|00_HOME]]

- INDEXED_BY: [[00_ROOT/AMOS_RSCF_NODES|AMOS_RSCF_NODES]]

- GOVERNED_BY: [[01_CANON/01_CORE_LAWS/LAW_HIERARCHY|LAW_HIERARCHY]]

______________________________________________________________________

**MOC:** [[01_CANON/00_INDEX/INDEX_CANON_README|INDEX_CANON_README]]
'''


def expand_file(filepath, content_def):
    filename = os.path.basename(filepath)
    title = content_def["title"]
    title_short = title.replace(" Registry", "").replace(" Matrix", "").replace(" Audit", "").replace(" Coverage", "").replace(" Index", "").replace(" Definitions", "")

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
    for filename, content_def in INDEX_FILES.items():
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
