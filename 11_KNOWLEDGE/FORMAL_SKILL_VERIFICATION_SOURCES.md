# Formal Skill Verification Source Registry

Epistemic class: `SOURCE_CLAIM` for upstream mechanisms; `AMOS_MODEL` for the local containment abstraction.

Pinned sources:
- `agentskills/agentskills` — portable Skill bundle/progressive-disclosure boundary; repository README observed 2026-09-14.
- `cisco-ai-defense/skill-scanner@431cb58a5ac333bc0bb9aaa23f7c30ac628f59f8` — AST-backed static findings, command/file markers, deterministic scan separation.
- `NVIDIA/SkillSpector@1c0eb569a2550172415aaebd83a62ea163cb3c06` — AST rules and reviewable baseline mechanism.
- `snyk/agent-scan@73ceb7119825edf06e6800f0acfe284a4cc9c842` — risk-to-affected-tool and permission-risk representation.

AMOS adaptation:
`observed AST effect set O` is compared with `declared allowed set A` using `O subseteq A`.

This does not prove analyzer completeness, semantic safety, exploitability absence, runtime authorization, or deployment validity.
