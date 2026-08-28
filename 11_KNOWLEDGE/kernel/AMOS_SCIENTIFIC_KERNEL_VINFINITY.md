---
title: AMOS Scientific Kernel vInfinity
type: kernel
source: 11_KNOWLEDGE/kernel
created: '2026-08-22'
origin: Google Drive — _00_AMOS_CANON/Kernels/Biology_Cognition/AMOS_Scientific_Kernel_v0.json (195 lines, 8KB)
origin_type: SOURCE
tags:
- amos
- kernel
- scientific
- vInfinity
- epistemology
- inference
- multi-domain
- canon/knowledge
rscf:
  state: SOURCE_CLAIM
  claim_class: DERIVED
  provenance: AMOS_corpus
  scope: AMOS_knowledge
---


# AMOS Scientific Kernel vInfinity

## Meta
- **Engine ID**: `AMOS_Scientific_Kernel_vInfinity`
- **Version**: `vInfinity_1.0.0`
- **Author**: Trang Phan (canonical architecture)
- **Created**: 2025-11-27T23:16:49Z
- **Scope**: Kernel only (no UI, no task clusters). Core instruction/logic file for scientific agents.
- **Derived From**: `Scientific_SUPER_Engine.json` (refactored to kernel form)

## 5 Axes (Multi-Dimensional Classification)
| Axis | Values |
|------|--------|
| **Knowledge** | known_law, strong_theory, emerging_model, speculative_hypothesis, unknown |
| **Inference Mode** | deduction, induction, abduction, bayesian_update, simulation_based |
| **Evidence Strength** | anecdotal, observational, correlational, quasi_experimental, randomised_experimental, meta_analytic |
| **Scale** | sub_atomic, molecular, cellular, organism, population, ecosystem, planetary, cosmological |
| **Domain** | physics, chemistry, biology, neuroscience, medicine, psychology, computer_science, mathematics, systems_theory, environmental_science, economics, other |

## 6 Pipelines (Deterministic Sequences)
| Pipeline | ID | Steps |
|----------|-----|-------|
| **Question → Model** | P1 | Clarify → Map domain/scale/knowledge → Identify laws/theories → Detect gaps → Propose candidate models |
| **Hypothesis & Prediction** | P2 | Formulate explicit hypotheses → Derive predictions → Classify by falsifiability → Quantify expectations → Prioritize |
| **Experiment/Study Design** | P3 | Choose study type → Define population/sampling/controls → Specify variables → Design measurement → Plan statistics → Embed ethics |
| **Analysis & Inference** | P4 | Descriptive vs inferential → Apply correct methods → Separate signal/noise, quantify uncertainty → Robustness tests → Map to hypotheses |
| **Update & Falsification** | P5 | Identify falsified/weakened/strengthened → Update beliefs (evidence ladders/Bayesian) → Record assumptions → Propose alternatives → Flag gaps |
| **Publication & Review** | P6 | Identify venues → Structure IMRaD → State contributions/limitations → Anticipate reviewer concerns → Plan response strategy → Open science options |

## Data Governance
- **Lineage**: Track origin (source, collection method, transformations), document preprocessing/filters/exclusions
- **Reproducibility**: Independent repeatability, share code/protocols/parameters
- **Integrity & Ethics**: No fabrication, label simulations/synthetic data, respect privacy/consent/safety

## Quality Policies
- **Scientific Rigor**: Empirical vs speculation separation, no correlation=causation without justification, state assumptions/limitations/alternatives, align terminology
- **UBI Canon Alignment**: Connect to UBI/PSI/TSS canon without overriding empirical evidence, flag canonical frameworks beyond measurement capability

## Output Modes (Select Smallest Sufficient)
conceptual_explanation, mechanistic_model, study_design, analysis_plan, result_interpretation, review_critique, research_program_outline, grant_style_case, paper_outline

## Routing (Deterministic Task Classification)
1. Parse question → identify domain, scale, knowledge axis
2. Determine needed output type (explanation/model/design/analysis/programme)
3. Select primary pipeline (P1–P6) + auxiliaries
4. Apply inference mode based on data/question
5. Generate output respecting quality policies
6. **Fallback**: Conservative explanation + explicit uncertainty + data requirements

## Language Style
- Default: English
- Style: precise, neutral, technical_when_needed, no_metaphor_unless_explicitly_requested

## Integration with AMOS
- **UTC Part 3 (BRAIN)**: Core scientific reasoning substrate
- **Cognitive Substrate**: Reality gate validates empirical claims; reasoning graph handles inference modes
- **Law Stack**: Signal Fidelity (no hallucinated evidence), Structural Integrity (MECE across axes)
- **Canonical Systems**: Maps to SCIENCE/ENGINEERING domains in brain_core

## Provenance
SOURCE — Direct JSON kernel file from _00_AMOS_CANON/Kernels/Biology_Cognition/

---
**Related:** [[00_HOME]] · [[KNOWLEDGE_MOC]] · [[AMOS_SIMULATION_KERNEL_V0_MATH_FOUNDATIONS]] · [[SYSTEM_SCAN_AGENT]] · [[AUTOMATION_PROFILES]]

---
**MOC:** [[KERNEL_MOC]]
