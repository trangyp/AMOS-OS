---
title: Vault Domain Knowledge — Amos Github Rscf Ingestion
type: reference
source: 07_SKILLS/amos-github-rscf-ingestion/references
tags:
- reference
- amos-github-rscf-ingestion
- canon/skill
rscf:
  state: SOURCE_CLAIM
  claim_class: SOURCE_CLAIM
  provenance: AMOS_corpus
  scope: skill_reference
---


# Vault-Sourced Domain Knowledge

> Source: AMOS_OS Obsidian vault (`_00_Cosmo brain/`)
> Epistemic class: SOURCE_CLAIM
> Extracted from skill: `amos-github-rscf-ingestion`

## Vault-Sourced Content

### Source 1: AMOS Full Infrastructure Brain for GitHub Copilot

> Path: `misc/CO/copilot-instructions.md` | Size: 1067 chars | Match score: 7 | content_hash: 74551a7694bd4705

# AMOS Full Infrastructure Brain for GitHub Copilot

Use the repository-local AMOS Markdown brain.

Always conceptually apply:
- `BRAIN.md`
- `brain/00_boot/BOOTSTRAP.md`
- `brain/10_core/INVARIANTS.md`
- `brain/10_core/CLAIM_CLASSES.md`

Use `brain/00_boot/ROUTER.md` to load only relevant modules.

### Code changes
Load:
- `brain/60_execution/REPOSITORY_REASONING.md`
- `brain/60_execution/EXECUTION_PROVENANCE.md`
- `brain/30_epistemics/SENSITIVITY_FALSIFIERS.md`

### Complex evidence
Load:
- provenance
- RSCF proof capsule
- competing hypotheses
- regime/freshness
- causal firewall

### Agent/harness changes
Load GMEF + evolution memory + repair/rollback.

### Concurrent knowledge/state changes
Use v3.9/v4.0/v4.1/v4.2/v4.3/v4.4 modules according to dependency overlap and consequence.

Prefer the v4.4 local fast lane only when independence is demonstrated. Otherwise escalate.

---

---

### Source 2: prediction_architecture_v19_no_overlap

> Path: `architecture/prediction_architecture_v19_no_overlap.md` | Size: 10349 chars | Match score: 5 | content_hash: 20f604c64ea931f3

{
  "metadata": {
    "title": "Prediction 500000 V19 No Overlap",
    "version": "19.0",
    "created_utc": "2026-05-06T14:51:27+00:00",
    "entry_count": 500000,
    "non_overlap_note": "V19 focuses on institutional prediction metabolism: ingestion, digestion, circulation, detox, waste, homeostasis, metabolic disease, and repair."
  },
  "core": "Prediction V19 = Data Ingestion + Signal Digestion + Absorption + Circulation + Detox + Waste Removal + Homeostasis + Metabolic Repair",
  "L_M_H": {
    "L": "metabolically sick: forecast obesity, toxin load, waste retention, insulin resistance",
    "M": "metabolically unstable: signal exists but digestion, circulation, or satiety is weak",
    "H": "metabolically healthy: digests signals, distributes decision energy, removes waste, restores homeostasis"
  },
  "fractal_scales": [
    "input",
    "signal",
    "decision_cell",
    "team",
    "department",
    "institution",
    "civilization"
  ],
  "main_law": "An institution predicts well only when it metabolizes information: ingesting, digesting, distributing, detoxing, recycling, and resting.",
  "templates": [
    {
      "id": "PR19_001",
      "name": "data_ingestion_rate",
      "formula": "DIR=raw_inputs/time",
      "layer": "institutional_metabolism"
    },
    {
      "id": "PR19_002",
      "name": "signal_digestion_quality",
      "formula": "SDQ=usable_signals/raw_inputs",
      "layer": "digestion"
    },
    {
      "id": "PR19_003",
      "name": "forecast_nutrient_absorption",
      "formula": "FNA=decision_value_extracted/useful_signal",
      "layer": "absorption"
    },
    {
      "id": "PR19_004",
      "name": "prediction_metabolic_rate",
      "formula": "PMR=forecast_cycles/time",
      "layer": "metabolism"
    },
    {
      "id": "PR19_005",
      "name": "decision_energy_distribution",
      "formula": "DED=decision_resources_allocated/decision_needs",
      "layer": "energy_distribution"
    },
    {
      "id": "PR19_006",
      "name": "forecast_caloric_surplus",
      "formula": "FCS=forecast_inputs>decision_capacity",
      "layer": "overload"
    },
    {
      "id": "PR19_007",
      "name": "forecast_caloric_deficit",
      "formula": "FCD=forecast_inputs<minimum_decision_needs",
      "layer": "underload"
    },
    {
      "id": "PR19_008",
      "name": "prediction_obesity",
      "formula": "PO=accumulated_unused_forecasts/storage_capacity",
      "layer": "metabolic_disease"
    },
    {
      "id": "PR19_009",
      "name": "prediction_starvation",
      "formula": "PS=insufficient_signal_for_action",
      "layer": "metabolic_disease"
    },
    {
      "id": "PR19_010",
      "name": "forecast_diabetes",
      "formula": "FD=high_signal_intake_low_decision_response",
      "layer": "metabolic_disease"
    },
    {
      "id": "PR19_011",
      "name": "insulin_of_decision",
      "formula": "IOD=mechanism_turning_signal_into_action",
      "layer": "conversion"
    },
    {
      "id": "PR19_012",
   

---


import json
from functools import lru_cache

_SPEC_JSON = r"""

---
**MOC:** [[references_MOC]]

## Related

- [[07_SKILLS_MOC]]
---

**Related:** [[00_HOME]] · [[AMOS_RSCF_NODES]] · [[LAW_HIERARCHY]] · [[references_MOC]] · [[07_SKILLS_MOC]]

**MOC:** [[references_MOC]]

**Trang Framework:** [[TRANG_FRAMEWORK_RECURSIVE_ONTOLOGY_DYNAMICS]]

---
RSCF-NODE
node_id: amos-github-rscf-ingestion-vault-domain-knowledge
node_type: reference
path: 07_SKILLS/amos-github-rscf-ingestion/references/vault_domain_knowledge.md
RSCF-RELATIONS:
- INDEXED_BY: [[00_HOME]]
- INDEXED_BY: [[AMOS_RSCF_NODES]]
- CHILD_OF: [[references_MOC]]
