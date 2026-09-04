---
canon-group: meta
canon-type: framework
rscf-state: source-claim
rscf-claim: verified
rscf-provenance: AMOS_corpus
conclusion_class: AMOS_MODEL
epistemic_class: SOURCE_CLAIM
topic: Provenance Integrity Canon
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

# Provenance Integrity Canon

## 0. Status

`PROVENANCE_INTEGRITY_CANON.md` defines the proposed AMOS OS **Provenance Integrity** core law.

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

The Provenance Integrity Canon defines the AMOS OS requirements for maintaining the integrity of provenance chains. It establishes the invariants that must hold for provenance to be considered trustworthy, and the conditions under which provenance integrity is violated.

Provenance integrity answers:

> What must be true for a provenance chain to be considered trustworthy, and what happens when provenance integrity is violated?

The Provenance Integrity Canon states:

> **A provenance chain has integrity if and only if it is complete (no missing links), tamper-evident (modifications are detectable), independently verifiable (verification does not depend on the source being verified), and fresh (not stale beyond declared validity). Provenance integrity violation is a fail-closed condition.**

______________________________________________________________________

## 2. Formal Definition

### 2.1 Provenance Integrity Invariant

$$\text{ProvenanceIntegrity}(P) \iff \text{Complete}(P) \wedge \text{TamperEvident}(P) \wedge \text{IndependentlyVerifiable}(P) \wedge \text{Fresh}(P)$$

### 2.2 Completeness

$$\text{Complete}(P) \iff \forall\, n \in P, \text{Source}(n) \neq \text{null} \wedge \text{Timestamp}(n) \neq \text{null} \wedge \text{Identity}(n) \neq \text{null}$$

Every node in the provenance chain must have a source, timestamp, and identity.

### 2.3 Tamper-Evidence

$$\text{TamperEvident}(P) \iff \forall\, n \in P, \exists\, h(n) : \text{Hash}(n) \text{ is cryptographically bound to } \text{Hash}(\text{pred}(n))$$

Each node's hash includes the hash of its predecessor, creating a tamper-evident chain.

### 2.4 Independent Verifiability

$$\text{IndependentlyVerifiable}(P) \iff \text{Verify}(P) \text{ does not require trust in any node in } P$$

### 2.5 Freshness

$$\text{Fresh}(P) \iff \text{Age}(P) \leq \text{ValidityWindow}(P)$$

______________________________________________________________________

## 3. Relationship to Other Core Laws

| Law | Relationship |
|:---|:---|
| **L2 Provenance** | L2 defines provenance laws; this canon governs their integrity |
| **Rule of 2 (R2)** | R2 requires source independence; provenance integrity requires independent verifiability |
| **Provenance Trust Firewall** | Enforces provenance integrity at the trust boundary |
| **L22 Replayability** | Provenance integrity is required for deterministic replay |

______________________________________________________________________

## 4. Application Domains

### 4.1 Knowledge Ingestion

When ingesting knowledge into the vault:
- Every claim must have complete provenance (source, timestamp, identity)
- Provenance chain must be tamper-evident (hash-chained)
- Verification must not depend on the source being verified
- Provenance must be fresh (within validity window)

### 4.2 Decision Recording

When recording decisions:
- Decision provenance must include all premises and their sources
- Provenance chain must be complete and tamper-evident
- Decision freshness must be within validity window

### 4.3 Memory Admission

When admitting to persistent memory:
- Memory entry provenance must be complete
- Provenance integrity must be verified before admission
- Stale provenance triggers revalidation or eviction

______________________________________________________________________

## 5. Worked Semantics

Given a provenance chain $P$ undergoing integrity validation:

1. **Check completeness** — verify every node has source, timestamp, identity
2. **Check tamper-evidence** — verify hash chain is intact
3. **Check independent verifiability** — verify that verification doesn't require trust in chain nodes
4. **Check freshness** — verify age is within validity window
5. **Classify** — if all pass, provenance integrity holds; if any fail, fail-closed
6. **Record** — log the validation result

```text
validate provenance chain P
  ↓
check completeness  ──fail──→  flag missing source/timestamp/identity
  ↓ pass
check tamper-evidence  ──fail──→  flag hash chain break
  ↓ pass
check independent verifiability  ──fail──→  flag circular trust
  ↓ pass
check freshness  ──fail──→  flag stale provenance
  ↓ pass
provenance integrity holds
  ↓
record validation receipt
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

node_id: amos_01_canon_01_core_laws_provenance_integrity_canon

node_type: canon

path: 01_CANON/01_CORE_LAWS/PROVENANCE_INTEGRITY_CANON.md

claim_class: AMOS_MODEL

rscf_state: SOURCE_CLAIM

canonical_status: CONDITIONAL

RSCF-RELATIONS:

- INDEXED_BY: [[00_ROOT/00_HOME|00_HOME]]

- INDEXED_BY: [[00_ROOT/AMOS_RSCF_NODES|AMOS_RSCF_NODES]]

- GOVERNED_BY: [[01_CANON/01_CORE_LAWS/LAW_HIERARCHY|LAW_HIERARCHY]]

______________________________________________________________________

**MOC:** [[01_CANON/01_CORE_LAWS/01_CORE_LAWS_MOC|01_CORE_LAWS_MOC]]
