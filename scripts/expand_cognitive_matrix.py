#!/usr/bin/env python3
"""
expand_cognitive_matrix.py

Finds all placeholder files (status: "PLACEHOLDER" or status: PLACEHOLDER) in
25_COGNITIVE_MATRIX recursively and expands them with substantive AMOS content.

Each expanded file includes:
  - Updated frontmatter (status: SUBSTANTIVE_SPECIFICATION, version: 1.0.0,
    updated: 2026-09-04, placeholder_expanded tag)
  - Section 0: Status with standard AMOS disclaimer block
  - Section 1: Purpose
  - Section 2: Formal Definition with mathematical notation
  - Section 3: Application / Cross-references
  - Section 4: Gaps
  - Section 5: Ingestion Rule
  - RSCF-NODE footer

Origin architect: Trang Phan
"""

import os
import re
import sys
from pathlib import Path

VAULT_ROOT = Path("/Users/mac/Documents/AMOS_OS/25_COGNITIVE_MATRIX")

# ---------------------------------------------------------------------------
# Domain-specific content generators
# ---------------------------------------------------------------------------

def _disclaimer_block():
    return """```text
PLACEHOLDER != IMPLEMENTED

ADDRESSABLE != VALIDATED

DOCUMENTED != ENFORCED

MODEL != OBSERVATION

SOURCE_CLAIM != VERIFIED

CANON_CANDIDATE != CANONICAL

CANONICAL != EMPIRICAL_TRUTH

CAPABILITY != AUTHORITY

AUTHORIZATION != COMMIT

PROPOSAL != COMMIT

IMPLEMENTED != VALIDATED

LOGGED != APPROVED

UNKNOWN/GAP != PASS
```"""

def _ingestion_rule():
    return """```yaml
AMOS_CANON_INGESTION_RULE:
  existing_folder:
    preserve: true
  existing_file:
    preserve: true
    overwrite: false
  new_framework:
    action: ADD_FILE_TO_EXISTING_FOLDER
  master_source:
    action: NORMALIZE_TO_RSCF_FILE
  framework_existing_in_multiple_sources:
    action:
      - CREATE_ONE_CANONICAL_NODE
      - LINK_ALL_SOURCE_PROVENANCE
      - DO_NOT_CREATE_DUPLICATE_CANON
  historical_source:
    action:
      - LINK_TO_CANON
      - RECORD_LINEAGE
      - PRESERVE_HERITAGE
  external_research:
    action:
      - KEEP_OUT_OF_NATIVE_CANON
      - LINK_AS_EVIDENCE
  duplicate_filename:
    action:
      - COMPARE_CONTENT_AND_LINEAGE
      - DO_NOT_OVERWRITE
  uncertainty:
    action:
      - MARK_GAP_OR_COMPETING
      - NEVER_INVENT_CANON
```"""

# ---------------------------------------------------------------------------
# Per-file substantive content
# ---------------------------------------------------------------------------

CONTENT_MAP = {

    # =======================================================================
    # 12_GENERATORS_CONTRACT.md
    # =======================================================================
    "12_GENERATORS_CONTRACT.md": {
        "title": "12 GENERATORS CONTRACT",
        "node_type": "contract",
        "artifact_kind": "CONTRACT",
        "tags_extra": ["contract", "generators", "canon_placeholder", "rscf", "placeholder_expanded"],
        "segment": "25_COGNITIVE_MATRIX/12_GENERATORS",
        "path": "25_COGNITIVE_MATRIX/12_GENERATORS/12_GENERATORS_CONTRACT.md",
        "artifact_id": "amos_25_cognitive_matrix_12_generators_12_generators_contract",
        "purpose": """`12_GENERATORS_CONTRACT.md` defines the governing contract for the **12_GENERATORS** subsystem within the **25_COGNITIVE_MATRIX** plane.

The Cognitive Matrix plane governs cross-plane routing tables between AMOS planes: Canon ↔ Control Plane, Canon ↔ Runtime, UBI ↔ Cognition, UBI ↔ Emotion. Within this plane, the 12_GENERATORS segment governs the lifecycle, admission, validation, provenance, versioning, and supersession of **generator artifacts** — components that produce derived artifacts from canon sources under governed constraints.

A generator is not merely a function. It is a **governed artifact-producing component** whose outputs must pass through promotion gates before becoming canonical. The contract establishes:

```text
CANON_SOURCE
    ↓
GENERATOR (governed)
    ↓
CANDIDATE ARTIFACT
    ↓
VALIDATION
    ↓
PROMOTION GATE
    ↓
ADMITTED ARTIFACT
```

The contract binds generators to:
1. **Provenance preservation** — every generated artifact must carry recoverable source ancestry.
2. **Epistemic class declaration** — generated outputs are `DERIVED` or `MODEL`, never silently `OBSERVATION` or `CANONICAL`.
3. **Confidence ceiling** — generated artifact confidence cannot exceed the weakest load-bearing source.
4. **Fail-closed on UNKNOWN/GAP** — generators may not invent canon to fill gaps.
5. **Receipts for consequential outputs** — every promoted generated artifact must carry a validation receipt.
6. **Rollback basin** — generators must support rollback of their outputs.
7. **No self-promotion** — a generator's own output cannot automatically cross promotion gates (`I-PROM-022`).""",

        "formal_def": """A generator contract is modeled as:

$$\\boxed{
GC = \\langle G_{id}, S_{canon}, T_{transform}, V_{schema}, P_{provenance}, E_{epistemic}, C_{ceiling}, R_{receipts}, B_{rollback} \\rangle
}$$

where:
- $G_{id}$ = generator identity (registered, versioned, hash-bound)
- $S_{canon}$ = canon source set (admitted sources only)
- $T_{transform}$ = transformation specification (deterministic or stochastic, declared)
- $V_{schema}$ = output schema validator
- $P_{provenance}$ = provenance binding (source ancestry preserved)
- $E_{epistemic}$ = epistemic class of output (`DERIVED` | `MODEL`)
- $C_{ceiling}$ = confidence ceiling function
- $R_{receipts}$ = receipt emission for promoted outputs
- $B_{rollback}$ = rollback basin for output invalidation

The generator admission predicate:

$$\\text{Admissible}(G) \\iff \\text{Registered}(G_{id}) \\land \\text{CanonSourcesValid}(S_{canon}) \\land \\text{SchemaDeclared}(V_{schema}) \\land \\text{ProvenanceBound}(P_{provenance})$$

The output promotion predicate:

$$\\text{Promotable}(O) \\iff \\text{Validated}(O) \\land \\text{ProvenanceRecoverable}(O) \\land \\text{EpistemicClassDeclared}(O) \\land \\text{ConfidenceBounded}(O) \\land \\neg \\text{SelfPromoted}(O)$$

The confidence ceiling law:

$$C(O) \\le \\min_{s \\in \\text{LoadBearing}(O)} C(s)$$

where $C(s)$ is the confidence of source $s$ and the minimum is taken over all load-bearing sources.

The rollback invariant:

$$\\text{Rollback}(O_k) \\circ \\text{Generate}(O_k) = \\mathbb{I} \\quad \\text{(reversible generation)}$$

for generators that declare reversibility. Irreversible generators require explicit irreversibility governance.""",

        "application": """### Cross-plane bindings

- **Canon ↔ Generator** — generators consume admitted canon sources: [[01_CANON/01_CORE_LAWS/LAW_HIERARCHY|AMOS Core Laws]]
- **Control Plane ↔ Generator** — generator activation requires control-plane authority: [[03_CONTROL_PLANE/03_CONTROL_PLANE_README|CONTROL_PLANE_README]]
- **Validation ↔ Generator** — generated artifacts pass through [[25_COGNITIVE_MATRIX/11_VALIDATION/PROMOTION_GATES|PROMOTION_GATES]]
- **Routing ↔ Generator** — generator routing governed by [[25_COGNITIVE_MATRIX/10_ROUTING/ROUTING_POLICY|ROUTING_POLICY]]
- **Kernel interaction** — [[02_KERNEL/02_KERNEL_README|KERNEL_README]]
- **Observability** — [[17_OBSERVABILITY/17_OBSERVABILITY_README|OBSERVABILITY_README]] (observer, never authority)
- **Operations** — [[20_OPERATIONS/20_OPERATIONS_README|OPERATIONS_README]]

### Related artifacts

- [[25_COGNITIVE_MATRIX/12_GENERATORS/GENERATOR_ADMISSION|GENERATOR_ADMISSION]]
- [[25_COGNITIVE_MATRIX/12_GENERATORS/GENERATORS_AUDIT|GENERATORS_AUDIT]]
- [[25_COGNITIVE_MATRIX/12_GENERATORS/GENERATOR_VALIDATION|GENERATOR_VALIDATION]]
- [[25_COGNITIVE_MATRIX/12_GENERATORS/GENERATOR_PROMOTION|GENERATOR_PROMOTION]]
- [[25_COGNITIVE_MATRIX/12_GENERATORS/GENERATOR_REGISTRY|GENERATOR_REGISTRY]]
- [[25_COGNITIVE_MATRIX/12_GENERATORS/GENERATORS_PROVENANCE|GENERATORS_PROVENANCE]]
- [[25_COGNITIVE_MATRIX/12_GENERATORS/GENERATOR_SUPERSESSION|GENERATOR_SUPERSESSION]]""",

        "gaps": """1. **Executable binding NOT_ESTABLISHED** — the generator contract is a structural specification; no runtime generator framework has been independently verified as implementing this contract.
2. **Canonical status UNKNOWN/GAP** — the contract is an AMOS_MODEL, not admitted canon.
3. **Generator registry implementation** — the registry schema is specified but no executed registry has been validated.
4. **Stochastic generator governance** — the contract distinguishes deterministic and stochastic transforms but does not fully specify governance for stochastic outputs (seed binding, reproducibility, distribution validation).
5. **Multi-generator composition** — composition of multiple generators (pipeline, fan-out, fan-in) is not fully specified.
6. **Generator supersession** — the supersession protocol for replacing a generator is referenced but not fully operationalized in this artifact.
7. **Cross-plane generator routing** — routing between generators across planes (Canon → Control Plane → Runtime) requires integration with ROUTING_POLICY and BINDING_RULES.
8. **Validation receipt specificity** — validation receipts for generated artifacts require artifact-specific test harnesses not yet established.""",
    },

    # =======================================================================
    # 12_GENERATORS_VERSIONING.md
    # =======================================================================
    "12_GENERATORS_VERSIONING.md": {
        "title": "12 GENERATORS VERSIONING",
        "node_type": "artifact",
        "artifact_kind": "ARTIFACT",
        "tags_extra": ["artifact", "versioning", "generators", "canon_placeholder", "rscf", "placeholder_expanded"],
        "segment": "25_COGNITIVE_MATRIX/12_GENERATORS",
        "path": "25_COGNITIVE_MATRIX/12_GENERATORS/12_GENERATORS_VERSIONING.md",
        "artifact_id": "amos_25_cognitive_matrix_12_generators_12_generators_versioning",
        "purpose": """`12_GENERATORS_VERSIONING.md` defines the versioning contract for generator artifacts within the **12_GENERATORS** segment of the **25_COGNITIVE_MATRIX** plane.

Generator versioning governs how generator identities, outputs, schemas, and contracts evolve over time while preserving provenance, reproducibility, and rollback capability.

The versioning contract establishes:

```text
GENERATOR_ID + VERSION + HASH
    ↓
OUTPUT_SCHEMA_VERSION
    ↓
CONTRACT_VERSION
    ↓
SOURCE_CANON_VERSION
    ↓
PROVENANCE_EPOCH
```

Key principles:
1. **Semantic versioning** — generator versions follow `MAJOR.MINOR.PATCH` where MAJOR indicates contract-breaking changes, MINOR indicates additive changes, PATCH indicates fixes.
2. **Hash binding** — every generator version is bound to a content hash for reproducibility.
3. **Output schema versioning** — generator output schemas are independently versioned and backward-compatible where possible.
4. **Source canon versioning** — generators must declare which canon source versions they consumed.
5. **Provenance epoch** — every generated artifact carries the provenance epoch under which it was produced.
6. **Supersession lineage** — when a generator version is superseded, the supersession chain must be explicit and recoverable.
7. **No silent version drift** — stale generator versions must not silently produce artifacts as if current.""",

        "formal_def": """A generator version is modeled as:

$$\\boxed{
GV = \\langle G_{id}, V_{sem}, H_{content}, S_{schema}, C_{canon}, E_{epoch}, L_{lineage} \\rangle
}$$

where:
- $G_{id}$ = generator identity (stable across versions)
- $V_{sem}$ = semantic version tuple $(major, minor, patch)$
- $H_{content}$ = content hash (BLAKE3 or SHA-256)
- $S_{schema}$ = output schema version
- $C_{canon}$ = canon source version set
- $E_{epoch}$ = provenance epoch
- $L_{lineage}$ = supersession lineage (predecessor → successor chain)

The version compatibility predicate:

$$\\text{Compatible}(GV_a, GV_b) \\iff V_{sem}(a).major = V_{sem}(b).major \\land S_{schema}(a) \\le S_{schema}(b)$$

The freshness predicate:

$$\\text{Fresh}(GV, t) \\iff \\neg \\exists GV' : \\text{Supersedes}(GV', GV) \\land E_{epoch}(GV') \\le t$$

The supersession law:

$$\\text{Supersedes}(GV_{new}, GV_{old}) \\implies \\text{ExplicitLineage}(GV_{new}, GV_{old}) \\land \\text{ProvenancePreserved}(GV_{new})$$

The reproducibility invariant:

$$\\forall t, GV : \\text{Generate}(GV, S_{canon}(GV), t) = \\text{Generate}(GV, S_{canon}(GV), t')$$

for deterministic generators with identical inputs (seed-bound for stochastic generators).

The version drift detection:

$$\\text{Drifted}(GV) \\iff \\exists GV' : \\text{Registered}(GV') \\land G_{id}(GV') = G_{id}(GV) \\land V_{sem}(GV') > V_{sem}(GV) \\land \\neg \\text{Superseded}(GV, GV')$$

Drifted generators must be flagged and their outputs quarantined until lineage is resolved.""",

        "application": """### Cross-plane bindings

- **Canon ↔ Versioning** — canon source versions must be declared: [[01_CANON/01_CORE_LAWS/LAW_HIERARCHY|AMOS Core Laws]]
- **Control Plane ↔ Versioning** — version activation requires control-plane epoch: [[03_CONTROL_PLANE/03_CONTROL_PLANE_README|CONTROL_PLANE_README]]
- **Validation ↔ Versioning** — versioned artifacts pass through [[25_COGNITIVE_MATRIX/11_VALIDATION/PROMOTION_GATES|PROMOTION_GATES]]
- **Routing ↔ Versioning** — version-aware routing governed by [[25_COGNITIVE_MATRIX/10_ROUTING/ROUTING_POLICY|ROUTING_POLICY]]
- **Kernel interaction** — [[02_KERNEL/02_KERNEL_README|KERNEL_README]]
- **Observability** — [[17_OBSERVABILITY/17_OBSERVABILITY_README|OBSERVABILITY_README]]
- **Operations** — [[20_OPERATIONS/20_OPERATIONS_README|OPERATIONS_README]]

### Related artifacts

- [[25_COGNITIVE_MATRIX/12_GENERATORS/GENERATOR_VERSIONING|GENERATOR_VERSIONING]]
- [[25_COGNITIVE_MATRIX/12_GENERATORS/GENERATORS_VERSIONING|GENERATORS_VERSIONING]]
- [[25_COGNITIVE_MATRIX/12_GENERATORS/GENERATOR_REGISTRY|GENERATOR_REGISTRY]]
- [[25_COGNITIVE_MATRIX/12_GENERATORS/GENERATOR_SUPERSESSION|GENERATOR_SUPERSESSION]]
- [[25_COGNITIVE_MATRIX/12_GENERATORS/GENERATORS_CHANGE_LOG|GENERATORS_CHANGE_LOG]]
- [[25_COGNITIVE_MATRIX/12_GENERATORS/GENERATORS_PROVENANCE|GENERATORS_PROVENANCE]]""",

        "gaps": """1. **Executable binding NOT_ESTABLISHED** — the versioning contract is a structural specification; no runtime versioning system has been independently verified.
2. **Canonical status UNKNOWN/GAP** — the versioning model is an AMOS_MODEL, not admitted canon.
3. **Schema migration** — backward-compatible schema evolution is specified but migration protocols (automatic upgrade, deprecation windows) are not fully operationalized.
4. **Stochastic seed governance** — seed binding for stochastic generators is referenced but the seed provenance, storage, and verification protocol is not fully specified.
5. **Multi-generator version composition** — when generators compose (pipeline), version compatibility across the pipeline is not fully specified.
6. **Version conflict resolution** — when two generator versions produce conflicting outputs, the resolution protocol references PROMOTION_GATES but is not independently operationalized here.
7. **Deprecation lifecycle** — the deprecation → retirement → archival lifecycle for old generator versions is not fully specified.
8. **Cross-plane version propagation** — when a canon source version changes, dependent generator version invalidation propagation is not fully specified.""",
    },

    # =======================================================================
    # COGNITIVE_MATRIX_GENERATED_ARTIFACT_NORMALIZATION_POLICY.md
    # =======================================================================
    "COGNITIVE_MATRIX_GENERATED_ARTIFACT_NORMALIZATION_POLICY.md": {
        "title": "COGNITIVE MATRIX GENERATED ARTIFACT NORMALIZATION POLICY",
        "node_type": "policy",
        "artifact_kind": "POLICY",
        "tags_extra": ["policy", "normalization", "generated-artifacts", "canon_placeholder", "rscf", "placeholder_expanded"],
        "segment": "25_COGNITIVE_MATRIX",
        "path": "25_COGNITIVE_MATRIX/COGNITIVE_MATRIX_GENERATED_ARTIFACT_NORMALIZATION_POLICY.md",
        "artifact_id": "amos_25_cognitive_matrix_cognitive_matrix_generated_artifact_normalization_policy",
        "purpose": """`COGNITIVE_MATRIX_GENERATED_ARTIFACT_NORMALIZATION_POLICY.md` defines the normalization policy for artifacts generated within or routed through the **25_COGNITIVE_MATRIX** plane.

The Cognitive Matrix plane governs cross-plane routing tables between AMOS planes. Generated artifacts — those produced by generators, templates, or automated processes — must be normalized to a consistent RSCF structure before they can be admitted, routed, validated, or promoted.

Normalization is not merely formatting. It is the **governed transformation of a generated artifact into a structurally valid, provenance-preserving, epistemically classified RSCF-compatible artifact**.

The normalization pipeline:

```text
RAW GENERATED ARTIFACT
    ↓
STRUCTURAL NORMALIZATION (frontmatter, sections, RSCF node)
    ↓
PROVENANCE NORMALIZATION (source ancestry binding)
    ↓
EPISTEMIC NORMALIZATION (claim class declaration)
    ↓
SCOPE/REGIME NORMALIZATION (applicability binding)
    ↓
FRESHNESS NORMALIZATION (epoch binding)
    ↓
NORMALIZED ARTIFACT (ready for validation/promotion)
```

Key policy principles:
1. **Normalization preserves content** — normalization must not alter the semantic content of the generated artifact; it only structures it.
2. **Normalization preserves provenance** — source ancestry must remain recoverable through normalization.
3. **Normalization declares epistemic class** — normalized artifacts must declare `DERIVED` or `MODEL`, not silently inherit `CANONICAL` or `OBSERVATION`.
4. **Normalization is idempotent** — normalizing an already-normalized artifact produces the same artifact.
5. **Normalization fails closed** — if normalization cannot preserve a required property, the artifact is quarantined, not silently admitted.
6. **Normalization is versioned** — the normalization policy itself is versioned and artifacts carry the normalization policy version.""",

        "formal_def": """The normalization function is modeled as:

$$\\boxed{
N(A_{raw}) = A_{normalized}
}$$

subject to the idempotency law:

$$N(N(A)) = N(A) \\quad \\text{(idempotent)}$$

The normalization predicate:

$$\\text{Normalizable}(A) \\iff \\text{Parseable}(A) \\land \\text{ProvenanceRecoverable}(A) \\land \\text{EpistemicClassInferrable}(A) \\land \\text{ScopeBoundable}(A)$$

The normalization contract:

$$\\boxed{
N = \\langle N_{struct}, N_{prov}, N_{epist}, N_{scope}, N_{fresh}, N_{rscf} \\rangle
}$$

where:
- $N_{struct}$ = structural normalization (frontmatter, sections, formatting)
- $N_{prov}$ = provenance normalization (source ancestry binding)
- $N_{epist}$ = epistemic normalization (claim class declaration)
- $N_{scope}$ = scope/regime normalization (applicability binding)
- $N_{fresh}$ = freshness normalization (epoch binding)
- $N_{rscf}$ = RSCF node generation (node_id, node_type, relations)

The content preservation invariant:

$$\\text{Semantics}(N(A)) = \\text{Semantics}(A) \\quad \\text{(content-preserving)}$$

The provenance preservation invariant:

$$\\text{Provenance}(N(A)) \\supseteq \\text{Provenance}(A) \\quad \\text{(provenance-monotonic)}$$

The epistemic non-promotion invariant:

$$\\text{EpistemicClass}(N(A)) \\le \\text{EpistemicClass}(A) \\quad \\text{(never elevated)}$$

where $\\le$ is the epistemic trust ordering: `UNKNOWN/GAP < SOURCE_CLAIM < DERIVED < MODEL < OBSERVATION < CANONICAL`.

The quarantine rule:

$$\\neg \\text{Normalizable}(A) \\implies \\text{Quarantine}(A) \\land \\neg \\text{Admit}(A)$$

The policy version binding:

$$\\forall A : \\text{NormalizedBy}(A, N_v) \\implies \\text{PolicyVersion}(A) = v$$

where $v$ is the normalization policy version under which $A$ was normalized.""",

        "application": """### Cross-plane bindings

- **Canon ↔ Normalization** — normalized artifacts must respect canon structure: [[01_CANON/01_CORE_LAWS/LAW_HIERARCHY|AMOS Core Laws]]
- **Control Plane ↔ Normalization** — normalization policy activation requires control-plane epoch: [[03_CONTROL_PLANE/03_CONTROL_PLANE_README|CONTROL_PLANE_README]]
- **Validation ↔ Normalization** — normalized artifacts pass through [[25_COGNITIVE_MATRIX/11_VALIDATION/PROMOTION_GATES|PROMOTION_GATES]]
- **Routing ↔ Normalization** — only normalized artifacts are routable: [[25_COGNITIVE_MATRIX/10_ROUTING/ROUTING_POLICY|ROUTING_POLICY]]
- **Generators ↔ Normalization** — generator outputs require normalization before promotion: [[25_COGNITIVE_MATRIX/12_GENERATORS/12_GENERATORS_CONTRACT|12_GENERATORS_CONTRACT]]
- **Kernel interaction** — [[02_KERNEL/02_KERNEL_README|KERNEL_README]]
- **Observability** — [[17_OBSERVABILITY/17_OBSERVABILITY_README|OBSERVABILITY_README]]
- **Operations** — [[20_OPERATIONS/20_OPERATIONS_README|OPERATIONS_README]]

### Related artifacts

- [[25_COGNITIVE_MATRIX/12_GENERATORS/GENERATOR_OUTPUT|GENERATOR_OUTPUT]]
- [[25_COGNITIVE_MATRIX/12_GENERATORS/GENERATOR_TEMPLATES|GENERATOR_TEMPLATES]]
- [[25_COGNITIVE_MATRIX/12_GENERATORS/GENERATOR_REGISTRY|GENERATOR_REGISTRY]]
- [[25_COGNITIVE_MATRIX/11_VALIDATION/PROMOTION_GATES|PROMOTION_GATES]]
- [[25_COGNITIVE_MATRIX/10_ROUTING/ROUTING_POLICY|ROUTING_POLICY]]
- [[25_COGNITIVE_MATRIX/10_ROUTING/BINDING_RULES|BINDING_RULES]]""",

        "gaps": """1. **Executable binding NOT_ESTABLISHED** — the normalization policy is a structural specification; no runtime normalizer has been independently verified.
2. **Canonical status UNKNOWN/GAP** — the policy is an AMOS_MODEL, not admitted canon.
3. **Semantic preservation verification** — the content preservation invariant is stated but no automated semantic equivalence checker has been validated.
4. **Cross-format normalization** — normalization from non-markdown formats (JSON, YAML, code) into RSCF markdown is not fully specified.
5. **Policy version migration** — when the normalization policy itself versions, re-normalization of existing artifacts is not fully specified.
6. **Partial normalization** — artifacts that are partially normalizable (some properties preservable, others not) require a partial-admission protocol not fully specified.
7. **Normalization audit trail** — the normalization process should emit receipts but the receipt schema is not independently specified in this artifact.
8. **Cross-plane normalization propagation** — when an artifact is normalized in the Cognitive Matrix plane, propagation to other planes (Canon, Runtime) is not fully specified.""",
    },
}


# ---------------------------------------------------------------------------
# Frontmatter and content generation
# ---------------------------------------------------------------------------

def build_frontmatter(info):
    tags_yaml = "\n".join(f"  - {t}" for t in info["tags_extra"])
    return f"""---
title: "{info['title']}"
artifact: "{Path(info['path']).name}"
artifact_id: "{info['artifact_id']}"
origin_architect: "Trang Phan"
steward: "Trang Phan"
system: "AMOS OS"
plane: "25_COGNITIVE_MATRIX"
segment: "{info['segment']}"
artifact_kind: "{info['artifact_kind']}"
path: "{info['path']}"

tags:
{tags_yaml}

version: "1.0.0"
updated: "2026-09-04"

status: "SUBSTANTIVE_SPECIFICATION"
epistemic_class: "AMOS_MODEL"
canonical_status: "UNKNOWN/GAP"
implementation_status: "NOT_ESTABLISHED"
validation_status: "NOT_ESTABLISHED"
executable_binding: "NOT_ESTABLISHED"
ingestion_action: "ADD_ONLY"
---"""


def build_body(info):
    title = info["title"]
    return f"""# {title}

## 0. Status

`{Path(info["path"]).name}` is a **substantive specification artifact** for the **Cognitive Matrix** plane segment at `{info["segment"]}`.

It has been expanded from an ADD-ONLY placeholder into a substantive AMOS_MODEL specification. It is NOT validated canon, NOT independently verified, and NOT enforced at runtime.

The governing boundaries are:

{_disclaimer_block()}

Origin architect / steward:

**Trang Phan**

System: **AMOS OS**

AMOS_CORE target: **v4.4**

---

## 1. Purpose

{info["purpose"]}

---

## 2. Formal Definition

{info["formal_def"]}

---

## 3. Application / Cross-references

{info["application"]}

---

## 4. Gaps

{info["gaps"]}

---

## 5. Ingestion Rule

{_ingestion_rule()}

---

[[00_ROOT_MOC|AMOS MOC]]

---

**Related:** [[00_ROOT/00_HOME]] · [[AMOS_RSCF_NODES]]

---

RSCF-NODE

node_id: {info["artifact_id"]}

node_type: {info["node_type"]}

path: {info["path"]}

claim_class: AMOS_MODEL

rscf_state: substantive_specification

canonical_status: UNKNOWN/GAP

RSCF-RELATIONS:

  - INDEXED_BY: [[00_ROOT/00_HOME]]

  - INDEXED_BY: [[AMOS_RSCF_NODES]]

  - GOVERNED_BY: [[01_CANON/01_CORE_LAWS/LAW_HIERARCHY]]
"""


def build_full_content(info):
    return build_frontmatter(info) + "\n\n" + build_body(info)


# ---------------------------------------------------------------------------
# Main logic
# ---------------------------------------------------------------------------

def is_placeholder(filepath):
    """Check if a file has status: PLACEHOLDER (quoted or unquoted)."""
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()
    except Exception:
        return False

    # Match status: "PLACEHOLDER" or status: PLACEHOLDER (exact, not PLACEHOLDER_EXPANDED)
    pattern = r'^status:\s*"?PLACEHOLDER"?\s*$'
    for line in content.splitlines():
        if re.match(pattern, line.strip()):
            return True
    return False


def main():
    if not VAULT_ROOT.exists():
        print(f"ERROR: Vault root not found: {VAULT_ROOT}", file=sys.stderr)
        sys.exit(1)

    # Find all placeholder files
    placeholder_files = []
    for md_file in VAULT_ROOT.rglob("*.md"):
        if is_placeholder(md_file):
            placeholder_files.append(md_file)

    print(f"Found {len(placeholder_files)} placeholder file(s) to expand.")

    expanded = 0
    skipped = 0

    for filepath in sorted(placeholder_files):
        filename = filepath.name
        info = CONTENT_MAP.get(filename)

        if info is None:
            print(f"  SKIP (no content map): {filepath}")
            skipped += 1
            continue

        # Generate expanded content
        expanded_content = build_full_content(info)

        # Write back
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(expanded_content)

        print(f"  EXPANDED: {filepath}")
        expanded += 1

    print(f"\nDone: {expanded} file(s) expanded, {skipped} skipped.")


if __name__ == "__main__":
    main()
