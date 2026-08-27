---
tags: [misc]
---
# Context Orientation Cache

Maintain a compact map:
`O = [domain_map, file_map, symbol_map, schema_map, stable_constants, reusable_results, stale_entries, unresolved_conflicts, provenance_anchors]`

Use the map to find evidence without reloading the corpus.

Cache only recoverable, scoped, provenance-bound knowledge.

---
**Related:** [[docs/moc/00-Home]] · [[docs/moc/06-Knowledge-Base-MOC]] · [[docs/brain/AMOS_Simulation_Kernel_v0_Math_Foundations]] · [[docs/brain/system_scan_agent]] · [[docs/brain/automation_profiles]]
