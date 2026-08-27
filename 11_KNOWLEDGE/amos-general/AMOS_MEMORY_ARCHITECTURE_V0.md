---
title: AMOS MEMORY ARCHITECTURE V0
canon-group: meta
canon-type: os-module
rscf-state: source-claim
topic: amos-memory-architecture-v0
tags: [canon-group/biology, canon/framework, rscf/claim, rscf/provenance, rscf/state/source-claim, topic/amos-memory-architecture-v0, amos-general]
created: 2026-08-22
---


```json
{
  "id": "AMOS.MemoryArchitecture.v0",
  "name": "Canonical Memory Architecture",
  "type": "engine",
  "domain": "memory",
  "version": "v0",
  "role": "mind_core",
  "safety": "core",
  "description": "Defines how traces, states, and canon references are stored, retrieved, and forgotten.",
  "memory_layers": {
    "short_term": {
      "description": "In-run context for current reasoning.",
      "content": [
        "current_request",
        "current_policy_context",
        "active_engines",
        "recent_decisions"
      ]
    },
    "long_term": {
      "description": "Logs and state snapshots across runs.",
      "content": [
        "organism_state_snapshots",
        "scenario_traces",
        "validation_reports"
      ]
    },
    "canonical": {
      "description": "GOD_MODE engines, kernels, and canonical laws.",
      "content": [
        "identity_law",
        "cognition_law",
        "emotion_law",
        "ethical_law",
        "interpersonal_law",
        "mind_engines"
      ]
    }
  },
  "formation_rules": [
    "Every significant decision must produce a trace that links to engines, policies, and inputs.",
    "Snapshots should be taken at important lifecycle boundaries (boot, major changes, failures)."
  ],
  "forgetting_rules": [
    "Log rotation is allowed for large traces, but summaries must be kept.",
    "Canonical laws and core configuration files must never be silently deleted.",
    "Compression and aggregation are allowed for older low-impact traces."
  ],
  "retrieval_rules": [
    "Prefer most recent relevant traces when analysing similar scenarios.",
    "Surface identity and policy version when replaying past decisions.",
    "Avoid overfitting to individual past cases; highlight differences."
  ]
}

---
**Related:** [[docs/moc/00-Home]] · [[docs/moc/06-Knowledge-Base-MOC]] · [[AMOS_SIMULATION_KERNEL_V0_MATH_FOUNDATIONS]] · [[SYSTEM_SCAN_AGENT]] · [[AUTOMATION_PROFILES]]
```

---
**MOC:** [[AMOS-GENERAL_MOC]]
