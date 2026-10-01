---
title: "AMOS GitHub MCP Adapter"
type: tool-adapter
origin_architect: Trang Phan
steward: Trang Phan
status: CANDIDATE
execution_tier: T3_EXTERNAL_NETWORK
source: github/github-mcp-server@7d13a7ad6f2a17f351a6d77ce280c85ae1821f4d
epistemic_class: AMOS_MODEL
---

# AMOS GitHub MCP Adapter

## 1. Purpose

Map GitHub's MCP tool surface into AMOS OS without equating protocol discovery, authenticated GitHub access, or host configuration with AMOS authorization.

```text
MCP CONNECTED != AMOS AUTHORIZED
GITHUB PERMISSION != AMOS TASK AUTHORITY
TOOL DISCOVERED != TOOL SELECTED
TOOL SELECTED != EFFECT COMMITTED
```

## 2. Source boundary

Observed upstream source:

```text
repository: github/github-mcp-server
commit: 7d13a7ad6f2a17f351a6d77ce280c85ae1821f4d
license: MIT
verified: 2026-09-14
```

Upstream provides repository/code access, issue/PR operations, workflow intelligence, security surfaces, and multiple GitHub authentication modes. AMOS treats those as external capabilities subject to independent AMOS policy.

## 3. Capability partition

Do not expose one undifferentiated `github` capability.

```yaml
github_capability_classes:
  read_repository:
    effect: READ_ONLY
    examples: [repository_metadata, file_read, code_search, commit_read]

  read_collaboration:
    effect: READ_ONLY
    examples: [issue_read, pull_request_read, review_read, discussion_read]

  read_ci_security:
    effect: READ_ONLY_SENSITIVE
    examples: [workflow_status, workflow_logs, security_findings]

  write_collaboration:
    effect: EXTERNAL_MUTATION_REVERSIBLE
    examples: [issue_create, issue_update, pr_create, review_comment]

  write_repository:
    effect: DURABLE_REPOSITORY_MUTATION
    examples: [branch_create, file_create, file_update]

  merge_release:
    effect: HIGH_CONSEQUENCE
    examples: [merge_pr, release_create, protected_branch_change]
```

Each class is separately resolvable and authorizable.

## 4. Authentication modes

Supported upstream authentication mechanisms may include:

```text
OAuth
GitHub App installation token
fine-grained PAT
classic PAT (legacy/broader-risk)
```

AMOS preference order for automation:

```text
GitHub App installation identity
> OAuth user delegation where appropriate
> fine-grained PAT
> classic PAT only when no narrower supported mechanism exists
```

This is a governance preference, not a claim that every host supports every mode.

## 5. Principal binding

For every invocation preserve:

```text
GitHubPrincipal = (
  authentication_mode,
  account_or_app_identity,
  repository_scope,
  github_permission_scope,
  token_or_session_expiry,
  organization_policy_context
)
```

Then bind separately:

```text
AMOSAuthority = (
  task,
  operation,
  repository,
  path_or_object_scope,
  effect_class,
  expiry,
  policy_epoch
)
```

Invocation requires both. A broad GitHub token never expands AMOS authority.

## 6. Read/write firewall

Default GitHub MCP posture for research agents is read-only.

Write capability is enabled only for an explicit workflow state requiring it.

```text
READ_AGENT
  -> no issue/PR/repository mutation

UPGRADER_AGENT
  -> branch and PR writes only within task contract

AUDITOR_AGENT
  -> read + review finding output; no code mutation by default

MERGE/RELEASE
  -> separate authority; never inherited from updater role
```

## 7. Tool descriptor mapping

A discovered MCP tool is normalized before routing:

```yaml
amos_tool_descriptor:
  provider: github-mcp
  upstream_name: string
  capability_class: string
  input_schema_hash: string
  effect_class: string
  repository_scope: string
  credential_principal: string
  provenance_required: true
  authority_required: true
```

If effect class cannot be determined, classify conservatively and fail closed before mutation.

## 8. Invocation sequence

```text
MCP DISCOVERY
-> NORMALIZE TOOL DESCRIPTOR
-> RESOLVE AMOS CAPABILITY
-> CHECK TASK CONTRACT
-> CHECK GITHUB PRINCIPAL SCOPE
-> CHECK AMOS AUTHORITY
-> VALIDATE INPUT PROVENANCE
-> INVOKE
-> CLASSIFY RESPONSE
-> RECORD OBSERVATION/EFFECT
-> RECONCILE RECEIPT FOR MUTATION
```

## 9. Repository mutations

Branch/file/PR operations MUST bind:

```text
repository
base SHA
working branch
path/object target
expected prior state when available
new content/effect digest
invoking task
```

This supports compare-and-swap style reasoning and prevents a stale agent from treating a path as unchanged.

## 10. CI/workflow intelligence

Workflow status is `OBSERVATION`.

```text
workflow exists != workflow ran
run exists != run belongs to current head
job success != all required gates passed
CI success != merge authority
```

When using CI as validation evidence, bind the exact:

```text
repository + workflow + run_id + head_sha + conclusion
```

## 11. Security and privacy

- never commit PATs, OAuth tokens, GitHub App private keys, or session secrets;
- prefer least-privilege repository-specific grants;
- do not place secrets in prompts, logs, issue bodies, PR bodies, or trace payloads;
- security findings may require a narrower disclosure scope than normal repository content;
- external MCP hosts remain separate trust domains and must not receive data merely because they are reachable.

## 12. Observability gap

GitHub audit/API logs and MCP host telemetry may provide useful evidence, but AMOS MUST NOT assume tool-level MCP audit completeness unless the deployed environment demonstrates it.

Missing granular telemetry is represented as an observability gap, not silently treated as full coverage.

## 13. Admission state

This adapter is `CANDIDATE` until the deployed AMOS host demonstrates:

- exact GitHub MCP transport configuration;
- principal/authentication binding;
- read/write tool partition;
- AMOS authority mediation;
- mutation reconciliation;
- secret handling;
- executed positive and negative tests.

No upstream installation is performed by this document.
