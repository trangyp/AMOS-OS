---
title: "SKILL — Arxiv Rag Evaluation Rscf"
type: skill
source: 07_SKILLS/arxiv-rag-evaluation-rscf
name: arxiv-rag-evaluation-rscf
description: Rag Evaluation — arxiv research capability. Use when arxiv research, paper analysis, or literature review. Use when amos-knowledge-research-master routes to this specialized capability.
parent_skill: amos-knowledge-research-master
domain: arxiv
origin_architect: Trang Phan
epistemic_class: SOURCE_CLAIM
tags: [note, arxiv-rag-evaluation-rscf, canon/skill]
rscf:
  state: DERIVED
  claim_class: DERIVED
  provenance: AMOS_corpus
  scope: AMOS_general
version: "1.1.0"
---


# Arxiv: rag Evaluation Rscf

## Identity

- **Origin architect and steward**: Trang Phan
- **Parent skill**: `amos-knowledge-research-master`
- **Domain**: arxiv
- **Epistemic class**: SOURCE_CLAIM (vault-sourced from AMOS framework)

Arxiv research paper RSCF skill for Arxiv: rag Evaluation Rscf

## When to Use

- When arxiv research paper rscf skill for arxiv: rag evaluation rscf is needed within the arxiv domain
- When the parent skill (`amos-knowledge-research-master`) routes to this specialized capability
- When a query requires arxiv-specific reasoning grounded in vault sources
- When managing lifecycle operations across classify, validate, trace, assess, and detect
- When detecting drift in evidence chains, provenance freshness, or confidence calibration
- When validating outputs against domain constraints and epistemic class

## Capabilities

- **rag_evaluation.analyze_paper**: Analyze arxiv papers: extract claims, methods, evidence, and limitations
- **rag_evaluation.classify_research**: Classify research by epistemic state: established, emerging, speculative, refuted
- **rag_evaluation.assess_reproducibility**: Assess reproducibility: can the results be independently verified?
- **rag_evaluation.trace_literature**: Trace literature chains: citations, dependencies, and influence networks
- **rag_evaluation.manage_lifecycle**: Manage lifecycle: classify, validate, trace, assess, detect.
- **rag_evaluation.detect_drift**: Detect drift in evidence chains, provenance freshness, or confidence calibration.
- **rag_evaluation.validate_outputs**: Validate outputs against domain constraints and epistemic class.

## Vault-Sourced Content

(No matching vault sources found. This skill will be enriched with vault content in a future pass.)

## 11_KNOWLEDGE Vault Content

> **Source**: `11_KNOWLEDGE/_arxiv_md/2026/2026-07/E/2607.10491v1_EvidentialRAG__Quantifying_and_Mitigating_Information_Conflict_in_Multi-Source_R.md` (arxiv paper, SOURCE_CLAIM)

### EvidentialRAG: Information Conflict in Multi-Source RAG

**Problem**: Multi-source RAG systems face information conflict when retrieved chunks from different sources disagree. Standard RAG does not quantify or mitigate this conflict.

**Approach**: Evidential Deep Learning converts retrieved chunks into probabilistic evidence before generation. Each chunk contributes a Dirichlet distribution over the answer space, allowing uncertainty quantification.

**Key contributions**:
1. Formal definition of information conflict in multi-source RAG
2. Evidential framework that quantifies source-level uncertainty
3. Mitigation strategy that downweights conflicting evidence
4. Benchmark showing improved accuracy on conflicting-source scenarios

**RAG evaluation dimensions**:
- Retrieval quality: precision, recall, relevance of retrieved chunks
- Source conflict: degree of disagreement across sources
- Evidence uncertainty: quantified via Dirichlet distributions
- Generation fidelity: faithfulness to evidence vs hallucination
- Answer calibration: confidence matches accuracy

**Epistemic boundary**: This is an arxiv-sourced research paper (AMOS_MODEL when applied to AMOS). The evidential framework is a research contribution, not a proven production method.

## Failure Modes

- **Insufficient evidence**: If source material is insufficient, mark as UNKNOWN/GAP and fail closed — do not fabricate.
- **Scope violation**: If the query falls outside the skill's declared scope, escalate to the parent skill or steward.
- **Binding broken**: If 1:1:1 binding (skill→agent→workflow) is broken, flag routing mismatch and block execution.
- **Validation failure**: If validation gates fail, downgrade confidence, flag the gap, and escalate — do not force-fit.
- **Epistemic overreach**: If a claim exceeds the established evidence or epistemic class, retract and relabel.

## Validation Gates

- **G1 (Law of Law)**: No unresolved contradictions within the skill's scope.
- **G2 (Epistemic class)**: All claims labeled SOURCE / DERIVED / AMOS_MODEL / EMPIRICAL — never claim beyond evidence.
- **G3 (Provenance)**: Source path recorded for every derived claim.
- **G4 (Anti-overreach)**: No claim beyond the skill's declared scope and epistemic class.
- **G5 (Equation firewall)**: Equations carry status tags (ESTABLISHED_MATH / SOURCE_DERIVED / AMOS_MODEL / EMPIRICALLY_CALIBRATED / UNVERIFIED).
- **G6 (Failure mode)**: On validation failure, downgrade confidence, flag the gap, escalate — do not force-fit.


> **Reference**: See `references/brain_router_for_rag.md` (content_hash: 9c4cf65513ae1b0c) fo

---
**Links:** [[07_SKILLS_MOC]]

## Related

- [[arxiv-rag-evaluation-rscf_MOC]]

## Examples

- **Scenario**: When arxiv research paper rscf skill for arxiv: rag evaluation rscf is needed within the arxiv domain
  - **Input**: A query matching this skill's domain (arxiv)
  - **Output**: Structured result with epistemic labels and provenance

- **Scenario**: When the parent skill (`amos-knowledge-research-master`) routes to this specialized capability
  - **Input**: A query matching this skill's domain (arxiv)
  - **Output**: Structured result with epistemic labels and provenance

- **Scenario**: When a query requires arxiv-specific reasoning grounded in vault sources
  - **Input**: A query matching this skill's domain (arxiv)
  - **Output**: Structured result with epistemic labels and provenance


## Anti-Patterns

- **Do not use** for tasks outside the arxiv domain
- **Do not use** when the query requires empirical validation that this skill cannot provide
- **Do not use** when a parent skill or higher-level orchestrator should route instead
- **Do not bypass** epistemic class labeling — every output must carry SOURCE/DERIVED/AMOS_MODEL tags
- **Do not chain** more than 3 skills without explicit orchestrator approval


## Composition

- **Parent**: `amos-knowledge-research-master` — routes to this skill when arxiv specialization is needed
- **Peers**: Other skills in the `arxiv` domain may be composed in sequence
- **Orchestrator**: The parent skill or `AMOS_HOME` orchestrates routing
- **Workflow**: Each skill has a corresponding workflow in `08_WORKFLOWS/`
- **Agent**: Each skill has a corresponding agent in `06_AGENTS/`


## Evaluation

### Success Criteria

- Output includes epistemic class label (SOURCE/DERIVED/AMOS_MODEL/EMPIRICAL)
- Output includes provenance reference to source evidence
- Output includes confidence ceiling (capped at 0.95 for DERIVED, 1.0 for SOURCE_CANON)
- Output includes gap flags for unresolved unknowns
- Output does not exceed declared scope

### Failure Modes

- **Overreach**: Output claims validity beyond its epistemic class
- **Scope creep**: Output addresses questions outside the declared domain
- **Provenance loss**: Output cannot trace back to source evidence
- **Confidence inflation**: Output confidence exceeds the weakest-premise ceiling


## Error Handling

- **On scope violation**: Reject the query and route back to parent skill
- **On missing evidence**: Flag as GAP and reduce confidence ceiling to 0.5
- **On contradiction**: Flag as CRITICAL_GAP and halt until resolved
- **On provenance loss**: Mark output as UNKNOWN and require human review
- **On drift**: Trigger drift alignment via `amos-ai-drift-alignment-governor`


## References

- `references/brain_router_for_rag.md` — loaded on demand
- `references/references_MOC.md` — loaded on demand
- `[[arxiv-rag-evaluation-rscf_MOC]]` — skill Map of Content
- `amos-knowledge-research-master` — parent skill
- `[[arxiv-rag-evaluation-rscf-workflow]]` — corresponding workflow
- `arxiv-rag-evaluation-rscf-agent` — corresponding agent

