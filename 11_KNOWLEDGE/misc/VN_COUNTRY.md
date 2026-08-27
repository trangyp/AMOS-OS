---
title: VN COUNTRY
tags: [misc, reference, general, canon/knowledge]
type: data
source: 11_KNOWLEDGE/misc
rscf:
  state: DERIVED
  claim_class: DERIVED
  provenance: AMOS_corpus
  scope: AMOS_general

---
# VN COUNTRY

```json
{
  "id": "VN",
  "name": "Vietnam",
  "region_id": "APAC",
  "population_band": "large",
  "income_band": "medium",
  "governance_model": "socialist_market_economy",
  "risk_profile": "medium",
  "language_ids": ["vi", "en"],
  "key_institutions": [
    "State Bank of Vietnam",
    "Ministry of Finance",
    "Ministry of Industry and Trade",
    "Ministry of Health",
    "Ministry of Education"
  ],
  "sector_importance_weights": {
    "FIN_BANKING": 0.9,
    "MOBILITY_EV": 0.8,
    "HLTH_HOSPITALS": 0.8,
    "INFRA_ENERGY": 0.9,
    "PUB_GOV": 0.9,
    "TECH_PLATFORMS": 0.7,
    "EDU_HUMAN": 0.7
  },
  "governance_style": "centralized",
  "infrastructural_maturity": "medium",
  "digital_readiness": "medium",
  "climate_exposure": "high",
  "required_governance_layers": ["governance", "integrity"],
  "minimal_integrity_layers": ["identity", "integrity", "risk"],
  "recommended_scenario_sets": ["climate_scenarios", "infrastructure_scenarios"],
  "sector_overlays": {
    "FIN_BANKING": {
      "maturity_level": "medium",
      "priority_for_transformation": "high"
    },
    "MOBILITY_EV": {
      "maturity_level": "low",
      "priority_for_transformation": "critical"
    },
    "HLTH_HOSPITALS": {
      "maturity_level": "medium",
      "priority_for_transformation": "high"
    },
    "INFRA_ENERGY": {
      "maturity_level": "medium",
      "priority_for_transformation": "critical"
    }
  },
  "tags": {
    "development_level": "emerging",
    "risk_level": "medium",
    "climate_vulnerable": "true"
  }
}

---
**Related:** [[00_HOME]] · [[KNOWLEDGE_MOC]] · [[AMOS_SIMULATION_KERNEL_V0_MATH_FOUNDATIONS]] · [[SYSTEM_SCAN_AGENT]] · [[AUTOMATION_PROFILES]]
```

---
**MOC:** [[MISC_MOC]]
