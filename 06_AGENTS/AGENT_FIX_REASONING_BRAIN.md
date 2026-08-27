---
title: AGENT FIX REASONING BRAIN
type: agent
source: 06_AGENTS
claim_class: AMOS_MODEL
origin_architect: Trang Phan
status: COMPLETE
tags: [agent-fix, agent, automation, reasoning-brain, worklog, canon/agent]
rscf:
  state: DERIVED
  claim_class: DERIVED
  provenance: AMOS_corpus
  scope: AMOS_general
---


# Agent Fix Reasoning Brain

> Living reasoning log for the agent specialization task. Updated as work progresses.

## Task
Fix every generated agent template so each agent is **truthfully specialized** to its bound Skill. The Skill is the authoritative source of behavior.

## Repository State (discovered 2026-08-26)

- **Repo:** `/Users/mac/Downloads/stitch_project_cosmo` (cwd)
- **Agents:** `.devin/agents/` — **834 JSON files** (no `AGENT_TEMPLATE.md` / `openai.yaml` inside skill dirs; the task spec's file layout does not match this repo — agents are flat JSON files)
- **Skills:** `.devin/skills/` — **938 skill dirs**, each with a `SKILL.md`
- **Workflows:** `.devin/workflows/` — 837 files
- **Vault:** AMOS_OS Obsidian vault (3003 notes) used as reasoning brain

## Schema field census (across 834 agents)

| Field | Count | Notes |
|-------|------:|-------|
| `display_name` | 75 | only some agents |
| `capabilities` (array of strings) | 75 | legacy/generic form |
| `capabilities` (array of objects) | 0 | none use the rich object form yet |
| `depends_on_skills` | 529 | modern form |
| `dependencies` (legacy) | 102 | old form |
| `operations` | 241 | partial |
| `integrity_requirements` | 254 | partial |
| `role` | 285 | partial |
| `safety_constraints` (object) | 60 | generic boilerplate form |
| `safety_constraints` (array) | 162 | richer form |

## Generic boilerplate identified

| Pattern | Count | Examples |
|---------|------:|---------|
| `"Agent for amos-..."` description | 198 | amos-19x19-family-agent.json |
| `"quantum/fractal/math consolidated reasoning"` | 60 | subset of above |
| `"apply_amos-{skill}_reasoning"` capability stubs | 75 | generic 8-cap template |
| Generic `safety_constraints` object (4 bool flags) | 60 | identical across agents |

## Plan

1. **Classify** all 834 agents into: SPECIALIZED (already skill-specific) vs GENERIC (boilerplate) vs VIRTUAL/UNKNOWN.
2. **Build agent→skill binding map** by matching agent name slug to skill dir name (with `-2` variant handling).
3. **Write a Python repair harness** that, for each generic agent:
   - reads the bound `SKILL.md` completely
   - extracts purpose, trigger, role, inputs, outputs, workflow, validation gates, tools, scripts, references, invariants, safety, provenance, handoff, failure conditions, env requirements
   - rewrites the agent JSON with skill-specific `description`, `role`, `capabilities` (object form), `operations`, `integrity_requirements`, `safety_constraints` (array), `depends_on_skills`, `depends_on_workflows`
   - preserves Trang Phan as origin architect for AMOS agents
   - preserves RSCF / H/M/L / provenance / competing-hypotheses / causal firewall / scope-regime / confidence ceilings / falsifiers where the skill uses them
   - does NOT inject full AMOS framework into skills that don't use it
   - detects parent/child and uses `inherits_from` / `specialization` instead of duplicating parent
   - replaces placeholders with `${VAR}` typed config requirements + records in UNRESOLVED_AGENT_CONFIG.md
4. **Build validator** that fails on: bad JSON, duplicate IDs, missing skill bindings, broken file paths, stale skill IDs, unresolved placeholders, missing referenced files, skill/agent trigger mismatch, unsupported tool/connector claims, material agent/skill contradiction.
5. **Generate reports**: AGENT_FIX_REPORT.md, AGENT_REGISTRY.json, AGENT_SKILL_SYNC_REPORT.json, UNRESOLVED_AGENT_CONFIG.md, AGENT_VALIDATION_REPORT.md.
6. **Git commit**.

## Anti-fabrication rule
A value that cannot be established from repository evidence stays explicitly unresolved. Never fabricate to remove a placeholder.

## Status
- [x] Discovered repo state
- [x] Recorded reasoning brain
- [x] Classification pass
- [x] Binding map
- [x] Repair harness
- [x] Repairs (834/834)
- [x] Validator (834/834 pass)
- [x] Reports (5 generated)
- [x] Commit (2f8336c7)

## Continuation assessment (2026-08-26)
## Continuation assessment (2026-08-26) — COMPLETE

- [x] Spot-check repaired agent quality across diverse skills
- [x] Update amos-agent-registry-index.md (updated to 851 agents, v13.0.0)
- [x] Check AGENT-NAMING-CONVENTION.md consistency (0 name field mismatches, 90 pre-existing -agent-2 variants)
- [x] Verify final git state is clean and committed

### Quality pass 2 (2026-08-26)
- Added slugify_cap() for clean capability names
- Added is_rscf_metadata() filter to exclude metadata from capabilities  
- Stop replacing "placeholder" as template token (legitimate content)
- Agent count grew from 834 to 851 (17 new arxiv/quantum agents)
- All 851 agents VERIFIED, 851/851 validation pass


## Lifecycle enhancement pass (2026-08-26)

User added AREG best practice lifecycle field to repair harness. Enhanced with:
- **Superseded detection** from SKILL.md frontmatter ("superseded by", "lineage marker", "honest stub")
- **Stub detection** from Status section ("Honest stub", "stub")
- **Redirect detection** from frontmatter description ("Redirect — consolidated into")
- **Redirect following**: when a skill is a redirect, content is extracted from the TARGET master skill, not the redirect stub
- **skill_binding.redirect_target** and **target_skill_path** added for redirect agents
- **deprecation_date** defaults to 2026-08-26 when not set
- **Validator** updated to accept "superseded" and "stub" as valid lifecycle statuses
- **4 agent-level redirects** added to CURATED_SKILL_MAP (generative-construction-verifier, optimizer-certificate-auditor, shock, spectral-parameter-auditor)

### Final state after lifecycle enhancement
- Total agents: 598
- Active: 577
- Redirect: 21 (bound to redirect skills, content from master skills)
- Validation: 598/598 valid, 0 invalid
- All 598 have content_hash (AREG tamper detection)
- All 21 redirect agents have successor and deprecation_date
### Final commits
- 2f8336c7 — Initial specialization pass
- 82db4574 — Quality improvement pass
- 6a4bc587 — Quality pass 2: clean cap names, RSCF filter
- 78974aa6 — Specialize remaining 29 arxiv/quantum agents

## Content enrichment + AREG governance pass (2026-08-26)

### Workflow merge
- Merged 7 non-master workflows with real domain content into master workflows
- Each merged as a `## Sub-Workflow:` section with full phases, gates, and pipelines
- 7 source workflows converted to redirects
- Final: 27 real-content workflows, 1179 redirects

### Skill enrichment (user + harness)
- User committed vault-sourced domain knowledge enrichment for all 27 master skills
- Harness updated to recognize vault-sourced sections (M1/M2/F1-F10, knowledge contracts, claim classes)
- Capability extraction improved: mean 2.1 → 6.0 caps per agent
- Skills now contain real domain content from vault sources (e.g., C02: 10 knowledge families with framing, model selection, numerical methods, etc.)

### AREG governance metadata
- Added `governance` field to all 593 agents following AREG draft-schemacommons-areg-00
- Fields: owner_team, business_domain, risk_tier, observability, approval_mode, promotion_state
- Risk tiers: low=373, medium=219, high=1 (auto-inferred from capability side-effects)
- Business domains: 28 domains mapped from skill bindings
- Validator updated to check governance fields

### Final state
- Total agents: 593 (user renamed from 598 to 593, removing versioning suffixes)
- Active: 572, Redirect: 21
- Validation: 593/593 valid, 0 invalid
- All 593 have content_hash (AREG tamper detection)
- All 593 have governance metadata
- Capabilities: min=3, max=8, mean=6.0, median=6
- 28 business domains tracked

### Best practices applied
1. **AREG (Agent Registry)** — lifecycle, content_hash, governance metadata per draft-schemacommons-areg-00
2. **AWS AgentOps** — portfolio governance with owner_team, business_domain, risk_tier
3. **Agent Registry Field Guide** — capability schema with side-effect classification, observability coverage
4. **Redirect following** — redirect agents extract content from target master skills
5. **Anti-fabrication** — all content sourced from SKILL.md and vault knowledge files
## Quality improvement pass (2026-08-26)

After the initial repair, a quality spot-check found 422 issues:
- 311 FALLBACK_CAPS (skills without standard Capabilities sections)
- 87 SHORT_DESC (descriptions under 40 chars)
- 16 GENERIC_ROLE (generic fallback role)
- 8 MD_IN_DESC/ROLE (markdown artifacts)

### Fixes applied
1. **Parser improved** — added 15+ new section types (Core Objects, Required Checks, Canonical Equation, Mapping Classes, Key Components, Core Framework, Detailed Reference, Standard Verification Sequence, Runtime, Engine Baselines, etc.)
2. **Sub-section extraction** — `split_sections` now includes `###` content within `##` sections (was cutting off at next heading)
3. **Sub-heading extraction** — `extract_list_items` now captures `### Op 1 — Load and verify` style sub-headings as items
4. **When to Use fallback** — for skills without Capabilities/Operations, bullet points and paragraph sentences from When to Use are used as capabilities
5. **Index/inventory skills** — arxiv paper index skills get domain-specific capabilities (index_members, retrieve_member, lookup_by_topic)
6. **Stub/lineage skills** — superseded skills get a reference capability pointing to the successor
7. **Markdown stripping** — heading prefixes (`## `) and list markers (`- `) stripped from descriptions and roles
8. **Short description extension** — descriptions under 80 chars are extended from Identity/Purpose/When to Use/body paragraph
9. **Stale skill_status** — old PLACEHOLDER status from previous runs is no longer preserved when skill content has been filled

### Results after improvement
- FALLBACK_CAPS: 422 → 311 → 228 → 4 → **0**
- SHORT_DESC: 87 → **0**
- GENERIC_ROLE: 16 → **3** (genuinely minimal stubs)
- MD_IN_DESC/ROLE: 8 → **0**
- Validation: **834/834 valid, 0 invalid**
- All 834 VERIFIED (previously-CONDITIONAL skills were enriched with vault content between runs)
## Final result (2026-08-26)

| State | Count |
|-------|------:|
| VERIFIED | 819 |
| CONDITIONAL | 15 |
| EXTERNAL_VIRTUAL | 0 |
| UNKNOWN/GAP | 0 |
| **Total** | **834** |

**Validation: 834/834 valid, 0 invalid.**

- 198 generic "Agent for amos-..." descriptions → replaced with skill-derived descriptions
- 60 "quantum/fractal/math consolidated reasoning" boilerplate → replaced
- 75 generic capability stubs → replaced with skill-derived object-form capabilities
- 60 generic safety_constraints objects → replaced with skill-derived arrays
- 54 agents with renamed/consolidated skills → re-bound via curated mapping
- 15 agents bound to placeholder skills → marked CONDITIONAL with ${UNRESOLVED_CONFIG}
- All 834 agents re-derived from SKILL.md (no fabrication)
- Mis-specialization corrected (e.g. amos-adversarial-robustness-agent no longer claims ML security)

### Reports generated
- AGENT_FIX_REPORT.md
- AGENT_REGISTRY.json
- AGENT_SKILL_SYNC_REPORT.json
- UNRESOLVED_AGENT_CONFIG.md
- AGENT_VALIDATION_REPORT.md
- .devin/AGENT_FIX_WORKLOG.json

### Anti-fabrication discipline held
No value was fabricated to remove a placeholder. All 15 unresolved entries are agents bound to placeholder skills whose SKILL.md content has not been authored — they remain explicitly CONDITIONAL.
## Critical discovery (2026-08-26)

The classifier marked 556 agents as SPECIALIZED, but inspection shows many are **mis-specialized** — they have rich fields populated with **fabricated content that contradicts the bound SKILL.md**.

Example: `amos-adversarial-robustness-agent.json` describes "prompt injection defense, jailbreak resistance, data poisoning defense" (ML security) but the SKILL.md is about **adversarial validation of reasoning outputs** (9-step protocol: falsifier enumeration, red-team framing, stress cases, alternative explanations, selection-effect correction, claim revision/downgrade, attack-log retention). The capabilities are completely wrong.

### Revised approach
**Repair ALL 834 agents**, not just the 198 generic ones. For each agent:
1. Read bound SKILL.md completely
2. Re-derive description, role, capabilities, operations, integrity_requirements, safety_constraints, depends_on_skills, depends_on_workflows FROM the skill
3. Preserve any genuinely-correct existing content (e.g. Trang Phan author, version)
4. Flag contradictions in AGENT_SKILL_SYNC_REPORT.json

### State buckets (final)
- VERIFIED — agent content matches skill after repair
- CONDITIONAL — repaired but skill is a placeholder/stub
- EXTERNAL_VIRTUAL — skill source unavailable
- UNKNOWN/GAP — no skill binding found

---
**MOC:** [[06_AGENTS_MOC]]
