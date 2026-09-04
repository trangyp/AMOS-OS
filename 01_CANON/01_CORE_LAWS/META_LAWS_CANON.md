---
canon-group: meta
canon-type: framework
rscf-state: source-claim
rscf-claim: verified
rscf-provenance: AMOS_corpus
conclusion_class: AMOS_MODEL
epistemic_class: SOURCE_CLAIM
topic: Meta Laws Canon
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

# Meta-Laws Canon

## 0. Status

`META_LAWS_CANON.md` defines the proposed AMOS OS **Meta-Laws** core law.

This artifact replaces a structural placeholder with substantive content. It does not, by its own existence, establish final AMOS canon, executable enforcement, empirical validity, or runtime implementation.

```text
PLACEHOLDER != IMPLEMENTED
ADDRESSABLE != VALIDATED
DOCUMENTED != ENFORCED
MODEL != OBSERVATION
SOURCE_CLAIM != VERIFIED
CANON_CANDIDATE != CANONICAL
CANONICAL != EMPIRICAL_TRUTH
CAPABILITY != AUTHORITY
AUTHORIZATION != COMMIT
PROPOSAL != COMMIT
IMPLEMENTED != VALIDATED
LOGGED != APPROVED
UNKNOWN/GAP != PASS
```

Origin architect / steward: **Trang Phan**

______________________________________________________________________

## 1. Purpose

The Meta-Laws Canon defines the AMOS OS requirements for laws that govern other laws. It establishes the hierarchy, precedence, and conflict resolution rules that apply when multiple AMOS laws interact or conflict.

Meta-laws answer:

> What governs the laws themselves? When laws conflict, which prevails? How are new laws created, validated, and promoted?

The Meta-Laws Canon states:

> **Every law in AMOS OS is governed by a higher-order law. The Law of Law (LoL) is the highest-order law: it requires that every system operate within a consistent set of structural constraints that cannot be violated without destabilizing the entire system. No law may contradict its governing meta-law.**

______________________________________________________________________

## 2. Formal Definition

### 2.1 Law Hierarchy

```text
LEVEL 0: Law of Law (LoL) — the law that governs all other laws
LEVEL 1: Rule of 2 (R2), Rule of 4 (R4) — foundational structural laws
LEVEL 2: L0-L32 core laws — domain-specific canonical laws
LEVEL 3: Domain canons — universe, cognition, infrastructure canons
LEVEL 4: Operational laws — runtime, control-plane, kernel laws
```

### 2.2 Precedence Rule

$$\text{Conflict}(L_i, L_j) \implies \text{Prevail}(\arg\max_{L \in \{L_i, L_j\}} \text{Level}(L))$$

When two laws conflict, the higher-level law prevails. Same-level conflicts require explicit resolution rules.

### 2.3 Law Creation Protocol

```text
1. PROPOSE:  new law is proposed with formal definition and scope
2. VALIDATE: law is validated against all higher-level meta-laws
3. TEST:     law is tested against negative cases and edge cases
4. PROMOTE:  law is promoted from PROPOSED to CONDITIONAL
5. ENFORCE:  law is promoted from CONDITIONAL to CANON_LAW (requires evidence)
```

### 2.4 Law Invalidation

A law may be invalidated if:
- It contradicts a higher-level meta-law
- Its premises are proven false
- Its consequences are proven harmful
- Its scope is proven incoherent

Invalidation preserves lineage — the invalidated law is archived, not erased.

______________________________________________________________________

## 3. Relationship to Other Core Laws

| Law | Relationship |
|:---|:---|
| **Law of Law (LoL)** | LoL is the highest meta-law; Meta-Laws Canon governs its application |
| **Rule of 2 (R2)** | R2 is a Level 1 law governed by LoL |
| **Rule of 4 (R4)** | R4 is a Level 1 law governed by LoL |
| **L0-L32** | All numbered core laws are Level 2, governed by R2/R4 and LoL |
| **GMEF Canon** | GMEF governs mutation of laws themselves |
| **Supersession** | Law invalidation follows supersession protocols |

______________________________________________________________________

## 4. Application Domains

### 4.1 Law Conflict Resolution

When two AMOS laws conflict:
- Identify the level of each law
- The higher-level law prevails
- Same-level conflicts require explicit resolution (e.g., scope disambiguation)
- The conflict and resolution are recorded with provenance

### 4.2 New Law Creation

When proposing a new AMOS law:
- Define the law formally with invariants
- Validate against all higher-level meta-laws
- Test against negative cases
- Promote through PROPOSED → CONDITIONAL → CANON_LAW
- Each promotion requires evidence and receipts

### 4.3 Law Evolution

When a law needs to change:
- The change is governed by GMEF (Governed Mutation Evolution Framework)
- The old law is archived, not erased (supersession)
- The new law inherits provenance from the old
- Dependencies are updated to reference the new law

### 4.4 Cross-System Law Application

When applying AMOS laws to external systems:
- Laws are AMOS_MODEL, not empirical truth
- Application requires scope declaration
- Results carry the epistemic class of the law, not higher

______________________________________________________________________

## 5. Worked Semantics

Given a conflict between laws $L_i$ (level $i$) and $L_j$ (level $j$):

1. **Identify levels** — determine $\text{Level}(L_i)$ and $\text{Level}(L_j)$
2. **Apply precedence** — if $i > j$, $L_i$ prevails; if $j > i$, $L_j$ prevails
3. **Same-level resolution** — if $i = j$, apply scope disambiguation or explicit resolution rule
4. **Record** — log the conflict and resolution with provenance
5. **Notify** — update all dependents that referenced the subordinate law

```text
conflict detected between L_i and L_j
  ↓
identify levels: Level(L_i) = i, Level(L_j) = j
  ↓
i > j?  ──yes──→  L_i prevails
  ↓ no
j > i?  ──yes──→  L_j prevails
  ↓ no (same level)
apply scope disambiguation
  ↓
record conflict resolution receipt
  ↓
notify dependents
```

______________________________________________________________________

## 6. Non-Purpose

This law MUST NOT be used to claim:
- universal laws of reality;
- scientific proof;
- empirical truth;
- runtime enforcement that has not been implemented;
- final canonical status;
- authority merely from architectural importance;
- or successful validation merely because the slot is addressable.

______________________________________________________________________

## 7. Gaps

- Executable binding NOT_ESTABLISHED — this law is specified but not yet enforced by runtime code
- Canonical status CONDITIONAL — proposed specification, not yet promoted to full canon
- Automated validation NOT_ESTABLISHED — automated enforcement is not implemented
- Cross-domain testing NOT_ESTABLISHED — testing across all AMOS domains is not complete

______________________________________________________________________

## 8. Promotion-Gate Checklist

- [x] substantive content populated from AMOS corpus sources
- [x] formal definition provided (§2)
- [x] relationship to other core laws documented (§3)
- [x] application domains specified (§4)
- [x] worked semantics defined (§5)
- [ ] typed schema bound to this artifact
- [ ] identity + versioning implemented
- [ ] negative cases covered (missing · malformed · stale · unauthorized input)
- [ ] provenance edges persisted and validated
- [ ] rollback basin demonstrated for consequential effects
- [ ] executed validation receipt specific to this artifact
- [ ] unresolved critical gaps registered as UNKNOWN/GAP (visible)

______________________________________________________________________

## 9. Cross-Plane Bindings

- Governed by — [[01_CANON/01_CORE_LAWS/LAW_HIERARCHY|LAW_HIERARCHY]] · [[01_CANON/01_CORE_LAWS/AMOS_CORE_LAWS|AMOS_CORE_LAWS]]
- Kernel enforcement — [[02_KERNEL/02_KERNEL_MOC|02_KERNEL_MOC]]
- Control-plane gates — [[03_CONTROL_PLANE/03_CONTROL_PLANE_MOC|03_CONTROL_PLANE_MOC]]
- Observed by — [[17_OBSERVABILITY/OBSERVABILITY_README|OBSERVABILITY_README]] · never treated as authority
- Recovered via — [[20_OPERATIONS/20_OPERATIONS_MOC|20_OPERATIONS_MOC]]

______________________________________________________________________

## 10. Ingestion Rule

```yaml
AMOS_CANON_INGESTION_RULE:
  existing_folder:
    preserve: true
  existing_file:
    preserve: true
    overwrite: false
  new_framework:
    action: ADD_FILE_TO_EXISTING_FOLDER
  master_source:
    action: NORMALIZE_TO_RSCF_FILE
  framework_existing_in_multiple_sources:
    action:
      - CREATE_ONE_CANONICAL_NODE
      - LINK_ALL_SOURCE_PROVENANCE
      - DO_NOT_CREATE_DUPLICATE_CANON
  historical_source:
    action:
      - LINK_TO_CANON
      - RECORD_LINEAGE
      - PRESERVE_HERITAGE
  external_research:
    action:
      - KEEP_OUT_OF_NATIVE_CANON
      - LINK_AS_EVIDENCE
  duplicate_filename:
    action:
      - COMPARE_CONTENT_AND_LINEAGE
      - DO_NOT_OVERWRITE
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

node_id: amos_01_canon_01_core_laws_meta_laws_canon

node_type: canon

path: 01_CANON/01_CORE_LAWS/META_LAWS_CANON.md

claim_class: AMOS_MODEL

rscf_state: SOURCE_CLAIM

canonical_status: CONDITIONAL

RSCF-RELATIONS:

- INDEXED_BY: [[00_ROOT/00_HOME|00_HOME]]

- INDEXED_BY: [[00_ROOT/AMOS_RSCF_NODES|AMOS_RSCF_NODES]]

- GOVERNED_BY: [[01_CANON/01_CORE_LAWS/LAW_HIERARCHY|LAW_HIERARCHY]]

______________________________________________________________________

**MOC:** [[01_CANON/01_CORE_LAWS/01_CORE_LAWS_MOC|01_CORE_LAWS_MOC]]
