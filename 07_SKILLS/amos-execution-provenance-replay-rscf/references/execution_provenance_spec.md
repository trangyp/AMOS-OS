---
title: execution provenance spec
type: reference
source: 07_SKILLS/amos-execution-provenance-replay-rscf/references
tags: [reference, amos-execution-provenance-replay-rscf, canon/skill]
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
  "status": "passed_incremental_locality_then_failed_overlapping_concurrency",
  "results": {
    "million_node_single_add_mean_ms": 0.019,
    "million_node_single_add_median_ms": 0.0097,
    "million_node_single_add_p95_ms": 0.061,
    "leaf_mutation_mean_ms": 0.036,
    "leaf_mutation_median_ms": 0.023,
    "leaf_mutation_p95_ms": 0.072,
    "affected_cone_5000_update_ms": 1.73,
    "global_root_change_1001000_nodes_ms": 368,
    "semantic_regression_random_DAGs": "0 mismatches / 2000",
    "independent_concurrent_additions": "100000/100000",
    "independent_append_throughput_8_threads_per_sec": 84105,
    "overlapping_conflict_trials": 2000,
    "schedule_dependent_winner_distribution": {
      "A": 977,
      "B": 1023
    }
  }
}
```

---
**MOC:** [[references_MOC]]

## Related

- [[07_SKILLS_MOC]]
