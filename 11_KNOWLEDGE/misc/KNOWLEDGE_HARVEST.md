---
tags: [misc]
---
# Knowledge Harvest Runtime

## Principle
**Ephemeral Code -> Persistent Evidence -> Validated Knowledge**

Reject:
**Ephemeral Code -> LLM Summary -> Delete Evidence**

## Structural equation
`PermanentKnowledge = Claim + Scope + Evidence + Provenance + Constraint + FailureMode + Validity + Lineage`

## Pipeline
1. acquire/fingerprint
2. deterministic structure extraction
3. small falsifiable semantic claims
4. provenance/evidence/regime/governance validation
5. structured storage
6. retention-class-controlled cleanup
7. compact retrieval compilation

## Retrieval compiler
user_problem → AMOS_structural_decomposition → knowledge_registry_query → candidate_RSCF_retrieval → scope_filter → evidence_filter → freshness_filter → governance_filter → conflict_field_resolution → compact_context_compile → LLM_or_agent

Anti-pattern:
`vector_search -> dump_many_raw_repository_chunks -> LLM`

---
**Related:** [[docs/moc/00-Home]] · [[docs/moc/06-Knowledge-Base-MOC]] · [[docs/brain/AMOS_Simulation_Kernel_v0_Math_Foundations]] · [[docs/brain/system_scan_agent]] · [[docs/brain/automation_profiles]]
