---
title: sybil hardening spec
type: reference
tags: [reference, amos-provenance-sybil-hardening-rscf-engine]
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
