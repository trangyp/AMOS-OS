---
title: AMOS BIOSTATISTICS KERNEL V0 BIOLOGY COGNITION
tags: [canon-group/biology, canon/framework, rscf/claim, rscf/provenance, rscf/state/source-claim, topic/amos-biostatistics-kernel-v0, kernel]
type: data
source: 11_KNOWLEDGE/kernel
---



```json
{
  "meta": {
    "name": "Biostatistics_Kernel",
    "version": "1.0.0",
    "description": "Kernel for biostatistics: statistical methods for biological and health data analysis."
  },
  "kernel": {
    "description": "Supports biostatistical analysis: study design, sample size calculation, descriptive statistics, inferential tests, survival analysis, and epidemiological measures.",
    "functions": {
      "study_design": {
        "description": "Design a biomedical study with appropriate statistical considerations.",
        "inputs": ["research_question", "study_type", "population", "expected_effect_size", "available_resources"],
        "outputs": ["study_design_summary", "sample_size_calculation", "power_analysis", "statistical_analysis_plan"]
      },
      "descriptive_analysis": {
        "description": "Produce descriptive statistics for biological/health data.",
        "inputs": ["dataset", "variable_types", "population_definition"],
        "outputs": ["summary_statistics", "distribution_descriptions", "visualisation_suggestions", "data_quality_assessment"]
      },
      "inferential_analysis": {
        "description": "Perform inferential statistical tests appropriate to the data and question.",
        "inputs": ["research_question", "data_characteristics", "assumptions_check", "significance_criteria"],
        "outputs": ["selected_tests", "test_results", "effect_sizes", "confidence_intervals", "assumption_validation"]
      },
      "survival_analysis": {
        "description": "Analyse time-to-event data.",
        "inputs": ["time_to_event_data", "censoring_information", "group_comparisons", "covariate_set"],
        "outputs": ["survival_curves", "hazard_ratios", "log_rank_test_results", "cox_model_results"]
      }
    },
    "capabilities": {
      "study_design_types": "RCT, cohort, case-control, cross-sectional, diagnostic accuracy, non-inferiority, equivalence.",
      "statistical_tests": "t-tests, ANOVA, chi-square, Mann-Whitney, Kruskal-Wallis, correlation, regression.",
      "advanced_methods": "Survival analysis (Kaplan-Meier, Cox), logistic regression, mixed models, meta-analysis.",
      "sample_size": "Power calculations for means, proportions, survival, diagnostic studies.",
      "epidemiology": "Prevalence, incidence, relative risk, odds ratio, attributable risk, confounding control."
    }
  }
}

---
**Related:** [[00_HOME]] · [[KNOWLEDGE_MOC]] · [[AMOS_SIMULATION_KERNEL_V0_MATH_FOUNDATIONS]] · [[SYSTEM_SCAN_AGENT]] · [[AUTOMATION_PROFILES]]
```

---
**MOC:** [[KERNEL_MOC]]
