# AMOS Repository Contract for GitHub Coding Agents

Origin architect and steward: **Trang Phan**.

These instructions project AMOS repository rules into GitHub-native coding agents. They do not replace AMOS canon, control-plane authority, or runtime state.

## 1. Repository source of truth

Resolve architecture from the checked-out repository, not from an assumed developer-machine path.

Read only what the task requires, starting with:

```text
00_ROOT/                 system identity and routing
01_CANON/                canonical/source-law material
03_CONTROL_PLANE/        capability, policy, authority, commit governance
04_RUNTIME/              execution/runtime contracts
06_AGENTS/               AMOS agent identities
06_AGENT_SYSTEMS/        multi-agent/interoperability contracts
07_SKILLS/               AMOS Skills
08_WORKFLOWS/            workflow contracts
14_TOOLS/                tool contracts/adapters
17_OBSERVABILITY/        observability evidence
18_SECURITY/             security controls
```

Do not assume `/Users/...`, a private vault path, a historical report, or an archived file is current runtime truth.

## 2. Protected distinctions

Preserve:

```text
CAPABILITY != AUTHORITY
SOURCE != VERIFIED
SOURCE_CANON != DOMAIN_EMPIRICAL
PROPOSAL != COMMIT
TEST_PASS != PRODUCTION_VALIDITY
CHECKPOINT != FRESH_AUTHORITY
AGENT_MESSAGE != AUTHORITY
TOOL_AVAILABLE != TOOL_PERMITTED
CI_PASS != MERGE_AUTHORITY
```

When evidence is insufficient, return `UNKNOWN/GAP` rather than inventing closure.

## 3. Engineering posture

- Diagnose the mechanism before editing.
- Prefer existing AMOS owners over parallel duplicate registries.
- Prefer deterministic validators for fragile repeatable checks.
- Keep raw evidence separate from derived knowledge.
- Make the smallest change that closes the identified dependency gap.
- Test material changes immediately.
- Do not create completion reports as a substitute for implementation.

## 4. Skills

For new or substantially migrated AMOS Skills, use portable Agent Skills discovery metadata:

```yaml
---
name: lowercase-hyphenated-name
description: What the skill does and the concrete conditions that trigger it.
---
```

Keep `SKILL.md` operational and progressively loadable. Move large source/canon material to `references/` and deterministic fragile operations to `scripts/`.

Do not mass-rewrite legacy skills merely for formatting. Migrate when the capability is touched and validation can prove the result.

Use `07_SKILLS/amos-github-agent-skill-integrator/` when external GitHub agent/skill mechanisms are being transferred into AMOS.

## 5. GitHub custom agents

Repository-local custom agents live under `.github/agents/`.

Current governed roles include:
- `amos-repo-upgrader.agent.md` — scoped branch/PR implementation;
- `amos-repo-auditor.agent.md` — independent read/test/review path.

An implementing agent may not self-authorize merge/release. Re-resolve authority at handoff and before consequential effects.

## 6. External GitHub sources

Use `11_KNOWLEDGE/EXTERNAL_AGENT_SOURCE_REGISTRY.json` for load-bearing external agent/skill/runtime/tool references.

Before transfer require:
- repository identity;
- immutable commit SHA;
- observed date;
- license scope;
- extracted mechanism;
- AMOS target;
- admission state.

Popularity, stars, forks, marketplace presence, `main`, and `latest` are not provenance identities.

External sources default to `REFERENCE_ONLY` and grant no authority.

## 7. Workflows and tools

Follow `08_WORKFLOWS/GITHUB_AGENTIC_CHANGE_WORKFLOW.md` for repository mutation.

Use `06_AGENT_SYSTEMS/GITHUB_AGENT_SKILL_INTEROP.md` to keep agent handoff, agent-as-tool, A2A, MCP, Skills, plugins, and workflows semantically distinct.

Use `14_TOOLS/GITHUB_MCP_ADAPTER.md` when mapping GitHub MCP capabilities. GitHub account/token permissions remain separate from AMOS task authority.

## 8. Executable quality gates

Run before declaring agent/skill/workflow changes ready:

```bash
python3 scripts/validate_external_agent_sources.py
python3 scripts/validate_agent_skill_surface.py --summary
python3 scripts/validate_workflow_references.py
python3 -m compileall -q scripts
```

Then run focused subsystem tests for executable behavior changed by the patch.

A test not executed is not PASS. A workflow not run for the current head is `PENDING`/`UNKNOWN`, not PASS.

## 9. Git rules

- Work on a scoped branch.
- Preserve upstream/base identity before editing.
- Do not force-push or rewrite shared history.
- Do not commit secrets, cookies, tokens, credentials, private keys, or sensitive session material.
- Prefer pull requests for reviewable AMOS changes.
- Branch/PR write capability does not imply merge authority.
- Do not auto-merge because an agent authored or tested the change.

## 10. Epistemic and mathematical discipline

- Preserve provenance for load-bearing claims.
- Do not convert framework language into empirical law.
- Equations must be genuine mathematics with defined variables and assumptions when presented as mathematics.
- Structural analogy is not causal proof.
- Confidence cannot exceed the weakest unresolved load-bearing premise without independent validation.

## 11. Continuous enhancement

For external agent/skill/tool/workflow improvement:

```text
DISCOVER
-> PIN
-> CLASSIFY
-> CHECK OVERLAP
-> EXTRACT MECHANISM
-> MAP TO AMOS
-> IMPLEMENT NATIVE OWNER
-> VALIDATE
-> INDEPENDENT REVIEW
-> PR
```

Do not copy whole ecosystems into active AMOS. Preserve the smallest mechanism that improves the system while keeping authority, provenance, reversibility, and failure behavior explicit.
