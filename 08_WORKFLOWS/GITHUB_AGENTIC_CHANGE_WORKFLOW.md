---
title: "AMOS GitHub Agentic Change Workflow"
type: workflow
origin_architect: Trang Phan
steward: Trang Phan
status: CANDIDATE_IMPLEMENTED_CONTRACT
epistemic_class: AMOS_MODEL
---

# AMOS GitHub Agentic Change Workflow

## 1. Objective

Provide one governed repository-change lifecycle for GitHub-native coding agents, AMOS Skills, external research sources, validators, CI, and human authority.

The workflow adopts useful graph/checkpoint/handoff patterns from current agent runtimes while preserving AMOS control-plane precedence.

## 2. State machine

```text
REQUESTED
  -> ORIENTED
  -> EVIDENCE_ACQUIRED
  -> CHANGE_PROPOSED
  -> BRANCH_STAGED
  -> LOCALLY_VALIDATED
  -> PR_OPEN
  -> CI_PENDING
  -> CI_VALIDATED
  -> REVIEW_PENDING
  -> APPROVED
  -> MERGE_ELIGIBLE
  -> MERGED
  -> POST_MERGE_OBSERVED
```

Exceptional states:

```text
BLOCKED_GAP
QUARANTINED_SOURCE
VALIDATION_FAILED
CI_FAILED
REVIEW_REJECTED
AUTHORITY_EXPIRED
CONFLICTED
ROLLBACK_REQUIRED
```

Transitions are explicit. A later state MUST NOT be inferred from prose claiming completion.

## 3. Role separation

### Planner / researcher

May:
- inspect repository state;
- search pinned external sources;
- identify gaps;
- construct a change plan;
- propose target files and tests.

May not:
- promote external source material to canon;
- claim execution that did not occur;
- authorize merge.

### Upgrader / implementer

May:
- create a branch;
- edit files inside task scope;
- add focused tests/validators;
- create a pull request.

May not:
- widen its own permissions;
- suppress failing evidence;
- merge its own PR solely because it authored it.

### Auditor / reviewer

May:
- inspect diff and provenance;
- run/review validators;
- challenge authority, scope, and regression assumptions;
- issue PASS / FAIL / GAP findings.

Should remain independent from implementation context where practical.

### Control plane / human authority

Owns:
- high-impact scope changes;
- policy exceptions;
- final merge authorization when required;
- credentials/secrets;
- production or external-effect release.

## 4. Task contract

Before mutation, freeze:

```yaml
task_contract:
  objective: string
  repository: owner/name
  base_ref: string
  allowed_paths: []
  prohibited_paths: []
  external_sources: []
  required_validators: []
  effect_ceiling: BRANCH_WRITE
  merge_authority: HUMAN_OR_CONTROL_PLANE
  stop_conditions: []
```

A GitHub agent may propose a broader task contract. It may not silently expand the active one.

## 5. Discovery and evidence stage

Use a progressive search order:

```text
current repository facts
-> existing AMOS capability/skill/workflow
-> pinned official external repositories
-> broader community sources only for unresolved gaps
```

For external GitHub sources capture:

```text
repository
commit SHA
date observed
license/scope
mechanism extracted
AMOS target
contradictions/gaps
```

Star count, forks, popularity, or marketplace presence are discovery signals only.

## 6. Implementation topology

### 6.1 Sequential path

Use for dependent edits:

```text
contract -> implementation -> validator -> PR
```

### 6.2 Fan-out / fan-in

Use when independent evidence classes can be acquired in parallel:

```text
                 -> skill-source analysis --\
REQUEST -> ROUTE -> runtime analysis -------+-> SYNTHESIZE -> CHANGE
                 -> security analysis ------/
```

Fan-in requires provenance-preserving synthesis. Independent branches do not become independent evidence if they share the same root source.

### 6.3 Handoff

Use when a specialist becomes the new task owner. Re-resolve capability/authority at handoff.

### 6.4 Agent-as-tool

Use for bounded specialist calls where the parent remains workflow owner.

## 7. Checkpoint and resume

Checkpoint after each material state transition:

```text
Checkpoint_i = hash(
  task_contract,
  base_commit,
  staged_diff,
  validation_results,
  source_pins,
  unresolved_gaps
)
```

The hash is an integrity identifier, not an authority token.

On resume:

1. compare current base/head identity;
2. detect changed task constraints;
3. re-check source pins if source-dependent logic changed;
4. re-run validators affected by the diff;
5. revalidate merge/effect authority.

## 8. Change gates

### Gate A — repository understanding

Required:
- target mechanism identified;
- ownership/path understood;
- current implementation inspected;
- duplication check completed.

### Gate B — source admission

Required for external patterns:
- immutable source pin;
- license classified;
- mechanism extracted rather than copied wholesale;
- source remains `REFERENCE_ONLY` unless independently promoted.

### Gate C — static validation

Required:
- syntax/parse checks;
- referenced local executables exist;
- agent/skill metadata structurally valid;
- registry schemas valid.

### Gate D — behavioral validation

When executable behavior changes:
- focused positive case;
- negative case;
- regression case;
- recovery/replay case where stateful.

### Gate E — PR boundary

PR description MUST state:
- objective;
- files changed;
- provenance/source pins;
- validation performed;
- unresolved gaps;
- effect/authority boundary.

### Gate F — CI

`CI_PENDING != PASS`.

Only an actual successful workflow run can support `CI_VALIDATED` for that exact head SHA.

### Gate G — review and merge

```text
Authoring capability
!=
Review independence
!=
Merge authority
```

An autonomous agent MUST NOT interpret its own successful implementation and tests as merge authority.

## 9. GitHub write effects

Classify repository effects:

```text
R0  READ              repository/search/read only
R1  BRANCH_WRITE      commits to non-protected working branch
R2  PR_WRITE          create/update PR, issue, review comment
R3  BASE_MUTATION     merge, force update, protected branch change
R4  RELEASE_EFFECT    release, deployment, secret/environment mutation
```

Default autonomous ceiling for an AMOS repository upgrader:

```text
R2 PR_WRITE
```

R3/R4 require separately resolved authority.

## 10. Failure and recovery

### Validation failure

Return to `CHANGE_PROPOSED`, repair only dependent changes, then re-run affected gates.

### Base drift

Rebase/merge only after checking semantic conflicts. Passing tests on the old base do not survive automatically.

### Source drift

Keep the pinned source for reproducibility. Open a separate update proposal rather than silently switching to latest.

### CI infrastructure failure

Classify as `UNKNOWN/GAP` or infrastructure failure, not code PASS/FAIL, until discriminated.

### Ambiguous external side effect

Do not blind retry. Reconcile observable GitHub state first.

## 11. Pull-request output contract

A completed pre-merge workflow returns:

```yaml
change_result:
  branch: string
  head_sha: string
  pull_request: string
  validation:
    local: PASS | FAIL | GAP
    ci: PASS | FAIL | PENDING | GAP
  sources: []
  unresolved_gaps: []
  merge_eligible: boolean
  merge_authority_observed: false
```

`merge_eligible: true` is a technical/governance readiness signal, not permission to merge.

## 12. Repository-native projections

Compatible GitHub clients may use:

- `.github/agents/amos-repo-upgrader.agent.md`
- `.github/agents/amos-repo-auditor.agent.md`
- `.github/copilot-instructions.md`
- `.github/workflows/skill-audit.yml`

These files implement or project this workflow for GitHub-native agents. AMOS canon/control-plane rules remain authoritative.
