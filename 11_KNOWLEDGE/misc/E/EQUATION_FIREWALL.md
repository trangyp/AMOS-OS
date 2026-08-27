---
tags: [misc]
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
**Related:** [[docs/moc/00-Home]] · [[docs/moc/06-Knowledge-Base-MOC]] · [[docs/brain/AMOS_Simulation_Kernel_v0_Math_Foundations]] · [[docs/brain/system_scan_agent]] · [[docs/brain/automation_profiles]]
