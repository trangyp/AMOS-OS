---
canon-group: meta
canon-type: framework
rscf-state: source-claim
rscf-claim: verified
rscf-provenance: AMOS_corpus
conclusion_class: AMOS_MODEL
epistemic_class: SOURCE_CLAIM
topic: Amos Framework Glossary
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

# AMOS Framework Glossary

## 0. Status

`AMOS_FRAMEWORK_GLOSSARY.md` defines the proposed AMOS OS **AMOS Framework** glossary.

This artifact replaces a structural placeholder with substantive content.

```text
PLACEHOLDER != IMPLEMENTED
ADDRESSABLE != VALIDATED
DOCUMENTED != ENFORCED
MODEL != OBSERVATION
SOURCE_CLAIM != VERIFIED
CANON_CANDIDATE != CANONICAL
CANONICAL != EMPIRICAL_TRUTH
CAPABILITY != AUTHORITY
UNKNOWN/GAP != PASS
```

Origin architect / steward: **Trang Phan**

______________________________________________________________________

## 1. Purpose

The AMOS Framework Glossary defines the canonical terminology used across the AMOS OS framework — covering core architectural concepts, structural primitives, and governance mechanisms.

______________________________________________________________________

## 2. Term Definitions

| Term | Definition | Category |
|:---|:---|:---|
| AMOS | Autonomous Multi-Operational System — the complete cognitive architecture | Core |
| Canon | Canonical law or principle that governs a domain of the system | Governance |
| Core Law | Foundational law in the L0-L32 law hierarchy | Governance |
| Kernel | The runtime kernel that enforces canonical laws during execution | Runtime |
| Control Plane | The plane that manages authority, delegation, and policy | Governance |
| Runtime | The execution engine that carries out governed operations | Runtime |
| RSCF | Reasoning-Source-Claim-Freshness — epistemic classification framework | Epistemic |
| HML | High/Mid/Low — three-speed validation lens for claim rigor | Epistemic |
| MECE | Mutually Exclusive, Collectively Exhaustive — structural property | Architecture |
| GMEF | Governed Mutation Evolution Framework — governs system self-modification | Evolution |
| MOC | Map of Content — navigational index for a vault section | Navigation |
| Plane | A top-level architectural division (Canon, Kernel, Control, Runtime) | Architecture |
| Segment | A sub-division within a plane | Architecture |
| Artifact | A typed, provenance-stamped document in the vault | Structure |
| Receipt | A cryptographic record of a consequential action | Audit |
| Checkpoint | A verified state snapshot for recovery | Recovery |
| Epoch | A causal epoch — a validity interval for causal state | Causality |
| Shard | A locally-finalized partition of system state | Distributed |
| MVCC | Multi-Version Concurrency Control | Concurrency |
| CAS | Compare-And-Swap — atomic concurrency primitive | Concurrency |
| ALU | Absolute Logic Unit — irreducible logic primitive (19 total) | Logic |
| UML | Universal Meta-Law — governing meta-law (7 total) | Logic |
| UOP | Universal Operator Primitive — operational primitive (6 total) | Logic |
| LoL | Law of Law — the highest-order meta-law | Logic |
| R2 | Rule of 2 — minimum 2 independent sources for actionable claims | Epistemic |
| R4 | Rule of 4 — maximum 4 components per abstraction layer | Architecture |
| UBI | Unified Biological Intelligence — 4-domain biological model | Biology |
| QLS | Quantum Logic Structure — superposition reasoning framework | Quantum |
| QCLA | Quantum Causality Layer Architecture — quantum causal model | Quantum |
| FRAI | Fractal Reasoning AI — recursive self-similar reasoning | Reasoning |
| TSS | The Trang System — governance and institutional framework | Governance |
| TPE | Trang Prediction Engine — foresight and prediction system | Reasoning |

______________________________________________________________________

## 3. Usage Notes

- All terms in this glossary are AMOS_MODEL unless otherwise stated
- Terms marked as "Core" are foundational to the framework
- Terms marked as "Alias" are alternative names for canonical terms
- Terms marked as "Crosswalk" map concepts across different canons
- No term in this glossary should be interpreted as empirical truth

______________________________________________________________________

## 4. Cross-References

- See [[01_CANON/06_GLOSSARY/CANONICAL_GLOSSARY|CANONICAL_GLOSSARY]] for the master glossary
- See [[01_CANON/06_GLOSSARY/CANON_ALIASES|CANON_ALIASES]] for canonical aliases
- See [[01_CANON/06_GLOSSARY/DEPRECATED_TERMS|DEPRECATED_TERMS]] for deprecated terminology
- See [[01_CANON/05_VARIABLE_REGISTRY/UNIVERSAL_VARIABLE_REGISTRY|UNIVERSAL_VARIABLE_REGISTRY]] for variable definitions

______________________________________________________________________

## 5. Gaps

- Canonical status CONDITIONAL — proposed specification, not yet promoted to full canon
- Cross-glossary consistency validation NOT_ESTABLISHED
- Automated term resolution NOT_ESTABLISHED

______________________________________________________________________

## 6. Ingestion Rule

```yaml
AMOS_CANON_INGESTION_RULE:
  existing_folder:
    preserve: true
  existing_file:
    preserve: true
    overwrite: false
  new_framework:
    action: ADD_FILE_TO_EXISTING_FOLDER
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

node_id: amos_01_canon_06_glossary_amos_framework_glossary

node_type: glossary

path: 01_CANON/06_GLOSSARY/AMOS_FRAMEWORK_GLOSSARY.md

claim_class: AMOS_MODEL

rscf_state: DERIVED

canonical_status: CONDITIONAL

RSCF-RELATIONS:

- INDEXED_BY: [[00_ROOT/00_HOME|00_HOME]]

- INDEXED_BY: [[00_ROOT/AMOS_RSCF_NODES|AMOS_RSCF_NODES]]

- GOVERNED_BY: [[01_CANON/01_CORE_LAWS/LAW_HIERARCHY|LAW_HIERARCHY]]

______________________________________________________________________

**MOC:** [[01_CANON/06_GLOSSARY/06_GLOSSARY_MOC|06_GLOSSARY_MOC]]
