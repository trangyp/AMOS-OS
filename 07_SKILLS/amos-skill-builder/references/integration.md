---
title: "integration — References — Amos Skill Builder"
type: reference
source: 07_SKILLS/amos-skill-builder/references
tags:
- reference
- amos-skill-builder
- canon/skill
rscf:
  state: SOURCE_CLAIM
  claim_class: SOURCE_CLAIM
  provenance: AMOS_corpus
  scope: skill_reference
---


# Skill Builder — Integration Reference

## AMOS Routing Architecture

### 1:1:1 Binding Rule
Every AMOS skill MUST bind to exactly one agent and one workflow:
- **Skill** (`.devin/skills/<name>/SKILL.md`) — the knowledge content
- **Agent** (`.devin/agents/<name>-agent.json`) — the executable wrapper
- **Workflow** (`.devin/workflows/<name>-workflow.md`) — the operational sequence

### Parent/Child Skill Structure
- **Parent skills** (27 domain masters) contain rich, vault-sourced content
- **Child skills** redirect to their parent via `redirect_target` in frontmatter
- Each child retains its own `name` and `description` for routing
- The parent skill's content is the authoritative source

### RSCF Format
RSCF (Root → Stem → Crown → Fruit) is the AMOS knowledge structure:
- **Root**: foundational laws and axioms
- **Stem**: frameworks and methodologies
- **Crown**: capabilities and applications
- **Fruit**: outputs, evidence, and validation

### H/M/L Integrity Levels
- **H (High)**: vault-canonical, peer-reviewed content — claim ceiling 0.95
- **M (Medium)**: derived from vault sources — claim ceiling 0.85
- **L (Low)**: model-generated, unverified — claim ceiling 0.70

### Provenance Contracts
Every derived claim MUST record:
- Source file path (vault or repo)
- Epistemic class (SOURCE / DERIVED / AMOS_MODEL / EMPIRICAL)
- Confidence ceiling
- Date of derivation

### Domain Engine Mapping (C01–C12)
- C01: Meta Logic
- C02: Physics
- C03: Biology
- C04: Chemistry
- C05: Mind & Behavior
- C06: Society
- C07: Economy
- C08: Technology
- C09: Mathematics
- C10: Information
- C11: Governance
- C12: Evolution

### Agent Capability Naming Convention
- Format: `<domain>.<verb>` (e.g., `skill.design`, `workflow.validate`)
- No hyphens in capability names — use underscores
- No `run_` prefix — use `design_` or domain-specific verbs
- Each agent has 4–12 meaningful capabilities

### Content Hash
- Agent JSON includes a `content_hash` field (SHA-256, first 16 hex chars)
- Computed over all fields except `content_hash` itself
- Must match when validated — ensures integrity of agent definition

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
node_id: amos-skill-builder-integration
node_type: reference
path: 07_SKILLS/amos-skill-builder/references/integration.md
RSCF-RELATIONS:
- INDEXED_BY: [[00_HOME]]
- INDEXED_BY: [[AMOS_RSCF_NODES]]
- CHILD_OF: [[references_MOC]]
