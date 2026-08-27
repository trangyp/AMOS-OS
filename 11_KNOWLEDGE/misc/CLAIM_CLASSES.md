---
tags: [misc]
---
# Claim and Evidence Classes

## Evidence classes
- `SOURCE_CLAIM`: stated by a source; not independently verified.
- `OBSERVATION`: directly measured/seen in available evidence.
- `DERIVED`: logically or mathematically derived from explicit premises.
- `MODEL`: framework construct, simulation, analogy, or unvalidated formalization.
- `DECISION`: selected action/policy under constraints.
- `UNKNOWN/GAP`: unsupported or unresolved.

## Conclusion classes
- `VERIFIED`: directly supported within declared scope by appropriate evidence/validation.
- `DERIVED`: follows from accepted premises.
- `MODEL`: structural/formal proposal.
- `CONDITIONAL`: valid only if named premises/thresholds hold.
- `COMPETING`: unresolved alternatives remain.
- `UNKNOWN/GAP`: decision-critical information missing.

## Confidence ceiling
`Conf(C) <= min_i Conf(P_i)` for unresolved load-bearing premises.

Confidence is not evidence.

---
**Related:** [[docs/moc/00-Home]] · [[docs/moc/06-Knowledge-Base-MOC]] · [[docs/brain/AMOS_Simulation_Kernel_v0_Math_Foundations]] · [[docs/brain/system_scan_agent]] · [[docs/brain/automation_profiles]]
