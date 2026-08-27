---
title: AMOS V5 3 VERIFICATION REPORT
tags: [amos-general, amos, general]
type: data
source: 11_KNOWLEDGE/amos-general
---





```json
{
  "title": "AMOS v5.3 local verified successor benchmark",
  "classification": "VERIFIED_EXECUTED_LOCAL_SCOPE",
  "runtime": "/mnt/data/AMOS_CORE_v5_3_signed_recovery_authority_runtime.py",
  "runtime_sha256": "966c585f91bd7c0917389139acdabe4a8ae794108072eb7cb19fd8aa64091987",
  "parent": "v5.2",
  "falsified_parents": {
    "v5.1": "receipt-write failure allowed ambiguous duplicate replay after restart",
    "v5.2": "in-doubt abort resolution had no authenticated recovery authority"
  },
  "executed_results": {
    "v5_3_selftest": "5/5",
    "recovery_security_pytest": "5/5",
    "real_process_crash_boundaries": "3/3",
    "multiprocess_operations": "150/150",
    "multiprocess_prepare_records": 150,
    "multiprocess_receipt_records": 150,
    "artifact_ids_unique": true,
    "sequential_1000": {
      "throughput_ops_sec": 205.9971541555283,
      "mean_ms": 4.766457697,
      "median_ms": 3.956029,
      "p95_ms": 9.759397,
      "p99_ms": 15.790303
    },
    "public_only_human_key_verification": true
  },
  "external_material_used": [
    "Google Drive AMOS_CORE v4.1 Transactional Multi-RSCF Runtime",
    "Google Drive AMOS_CORE v4.2 Deterministic Causal Epoch Runtime",
    "GitHub sqlite/sqlite test/wal.test",
    "pytest 9.0.2",
    "filelock 3.29.0",
    "cryptography 46.0.4"
  ],
  "scope_boundaries": [
    "Single-host local filesystem/process/thread evidence only.",
    "PREPARE/IN_DOUBT prevents automatic duplicate retry; it does not prove exactly-once semantics for arbitrary external systems.",
    "File locking was not validated on network/distributed filesystems.",
    "Process death was simulated with os._exit at controlled code boundaries; physical power-loss/fsync hardware behavior was not tested.",
    "Recovery authority verifies configured Ed25519 key possession; no HSM/TPM or real-world identity attestation was tested.",
    "v5.3 is a local tested successor branch and does not rewrite the archived v3.0\u2192v4.4 canon lineage."
  ],
  "environment": {
    "python": "3.13.5",
    "platform": "Linux-6.18.35-x86_64-with-glibc2.41",
    "pytest": "9.0.2",
    "filelock": "3.29.0",
    "cryptography": "46.0.4"
  }
}

---
**Related:** [[00_HOME]] · [[KNOWLEDGE_MOC]] · [[AMOS_SIMULATION_KERNEL_V0_MATH_FOUNDATIONS]] · [[SYSTEM_SCAN_AGENT]] · [[AUTOMATION_PROFILES]]
```

---
**MOC:** [[AMOS-GENERAL_MOC]]
