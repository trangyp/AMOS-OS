---
title: sybil hardening spec
type: reference
source: 07_SKILLS/amos-provenance-sybil-hardening-rscf-engine/references
tags: [reference, amos-provenance-sybil-hardening-rscf-engine, canon/skill]
rscf:
  state: SOURCE_CLAIM
  claim_class: SOURCE_CLAIM
  provenance: AMOS_corpus
  scope: skill_reference
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

---
**MOC:** [[references_MOC]]

## Related

- [[07_SKILLS_MOC]]
---

**Related:** [[00_HOME]] · [[AMOS_RSCF_NODES]] · [[LAW_HIERARCHY]] · [[references_MOC]] · [[07_SKILLS_MOC]]

**MOC:** [[references_MOC]]

**Trang Framework:** [[TRANG_FRAMEWORK_RECURSIVE_ONTOLOGY_DYNAMICS]]

---
RSCF-NODE
node_id: amos-provenance-sybil-hardening-rscf-engine-sybil-hardening-spec
node_type: reference
path: 07_SKILLS/amos-provenance-sybil-hardening-rscf-engine/references/sybil_hardening_spec.md
RSCF-RELATIONS:
- INDEXED_BY: [[00_HOME]]
- INDEXED_BY: [[AMOS_RSCF_NODES]]
- CHILD_OF: [[references_MOC]]
