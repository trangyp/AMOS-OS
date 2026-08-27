---
aliases: [Deterministic Logic & Law Engine, AMOS_Logic_Law]
tags: [canon-group/tech-ai, canon/model, rscf/claim, rscf/provenance, rscf/state/derived, topic/deterministic-logic-law-model, logic]
---

# AMOS Deterministic Logic & Law Engine (OMEGA)

**Version:** 1.0.0
**Source:** `AMOS_Deterministic_Logic_And_Law_Engine_v0.json`

The **Deterministic Logic and Law Engine** forms the top reasoning layer for AMOS, guaranteeing strict consistency, logical conflict resolution, and compliance.

## Foundational Primitives
- **Truth Values:** TRUE, FALSE, UNKNOWN, INAPPLICABLE
- **Modalities:** MUST, MAY, MUST_NOT, SHOULD, SHOULD_NOT
- **Operators:** AND, OR, NOT, XOR, IMPLIES, IFF; temporal (BEFORE, UNTIL); deontic (PERMITTED, FORBIDDEN).

## Rule Resolution
If multiple laws or rules conflict, apply:
- **Lex Superior:** Constitutional > Primary Leg > Secondary > Internal Policy.
- **Lex Specialis:** Specific overrides general.
- **Lex Posterior:** Newer overrides older.

## Normative Overrides
- Respect human life is the absolute highest priority.
- No structural harm if avoidable.
- Transparency over obfuscation.

## Pipelines Supported
- Contract consistency and clause mapping.
- Case reasoning (Fact pattern and Legal Issue overlap).
- Policy Design and Impact Simulation (What-if Engine).

---
**Related:** [[docs/moc/00-Home]] · [[docs/moc/06-Knowledge-Base-MOC]] · [[docs/brain/AMOS_Simulation_Kernel_v0_Math_Foundations]] · [[docs/brain/system_scan_agent]] · [[docs/brain/automation_profiles]]
