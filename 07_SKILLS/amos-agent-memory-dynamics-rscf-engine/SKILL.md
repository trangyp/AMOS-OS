---
name: amos-agent-memory-dynamics-rscf-engine
description: Govern and execute AMOS agent-memory lifecycle operations including provenance-bound admission, retrieval, revision, temporal validity, expiry, quarantine, tombstones, contradiction isolation, context assembly, snapshot replay, stale-write protection, and integrity auditing. Use when agent memory or context must persist across turns or sessions, when retrieved memory may be stale or conflicting, or when memory writes must remain separate from knowledge promotion and external authority.
---

# AMOS Agent Memory Dynamics RSCF Engine

Preserve these boundaries:

```text
MEMORY != KNOWLEDGE
RETRIEVAL != VERIFICATION
RELEVANCE != TRUTH
REMEMBERED != AUTHORIZED
REVISION != OVERWRITE
TOMBSTONE != PHYSICAL_DELETE
CONFLICT != WINNER
CONTEXT_SNAPSHOT != CURRENT_STATE
CAPABILITY != AUTHORITY
```

## Execution

Use `scripts/memory_lifecycle.py` for deterministic local lifecycle operations and integrity checks.

Run:

```bash
python scripts/memory_lifecycle.py --self-test
python scripts/memory_lifecycle.py --check-db <sqlite-db>
```

Treat the executable as a local SQLite reference only. It does not establish production durability, distributed consistency, privacy compliance, semantic truth, or deployment authority.

## Memory object contract

Require every admitted memory to have:

- stable `memory_id`;
- namespace;
- immutable provenance identifier;
- explicit access scope;
- content hash;
- source epistemic class;
- temporal validity;
- monotonic revision number.

All reads return `epistemic_class = OBSERVATION` even when the source was a `SOURCE_CLAIM`, `DERIVED`, `MODEL`, or `DECISION` object.

## Write path

For admission or mutation:

1. Revalidate write authority outside this Skill at the AMOS control plane.
2. Bind stable object identity and provenance.
3. Require `expected_revision` for revision or status transitions.
4. Reject stale writes rather than merging silently.
5. Append a hash-chained lifecycle event.
6. Preserve prior revisions; never overwrite history in place.
7. Run integrity verification before consequential promotion or reuse.

Do not infer write authority from successful retrieval or from this Skill being invoked.

## Conflict path

When two memory objects are incompatible and discriminating evidence is absent:

1. Record the conflict.
2. Quarantine both objects.
3. Preserve both provenance chains.
4. Route resolution to evidence/knowledge governance.
5. Do not rank retrieval relevance as a truth decision.

## Retrieval and context assembly

For retrieval:

- enforce namespace and scope;
- select the revision valid at the requested `as_of` time;
- exclude quarantined, tombstoned, and expired memory by default;
- return source class separately from retrieval epistemic class;
- treat search score as relevance only.

For context assembly:

- deduplicate exact content hashes;
- respect the explicit context budget;
- persist ordered memory revision identities and hashes;
- compute a deterministic snapshot hash;
- mark replayed snapshots stale when selected revisions are no longer latest;
- block replay when a selected memory is now quarantined or tombstoned.

## Lifecycle states

Supported local states:

```text
ACTIVE -> QUARANTINED -> ACTIVE
ACTIVE -> TOMBSTONED
QUARANTINED -> TOMBSTONED
```

`TOMBSTONED` is terminal in the local reference. Expiry is a retrieval condition, not physical deletion.

## Progressive loading

Read `references/memory-lifecycle-contract.md` when evaluating design provenance, external GitHub mechanisms, temporal validity, context snapshots, or production boundaries.

## Evidence status

Use:

- `VERIFIED_TESTED_SCOPE` for behavior exercised by the bundled deterministic tests;
- `CONDITIONAL` for behavior that depends on external authority or evidence;
- `UNKNOWN/GAP` for distributed, production, privacy, compliance, or semantic-validity claims not established by the local reference.

Do not expose hidden chain-of-thought. Return memory identities, provenance, states, validation results, conflicts, and bounded conclusions.
