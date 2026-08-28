---
title: V4 1 ATOMIC MULTI RSCF
tags:
- rscf
- epistemic
- claim
- canon/knowledge
type: document
source: 11_KNOWLEDGE/rscf
rscf:
  state: SOURCE_CLAIM
  claim_class: EMPIRICAL
  provenance: AMOS_corpus
  scope: epistemic_framework
---


# v4.1 — Transactional Multi-RSCF Runtime

## Focus
- transaction IDs
- read/write sets
- transaction-level CAS
- atomic publication
- cross-RSCF invariants
- all-or-nothing rollback

## Markdown brain adaptation
Treat cross-RSCF update sets atomically: all-or-nothing.

## Historical gap
Distributed transaction finality under partition and competing certified transactions.

## Benchmark boundary
```json
{
  "status": "passed_transactional_multi_RSCF_suite",
  "results": {
    "overlapping_transaction_trials": 2000,
    "partial_mixed_states": 0,
    "schedule_dependent_final_states": 0,
    "atomicity_violations": 0,
    "write_skew_violations_accepted": 0,
    "forced_partial_failure_rollback": "passed",
    "transaction_sizes_passed": [
      3,
      10,
      100,
      1000
    ],
    "historical_snapshot_readers": "passed"
  }
}
```

Benchmark results are preserved only within their tested operationalization and are not universal guarantees.

---
**Related:** [[00_HOME]] · [[KNOWLEDGE_MOC]] · [[AMOS_SIMULATION_KERNEL_V0_MATH_FOUNDATIONS]] · [[SYSTEM_SCAN_AGENT]] · [[AUTOMATION_PROFILES]]

---
**MOC:** [[rscf_MOC]]
