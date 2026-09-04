---
canon-group: meta
canon-type: framework
rscf-state: source-claim
rscf-claim: verified
rscf-provenance: AMOS_corpus
conclusion_class: AMOS_MODEL
epistemic_class: SOURCE_CLAIM
topic: Sybil Hardening Spec
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

# JSON Specification

> Moved from SKILL.md for progressive loading.

```json
{
  "status": "passed_hardened_provenance_suite",
  "results": {
    "sybil_provenance_attacks": 5000,
    "sybil_incorrectly_dominant": 0,
    "provenance_cycles": "1000/1000 rejected",
    "missing_parent_graphs": "1000/1000 rejected",
    "same_id_evidence_equivocation": "1000/1000 rejected",
    "hot_resolution_mean_us_reported": 412.7,
    "hot_resolution_median_us_reported": 329.1,
    "hot_resolution_p95_us_reported": 647.5,
    "hot_resolution_throughput_per_sec_reported": 2423,
    "full_path_mean_us_reported": 605.4,
    "full_path_median_us_reported": 528.9,
    "full_path_p95_us_reported": 854.2,
    "full_path_throughput_per_sec_reported": 1652,
    "depth_3000": "FAIL RecursionError"
  }
}
```

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
node_id: amos-provenance-sybil-hardening-rscf-engine-sybil-hardening-spec
node_type: reference
path: 07_SKILLS/amos-provenance-sybil-hardening-rscf-engine/references/sybil_hardening_spec.md
RSCF-RELATIONS:

- INDEXED_BY: [[00_ROOT/00_HOME|00_HOME]]
- INDEXED_BY: [[00_ROOT/AMOS_RSCF_NODES|AMOS_RSCF_NODES]]
- CHILD_OF: references_MOC
