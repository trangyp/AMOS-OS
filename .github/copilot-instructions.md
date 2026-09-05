---
title: copilot-instructions
type: note
source: .github
tags:
  - vault
  - .github
rscf:
  state: DERIVED
  claim_class: DERIVED
  provenance: AMOS_corpus
  scope: AMOS_general

---

# AMOS Global Contract for AI Coding Agents

## 1. Brain source of truth

Use the Obsidian vault (`/Users/mac/Documents/AMOS_OS/`) as the reasoning brain.
Primary canon: `cosmo-brain/AMOS_UNIFIED_BRAIN_COGNITION_ARCHITECTURE_ROUTING_v1.md`.
Read UBCAR before making architectural or naming decisions.

## 2. Engineering posture

- Think like a software engineer: prefer scripts, guardrails, and repeatable pipelines over one-off edits.
- Use the vault to decide, then commit back to the vault.
- For skills: ensure `SKILL.md` has `## Identity`, `## Capabilities`, `## Operations`, `## When to Use`, and `## Detailed Reference`.
- For agents: ensure JSON has real capabilities, no broken dependencies, and `amos-{name}-agent.json` naming.
- For workflows: ensure markdown and JSON are bound to a skill and an agent.

## 3. Epistemic discipline (RSCF)

Every claim-bearing artifact must carry:

```yaml
rscf:
  state: <SOURCE_CLAIM | DERIVED | AMOS_MODEL | CONDITIONAL | COMPETING | UNKNOWN/GAP>
  claim_class: <same as state>
  provenance: <AMOS_corpus | arxiv | web | AMOS_CANON>
  scope: <AMOS_general | canon | arxiv | ...>
```

## 4. Quality gates

Run before committing:

- `python3 scripts/skill_guardrail_checker.py --skills-dir .devin/skills --summary`
- `python3 scripts/skill_binding_checker.py`
- `python3 scripts/skill_operations_enhancer.py --dry-run 07_SKILLS` (when needed)

## 5. Git rules

- Use `.devin/` for new configuration; use `~/.config/devin/` for global config only.
- Do not write to `.claude/`, `.cursor/`, or other tool-specific directories.
- Commit messages use the multi-line `$(cat <<'EOF'...EOF)` pattern with a Devin co-authored footer.
- Do not force-push, rewrite history, or commit secrets.

## 6. Anti-overclaim

- UBCAR is a composition model, not a new architecture.
- Quantum, fractal, and math terms are reasoning analogies unless explicitly grounded.
- No claim without proof capsule or `rscf` provenance.

## 7. Continuous enhancement

- Keep searching public repositories for best skill / agent / workflow patterns.
- Ingest findings into `11_KNOWLEDGE/LLM_WIKI/` as `raw/` captures and `wiki/` synthesis.
- Run end-to-end ingestion trials (guardrail + RSCF canonicalizer) before promoting an external skill.

______________________________________________________________________

**MOC:** [[00_ROOT/00_COSMO_BRAIN_MOC|00_COSMO_BRAIN_MOC]]
