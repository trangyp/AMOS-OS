---
canon-group: meta
canon-type: framework
rscf-state: source-claim
rscf-claim: verified
rscf-provenance: AMOS_corpus
conclusion_class: AMOS_MODEL
epistemic_class: SOURCE_CLAIM
topic: Atomic Reasoning Legacy
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

# Atomic Reasoning Legacy

## 0. Status

`ATOMIC_REASONING_LEGACY.md` defines the proposed AMOS OS **Atomic Reasoning** core law.

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

The Atomic Reasoning Legacy artifact preserves the historical formulation of AMOS atomic reasoning laws before their promotion to the L22 core law. It serves as a lineage record, not as active canon.

Atomic reasoning answers:

> What is the smallest unit of reasoning that can be independently validated, and what laws govern it?

The Atomic Reasoning Legacy states:

> **The smallest unit of reasoning is an atomic reasoning step: a single inference from premises to conclusion, with declared provenance, that can be independently validated. Atomic reasoning steps are the building blocks of all AMOS reasoning chains.**

______________________________________________________________________

## 2. Formal Definition

### 2.1 Atomic Reasoning Step

$$\text{AtomicStep}(p_1, \ldots, p_n \vdash c) \iff \text{SingleInference}(p_1, \ldots, p_n, c) \wedge \text{DeclaredProvenance}(c) \wedge \text{IndependentlyValidatable}(c)$$

### 2.2 Composition Law

$$\text{ReasoningChain} = \text{AtomicStep}_1 \circ \text{AtomicStep}_2 \circ \ldots \circ \text{AtomicStep}_n$$

A reasoning chain is a composition of atomic steps. Each step's conclusion becomes the next step's premise.

### 2.3 Validation Law

Each atomic step must be independently validatable:
- Premises are explicit and declared
- Inference rule is explicit and declared
- Conclusion follows from premises via the declared rule
- Provenance is complete and verifiable

______________________________________________________________________

## 3. Relationship to Other Core Laws

| Law | Relationship |
|:---|:---|
| **L22 Atomic Reasoning** | L22 is the promoted core law version of this legacy artifact |
| **L22 Replayability** | Atomic steps are required for deterministic replay |
| **L17 RSCF** | Atomic reasoning steps are the unit of RSCF claim discipline |
| **MURK Reasoning Engine** | MURK primitives are atomic reasoning units |

______________________________________________________________________

## 4. Application Domains

### 4.1 Reasoning Chain Construction

When building reasoning chains:
- Each step must be atomic (single inference)
- Premises must be explicit
- Provenance must be declared
- Each step must be independently validatable

### 4.2 Reasoning Validation

When validating reasoning:
- Validate each atomic step independently
- If any step fails, the chain fails at that point
- Dependent steps are invalidated, not the entire chain

### 4.3 Historical Reference

This artifact serves as:
- Lineage record for L22 Atomic Reasoning
- Reference for the original formulation
- Provenance anchor for the promotion to core law

______________________________________________________________________

## 5. Worked Semantics

Given a reasoning chain $C = s_1 \circ s_2 \circ \ldots \circ s_n$:

1. **Decompose** — verify $C$ is a composition of atomic steps
2. **Validate each step** — for each $s_i$, verify premises, inference rule, conclusion, provenance
3. **Check composition** — verify each step's conclusion is the next step's premise
4. **Identify failure point** — if any step fails, mark it and all dependent steps as invalid
5. **Record** — log the validation result with provenance

```text
reasoning chain C arrives
  ↓
decompose into atomic steps
  ↓
for each step s_i:
  verify premises are explicit
  verify inference rule is declared
  verify conclusion follows
  verify provenance is complete
  ↓
all steps valid?  ──no──→  mark failure point, invalidate dependents
  ↓ yes
chain is valid
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

node_id: amos_01_canon_01_core_laws_atomic_reasoning_legacy

node_type: canon

path: 01_CANON/01_CORE_LAWS/ATOMIC_REASONING_LEGACY.md

claim_class: AMOS_MODEL

rscf_state: SOURCE_CLAIM

canonical_status: CONDITIONAL

RSCF-RELATIONS:

- INDEXED_BY: [[00_ROOT/00_HOME|00_HOME]]

- INDEXED_BY: [[00_ROOT/AMOS_RSCF_NODES|AMOS_RSCF_NODES]]

- GOVERNED_BY: [[01_CANON/01_CORE_LAWS/LAW_HIERARCHY|LAW_HIERARCHY]]

______________________________________________________________________

**MOC:** [[01_CANON/01_CORE_LAWS/01_CORE_LAWS_MOC|01_CORE_LAWS_MOC]]
