````markdown
---
artifact_id: AMOS-UNIVERSAL-RENAME-ENGINE
name: amos-universal-rename-engine
title: "AMOS Universal Rename Engine — Governed Deterministic Namespace Migration"
document_version: "3.0.0"
engine_version: "2.0.0"
migration_contract_version: "1.0.0"
amos_core_target: "v4.4"

created: "2026-08-22"
updated: "2026-08-25"

origin_architect: "Trang Phan"
steward: "Trang Phan"

canon-group: tech-ai
canon-type: framework
rscf-state: source-claim
conclusion_class: "SOURCE_CLAIM / AMOS_MODEL"
implementation_state: "SOURCE_IMPLEMENTATION"
execution_risk: "MUTATING_FILESYSTEM"

topic: integratedagent

aliases:
  - AMOS Universal Rename Engine
  - AMOS Namespace Migration Engine
  - AMOS Deterministic Rename Engine
  - Universal Rename Engine

tags:
  - canon-group/tech-ai
  - canon/framework
  - rscf/claim
  - rscf/provenance
  - rscf/state/source-claim
  - topic/integratedagent
  - topic/rename-engine
  - topic/namespace-migration
  - topic/repository-migration
  - agents

governing_law: "integrity > completeness > fluency > speed > token savings"
---

# AMOS Universal Rename Engine
## Governed Deterministic Namespace Migration

> **Document version:** `3.0.0`  
> **Engine version:** `2.0.0`  
> **Migration contract:** `1.0.0`  
> **AMOS_CORE target:** `v4.4`  
> **Origin architect / steward:** Trang Phan  
> **Current source class:** `SOURCE_IMPLEMENTATION`  
> **Primary risk:** repository-wide filesystem mutation

---

# 0. EXECUTIVE STATUS

The supplied Python source implements a repository rename utility that:

```text
DISCOVERS TARGET ROOT
↓
ENUMERATES DIRECTORIES
↓
CLEANS SELECTED NAME TOKENS
↓
NORMALIZES UNDERSCORES
↓
ADDS _v0 WHEN VERSION IS ABSENT
↓
RENAMES DIRECTORIES DEEPEST-FIRST
↓
RENAMES SUPPORTED FILES
````

Its current source behavior is materially stronger than a stub.

It can perform real filesystem mutation because:

```python
DRY_RUN = False
```

and:

```python
path.rename(new_path)
```

is executed when rename conditions pass.

Therefore:

```text
CurrentSource
=
REAL_LOCAL_FILESYSTEM_MUTATOR
```

for the declared target tree, assuming normal Python `Path.rename()` semantics and successful filesystem permissions.

However:

```text
"clean"
"safe"
"deterministic"
```

are claims that require qualification.

The source is deterministic for a fixed filesystem snapshot and fixed configuration, but it is **not yet migration-safe** because it does not currently implement:

```text
collision detection
reference rewriting
dependency graph repair
manifest generation
transaction rollback
case-fold collision detection
cross-file import repair
canonical identity preservation
post-migration verification
```

Correct classification:

```yaml
status:
  target_discovery: IMPLEMENTED
  supported_extension_filter: IMPLEMENTED
  skip_directory_filter: PARTIAL
  name_cleaning: IMPLEMENTED
  version_suffix_insertion: IMPLEMENTED
  deepest_first_directory_pass: IMPLEMENTED
  file_rename_pass: IMPLEMENTED
  dry_run_mode: IMPLEMENTED
  real_mutation_mode: IMPLEMENTED

  collision_preflight: MISSING
  rename_manifest: MISSING
  reference_rewrite: MISSING
  import_repair: MISSING
  link_repair: MISSING
  rollback: MISSING
  atomic_transaction: MISSING
  provenance_ledger: MISSING
  post_migration_validation: MISSING

  overall:
    state: MUTATING_RENAME_ENGINE_V1
```

---

# 1. SOURCE IMPLEMENTATION

```python
from pathlib import Path
import re


# ============================================================
# AMOS UNIVERSAL RENAME ENGINE — CLEAN, SAFE, DETERMINISTIC
# ============================================================

# Toggle: DRY RUN vs REAL RUN
DRY_RUN = False

# Root folder automatically detected
TARGET_ROOT = Path(__file__).resolve().parent / "_AMOS_UNIVERSE"

# Folders we should NEVER modify
SKIP_DIRS = {
    ".git",
    ".idea",
    ".vscode",
    "__pycache__",
    "_Archive",
}

# Remove these patterns from filenames/folder names
REMOVE_PATTERNS = [
    r"SUPERSTACK",
    r"SUPER",
    r"SUPREME",
    r"vInfinity",
    r"vINFINITY",
    r"INFINITY",
    r"OMEGA",
    r"FULL",
    r"EXPANDED",
    r"CANON",
    r"ULTRA",
]

# Allowed file extensions to rename
FILE_EXTS = {
    ".json",
    ".py",
    ".ts",
    ".md",
}


# ----------------------- HELPERS -----------------------

def clean_base(name: str) -> str:
    """Cleans unwanted patterns and normalizes underscores."""
    cleaned = name

    for pat in REMOVE_PATTERNS:
        cleaned = re.sub(
            pat,
            "",
            cleaned,
            flags=re.IGNORECASE,
        )

    cleaned = re.sub(r"__+", "_", cleaned)

    cleaned = cleaned.strip("_")

    return cleaned


def apply_version(name: str) -> str:
    """Adds _v0 if there is no version suffix."""
    if re.search(r"_v\d+$", name):
        return name

    return f"{name}_v0"


def rename_item(path: Path):
    """Renames a single file or directory."""
    parent = path.parent
    old_name = path.name

    if path.is_dir() and old_name in SKIP_DIRS:
        return

    if path.is_dir():
        new_base = clean_base(old_name)
        new_base = apply_version(new_base)
        new_path = parent / new_base

    elif path.suffix in FILE_EXTS:
        stem = clean_base(path.stem)
        stem = apply_version(stem)
        new_path = parent / f"{stem}{path.suffix}"

    else:
        return

    if new_path == path:
        return

    print(
        f"{'DRY-RUN' if DRY_RUN else 'RENAME'}: "
        f"{path} → {new_path}"
    )

    if not DRY_RUN:
        path.rename(new_path)


# ----------------------- MAIN -----------------------

def main():
    if not TARGET_ROOT.exists():
        print(
            f"ERROR: Target root does not exist: "
            f"{TARGET_ROOT}"
        )
        return

    print(
        f"Running rename engine on: "
        f"{TARGET_ROOT}\n"
    )

    dirs = sorted(
        (
            p
            for p in TARGET_ROOT.rglob("*")
            if p.is_dir()
        ),
        key=lambda p: len(p.parts),
        reverse=True,
    )

    for d in dirs:
        rename_item(d)

    for f in TARGET_ROOT.rglob("*"):
        if f.is_file():
            rename_item(f)

    print("\nDONE.")


if __name__ == "__main__":
    main()
```

---

# 2. PURPOSE

The engine is intended to normalize AMOS repository namespace identity.

Its source policy is:

```text
REMOVE SELECTED DECORATIVE TOKENS
+
NORMALIZE UNDERSCORES
+
ENSURE EXPLICIT VERSION SUFFIX
```

Conceptually:

[
N'
==

V
\left(
C(N)
\right)
]

where:

* (N) = original name;
* (C) = cleaning transformation;
* (V) = version-normalization transformation;
* (N') = resulting filesystem name.

---

# 3. WHAT THE ENGINE ACTUALLY CHANGES

The source removes case-insensitive occurrences of:

```text
SUPERSTACK
SUPER
SUPREME
vInfinity
vINFINITY
INFINITY
OMEGA
FULL
EXPANDED
CANON
ULTRA
```

Then:

```text
multiple underscores
→
single underscore
```

and:

```text
leading/trailing underscore
→
removed
```

Finally:

```text
name without _vN suffix
→
name_v0
```

---

# 4. HARD SEMANTIC WARNING

The engine currently assumes the removable terms are non-load-bearing namespace decoration.

That assumption is not proven.

For example:

```text
AMOS_SUPER_CODE
```

may become:

```text
AMOS_CODE_v0
```

But:

```text
SUPER
```

could be semantically meaningful in a historical identifier, dependency, import path, canon lineage, or API contract.

Therefore:

```text
TokenRemoval
!=
SemanticPreservation
```

Hard AMOS rule:

```text
A rename migration is valid only if
identity and dependency semantics survive
the transformation.
```

---

# 5. VERSION / LINEAGE MODEL

Four version axes should remain separate.

```text
DocumentVersion
=
this Markdown specification

EngineVersion
=
rename engine implementation

MigrationContractVersion
=
rename/mapping semantics

TargetArtifactVersion
=
versions assigned to renamed files/directories
```

Do not collapse them.

```yaml
VERSION_ID:
  artifact: AMOS-UNIVERSAL-RENAME-ENGINE
  document: 3.0.0
  engine: 2.0.0
  migration_contract: 1.0.0
  core_target: AMOS_CORE_4.4
```

---

# 6. SOURCE VERSION RULE

Current rule:

```python
if re.search(r"_v\d+$", name):
    return name

return f"{name}_v0"
```

Therefore recognized versions are only:

```text
_v0
_v1
_v2
...
```

The source does **not** recognize:

```text
_v1.0
_v1.2.3
-v1
version_1
vInfinity
v4_4
_v4_4
```

The engine therefore implements:

```text
INTEGER_SUFFIX_VERSIONING
```

not general semantic versioning.

---

# 7. VERSIONING FIREWALL

Adding `_v0` is not equivalent to discovering an artifact's true version.

```text
MissingVersionLabel
→ _v0
```

means:

```text
assigned migration baseline
```

not:

```text
historically verified version zero
```

Correct epistemic class:

```text
MIGRATION_ASSIGNED_VERSION
```

---

# 8. RECOMMENDED VERSION MODEL

Use explicit state:

```yaml
ArtifactVersion:
  source_name:
  source_version:
  detected_version:
  assigned_version:
  assignment_reason:
  migration_epoch:
```

If no historical version can be resolved:

```text
source_version = UNKNOWN/GAP
assigned_version = v0
```

This preserves the distinction.

---

# 9. TARGET ROOT

Current source:

```python
TARGET_ROOT = (
    Path(__file__).resolve().parent
    / "_AMOS_UNIVERSE"
)
```

Therefore the migration scope is structurally anchored to:

```text
script directory
+
_AMOS_UNIVERSE
```

This is preferable to unconstrained filesystem traversal.

However, it should still be validated before mutation.

---

# 10. TARGET ROOT INVARIANTS

Before any real run:

```text
TargetRootExists
∧ TargetRootIsDirectory
∧ TargetRootResolved
∧ TargetRootAllowed
∧ TargetRootNotSymlinkEscape
```

Recommended:

```python
root = TARGET_ROOT.resolve(strict=True)

if root.name != "_AMOS_UNIVERSE":
    raise RuntimeError("Unexpected migration root")
```

For stronger environments, bind an expected root hash or repository identity.

---

# 11. SKIP DIRECTORY MODEL

Source:

```python
SKIP_DIRS = {
    ".git",
    ".idea",
    ".vscode",
    "__pycache__",
    "_Archive",
}
```

Important limitation:

The source checks:

```python
if path.is_dir() and old_name in SKIP_DIRS:
    return
```

but `TARGET_ROOT.rglob("*")` may still traverse **inside** those directories.

Therefore:

```text
SkipRename(directory)
!=
SkipTraversal(directory)
```

This is a structural bug in protection semantics.

A protected directory may remain named `.git`, but descendants may still be discovered depending on traversal behavior and root layout.

---

# 12. SKIP-SUBTREE INVARIANT

Correct semantics should be:

```text
ProtectedDirectory
→
ProtectedEntireSubtree
```

not merely:

```text
ProtectedDirectoryName
→
DoNotRenameDirectoryEntry
```

Recommended traversal should explicitly prune protected roots.

---

# 13. FILE EXTENSION SCOPE

Current source renames only:

```text
.json
.py
.ts
.md
```

This is a positive restriction.

Unsupported files remain unchanged.

But references to renamed files may exist inside:

```text
.yaml
.yml
.toml
.txt
tsx
js
jsonl
ini
cfg
lockfiles
shell scripts
```

Therefore:

```text
RenameScope
!=
ReferenceScope
```

Reference auditing must be broader than rename-extension filtering.

---

# 14. DIRECTORY-FIRST ORDERING

The source intentionally renames directories:

```text
deepest
→
shallowest
```

This is structurally reasonable because parent renames can invalidate paths to children.

The ordering function is:

```python
key=lambda p: len(p.parts),
reverse=True,
```

Therefore:

[
depth(p_i)>depth(p_j)
\Rightarrow
p_i
\text{ processed first}
]

for unequal depths.

---

# 15. CRITICAL TWO-PASS PATH PROBLEM

The source performs:

```text
PASS 1
rename directories

PASS 2
TARGET_ROOT.rglob("*")
rename files
```

This means file discovery occurs after directory movement.

That can work for many cases.

However, it creates a different issue:

the source has no single immutable migration plan.

The actual file set observed during pass 2 depends on successful pass-1 mutations.

Therefore:

```text
MigrationExecution
depends on
intermediate filesystem state
```

This weakens deterministic replay.

---

# 16. PLAN-FIRST ARCHITECTURE

AMOS should separate:

```text
PLAN
```

from:

```text
COMMIT
```

Correct migration pipeline:

```text
DISCOVER
↓
NORMALIZE
↓
BUILD COMPLETE RENAME PLAN
↓
VALIDATE
↓
DETECT COLLISIONS
↓
DETECT REFERENCE IMPACT
↓
APPROVE
↓
COMMIT
↓
VERIFY
↓
WRITE RECEIPT
```

Not:

```text
DISCOVER ITEM
↓
IMMEDIATELY RENAME ITEM
```

---

# 17. RENAME PLAN OBJECT

```yaml
RenamePlan:
  plan_id:
  engine_version:
  migration_contract_version:

  target_root:

  created_at:

  operations:
    - operation_id:
      object_type:
      old_path:
      new_path:
      old_name:
      new_name:
      reasons: []
      semantic_status:

  skipped: []

  collisions: []

  affected_references: []

  unresolved_gaps: []

  plan_hash:
```

---

# 18. RENAME OPERATION

```yaml
RenameOperation:
  operation_id:

  source:
    path:
    name:
    type:
    extension:

  destination:
    path:
    name:

  transformations:
    removed_tokens: []
    underscore_normalized:
    version_added:

  identity:
    source_version:
    assigned_version:

  risk:
    collision:
    reference_impact:
    semantic_impact:

  status:
    PLANNED
```

---

# 19. CLEANING FUNCTION

Current transformation:

[
C(n)
====

StripUnderscore
(
CollapseUnderscore
(
RemovePatterns(n)
)
)
]

This operation should satisfy:

```text
Deterministic:
C(n) = C(n)
```

for identical inputs and rule set.

However, another desired property is:

```text
Idempotent:
C(C(n)) = C(n)
```

The cleaning portion is broadly idempotent under current rules.

---

# 20. VERSION APPLICATION IDEMPOTENCE

For recognized `_vN` suffixes:

[
V(V(n))=V(n)
]

because the second pass detects the existing suffix.

Thus:

```text
apply_version()
```

is idempotent for the current version grammar.

---

# 21. FULL TRANSFORMATION IDEMPOTENCE

Define:

[
T(n)=V(C(n))
]

Then desired:

[
T(T(n))=T(n)
]

This should be explicitly tested.

---

# 22. EMPTY-NAME FAILURE

The current source can produce an empty cleaned name.

Example:

```text
FULL
```

becomes:

```text
""
```

then:

```text
_v0
```

Similarly:

```text
SUPER
OMEGA
CANON
```

may collapse into structurally weak names.

Therefore:

```text
NonEmptyInput
does not imply
MeaningfulOutput
```

Add:

```text
if not cleaned:
    reject/quarantine
```

---

# 23. TOKEN-CONCATENATION FAILURE

Example:

```text
SUPERSTACKAgent
```

may become:

```text
Agent
```

That may be intended.

But:

```text
OMEGABridge
```

becomes:

```text
Bridge
```

which can collide with an existing `Bridge`.

Token removal currently does not require token boundaries.

Therefore:

```text
substring removal
```

may mutate legitimate compound identifiers.

---

# 24. TOKEN BOUNDARY POLICY

Rename rules should explicitly declare whether each pattern is:

```text
EXACT_TOKEN
PREFIX
SUFFIX
SUBSTRING
REGEX
```

Example:

```yaml
RenameRule:
  rule_id: R-OMEGA
  pattern: OMEGA
  match_mode: TOKEN
  case_sensitive: false
  replacement: ""
```

This is safer than a flat regex list.

---

# 25. PATTERN PRECEDENCE

The source wisely places:

```text
SUPERSTACK
```

before:

```text
SUPER
```

because otherwise:

```text
SUPERSTACK
```

would partially become:

```text
STACK
```

first.

This means rule ordering is semantically load-bearing.

Therefore:

```text
REMOVE_PATTERNS
```

is not merely a set.

It is an ordered rewrite system.

---

# 26. RULESET VERSIONING

The rename rule set should have its own version.

```yaml
RenameRuleSet:
  id: AMOS_NAMESPACE_NORMALIZATION
  version: 1.0.0

  ordered_rules: []
```

Changing rule order may change outputs.

Therefore:

```text
RuleSetOrder
=
part of migration identity
```

---

# 27. COLLISION PROBLEM

Suppose:

```text
AMOS_SUPER_CORE.py
AMOS_CORE.py
```

Both can map to:

```text
AMOS_CORE_v0.py
```

Current source has no explicit collision preflight.

Depending on platform and destination existence:

```python
path.rename(new_path)
```

may fail or have platform-specific replacement semantics.

This is unacceptable for a governed repository migration.

---

# 28. COLLISION INVARIANT

Before mutation:

```text
∀ old_i ≠ old_j:
new_i ≠ new_j
```

and:

```text
new_path
must not already exist
```

unless the migration explicitly supports controlled merge semantics.

Default:

```text
COLLISION
→
ABORT
```

---

# 29. CASE-FOLD COLLISIONS

Cross-platform repositories may move between case-sensitive and case-insensitive filesystems.

Example:

```text
OmegaAgent.py
OMEGAAgent.py
```

may normalize unexpectedly.

Therefore compute:

```text
casefold(new_path)
```

and detect duplicates.

---

# 30. NORMALIZATION COLLISIONS

Unicode names can be canonically equivalent despite different byte sequences.

A hardened migration may normalize names using a declared Unicode form:

```text
NFC
```

before collision comparison.

This is especially relevant for cross-platform repositories.

---

# 31. NAME IDENTITY VS ARTIFACT IDENTITY

Filesystem names are representations.

They should not be the sole identity of an AMOS artifact.

```text
ArtifactIdentity
!=
Filename
```

Recommended persistent identity:

```yaml
ArtifactIdentity:
  artifact_id:
  current_path:
  previous_paths: []
  version:
  provenance:
```

This allows safe rename without identity loss.

---

# 32. PATH ALIAS LEDGER

A migration should retain:

```text
OLD PATH
→
NEW PATH
```

Example:

```yaml
PathAlias:
  old: "_AMOS_UNIVERSE/AMOS_SUPER_CORE.py"
  new: "_AMOS_UNIVERSE/AMOS_CORE_v0.py"
  migration_id:
  timestamp:
```

This supports:

```text
recovery
search
link repair
historical provenance
```

---

# 33. REFERENCE INTEGRITY

Renaming a file or folder can break:

```text
Python imports
TypeScript imports
Markdown links
JSON references
configuration paths
registry entries
test fixtures
documentation
runtime manifests
CI paths
package exports
```

Therefore:

```text
FilesystemRenameComplete
!=
RepositoryMigrationComplete
```

---

# 34. REFERENCE GRAPH

Before commit:

```text
Artifact
← referenced by ←
Files
Configs
Imports
Docs
Registries
Tests
Build Scripts
```

For each rename:

```text
old_path
→ locate references
→ classify reference
→ update or quarantine
```

---

# 35. REFERENCE TYPES

```text
PYTHON_IMPORT
TYPESCRIPT_IMPORT
RELATIVE_PATH
ABSOLUTE_PATH
MARKDOWN_LINK
WIKI_LINK
JSON_FIELD
YAML_FIELD
CONFIG_REFERENCE
REGISTRY_NAME
STRING_LITERAL
GENERATED_REFERENCE
UNKNOWN
```

Not all string matches should be automatically rewritten.

---

# 36. SYMBOL RENAME FIREWALL

Current engine renames filesystem objects only.

It does not rename Python classes, TypeScript exports, JSON IDs, or registry identifiers.

This is good unless semantic migration requires symbol renaming.

Hard distinction:

```text
PathRename
!=
SymbolRename
```

Automatic path cleanup must not silently imply object-symbol cleanup.

---

# 37. REGISTRY INTEGRITY

If a component registry contains:

```text
name="AMOS_SUPER_CORE"
```

but file becomes:

```text
AMOS_CORE_v0.py
```

the registry identity may intentionally remain unchanged.

Therefore:

```text
FileName
RegistryName
ArtifactID
ClassName
```

must be independently typed.

Do not mechanically force them to match.

---

# 38. DRY-RUN MODE

Source supports:

```python
DRY_RUN = True
```

which prevents `path.rename()`.

This is a strong prerequisite but currently only prints operations.

A governed dry run should produce a deterministic plan artifact.

```yaml
DryRunResult:
  plan_id:
  operations:
  collisions:
  skipped:
  affected_references:
  unresolved_gaps:
  plan_hash:
  status:
```

---

# 39. DEFAULT MODE CORRECTION

Current source:

```python
DRY_RUN = False
```

means real mutation is default.

For a repository-wide migration engine, AMOS safer default is:

```python
DRY_RUN = True
```

with explicit opt-in required for commit.

Hard rule:

```text
Mutation
requires
explicit commit intent.
```

---

# 40. TWO-PHASE MIGRATION

Recommended:

```text
PHASE 1 — PREPARE
discover
plan
validate
hash
approve

PHASE 2 — COMMIT
execute exact approved plan
verify
record
```

Conceptually:

[
Commit(P)
]

is permitted only if the filesystem snapshot still matches the prepared plan.

---

# 41. SNAPSHOT FRESHNESS

Between dry run and execution, the repository can change.

Therefore store:

```yaml
MigrationSnapshot:
  root:
  file_count:
  directory_count:
  tree_hash:
  created_at:
```

Before commit:

```text
PreparedSnapshotHash
=
CurrentSnapshotHash
```

or re-plan.

---

# 42. MIGRATION TRANSACTION

```yaml
RenameTransaction:
  tx_id:
  plan_id:
  snapshot_hash:

  state:
    PREPARED

  operations: []

  applied: []
  failed: []

  rollback_plan:

  started_at:
  finished_at:
```

---

# 43. TRANSACTION STATE MACHINE

```text
DISCOVERED
↓
PLANNED
↓
VALIDATED
↓
APPROVED
↓
PREPARED
↓
COMMITTING
↓
COMMITTED
↓
VERIFIED
```

Failure branches:

```text
REJECTED
ABORTED
FAILED
ROLLING_BACK
ROLLED_BACK
IN_DOUBT
```

---

# 44. DIRECTORY RENAME COMPLEXITY

Renaming nested paths changes descendant path strings.

Therefore migration plans should use stable object identity or carefully ordered mappings.

Example:

```text
A/B/C.py
```

with:

```text
B → B_v0
C.py → C_v0.py
```

final destination is:

```text
A/B_v0/C_v0.py
```

The engine must not use stale pre-parent-rename paths during commit.

---

# 45. STABLE PLAN REPRESENTATION

Represent each object relative to the root:

```yaml
RenameObject:
  object_id:
  original_relative_path:
  original_parent_id:
  new_local_name:
```

Then derive final paths after all parent transformations.

This is safer than storing only mutable absolute paths.

---

# 46. OBJECT IDENTITY

Possible deterministic migration object ID:

[
ID
==

H(
relative_path
\Vert
object_type
\Vert
pre_migration_metadata
)
]

This is a migration identity, not a universal object identity.

---

# 47. FILE HASHES

For files:

```yaml
FileIdentity:
  path:
  size:
  sha256:
```

Hash before rename and verify after rename.

Expected:

[
Hash_{before}
=============

Hash_{after}
]

because rename should not modify file contents.

---

# 48. CONTENT-INTEGRITY INVARIANT

For rename-only migration:

```text
FileBytesBefore
=
FileBytesAfter
```

unless reference rewriting is included in the same migration.

If references are rewritten, content changes must be separately recorded.

---

# 49. RENAME-ONLY VS REFACTOR MODE

Two modes should be explicit.

```text
MODE_A
RENAME_ONLY
```

changes paths only.

```text
MODE_B
RENAME_AND_REWRITE_REFERENCES
```

changes paths plus selected source references.

Do not mix them implicitly.

---

# 50. BACKUP / ROLLBACK

The source has no rollback.

A governed engine should record inverse operations.

For each:

```text
old → new
```

record:

```text
new → old
```

Rollback executes in reverse dependency order.

---

# 51. ROLLBACK LIMIT

Rollback is possible only if:

```text
destination still exists
source has not been recreated
no conflicting changes occurred
```

Therefore rollback should be verified, not assumed.

---

# 52. GIT-AWARE SAFETY

If running inside a Git repository:

recommended checks:

```text
repository root known
working tree state known
branch known
HEAD known
```

Optionally require:

```text
clean working tree
```

for large rename migrations.

Do not assume Git exists universally, but if present it provides strong recovery evidence.

---

# 53. GIT IS NOT MIGRATION AUTHORITY

Even if:

```text
git status clean
```

that does not mean rename policy is correct.

Git gives:

```text
recoverability
diff visibility
history
```

not semantic validation.

---

# 54. SYMLINK FIREWALL

Filesystem traversal can encounter symlinks.

The migration must explicitly define:

```text
rename symlink itself?
follow target?
ignore?
reject?
```

Recommended default:

```text
DO_NOT_FOLLOW_EXTERNAL_SYMLINK_TARGETS
```

to prevent root escape.

---

# 55. PATH ESCAPE INVARIANT

Every planned target must satisfy:

[
ResolvedPath
\in
TargetRoot
]

No operation may escape `_AMOS_UNIVERSE`.

---

# 56. PERMISSION FAILURES

Possible failure:

```text
permission denied
read-only filesystem
locked file
open handle
platform restriction
```

These must create structured failures rather than leaving an unexplained partial migration.

---

# 57. PARTIAL MIGRATION

Current source can:

```text
rename N objects
then fail at N+1
```

leaving a partially migrated repository.

This is one of the largest current risks.

Status must then be:

```text
PARTIAL / IN_DOUBT
```

not:

```text
DONE
```

---

# 58. COMMIT RECEIPT

```yaml
MigrationReceipt:
  migration_id:
  plan_hash:
  engine_version:
  ruleset_version:

  root:

  operations_planned:
  operations_applied:
  operations_failed:

  before_tree_hash:
  after_tree_hash:

  references_updated:

  verification:
    passed:

  rollback_available:

  status:
```

---

# 59. PROVENANCE

Every renamed object should retain lineage.

```yaml
RenameProvenance:
  artifact_id:
  old_path:
  new_path:

  migration_id:
  operation_id:

  rules:
    - rule_id

  source_version:
  assigned_version:

  performed_at:
```

---

# 60. RENAME RULE REGISTRY

```yaml
rules:
  - id: R001
    pattern: SUPERSTACK
    mode: SUBSTRING
    case_sensitive: false
    replacement: ""

  - id: R002
    pattern: SUPER
    mode: SUBSTRING
    case_sensitive: false
    replacement: ""

  - id: R003
    pattern: SUPREME
    mode: SUBSTRING
    case_sensitive: false
    replacement: ""

  - id: R004
    pattern: vInfinity
    mode: SUBSTRING
    case_sensitive: false
    replacement: ""

  - id: R005
    pattern: INFINITY
    mode: SUBSTRING
    case_sensitive: false
    replacement: ""

  - id: R006
    pattern: OMEGA
    mode: SUBSTRING
    case_sensitive: false
    replacement: ""

  - id: R007
    pattern: FULL
    mode: SUBSTRING
    case_sensitive: false
    replacement: ""

  - id: R008
    pattern: EXPANDED
    mode: SUBSTRING
    case_sensitive: false
    replacement: ""

  - id: R009
    pattern: CANON
    mode: SUBSTRING
    case_sensitive: false
    replacement: ""

  - id: R010
    pattern: ULTRA
    mode: SUBSTRING
    case_sensitive: false
    replacement: ""
```

This preserves exact migration semantics.

---

# 61. DUPLICATE RULE NOTE

The source lists both:

```text
vInfinity
vINFINITY
```

while matching with:

```python
flags=re.IGNORECASE
```

Therefore those two rules are semantically redundant.

```text
vInfinity
≈
vINFINITY
```

under the configured matcher.

This redundancy should be removed or documented.

---

# 62. RULE REDUNDANCY INVARIANT

For rules (r_i,r_j):

```text
EquivalentMatch(r_i, r_j)
→
deduplicate
```

unless order or provenance requires both identities.

---

# 63. REGEX SAFETY

Current patterns are simple literals encoded as regex strings.

Future patterns may contain metacharacters.

If rules are intended as literals:

```python
re.escape(token)
```

should be used.

Otherwise the rule schema must explicitly mark:

```text
REGEX
```

vs:

```text
LITERAL
```

---

# 64. RENAME DECISION FUNCTION

Conceptual:

[
Rename(p)
=========

Supported(p)
\land
NotProtected(p)
\land
T(name(p))\neq name(p)
]

But production-safe rename requires:

[
SafeRename(p)
=============

Rename(p)
\land
NoCollision(p)
\land
SemanticRiskAccepted(p)
\land
ReferenceImpactHandled(p)
]

---

# 65. DETERMINISM CONTRACT

For a fixed:

```text
filesystem snapshot
ruleset
engine version
platform normalization policy
```

the planned mapping should be identical.

```text
Plan(S,R,V)
=
Plan(S,R,V)
```

Output ordering should also be deterministic.

Sort all operations explicitly.

Do not rely on unspecified traversal order.

---

# 66. PLATFORM FIREWALL

`Path.rename()` behavior can differ by operating system and filesystem.

Potential differences:

```text
destination overwrite behavior
case-only rename behavior
locked-file semantics
unicode normalization
cross-device behavior
```

Therefore:

```text
DeterministicNameMapping
!=
PlatformIndependentExecution
```

---

# 67. CASE-ONLY RENAMES

On case-insensitive filesystems:

```text
Foo.py
→
foo.py
```

may require an intermediate temporary name.

The current source does not explicitly handle this class.

---

# 68. TEMPORARY NAMESPACE

For collision-safe commits, a two-step temporary namespace may be required:

```text
old
→
__amos_tmp_<operation_id>
→
final
```

This prevents rename cycles such as:

```text
A → B
B → A
```

Even if current rules rarely create swaps, the engine should model the case.

---

# 69. RENAME GRAPH

Treat rename mapping as directed graph:

[
G_R=(V,E)
]

where:

```text
old_path → new_path
```

Detect:

```text
collisions
cycles
self-edges
many-to-one edges
```

before commit.

---

# 70. MANY-TO-ONE FAILURE

If:

[
a\neq b
]

but:

[
T(a)=T(b)
]

then:

```text
MANY_TO_ONE_COLLISION
```

and migration must stop unless an explicit merge rule exists.

---

# 71. EMPTY / RESERVED NAMES

Validate output names against:

```text
empty name
"." / ".."
OS reserved names
invalid path characters
path length limits
```

Platform-specific checks should remain explicit.

---

# 72. SEMANTIC CLASSIFICATION

Each token removal should be classified:

```text
DECORATIVE
HISTORICAL
VERSION
CANONICAL_IDENTITY
UNKNOWN
```

Only:

```text
DECORATIVE
```

should be automatically removable without further evidence.

If classification is:

```text
UNKNOWN
```

default:

```text
QUARANTINE
```

for high-value repositories.

---

# 73. CANON TOKEN WARNING

The source removes:

```text
CANON
```

from names.

In AMOS, `CANON` may be epistemically load-bearing.

For example:

```text
AMOS_CANON_REGISTRY
```

becoming:

```text
AMOS_REGISTRY_v0
```

loses a meaningful distinction.

Therefore:

```text
CANON
```

should **not** be globally treated as decorative without a migration-specific evidence rule.

This is a critical semantic risk.

---

# 74. OMEGA TOKEN WARNING

Similarly:

```text
OMEGA
```

may represent a historically meaningful AMOS subsystem or lineage.

Removing it can collapse distinct components.

Therefore:

```text
OMEGA removal
```

should be:

```text
CONDITIONAL
```

not universally safe.

---

# 75. FULL / EXPANDED WARNING

Tokens such as:

```text
FULL
EXPANDED
```

may encode artifact completeness variants.

Removing them can merge:

```text
BASE
FULL
EXPANDED
```

into one namespace.

If the distinctions represent different content, token deletion causes identity collapse.

---

# 76. IDENTITY-COLLAPSE TEST

Before allowing a rule:

```text
Group artifacts by normalized name.
```

If multiple source artifacts map to one normalized identity:

```text
IDENTITY_COLLAPSE
```

must be surfaced.

---

# 77. CONTENT DIFFERENCE TEST

For colliding candidate files:

```text
hash(A) != hash(B)
```

means they are not byte-identical.

Never merge silently.

Even if:

```text
hash(A) == hash(B)
```

automatic merge still requires policy because provenance may differ.

---

# 78. DIRECTORY COLLAPSE TEST

Two directories may normalize to one destination.

Their child trees may differ.

Therefore directory collision analysis must recursively inspect:

```text
child identities
file hashes
subtree conflicts
```

before any merge decision.

---

# 79. AMOS MIGRATION PRINCIPLE

Correct transformation:

```text
Ephemeral Name
→ Canonical Identity
```

must preserve:

```text
meaning
provenance
dependencies
version lineage
```

not merely produce shorter names.

---

# 80. MIGRATION MANIFEST

```yaml
AMOSRenameManifest:
  manifest_version: 1.0.0

  migration_id:
  engine_version:
  ruleset_version:

  source_root:
  target_root:

  source_snapshot:
  target_snapshot:

  mappings: []

  collisions: []
  blocked: []
  skipped: []

  reference_updates: []

  provenance:

  verification:

  rollback:
```

---

# 81. PRE-FLIGHT PIPELINE

```text
RESOLVE ROOT
↓
VERIFY ROOT
↓
DISCOVER OBJECTS
↓
PRUNE PROTECTED SUBTREES
↓
COMPUTE NORMALIZED NAMES
↓
BUILD FINAL PATHS
↓
VALIDATE NAMES
↓
DETECT COLLISIONS
↓
BUILD REFERENCE GRAPH
↓
CLASSIFY SEMANTIC RISK
↓
GENERATE PLAN
↓
HASH PLAN
```

No mutation yet.

---

# 82. APPROVAL GATE

Real mutation should require:

```text
DRY RUN PASS
∧ No Critical Collision
∧ No Critical Semantic Gap
∧ Snapshot Fresh
∧ Rollback Available
∧ Explicit Commit Mode
```

---

# 83. COMMIT PIPELINE

```text
LOAD APPROVED PLAN
↓
VERIFY PLAN HASH
↓
VERIFY SOURCE SNAPSHOT
↓
ENTER TEMP NAMESPACE IF REQUIRED
↓
APPLY DIRECTORY OPERATIONS
↓
APPLY FILE OPERATIONS
↓
REWRITE APPROVED REFERENCES
↓
VERIFY TARGETS
↓
VERIFY HASHES
↓
RUN REPOSITORY TESTS
↓
WRITE RECEIPT
```

---

# 84. POST-MIGRATION VERIFICATION

Minimum:

```text
all planned old paths absent
all planned new paths present
no unintended files modified
file hashes preserved for rename-only objects
references resolve
imports resolve
tests pass
protected trees unchanged
manifest complete
```

---

# 85. PYTHON IMPORT VALIDATION

For Python repositories, run at minimum where applicable:

```text
syntax compile
import checks
repository tests
```

Renaming `.py` files can invalidate:

```text
from module import X
import module
package __init__
dynamic imports
plugin registries
```

---

# 86. TYPESCRIPT VALIDATION

Renaming `.ts` files can invalidate:

```text
relative imports
tsconfig path aliases
barrel exports
build references
dynamic imports
```

Therefore run:

```text
typecheck
build
tests
```

where available.

---

# 87. MARKDOWN VALIDATION

Renaming `.md` files can invalidate:

```text
wiki links
relative links
MOC indexes
RSCF paths
documentation references
```

Therefore update link graphs or preserve aliases.

---

# 88. JSON VALIDATION

Renaming `.json` files can invalidate:

```text
configuration references
manifest paths
runtime loaders
test fixtures
schema references
```

Validate JSON syntax and consumer references.

---

# 89. RSCF PATH LINEAGE

If an RSCF node stores:

```text
path:
```

to a renamed artifact, update it only if that field represents physical location.

Do not change:

```text
node_id
semantic identity
origin
claim class
```

merely because the path changed.

---

# 90. PROTECTED AMOS IDENTITIES

Potential protected identity classes:

```text
CANON identifiers
RSCF node IDs
artifact IDs
public API names
registry names
published skill names
version lineage IDs
external integration IDs
```

These require explicit migration rules.

---

# 91. EXTERNAL REFERENCES

Repository-local search cannot detect every consumer.

Possible external consumers:

```text
other repositories
CI
deployment manifests
Drive documents
user scripts
bookmarks
external APIs
published documentation
```

Therefore repository migration conclusion should be scoped:

```text
LOCAL_REFERENCE_COMPLETE
```

not:

```text
GLOBALLY_REFERENCE_COMPLETE
```

unless external dependencies are audited.

---

# 92. FAILURE REGISTRY

```text
F01 TARGET_ROOT_MISSING
F02 TARGET_ROOT_ESCAPE
F03 PROTECTED_SUBTREE_TRAVERSAL
F04 EMPTY_NORMALIZED_NAME
F05 INVALID_OUTPUT_NAME
F06 FILE_COLLISION
F07 DIRECTORY_COLLISION
F08 CASEFOLD_COLLISION
F09 MANY_TO_ONE_MAPPING
F10 RENAME_CYCLE
F11 DESTINATION_ALREADY_EXISTS
F12 SEMANTIC_TOKEN_REMOVAL
F13 CANON_IDENTITY_COLLAPSE
F14 VERSION_IDENTITY_LOSS
F15 REFERENCE_BREAK
F16 IMPORT_BREAK
F17 PARTIAL_MIGRATION
F18 PERMISSION_FAILURE
F19 FILESYSTEM_PLATFORM_DIFFERENCE
F20 SYMLINK_ESCAPE
F21 SNAPSHOT_STALE
F22 ROLLBACK_FAILURE
F23 CONTENT_MUTATION_DURING_RENAME
F24 MANIFEST_INCOMPLETE
F25 POST_MIGRATION_TEST_FAILURE
F26 UNVERIFIED_EXTERNAL_REFERENCE
F27 SOURCE_VERSION_OVERWRITE
F28 DRY_RUN_REAL_RUN_DIVERGENCE
```

---

# 93. FAILURE RECORD

```yaml
RenameFailure:
  failure_id:
  migration_id:
  operation_id:

  class:
  path:
  destination:

  message:

  state:
    BEFORE_MUTATION
    PARTIAL
    IN_DOUBT

  affected_operations: []

  rollback_required:

  repair:

  status:
```

---

# 94. FAILURE RECOVERY

```text
FAILURE
↓
STOP NEW MUTATIONS
↓
CAPTURE CURRENT TREE
↓
CLASSIFY APPLIED OPERATIONS
↓
COMPARE AGAINST MANIFEST
↓
ROLL BACK SAFE OPERATIONS
↓
QUARANTINE IN-DOUBT STATE
↓
VERIFY
↓
REPLAN
```

Hard rule:

```text
Do not continue blindly
after an unexpected rename failure.
```

---

# 95. SELECTIVE ROLLBACK

Rollback only affected migration descendants.

Do not reset unrelated repository changes if they were not caused by the rename transaction.

This preserves AMOS selective invalidation semantics.

---

# 96. EXECUTION PROVENANCE

```yaml
RenameExecution:
  run_id:
  migration_id:

  engine_version:
  ruleset_version:

  repository:
    root:
    branch:
    commit:
    dirty_state:

  environment:
    os:
    python:
    filesystem:

  dry_run:

  plan_hash:
  snapshot_hash:

  started_at:
  ended_at:

  applied_operations: []
  failures: []

  receipt_hash:
```

---

# 97. OBSERVABILITY

Track:

```text
objects scanned
directories scanned
files scanned
objects skipped
renames planned
renames applied
collisions
semantic blocks
reference updates
failures
rollback count
elapsed time
```

---

# 98. METRICS FIREWALL

A count such as:

```text
500 renamed files
```

does not imply:

```text
successful migration
```

Success requires:

```text
identity preserved
references valid
tests pass
manifest verified
```

---

# 99. SOURCE CLAIM — CLEAN

The engine title calls itself:

```text
CLEAN
```

AMOS interpretation:

```text
SOURCE_LABEL
```

A "clean" migration would need:

```text
no unresolved collision
no malformed output
no dependency break
no unintended mutation
```

---

# 100. SOURCE CLAIM — SAFE

The engine title calls itself:

```text
SAFE
```

Current source lacks:

```text
collision preflight
rollback
reference repair
transactionality
```

Therefore:

```text
Safe
=
OVERSTATED FOR CURRENT IMPLEMENTATION
```

The code is constrained, but not yet safely migrational in the AMOS governance sense.

---

# 101. SOURCE CLAIM — DETERMINISTIC

This claim is partially supported.

Name transformation itself is deterministic for fixed inputs.

But whole-run reproducibility depends on:

```text
filesystem snapshot
platform
traversal
mutation success
destination conflicts
```

Therefore:

```text
NameMappingDeterministic = DERIVED

WholeMigrationDeterministic =
CONDITIONAL
```

---

# 102. RENAME ENGINE STATE MACHINE

```text
UNINITIALIZED
↓
DISCOVERING
↓
PLANNING
↓
VALIDATING
↓
DRY_RUN_READY
↓
APPROVED
↓
COMMITTING
↓
VERIFYING
↓
COMPLETED
```

Failure states:

```text
BLOCKED
FAILED
PARTIAL
IN_DOUBT
ROLLING_BACK
ROLLED_BACK
```

---

# 103. GOVERNED CONFIGURATION

Recommended:

```yaml
RenameEngineConfig:
  target_root:
  dry_run: true

  file_extensions:
    - .json
    - .py
    - .ts
    - .md

  protected_directories:
    - .git
    - .idea
    - .vscode
    - __pycache__
    - _Archive

  rule_set:
    id: AMOS_NAMESPACE_NORMALIZATION
    version: 1.0.0

  versioning:
    strategy: ASSIGN_V0_WHEN_MISSING
    grammar: "_v[0-9]+"

  collision_policy: ABORT

  unknown_semantic_policy: QUARANTINE

  require_clean_git: false
  require_manifest: true
  require_verification: true
```

---

# 104. HARD RENAME INVARIANTS

```text
I01 TargetRootIsExplicit
I02 ProtectedSubtreesAreNotTraversed
I03 DryRunIsDefault
I04 PlanPrecedesMutation
I05 PlanIsDeterministic
I06 EveryMutationHasManifestEntry
I07 NoManyToOneMappingWithoutExplicitMerge
I08 DestinationCollisionBlocksCommit
I09 EmptyNormalizedNamesAreRejected
I10 PathRename != SemanticIdentityRename
I11 ArtifactIDSurvivesPathRename
I12 VersionAssignment != HistoricalVersionDiscovery
I13 CANONIsNotAutomaticallyDecorative
I14 OMEGAIsNotAutomaticallyDecorative
I15 FULL/EXPANDEDMayEncodeVariantIdentity
I16 FileBytesPreservedInRenameOnlyMode
I17 ReferencesMustBeAudited
I18 PartialMigrationMustRemainVisible
I19 RollbackMustBeExplicit
I20 DryRunSuccess != RealRunSuccess
I21 GitClean != SemanticSafety
I22 FilesystemMapping != RuntimeCorrectness
I23 MigrationSuccessRequiresPostValidation
I24 UnknownCriticalSemanticImpactBlocksCommit
```

---

# 105. TEST SUITE — PURE FUNCTIONS

```text
T01 clean_base removes SUPERSTACK
T02 clean_base removes SUPER case-insensitively
T03 clean_base removes OMEGA
T04 clean_base collapses duplicate underscores
T05 clean_base strips boundary underscores
T06 apply_version adds _v0
T07 apply_version preserves _v0
T08 apply_version preserves _v12
T09 transformation is idempotent
T10 unsupported semantic version grammar is detected
T11 empty cleaned base rejected
T12 redundant rules detected
```

---

# 106. TEST SUITE — PLANNER

```text
T13 protected directory excluded
T14 protected subtree excluded
T15 unsupported extension skipped
T16 supported extension planned
T17 directory planned
T18 deepest-parent relationships resolved
T19 old/new mapping deterministic
T20 many-to-one collision detected
T21 existing destination detected
T22 casefold collision detected
T23 rename cycle detected
T24 invalid target name rejected
T25 final descendant paths computed correctly
```

---

# 107. TEST SUITE — EXECUTION

```text
T26 dry run performs zero renames
T27 dry run produces manifest
T28 real run applies approved plan only
T29 stale snapshot blocks commit
T30 file hash preserved
T31 directory hierarchy preserved
T32 partial failure enters PARTIAL
T33 rollback reverses applied operations
T34 rollback conflict detected
T35 manifest matches actual filesystem
```

---

# 108. TEST SUITE — REPOSITORY INTEGRITY

```text
T36 Python imports valid
T37 TypeScript imports valid
T38 JSON consumers valid
T39 Markdown links valid
T40 RSCF path references updated
T41 registry identities preserved
T42 protected directories unchanged
T43 repository tests pass
T44 no unintended file-content changes
T45 migration receipt generated
```

---

# 109. RSCF — CURRENT SOURCE

```yaml
claim_id: RENAME-ENGINE-SOURCE-001

claim: >
  The supplied Python script traverses the _AMOS_UNIVERSE directory,
  removes configured case-insensitive name patterns, normalizes
  underscores, appends _v0 where an integer version suffix is absent,
  and renames supported filesystem objects when DRY_RUN is false.

class: SOURCE_CLAIM

evidence:
  - supplied Python source

dependencies:
  - pathlib.Path
  - re
  - local filesystem semantics

scope:
  supported_file_extensions:
    - .json
    - .py
    - .ts
    - .md

falsifiers:
  - runtime environment changes pathlib semantics materially
  - supplied source differs from executed version

confidence_ceiling:
  source_semantics: high
  repository_runtime_result: not_executed_here
```

---

# 110. RSCF — DETERMINISM CLAIM

```yaml
claim_id: RENAME-ENGINE-DETERMINISM-001

claim: >
  The name-normalization function is deterministic for a fixed input
  name and fixed ordered rule set.

class: DERIVED

premises:
  - regex rules are deterministic
  - no random state is used
  - transformation order is fixed

scope:
  name_transformation_only: true

does_not_establish:
  - platform-independent filesystem execution
  - transactionally deterministic repository migration
```

---

# 111. RSCF — SAFETY CLAIM

```yaml
claim_id: RENAME-ENGINE-SAFETY-001

claim: >
  The current rename engine is safe for unrestricted repository-wide
  production migration.

class: FALSIFIED / OVERSTATED

reasons:
  - no collision preflight
  - no reference repair
  - no rollback
  - no transaction manifest
  - real mutation is default
  - semantic token removal may collapse identities

confidence_ceiling:
  high
```

---

# 112. RSCF — SEMANTIC NORMALIZATION

```yaml
claim_id: RENAME-ENGINE-SEMANTIC-001

claim: >
  Removing SUPER, OMEGA, FULL, EXPANDED, CANON, ULTRA and related
  tokens preserves AMOS artifact meaning.

class: UNKNOWN/GAP

missing:
  - per-token semantic classification
  - artifact lineage analysis
  - collision audit
  - reference audit
  - canon identity audit

competing:
  - tokens are decorative
  - tokens encode historical versions
  - tokens distinguish real subsystem families
  - tokens encode canon status
  - mixed cases exist

confidence_ceiling:
  unknown
```

---

# 113. RSCF — `_v0` ASSIGNMENT

```yaml
claim_id: RENAME-ENGINE-VERSION-001

claim: >
  Appending _v0 to unversioned names provides a deterministic migration
  baseline.

class: AMOS_MODEL

does_not_establish:
  - artifact was historically version zero
  - artifact has never had earlier versions

hard_rule:
  assigned_version_must_remain_distinct_from_source_version: true
```

---

# 114. GAP REGISTRY

| Gap                              | Class                           | Consequence                      |
| -------------------------------- | ------------------------------- | -------------------------------- |
| No collision preflight           | CRITICAL                        | destructive conflict risk        |
| No reference graph               | CRITICAL                        | import/link break risk           |
| No rollback                      | CRITICAL                        | partial migration may persist    |
| `DRY_RUN=False` default          | CRITICAL                        | accidental mutation risk         |
| Protected subtree not pruned     | CRITICAL                        | skip semantics incomplete        |
| No semantic token classification | CRITICAL                        | identity collapse risk           |
| No manifest                      | DECISION-RELEVANT               | weak provenance                  |
| No snapshot hash                 | DECISION-RELEVANT               | dry-run/commit drift             |
| No post-tests                    | CRITICAL                        | migration correctness unverified |
| No external-reference audit      | EXPLANATORY / DECISION-RELEVANT | scope boundary unclear           |

---

# 115. CURRENT COMPLETION AUDIT

```yaml
completion:
  name_cleaning: COMPLETE
  underscore_normalization: COMPLETE
  version_suffix_assignment: COMPLETE
  file_extension_filtering: COMPLETE
  directory_ordering: COMPLETE
  dry_run_toggle: COMPLETE
  filesystem_rename: COMPLETE

  protected_subtree_pruning: INCOMPLETE
  semantic_validation: MISSING
  collision_detection: MISSING
  planning_manifest: MISSING
  reference_analysis: MISSING
  reference_rewrite: MISSING
  snapshot_freshness: MISSING
  transaction_model: MISSING
  rollback: MISSING
  post_migration_validation: MISSING
  provenance_ledger: MISSING

  overall:
    state: MUTATING_RENAME_ENGINE_V1
```

---

# 116. AMOS GOVERNED V2 ARCHITECTURE

```text
SOURCE TREE
↓
DISCOVERY
↓
PROTECTED-SUBTREE FILTER
↓
NORMALIZATION RULE ENGINE
↓
VERSION RESOLUTION
↓
IDENTITY AUDIT
↓
COLLISION DETECTOR
↓
REFERENCE GRAPH
↓
MIGRATION PLAN
↓
PLAN HASH
↓
DRY RUN
↓
APPROVAL
↓
SNAPSHOT REVALIDATION
↓
TRANSACTIONAL COMMIT
↓
REFERENCE REPAIR
↓
POST-VALIDATION
↓
MIGRATION RECEIPT
↓
ROLLBACK / CLOSE
```

---

# 117. RECOMMENDED ENGINE TYPES

```python
from dataclasses import dataclass
from pathlib import Path
from typing import Literal


@dataclass(frozen=True)
class RenameRule:
    rule_id: str
    pattern: str
    match_mode: Literal[
        "LITERAL",
        "TOKEN",
        "PREFIX",
        "SUFFIX",
        "REGEX",
    ]
    case_sensitive: bool = False
    replacement: str = ""


@dataclass(frozen=True)
class RenameOperation:
    operation_id: str
    object_type: Literal["file", "directory"]
    old_path: Path
    new_path: Path
    old_name: str
    new_name: str
    rules_applied: tuple[str, ...]
    version_assigned: bool


@dataclass(frozen=True)
class RenamePlan:
    plan_id: str
    target_root: Path
    operations: tuple[RenameOperation, ...]
    snapshot_hash: str
    plan_hash: str
```

---

# 118. RECOMMENDED SAFER DEFAULTS

```python
DRY_RUN = True

COLLISION_POLICY = "ABORT"

UNKNOWN_SEMANTIC_POLICY = "QUARANTINE"

FOLLOW_SYMLINKS = False

REQUIRE_MANIFEST = True

REQUIRE_POST_VALIDATION = True
```

---

# 119. RECOMMENDED SAFE `clean_base`

```python
def clean_base(
    name: str,
    rules: tuple[RenameRule, ...],
) -> tuple[str, tuple[str, ...]]:
    cleaned = name
    applied: list[str] = []

    for rule in rules:
        if rule.match_mode == "LITERAL":
            flags = 0 if rule.case_sensitive else re.IGNORECASE
            pattern = re.escape(rule.pattern)

        elif rule.match_mode == "TOKEN":
            flags = 0 if rule.case_sensitive else re.IGNORECASE
            pattern = rf"(?<![A-Za-z0-9]){re.escape(rule.pattern)}(?![A-Za-z0-9])"

        elif rule.match_mode == "PREFIX":
            flags = 0 if rule.case_sensitive else re.IGNORECASE
            pattern = rf"^{re.escape(rule.pattern)}"

        elif rule.match_mode == "SUFFIX":
            flags = 0 if rule.case_sensitive else re.IGNORECASE
            pattern = rf"{re.escape(rule.pattern)}$"

        else:
            flags = 0 if rule.case_sensitive else re.IGNORECASE
            pattern = rule.pattern

        updated = re.sub(
            pattern,
            rule.replacement,
            cleaned,
            flags=flags,
        )

        if updated != cleaned:
            applied.append(rule.rule_id)
            cleaned = updated

    cleaned = re.sub(r"__+", "_", cleaned)
    cleaned = cleaned.strip("_")

    if not cleaned:
        raise ValueError(
            f"Normalization produced empty name from {name!r}"
        )

    return cleaned, tuple(applied)
```

---

# 120. RECOMMENDED VERSION FUNCTION

```python
VERSION_RE = re.compile(
    r"_v(?P<major>\d+)$",
    flags=re.IGNORECASE,
)


def apply_version(name: str) -> tuple[str, bool]:
    if VERSION_RE.search(name):
        return name, False

    return f"{name}_v0", True
```

This preserves source compatibility while exposing whether the version was assigned.

---

# 121. PLAN-FIRST API

```python
def build_plan(
    root: Path,
    config: RenameEngineConfig,
) -> RenamePlan:
    ...
```

Then:

```python
def validate_plan(
    plan: RenamePlan,
) -> ValidationResult:
    ...
```

Then:

```python
def commit_plan(
    plan: RenamePlan,
) -> MigrationReceipt:
    ...
```

This separation is preferable to one `rename_item()` that decides and mutates immediately.

---

# 122. MIGRATION AUTHORITY

Because repository-wide rename is consequential:

```text
CapabilityToRename
!=
AuthorityToRename
```

The engine should receive explicit commit intent.

Conceptually:

```yaml
MigrationAuthority:
  migration_id:
  target_root:
  plan_hash:
  allowed_operations:
  issued_at:
  expires_at:
```

---

# 123. HUMAN REVIEW GATE

For large AMOS canon/repository migrations:

```text
DryRun
↓
Manifest Review
↓
Collision Review
↓
Semantic Identity Review
↓
Commit
```

Especially when removing:

```text
CANON
OMEGA
FULL
EXPANDED
```

because those may encode load-bearing distinctions.

---

# 124. 7-PART PERSISTENCE MAPPING

| 7-Part      | Rename Engine                           |
| ----------- | --------------------------------------- |
| Constraint  | root, extensions, skip rules, authority |
| Flow        | discovery → plan → commit               |
| Structure   | rules, mappings, manifests              |
| Enforcement | collision gates, validation             |
| Time        | snapshots, epochs, version lineage      |
| Adaptation  | migration rules, reference repair       |
| Termination | completed, aborted, rolled back         |

Class:

`AMOS_MODEL`

---

# 125. AGENT / TOOL CLASSIFICATION

Despite the topic tag `agents`, this source is primarily:

```text
DETERMINISTIC TOOL / MIGRATION ENGINE
```

not an autonomous reasoning agent.

Correct AMOS externalization:

```text
Rename procedure
→ CODE

Rename semantics
→ PROTOCOL

Migration state
→ PERSISTENT STATE

Commit permission
→ HARNESS POLICY

Semantic review
→ AGENT / HUMAN GOVERNANCE
```

Hard rule:

```text
Deterministic code
should not be inflated
into an "agent"
without an actual agent contract.
```

---

# 126. INTEGRATED-AGENT RELATION

If used inside an Integrated Agent architecture:

```text
Planning Agent
↓
Rename Plan Proposal
↓
Governance / Validator
↓
Universal Rename Engine
↓
Filesystem
↓
Migration Receipt
```

The engine itself should remain deterministic.

This separation is desirable:

```text
Stochastic cognition
→ proposes

Deterministic engine
→ executes approved mapping
```

---

# 127. CONTROL-PLANE BOUNDARY

The rename engine must not decide on its own that a semantic identifier is safe to delete.

Control plane responsibilities include:

```text
authority
semantic admission
canon identity protection
migration approval
rollback policy
```

The rename engine owns:

```text
deterministic transformation
collision detection
filesystem execution
receipt generation
```

---

# 128. RSCF MASTER NODE

```yaml
node_id: AMOS_UNIVERSAL_RENAME_ENGINE_V3

node_type: deterministic_migration_engine

domain: AMOS_REPOSITORY_GOVERNANCE

origin_architect: Trang Phan
steward: Trang Phan

document_version: 3.0.0
engine_version: 2.0.0
migration_contract_version: 1.0.0
core_target: AMOS_CORE_4.4

claim: >
  The AMOS Universal Rename Engine defines a deterministic namespace
  transformation that removes configured naming tokens, normalizes
  underscores, assigns baseline version suffixes, and renames selected
  filesystem objects within a bounded AMOS repository tree.

class: AMOS_MODEL

source_implementation:
  state: MUTATING_RENAME_ENGINE_V1

implemented:
  - bounded_target_root
  - ordered_cleanup_rules
  - underscore_normalization
  - integer_version_suffix_detection
  - v0_assignment
  - supported_extension_filter
  - deepest_first_directory_renaming
  - dry_run_toggle
  - real_filesystem_rename

critical_gaps:
  - semantic_identity_validation
  - protected_subtree_pruning
  - collision_preflight
  - reference_integrity
  - migration_manifest
  - snapshot_freshness
  - rollback
  - post_migration_verification

hard_invariants:
  - filename_is_not_artifact_identity
  - version_assignment_is_not_version_discovery
  - path_rename_is_not_symbol_rename
  - plan_precedes_mutation
  - collision_blocks_commit
  - unknown_semantic_impact_is_visible
  - canon_tokens_are_not_automatically_decorative
  - dry_run_is_not_commit
  - filesystem_success_is_not_repository_validity
  - migration_success_requires_post_validation

competing_interpretations:
  - removable tokens are purely decorative
  - removable tokens encode historical lineage
  - removable tokens encode subsystem identity
  - different tokens require different policies

falsifiers:
  - normalization creates semantic identity collisions
  - post-migration references fail
  - artifacts lose required lineage
  - migration cannot be safely rolled back
  - output differs across identical prepared snapshots

confidence_ceiling:
  source_name_transformation: high
  repository_semantic_safety: low_until_validated
  production_migration_readiness: not_established
```

---

# 129. CHANGELOG

## v3.0.0 — 2026-08-25

### MAJOR DOCUMENT / GOVERNANCE REVISION

* converted raw Python rename script into governed AMOS migration architecture;
* preserved the original source implementation;
* separated document, engine, migration-contract, and target-artifact versions;
* classified current engine as a real filesystem mutator rather than a stub;
* retained deterministic normalization semantics;
* identified integer-only version grammar;
* distinguished assigned `_v0` from historical artifact version;
* identified incomplete protected-directory semantics;
* added protected-subtree pruning invariant;
* added plan-before-mutation architecture;
* added deterministic rename manifest;
* added rename operation schema;
* added ordered rule registry;
* identified duplicate `vInfinity` / `vINFINITY` rule under `IGNORECASE`;
* added literal/regex/token rule modes;
* added empty-name detection;
* added semantic token-boundary handling;
* added collision detection;
* added many-to-one detection;
* added case-fold collision detection;
* added Unicode normalization considerations;
* added artifact identity vs filename separation;
* added path alias lineage;
* added reference graph;
* added Python/TypeScript/JSON/Markdown dependency validation;
* added registry/RSCF identity protection;
* added source snapshot hashing;
* added two-phase migration;
* added transaction state machine;
* added temporary namespace architecture;
* added rename graph/cycle detection;
* added rollback;
* added migration receipt;
* added filesystem/content integrity verification;
* added symlink/root-escape controls;
* added platform-dependent execution firewall;
* added Git-aware recovery guidance;
* added failure registry;
* added selective recovery;
* added 45-test validation progression;
* downgraded the source "safe" claim as overstated;
* retained "deterministic" only for scoped name transformation;
* flagged `CANON`, `OMEGA`, `FULL`, and `EXPANDED` as potentially semantic rather than universally decorative;
* classified the implementation primarily as deterministic code/tool rather than an autonomous agent;
* added governed Integrated-Agent composition.

## Source implementation — 2026-08-22

Implemented:

```text
TARGET_ROOT resolution
SKIP_DIRS declaration
REMOVE_PATTERNS
FILE_EXTS filter
clean_base()
apply_version()
rename_item()
deepest-first directory rename
supported-file rename
DRY_RUN / real-run mode
```

---

# 130. FINAL AMOS POSITION

The supplied code is a useful deterministic **rename primitive**, but it is not yet a complete repository migration system.

Its strongest valid statement is:

> **For a fixed name and fixed ordered pattern configuration, the engine deterministically produces a normalized name and can apply that rename to supported filesystem objects inside `_AMOS_UNIVERSE`.**

Its unsafe overstatement is:

> **That the resulting repository is automatically clean, safe, semantically equivalent, and fully migrated.**

The AMOS-correct evolution path is:

```text
RAW RENAME SCRIPT
↓
TYPED RULE SET
↓
SEMANTIC IDENTITY AUDIT
↓
IMMUTABLE MIGRATION PLAN
↓
COLLISION ANALYSIS
↓
REFERENCE GRAPH
↓
DRY RUN
↓
APPROVAL
↓
SNAPSHOT REVALIDATION
↓
TRANSACTIONAL COMMIT
↓
REFERENCE REPAIR
↓
POST-MIGRATION TESTING
↓
RECEIPT
↓
ROLLBACK / FINALIZE
```

The central invariant is:

> **A cleaner filename is not evidence of a cleaner architecture.**

The second invariant is:

> **Renaming is safe only when identity, dependency, provenance, and version lineage survive the transformation.**

The third invariant is:

> **`_v0` may be assigned as a migration baseline, but it must never be confused with evidence that the source artifact was historically version zero.**

The fourth invariant is:

> **A repository-wide rename is an effectful migration and must be planned, validated, reversible, and provenance-bound before it is trusted.**

---

**Related:** [[00-Home]] · [[06-Knowledge-Base-MOC]] · [[AMOS_AGENT_SCHEMA_FULL]] · [[AMOS_AGENT_TEMPLATES]] · [[AMOS_AGENT_ONBOARDING_GUIDE]] · [[EnvironmentScan_Agent]] · [[Executor_Agent]] · [[system_scan_agent]] · [[automation_profiles]]

```
```
