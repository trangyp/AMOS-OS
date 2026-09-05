---
canon-group: meta
canon-type: framework
rscf-state: source-claim
rscf-claim: verified
rscf-provenance: AMOS_corpus
conclusion_class: AMOS_MODEL
epistemic_class: SOURCE_CLAIM
topic: Rule Of 2 Canon
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

# Rule of 2 Canon

## 0. Status

`RULE_OF_2_CANON.md` defines the proposed AMOS OS **Rule of 2** core law.

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

The Rule of 2 (R2) is a foundational epistemic law in the AMOS OS core law hierarchy. It establishes the minimum independence requirement for treating a claim, decision, or belief as reliable enough to act upon.

R2 answers:

> How many independent sources must corroborate a claim before it may be treated as actionable?

The Rule of 2 states:

> **A claim, decision, or belief requires corroboration by at least two independent sources before it may be treated as reliable enough to act upon.**

This is the AMOS formalization of the "Trang Tát 2" principle — confirmation by at least two independent sources. It is not a "re-check" (verifying the same source twice). It is a requirement of **source independence**: the two sources must not share origin, dependency, or provenance lineage.

______________________________________________________________________

## 2. Formal Definition

### 2.1 R2 Invariant

$$\text{R2}: \quad \text{Actionable}(c) \implies \exists\, s_1, s_2 \in \text{Sources}(c) \;.\; \text{Independent}(s_1, s_2)$$

Where:
- $\text{Actionable}(c)$ — claim $c$ may be used as a premise for consequential action
- $\text{Sources}(c)$ — the set of sources providing evidence for $c$
- $\text{Independent}(s_1, s_2)$ — sources $s_1$ and $s_2$ have no shared origin, no shared dependency, and no shared provenance lineage

### 2.2 Independence Test

Two sources $s_1, s_2$ are independent if and only if:

```text
¬Shared_origin(s1, s2)
∧ ¬shared_dependency(s1, s2)
∧ ¬shared_provenance_lineage(s1, s2)
∧ ¬one_origin_represented_as_many(s1, s2)
```

This is enforced by the AMOS Sybil Hardening kernel contract ([[02_KERNEL/08_PROVENANCE/K_SYBIL_HARDENING|K_SYBIL_HARDENING]]]]), which prevents apparent multiplicity from being mistaken for independent epistemic support.

### 2.3 Failure Mode

If only one source is available, or if two sources share origin/dependency/provenance:

```text
R2_violation ⇒ ¬Actionable(c)
             ⇒ c retains state SOURCE_CLAIM or OBSERVATION
             ⇒ c MUST NOT be promoted to DERIVED or DECISION
             ⇒ consequential action MUST be deferred or escalated
```

______________________________________________________________________

## 3. Relationship to Other Core Laws

| Law | Relationship |
|:---|:---|
| **Law of Law (LoL)** | R2 is subordinate to LoL; LoL requires every system to operate within consistent structural constraints, R2 is one such constraint |
| **Rule of 4 (R4)** | R2 governs epistemic independence; R4 governs structural decomposition. They are orthogonal but composable |
| **L1 Epistemic** | R2 is the independence floor for L1 epistemic classification — a single-source claim cannot be promoted above SOURCE_CLAIM |
| **L17 RSCF** | R2 governs the minimum provenance independence for RSCF claim discipline |
| **L27 Gap Law** | When R2 cannot be satisfied, the claim MUST be registered as a GAP, not silently filled |

______________________________________________________________________

## 4. Application Domains

### 4.1 Knowledge Ingestion

When ingesting external research or claims into the AMOS knowledge plane:
- A single paper/source = SOURCE_CLAIM, not DERIVED
- Two independent papers = may be classified as DERIVED with confidence ceiling
- Two papers from the same lab/group = NOT independent (Sybil risk)

### 4.2 Decision Making

Before a consequential decision may be committed:
- The decision premise must be supported by ≥2 independent sources
- If only one source exists, the decision MUST be escalated or deferred
- This is enforced by the control-plane commit gate

### 4.3 Memory Admission

When admitting information to persistent AMOS memory:
- Single-source observations enter as OBSERVATION state
- Two-source corroborated observations may enter as DERIVED
- The memory admission kernel ([[02_KERNEL/05_MEMORY/K_MEMORY_ADMISSION|K_MEMORY_ADMISSION]]]]) enforces R2 at admission time

### 4.4 Provenance Validation

When validating provenance chains:
- R2 requires that provenance independence be verified, not assumed
- Two citations to the same original source = NOT independent
- This is enforced by the provenance trust firewall ([[17_OBSERVABILITY/PROVENANCE_TRUST_FIREWALL|PROVENANCE_TRUST_FIREWALL]])

______________________________________________________________________

## 5. Worked Semantics

Given a claim $c$ proposed for actionable status:

1. **Enumerate sources** — collect all sources providing evidence for $c$
2. **Test independence** — for each pair $(s_i, s_j)$, evaluate the independence test (§2.2)
3. **Apply R2** — if ≥1 independent pair exists, $c$ may be promoted to actionable; otherwise, $c$ retains its current state
4. **Record receipt** — log the independence determination with provenance
5. **Fail closed** — on any uncertainty about independence, treat as R2 violation

```text
claim c arrives
  ↓
enumerate Sources(c)
  ↓
|Sources(c)| < 2?  ──yes──→  ¬Actionable(c), register GAP
  ↓ no
test all pairs for Independence(s_i, s_j)
  ↓
∃ independent pair?  ──no──→  ¬Actionable(c), flag Sybil risk
  ↓ yes
c MAY be promoted to Actionable
  ↓
record independence receipt with provenance
```

______________________________________________________________________

## 6. Non-Purpose

This law MUST NOT be used to claim:
- That two sources are always sufficient (some domains require more)
- That independence is binary (it may be partial or uncertain)
- That R2 alone guarantees truth (it is necessary, not sufficient)
- That mechanical citation counting satisfies R2 (independence is the requirement, not count)
- That R2 overrides domain-specific evidence standards (medical, legal, safety domains may require higher thresholds)

______________________________________________________________________

## 7. Gaps

- Executable binding NOT_ESTABLISHED — R2 is specified but not yet enforced by runtime code
- Canonical status CONDITIONAL — proposed specification, not yet promoted to full canon
- Independence oracle NOT_ESTABLISHED — automated independence testing between arbitrary sources is not implemented
- Partial independence modeling NOT_ESTABLISHED — the binary independence test may be too coarse for real-world provenance graphs

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
- Kernel enforcement — [[02_KERNEL/08_PROVENANCE/K_SYBIL_HARDENING|K_SYBIL_HARDENING]]]] · [[02_KERNEL/05_MEMORY/K_MEMORY_ADMISSION|K_MEMORY_ADMISSION]]]]
- Control-plane gates — [[03_CONTROL_PLANE/04_AUTHORITY|04_AUTHORITY]] (commit gate enforces R2)
- Knowledge plane — [[11_KNOWLEDGE/00_INDEX/KNOWLEDGE_MAP|KNOWLEDGE_MAP]] (ingestion enforces R2)
- Observed by — [[17_OBSERVABILITY/OBSERVABILITY_README|OBSERVABILITY_README]] · never treated as authority
- Related skill — [[07_SKILLS/amos-rule-of-2-canon/SKILL|amos-rule-of-2-canon]]
- Related law — [[01_CANON/01_CORE_LAWS/RULE_OF_4_CANON|RULE_OF_4_CANON]] (orthogonal but composable)
- Related concept — [[07_SKILLS/amos-trang-tat-2/SKILL|Trang Tát 2]] (Vietnamese formulation)

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

node_id: amos_01_canon_01_core_laws_rule_of_2_canon

node_type: canon

path: 01_CANON/01_CORE_LAWS/RULE_OF_2_CANON.md

claim_class: AMOS_MODEL

rscf_state: SOURCE_CLAIM

canonical_status: CONDITIONAL

RSCF-RELATIONS:

- INDEXED_BY: [[00_ROOT/00_HOME|00_HOME]]

- INDEXED_BY: [[00_ROOT/AMOS_RSCF_NODES|AMOS_RSCF_NODES]]

- GOVERNED_BY: [[01_CANON/01_CORE_LAWS/LAW_HIERARCHY|LAW_HIERARCHY]]

- PAIRED_WITH: [[01_CANON/01_CORE_LAWS/RULE_OF_4_CANON|RULE_OF_4_CANON]]

- ENFORCED_BY: [[02_KERNEL/08_PROVENANCE/K_SYBIL_HARDENING|K_SYBIL_HARDENING]]]]

______________________________________________________________________

**MOC:** [[01_CANON/01_CORE_LAWS/01_CORE_LAWS_MOC|01_CORE_LAWS_MOC]]
