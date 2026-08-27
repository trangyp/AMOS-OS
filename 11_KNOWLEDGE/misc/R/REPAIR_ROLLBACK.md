---
tags: [misc]
---
# Repair and Rollback

## Repair sequence
Detect failed premise/state → identify affected dependency cone → quarantine invalid state → restore nearest valid state → repair locally → revalidate descendants → release.

## Rules
- Do not globally recompute unless local repair cannot restore integrity.
- Do not repeat a failed path without changed evidence.
- Rollback restores state but preserves failure evidence and lineage.
- Audit repair externalities; a local fix can create higher-scale harm.

---
**Related:** [[docs/moc/00-Home]] · [[docs/moc/06-Knowledge-Base-MOC]] · [[docs/brain/AMOS_Simulation_Kernel_v0_Math_Foundations]] · [[docs/brain/system_scan_agent]] · [[docs/brain/automation_profiles]]
