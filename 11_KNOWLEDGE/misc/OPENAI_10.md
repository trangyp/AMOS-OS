---
title: OPENAI 10
tags: [misc]
type: note
source: 11_KNOWLEDGE/misc
---


interface:
  name: amos-openai-config-10
  type: openai-api-config
  version: "1.0.0"
  description: >
    OpenAI API configuration for the AMOS organism.
    Defines model endpoints, parameters, and governance constraints.
  model: gpt-4
  temperature: 0.7
  max_tokens: 4096
  governance:
    mutation_class_ceiling: M2
    authority_required: true
    audit_enabled: true

---
**Related:** [[docs/moc/00-Home]] · [[docs/moc/06-Knowledge-Base-MOC]] · [[AMOS_SIMULATION_KERNEL_V0_MATH_FOUNDATIONS]] · [[SYSTEM_SCAN_AGENT]] · [[AUTOMATION_PROFILES]]

---
**MOC:** [[MISC_MOC]]
