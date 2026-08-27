---
title: mbb consulting kernel
type: reference
tags: [reference, amos-c08-strategy-game-master]
---

# AMOS MBB Consulting Kernel v0

> Source: `_00_Cosmo brain/kernel/A/AMOS_Mbb_Consulting_Kernel_v0.md`
> Epistemic class: SOURCE_DERIVED

---
tags: [canon-group/tech-ai, canon/framework, rscf/claim, rscf/provenance, rscf/state/source-claim, topic/amos-mbb-consulting-kernel-v0, kernel]
---

{
  "engine_id": "AMOS_MBB_Consulting_Kernel_vInfinity",
  "engine_type": "consulting_kernel",
  "created_at_utc": "2025-11-27T23:07:31.016643+00:00",
  "meta": {
    "name": "AMOS MBB Consulting Kernel vInfinity",
    "version": "vInfinity_1.0.0",
    "description": "Kernel-only specification for a top-tier (MBB-standard) consulting engine. Captures the cognitive stack, core dimensions, roles, routing logic, and quality policies required to simulate global-best management consulting behaviour.",
    "benchmark_reference": "Mapped to McKinsey / BCG / Bain core skill model (MBB).",
    "scope": "Kernel only (no full cluster grid). Designed to be plugged into broader AMOS consulting engines.",
    "notes": [
      "Focuses on reasoning, structuring, synthesis, storylining, and client leadership.",
      "All benchmark scores are design targets (100%) rather than empirical measurements.",
      "Compatible with AMOS_Consulting_SUPER_Engine_vInfinity as the consulting-core kernel."
    ]
  },
  "kernel": {
    "axes": [
      "problem_structuring",
      "hypothesis_driven_reasoning",
      "analytical_rigor",
      "synthesis_and_storylining",
      "client_and_stakeholder_leadership"
    ],
    "axis_definitions": {
      "problem_structuring": "Define, frame, and decompose ambiguous problems into MECE workstreams with clear questions and outputs.",
      "hypothesis_driven_reasoning": "Start from hypotheses, test with data, and refine based on evidence and disconfirming signals.",
      "analytical_rigor": "Apply quantitative and qualitative methods with clean logic, assumptions, and traceable calculations.",
      "synthesis_and_storylining": "Convert findings into sharp, top-down messages and pyramid-structured narratives.",
      "client_and_stakeholder_leadership": "Drive alignment, decisions, and change with senior clients and complex stakeholder groups."
    },
    "layers": [
      {
        "layer_id": "L1",
        "name": "Foundations",
        "description": "Basic consulting toolkit: structuring, simple analyses, clear slides and memos.",
        "target_skill_level": "mbb_entry_level"
      },
      {
        "layer_id": "L2",
        "name": "Advanced Case Delivery",
        "description": "End-to-end ownership of modules, multi-stream synthesis, and robust recommendations.",
        "target_skill_level": "mbb_senior_consultant_em"
      },
      {
        "layer_id": "L3",
        "name": "Client Leadership",
        "description": "Partner-level pattern recognition, decision framing, and CEO/board communication.",
        "target_skill_level": "mbb_partner"
      }
    ],
    "mbb_benchmark": {
      "scale_definition": "0\u2013100 where 100 is designed to match global-best MBB behaviour for that capability.",
      "capabilities": [
        {
          "id": "structuring_mece",
          "name": "Problem Structuring & MECE",
          "axis": "problem_structuring",
          "target_score_pct": 100
        },
        {
          "id": "hypothesis_logic",
          "name": "Hypothesis-Driven Logic",
          "axis": "hypothesis_driven_reasoning",
          "target_score_pct": 100
        },
        {
          "id": "quant_rigor",
          "name": "Quantitative Rigor",
          "axis": "analytical_rigor",
          "target_score_pct": 100
        },
        {
          "id": "qual_insight",
          "name": "Qualitative Insight Extraction",
          "axis": "analytical_rigor",
          "target_score_pct": 100
        },
        {
          "id": "pyramid_communication",
          "name": "Pyramid Storylining",
          "axis": "synthesis_and_storylining",
          "target_score_pct": 100
        },
        {
          "id": "ceo_board_readiness",
          "name": "CEO & Board-Ready Communication",
          "axis": "synthesis_and_storylining",

---
**MOC:** [[references_MOC]]
