# GitHub Actions Supply-Chain Auditor

## Purpose

Validate that AMOS GitHub Actions workflows bind external actions to immutable commit identities rather than movable tags or branches.

Executable:

`python scripts/validate_workflow_supply_chain.py --repo .`

## Capability boundary

```text
TOOL_CAPABILITY = FS_READ_WORKFLOWS | ACTION_REF_VALIDATE
TOOL_AUTHORITY = NONE
```

This tool is read-only. It does not update dependencies, approve releases, merge pull requests, or grant workflow execution authority.

## Admission rule

External `uses:` references must use:

`owner/repository/path@<40-character Git commit SHA>`

Repository-local actions beginning with `./` are allowed without an external SHA.

The following are rejected:

- floating major tags such as `@v4`;
- release tags such as `@v7.0.1`;
- branches such as `@main`;
- missing refs.

## Invariants

- `TAG != IMMUTABLE_DEPENDENCY_IDENTITY`
- `POPULAR_ACTION != TRUSTED_ACTION`
- `PINNED_SHA != SAFE_ACTION`
- `DEPENDENCY_IDENTITY != DEPENDENCY_BEHAVIOR_VALIDATION`
- `CI_PASS != SUPPLY_CHAIN_PROOF`

A SHA pin prevents silent ref movement; it does not prove the referenced action is benign or correct.

## Evidence scope

The validator statically audits workflow action references. Reusable workflow security, action source review, provenance/signing, transitive dependencies, runner compromise, token permissions, and artifact integrity require separate controls.
