---
title: "Circuit-Guided Weight Scaling — From Detection to Refusal in LLMs"
type: research_paper
source: arxiv
arxiv_id: "2609.00051"
url: "https://arxiv.org/abs/2609.00051"
amos_core_target: v4.4
origin_architect: Trang Phan
steward: Trang Phan
epistemic_class: SOURCE_CLAIM
conclusion_class: DERIVED
rscf:
  state: SOURCE_CLAIM
  claim_class: SOURCE_CLAIM
  provenance:
    - arxiv:2609.00051
    - EMNLP_2026_Findings
  scope: llm_safety_circuit_enforcement
tags:
  - research
  - arxiv
  - llm-safety
  - circuit-analysis
  - refusal-mechanism
  - weight-scaling
  - enforcement
  - layered-enforcement
created: 2026-09-05
---

# Circuit-Guided Weight Scaling — From Detection to Refusal

> **arXiv:** [2609.00051](https://arxiv.org/abs/2609.00051)
> **Venue:** Findings of EMNLP 2026
> **Epistemic class:** `SOURCE_CLAIM` (peer-reviewed, EMNLP 2026 Findings; causal evidence via targeted interventions)
> **AMOS bridge:** Layered Enforcement, Enforcement Trust Contract, K_Effect_Classification, Security Plane

## Abstract summary

The paper identifies a **three-stage safety circuit** inside LLMs that mediates refusal behavior under harmful inputs. Rather than treating refusal as a monolithic behavior, the authors decompose it into causally linked stages and provide intervention evidence for each:

1. **Harmful Detection Heads** — attention heads that activate in response to harmful inputs, performing early classification of input intent.
2. **Safety Neurons** — mediate and stabilize safety signals in the residual stream, carrying the detection signal forward.
3. **Refusal Heads** — translate the stabilized safety signal into safe response generation (refusal or redirection).

The authors propose **circuit-guided weight scaling** — scaling the weights of identified safety-circuit components without modifying the model architecture — and demonstrate that this improves safety rates by **26.5%** under adversarial attacks with only **1.7%** accuracy drop across **6 LLMs**. The result recurs across architectures and attack settings.

## Key results

- Three-stage safety circuit (detection → mediation → refusal) identified with causal evidence via targeted interventions
- Circuit-guided weight scaling improves safety rates by **26.5%** under attacks
- Only **1.7%** accuracy drop on benign tasks — capability preservation
- Validated across **6 LLMs** spanning multiple architectures
- Results recur across multiple attack settings (adversarial prompts, jailbreak attempts)
- No architecture change required — weight scaling is an enforcement-mechanism modification, not a policy or structural change

## AMOS bridge analysis

### Bridge to Layered Enforcement

The three-stage safety circuit is a direct empirical instance of AMOS layered enforcement — a sequential chain where each stage has a distinct role and the chain fails closed if any stage is bypassed.

```text
AMOS Layered Enforcement:
  detect  →  mediate  →  refuse
  (classify intent)  (stabilize signal)  (enforce safe response)

Paper's Safety Circuit:
  Harmful Detection Heads  →  Safety Neurons  →  Refusal Heads
  (detect harmful input)     (mediate/stabilize)   (refuse/redirect)
```

Both enforce the same invariant: **refusal is not a single gate but a causal chain; each stage must carry the signal forward or the system fails closed.**

### Bridge to Enforcement Trust Contract

Circuit-guided weight scaling is an instance of AMOS capability attenuation via enforcement mechanism modification — the model's policy (weights) is adjusted without changing the architecture (runtime structure). This maps to the AMOS Enforcement Trust Contract principle that enforcement chain modification is distinct from policy change and must be independently attested.

```text
AMOS Enforcement Trust Contract:
  enforcement mechanism modification ≠ policy change
  capability attenuation without architecture change
  enforcement chain must be identified, current, and outside governed agent's mutation authority

Paper's Weight Scaling:
  scale safety-circuit weights ≠ modify model architecture
  attenuate harmful capability without retraining or restructuring
  circuit components identified via causal intervention, then scaled
```

The key parallel: both hold that **strengthening the enforcement mechanism is not equivalent to changing the policy goal** — the safety objective is unchanged; the mechanism that enforces it is made more robust.

### Bridge to K_Effect_Classification

Harmful Detection Heads classify inputs as harmful *before* the refusal stage acts. This is an instance of AMOS K_Effect_Classification — classifying the effect class of an input before committing to a response path.

```text
AMOS K_Effect_Classification:
  classify effect class before commit
  effect class determines which enforcement path activates

Paper's Detection Heads:
  classify input as harmful before refusal heads act
  detection signal determines whether refusal path activates
```

Both enforce the same invariant: **the system must classify what it is dealing with before deciding how to respond.** Refusal without prior detection is ungrounded; detection without subsequent refusal is inert.

### Bridge to Security Plane

The safety circuit functions as an **internal security mechanism** within the LLM — a security plane that operates inside the model's own computation, not as an external filter or guardrail. This maps to AMOS's concept of an internal security plane that enforces safety as a first-class internal concern.

```text
AMOS Security Plane:
  internal security enforcement as first-class concern
  security mechanism embedded in the system, not bolted on externally

Paper's Safety Circuit:
  safety circuit is internal to the LLM's own attention/neuron structure
  not an external filter, prompt guard, or post-hoc classifier
  circuit components are native model components identified and strengthened
```

Both enforce the same invariant: **security must be internal to the system's own computation, not an external wrapper that can be bypassed.**

## Epistemic boundary

- The paper is `SOURCE_CLAIM` — peer-reviewed (EMNLP 2026 Findings) with causal evidence via targeted interventions, not merely correlational observations.
- Causal evidence is established via intervention (ablation, activation patching, weight scaling), strengthening the claim beyond observational circuit analysis.
- The AMOS bridges are `AMOS_MODEL` — structural analogies between the paper's safety circuit and AMOS enforcement concepts. They are not empirical validations of AMOS runtime mechanisms.
- Results are validated across 6 LLMs and multiple attack settings, but generalization to all architectures and all attack types is not established.
- Weight scaling preserves capability (1.7% accuracy drop), but the trade-off frontier between safety and capability is not fully characterized — extreme scaling may degrade benign task performance beyond reported bounds.
- The three-stage circuit decomposition is supported by intervention evidence, but finer-grained sub-circuits or alternative decompositions are not ruled out.

## Related

- [[22_RESEARCH/22_RESEARCH_MOC|22_RESEARCH_MOC]]
- [[07_SKILLS/amos-layered-enforcement/SKILL|Layered Enforcement]]
- [[07_SKILLS/amos-enforcement-trust-contract/SKILL|Enforcement Trust Contract]]
- [[07_SKILLS/amos-k-effect-classification/SKILL|K_Effect_Classification]]
- [[07_SKILLS/amos-security-plane/SKILL|Security Plane]]
- [[07_SKILLS/amos-capability-bound-governance/SKILL|Capability Bound Governance]]
- [[07_SKILLS/amos-capability-attenuation/SKILL|Capability Attenuation]]
