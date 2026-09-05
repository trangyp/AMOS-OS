---
title: 02 Research MOC
type: moc
source: 21_DOMAINS/49_RESEARCH
tags:
  - 02-research
  - canon/domain
  - canon-validation
  - framework-validation
  - heritage-research-method
  - research-domains-domain-spec
  - research-domains-interfaces
  - research-domains-provenance
moc: true
rscf:
  state: DERIVED
  claim_class: DERIVED
  provenance: AMOS_corpus
  scope: AMOS_general
---

# 02 Research — Map of Content

**Path:** `21_DOMAINS/49_RESEARCH`
**Files:** 8 | **Subdirectories:** 1

## Files

- [[21_DOMAINS/49_RESEARCH/CANON_VALIDATION|CANON_VALIDATION]]
- [[21_DOMAINS/49_RESEARCH/DOMAINS_RESEARCH_CONTRACT|DOMAINS_RESEARCH_CONTRACT]]
- [[21_DOMAINS/49_RESEARCH/FRAMEWORK_VALIDATION|FRAMEWORK_VALIDATION]]
- [[21_DOMAINS/49_RESEARCH/HERITAGE_RESEARCH_METHOD|HERITAGE_RESEARCH_METHOD]]
- [[21_DOMAINS/49_RESEARCH/RESEARCH_DOMAINS_DOMAIN_SPEC|RESEARCH_DOMAINS_DOMAIN_SPEC]]
- [[21_DOMAINS/49_RESEARCH/RESEARCH_DOMAINS_INTERFACES|RESEARCH_DOMAINS_INTERFACES]]
- [[21_DOMAINS/49_RESEARCH/RESEARCH_DOMAINS_PROVENANCE|RESEARCH_DOMAINS_PROVENANCE]]
- [[21_DOMAINS/49_RESEARCH/RESEARCH_DOMAINS_README|RESEARCH_DOMAINS_README]]

## Subdirectories

- [[01_CANON/00_INDEX/00_INDEX_MOC|00_INDEX_MOC]] — 00_INDEX

______________________________________________________________________


## Domain Scope

The Research domain covers scientific research methodology, evidence standards, and knowledge production within AMOS OS:

### Sub-domains
- **Research methodology**: hypothesis generation, experimental design, statistical analysis, peer review
- **Evidence standards**: RSCF epistemic classification (SOURCE_CLAIM → OBSERVATION → DERIVED → MODEL → DECISION)
- **Reproducibility**: computational reproducibility, empirical reproducibility, conceptual reproducibility
- **Knowledge production**: literature review, systematic review, meta-analysis, Bayesian synthesis

### SOTA Methods
- **Statistical methods**: Bayesian inference (MCMC, variational), frequentist (NHST, CI), bootstrap, permutation tests
- **Machine learning research**: benchmark suites (MMLU, HumanEval, SWE-bench), ablation studies, scaling laws
- **Reproducibility tools**: MLflow, W&B, DVC, Hydra; containerized experiments; pre-registration
- **Meta-science**: replication crisis (psychology, medicine); pre-registration; registered reports; open science

### AMOS Integration
- **22_RESEARCH plane**: [[22_RESEARCH/22_RESEARCH_MOC|22_RESEARCH_MOC]] — canonical research plane
- **RSCF epistemic master**: [[07_SKILLS/amos-rscf-epistemic-master/SKILL|RSCF Epistemic Master]]
- **Knowledge harvest**: [[07_SKILLS/amos-knowledge-harvest-runtime/SKILL|Knowledge Harvest Runtime]]
- **arXiv ingestion**: [[22_RESEARCH/ARXIV_SOTA_INGESTION_2026-07_BATCH3|arXiv SOTA Batch 3]]
- **SOTA embodied AI**: [[22_RESEARCH/01_PAPERS/SOTA_EMBODIED_AI_AND_ROBOT_LEARNING_2026|SOTA Embodied AI 2026]]

### Invariants
1. `PREPRINT != PEER_REVIEWED` — arXiv preprints are SOURCE_CLAIM, not validated OBSERVATION
2. `BENCHMARK_PASSED != INTELLIGENCE_DEMONSTRATED` — benchmark scores can be gamed
3. `SINGLE_STUDY != CONSENSUS` — single studies require replication
4. All research claims must cite provenance (paper, authors, date, venue, peer-review status)


**Parent:** [[21_DOMAINS/21_DOMAINS_MOC|21_DOMAINS_MOC]]
