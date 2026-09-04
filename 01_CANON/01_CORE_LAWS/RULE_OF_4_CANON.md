---
canon-group: meta
canon-type: framework
rscf-state: source-claim
rscf-claim: verified
rscf-provenance: AMOS_corpus
conclusion_class: AMOS_MODEL
epistemic_class: SOURCE_CLAIM
topic: Rule Of 4 Canon
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

# Rule of 4 Canon

## 0. Status

`RULE_OF_4_CANON.md` defines the proposed AMOS OS **Rule of 4** core law.

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

The Rule of 4 (R4) is a foundational structural law in the AMOS OS core law hierarchy. It establishes the maximum decomposition width for any single level of abstraction in AMOS system design.

R4 answers:

> How many components may coexist at a single level of abstraction before the system becomes structurally unmanageable?

The Rule of 4 states:

> **Any system, subsystem, or reasoning layer MUST be decomposable into at most 4 components at any single level of abstraction. If more than 4 components appear, a new intermediate level MUST be introduced.**

This is the AMOS formalization of bounded cognitive complexity per layer. It prevents flat architectures that exceed human and agent comprehension capacity, and it enforces hierarchical depth over horizontal sprawl.

______________________________________________________________________

## 2. Formal Definition

### 2.1 R4 Invariant

$$\text{R4}: \quad \forall\, L \in \text{Layers}(S), \quad |\text{Components}(L)| \leq 4$$

Where:
- $\text{Layers}(S)$ — the set of abstraction layers in system $S$
- $\text{Components}(L)$ — the set of peer components at layer $L$
- The bound is 4, not "approximately 4" — a 5th component requires restructuring

### 2.2 Decomposition Rule

When a layer $L$ would contain $n > 4$ components:

```text
n > 4 ⇒ ∃ L' : Components(L') ⊂ Components(L)
      ∧ |Components(L')| ≤ 4
      ∧ L' is a new intermediate layer between L and its parent
```

The decomposition must preserve:
- **MECE property** — components at each layer are Mutually Exclusive and Collectively Exhaustive
- **Functional ownership** — each component has a single, clear functional responsibility
- **No hidden coupling** — inter-component dependencies are explicit and declared

### 2.3 AMOS Application

The AMOS OS itself follows R4 at its top level:

```text
AMOS OS Top Layer (4 components):
  1. CANON     — 01_CANON (laws, universe canon, cognition canon)
  2. KERNEL    — 02_KERNEL (cognition, causal, risk, memory, identity)
  3. CONTROL   — 03_CONTROL_PLANE (authority, policy, delegation)
  4. RUNTIME   — 04_RUNTIME (execution, observability, repair)
```

Each of these decomposes into at most 4 sub-components, and so on recursively.

______________________________________________________________________

## 3. Relationship to Other Core Laws

| Law | Relationship |
|:---|:---|
| **Law of Law (LoL)** | R4 is subordinate to LoL; LoL requires consistent structural constraints, R4 is the decomposition constraint |
| **Rule of 2 (R2)** | R2 governs epistemic independence; R4 governs structural decomposition. They are orthogonal but composable |
| **L0 Integrity** | R4 preserves structural integrity by preventing unbounded horizontal sprawl |
| **L5 Scope Regime** | R4 bounds the scope of any single layer, supporting scope regime enforcement |
| **L16 HML** | R4 applies at each H/M/L level — the 4-component limit is per-level, not global |

______________________________________________________________________

## 4. Application Domains

### 4.1 Architecture Design

When designing AMOS subsystems:
- Each layer may have at most 4 peer components
- A 5th component triggers mandatory restructuring
- New intermediate layers absorb overflow while preserving MECE property

### 4.2 Reasoning Decomposition

When decomposing a reasoning problem:
- A problem may be split into at most 4 sub-problems per level
- Each sub-problem inherits scope and provenance from its parent
- Deeper decomposition increases depth but not width

### 4.3 Agent Delegation

When delegating tasks to sub-agents:
- A parent agent may delegate to at most 4 direct child agents
- A 5th child requires introducing a coordinator agent layer
- This prevents fan-out explosion in multi-agent systems

### 4.4 Memory Organization

When organizing memory structures:
- Each memory tier may have at most 4 peer categories
- This supports efficient retrieval and bounded search width

______________________________________________________________________

## 5. Worked Semantics

Given a system $S$ with a layer $L$ containing $n$ components:

1. **Count components** — enumerate peer components at layer $L$
2. **Apply R4** — if $n \leq 4$, layer is compliant; if $n > 4$, restructure required
3. **Restructure** — group components into $\lceil n/4 \rceil$ clusters, each with $\leq 4$ members
4. **Insert intermediate layer** — the clusters become components of a new intermediate layer
5. **Verify MECE** — confirm the new structure preserves mutual exclusivity and collective exhaustiveness
6. **Record** — log the decomposition decision with provenance

```text
layer L has n components
  ↓
n ≤ 4?  ──yes──→  R4 compliant, proceed
  ↓ no
group into clusters of ≤ 4
  ↓
create intermediate layer L'
  ↓
assign clusters as components of L'
  ↓
verify MECE property
  ↓
record decomposition receipt
```

______________________________________________________________________

## 6. Non-Purpose

This law MUST NOT be used to claim:
- That 4 is always the optimal number (some layers may function well with 2 or 3)
- That depth is unlimited (other laws govern maximum depth)
- That R4 alone guarantees good architecture (MECE and functional ownership are also required)
- That R4 applies to leaves (terminal components are not subject to decomposition)
- That R4 overrides domain-specific architectural standards

______________________________________________________________________

## 7. Gaps

- Executable binding NOT_ESTABLISHED — R4 is specified but not yet enforced by runtime code
- Canonical status CONDITIONAL — proposed specification, not yet promoted to full canon
- Automated MECE verification NOT_ESTABLISHED — checking mutual exclusivity and collective exhaustiveness automatically is not implemented
- Cross-layer dependency analysis NOT_ESTABLISHED — verifying that R4 compliance at one layer doesn't create violations at another

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
- Kernel enforcement — [[02_KERNEL/02_KERNEL_MOC|02_KERNEL_MOC]] (structural reasoning)
- Control-plane gates — [[03_CONTROL_PLANE/03_CONTROL_PLANE_MOC|03_CONTROL_PLANE_MOC]] (delegation width)
- Cognitive matrix — [[25_COGNITIVE_MATRIX/25_COGNITIVE_MATRIX_MOC|25_COGNITIVE_MATRIX_MOC]] (decomposition validation)
- Observed by — [[17_OBSERVABILITY/OBSERVABILITY_README|OBSERVABILITY_README]] · never treated as authority
- Related skill — [[07_SKILLS/amos-rule-of-4-canon/SKILL|amos-rule-of-4-canon]]
- Related law — [[01_CANON/01_CORE_LAWS/RULE_OF_2_CANON|RULE_OF_2_CANON]] (orthogonal but composable)

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

node_id: amos_01_canon_01_core_laws_rule_of_4_canon

node_type: canon

path: 01_CANON/01_CORE_LAWS/RULE_OF_4_CANON.md

claim_class: AMOS_MODEL

rscf_state: SOURCE_CLAIM

canonical_status: CONDITIONAL

RSCF-RELATIONS:

- INDEXED_BY: [[00_ROOT/00_HOME|00_HOME]]

- INDEXED_BY: [[00_ROOT/AMOS_RSCF_NODES|AMOS_RSCF_NODES]]

- GOVERNED_BY: [[01_CANON/01_CORE_LAWS/LAW_HIERARCHY|LAW_HIERARCHY]]

- PAIRED_WITH: [[01_CANON/01_CORE_LAWS/RULE_OF_2_CANON|RULE_OF_2_CANON]]

______________________________________________________________________

**MOC:** [[01_CANON/01_CORE_LAWS/01_CORE_LAWS_MOC|01_CORE_LAWS_MOC]]
