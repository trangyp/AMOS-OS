# Upstream mechanisms

All external mechanisms remain `SOURCE_CLAIM` until independently executed in AMOS.

- Agent Skills: portable `SKILL.md` bundle plus optional scripts/references/assets; progressive loading defines package boundary, not permission safety.
- Cisco AI Defense skill-scanner `431cb58a5ac333bc0bb9aaa23f7c30ac628f59f8`: AST-backed static findings, execution/file markers, severity taxonomy, deterministic no-network scan path.
- NVIDIA SkillSpector `1c0eb569a2550172415aaebd83a62ea163cb3c06`: AST rules for eval/import/subprocess plus reviewable security baselines.
- Snyk agent-scan `73ceb7119825edf06e6800f0acfe284a4cc9c842`: risk-to-affected-tool mapping and permission-risk framing.

AMOS adapts these mechanisms into explicit effect containment. It does not inherit upstream trust or authority.
