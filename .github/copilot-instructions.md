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

## 1. Repository source of truth

Operate from the checked-out repository, not a hard-coded local filesystem path.

Resolve architecture in this order:
1. `AGENTS.md`
2. `00_ROOT/`
3. `01_CANON/` when canonical AMOS semantics are involved
4. `02_KERNEL/`, `03_CONTROL_PLANE/`, `04_RUNTIME/` for executable/runtime ownership
5. the directly affected plane, schemas, tests, and provenance records

`LATEST != AUTHORITATIVE`. Search supersession/version lineage instead of assuming newest filename wins.

## 2. Engineering posture

- Prefer deterministic scripts, typed contracts, tests, and repeatable pipelines over one-off prose edits.
- Search before creating a new owner, registry, schema, agent, skill, workflow, or tool.
- Use feature branches for material changes.
- Prefer adapters around third-party systems rather than vendoring entire external repositories.
- Keep external source identity and immutable commit/ref in provenance when a mechanism is adopted.

## 3. GitHub-native specialization

Use the repository agents under `.github/agents/` when their role matches:
- `AMOS Architect` for architecture and ownership decisions;
- `AMOS Skill Security Auditor` for external skill/agent/tool admission and security review;
- `AMOS Integration Engineer` for approved implementation work.

File-pattern rules under `.github/instructions/` provide additional contracts for skills, workflows, and tools.

## 4. Epistemic discipline

Preserve:
- SOURCE_CANON / SOURCE_CLAIM / OBSERVATION / DERIVED / AMOS_MODEL / PREDICTION / DECISION / UNKNOWN/GAP;
- capability / authority / permission;
- declared / implemented / available / validated / approved;
- proposal / staged effect / committed effect.

Do not promote external README claims, benchmarks, star counts, or security claims into AMOS truth without independent evidence.

## 5. Skill discipline

Use the portable Agent Skills baseline: `name` + `description` frontmatter, compact `SKILL.md`, and progressive loading through `scripts/`, `references/`, and `assets/` when needed.

AMOS metadata may extend this format but must not break portability unnecessarily.

External skills are quarantined candidates until structural, security, dependency, license, test, and governance gates pass.

## 6. Quality gates

Use the repository-native validators applicable to the change. Typical skill gates include:

- `python3 scripts/validate.py`
- `python3 scripts/skill_binding_checker.py`
- `python3 scripts/skill_dependency_graph.py`
- `python3 scripts/skill_guardrail_checker.py --skip-references`
- `python3 scripts/skill_regression_harness.py`
- `python3 scripts/skill_quality_scorer.py --min-score 80`

Do not convert a failed gate into a warning merely to obtain a green build.

## 7. Git and security rules

- Do not force-push or rewrite history.
- Do not commit secrets, cookies, tokens, credentials, local absolute paths, generated caches, or personal authentication state.
- Do not execute arbitrary install/bootstrap commands copied from newly discovered repositories before inspection.
- Pin third-party CI/workflow dependencies to immutable commits when security or reproducibility matters.
- Tool availability is not tool authority.

## 8. Continuous enhancement

When scanning public repositories for improvements:
1. identify the AMOS gap first;
2. inspect primary source code/docs at a specific commit;
3. extract the mechanism, assumptions, limits, and failure modes;
4. compare against existing AMOS capability before adding anything;
5. integrate the smallest non-duplicative mechanism;
6. preserve provenance and test the result.

Do not accumulate GitHub patterns merely because they are popular.
