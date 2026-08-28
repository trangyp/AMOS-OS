---
title: INFORMATION ARCHITECTURE
tags:
- architecture
- design
- structure
- canon/knowledge
type: data
source: 11_KNOWLEDGE/architecture
rscf:
  state: AMOS_MODEL
  claim_class: AMOS_MODEL
  provenance: AMOS_corpus
  scope: architecture_design
---
# INFORMATION ARCHITECTURE

```json
{
  "metadata": {
    "title": "Information Fractal Architecture 500000",
    "version": "1.0",
    "created_utc": "2026-05-06T09:01:35+00:00",
    "entry_count": 500000
  },
  "core": "Information = Signal + Noise + Meaning + Context + Transmission + Memory + Entropy + Validation + Trust + Action",
  "L_M_H": {
    "L": "low integrity information: noisy, incomplete, low context, low validation",
    "M": "usable but uncertain information: partially clear, partially validated, context dependent",
    "H": "high integrity information: clear signal, high context, validated, trusted, actionable"
  },
  "fractal_scales": [
    "bit",
    "symbol",
    "word",
    "sentence",
    "message",
    "document",
    "narrative",
    "network",
    "civilization"
  ],
  "main_law": "Information becomes actionable only when signal, context, meaning, validation, and trust exceed entropy and distortion.",
  "templates": [
    {
      "id": "INF001",
      "name": "signal_strength",
      "formula": "SS=useful_signal/total_input",
      "layer": "signal"
    },
    {
      "id": "INF002",
      "name": "noise_level",
      "formula": "NL=noise/total_input",
      "layer": "noise"
    },
    {
      "id": "INF003",
      "name": "signal_noise_ratio",
      "formula": "SNR=signal_strength/noise_level",
      "layer": "signal"
    },
    {
      "id": "INF004",
      "name": "information_entropy",
      "formula": "H=-sum(p_i*log(p_i))",
      "layer": "entropy"
    },
    {
      "id": "INF005",
      "name": "meaning_density",
      "formula": "MD=meaning_units/data_size",
      "layer": "meaning"
    },
    {
      "id": "INF006",
      "name": "context_completeness",
      "formula": "CC=available_context/required_context",
      "layer": "context"
    },
    {
      "id": "INF007",
      "name": "context_gap",
      "formula": "CG=1-context_completeness",
      "layer": "context_entropy"
    },
    {
      "id": "INF008",
      "name": "compression_ratio",
      "formula": "CR=original_size/compressed_size",
      "layer": "compression"
    },
    {
      "id": "INF009",
      "name": "compression_loss",
      "formula": "CL=meaning_lost/original_meaning",
      "layer": "compression"
    },
    {
      "id": "INF010",
      "name": "transmission_integrity",
      "formula": "TI=received_information/sent_information",
      "layer": "transmission"
    },
    {
      "id": "INF011",
      "name": "distortion_score",
      "formula": "DS=1-transmission_integrity",
      "layer": "distortion"
    },
    {
      "id": "INF012",
      "name": "source_reliability",
      "formula": "SR=verified_history/total_history",
      "layer": "source"
    },
    {
      "id": "INF013",
      "name": "evidence_support",
      "formula": "ES=supported_claims/total_claims",
      "layer": "evidence"
    },
    {
      "id": "INF014",
      "name": "claim_risk",
      "formula": "CRisk=unsupported_claims*confidence_strength",
      "layer": "risk"
    },
    {
      "id": "INF015",
      "name": "misinformation_risk",
      "formula": "MR=distortion+low_source_reliability+high_claim_risk",
      "layer": "risk"
    },
    {
      "id": "INF016",
      "name": "disinformation_risk",
      "formula": "DR=intent_to_mislead*distortion*amplification",
      "layer": "risk"
    },
    {
      "id": "INF017",
      "name": "ambiguity_score",
      "formula": "AS=possible_interpretations-1",
      "layer": "ambiguity"
    },
    {
      "id": "INF018",
      "name": "redundancy_score",
      "formula": "RS=repeated_units/total_units",
      "layer": "redundancy"
    },
    {
      "id": "INF019",
      "name": "novelty_score",
      "formula": "NS=new_information/known_information",
      "layer": "novelty"
    },
    {
      "id": "INF020",
      "name": "relevance_score",
      "formula": "REL=relevant_units/total_units",
      "layer": "relevance"
    },
    {
      "id": "INF021",
      "name": "attention_value",
      "formula": "AV=relevance*novelty*urgency",
      "layer": "attention"
    },
    {
      "id": "INF022",
      "name": "memory_fit",
      "formula": "MF=match(information,existing_memory_schema)",
      "layer": "memory"
    },
    {
      "id": "INF023",
      "name": "memory_conflict",
      "formula": "MC=conflict(information,existing_memory)",
      "layer": "memory_entropy"
    },
    {
      "id": "INF024",
      "name": "update_value",
      "formula": "UV=novelty*relevance*evidence_support",
      "layer": "learning"
    },
    {
      "id": "INF025",
      "name": "belief_update",
      "formula": "BU=learning_rate*(new_evidence-old_belief)",
      "layer": "belief"
    },
    {
      "id": "INF026",
      "name": "trust_score",
      "formula": "TS=source_reliability*evidence_support*transmission_integrity*(1-distortion)",
      "layer": "trust"
    },
    {
      "id": "INF027",
      "name": "validation_score",
      "formula": "VS=context_completeness*evidence_support*source_reliability*(1-misinformation_risk)",
      "layer": "validation"
    },
    {
      "id": "INF028",
      "name": "confidence",
      "formula": "CF=validation_score*(1-entropy)*(1-claim_risk)",
      "layer": "confidence"
    },
    {
      "id": "INF029",
      "name": "information_integrity",
      "formula": "II=meaning_density*context_completeness*transmission_integrity*validation_score",
      "layer": "integrity"
    },
    {
      "id": "INF030",
      "name": "observer_bias",
      "formula": "OB=observer_interpretation-validated_interpretation",
      "layer": "observer"
    },
    {
      "id": "INF031",
      "name": "representation_loss",
      "formula": "RL=real_state-represented_state",
      "layer": "representation"
    },
    {
      "id": "INF032",
      "name": "fractal_information_match",
      "formula": "FIM=similarity(bit,message,narrative,system_pattern)",
      "layer": "fractal"
    },
    {
      "id": "INF033",
      "name": "fractal_error",
      "formula": "FE=1-fractal_information_match",
      "layer": "fractal"
    },
    {
      "id": "INF034",
      "name": "propagation_speed",
      "formula": "PS=spread_distance/time",
      "layer": "propagation"
    },
    {
      "id": "INF035",
      "name": "amplification_factor",
      "formula": "AF=shares_or_repeats/original_instances",
      "layer": "amplification"
    },
    {
      "id": "INF036",
      "name": "decay_rate",
      "formula": "DRate=information_value_loss/time",
      "layer": "decay"
    },
    {
      "id": "INF037",
      "name": "information_half_life",
      "formula": "HL=time_until_value_halves",
      "layer": "decay"
    },
    {
      "id": "INF038",
      "name": "filter_quality",
      "formula": "FQ=relevant_passed/total_passed",
      "layer": "filter"
    },
    {
      "id": "INF039",
      "name": "permission_to_act",
      "formula": "Allow=validation_score*relevance*(1-risk)",
      "layer": "permission"
    },
    {
      "id": "INF040",
      "name": "block_information",
      "formula": "Block=misinformation_high or context_missing or evidence_low",
      "layer": "permission"
    },
    {
      "id": "INF041",
      "name": "compression_permission",
      "formula": "Compress=redundancy_high*meaning_preserve_possible",
      "layer": "action"
    },
    {
      "id": "INF042",
      "name": "expand_permission",
      "formula": "Expand=context_gap_high*audience_needs_context",
      "layer": "action"
    },
    {
      "id": "INF043",
      "name": "verify_permission",
      "formula": "Verify=claim_risk_high or source_unknown or decision_impact_high",
      "layer": "action"
    },
    {
      "id": "INF044",
      "name": "discard_permission",
      "formula": "Discard=low_relevance*low_evidence*high_noise",
      "layer": "action"
    },
    {
      "id": "INF045",
      "name": "store_permission",
      "formula": "Store=relevance*novelty*trust_score",
      "layer": "memory"
    },
    {
      "id": "INF046",
      "name": "forget_permission",
      "formula": "Forget=low_value*high_decay*low_relevance",
      "layer": "memory"
    },
    {
      "id": "INF047",
      "name": "information_load",
      "formula": "IL=units/processing_capacity",
      "layer": "load"
    },
    {
      "id": "INF048",
      "name": "overload_risk",
      "formula": "OR=information_load*(1-filter_quality)",
      "layer": "load"
    },
    {
      "id": "INF049",
      "name": "system_entropy",
      "formula": "SE=noise+ambiguity+context_gap+memory_conflict+distortion",
      "layer": "system_entropy"
    },
    {
      "id": "INF050",
      "name": "final_information_quality",
      "formula": "Q=signal_strength*meaning_density*validation_score*trust_score*(1-system_entropy)",
      "layer": "quality"
    }
  ],
  "rules": {
    "allow_action_if": [
      "signal_clear",
      "context_sufficient",
      "evidence_supported",
      "source_reliable",
      "entropy_not_high",
      "risk_acceptable"
    ],
    "block_action_if": [
      "noise_high",
      "context_missing",
      "misinformation_risk_high",
      "source_unreliable",
      "distortion_high",
      "overload_high"
    ],
    "main_goal": "Reduce information entropy by separating signal from noise, adding context, validating claims, and preserving meaning."
  }
}

---
**Related:** [[00_HOME]] · [[KNOWLEDGE_MOC]] · [[AMOS_SIMULATION_KERNEL_V0_MATH_FOUNDATIONS]] · [[SYSTEM_SCAN_AGENT]] · [[AUTOMATION_PROFILES]]
```

---
**MOC:** [[ARCHITECTURE_MOC]]

---
**Trang Framework:** [[TRANG_FRAMEWORK_RECURSIVE_ONTOLOGY_DYNAMICS]]
