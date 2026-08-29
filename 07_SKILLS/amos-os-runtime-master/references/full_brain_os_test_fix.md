---
title: full brain os test fix
type: reference
source: 07_SKILLS/amos-os-runtime-master/references
tags:
- reference
- amos-os-runtime-master
- type/skill
- effect-release-state
- system-scan-agent
- automation-profiles
- amos-simulation-kernel-v0-math-foundations
- law-hierarchy
- trang-framework-recursive-ontology-dynamics
rscf:
  state: SOURCE_CLAIM
  claim_class: SOURCE_CLAIM
  provenance: AMOS_corpus
  scope: skill_reference
---

# Full Brain OS Test-Fix-Rerun

> Source: `_00_Cosmo brain/dated/2026-08-25/2026-08-25 Full Brain OS Test-Fix-Rerun.md`
> Epistemic class: SOURCE_DERIVED

---
title: 2026-08-25 Full Brain OS Test-Fix-Rerun and External Substrate Research
type: daily-learning
date: 2026-08-25
epistemic: DERIVED/VERIFIED
tags: [testing, infrastructure, full-brain-os, open-source, enforcement, dated, dated/2026-08-25]
---

# 2026-08-25 — AMOS Infrastructure Test·Fix·Re-run + Open-Source Substrate Verification

## Cycle 1: Test → found defect

Ran the full executable brain stack. One real failure in 66 EngineABI tests:

| Suite | Result |
|---|---|
| executable_brain_model.py (70-layer demo) | PASS |
| MURK engine self-test | 10/10 |
| MURK comprehensive | 110/110 |
| MURK↔GoBoard integration | 251/251 |
| Go Board self + comprehensive | 226 + 190 |
| Semantic Matrix | 119/119 |
| Cognitive Substrate | 178/178 |
| DMER kernel | 21/21 |
| LLM Operator Pipeline | 11/11 |
| Expression translation constrained | 5/5 |
| Determinism suite (incl. R12 audit hash) | PASS |
| cosmo-brain TS vitest | **1142/1142** (72 files) |
| **EngineABI Phase B** | **65/66 — 1 FAIL** |
| @cosmo/ui jest | **suite failed to run** |

## Fix 1: `_infer_rule_of_4_state` crash on partial states

`AMOS_MURK_BRAIN_INTEGRATION.py` accessed `state.convergence_rate`, `state.threat_index`, `state.absolute_collapse_risk`, `state.performance_trend` as hard attributes. Minimal states (e.g. ABI test State with only core fields) crashed with AttributeError before MURK could run at all.

Fix: getattr-with-defaults; missing fields treated as neutral and never select Omega or F on their own. Semantic contract preserved for full CognitiveState inputs.

## Fix 2: Jest moduleNameMapper bypassed by relative require

`packages/ui`: react-native's `jest/setup.js` requires ErrorUtils by *relative path* (`'../Libraries/vendor/core/ErrorUtils'`), which moduleNameMapper package-root patterns never matched → real Flow-syntax source loaded → transform crash.

Fix: added mapper entries for the relative form (`'\.\./Libraries/vendor/core/ErrorUtils$'` and optional-.js variants). Result: **19/19 tests pass**.

## Cycle 2: Re-run — all green

```
EngineABI:        66 passed, 0 failed
@cosmo/ui:        19 passed
turbo test:       9 successful, 9 total
Python suites:    ~2,300+ tests, 0 failures
TS suites:        1,142 tests, 0 failures
```

## External substrate research (web-verified, not embedded canon)

| Substrate | Maps to AMOS object | Key verified capability |
|---|---|---|
| SPIFFE/SPIRE (CNCF grad.) | ERA workload_identity | node AND workload attestation, SPIFFE ID/SVID issuance, AI-agent identity management |
| ActPlane | OS reference monitor layer | eBPF/BPF-LSM info-flow DSL across process lineage trees; corrective hooks to Claude Code/Codex |
| NVIDIA OpenShell | environment/enforcement epochs | static filesystem (Landlock) vs hot-reloadable network policy w/ generation-pinned connections — direct analog of epoch freshness; REST/WS/GraphQL/MCP inspection; fail-closed middleware |
| agent-ledger | [[EFFECT_RELEASE_STATE]] | idempotency+replay, intent-bound approvals (no arg drift), started/succeeded ledger states for ambiguous crashes — independent production confirmation of v42 design |
| gVisor/Firecracker | isolation layers | unchanged |

Notable corroboration: agent-ledger's started/succeeded ledger-state split independently confirms AMOS's EXTERNALIZED_UNKNOWN→RECONCILE_EFFECT handling matches current production practice.

---
**Related:** [[00_HOME]] · [[KNOWLEDGE_MOC]] · AMOS_SIMULATION_KERNEL_V0_MATH_FOUNDATIONS · SYSTEM_SCAN_AGENT · AUTOMATION_PROFILES

---
**MOC:** references_MOC
---

**Related:** [[00_HOME]] · [[AMOS_RSCF_NODES]] · [[LAW_HIERARCHY]] · references_MOC · [[07_SKILLS_MOC]]

**MOC:** references_MOC

**Trang Framework:** [[TRANG_FRAMEWORK_RECURSIVE_ONTOLOGY_DYNAMICS]]

---
RSCF-NODE
node_id: amos-os-runtime-master-full-brain-os-test-fix
node_type: reference
path: 07_SKILLS/amos-os-runtime-master/references/full_brain_os_test_fix.md
RSCF-RELATIONS:
- INDEXED_BY: [[00_HOME]]
- INDEXED_BY: [[AMOS_RSCF_NODES]]
- CHILD_OF: references_MOC
