---
title: V4 2 CAUSAL EPOCH
tags: [misc, reference, general]
type: document
source: 11_KNOWLEDGE/misc
---




# v4.2 — Deterministic Causal Epoch Runtime

## Focus
- quorum certification
- causal epochs
- closed membership
- deterministic conflict ordering
- compact epoch encoding

## Markdown brain adaptation
Use epoch-style finality for conflicting coordinated updates when independence cannot be proven.

## Historical gap
Caller-supplied shard subset could omit touched shard; transaction-ID equivocation across disjoint payloads.

## Benchmark boundary
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

Benchmark results are preserved only within their tested operationalization and are not universal guarantees.

---
**Related:** [[00_HOME]] · [[KNOWLEDGE_MOC]] · [[AMOS_SIMULATION_KERNEL_V0_MATH_FOUNDATIONS]] · [[SYSTEM_SCAN_AGENT]] · [[AUTOMATION_PROFILES]]

---
**MOC:** [[MISC_MOC]]
