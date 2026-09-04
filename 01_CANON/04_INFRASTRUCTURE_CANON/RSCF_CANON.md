---
canon-group: meta
canon-type: framework
rscf-state: source-claim
rscf-claim: verified
rscf-provenance: AMOS_corpus
conclusion_class: AMOS_MODEL
epistemic_class: SOURCE_CLAIM
topic: Rscf Canon
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

# RSCF Infrastructure Canon — Recursive Self-Consistent Format

> **Authoritative Canon Boundary**
>
> This document defines the canonical laws governing the **Recursive Self-Consistent Format (RSCF)**, the universal structural representation envelope of AMOS Core v4.4.
>
> ```text
> TEXT != STRUCTURED_CLAIM
> SELF_CONSISTENCY REQUIRES PROVENANCE CLOSURE
> EPISTEMIC CLASS IS NEVER OPTIONAL
> CONFIDENCE WITHOUT FALSIFIERS IS FABRICATION
> ```

---

## 1. Architectural Purpose

Unstructured markdown or natural language lacks computational parseability, invariant verification, and provenance traceability.

The **Recursive Self-Consistent Format (RSCF)** is the canonical data and knowledge encapsulation standard in AMOS Core v4.4. Every governed node in the vault must be self-contained, typed, versioned, provenance-tracked, and bound to explicit falsification criteria.

---

## 2. The Three-Layer RSCF Structural Envelope

Every compliant RSCF document consists of three mandatory structural layers:

```text
┌────────────────────────────────────────────────────────────┐
│ LAYER 1: STRICT YAML FRONTMATTER                           │
│ - Identity, Type, Source, Architect, Steward               │
│ - Status, Epistemic Class, Canonical Status                │
│ - RSCF Metadata Block: {state, claim_class, provenance}    │
├────────────────────────────────────────────────────────────┤
│ LAYER 2: BOUNDED DOCUMENTARY BODY                          │
│ - Markdown content structured by numbered sections         │
│ - Explicit Epistemic Boundary block (firewalls: A != B)    │
│ - Typed mathematical formulas and invariant definitions    │
├────────────────────────────────────────────────────────────┤
│ LAYER 3: RSCF-NODE FOOTER                                  │
│ - Node ID, Node Type, Plane, Domain                        │
│ - Confidence ceiling and explicit falsifiers               │
│ - RSCF-RELATIONS graph edges (INDEXED_BY, GOVERNED_BY)     │
└────────────────────────────────────────────────────────────┘
```

---

## 3. Canonical RSCF Invariants

### Law RSCF-01: Explicit Epistemic Typing
Every assertion in an RSCF node must carry an explicit epistemic classification:
- `OBSERVATION`: Raw, uninterpreted sensory or system telemetry;
- `SOURCE_CLAIM`: Unverified claim bound to a specific external paper/author;
- `AMOS_MODEL`: Internal theoretical framework or architectural design;
- `DERIVED`: Conclusion logically derived from verified premises;
- `COMPETING`: Multiple viable hypotheses under active evaluation;
- `UNKNOWN/GAP`: Missing knowledge or unverified premise.

### Law RSCF-02: Provenance Closure
No node may assert conclusions without recording an explicit list of parent provenance roots (`provenance: [parent_nodes]`). An orphan claim without provenance cannot be promoted beyond `SOURCE_CLAIM`.

### Law RSCF-03: Falsification Enclosure
Every authoritative RSCF specification must state at least one explicit falsifier: an empirical or logical condition under which the node's conclusions would be formally refuted.

---

## 4. Cross-Plane Bindings

- **`02_KERNEL/09_INTEGRATION/K_RSCF`**: Provides schema validation and serialization parsers.
- **`16_SCHEMAS`**: Defines YAML and JSON schemas for RSCF validation.
- **`17_OBSERVABILITY`**: Ingests RSCF node lineage graphs into the Provenance Graph family.

---

```RSCF-NODE
node_id: amos_01_canon_04_infrastructure_canon_rscf_canon
node_type: infrastructure_canon
plane: 01_CANON
domain: INFRASTRUCTURE
claim_class: CANONICAL_LAW
status: ACTIVE_CANON
confidence_ceiling: ABSOLUTE_FOR_CANONICAL_LAW
falsifiers:
  - Acceptance of an RSCF node lacking epistemic classification or provenance roots.
  - Silent omission of falsification conditions in an authoritative specification.
```
