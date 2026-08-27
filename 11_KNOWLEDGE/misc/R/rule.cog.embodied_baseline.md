---
tags: [misc]
---
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
**Related:** [[docs/moc/00-Home]] · [[docs/moc/06-Knowledge-Base-MOC]] · [[docs/brain/AMOS_Simulation_Kernel_v0_Math_Foundations]] · [[docs/brain/system_scan_agent]] · [[docs/brain/automation_profiles]]
