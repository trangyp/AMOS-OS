---
tags: [misc]
---
# Repository Reasoning

## Acquisition before patch
Resolve:
- entrypoint
- implementation location
- callers/callees
- data/control dependencies
- config/environment
- tests/invariants
- smallest causal patch
- affected dependency cone

## Evidence priority
tests/execution > implementation > config/schema > documentation > comments > assumptions.

README claims default to SOURCE_CLAIM.

## Patch rule
Fix mechanism, not symptom.
Prefer minimal causal patch with explicit regression surface.

## Validation
narrow discriminating test → affected tests → repository-native CI/regression gates.

---
**Related:** [[docs/moc/00-Home]] · [[docs/moc/06-Knowledge-Base-MOC]] · [[docs/brain/AMOS_Simulation_Kernel_v0_Math_Foundations]] · [[docs/brain/system_scan_agent]] · [[docs/brain/automation_profiles]]
