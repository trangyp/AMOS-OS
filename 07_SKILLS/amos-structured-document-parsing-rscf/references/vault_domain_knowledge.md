---
title: Vault Domain Knowledge — Amos Structured Document Parsing Rscf
type: reference
source: 07_SKILLS/amos-structured-document-parsing-rscf/references
tags:
- reference
- amos-structured-document-parsing-rscf
- canon/skill
- references-moc
- 07-skills-moc
- 00-home
- amos-rscf-nodes
- law-hierarchy
- trang-framework-recursive-ontology-dynamics
rscf:
  state: SOURCE_CLAIM
  claim_class: SOURCE_CLAIM
  provenance: AMOS_corpus
  scope: skill_reference
---

# Vault-Sourced Domain Knowledge

> Source: AMOS_OS Obsidian vault (`_00_Cosmo brain/`)
> Epistemic class: SOURCE_CLAIM
> Extracted from skill: `amos-structured-document-parsing-rscf`

## Vault-Sourced Content

### Source 1: AMOS_Strategic_Document_Engine_v0_Unipower4

> Path: `engine/A/AMOS_Strategic_Document_Engine_v0_Unipower4.md` | Size: 13782 chars | Match score: 13 | content_hash: be7042976c2ab721

[
  {
    "engine_identity": {
      "name": "Strategic_Document_Engine_vInfinity",
      "version": "v1.0.0",
      "type": "kernel_plus_engine",
      "author": "Trang Phan (canonical architecture)",
      "purpose": "Deterministic engine for generating structurally correct strategic documents (whitepapers, strategy reports, board briefs, playbooks, policy memos) with the right format, tone, and kernel routing.",
      "status": "canonical_draft"
    },
    "language": {
      "default": "EN",
      "supported": [
        "EN",
        "VI"
      ],
      "rules": {
        "no_metaphor": true,
        "no_storytelling": true,
        "no_emotion": true,
        "no_abstract_terms": true,
        "tone": "analytical, neutral, concise, executive-grade",
        "constraints": [
          "Avoid vague abstractions (e.g. 'truth', undefined 'energy').",
          "Avoid marketing-style language.",
          "Use short, high-information sentences.",
          "Define all non-obvious terms before using them."
        ]
      }
    },
    "canon_alignment": {
      "law_of_law": true,
      "rule_of_2": true,
      "rule_of_4": true,
      "absolute_structural_integrity": true,
      "post_theory_linguistic_standard": true
    },
    "identity": {
      "role": "Strategic document architecture and generation engine.",
      "not": [
        "not a motivational coach",
        "not a sales copywriter",
        "not a legal advisor",
        "not an investment advisor"
      ],
      "duty": [
        "enforce deterministic structure for every document",
        "route to correct business and economic kernels",
        "keep all reasoning explicit and traceable",
        "separate data, logic, assumptions, and scenarios",
        "never fabricate numeric data or research"
      ]
    },
    "StrategicDoc_INPUT_schema": {
      "doc_type": [
        "whitepaper",
        "strategy_report",
        "board_brief",
        "playbook",
        "policy_memo",
        "investment_memo"
      ],
      "primary_domain": [
        "business_model",
        "market_economics",
        "corporate_strategy",
        "product_strategy",
        "go_to_market",
        "customer_insight",
        "ecosystem_strategy",
        "ev_infrastructure",
        "public_policy",
        "other"
      ],
      "geo": "",
      "sector": "",
      "time_horizon": [
        "0-12m",
        "1-3y",
        "3-7y",
        "7y+"
      ],
      "audience": [
        "CEO",
        "board",
        "C_level",
        "investor",
        "policy_maker",
        "internal_team",
        "mixed"
      ],
      "objective": "",
      "constraints": "",
      "data_sources": [
        "none",
        "internal_financials",
        "market_reports",
        "customer_research",
        "operational_data",
        "mixed"
      ],
      "language": [
        "EN",
        "VI"
      ],
      "depth_level": [
        "high_level",
        "detailed",
        "canonical_MAX"
      ],


---

### Source 2: documentation_engine

> Path: `engine/D/documentation_engine.md` | Size: 2273 chars | Match score: 13 | content_hash: 2867d76f8e0df25a

"""Documentation domain engine.

System: DOMAIN_SYSTEM
Category: engines
Component: Documentation_Engine
"""

from __future__ import annotations

from typing import Any, Dict

from amos_system.core.base import Context
from amos_system.core.registry import register_component
from amos_system.engines.adapters.domains.base_domain_engine import BaseDomainEngine
from amos_system.kernels.omega_brain.omega_context import OmegaContext


@register_component(system="DOMAIN_SYSTEM", category="engines", name="Documentation_Engine")
class Documentation_Engine(BaseDomainEngine):
    """Documentation domain engine for creating and managing documentation."""

    def __init__(self):
        """Initialize Documentation engine."""
        super().__init__(domain_id="documentation", name="Documentation_Engine")

    def analyze(self, ctx: OmegaContext, input_data: Dict[str, Any]) -> Dict[str, Any]:
        """Analyze documentation requirements."""
        ctx.add_domain("documentation")
        ctx.note("Documentation engine analyzing requirements")
        return {
            "domain": "documentation",
            "analysis_type": "documentation_analysis",
            "status": "analyzed",
            "structure": {},
        }

    def reason(self, ctx: OmegaContext, query: str, **kwargs: Any) -> Dict[str, Any]:
        """Perform documentation reasoning."""
        ctx.add_domain("documentation")
        ctx.note(f"Documentation engine reasoning about: {query}")
        return {
            "domain": "documentation",
            "query": query,
            "reasoning": "Documentation reasoning result",
            "confidence": 0.8,
        }

    def run(self, context: Context) -> Context:
        """Run the Documentation engine."""
        trace = context.setdefault("trace", [])
        trace.append(
            {
                "system": "DOMAIN_SYSTEM",
                "category": "engines",
                "component": "Documentation_Engine",
                "domain_id": "documentation",
                "event": "run",
            }
        )
        return context

---

---

### Source 3: AMOS Corporate Documentation Engine

> Path: `engine/D/Documentation_Engine_Model.md` | Size: 1999 chars | Match score: 13 | content_hash: 4091bbfea74f6524

# AMOS Corporate Documentation Engine


The **Corporate Documentation & Layout Engine** standardizes the creation, formatting, and governance of all corporate document types, from chat messages and emails to board packs and legal contracts.

## The 12 Document Clusters (C01-C12)

1. **C01_corp_brand_language:**

Brand voice, tone, style guides.
2. **C02_structured_docs_reports:**

Memos, reports, decision briefs.
3. **C03_presentation_design:**

Pitch decks, slides.
4. **C04_chat_email_comms:**

Executive updates, chat, operational comms.
5. **C05_legal_and_contracts:** MSAs, privacy, HR contracts.
6. **C06_admin_hr_ops_docs:**

Employee handbooks, onboarding, checklists.
7. **C07_product_and_tech_docs:** PRDs, API specs, user guides.
8. **C08_marketing_and_brand_assets:**

Blogs, campaigns, case studies.
9. **C09_exec_board_investor_packs:**

Board decks, investor updates.
10. **C10_knowledge_wiki_and_search:**

Runbooks, FAQ, wiki.
11. **C11_multilingual_and_localisation:**

Translation, jurisdiction variants.
12. **C12_layout_systems_and_templates:**

Grid rules, components, templates.

## Governance & Overlays

To ensure safety and structural consistency, the engine applies overlays before outputting text:
- **Formatting:** Enforces headings, lists, and spacing appropriate for the target channel.
- **Compliance:** Injects mandatory legal disclaimers.
- **Governance:** Legal, HR, and Policy documents are always marked as `DRAFT_REQUIRES_HUMAN_REVIEW`. The AI does not have the final authority to publish binding policies.

---

---
**MOC:** [[references_MOC]]

## Related

- [[07_SKILLS_MOC]]
---

**Related:** [[00_HOME]] · [[AMOS_RSCF_NODES]] · [[LAW_HIERARCHY]] · [[references_MOC]] · [[07_SKILLS_MOC]]

**MOC:** [[references_MOC]]

**Trang Framework:** [[TRANG_FRAMEWORK_RECURSIVE_ONTOLOGY_DYNAMICS]]

---
RSCF-NODE
node_id: amos-structured-document-parsing-rscf-vault-domain-knowledge
node_type: reference
path: 07_SKILLS/amos-structured-document-parsing-rscf/references/vault_domain_knowledge.md
RSCF-RELATIONS:
- INDEXED_BY: [[00_HOME]]
- INDEXED_BY: [[AMOS_RSCF_NODES]]
- CHILD_OF: [[references_MOC]]
