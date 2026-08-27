---
title: vault domain knowledge
type: reference
source: 07_SKILLS/arxiv-grpo-reasoning-policy-rscf/references
tags: [reference, arxiv-grpo-reasoning-policy-rscf, canon/skill]
rscf:
  state: SOURCE_CLAIM
  claim_class: SOURCE_CLAIM
  provenance: AMOS_corpus
  scope: skill_reference
---


# Vault-Sourced Domain Knowledge

> Source: AMOS_OS Obsidian vault (`_00_Cosmo brain/`)
> Epistemic class: SOURCE_CLAIM
> Extracted from skill: `arxiv-grpo-reasoning-policy-rscf`

## Vault-Sourced Content

### Source 1: AMOS_Multi_Perspective_Reasoning_Kernel_v0_Meta_Cognition4_2

> Path: `kernel/A/AMOS_Multi_Perspective_Reasoning_Kernel_v0_Meta_Cognition4_2.md` | Size: 7205 chars | Match score: 10

{
  "kernel_id": "Multi_Perspective_Reasoning_Kernel",
  "version": "1.0.0",
  "source": "md/Core/AMOS_Multi_Perspective_Reasoning_Kernel_v0.md (category: meta_cognition, from AMOS_Omni_KERNEL.json)",
  "description": "Kernel for multi-perspective reasoning — holding, comparing, and integrating multiple viewpoints on the same subject, detecting bias through perspective gaps, and synthesising coherent conclusions from competing interpretations.",
  "group": "Kernels.Meta_Cognition",
  "category": "Meta_Cognition",
  "priority": 9,
  "required": true,
  "domains": ["multi_perspective", "viewpoint", "bias_detection", "perspective-taking", "integration", "competing_interpretations"],
  "depends_on": ["Meta_Logic_Kernel", "Meta_Epistemology_Kernel", "Counterfactual_Reasoning_Kernel", "Psychology_Decision_Kernel"],
  "meta": {
    "role": "Multi-Perspective Reasoning Kernel",
    "creator": "Trang Phan (Origin Architect)",
    "status": "defined",
    "binding_rules": ["Law_of_Law", "Rule_of_2", "Rule_of_4", "Absolute_Integrity"],
    "omni_category": "meta_cognition",
    "position": 7
  },
  "purpose": "Enable reasoning that holds multiple perspectives simultaneously, compares them structurally, detects where perspectives diverge and why, and integrates them into conclusions that respect the tensions rather than collapsing them.",
  "perspective_dimensions": {
    "agent_perspective": "How different agents (humans, organisations, systems) view the same situation based on their position, incentives, knowledge, and values",
    "disciplinary_perspective": "How different domains of knowledge (biology, economics, psychology, engineering, law) frame the same phenomenon",
    "temporal_perspective": "How the same situation looks from short-term vs medium-term vs long-term time horizons",
    "scale_perspective": "How the same situation looks at micro vs meso vs macro scale; what's visible at each level",
    "value_perspective": "How different values and ethical frameworks evaluate the same situation or decision"
  },
  "perspective_holding_procedure": {
    "step_1": "Identify the subject or question being reasoned about",
    "step_2": "Identify relevant perspectives (which agents, disciplines, time horizons, scales, values are relevant?)",
    "step_3": "For each perspective, construct the most charitable version: what would a competent holder of that perspective say?",
    "step_4": "Map where perspectives agree (overlap) and where they diverge (tension points)",
    "step_5": "For each tension point, identify the source of divergence: different facts? different values? different time horizons? different scale? different incentives?",
    "step_6": "Check whether any perspective is being under-represented or straw-manned",
    "step_7": "Synthesize: what can be concluded that respects the divergences? What remains genuinely contested?"
  },
  "tension_types": {
    "factual_tension": "Perspectives disagree on what is the case; resolution requires evide

---

### Source 2: AMOS_Counterfactual_Reasoning_Kernel_v0_Meta_Cognition4_2

> Path: `kernel/A/AMOS_Counterfactual_Reasoning_Kernel_v0_Meta_Cognition4_2.md` | Size: 6550 chars | Match score: 10

{
  "kernel_id": "Counterfactual_Reasoning_Kernel",
  "version": "1.0.0",
  "source": "md/Core/AMOS_Counterfactual_Reasoning_Kernel_v0.md (category: meta_cognition, from AMOS_Omni_KERNEL.json)",
  "description": "Kernel for counterfactual reasoning — what-if analysis, alternative scenario reasoning, reasoning about events that did not happen, and causal inference through comparison of actual vs hypothetical states.",
  "group": "Kernels.Meta_Cognition",
  "category": "Meta_Cognition",
  "priority": 9,
  "required": true,
  "domains": ["counterfactual", "what_if", "alternative_scenarios", "causal_inference", "hypothetical_reasoning", "scenario_analysis"],
  "depends_on": ["Meta_Logic_Kernel", "Meta_Epistemology_Kernel", "Probability_Statistics_Kernel"],
  "meta": {
    "role": "Counterfactual Reasoning Kernel",
    "creator": "Trang Phan (Origin Architect)",
    "status": "defined",
    "binding_rules": ["Law_of_Law", "Rule_of_2", "Rule_of_4", "Absolute_Integrity"],
    "omni_category": "meta_cognition",
    "position": 6
  },
  "purpose": "Enable reasoning about alternative scenarios — what would have happened if X had been different, what could happen if Y changes, and what causal relationships can be inferred by comparing actual outcomes with hypothetical alternatives.",
  "counterfactual_types": {
    "past_counterfactual": "What would have happened if something in the past had been different? (e.g., 'If we had launched earlier...')",
    "future_counterfactual": "What would happen if something changes in the future? (e.g., 'If we increase price by 10%...')",
    "structural_counterfactual": "What does the structure imply would happen under different conditions? (e.g., 'Given this system design, if load doubles...')",
    "causal_counterfactual": "What can we infer about causation by comparing what happened with what would have happened without the cause?"
  },
  "valid_counterfactual_criteria": {
    "plausible_initial_state": "The counterfactual starting point must be plausible or clearly flagged as implausible",
    "minimal_change_principle": "Change only what's necessary for the counterfactual; don't silently change other things",
    "causal_chain_conservation": "Respect the causal structure: if A causes B causes C, changing A propagates through B to C",
    "uncertainty_proportionate": "The further from actuality, the larger the uncertainty. Near-counterfactuals are more reliable than far ones.",
    "assumption_transparency": "All assumptions about how the world would differ must be explicit"
  },
  "common_errors": {
    "over_determination": "Assuming the counterfactual outcome would definitely be X without considering other influencing factors",
    "ignoring_system_reactions": "Treating the system as static when it would react to the change",
    "confusing_correlation_with_causation": "Assuming that because B followed A, changing A would change B",
    "unrealistic_baseline": "Comparing against an unrealistic or cherry-picked base

---

### Source 3: AMOS Policy Geostrategy Engine vInfinity

> Path: `engine/A/AMOS Policy Geostrategy Engine vInfinity.md` | Size: 6525 chars | Match score: 10

# AMOS Policy Geostrategy Engine vInfinity

## Meta
- **Name**: Policy_Geostrategy_Kernel_vInfinity_SUPER
- **Version**: v2.0.0+lens_integration
- **Created**: 2025-11-28T00:10:18.516087Z
- **Description**: Policy & Geostrategy kernel for state-level options and impact mapping. Enriched with cross-canon integration, lens_space, and template_library.
- **Domain**: policy_and_geostrategy
- **Density Profile**: kernel_x100k_virtual
- **Cluster Count**: 20
- **Dimension Count**: 20

---

## 20 Policy & Geostrategy Clusters
| ID | Cluster | Focus |
|----|---------|-------|
| 1 | country_and_regime_profiles | Country and regime profiling |
| 2 | political_system_and_stability | Political system and stability analysis |
| 3 | economic_structure_and_dependencies | Economic structure and dependencies |
| 4 | demographics_and_migration | Demographics and migration patterns |
| 5 | energy_and_resource_security | Energy and resource security |
| 6 | infrastructure_and_connectivity | Infrastructure and connectivity |
| 7 | military_and_security_posture | Military and security posture |
| 8 | regional_alliances_and_blocs | Regional alliances and blocs |
| 9 | international_organisations_and_norms | International organisations and norms |
| 10 | domestic_political_economy | Domestic political economy |
| 11 | policy_options_space | Policy options space mapping |
| 12 | stakeholder_mapping_domestic | Domestic stakeholder mapping |
| 13 | stakeholder_mapping_international | International stakeholder mapping |
| 14 | policy_impact_chains | Policy impact chain analysis |
| 15 | regulatory_change_analysis | Regulatory change analysis |
| 16 | scenario_and_war_gaming | Scenario and war gaming |
| 17 | sanctions_and_counter_sanctions | Sanctions and counter-sanctions |
| 18 | information_and_influence_operations | Information and influence operations |
| 19 | crisis_escalation_and_de_escalation_options | Crisis escalation and de-escalation |
| 20 | long_term_geostrategic_trends | Long-term geostrategic trends |

---

## 20 Policy Dimensions
| ID | Dimension | Description |
|----|-----------|-------------|
| 01 | national_interest_alignment | Alignment with national interest |
| 02 | economic_impact | Economic impact assessment |
| 03 | security_impact | Security impact assessment |
| 04 | domestic_political_impact | Domestic political impact |
| 05 | international_reputation | International reputation impact |
| 06 | alliance_cohesion | Alliance cohesion effects |
| 07 | escalation_risk | Escalation risk |
| 08 | deterrence_strength | Deterrence strength |
| 09 | implementation_feasibility | Implementation feasibility |
| 10 | enforcement_capacity | Enforcement capacity |
| 11 | legal_and_normative_alignment | Legal and normative alignment |
| 12 | humanitarian_impact | Humanitarian impact |
| 13 | civil_rights_impact | Civil rights impact |
| 14 | long_term_stability | Long-term stability |
| 15 | short_term_shock_risk | Short-term shock risk |
| 16 | uncertainty_lev

---
**MOC:** [[references_MOC]]

## Related

- [[07_SKILLS_MOC]]
