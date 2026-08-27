---
title: causal discovery spec
type: reference
source: 07_SKILLS/amos-arxiv-multistage-order-causal-discovery-rscf/references
tags: [reference, amos-arxiv-multistage-order-causal-discovery-rscf, canon/skill]
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
  "status": "passed_epoch_finality_suite_then_hardened_for_omission_and_equivocation",
  "results": {
    "conflicting_certified_pairs": 20000,
    "arrival_order_dependent_final_states": 0,
    "deterministic_winner": "20000/20000",
    "late_transactions_admitted_closed_epoch": 0,
    "partial_visibility": 0,
    "pre_prepare_partition_cases": 10000,
    "false_commit_certificates": 0,
    "post_certificate_partition_recovery": 10000,
    "recovery_failures": 0,
    "byzantine_invalid_state_attacks": 10000,
    "forged_quorum_acceptance": 0,
    "optimized_distributed_mean_ms_reported": 0.35,
    "optimized_distributed_median_ms_reported": 0.31,
    "optimized_distributed_p95_ms_reported": 0.49,
    "optimized_distributed_p99_ms_reported": 0.88,
    "throughput_finalized_per_sec_reported": 2800,
    "compact_epoch_serialized_reduction_percent_approx": 62
  }
}
```

---
**MOC:** [[references_MOC]]

## Related

- [[07_SKILLS_MOC]]
