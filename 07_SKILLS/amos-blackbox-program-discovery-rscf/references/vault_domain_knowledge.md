---
title: Vault Domain Knowledge — Amos Blackbox Program Discovery Rscf
type: reference
source: 07_SKILLS/amos-blackbox-program-discovery-rscf/references
tags:
- reference
- amos-blackbox-program-discovery-rscf
- type/skill
- references-moc
- 07-skills-moc
- 00-home
- amos-rscf-nodes
- law-hierarchy
- trang-framework-recursive-ontology-dynamics
rscf:
  state: SOURCE_CLAIM
  claim_class: SOURCE_CLAIM
  provenance: AMOS_corpus
  scope: skill_reference
---

# Vault-Sourced Domain Knowledge

> Source: AMOS_OS Obsidian vault (`_00_Cosmo brain/`)
> Epistemic class: SOURCE_CLAIM
> Extracted from skill: `amos-blackbox-program-discovery-rscf`

## Vault-Sourced Content

### Source 1: coding_programming_architecture

> Path: `tech-coding/coding_programming_architecture.md` | Size: 7718 chars | Match score: 13 | content_hash: 63a4c330a2d4bd73

{
  "metadata": {
    "title": "Coding Programming Fractal Architecture 500000",
    "version": "1.0",
    "created_utc": "2026-05-06T08:42:01+00:00",
    "entry_count": 500000
  },
  "core": "Code = Intent + Input + State + Logic + Entropy + Validation + Tests + Output + Deployment",
  "L_M_H": {
    "L": "low-level function, local behavior, isolated correctness",
    "M": "integration zone where bugs, entropy, and hidden assumptions appear",
    "H": "system-level behavior, production outcome, user impact"
  },
  "fractal_scales": [
    "line",
    "function",
    "class",
    "module",
    "service",
    "application",
    "platform",
    "ecosystem"
  ],
  "main_law": "Code is real only when intention, input, state, implementation, validation, output, and error handling all exist.",
  "templates": [
    {
      "id": "COD001",
      "name": "intent_alignment",
      "formula": "IA=match(feature_intent,implementation_intent)",
      "layer": "intent"
    },
    {
      "id": "COD002",
      "name": "input_contract_score",
      "formula": "IC=validated_inputs/required_inputs",
      "layer": "input"
    },
    {
      "id": "COD003",
      "name": "output_contract_score",
      "formula": "OC=valid_outputs/required_outputs",
      "layer": "output"
    },
    {
      "id": "COD004",
      "name": "state_visibility",
      "formula": "SV=explicit_state/total_state",
      "layer": "state"
    },
    {
      "id": "COD005",
      "name": "hidden_state_risk",
      "formula": "HS=hidden_state/total_state",
      "layer": "entropy"
    },
    {
      "id": "COD006",
      "name": "dependency_reality",
      "formula": "DR=verified_dependencies/claimed_dependencies",
      "layer": "dependency"
    },
    {
      "id": "COD007",
      "name": "fake_api_risk",
      "formula": "FA=unknown_calls/total_external_calls",
      "layer": "risk"
    },
    {
      "id": "COD008",
      "name": "data_flow_integrity",
      "formula": "DF=connected_flow_edges/expected_flow_edges",
      "layer": "flow"
    },
    {
      "id": "COD009",
      "name": "control_flow_integrity",
      "formula": "CF=valid_branches/total_branches",
      "layer": "flow"
    },
    {
      "id": "COD010",
      "name": "error_handling_score",
      "formula": "EH=handled_error_cases/expected_error_cases",
      "layer": "error"
    },
    {
      "id": "COD011",
      "name": "validation_score",
      "formula": "VS=input_validation*state_validation*output_validation",
      "layer": "validation"
    },
    {
      "id": "COD012",
      "name": "test_coverage",
      "formula": "TC=tested_paths/total_paths",
      "layer": "testing"
    },
    {
      "id": "COD013",
      "name": "runtime_risk",
      "formula": "RR=unhandled_cases+bad_types+missing_imports",
      "layer": "risk"
    },
    {
      "id": "COD014",
      "name": "code_entropy",
      "formula": "E=w1*hidden_state+w2*fake_api+w3*broken_flow+w4*missing_validation+w5*complexity",
      "layer": "entropy"
    },


---

### Source 2: AMOS Gap Discovery Engine — All 6 Modes Implemented

> Path: `dated/2026-08-23/2026-08-23 AMOS Gap Discovery Engine All 6 Modes.md` | Size: 5697 chars | Match score: 10 | content_hash: c4e7f1380d9d2bbb

# AMOS Gap Discovery Engine — All 6 Modes Implemented

> Epistemic class: OBSERVATION
> Conclusion label: `HIGH` — All 6 discovery modes now operational.
> Test results: 15/15 self-tests pass (was 11/11).
> Governing law: `integrity > completeness > fluency > speed > token savings`.

## Summary

Implemented the 3 remaining placeholder discovery modes in
`AMOS_GapRegistry.py`'s `GapDiscoveryEngine` class:
- **Compliance-driven**: diffs current capabilities against external requirements
- **Contradiction-driven**: maps detected conflicts to missing resolution mechanisms
- **Temporal**: re-verifies claims whose validity has expired

All 6 discovery modes are now operational. GAP-MGMT-001 coverage status
upgraded from NOT_COVERED to COVERED.

## What Was Done

### 3 New Discovery Methods

#### 1. `discover_compliance_driven(compliance_spec)`
- **Input**: compliance spec with standard name and requirements list
- **Each requirement**: id, description, component, current_coverage
- **Output**: gap candidates for NOT_COVERED and PARTIALLY_COVERED requirements
- **Impact**: HIGH for NOT_COVERED, MEDIUM for PARTIALLY_COVERED
- **Provenance**: `compliance_driven:{standard}`

#### 2. `discover_contradiction_driven(conflict)`
- **Input**: conflict dict with type, description, component, resolution_attempted, missing_mechanism
- **Output**: gap candidate for missing resolution mechanism
- **Impact**: from conflict severity (default MEDIUM)
- **Provenance**: `contradiction_driven:{conflict_type}`

#### 3. `discover_temporal(expiry_report)`
- **Input**: expiry report with expired_claims list
- **Each claim**: id, component, expired_at, original_claim, re_verification_status
- **Output**: gap candidates for NOT_VERIFIED and VERIFIED_INVALID claims
- **Impact**: HIGH for VERIFIED_INVALID, MEDIUM for NOT_VERIFIED
- **Provenance**: `temporal:validity_expiry`

### Updated `run_all_discovery()`
- Now accepts 6 optional parameters (one per discovery mode)
- Returns results dict with all 6 modes populated
- No more placeholder empty lists

### Gap Status Update
- **GAP-MGMT-001**: NOT_COVERED → COVERED (all 6 modes implemented)
- **GAP-MGMT-002**: still NOT_COVERED (unknown-unknown registry not implemented)
- **GAP_MANAGEMENT component**: NOT_COVERED → PARTIALLY_COVERED (1 of 2 gaps covered)

### Tests Added (4 new tests, 11 → 15 total)
- **Test 11**: Compliance-driven discovery finds 3 unmet requirements (from 4, 1 covered)
- **Test 12**: Contradiction-driven discovery maps conflict to missing mechanism
- **Test 13**: Temporal discovery finds 2 expired claims (from 3, 1 still valid)
- **Test 14**: `run_all_discovery` with all 6 modes produces 10 total candidates

## Test Results

| Metric | Before | After |
|--------|--------|-------|
| Discovery modes | 3 of 6 | **6 of 6** |
| Self-tests | 11/11 | **15/15** |
| GAP-MGMT-001 | NOT_COVERED | **COVERED** |
| GAP_MANAGEMENT | NOT_COVERED | **PARTIALLY_COVERED** |

## All Test Suites Status

| Suite | Tests | Status |
|--

---

### Source 3: Vietnam_Omnistructure_Program

> Path: `misc/V/Vietnam_Omnistructure_Program.md` | Size: 1148 chars | Match score: 10 | content_hash: 2ea3566f944bde37

{
  "id": "Vietnam_Omnistructure_Program",
  "name": "Vietnam Omnistructure OS Program",
  "description": "Comprehensive national omnistructure program integrating multiple sectors for Vietnam",
  "sectors": [
    "FIN_BANKING",
    "INFRA_ENERGY",
    "HLTH_HOSPITALS",
    "EDU_HUMAN",
    "PUB_GOV",
    "TECH_PLATFORMS"
  ],
  "domains": [
    "Econ_Engine",
    "Governance_Engine",
    "Tech_Engine",
    "Org_Engine",
    "Health_Engine",
    "Education_Engine",
    "City_Engine",
    "Energy_Engine"
  ],
  "country_id": "VN",
  "mission_ids": [
    "National_Digital_Identity_VN",
    "National_Infrastructure_VN",
    "National_Health_System_VN",
    "National_Education_System_VN"
  ],
  "program_horizon": "long",
  "risk_appetite": "high",
  "common_frameworks": [
    "fw.ai_governance.trang_01",
    "fw.systems_architecture.trang_01"
  ],
  "law_family_ids": [
    "seven_cycles",
    "drift_laws",
    "regeneration_laws",
    "collapse_classes"
  ]
}

---

---
**MOC:** references_MOC

## Related

- [[07_SKILLS_MOC]]
---

**Related:** [[00_HOME]] · [[AMOS_RSCF_NODES]] · [[LAW_HIERARCHY]] · references_MOC · [[07_SKILLS_MOC]]

**MOC:** references_MOC

**Trang Framework:** [[TRANG_FRAMEWORK_RECURSIVE_ONTOLOGY_DYNAMICS]]

---
RSCF-NODE
node_id: amos-blackbox-program-discovery-rscf-vault-domain-knowledge
node_type: reference
path: 07_SKILLS/amos-blackbox-program-discovery-rscf/references/vault_domain_knowledge.md
RSCF-RELATIONS:
- INDEXED_BY: [[00_HOME]]
- INDEXED_BY: [[AMOS_RSCF_NODES]]
- CHILD_OF: references_MOC
