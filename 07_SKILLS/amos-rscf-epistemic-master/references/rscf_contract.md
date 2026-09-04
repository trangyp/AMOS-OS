---
canon-group: meta
canon-type: framework
rscf-state: source-claim
rscf-claim: verified
rscf-provenance: AMOS_corpus
conclusion_class: AMOS_MODEL
epistemic_class: SOURCE_CLAIM
topic: Rscf Contract
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

# RSCF Contract — Canonical Schema

> Source: `_00_Cosmo brain/rscf/rscf.md` from the AMOS_OS Obsidian vault.
> Epistemic class: SOURCE_CANON

## RSCF YAML Schema

```yaml
claim_id: stable-id
claim: concise proposition
class: VERIFIED | DERIVED | MODEL | CONDITIONAL | COMPETING | UNKNOWN/GAP
scale: H | M | L
premises: []
evidence: []
provenance:
  ancestry: []
  independence_status: demonstrated | correlated | unknown
scope:
  system_or_population: null
  environment: null
  scale: null
  time_window: null
  measurement_method: null
  assumptions: []
regime:
  id: null
  validity_conditions: []
freshness:
  observed_at: null
  revalidate_at: null
dependencies: []
competing_hypotheses: []
falsifiers: []
confidence_ceiling: 0.0
decision_relevance: low | medium | high
```

## RSCF Invariants

1. Confidence cannot exceed the weakest load-bearing premise without independent revalidation.
1. Descendants of one source are correlated provenance, not independent confirmation.
1. Scope, regime, and freshness propagate to dependent claims.
1. Structural similarity never proves causation.
1. Equal/incomparable support remains COMPETING.
1. Failed premises invalidate only dependent descendants.
1. Framework equations remain MODEL unless independently validated.

## 6 State Kinds

- **OBSERVATION**: Directly measured, empirically grounded.
- **SOURCE_CLAIM**: Sourced from a canonical reference, not independently verified.
- **DERIVED**: Logically derived from premises and evidence.
- **MODEL**: Framework assertion, not empirically validated.
- **CONDITIONAL**: Valid only under stated regime conditions.
- **COMPETING**: Equal/incomparable support, no dominant hypothesis.
- **UNKNOWN/GAP**: Insufficient evidence to classify.

______________________________________________________________________

**MOC:** references_MOC

## Related

- [[07_SKILLS/07_SKILLS_MOC|07_SKILLS_MOC]]

______________________________________________________________________

**Related:** [[00_ROOT/00_HOME|00_HOME]] · [[00_ROOT/AMOS_RSCF_NODES|AMOS_RSCF_NODES]] · [[01_CANON/01_CORE_LAWS/LAW_HIERARCHY|LAW_HIERARCHY]] · references_MOC · [[07_SKILLS/07_SKILLS_MOC|07_SKILLS_MOC]]

**MOC:** references_MOC

**Trang Framework:** [[11_KNOWLEDGE/TRANG_FRAMEWORK_RECURSIVE_ONTOLOGY_DYNAMICS|TRANG_FRAMEWORK_RECURSIVE_ONTOLOGY_DYNAMICS]]

______________________________________________________________________

RSCF-NODE
node_id: amos-rscf-epistemic-master-rscf-contract
node_type: reference
path: 07_SKILLS/amos-rscf-epistemic-master/references/rscf_contract.md
RSCF-RELATIONS:

- INDEXED_BY: [[00_ROOT/00_HOME|00_HOME]]
- INDEXED_BY: [[00_ROOT/AMOS_RSCF_NODES|AMOS_RSCF_NODES]]
- CHILD_OF: references_MOC
