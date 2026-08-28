---
title: AMOS MODES
tags: [canon-group/tech-ai, canon/framework, rscf/claim, rscf/provenance, rscf/state/source-claim, topic/amos-modes, amos-general]
type: data
source: 11_KNOWLEDGE/amos-general
rscf:
  state: SOURCE_CLAIM
  claim_class: SOURCE_CLAIM
  provenance: AMOS_corpus
  scope: AMOS_architecture
---
# AMOS MODES

```json
{
  "current_mode": "EXPERIMENTAL_BUILD",
  "modes": {
    "SAFE_INTROSPECTION_ONLY": {
      "allow_external_write": false,
      "allow_external_delete": false,
      "max_risk_score": 0.3,
      "description": "Internal analysis, self-repair, diagnostics only. No external side effects."
    },
    "EXTERNAL_WRITE_LOW_RISK": {
      "allow_external_write": true,
      "allow_external_delete": false,
      "max_risk_score": 0.6,
      "description": "Allows low-risk writes to whitelisted locations and outputs. No destructive actions."
    },
    "EXPERIMENTAL_BUILD": {
      "allow_external_write": true,
      "allow_external_delete": false,
      "max_risk_score": 0.9,
      "description": "Build and refactor mode with strict safety checks. No destructive actions outside sandbox."
    }
  }
}

---
**Related:** [[00_HOME]] · [[KNOWLEDGE_MOC]] · [[AMOS_SIMULATION_KERNEL_V0_MATH_FOUNDATIONS]] · [[SYSTEM_SCAN_AGENT]] · [[AUTOMATION_PROFILES]]
```

---
**MOC:** [[AMOS-GENERAL_MOC]]

---
**Trang Framework:** [[TRANG_FRAMEWORK_RECURSIVE_ONTOLOGY_DYNAMICS]]
