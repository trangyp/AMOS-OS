---
title: Competing Hypothesis Schema (RSCF)
type: schema
source: 16_SCHEMAS/10_RSCF
artifact_id: AMOS-SCHEMA-COMPETING-HYPOTHESIS
canonical_name: COMPETING_HYPOTHESIS_SCHEMA
artifact_type: json_yaml_schema_contract
status: CANONICAL
conclusion_class: CANONICAL
amos_core_target: v4.4
origin_architect: Trang Phan
steward: Trang Phan
plane: 16_SCHEMAS
segment: 16_SCHEMAS/10_RSCF
schema_family: RSCF
domain: competing-hypotheses
scope: AMOS_OS
created: '2026-08-25'
updated: '2026-08-28'
tags:
- amos-os
- schema
- rscf
- competing-hypothesis
- bayesian-evidence
- likelihood-ratios
- multi-hypothesis-matrix
- rscf/claim
- rscf/state/canonical
- 10-rscf-moc
- 16-schemas-moc
- 00-home
- 00-root-moc
aliases:
- Competing Hypothesis Schema
- Multi-Hypothesis Evaluation Contract
- competing_hypothesis.schema
- AMOS Hypothesis Matrix Specification
---

# Competing Hypothesis Schema (RSCF)

> **Origin Architect / Steward:** Trang Phan  
> **Plane:** `16_SCHEMAS/10_RSCF`  
> **Status:** `CANONICAL`  
> **Analysis Paradigm:** Analysis of Competing Hypotheses (ACH) $\times$ Bayesian Likelihood Ratios $\times$ Epistemic Humility

---

## 1. Schema Purpose

`COMPETING_HYPOTHESIS_SCHEMA` governs the formal representation of unresolved, ambiguous, or multi-candidate scenarios in AMOS OS. Rather than prematurely collapsing into a single biased answer, the system instantiates an explicit matrix comparing competing hypotheses $\{H_1 \dots H_n\}$ against observed evidence items $\{E_1 \dots E_m\}$.

```
+-------------------------------------------------------------------------+
|                  COMPETING HYPOTHESIS EVALUATION MATRIX                 |
|                                                                         |
|                +------------------+------------------+                  |
|                | Hypothesis H_1   | Hypothesis H_2   |                  |
|  +-------------+------------------+------------------+                  |
|  | Evidence E1 | + Consistent     | - Inconsistent   |                  |
|  | Evidence E2 | 0 Neutral        | + Consistent     |                  |
|  | Evidence E3 | - Falsifying     | + Consistent     |                  |
|  +-------------+------------------+------------------+                  |
|                         |                  |                            |
|                         v                  v                            |
|  [ Score Matrix: S(H1) = 0.21 ]    [ Score Matrix: S(H2) = 0.88 ]       |
+-------------------------------------------------------------------------+
```

---

## 2. Formal JSON Schema Specification

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "https://amos-os.org/schemas/rscf/competing_hypothesis.schema.json",
  "title": "AMOS_Competing_Hypothesis",
  "type": "object",
  "required": [
    "evaluation_id",
    "problem_statement",
    "hypotheses",
    "evidence_items",
    "consistency_matrix",
    "posterior_probabilities",
    "dominant_hypothesis"
  ],
  "properties": {
    "evaluation_id": {
      "type": "string",
      "format": "uuid"
    },
    "problem_statement": {
      "type": "string"
    },
    "hypotheses": {
      "type": "array",
      "items": {
        "type": "object",
        "required": ["id", "description", "prior_probability"],
        "properties": {
          "id": { "type": "string" },
          "description": { "type": "string" },
          "prior_probability": { "type": "number", "minimum": 0.0, "maximum": 1.0 }
        }
      },
      "minItems": 2
    },
    "evidence_items": {
      "type": "array",
      "items": {
        "type": "object",
        "required": ["id", "description", "credibility", "relevance"],
        "properties": {
          "id": { "type": "string" },
          "description": { "type": "string" },
          "credibility": { "type": "number", "minimum": 0.0, "maximum": 1.0 },
          "relevance": { "type": "number", "minimum": 0.0, "maximum": 1.0 }
        }
      },
      "minItems": 1
    },
    "consistency_matrix": {
      "type": "object",
      "description": "Mapping of hypothesis_id to evidence_id consistency scores [-1.0 .. +1.0]"
    },
    "posterior_probabilities": {
      "type": "object",
      "description": "Normalized posterior probability for each hypothesis_id"
    },
    "dominant_hypothesis": {
      "type": "string"
    }
  },
  "additionalProperties": false
}
```

---

## 3. Invariant Validation Rules

1. **Multiplicity Floor:** Every competing hypothesis evaluation must contain at least 2 distinct hypotheses ($\ge 2$).
2. **Probability Normalization:** $\sum_{h} P(h) = 1.0 \pm 10^{-5}$.
3. **No Uncontested Promotion:** A hypothesis cannot be promoted to canonical belief unless its likelihood ratio over the second-best candidate exceeds the decision threshold ($\frac{P(H_{\text{lead}})}{P(H_{\text{second}})} \ge 3.0$).

---

## 4. Cross-Plane Bindings

- **Reasoning Skills:** `amos-competing-hypotheses` · [[K_CORE_LAWS]] · [[K_METACOGNITIVE_LOOP]]
- **Schemas:** [[PROOF_CAPSULE_SCHEMA]] · [[PROVENANCE_TOPOLOGY_SCHEMA]]
- **Navigation:** [[00_HOME]] · [[16_SCHEMAS_MOC]] · [[10_RSCF_MOC]] · [[00_ROOT_MOC]]

