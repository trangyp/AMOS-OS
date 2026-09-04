---
title: Research Papers Ingestion & Peer Review Contract
type: control_contract
source: 22_RESEARCH/01_PAPERS
origin_architect: Trang Phan
steward: Trang Phan
amos_core_target: v4.4
status: ACTIVE_GOVERNING_CONTRACT
epistemic_class: AMOS_MODEL
conclusion_class: DERIVED
rscf:
  state: DERIVED
  claim_class: AMOS_MODEL
  provenance:
    - 22_RESEARCH/RESEARCH_RESEARCH_CONTRACT
    - 20_OPERATIONS/AMOS_OS_AUDIT_2026-09-03
  scope: papers_ingestion
tags:
  - amos-os
  - research
  - papers
  - arxiv
  - peer-review
---

# Research Papers Ingestion & Peer Review Contract

> **Origin Architect / Steward:** Trang Phan
> **AMOS_CORE Target:** `v4.4`
> **Status:** `ACTIVE_GOVERNING_CONTRACT`

---

## 1. Mandate & Epistemic Scope
Governs the intake, structural normalization, formula parsing, algorithmic extraction, and rigorous peer review of scientific publications, arXiv preprints, technical monographs, and laboratory discovery reports across the AMOS Research Substrate (`22_RESEARCH`).

```
+------------------------------------------------------------------------------------+
|               RESEARCH PAPERS INGESTION & AUDIT PIPELINE                           |
|                                                                                    |
|  [ Raw Paper / ArXiv Source ] ===> [ Metadata & Mathematical Extraction Engine ]   |
|                                                     ||                             |
|                                                     \/                             |
|  [ Epistemic Labeling (SOURCE_CLAIM) ] <=== [ LaTeX Proof AST Dissection ]         |
|                 ||                                                                 |
|                 \/                                                                 |
|  [ 9-Part Contract Validation ] ===> [ Formal Lean 4 / Python Simulation Sandbox ] |
|                                                     ||                             |
|                                                     \/                             |
|                                     [ Vault Ingestion Receipt Sealed ]             |
+------------------------------------------------------------------------------------+
```

---

## 2. Ingestion & Admission Invariants

1. **Immutable RSCF Identity (`INV-PAPER-01`):** Every ingested paper must be assigned an immutable RSCF identity formatted as `arxiv-{arxiv_id}-{slug}` or `paper-{doi_hash}-{slug}`.
2. **Epistemic Classification (`INV-PAPER-02`):** Unreproduced scientific claims must carry `epistemic_class: SOURCE_CLAIM` and `conclusion_class: UNKNOWN/GAP` until verified through numerical simulation or formal theorem checking.
3. **Venues Do Not Dictate Truth (`INV-PAPER-03`):** In accordance with AMOS Master Axiom `SOURCE_CLAIM != VERIFIED`, publication in high-impact venues (Nature, Science, Physical Review Letters, NeurIPS) confers high prior hypothesis interest, but does not bypass empirical validation within the AMOS runtime.
4. **Mathematical AST Extraction (`INV-PAPER-04`):** All mathematical theorems, dynamical equations, and loss formulations must be extracted into computable AST representations capable of unit and dimensional analysis.
5. **Confidence Ceiling (`INV-PAPER-05`):** External preprints carry an absolute confidence ceiling $\mathcal{C} \le 0.85$ until independent verification yields $\mathcal{C} \to 0.99$.

---

## 3. Mandatory Nine-Part Contract Specification

1. **ROLE:** Authoritative control contract regulating scientific paper ingestion, structural parsing, LaTeX equation verification, and peer-review synthesis.
2. **INTERFACES:** `IF-PAPER-INGEST` (PDF/Markdown raw stream), `IF-PAPER-VALIDATE` (LaTeX AST, Python test suite runner).
3. **DEPENDENCIES:** `03_CONTROL_PLANE/CONTROL_PLANE_CONTROL_PLANE_CONTRACT.md`, `19_TESTS/TESTS_TEST_CONTRACT.md`, `22_RESEARCH/22_RESEARCH_MOC.md`.
4. **INVARIANTS:** `INV-PAPER-01` through `INV-PAPER-05` as defined in Section 2.
5. **AUTHORITY:** AMOS Core Research & Epistemics Plane (`22_RESEARCH`).
6. **PROVENANCE:** Scientific Epistemics Directorate (Trang Phan).
7. **TESTS:** Automated syntax validation, equation parser checks, and citation graph cycle detection (`scripts/verify_137_math_formulas.py`).
8. **FAILURE:** Ingesting malformed YAML, unescaped LaTeX collisions, or unverified claims marked as canon results in immediate quarantine into `24_ARCHIVE/03_EXPERIMENTAL/`.
9. **RECOVERY:** Automatic schema patcher execution via `scripts/master_vault_validator_2026.py` and re-ingestion audit.
