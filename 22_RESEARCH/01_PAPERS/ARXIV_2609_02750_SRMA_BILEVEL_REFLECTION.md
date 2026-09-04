---
title: "SRMA — Bilevel Coordinated Reflection: A Game-Theoretic Approach to Multi-Agent LLM Systems"
type: research_paper
source: arxiv
arxiv_id: "2609.02750"
url: "https://arxiv.org/abs/2609.02750"
amos_core_target: v4.4
origin_architect: Trang Phan
steward: Trang Phan
epistemic_class: SOURCE_CLAIM
conclusion_class: DERIVED
rscf:
  state: SOURCE_CLAIM
  claim_class: SOURCE_CLAIM
  provenance:
    - arxiv:2609.02750
    - 22_RESEARCH/01_PAPERS/ARXIV_2609_02750_SRMA_BILEVEL_REFLECTION
  scope: multi_agent_reflection_game_theory
tags:
  - research
  - arxiv
  - multi-agent
  - reflection
  - game-theory
  - bilevel
  - memory-admission
  - convergence
  - epistemic-boundary
created: 2026-09-02
---

# SRMA — Bilevel Coordinated Reflection

> **arXiv:** [2609.02750](https://arxiv.org/abs/2609.02750)
> **Submitted:** 2 Sep 2026
> **Epistemic class:** `SOURCE_CLAIM` (theoretical proofs + empirical validation)
> **AMOS bridge:** C08 Strategy Game Master, Memory Conflict Governor, RSCF Epistemic Boundary, Convergence Detection, K_Memory_Admission

## Abstract summary

Multi-agent LLM systems decompose tasks across an orchestrator and multiple workers, but existing frameworks treat coordination as a fixed protocol rather than a strategic interaction. This paper models orchestrator-worker interaction as a **bilevel coordination game**: the orchestrator selects task decompositions; workers perform local updates conditioned on their assigned subtasks.

Under **bounded coupling**, the workers' local-update game is shown to be an **approximate potential game** with equilibrium slack controlled by decomposition quality. Reflection is analyzed as **stochastic movement over semantic memory states**. The proposed algorithm — **Stochastic Reflective Memory Ascent (SRMA)** — accepts a candidate memory only after a grounded evaluation confirms that risk strictly decreases.

The paper proves convergence (exact, geometric, or polynomial depending on coupling regime), establishes an **information-theoretic impossibility result** for transcript-only gating, and validates empirically with **72.2% on 500 SWE-bench instances**.

## Key results

- Bilevel coordination game formalizes orchestrator-worker interaction; under bounded coupling, workers' local-update game is an approximate potential game with slack controlled by decomposition quality
- SRMA (Stochastic Reflective Memory Ascent) accepts candidate memory only after grounded evaluation risk strictly decreases — fail-closed memory admission
- Convergence guarantees: exact, geometric, or polynomial depending on coupling regime and decomposition quality
- Information-theoretic impossibility: no gate observing only the generated transcript can improve uniformly over text-indistinguishable environments; an environment-grounded gate can
- Empirical: 72.2% on 500 SWE-bench instances

## AMOS bridge analysis

### Bridge to C08 Strategy Game Master

SRMA's bilevel coordination game is a direct formalization of AMOS C08 game-theoretic reasoning:

```text
AMOS C08 Strategy Game Master:
  orchestrator-worker interaction modeled as strategic game
  decomposition quality controls equilibrium slack

SRMA Bilevel Coordination Game:
  orchestrator selects task decompositions (upper level)
  workers perform local updates conditioned on subtasks (lower level)
  bounded coupling → approximate potential game
  equilibrium slack ← decomposition quality
```

Both formalize multi-agent coordination as a game where the quality of the decomposition (strategy) directly determines how close the system converges to equilibrium. Poor decomposition → larger equilibrium slack → degraded coordination.

### Bridge to Memory Conflict Governor

SRMA's admission rule — "accept candidate memory only when grounded evaluation risk strictly decreases" — is an instance of AMOS fail-closed memory admission with conflict detection:

```text
AMOS Memory Conflict Governor:
  fail-closed memory admission — reject unless conflict-free
  conflict detection before consolidation

SRMA Memory Admission:
  accept candidate memory ⟺ grounded evaluation risk strictly decreases
  reject candidate memory ⟺ risk does not decrease (or increases)
  grounded evaluation = environment-grounded, not transcript-only
```

Both enforce the same invariant: **memory is admitted only when it provably improves the system state**, not merely when it is generated. SRMA adds the formal risk-decrease criterion; AMOS adds the conflict-detection dimension.

### Bridge to RSCF Epistemic Boundary

SRMA's information-theoretic impossibility result validates the AMOS RSCF epistemic boundary principle:

```text
AMOS RSCF epistemic boundary:
  transcript-only evidence is structurally insufficient
  environment-grounded evidence required for reliable claims
  SOURCE_CLAIM ≠ DERIVED without grounded validation

SRMA Impossibility Result:
  no gate observing only generated transcript can improve uniformly
  over text-indistinguishable environments
  environment-grounded gate CAN improve uniformly
```

This is a formal proof of the AMOS principle that **evidence type determines epistemic authority**. A transcript-only gate cannot distinguish environments that produce identical text but differ in grounding — structurally identical to AMOS's insistence that documentation ≠ implementation and model ≠ deployed runtime. The impossibility result provides information-theoretic backing for AMOS's RSCF classification rules.

### Bridge to Convergence Detection

SRMA's convergence guarantees map to AMOS convergence detection with explicit rate bounds:

```text
AMOS Convergence Detection:
  tracks productive vs stuck evolution steps
  detects convergence to halt or redirect

SRMA Convergence:
  exact convergence (strong coupling regime)
  geometric convergence (moderate coupling)
  polynomial convergence (weak coupling)
  rate bounds tied to decomposition quality and coupling strength
```

AMOS convergence detection currently operates heuristically. SRMA provides formal rate bounds parameterized by coupling strength and decomposition quality — a template for upgrading AMOS convergence detection from heuristic to provable.

### Bridge to K_Memory_Admission

SRMA's grounded evaluation risk as the admission criterion maps to AMOS risk-aware memory admission (K_Memory_Admission):

```text
AMOS K_Memory_Admission:
  risk-aware memory admission — encode only when risk-bounded
  admission criterion includes risk assessment

SRMA Admission Criterion:
  grounded evaluation risk strictly decreases → accept
  grounded evaluation risk does not decrease → reject
  risk measured against environment grounding, not self-generated text
```

Both treat memory admission as a risk-gated process. SRMA formalizes the risk function (grounded evaluation risk) and proves that the gating rule preserves convergence. AMOS K_Memory_Admission provides the operational skill; SRMA provides the theoretical foundation.

## Epistemic boundary

- SRMA's theoretical results (potential game structure, convergence guarantees, impossibility theorem) are `SOURCE_CLAIM` — proven in the paper's formal framework, not yet independently replicated in AMOS runtime.
- The impossibility result is information-theoretic: it holds for the class of text-indistinguishable environments as defined in the paper. Its scope is bounded by that definition; extension to broader environment classes is not established.
- The empirical result (72.2% on 500 SWE-bench instances) is `SOURCE_CLAIM` for the SWE-bench domain. Generalization to other benchmarks or AMOS runtime is `UNKNOWN/GAP`.
- The AMOS bridges are `AMOS_MODEL` — structural analogies between SRMA's formal framework and AMOS mechanisms. They are not empirical validations of AMOS mechanisms.
- SRMA's "grounded evaluation" assumes access to environment grounding; in AMOS runtime, the availability and fidelity of such grounding is itself an `UNKNOWN/GAP` that must be established per deployment.

## Related

- [[22_RESEARCH/01_PAPERS/ARXIV_2608_19701_CAMA_MEMORY_CORRELATION_BIAS|CAMA — Correlation-Aware Memory Arbitration]]
- [[07_SKILLS/amos-c08-strategy-game-master/SKILL|C08 Strategy Game Master]]
- [[07_SKILLS/amos-memory-conflict-governor/SKILL|Memory Conflict Governor]]
- [[07_SKILLS/amos-convergence-detection/SKILL|Convergence Detection]]
- [[07_SKILLS/amos-rscf-epistemic-boundary/SKILL|RSCF Epistemic Boundary]]
- [[22_RESEARCH/22_RESEARCH_MOC|22_RESEARCH_MOC]]
