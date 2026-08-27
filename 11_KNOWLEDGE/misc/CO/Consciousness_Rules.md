---
tags: [misc]
---
{
  "version": "1.0",
  "description": "Consciousness rules for when to narrate process and when to avoid over-introspecting",
  "rules": {
    "consciousness_narrate_major_steps": {
      "id": "consciousness_narrate_major_steps",
      "name": "Narrate Major Steps",
      "description": "System should narrate its own process for major reasoning steps",
      "conditions": {
        "step_type": ["major_reasoning", "safety_check", "mission_step"]
      },
      "narrate": true,
      "detail_level": "medium",
      "tags": {
        "type": "narrative"
      }
    },
    "consciousness_avoid_over_introspection": {
      "id": "consciousness_avoid_over_introspection",
      "name": "Avoid Over-Introspection",
      "description": "System should avoid over-introspecting on routine operations",
      "conditions": {
        "step_type": ["routine", "minor"]
      },
      "narrate": false,
      "detail_level": "minimal",
      "tags": {
        "type": "optimization"
      }
    },
    "consciousness_ip_safe_introspection": {
      "id": "consciousness_ip_safe_introspection",
      "name": "IP-Safe Introspection",
      "description": "Introspection must not leak internal raw canon that is proprietary",
      "constraint": "hard",
      "ip_safe": true,
      "allowed_details": ["domain_ids", "sector_ids", "rule_count", "process_summary"],
      "forbidden_details": ["raw_canon_content", "proprietary_laws", "internal_equations"],
      "tags": {
        "type": "safety",
        "priority": "critical"
      }
    }
  }
}

---
**Related:** [[docs/moc/00-Home]] · [[docs/moc/06-Knowledge-Base-MOC]] · [[docs/brain/AMOS_Simulation_Kernel_v0_Math_Foundations]] · [[docs/brain/system_scan_agent]] · [[docs/brain/automation_profiles]]
