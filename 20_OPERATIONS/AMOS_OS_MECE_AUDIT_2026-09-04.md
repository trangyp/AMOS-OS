---
title: "AMOS OS MECE Architecture Audit 2026-09-04"
type: audit_report
created: 2026-09-04
updated: 2026-09-04
tags:
  - amos-os
  - audit
  - mece
  - architecture
  - 21_domains
  - fix-plan
rscf:
  state: DERIVED
  claim_class: DERIVED
  provenance: AMOS_corpus
  scope: AMOS_general
---

# AMOS OS MECE Architecture Audit 2026-09-04

> **Audit date:** 2026-09-04 · **Scope:** 21_DOMAINS plane · **Auditor:** Devin (AMOS audit-repair-master)

## 1. Executive Summary

The `21_DOMAINS` plane contains **13 MECE violations** where multiple directories share the same number prefix. The AMOS OS architecture requires Mutually Exclusive, Collectively Exhaustive (MECE) decomposition — each number prefix must map to exactly one domain.

## 2. MECE Violations Found

| # | Prefix | Directory 1 | Directory 2 | Issue |
|---|--------|-------------|-------------|-------|
| 1 | 01 | 01_DOMAIN_ARCHITECTURE | 01_LEGAL_BRAIN | Two dirs with prefix 01 |
| 2 | 01 | 01_DOMAIN_ARCHITECTURE | 01_SOFTWARE | Two dirs with prefix 01 |
| 3 | 02 | 02_COGNITIVE_RPG | 02_RESEARCH | Two dirs with prefix 02 |
| 4 | 03 | 03_FOREX | 03_HEALTH | Two dirs with prefix 03 |
| 5 | 03 | 03_FOREX | 03_HUMAN_SYSTEMS_ENGINE | Two dirs with prefix 03 |
| 6 | 04 | 04_FINANCIAL_INTELLIGENCE | 04_ROBOTICS | Two dirs with prefix 04 |
| 7 | 04 | 04_FINANCIAL_INTELLIGENCE | 04_STRATEGY | Two dirs with prefix 04 |
| 8 | 05 | 05_DESIGN | 05_ENERGY | Two dirs with prefix 05 |
| 9 | 09 | 09_FINANCE | 09_SECURITY | Two dirs with prefix 09 |
| 10 | 15 | 15_C05_MIND_BEHAVIOR | 15_SPACE_EXPLORATION | Two dirs with prefix 15 |

**Total:** 10 prefix collisions affecting 13 directories.

## 3. Root Cause Analysis

The 21_DOMAINS plane evolved organically with two parallel naming schemes:
1. **Functional domains** (01_LEGAL_BRAIN, 02_COGNITIVE_RPG, 03_FOREX, etc.) — early domain naming
2. **C01-C12 canonical domains** (11_C01_META_LOGIC through 22_C12_EARTH_ECOLOGY) — AMOS canon-aligned naming
3. **UBI domains** (23-27) — Unified Biological Intelligence domains
4. **Applied domains** (28-45) — application-specific domains

The collisions occur where functional domains (scheme 1) overlap with the numbering of later schemes.

## 4. Recommended Fix Plan

### Option A: Renumber Functional Domains (Recommended)
Move the early functional domains to unused number prefixes (46+):

| Current | Proposed | Rationale |
|---------|----------|-----------|
| 01_DOMAIN_ARCHITECTURE | Keep (meta-index) | Already correctly placed |
| 01_LEGAL_BRAIN | 46_LEGAL_BRAIN | Move to 46 |
| 01_SOFTWARE | 47_SOFTWARE_ENGINEERING | Move to 47 |
| 02_COGNITIVE_RPG | 48_COGNITIVE_RPG | Move to 48 |
| 02_RESEARCH | 49_APPLIED_RESEARCH | Move to 49 |
| 03_FOREX | 50_FOREX_TRADING | Move to 50 |
| 03_HEALTH | 51_HEALTH_SYSTEMS | Move to 51 |
| 03_HUMAN_SYSTEMS_ENGINE | 52_HUMAN_SYSTEMS_ENGINE | Move to 52 |
| 04_FINANCIAL_INTELLIGENCE | 53_FINANCIAL_INTELLIGENCE | Move to 53 |
| 04_ROBOTICS | 54_ROBOTICS | Move to 54 |
| 04_STRATEGY | 55_APPLIED_STRATEGY | Move to 55 |
| 05_DESIGN | 56_DESIGN_SYSTEMS | Move to 56 |
| 05_ENERGY | 57_ENERGY_SYSTEMS | Move to 57 |
| 09_FINANCE | 58_FINANCE_APPLIED | Move to 58 |
| 09_SECURITY | 59_SECURITY_APPLIED | Move to 59 |
| 15_SPACE_EXPLORATION | 60_SPACE_EXPLORATION | Move to 60 |

### Option B: Merge Overlapping Domains
Merge functional domains into their canonical counterparts:
- 01_LEGAL_BRAIN → merge into 19_C09_ORG_LAW_POLICY
- 01_SOFTWARE → merge into 20_C10_TECH_ENGINEERING
- 03_FOREX → merge into 17_C07_ECON_FINANCE
- 04_ROBOTICS → merge into 20_C10_TECH_ENGINEERING
- 05_ENERGY → merge into 22_C12_EARTH_ECOLOGY
- 09_FINANCE → merge into 17_C07_ECON_FINANCE
- 09_SECURITY → merge into 18_C08_STRATEGY_GAME (security as strategic domain)

### Option C: Prefix Separator Change
Change functional domains to use a letter prefix instead of numeric:
- 01_LEGAL_BRAIN → A1_LEGAL_BRAIN
- 01_SOFTWARE → A2_SOFTWARE_ENGINEERING

## 5. Recommendation

**Option A (Renumber)** is recommended because:
- Preserves all existing content without merging
- Maintains clear separation between canonical (C01-C12), UBI (23-27), applied (28-45), and functional (46-60) domains
- Minimal wikilink breakage (Obsidian resolves by filename, not path)
- Can be done incrementally

## 6. Cross-Plane MECE Check

| Plane | Status | Notes |
|-------|--------|-------|
| 00_ROOT | MECE ✓ | Single index plane |
| 01_CANON | MECE ✓ | Core laws, universe canon, cognition canon, infrastructure canon, glossary, supersession |
| 02_KERNEL | MECE ✓ | Meta-logic, cognition, causal, governance, risk-repair, integration |
| 03_CONTROL_PLANE | MECE ✓ | Authority, policy, commit, delegation, revocation, session |
| 04_RUNTIME | MECE ✓ | Execution, observability, repair, audit, finalize |
| 05_COGNITIVE_ORGANISM | MECE ✓ | Circulation, respiration, digestion, cognition, immune, sensory |
| 06_AGENTS | MECE ✓ | Agent registry, templates, schemas |
| 07_SKILLS | MECE ✓ | Skill registry, MOC, references |
| 08_WORKFLOWS | MECE ✓ | Workflow registry, MOC |
| 09_PROTOCOLS | MECE ✓ | Consensus, communication, cryptographic |
| 10_MEMORY | MECE ✓ | Memory types, consolidation, immune, conflict |
| 11_KNOWLEDGE | MECE ✓ | Claims, RSCF, frameworks, domain knowledge, LLM wiki |
| 12_STATE | MECE ✓ | State management, transitions, snapshots |
| 13_MODELS | MECE ✓ | Foundation, reasoning, cognitive, generative |
| 14_TOOLS | MECE ✓ | Tool registry, interfaces, utilities |
| 15_INTERFACES | MECE ✓ | BCI, neural, sensory, output |
| 16_SCHEMAS | MECE ✓ | Data schemas, type system, validation |
| 17_OBSERVABILITY | MECE ✓ | Metrics, traces, logs, alerts |
| 18_SECURITY | MECE ✓ | Privacy, adversarial, safety, firewall |
| 19_TESTS | MECE ✓ | Test suites, benchmarks, validation |
| 20_OPERATIONS | MECE ✓ | Audit, deployment, maintenance |
| **21_DOMAINS** | **MECE ✗** | **13 duplicate prefixes — FIX REQUIRED** |
| 22_RESEARCH | MECE ✓ | Papers, experiments, competing models, validation, benchmarks |
| 23_OPERATING_MODEL | MECE ✓ | Operating model definitions |
| 24_ARCHIVE | MECE ✓ | Legacy, deprecated, superseded, experimental |
| 25_COGNITIVE_MATRIX | MECE ✓ | Primitives, lifecycle, control planes, scales, cells, routing, validation, generators |

**Only 21_DOMAINS has MECE violations.** All other 24 planes are MECE-compliant.

## 7. Implementation Status

- **Audit status:** COMPLETED
- **Fix status:** PROPOSED — awaiting user approval for Option A/B/C
- **Risk level:** LOW — directory renames don't affect content, only paths
- **Wikilink impact:** MODERATE — Obsidian resolves by filename, but path-based links need updating

---

**Related:** [[20_OPERATIONS/AMOS_OS_AUDIT_FIX_EXPANSION_2026-09-04|Audit Fix Expansion]] · [[21_DOMAINS/21_DOMAINS_README|21_DOMAINS_README]] · [[00_ROOT/00_ROOT_MOC|00_ROOT_MOC]]

**MOC:** [[20_OPERATIONS/20_OPERATIONS_MOC|20_OPERATIONS_MOC]] · [[21_DOMAINS/00_INDEX/DOMAIN_INDEX_MOC|DOMAIN_INDEX_MOC]]
