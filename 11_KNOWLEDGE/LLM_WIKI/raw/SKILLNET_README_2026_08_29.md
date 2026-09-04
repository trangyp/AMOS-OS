---
canon-group: meta
canon-type: framework
rscf-state: source-claim
rscf-claim: verified
rscf-provenance: AMOS_corpus
conclusion_class: AMOS_MODEL
epistemic_class: SOURCE_CLAIM
topic: Skillnet Readme 2026 08 29
tags:
  - canon-group/tech-ai
  - rscf/claim
  - rscf/provenance
  - rscf/state/source-claim
  - misc
created: 2026-08-22
---
---
---

# SkillNet README — Raw Capture

Source: `https://github.com/zjunlp/SkillNet`

## Elevator pitch

SkillNet is an open infrastructure for discovering, evaluating, composing, and orchestrating reusable AI agent skills. It treats agent skills as software assets: searchable, installable, inspectable, evaluable, and composable.

## Capabilities

- **Discovery:** search a public skill library by keyword or semantic intent.
- **Installation:** download skill folders from GitHub into local agent workspaces.
- **Creation:** generate structured skills from repositories, documents, prompts, or execution traces.
- **Evaluation:** score skills for safety, completeness, executability, maintainability, and cost awareness.
- **Composition:** infer relationships and scenario handoffs between local skills.
- **Orchestration:** select scene-specific skills and generate a prompt for a downstream execution agent.

## News and scale

- 2026-08-20: SkillNet-Gym executable benchmarks + SkillNet-Fabric task-routing.
- 2026-07-11: 500K+ GitHub skills indexed, scientific-research and data-analysis skill coverage expanded.
- 2026-03-26: JiuwenClaw integration (built-in skill marketplace).
- 2026-03-12: MCP server released (maintained by CycleChain).
- 2026-02-23: OpenClaw integration released.

## Quick start

```bash
pip install skillnet-ai
```

```python
from skillnet_ai import SkillNetClient
client = SkillNetClient()
results = client.search("pdf understanding", limit=5)
client.download(results[0].skill_url, target_dir="./my_skills")
```

CLI:

```bash
skillnet search "pdf understanding" --limit 5
skillnet download <skill_url> -d ./my_skills
```

## What you can build

| Layer           | Capability                              | Enables                                     |
| --------------- | --------------------------------------- | ------------------------------------------- |
| Skill library   | Search and download                     | Reuse existing skills                       |
| Skill authoring | Create                                  | Turn traces/prompts/repos into packages     |
| Skill quality   | Evaluate                                | Compare skill readiness                     |
| Skill graph     | Analyze                                 | Discover `compose_with`, `depend_on`        |
| Orchestration   | Orchestrate                             | Pick skills for a scene and return a prompt |
| Integrations    | Agent skills, MCP, OpenClaw, JiuwenClaw | Use inside existing runtimes                |

## Configuration and credentials

- Public search and GitHub downloads require no API key.
- `create`, `evaluate`, `analyze`, and `orchestrate` require `API_KEY`, `BASE_URL`, `SKILLNET_MODEL`.
- Optional `GITHUB_TOKEN` for private repos or higher rate limits.
- Optional extras: `skillnet-ai[graph]` for scenario graphs, `skillnet-ai[orchestrate]` for scene orchestration.

## AMOS relevance (unverified)

- Provides the largest public skill search index (500K+) — ideal for gap-filling AMOS `.devin/skills`.
- Evaluation dimensions (safety, completeness, executability, maintainability, cost) mirror AMOS `skill-check` and guardrail concerns.
- MCP server lets AMOS agents query SkillNet directly.
- `create` and `analyze` could feed into `amos-skill-builder` and `amos-routing-audit`.

## Confidence ceiling

README claims only. Empirical benchmarks (SkillNet-Gym) mentioned but not reproduced.
