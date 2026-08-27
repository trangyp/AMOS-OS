---
title: EQUATION FIREWALL
tags: [misc, reference, general, canon/knowledge]
type: document
source: 11_KNOWLEDGE/misc
rscf:
  state: DERIVED
  claim_class: EMPIRICAL
  provenance: AMOS_corpus
  scope: AMOS_general

---


# Equation Firewall

For every equation record:
`EQR = [id, expression, variable_types, units, domain, assumptions, scope, provenance, status, falsifiers]`

## Status
- `ESTABLISHED_MATH`: standard mathematics under stated definitions.
- `SOURCE_DERIVED`: quoted or reconstructed from source.
- `AMOS_MODEL`: framework equation or symbolic model.
- `EMPIRICALLY_CALIBRATED`: parameters fitted to evidence.
- `UNVERIFIED`: formal expression without validation.

## Rules
- Dimensional/type mismatch invalidates composition.
- A symbolic equality does not imply empirical equality.
- A threshold is not universal unless validated for the applicable domain.
- “Entropy” and “lacunarity” require domain-specific definitions before numerical use.

---
**Related:** [[00_HOME]] · [[KNOWLEDGE_MOC]] · [[AMOS_SIMULATION_KERNEL_V0_MATH_FOUNDATIONS]] · [[SYSTEM_SCAN_AGENT]] · [[AUTOMATION_PROFILES]]

---
**MOC:** [[MISC_MOC]]
