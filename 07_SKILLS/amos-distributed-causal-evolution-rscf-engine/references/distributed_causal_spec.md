---
title: distributed causal spec
type: reference
tags: [reference, amos-distributed-causal-evolution-rscf-engine]
---

# JSON Specification

> Moved from SKILL.md for progressive loading.

```json
{
  "status": "passed_distributed_causal_suite",
  "results": {
    "concurrent_pairs": 100000,
    "same_target_conflicts": 33374,
    "order_dependent_final_states": 0,
    "stale_parent_mutations": 50000,
    "stale_accepted": 0,
    "retarget_value_tamper_attacks": 50000,
    "tamper_accepted": 0,
    "duplicate_delivery": 25000,
    "duplicate_divergence": 0,
    "partition_heal": 20000,
    "post_heal_failures": 0,
    "byzantine_attacks": 40000,
    "byzantine_escapes": 0,
    "logic_regression_mismatches_10000": 0
  }
}
```

---
**MOC:** [[references_MOC]]
