---
canon-group: meta
canon-type: framework
rscf-state: source-claim
rscf-claim: verified
rscf-provenance: AMOS_corpus
conclusion_class: AMOS_MODEL
epistemic_class: SOURCE_CLAIM
topic: Ubi Glossary
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

# UBI Glossary

## 0. Status

`UBI_GLOSSARY.md` defines the proposed AMOS OS **UBI** glossary.

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

The UBI (Unified Biological Intelligence) Glossary defines terminology for the 4 non-compensatory biological intelligence domains and their integration into cognitive architecture.

______________________________________________________________________

## 2. Term Definitions

| Term | Definition | Category |
|:---|:---|:---|
| UBI | Unified Biological Intelligence — 4-domain biological model | Core |
| NBI | Neurobiological Intelligence — cognitive, perceptual, executive function | Domain |
| NEI | Neuroemotional Intelligence — emotional awareness, autonomic balance | Domain |
| SI | Somatic Intelligence — body awareness, interoceptive accuracy | Domain |
| BEI | Bioelectromagnetic Intelligence — cardiac electromagnetic coherence | Domain |
| Non-compensatory | No domain can compensate for deficiency in another | Property |
| Substrate Distress | Biological substrate under harmful stress (τ < 0.2) | Safety |
| Quadratic Emergence | e = i² — emergence from interaction is quadratic | Model |
| 40Hz Clock | Gamma-band multi-agent synchronization frequency | Synchronization |
| Vagal Coherence | Autonomic nervous system balance measure [0,1] | Physiology |
| Cognitive Load | Current cognitive resource utilization [0,1] | Cognition |
| ConsentX | Consent arbitration rooted in biological law and autonomic alignment | Governance |
| UBI Score | Composite biological intelligence score = min(NBI, NEI, SI, BEI) | Measurement |
| Wearable Telemetry | Continuous physiological monitoring interface | Interface |

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

node_id: amos_01_canon_06_glossary_ubi_glossary

node_type: glossary

path: 01_CANON/06_GLOSSARY/UBI_GLOSSARY.md

claim_class: AMOS_MODEL

rscf_state: DERIVED

canonical_status: CONDITIONAL

RSCF-RELATIONS:

- INDEXED_BY: [[00_ROOT/00_HOME|00_HOME]]

- INDEXED_BY: [[00_ROOT/AMOS_RSCF_NODES|AMOS_RSCF_NODES]]

- GOVERNED_BY: [[01_CANON/01_CORE_LAWS/LAW_HIERARCHY|LAW_HIERARCHY]]

______________________________________________________________________

**MOC:** [[01_CANON/06_GLOSSARY/06_GLOSSARY_MOC|06_GLOSSARY_MOC]]
