---
title: 00_INDEX_MOC
type: map_of_content
amos_core_target: v4.4
origin_architect: Trang Phan
steward: Trang Phan
status: ACTIVE_INDEX
conclusion_class: DERIVED
rscf:
  state: DERIVED
  claim_class: DERIVED
  provenance: authoritative_AMOS_OS_structure
  scope: active__AMOS_OS
tags:
  - knowledge
  - index
  - moc
---

# Knowledge Plane Index (00_INDEX)

## 1. Domain Overview
The Knowledge Plane (`11_KNOWLEDGE`) hosts structured semantic domains, deep wiki knowledge repositories, SOTA research indexes, and historical corpora.

## 2. Key Directories & Navigation
- [[11_KNOWLEDGE/11_KNOWLEDGE_MOC|Knowledge Main MOC]]
- [[11_KNOWLEDGE/KNOWLEDGE_MOC|Knowledge Secondary MOC]]
- [[11_KNOWLEDGE/COSMO_BRAIN_MOC|Cosmo Brain Knowledge Network]]
- [[11_KNOWLEDGE/ARXIV_66K_INDEX_MANIFEST|ArXiv 66k Research Manifest]]
- [[11_KNOWLEDGE/_arxiv_md/_arxiv_md_MOC|ArXiv Structured Research Index]]
- [[00_ROOT/00_ROOT_MOC|Root Master MOC]]

## Domain/Plane Overview
The Knowledge Plane (`11_KNOWLEDGE`) is the semantic backbone of AMOS OS. It hosts structured domain knowledge, deep wiki repositories, SOTA research indexes, historical corpora, and specialized kernel specifications. The `00_INDEX` subdirectory provides the top-level navigation surface for this plane, routing readers to domain MOCs, research manifests, and kernel archives.

The plane is distinct from the Domains plane (`21_DOMAINS`), which houses domain *specifications*. `11_KNOWLEDGE` houses the *knowledge content* — wikis, papers, kernels, and structured corpora that those specifications reference.

## MECE Classification
| Category | Artifact | Role |
|----------|----------|------|
| Plane MOC | `11_KNOWLEDGE_MOC` | Primary plane routing |
| Secondary MOC | `KNOWLEDGE_MOC` | Alternate knowledge routing |
| Network | `COSMO_BRAIN_MOC` | Cosmo Brain knowledge graph |
| Research Index | `ARXIV_66K_INDEX_MANIFEST` | ArXiv 66k manifest |
| Structured Research | `_arxiv_md_MOC` | Structured ArXiv index |
| Root | `00_ROOT_MOC` | Vault-wide navigation |

## Key Artifacts
- [[11_KNOWLEDGE/11_KNOWLEDGE_MOC|Knowledge Main MOC]] — primary plane routing.
- [[11_KNOWLEDGE/KNOWLEDGE_MOC|Knowledge Secondary MOC]] — alternate routing surface.
- [[11_KNOWLEDGE/COSMO_BRAIN_MOC|Cosmo Brain Knowledge Network]] — knowledge graph.
- [[11_KNOWLEDGE/ARXIV_66K_INDEX_MANIFEST|ArXiv 66k Research Manifest]] — research manifest.
- [[11_KNOWLEDGE/_arxiv_md/_arxiv_md_MOC|ArXiv Structured Research Index]] — structured papers.
- [[11_KNOWLEDGE/kernel/KERNEL_MOC|KERNEL_MOC]] — kernel specifications index.

## Cross-Plane Relationships
- **Domains (`21_DOMAINS`)**: domain specifications reference knowledge artifacts here for semantic grounding.
- **Research (`22_RESEARCH`)**: research papers and manifests feed into the ArXiv indexes hosted in this plane.
- **Memory (`10_MEMORY`)**: agent-learned memory may reference knowledge kernels for provenance.
- **Root (`00_ROOT`)**: the root MOC provides vault-wide navigation that includes this plane.

## Epistemic Boundary
This MOC is `DERIVED` from the authoritative AMOS OS structure. It describes topology and routing only. `INDEXED != AUTHORITATIVE`, `LINKED != VALIDATED`. The presence of a knowledge artifact in this index does not prove its epistemic class, implementation status, or canonical authority. Cross-plane dependencies must be established by each referenced artifact's own typed contract and provenance.

---

**Parent:** [[00_ROOT/00_ROOT_MOC|00_ROOT_MOC]]
