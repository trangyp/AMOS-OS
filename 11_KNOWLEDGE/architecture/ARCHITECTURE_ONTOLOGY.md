---
title: ARCHITECTURE ONTOLOGY
tags: [architecture]
type: data
source: 11_KNOWLEDGE/architecture
---



```json
{
  "title": "Fractal Cognitive Architecture v2",
  "created_utc": "2026-05-05T13:20:31+00:00",
  "core": "Same cognitive architecture repeats at every scale.",
  "layers": [
    "intention",
    "input",
    "memory",
    "deterministic_core",
    "entropy_layer",
    "validation",
    "output"
  ],
  "deterministic": {
    "definition": "same input, same memory, same constraints, same output",
    "rules": [
      "explicit intention",
      "visible data flow",
      "known dependencies",
      "named state transitions",
      "validated output"
    ]
  },
  "entropy": {
    "definition": "layered deterministic complexity",
    "sources": [
      "missing input",
      "ambiguous intention",
      "unknown dependency",
      "hidden state",
      "conflicting rules",
      "external system instability",
      "overgenerated feature"
    ]
  },
  "relationships": {
    "deterministic_to_entropy": "Many deterministic layers interacting create entropy.",
    "entropy_to_validation": "Entropy must lower confidence unless handled.",
    "fractal_to_code": "Function, class, module, service, and application repeat the same architecture."
  }
}

---
**Related:** [[docs/moc/00-Home]] · [[docs/moc/06-Knowledge-Base-MOC]] · [[AMOS_SIMULATION_KERNEL_V0_MATH_FOUNDATIONS]] · [[SYSTEM_SCAN_AGENT]] · [[AUTOMATION_PROFILES]]
```

---
**MOC:** [[ARCHITECTURE_MOC]]
