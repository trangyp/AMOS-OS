---
title: RULE COG EMBODIED BASELINE
tags: [misc, reference, general, canon/knowledge]
type: data
source: 11_KNOWLEDGE/misc
rscf:
  state: DERIVED
  claim_class: DERIVED
  provenance: AMOS_corpus
  scope: AMOS_general

---
# RULE COG EMBODIED BASELINE

```json
{
  "id": "rule.cog.embodied_baseline",
  "name": "Embodied baseline reasoning",
  "description": "Ensure embodied signals are present, compute stress, and annotate embodied state.",
  "layer_id": "cognitive",
  "domain_id": "cog.embodied_interoceptive",
  "invariant_ids": ["inv.cog.embodied_signals_present"],
  "equation_ids": ["eq.cog.embodied_stress_score"],
  "operator_ids": ["op.cog.annotate_embodied_state"],
  "tensor_ids": [],
  "cycle_ids": [],
  "collapse_ids": [],
  "regeneration_ids": [],
  "drift_ids": [],
  "tags": {
    "family": "cognition",
    "subfamily": "embodied",
    "tier": "baseline"
  }
}

---
**Related:** [[00_HOME]] · [[KNOWLEDGE_MOC]] · [[AMOS_SIMULATION_KERNEL_V0_MATH_FOUNDATIONS]] · [[SYSTEM_SCAN_AGENT]] · [[AUTOMATION_PROFILES]]
```

---
**MOC:** [[MISC_MOC]]
