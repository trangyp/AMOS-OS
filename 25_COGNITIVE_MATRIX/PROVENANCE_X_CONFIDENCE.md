---
canon-group: meta
canon-type: framework
rscf-state: source-claim
rscf-claim: verified
rscf-provenance: AMOS_corpus
conclusion_class: AMOS_MODEL
epistemic_class: SOURCE_CLAIM
topic: Provenance X Confidence
tags:
  - canon-group/tech-ai
  - rscf/claim
  - rscf/provenance
  - rscf/state/source-claim
  - misc
created: 2026-08-22
---
---
---

# Provenance × Confidence — Full Canon Expansion

## 1. Role

This matrix governs how provenance ancestry, source independence, empirical grounding, and inherited premises constrain epistemic confidence. Its decisive invariant is: **source multiplicity is not evidence independence**, and derived confidence cannot outrun the weakest load-bearing premise.

## 2. Provenance Dimensions

| Dimension | Description | Impact on Confidence |
|-----------|-------------|---------------------|
| **Ancestry Depth** | How many steps from the original source | Deeper ancestry → more potential for error injection |
| **Source Independence** | Whether sources are genuinely independent | Dependent sources do not increase confidence |
| **Empirical Grounding** | Whether claims are tied to empirical observation | Empirical grounding → higher confidence ceiling |
| **Cross-Regime Bridging** | Whether claims transfer across regimes | Regime transfer → confidence reduction |
| **Temporal Freshness** | Whether evidence is current | Stale evidence → confidence decay |

## 3. Confidence Ceiling Law

The confidence ceiling is defined by:

$$C_{claim} \leq \min(C_{premise_1}, C_{premise_2}, \ldots, C_{premise_n})$$

Where $C_{premise_i}$ is the confidence of each load-bearing premise.

**Hard rule:** A conclusion's confidence can never exceed the confidence of its weakest premise.

## 4. Source Independence Rules

### 4.1 Independence Test

Two sources $S_1$ and $S_2$ are independent iff:

$$P(S_1 | S_2) = P(S_1)$$

i.e., knowing one source gives no information about the other.

### 4.2 Dependence Detection

Sources are **dependent** if they share:
- Common ancestry (one derived from the other)
- Common methodology (same measurement technique)
- Common bias (same systemic error)
- Common data (same underlying dataset)

### 4.3 Confidence Scaling

| Scenario | Confidence Multiplier |
|----------|----------------------|
| $n$ truly independent sources | $\sqrt{n}$ improvement (up to ceiling) |
| $n$ partially dependent sources | Improvement < $\sqrt{n}$ |
| $n$ fully dependent sources | No improvement (1×) |
| Echo chamber ($n$ copies of 1 source) | No improvement (1×) |

## 5. Confidence Governance Matrix

| Claim Class | Minimum Evidence | Maximum Confidence | Override Allowed |
|------------|-----------------|-------------------|-----------------|
| UNKNOWN/GAP | None | 0.0 | No |
| SOURCE_CLAIM | Single source | 0.5 | No |
| DERIVED | Valid proof trail | 0.7 | No |
| MODEL | Stated assumptions | 0.8 | No |
| EVIDENCE | Multiple independent sources | 0.9 | No |
| VERIFIED | Robust evidence + adversarial testing | 0.95 | No |

## 6. Inherited Premise Rules

### 6.1 Premise Inheritance

When a conclusion is derived from premises, it inherits the confidence profile of all premises:

$$\text{ConfidenceProfile}(conclusion) = \bigotimes_{i=1}^{n} \text{ConfidenceProfile}(premise_i)$$

Where $\bigotimes$ is the confidence convolution operator (weakest-link composition).

### 6.2 Premise Degradation

If a premise is retracted or demoted:
1. All conclusions that depend on it are flagged
2. If the premise was load-bearing, the conclusion is demoted to QUARANTINED
3. If an alternative proof trail exists, the conclusion may survive with reduced confidence

### 6.3 Confidence Decay Over Depth

Each inference step introduces uncertainty:

$$C_{depth=d} = C_{root} \times \prod_{i=1}^{d} (1 - \epsilon_i)$$

Where $\epsilon_i$ is the error rate at inference step $i$.

## 7. Anti-Patterns

| Pattern | Description | Detection | Mitigation |
|---------|-------------|-----------|------------|
| **Echo Chamber** | Same source cited multiple times | Check source ancestry | Count as 1 source |
| **Confidence Laundering** | Indirect claims used to boost confidence | Trace provenance chain | Cap confidence at source level |
| **Premise Smuggling** | Unstated premises used in reasoning | Require explicit premises | Force premise declaration |
| **Scope Creep** | Confidence from one regime applied to another | Check regime labels | Regime-specific confidence |

## 8. Inter-Plane Connections

- **Provenance:** [[01_CANON/07_PROVENANCE/PROVENANCE_ROOT_REGISTRY|PROVENANCE_ROOT_REGISTRY]] — Provenance infrastructure
- **Core Laws:** [[01_CANON/01_CORE_LAWS/L0_INTEGRITY|L0_INTEGRITY]] — Integrity axiom
- **Knowledge:** [[11_KNOWLEDGE/KNOWLEDGE_CONTRACT|KNOWLEDGE_CONTRACT]] — Knowledge promotion rules
- **RSCF:** [[11_KNOWLEDGE/TENSORS|TENSORS]] — RSCF claim structure
- **Deterministic Logic:** [[02_KERNEL/DETERMINISTIC_LOGIC_KERNEL|DETERMINISTIC_LOGIC_KERNEL]] — Proof trail requirements

______________________________________________________________________

**MOC:** [[25_COGNITIVE_MATRIX/00_INDEX/COGNITIVE_MATRIX_MOC|COGNITIVE_MATRIX_MOC]] · [[00_ROOT/00_HOME|00_HOME]]
