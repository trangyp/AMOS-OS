---
title: AMOS SKILL CREATION WORKFLOW
tags: [canon-group/tech-ai, canon/framework, rscf/claim, rscf/provenance, rscf/state/source-claim, topic/amos-skill-creation-workflow, amos-general]
type: document
source: 11_KNOWLEDGE/amos-general
---



# AMOS Skill Creation Workflow

Use this workflow to create new AMOS skills that extend the brain's capabilities. Follow the brain's kernel registry and routing rules to ensure new skills integrate properly.

## When to Use
- When a new capability is needed that doesn't exist in the current skill set
- When a brain engine/spec needs a corresponding operational skill
- When the agent registry needs a new agent-focused skill

## Step 1: Identify the Capability Gap

1. Check existing skills in these categories:
   - `reasoning/` — amos-reasoning-loop, amos-law-stack, amos-cognition-modes, amos-expression-overlay
   - `tech/` — amos-tech-kernel-catalog
   - `docs/` — amos-docs-bridge
   - `communication/` — amos-expression-overlay

2. Check the brain's kernel registry (md/Core/AMOS_Kernel_Routing_Workflow.md):
   - K_META_LOGIC — logic, law_of_law, reasoning
   - K_MATH_COMPUTE — math, compute, optimization
   - K_BIO_NEURO — ubi, biology, nervous_system
   - K_MIND_BEHAVIOR — psychology, emotion, behaviour
   - K_TECH_ENGINE — software, ai, cloud, infra
   - K_EV_INFRA — ev, charging, logistics, fleet
   - K_UNIPOWER_OPS — unipower, vn, ops, drivers, stations
   - K_UNIPOWER_TECH — unipower, tech, ai, design

3. Check the brain's routing rules for task type matching:
   - ROUTE_EV: ev, charging, station, driver, fleet
   - ROUTE_TECH: software, ai, architecture, system_design
   - ROUTE_PSYCH: emotion, behaviour, psychology, ubi
   - ROUTE_DEFAULT: * (fallback)

## Step 2: Name and Categorize

1. **Name:** lowercase, hyphens, descriptive of capability (e.g., `amos-something-descriptive`)
2. **Category:** one of `reasoning`, `tech`, `docs`, `communication`, or a new category if justified
3. **Related skills:** list skills this new skill depends on or complements

## Step 3: Define the Skill Content

Every AMOS skill must include:

### Frontmatter (YAML)
```yaml
---
name: amos-something-descriptive
description: One-line trigger condition — when to use this skill.
version: 1.0.0
author: AMOS Brain (Trang Phan)
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [tag1, tag2]
    related_skills: [skill1, skill2]
---
```

### When to Use
Clear trigger condition. What task tags match? Which routing rule applies?

### What It Does
High-level capability description. Which kernels does it activate?

### How to Use
Step-by-step or bullet instructions. Reference brain files where relevant.

### Examples (optional)
Concrete task → skill → outcome examples.

### References
Brain files, engine IDs, or other skills this skill builds on.

## Step 4: Check Integration

1. **Kernel routing:** Does this skill activate the right kernels per the routing rules?
2. **Law compliance:** Does the skill obey Law of Law, Rule of 2, Rule of 4, Absolute Structural Integrity, Post-Theory Communication, UBI Alignment?
3. **IP protection:** Does the skill avoid exposing internal paths/filenames, raw schema dumping, and exact internal kernel generation?
4. **Expression translation:** Does the skill translate AMOS internal structures to high-level descriptions?

## Step 5: Create the Skill File

1. Create skill directory: `~/.hermes/skills/<category>/amos-<name>/`
2. Create `SKILL.md` with the content from Step 3
3. Verify with `skill_view(name='amos-<name>')`

## Step 6: Document in Brain

If the skill represents a significant capability, document it in the brain vault:
- File: `md/Core/AMOS_<Capability>_Skill.md` or appropriate subdirectory
- Include: what it does, when to use, how it integrates with kernels, limitations

## Examples

### Example 1: New reasoning skill for multi-perspective analysis
- **Name:** `amos-multi-perspective`
- **Category:** `reasoning`
- **When to use:** Task tags include `multi_perspective`, `bias_detection`, `viewpoint_comparison`
- **Kernels:** K_META_LOGIC (primary), K_MIND_BEHAVIOR (secondary)
- **Routing:** Complements ROUTE_PSYCH and ROUTE_DEFAULT
- **References:** AMOS_Multi_Perspective_Reasoning_Kernel_v0 (brain spec)

### Example 2: New tech skill for system architecture design
- **Name:** `amos-architecture-design`
- **Category:** `tech`
- **When to use:** Task tags include `architecture`, `system_design`, `software_architecture`
- **Kernels:** K_TECH_ENGINE (primary), K_META_LOGIC (secondary), K_UNIPOWER_TECH (if unipower context)
- **Routing:** ROUTE_TECH
- **References:** AMOS_Tech_Architecture_Kernel_v0 (brain spec)

## Memory: Skill Creation Workflow

AMOS skills live in `~/.hermes/skills/<category>/amos-<name>/SKILL.md`. Categories: reasoning, tech, docs, communication. Skill creation workflow: identify gap → name+categorize → define content (frontmatter, when to use, what it does, how to use, examples, references) → check integration (kernel routing, law compliance, IP protection, expression translation) → create file → document in brain vault. Existing skills: amos-reasoning-loop (reasoning), amos-law-stack (reasoning), amos-cognition-modes (reasoning), amos-expression-overlay (communication), amos-tech-kernel-catalog (tech), amos-docs-bridge (docs).

---
**Related:** [[00_HOME]] · [[KNOWLEDGE_MOC]] · [[AMOS_SIMULATION_KERNEL_V0_MATH_FOUNDATIONS]] · [[SYSTEM_SCAN_AGENT]] · [[AUTOMATION_PROFILES]]

---
**MOC:** [[AMOS-GENERAL_MOC]]
