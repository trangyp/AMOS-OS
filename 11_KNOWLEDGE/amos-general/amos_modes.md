---
tags: [canon-group/tech-ai, canon/framework, rscf/claim, rscf/provenance, rscf/state/source-claim, topic/amos-modes, amos-general]
---

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
**Related:** [[docs/moc/00-Home]] · [[docs/moc/06-Knowledge-Base-MOC]] · [[docs/brain/AMOS_Simulation_Kernel_v0_Math_Foundations]] · [[docs/brain/system_scan_agent]] · [[docs/brain/automation_profiles]]
