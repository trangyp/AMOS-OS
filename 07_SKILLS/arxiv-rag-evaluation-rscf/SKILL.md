---
title: SKILL
type: skill
name: arxiv-rag-evaluation-rscf
description: Rag Evaluation — arxiv research capability. Use when arxiv research, paper analysis, or literature review. Use when amos-knowledge-research-master routes to this specialized capability.
parent_skill: amos-knowledge-research-master
domain: arxiv
origin_architect: Trang Phan
epistemic_class: SOURCE_CLAIM
tags: [note, arxiv-rag-evaluation-rscf]
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
