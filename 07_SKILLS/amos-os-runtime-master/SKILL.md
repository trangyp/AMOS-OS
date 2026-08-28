---
title: SKILL — Amos Os Runtime Master
type: skill
source: 07_SKILLS/amos-os-runtime-master
name: amos-os-runtime-master
description: AMOS OS & Runtime — OS Kernel v4.4, runtime pipeline (Perceive→Route→Admit→Plan→Schedule→Execute→Observe→Repair→Audit→Finalize),
  infrastructure control plane, deployment. Use for runtime reasoning,...
parent_skill: none
domain: runtime
origin_architect: Trang Phan
epistemic_class: SOURCE_CANON
tags:
- type/skill
- canon/skill
- domain/os-runtime
- canon-group/tech-ai
- topic/runtime
- capability/runtime
- capability/ast
- capability/audit
- capability/repair
- capability/execution
- rscf/epistemic
- rscf/S-state
- rscf/T-topology
- rscf/M-memory
- rscf/C-constraint
- rscf/type-system
- sota/progressive-disclosure
- sota/anti-patterns
- amos_os
- amos-os-runtime-master
rscf:
  state: DERIVED
  claim_class: DERIVED
  provenance: AMOS_corpus
  scope: AMOS_general
version: 1.1.0
---






# AMOS Full Brain OS — Rebuilt Architecture (2026-08-22)

## Identity

Origin architect and steward: **Trang Phan**.

This is a **parent skill** that consolidates 141 sub-skills into a single domain master.
Following the skill-organizer best practice: fewer, richer skills beat many overlapping ones.
A parent skill with clearly labeled sections is better than 141 separate shallow skills.

**Epistemic class**: SOURCE_CLAIM (vault-sourced from `11_KNOWLEDGE/AMOS_Full_Brain_OS_Architecture.md` (content_hash: 33b191af65b363b7)).

## When to Use

AMOS OS & Runtime — OS Kernel v4.4, runtime pipeline (Perceive→Route→Admit→Plan→Schedule→Execute→Observe→Repair→Audit→Finalize), infrastructure control plane, deployment. Use for runtime reasoning,...
- When validating outputs against domain constraints and epistemic class

## Capabilities

- **os_runtime.execute_recovery**: Execute AMOS OS & Runtime failure recovery: detect failure, diagnose root cause, apply repair, verify recovery.
- **os_runtime.validate_quality**: Validate AMOS OS & Runtime outputs against validation gates, equation firewall, golden ratio, and integrity requirements.
- **os_runtime.discover_gaps**: Discover knowledge gaps using AMOS OS & Runtime gap discovery engine, completion graph, and unknown-unknown registry.
- **os_runtime.trace_provenance**: Trace AMOS OS & Runtime findings to test results, integrity scans, gap registry, and validation gate outputs.
- **os_runtime.assess_claim**: Assess AMOS OS & Runtime audit claims for severity, scope, evidence strength, and repair priority.
- **os_runtime.manage_lifecycle**: Manage AMOS OS & Runtime audit lifecycle: scan, detect, classify, allocate repair, verify, and document.
- **os_runtime.detect_drift**: Detect audit drift: test count drift, gap regression, integrity degradation, and validation gate erosion.
- **os_runtime.escalate_gaps**: Escalate AMOS OS & Runtime audit gaps: flag CRITICAL gaps, prioritize repair allocation, trigger bounded recovery.
- **os_runtime.validate_outputs**: Validate outputs against domain constraints and epistemic class.

## Consolidated Sub-Skills (141)

This parent skill consolidates the following sub-skills. Each is a section within this domain:

*...and 121 more sub-skills.*

> **Reference**: See `references/vault_domain_knowledge.md` (content_hash: 498509af736d95f6) for detailed vault-sourced domain knowledge.


> **Reference**: See `references/speed_governor.md` (content_hash: 183c93ed4d3e174b) for the AMOS Speed Governor (FAST/BALANCED/DEEP modes and selection criteria).


> **Reference**: See `references/golden_ratio_diagnostics.md` (content_hash: 91fb235d21638428) for the Golden-Ratio Diagnostics Layer (phi-ratio validation, golden ratio gate, structural harmony metrics).


> **Reference**: See `references/full_brain_os_test_fix.md` (content_hash: ceefd580c8932435) for the Full Brain OS Test-Fix-Rerun (test failures, fixes applied, rerun results, regression coverage).


> **Reference**: See `references/error_recovery.md` (content_hash: c844ad5a7e7024ae) for the Error Recovery (error classification, recovery patterns, failure modes).


> **Reference**: See `references/continuous_evolution.md` (content_hash: fbe2fb0541f56811) for the Continuous Evolution Complete (evolution loop, continuous improvement, adaptive runtime).


> **Reference**: See `references/core_v44_coordination_avoidance.md` (content_hash: d63cc867976c4e5f) for the AMOS Core v4.4 Coordination Avoidance Runtime (coordination avoidance, runtime optimization, concurrent execution).


> **Reference**: See `references/brain_complete_integration_report.md` (content_hash: a4878e6938f5fb47) for the AMOS Brain Complete Integration Report (integration status, brain architecture, completion summary).


> **Reference**: See `references/speed_engine_root.md` (content_hash: 4d7d368bca8653a9) for the AMOS Speed Engine v0 Root (speed optimization, performance modes, FAST/BALANCED/DEEP selection).


> **Reference**: See `references/systems_core_engine.md` (content_hash: 2ff73a6ff01e613b) for the AMOS Systems Core Engine v0 (systems core, runtime architecture, system coordination).


> **Reference**: See `references/operating_systems_survival.md` (content_hash: ab72abd251043a29) for the Operating Systems for Survival (survival OS, resilience patterns, adaptive operating systems).


> **Reference**: See `references/v44_coordination_avoidance_detailed.md` (content_hash: 8a9f678ab19eda44) for the V4.4 Coordination Avoidance Detailed (coordination avoidance runtime, MVCC, conflict-free execution).


> **Reference**: See `references
- [[AGENT_TEMPLATE]]

---
**MOC:** [[amos-os-runtime-master_MOC]]

## Examples

- **Scenario**: When validating outputs against domain constraints and epistemic class
  - **Input**: A query matching this skill's domain (runtime)
  - **Output**: Structured result with epistemic labels and provenance


## Anti-Patterns

- **Do not use** for tasks outside the runtime domain
- **Do not use** when the query requires empirical validation that this skill cannot provide
- **Do not use** when a parent skill or higher-level orchestrator should route instead
- **Do not bypass** epistemic class labeling — every output must carry SOURCE/DERIVED/AMOS_MODEL tags
- **Do not chain** more than 3 skills without explicit orchestrator approval


## Composition

- **Parent**: `none` — routes to this skill when runtime specialization is needed
- **Peers**: Other skills in the `runtime` domain may be composed in sequence
- **Orchestrator**: The parent skill or `AMOS_HOME` orchestrates routing
- **Workflow**: Each skill has a corresponding workflow in `08_WORKFLOWS/`
- **Agent**: Each skill has a corresponding agent in `06_AGENTS/`


## Evaluation

### Success Criteria

- Output includes epistemic class label (SOURCE/DERIVED/AMOS_MODEL/EMPIRICAL)
- Output includes provenance reference to source evidence
- Output includes confidence ceiling (capped at 0.95 for DERIVED, 1.0 for SOURCE_CANON)
- Output includes gap flags for unresolved unknowns
- Output does not exceed declared scope

### Failure Modes

- **Overreach**: Output claims validity beyond its epistemic class
- **Scope creep**: Output addresses questions outside the declared domain
- **Provenance loss**: Output cannot trace back to source evidence
- **Confidence inflation**: Output confidence exceeds the weakest-premise ceiling


## Error Handling

- **On scope violation**: Reject the query and route back to parent skill
- **On missing evidence**: Flag as GAP and reduce confidence ceiling to 0.5
- **On contradiction**: Flag as CRITICAL_GAP and halt until resolved
- **On provenance loss**: Mark output as UNKNOWN and require human review
- **On drift**: Trigger drift alignment via `amos-ai-drift-alignment-governor`


## References

- `references/11k_executor_agent.md` — loaded on demand
- `references/advanced_system_enhancement.md` — loaded on demand
- `references/ai_integration_layer.md` — loaded on demand
- `references/brain_2026_ultimate_enhancement.md` — loaded on demand
- `references/brain_advanced_ai_complete.md` — loaded on demand
- `references/brain_complete_integration_report.md` — loaded on demand
- `references/brain_enhancement_completion.md` — loaded on demand
- `references/brain_taskengine_integration.md` — loaded on demand
- `references/complete_system_integration.md` — loaded on demand
- `references/continuation_engine.md` — loaded on demand
- `references/continuous_evolution.md` — loaded on demand
- `references/core_v44_coordination_avoidance.md` — loaded on demand
- `references/emergency_crash_prevention.md` — loaded on demand
- `references/error_recovery.md` — loaded on demand
- `references/final_system_integration_report.md` — loaded on demand
- `references/full_brain_os_test_fix.md` — loaded on demand
- `references/golden_ratio_diagnostics.md` — loaded on demand
- `references/next_gen_system_evolution.md` — loaded on demand
- `references/omega_precision_core.md` — loaded on demand
- `references/operating_systems_survival.md` — loaded on demand
- `references/operational_status.md` — loaded on demand
- `references/phase2_completion.md` — loaded on demand
- `references/phase7_completion.md` — loaded on demand
- `references/phase8_completion.md` — loaded on demand
- `references/production_deployment_report.md` — loaded on demand
- `references/references_MOC.md` — loaded on demand
- `references/resilience_vs_control.md` — loaded on demand
- `references/resource_optimization_final.md` — loaded on demand
- `references/speed_engine_root.md` — loaded on demand
- `references/speed_governor.md` — loaded on demand
- `references/speed_moral_decision.md` — loaded on demand
- `references/system_architecture_report_v2.md` — loaded on demand
- `references/system_integration_complete.md` — loaded on demand
- `references/system_interfaces.md` — loaded on demand
- `references/system_optimization_complete.md` — loaded on demand
- `references/system_optimization_mission.md` — loaded on demand
- `references/system_schema.md` — loaded on demand
- `references/system_status.md` — loaded on demand
- `references/system_status_march16.md` — loaded on demand
- `references/system_status_march17.md` — loaded on demand
- `references/system_status_summary.md` — loaded on demand
- `references/system_status_summary_v2.md` — loaded on demand
- `references/system_status_summary_v3.md` — loaded on demand
- `references/systems_core_engine.md` — loaded on demand
- `references/tool_routing_failure_model.md` — loaded on demand
- `references/uni_system_operations_engine.md` — loaded on demand
- `references/uni_system_operations_model.md` — loaded on demand
- `references/v43_shard_local_finalization.md` — loaded on demand
- `references/v44_coordination_avoidance_detailed.md` — loaded on demand
- `references/vault_domain_knowledge.md` — loaded on demand
- `[[amos-os-runtime-master_MOC]]` — skill Map of Content
- `none` — parent skill
- `[[amos-os-runtime-master-workflow]]` — corresponding workflow
- `amos-os-runtime-master-agent` — corresponding agent
---

**Related:** [[00_HOME]] · [[AMOS_RSCF_NODES]] · [[LAW_HIERARCHY]] · [[07_SKILLS_MOC]] · [[references_MOC]]

**MOC:** [[07_SKILLS_MOC]]

**Trang Framework:** [[TRANG_FRAMEWORK_RECURSIVE_ONTOLOGY_DYNAMICS]]

---
RSCF-NODE
node_id: amos-os-runtime-master
node_type: skill
path: 07_SKILLS/amos-os-runtime-master/SKILL.md
RSCF-RELATIONS:
- INDEXED_BY: [[00_HOME]]
- INDEXED_BY: [[AMOS_RSCF_NODES]]
- CHILD_OF: [[07_SKILLS_MOC]]
