---
canon-group: meta
canon-type: framework
rscf-state: source-claim
rscf-claim: verified
rscf-provenance: AMOS_corpus
conclusion_class: AMOS_MODEL
epistemic_class: SOURCE_CLAIM
topic: Ubi Integrity Policy
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

# UBI Integrity Policy

## 0. Status

`UBI_INTEGRITY_POLICY.md` defines the proposed AMOS OS **UBI Integrity**.

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

The UBI Integrity Policy enforces the non-compensatory biological intelligence integrity requirements.

______________________________________________________________________

## 2. Formal Definition

### 2.1 UBI Integrity Rules

| Rule | Enforcement |
|:---|:---|
| Non-compensatory | Reject any attempt to compensate one domain with another |
| Substrate distress | Veto all actions when τ < 0.2 |
| Domain independence | Each domain (NBI, NEI, SI, BEI) scored independently |
| Composite score | UBI_total = min(NBI, NEI, SI, BEI) |

### 2.2 Integrity Invariant

$$\text{UBI}_{\text{total}} = \min(\text{NBI}, \text{NEI}, \text{SI}, \text{BEI})$$

This invariant must be preserved by all policies. No policy may weaken the non-compensatory property.

### 2.3 Veto Authority

The UBI integrity veto (substrate distress) is absolute. No authority can override it.

______________________________________________________________________

## 3. Cross-References

- [[03_CONTROL_PLANE/03_CONTROL_PLANE_MOC|03_CONTROL_PLANE_MOC]]
- [[01_CANON/01_CORE_LAWS/LAW_HIERARCHY|LAW_HIERARCHY]]
- [[00_ROOT/00_ROOT_MOC|00_ROOT_MOC]]

______________________________________________________________________

## 4. Gaps

- Executable binding NOT_ESTABLISHED
- Canonical status CONDITIONAL
- Automated enforcement NOT_ESTABLISHED

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

node_id: amos_03_control_plane_ubi_integrity_policy

node_type: CONTRACT

path: 03_CONTROL_PLANE/03_POLICY/UBI_INTEGRITY_POLICY.md

claim_class: AMOS_MODEL

rscf_state: DERIVED

canonical_status: CONDITIONAL

RSCF-RELATIONS:

- INDEXED_BY: [[00_ROOT/00_HOME|00_HOME]]

- INDEXED_BY: [[00_ROOT/AMOS_RSCF_NODES|AMOS_RSCF_NODES]]

- GOVERNED_BY: [[01_CANON/01_CORE_LAWS/LAW_HIERARCHY|LAW_HIERARCHY]]

______________________________________________________________________

**MOC:** [[03_CONTROL_PLANE/03_CONTROL_PLANE_MOC|03_CONTROL_PLANE_MOC]]
