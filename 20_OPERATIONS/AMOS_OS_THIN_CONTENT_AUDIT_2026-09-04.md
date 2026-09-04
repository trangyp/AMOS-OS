---
canon-group: meta
canon-type: framework
rscf-state: source-claim
rscf-claim: verified
rscf-provenance: AMOS_corpus
conclusion_class: AMOS_MODEL
epistemic_class: SOURCE_CLAIM
topic: Amos Os Thin Content Audit 2026 09 04
tags:
  - canon-group/tech-ai
  - rscf/claim
  - rscf/provenance
  - rscf/state/source-claim
  - misc
created: 2026-08-22
---
---
# AMOS_OS Vault Thin-Content Audit Report
**Date:** 2026-09-04  
**Total .md files scanned:** 7,472  
**Files with issues:** 4,753 (63.6%)  
**Unclosed code fences:** 0  

---

## Executive Summary

The vault has a **systemic thin-content problem**. The majority of files across all directories are structural shells — YAML frontmatter with minimal or no substantive body content. The most affected directories are:

| Directory | Thin / Total | % | Primary Issue |
|---|---|---|---|
| 25_COGNITIVE_MATRIX | 1,587 / 1,677 | **95%** | Generated template cells |
| 26_WORKFLOWS | 342 / 351 | **97%** | Boilerplate workflow stubs |
| 16_SCHEMAS | 30 / 31 | **97%** | Schema stubs with no body |
| 09_PROTOCOLS | 10 / 11 | **91%** | Protocol stubs |
| 19_TESTS | 12 / 13 | **92%** | Empty test contracts |
| 23_OPERATING_MODEL | 41 / 43 | **95%** | Template operating model |
| 12_STATE | 9 / 10 | **90%** | Snapshot-only |
| 03_CONTROL_PLANE | 685 / 789 | **87%** | Placeholder modes/specs |
| 01_CANON | 332 / 376 | **88%** | Registry stubs |
| 21_DOMAINS | 330 / 384 | **86%** | Domain stubs |
| 00_ROOT | 85 / 99 | **86%** | Index/registry stubs |
| 20_OPERATIONS | 77 / 89 | **87%** | Audit receipt files |

---

## SECTION 1: Critically Thin Files (under 20 lines)

Only 1 file found in this category:

**`24_ARCHIVE/01_CANON_google_drive_sync_conflicts_2026-09-03/01_CORE_LAWS (1)/LAW_HIERARCHY.md`** — 10 lines, 3 non-empty body lines. Archive conflict remnant.

---

## SECTION 2: Thin Files (20–50 lines) — Frontmatter Dominant

These files are mostly YAML with almost no body:

| File | Lines | Body | FM% |
|---|---|---|---|
| `11_KNOWLEDGE/engine/AMOS_COGNITION_ENGINE_LAYER.md` | 40 | 9 | 55% |
| `11_KNOWLEDGE/engine/AMOS_EMOTION_ENGINE_LAYER.md` | 40 | 9 | 55% |
| `11_KNOWLEDGE/engine/AMOS_CONSCIOUSNESS_ENGINE_LAYER.md` | 40 | 9 | 55% |
| `11_KNOWLEDGE/engine/AMOS_CODING_ENGINE_LAYER.md` | 41 | 10 | 54% |
| `11_KNOWLEDGE/engine/AMOS_ORG_GOVERNANCE_ENGINE_LAYER.md` | 41 | 10 | 54% |
| `11_KNOWLEDGE/engine/AMOS_AUTOMATION_ENGINE_LAYER.md` | 41 | 10 | 54% |
| `11_KNOWLEDGE/engine/AMOS_PERSONALITY_ENGINE_LAYER.md` | 41 | 10 | 54% |
| `11_KNOWLEDGE/engine/AMOS_DESIGN_LANGUAGE_ENGINE_LAYER.md` | 41 | 10 | 54% |
| `11_KNOWLEDGE/engine/AMOS_PHYSICS_COSMOS_ENGINE_LAYER.md` | 41 | 10 | 54% |
| `11_KNOWLEDGE/engine/AMOS_MECHANICAL_STRUCTURAL_ENGINE_LAYER.md` | 41 | 10 | 54% |
| `11_KNOWLEDGE/engine/AMOS_LEGAL_ENGINE_LAYER.md` | 41 | 10 | 54% |
| `11_KNOWLEDGE/engine/AMOS_RISK_COMPLIANCE_ENGINE_LAYER.md` | 41 | 10 | 54% |
| `11_KNOWLEDGE/engine/AMOS_ELECTRICAL_POWER_ENGINE_LAYER.md` | 41 | 10 | 54% |
| `11_KNOWLEDGE/engine/AMOS_NUMERICAL_METHODS_ENGINE_LAYER.md` | 41 | 10 | 54% |
| `11_KNOWLEDGE/engine/AMOS_DOCUMENTATION_ENGINE_LAYER.md` | 41 | 10 | 54% |

**What they have:** YAML frontmatter + 1 line saying "Bridge note" + a link to a skill folder.  
**What they should contain:** Full engine layer specifications with domains, operators, equations, invariants.

---

## SECTION 3: Frontmatter-Dominant Files (50–200 lines, >50% frontmatter)

**46 files** in `21_DOMAINS/` have 54–55% frontmatter with only ~34 non-empty body lines. These are domain specification stubs that should contain domain-specific knowledge, laws, and ontologies.

Key pattern: Every `*_DOMAIN_SPEC.md` and `*_CONTRACT.md` in `21_DOMAINS/` subdirectories follows this template structure with minimal body.

Also affected:
- `04_RUNTIME/06_EXECUTION/SENSITIVITY_RUNTIME.md` (52% FM, 35 body)
- `04_RUNTIME/06_EXECUTION/UNCERTAINTY_VECTOR_RUNTIME.md` (51% FM, 36 body)
- `04_RUNTIME/09_FINALIZATION/CAUSAL_EPOCH_FINALIZER.md` (51% FM, 36 body)

---

## SECTION 4: Template/Boilerplate-Only Files

The `11_KNOWLEDGE/engine/` directory contains **15+ files** that are all identical bridge-note stubs (40–42 lines each). Each says:

> "Bridge note — resolves the `amos-*-engine-layer` link from the Cosmo Brain MOC"

These are redirect stubs, not engine specifications. They should contain full engine layer specs.

---

## SECTION 5: UNKNOWN/GAP Marker Analysis

**Massive pattern found:** Files containing `UNKNOWN/GAP` as their primary content rather than as a legitimate gap marker.

### 5a. 25_COGNITIVE_MATRIX RSCF Files (~50 files, 74 lines each)
Every `*_RSCF.md` file in `01_PRIMITIVES/`, `02_LIFECYCLE_OPERATIONS/`, `03_CONTROL_PLANES/`, `04_SCALES/` is exactly **74 lines** with the same template structure and `UNKNOWN/GAP` as the substantive content. These are generated placeholder RSCF contracts.

**Files affected (sample):**
- `25_COGNITIVE_MATRIX/01_PRIMITIVES/L*_PRIMITIVES_COGNITIVE_MATRIX_RSCF.md` (~30 files)
- `25_COGNITIVE_MATRIX/02_LIFECYCLE_OPERATIONS/O*_*_LIFECYCLE_OPERATIONS_COGNITIVE_MATRIX_RSCF.md` (~18 files)
- `25_COGNITIVE_MATRIX/03_CONTROL_PLANES/C*_*_CONTROL_PLANES_COGNITIVE_MATRIX_RSCF.md` (~9 files)
- `25_COGNITIVE_MATRIX/04_SCALES/*_SCALES_COGNITIVE_MATRIX_RSCF.md` (3 files)

### 5b. 01_CANON Provenance/Supercession Registries (~30 files, 151–160 lines)
Files like `CANON_HERITAGE_REGISTRY.md`, `CANON_IP_REGISTRY.md`, `CANON_VERSION_REGISTRY.md`, all `*_PROVENANCE.md` files, and all `*_SUPERSESSION.md` files contain 150+ lines of mostly `UNKNOWN/GAP` placeholders and governance boilerplate with no actual registry data.

### 5c. 07_SKILLS SKILL.md Files (~200+ files, 238–260 lines)
Almost every skill file contains the same template structure with `UNKNOWN/GAP` in the vault_domain_knowledge sections. The body is structural scaffolding, not skill-specific knowledge.

### 5d. 11_KNOWLEDGE Master Knowledge Files (7 files, 679–1989 lines)
Large files like `AMOS_C07_ECON_FINANCE_MASTER_KNOWLEDGE.md` (715 lines) contain sections that are mostly `UNKNOWN/GAP` placeholders interspersed with structural boilerplate.

---

## SECTION 6: Critical Architectural Files That Are Thin

| File | Expected Content | Actual Content |
|---|---|---|
| `13_MODELS/01_FOUNDATION/UBA_MODEL.md` | Full UBA model spec | 1,900 lines of "we don't know what UBA means" governance |
| `09_PROTOCOLS/TASK_HANDOFF_PROTOCOL.md` | Complete protocol spec | 346 lines, starts with real content but 97% thin per marker scan |
| `09_PROTOCOLS/KNOWLEDGE_PROVENANCE_BINDING_PROTOCOL.md` | Binding protocol | 443 lines of governance meta-documentation |
| `10_MEMORY/TIERED_MEMORY_LIFECYCLE_ARCHITECTURE.md` | Memory architecture | Listed as thin, template-heavy |
| `10_MEMORY/10_MEMORY_README.md` | Memory plane overview | Contains UNKNOWN/GAP markers |
| `00_ROOT/AMOS_TOTAL_FRAMEWORK_REGISTRY.md` | Master framework registry | 105 lines, mostly UNKNOWN/GAP |
| `00_ROOT/AMOS_TOTAL_ARCHITECTURE.md` | Architecture overview | 227 lines, UNKNOWN/GAP throughout |

---

## SECTION 7: Duplicate/Near-Duplicate Content

### 7a. Triple-README Pattern
Many directories have 3 README files:
- `{DIR}_README.md`
- `{NN}_{DIR}_README.md`
- `README.md`

Example: `10_MEMORY/` has `MEMORY_README.md`, `10_MEMORY_README.md`, and `10_MEMORY_MOC.md` — all thin.

### 7b. 11_KNOWLEDGE/engine/ — 15 Identical Bridge Notes
All engine layer files (`AMOS_COGNITION_ENGINE_LAYER.md`, `AMOS_EMOTION_ENGINE_LAYER.md`, etc.) are structurally identical with only the name changed. Each is a 40-line redirect stub.

### 7c. 25_COGNITIVE_MATRIX RSCF Files — ~50 Near-Identical Templates
All `_RSCF.md` files in the cognitive matrix are 74 lines of the same template with only the primitive/operation name swapped.

### 7d. AGENT_SCHEMA.md Duplicated
`16_SCHEMAS/06_AGENTS/agent.schema.md` (1,820 lines) is identical to `11_KNOWLEDGE/AGENT_SCHEMA.md` (1,842 lines) and `06_AGENTS/AMOS_AGENT_SCHEMA_FULL.md` (1,820 lines).

### 7e. 00_ROOT Duplicate Registries
`AMOS_TOTAL_FRAMEWORK_REGISTRY.md`, `AMOS_FRAMEWORK_STATUS_MASTER.md`, `AMOS_FRAMEWORK_ALIAS_MASTER.md`, `AMOS_FRAMEWORK_DEPENDENCY_MASTER.md`, `AMOS_FRAMEWORK_PLACEMENT_MASTER.md` — five framework registry files with overlapping content.

---

## SECTION 8: Missing MOC Files

Most subdirectories already have MOC files. No significant missing MOCs found — the vault has over-generated navigation files at the expense of content.

---

## SECTION 9: Naming Convention Inconsistencies

1. **Mixed case:** `AMOS Global Contract for AI Coding Agents.md` uses spaces; all others use underscores.
2. **Duplicate directory numbers:** Both `08_PLANETARY/` and `26_WORKFLOWS/` share prefix `08_`.
3. **Inconsistent README naming:** Some dirs use `{NN}_{DIR}_README.md`, others use `README.md`, others `{DIR}_README.md`.
4. **Archive path with spaces:** `24_ARCHIVE/01_CANON_google_drive_sync_conflicts_2026-09-03/01_CORE_LAWS (1)/` has spaces in directory name.

---

## SECTION 10: Orphaned Files

The following appear unlinked from any index/MOC based on naming patterns:
- `00_ROOT/Agent Skills.md` (space in name, non-standard)
- `00_ROOT/AMOS MOC.md` (space in name, duplicates `MOC.md` and `00_ROOT_MOC.md`)
- Multiple `*_README.md` variants that aren't referenced from parent MOCs

---

## Summary Statistics

| Category | Count |
|---|---|
| Total .md files | 7,472 |
| Files with thin markers | ~4,753 |
| Files with UNKNOWN/GAP as content | ~500+ |
| Files under 50 lines | ~25 |
| Files 50–200 lines with <10 body lines | ~46 |
| Frontmatter-dominant (50%+) | ~100+ |
| Duplicated schema files | 3 (AGENT_SCHEMA) |
| Identical bridge-note stubs | 15 |
| Generated 74-line RSCF templates | ~50 |
| Total estimated thin content files | **~3,200+** |

---

## Recommendations

1. **Highest priority:** The ~50 generated 74-line RSCF files in `25_COGNITIVE_MATRIX/` should be consolidated into a single template with instance data, or expanded with actual content.
2. **11_KNOWLEDGE/engine/** bridge notes should be replaced with actual engine specifications or removed.
3. **07_SKILLS** SKILL.md files need real workflow/content bodies, not just structural scaffolding.
4. **01_CANON registries** need actual registry data populated, not just governance meta-documentation.
5. **Triple-README files** should be consolidated — each directory needs exactly one README.
6. **Duplicated AGENT_SCHEMA** should be consolidated to one canonical location.
7. **Frontmatter-heavy domain specs** in `21_DOMAINS/` should have their body content expanded.
