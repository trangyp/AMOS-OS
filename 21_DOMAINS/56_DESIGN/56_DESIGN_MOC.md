---
title: 05 Design MOC
type: moc
source: 21_DOMAINS/56_DESIGN
tags:
  - 05-design
  - canon/domain
  - bio-logical-architecture-design
  - design-domains-domain-spec
  - design-domains-interfaces
  - design-domains-provenance
  - design-for-absolute-integrity
  - irreducible-systems-design
moc: true
rscf:
  state: DERIVED
  claim_class: DERIVED
  provenance: AMOS_corpus
  scope: AMOS_general
---

# 05 Design — Map of Content

**Path:** `21_DOMAINS/56_DESIGN`
**Files:** 8 | **Subdirectories:** 1

## Files

- [[21_DOMAINS/56_DESIGN/BIO_LOGICAL_ARCHITECTURE_DESIGN|BIO_LOGICAL_ARCHITECTURE_DESIGN]]
- [[21_DOMAINS/56_DESIGN/DESIGN_DOMAINS_DOMAIN_SPEC|DESIGN_DOMAINS_DOMAIN_SPEC]]
- [[21_DOMAINS/56_DESIGN/DESIGN_DOMAINS_INTERFACES|DESIGN_DOMAINS_INTERFACES]]
- [[21_DOMAINS/56_DESIGN/DESIGN_DOMAINS_PROVENANCE|DESIGN_DOMAINS_PROVENANCE]]
- [[21_DOMAINS/56_DESIGN/DESIGN_DOMAINS_README|DESIGN_DOMAINS_README]]
- [[11_KNOWLEDGE/05_FRAMEWORKS/DESIGN_FOR_ABSOLUTE_INTEGRITY|DESIGN_FOR_ABSOLUTE_INTEGRITY]]
- [[21_DOMAINS/56_DESIGN/DOMAINS_DESIGN_CONTRACT|DOMAINS_DESIGN_CONTRACT]]
- [[21_DOMAINS/56_DESIGN/IRREDUCIBLE_SYSTEMS_DESIGN|IRREDUCIBLE_SYSTEMS_DESIGN]]

## Subdirectories

- [[01_CANON/00_INDEX/00_INDEX_MOC|00_INDEX_MOC]] — 00_INDEX

______________________________________________________________________


## Domain Scope

The Design domain covers visual design, UX/UI, design systems, and design language within AMOS OS:

### Sub-domains
- **Design systems**: design tokens (W3C), component libraries, design language (Material 3, Fluent 2, HIG, Carbon)
- **UX/UI**: user research, wireframing, prototyping, usability testing, accessibility (WCAG 2.2)
- **Visual design**: typography, color theory (OKLCH), layout (Gestalt), visual hierarchy, branding
- **Design tools**: Figma (Dev Mode, variables), Sketch, Adobe XD; design-to-code handoff

### SOTA Methods
- **Design tokens**: W3C Design Tokens Format Module; primitive → semantic → component tokens
- **Component libraries**: Radix UI, shadcn/ui, Headless UI; accessible primitives
- **Accessibility**: WCAG 2.2 (A/AA/AAA); semantic HTML; ARIA; keyboard navigation; screen reader testing
- **AI design**: Figma AI, Galileo AI, v0.dev; LLM-generated UI; design-to-code automation

### AMOS Integration
- **C11 domain**: [[21_DOMAINS/21_C11_DESIGN_LANGUAGE/21_C11_DESIGN_LANGUAGE_MOC|C11 design-language domain]]
- **Design language engine**: [[11_KNOWLEDGE/engine/AMOS_DESIGN_LANGUAGE_ENGINE_LAYER|Design Language Engine]]
- **Documentation engine**: [[11_KNOWLEDGE/engine/AMOS_DOCUMENTATION_ENGINE_LAYER|Documentation Engine]]

### Invariants
1. `DESIGN_TOKEN != DESIGN_SYSTEM` — tokens are primitives, not a complete system
2. `ACCESSIBLE != USABLE` — WCAG compliance is necessary but not sufficient
3. All design claims must cite provenance (standard, version, guideline reference)


**Parent:** [[21_DOMAINS/21_DOMAINS_MOC|21_DOMAINS_MOC]]
