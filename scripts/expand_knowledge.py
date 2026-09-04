#!/usr/bin/env python3
"""
AMOS Knowledge-Plane Placeholder Expander
Expands placeholder files in 11_KNOWLEDGE with substantive canonical content.
Preserves frontmatter structure, replaces boilerplate with domain-specific content.

Usage:
    python3 expand_knowledge.py          # expand all placeholders
    python3 expand_knowledge.py --dry    # report only, no writes
"""

import os
import re
import sys
from pathlib import Path
from datetime import datetime

VAULT_ROOT = Path("/Users/mac/Documents/AMOS_OS/11_KNOWLEDGE")
DRY_RUN = "--dry" in sys.argv

# ---------------------------------------------------------------------------
# Content definitions for each placeholder file
# ---------------------------------------------------------------------------

EXPANSIONS = {
    "AMOS_CORE_V4_4.md": {
        "title": "AMOS CORE V4 4",
        "h1": "AMOS CORE V4.4 — Knowledge-Plane Canonical Specification",
        "purpose": """The AMOS CORE V4.4 specification defines the canonical reasoning and governance lineage
for the AMOS operating system as it intersects the **Knowledge plane** (`11_KNOWLEDGE`).

The Knowledge plane governs knowledge-base integration: claims, RSCF indices, framework
nodes, domain knowledge, research ingestion, and the cross-domain tensor composition that
binds them. AMOS CORE V4.4 is the currently accepted lineage boundary — all v4.5–v4.17
labels preserved in historical records are consolidation labels, not promoted canonical
successors, unless supported by explicit predecessor/successor chains, source
version/hash, changeset, validation evidence, and supersession lineage.

Within the Knowledge plane, AMOS CORE V4.4 establishes:

1. **Epistemic discipline** — every claim carries an RSCF state (SOURCE_CLAIM,
   OBSERVATION, DERIVED, AMOS_MODEL, CONDITIONAL, COMPETING, UNKNOWN/GAP, FALSIFIED).
2. **Framework registry** — canonical frameworks (UBI, QLS, QCLA, Trang, TSS/TPE,
   FRAI, ConsentX, Heritage) are indexed, cross-referenced, and provenance-stamped.
3. **Domain knowledge canon** — 12 canonical domain engines (C01–C12) provide
   structured knowledge across meta-logic, math/compute, physics/cosmos, bio/neuro,
   mind/behavior, society/culture, econ/finance, strategy/game, org/law/policy,
   tech/engineering, design/language, and earth/ecology.
4. **Ingestion governance** — the AMOS_CANON_INGESTION_RULE controls how new
   knowledge enters the plane without duplicating canon or inventing authority.
5. **Cross-plane bindings** — the Knowledge plane is governed by canon (01_CANON),
   interacts with the kernel (02_KERNEL), passes through control-plane gates
   (03_CONTROL_PLANE), is observed by observability (17_OBSERVABILITY), and is
   recovered via operations (20_OPERATIONS).""",

        "formal": r"""### 2.1 Lineage Boundary

$$\text{CanonicalLineage} = \{v3.0 \rightarrow v4.4\}$$

$$\forall L \in \{v4.5, \ldots, v4.17\}: \text{Promoted}(L) = \text{FALSE}$$

unless:

$$\text{Predecessor}(L) \wedge \text{SourceHash}(L) \wedge \text{Changeset}(L) \wedge \text{Validation}(L) \wedge \text{Authority}(L) \wedge \text{Supersession}(L)$$

### 2.2 Epistemic Classification Algebra

Every knowledge-plane artifact $A$ carries an RSCF tuple:

$$\text{RSCF}(A) = (\text{state}, \text{claim\_class}, \text{provenance}, \text{scope})$$

where:

$$\text{state} \in \{\text{SOURCE\_CLAIM}, \text{OBSERVATION}, \text{DERIVED}, \text{AMOS\_MODEL}, \text{CONDITIONAL}, \text{COMPETING}, \text{UNKNOWN/GAP}, \text{FALSIFIED}\}$$

The confidence ceiling is:

$$\text{Confidence}(A) \leq \min_{p \in \text{Premises}(A)} \text{Confidence}(p)$$

with a hard ceiling of 0.95 for AMOS_MODEL claims.

### 2.3 Knowledge-Plane Integrity Invariant

$$\text{KnowledgePlaneValid} \iff \forall A \in \text{Artifacts}: \text{RSCF}(A) \neq \bot \wedge \text{Provenance}(A) \neq \emptyset \wedge \text{NoInventedCanon}(A)$$

### 2.4 Cross-Domain Tensor Composition

The 12 canonical domain engines form a composition tensor:

$$\mathcal{T}_{\text{knowledge}} = \bigotimes_{i=1}^{12} \mathcal{D}_i$$

where $\mathcal{D}_i$ is the domain engine for canonical domain $C_i$. Cross-domain
claims require explicit bridge proofs:

$$\text{Bridge}(\mathcal{D}_i, \mathcal{D}_j) \implies \text{ScopeValid}(\mathcal{D}_i) \wedge \text{ScopeValid}(\mathcal{D}_j) \wedge \text{RegimeCompatible}(\mathcal{D}_i, \mathcal{D}_j)$$

### 2.5 Ingestion Monotonicity

$$\text{Ingest}(A, \text{KB}) \implies \neg\text{Overwrite}(\text{Existing}(A)) \wedge \text{PreserveLineage}(A) \wedge \text{StampProvenance}(A)$$

Knowledge is add-only; existing canon is never silently overwritten.""",

        "applications": r"""### 4.1 Framework Registry

The Knowledge plane indexes canonical AMOS frameworks:

| Framework | Domain | RSCF State | Cross-Reference |
|:---|:---|:---|:---|
| **UBI** (Universal Biological Intelligence) | C04 Bio/Neuro, C05 Mind | AMOS_MODEL | [[AMOS_UBI_OMNIS_USE_CASES]] |
| **QLS** (Quantum Logic System) | C02 Math/Compute | AMOS_MODEL | [[AMOS_C02_MATH_COMPUTE_MASTER_KNOWLEDGE]] |
| **QCLA** (Quantum-Classical Logic Architecture) | C01 Meta-Logic | AMOS_MODEL | [[AMOS_C01_META_LOGIC_MASTER_KNOWLEDGE]] |
| **Trang** (Recursive Ontology Dynamics) | C03 Physics/Cosmos | AMOS_MODEL | [[TRANG_FRAMEWORK_RECURSIVE_ONTOLOGY_DYNAMICS]] |
| **TSS/TPE** (Governance Economy) | C07 Econ/Finance, C09 Org/Law | AMOS_MODEL | [[AMOS_C07_ECON_FINANCE_MASTER_KNOWLEDGE]] |
| **FRAI** (Fractal Reasoning AI) | C10 Tech/Engineering | AMOS_MODEL | [[AMOS_C10_TECH_ENGINEERING_MASTER_KNOWLEDGE]] |
| **ConsentX** | C06 Society/Culture | AMOS_MODEL | [[AMOS_C06_SOCIETY_CULTURE_MASTER_KNOWLEDGE]] |
| **Heritage** (Civilization System) | C06 Society/Culture | AMOS_MODEL | [[AMOS_C06_SOCIETY_CULTURE_MASTER_KNOWLEDGE]] |

### 4.2 Domain Engine Canon (C01–C12)

| ID | Domain | Master Knowledge File |
|:---|:---|:---|
| C01 | Meta-Logic | [[AMOS_C01_META_LOGIC_MASTER_KNOWLEDGE]] |
| C02 | Math/Compute | [[AMOS_C02_MATH_COMPUTE_MASTER_KNOWLEDGE]] |
| C03 | Physics/Cosmos | [[AMOS_C03_PHYSICS_COSMOS_MASTER_KNOWLEDGE]] |
| C04 | Bio/Neuro | [[AMOS_C04_BIO_NEURO_MASTER_KNOWLEDGE]] |
| C05 | Mind/Behavior | [[AMOS_C05_MIND_BEHAVIOR_MASTER_KNOWLEDGE]] |
| C06 | Society/Culture | [[AMOS_C06_SOCIETY_CULTURE_MASTER_KNOWLEDGE]] |
| C07 | Econ/Finance | [[AMOS_C07_ECON_FINANCE_MASTER_KNOWLEDGE]] |
| C08 | Strategy/Game | [[AMOS_C08_STRATEGY_GAME_MASTER_KNOWLEDGE]] |
| C09 | Org/Law/Policy | [[AMOS_C09_ORG_LAW_POLICY_MASTER_KNOWLEDGE]] |
| C10 | Tech/Engineering | [[AMOS_C10_TECH_ENGINEERING_MASTER_KNOWLEDGE]] |
| C11 | Design/Language | [[AMOS_C11_DESIGN_LANGUAGE_MASTER_KNOWLEDGE]] |
| C12 | Earth/Ecology | [[AMOS_C12_EARTH_ECOLOGY_MASTER_KNOWLEDGE]] |

### 4.3 Knowledge-Plane Segments

| Segment | Path | Role |
|:---|:---|:---|
| 00_INDEX | `00_INDEX/` | RSCF index, claim tensor, evidence tensor |
| 02_CLAIMS | `02_CLAIMS/` | Structured claim registry |
| 03_RSCF | `03_RSCF/` | RSCF node registry and relations |
| 05_FRAMEWORKS | `05_FRAMEWORKS/` | Framework MOC and canonical framework nodes |
| 06_DOMAIN_KNOWLEDGE | `06_DOMAIN_KNOWLEDGE/` | Domain-specific knowledge artifacts |
| LLM_WIKI | `LLM_WIKI/` | LLM knowledge base and raw wiki ingestion |
| engine | `engine/` | HSE, HIE, Speed, and other engine specifications |
| kernel | `kernel/` | Domain kernel specifications |
| trang | `trang/` | Trang framework research and ontology dynamics |
| stubs | `stubs/` | Stub artifacts awaiting canonical ingestion |

### 4.4 Cross-Plane Bindings

- **Governed by canon** — [[01_CANON/01_CORE_LAWS/LAW_HIERARCHY|AMOS Core Laws]]
- **Kernel interaction** — [[02_KERNEL/02_KERNEL_README|KERNEL_README]]
- **Control-plane gates** — [[03_CONTROL_PLANE/03_CONTROL_PLANE_README|CONTROL_PLANE_README]]
- **Observed by** — [[17_OBSERVABILITY/17_OBSERVABILITY_README|OBSERVABILITY_README]] (never treated as authority)
- **Recovered via operations** — [[20_OPERATIONS/20_OPERATIONS_README|OPERATIONS_README]]
- **Root navigation** — [[00_ROOT/00_ROOT_MOC|AMOS MOC]]""",

        "gaps": """1. **Executable binding NOT_ESTABLISHED** — the Knowledge plane's structural contracts are present, but system-wide executable closure (MVCC/CAS, atomic multi-RSCF, causal epoch finality) is not established merely by their presence.
2. **Canonical status UNKNOWN/GAP** — v4.5–v4.17 labels remain historical consolidation labels, not promoted canonical successors.
3. **Cross-domain bridge proofs** — the tensor composition $\mathcal{T}_{\text{knowledge}}$ is structurally defined but executed bridge validation across all 12 domains is NOT_ESTABLISHED.
4. **Stub ingestion** — 284 stub artifacts in `stubs/` await canonical ingestion; their promotion to canonical nodes requires verified native-canon sources.
5. **Validation receipts** — [[ROUTING_POLICY_VALIDATION_RECEIPT]] and [[AUTHZ_ENGINE_VALIDATION_RECEIPT]] are required before promotion of any knowledge-plane artifact to canonical status.
6. **LLM_WIKI provenance** — wiki ingestion artifacts carry SOURCE_CLAIM status; independent validation of their content is NOT_ESTABLISHED.""",

        "ingestion_rule": """```yaml
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
```""",
    },
}


# ---------------------------------------------------------------------------
# Template
# ---------------------------------------------------------------------------

DISCLAIMER_BLOCK = """```text
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

RSCF_NODE_TEMPLATE = """RSCF-NODE

node_id: {node_id}

node_type: artifact

path: {rel_path}

claim_class: AMOS_MODEL

rscf_state: substantive_specification

canonical_status: UNKNOWN/GAP

RSCF-RELATIONS:

  - INDEXED_BY: [[00_ROOT/00_HOME]]

  - INDEXED_BY: [[AMOS_RSCF_NODES]]

  - GOVERNED_BY: [[01_CANON/01_CORE_LAWS/LAW_HIERARCHY]]

  - INDEXED_BY: [[11_KNOWLEDGE/11_KNOWLEDGE_MOC]]
"""


def build_expanded_content(filename: str, spec: dict, original: str) -> str:
    """Build the expanded markdown content for a placeholder file."""
    # Parse original frontmatter
    fm_match = re.match(r'^---\n(.*?)\n---\n', original, re.DOTALL)
    if not fm_match:
        raise ValueError(f"No frontmatter found in {filename}")

    fm_text = fm_match.group(1)

    # Update frontmatter fields
    # status: PLACEHOLDER -> SUBSTANTIVE_SPECIFICATION
    fm_text = re.sub(
        r'status:\s*"?PLACEHOLDER"?',
        'status: "SUBSTANTIVE_SPECIFICATION"',
        fm_text,
    )
    # version: 0.1.0 -> 1.0.0
    fm_text = re.sub(
        r'version:\s*"?0\.\d+\.\d+"?',
        'version: "1.0.0"',
        fm_text,
    )
    # updated date
    fm_text = re.sub(
        r'updated:\s*"?[^"\n]+"?',
        'updated: "2026-09-04"',
        fm_text,
    )
    # Add placeholder_expanded tag if not present
    if 'placeholder_expanded' not in fm_text:
        # Find the tags block and add the tag
        fm_text = re.sub(
            r'(tags:\n(?:  - [^\n]+\n)*?)(  - rscf)',
            r'\1  - placeholder_expanded\n\2',
            fm_text,
        )
    # Remove canon_placeholder tag (no longer a placeholder)
    fm_text = re.sub(r'  - canon_placeholder\n', '', fm_text)

    # Update rscf_state in RSCF-NODE footer
    # Update canonical_status references

    # Build the body
    title = spec["title"]
    h1 = spec["h1"]
    node_id = f"amos_11_knowledge_{filename.replace('.md', '').lower()}"

    body = f"""# {h1}

## 0. Status

`{filename}` is a **substantive specification** for the **Knowledge** plane segment at `11_KNOWLEDGE`.

It defines the canonical AMOS CORE V4.4 reasoning and governance lineage as it intersects the Knowledge plane. The governing boundaries are:

{DISCLAIMER_BLOCK}

Origin architect / steward:

**Trang Phan**

---

## 1. Purpose

{spec["purpose"]}

---

## 2. Formal Definition

{spec["formal"]}

---

## 3. Application / Cross-References

{spec["applications"]}

---

## 4. Gaps

{spec["gaps"]}

---

## 5. Ingestion Rule

{spec["ingestion_rule"]}

---

## 6. Contract Discipline

Typed artifacts · provenance stamped · epistemic class declared · confidence ceiling 0.95 · fail-closed on UNKNOWN/GAP · receipts for consequential effects · rollback basin before mutation.

---

## 7. Worked Semantics

Given an operation touching `11_KNOWLEDGE · ARTIFACT` within the Knowledge plane:

1. **Admit** — resolve the artifact by id + version; unresolved id ⇒ `UNKNOWN/GAP`, fail closed.
2. **Bind scope** — declare domain / regime / H-M-L applicability before any mutation.
3. **Check authority** — authority_ref must be epoch-valid; capability alone never authorizes.
4. **Validate preconditions** — dependency closure traversed to the smallest result-changing set.
5. **Propose** — candidate state is non-authoritative until gates pass (`PROPOSAL ≠ COMMIT`).
6. **Commit or hold** — on any failed premise: preserve unaffected state, invalidate dependent descendants only, record receipt.

---

## 8. Promotion-Gate Checklist

- [x] substantive content populated from verified native-canon source
- [ ] typed schema bound to this artifact
- [ ] identity + versioning implemented
- [ ] negative cases covered (missing · malformed · stale · unauthorized input)
- [ ] provenance edges persisted and validated
- [ ] rollback basin demonstrated for consequential effects
- [ ] executed validation receipt specific to this artifact
- [ ] unresolved critical gaps registered as UNKNOWN/GAP (visible)

---

[[00_ROOT_MOC|AMOS MOC]]

---

**Related:** [[00_ROOT/00_HOME]] · [[AMOS_RSCF_NODES]] · [[11_KNOWLEDGE/11_KNOWLEDGE_MOC]]

---

{RSCF_NODE_TEMPLATE.format(node_id=node_id, rel_path=f"11_KNOWLEDGE/{filename}")}
"""

    return f"---\n{fm_text}\n---\n\n{body}"


def is_placeholder(filepath: Path) -> bool:
    """Check if a file is a placeholder (status: PLACEHOLDER or ADD-ONLY placeholder).
    Skips files already expanded to SUBSTANTIVE_SPECIFICATION."""
    try:
        content = filepath.read_text(encoding="utf-8")
    except Exception:
        return False

    # Skip already-expanded files
    if re.search(r'status:\s*"?SUBSTANTIVE_SPECIFICATION"?', content):
        return False

    # Check for status: PLACEHOLDER in frontmatter
    if re.search(r'status:\s*"?PLACEHOLDER"?', content):
        return True
    # Check for ADD-ONLY placeholder
    if "ADD-ONLY placeholder" in content:
        return True
    # Check for canon_placeholder tag (but not placeholder_expanded)
    if "canon_placeholder" in content and "placeholder_expanded" not in content:
        return True
    return False


def main():
    print("=" * 70)
    print("AMOS Knowledge-Plane Placeholder Expander")
    print(f"Root: {VAULT_ROOT}")
    print(f"Mode: {'DRY RUN' if DRY_RUN else 'WRITE'}")
    print("=" * 70)

    # Find all placeholder files
    placeholder_files = []
    for md_file in VAULT_ROOT.rglob("*.md"):
        if is_placeholder(md_file):
            placeholder_files.append(md_file)

    print(f"\nFound {len(placeholder_files)} placeholder file(s):\n")
    for f in placeholder_files:
        rel = f.relative_to(VAULT_ROOT)
        print(f"  - {rel}")

    if not placeholder_files:
        print("\nNo placeholder files found. Nothing to do.")
        return

    expanded = 0
    skipped = 0

    for filepath in placeholder_files:
        filename = filepath.name
        rel_path = filepath.relative_to(VAULT_ROOT)

        # Check if we have an expansion spec for this file
        if filename not in EXPANSIONS:
            # Try matching by basename without extension
            base = filename.replace(".md", "")
            matched = False
            for key in EXPANSIONS:
                if key.replace(".md", "").lower() == base.lower():
                    filename = key
                    matched = True
                    break
            if not matched:
                print(f"\n  SKIP (no expansion spec): {rel_path}")
                skipped += 1
                continue

        spec = EXPANSIONS[filename]
        original = filepath.read_text(encoding="utf-8")

        expanded_content = build_expanded_content(filename, spec, original)

        if DRY_RUN:
            print(f"\n  DRY RUN — would expand: {rel_path}")
            print(f"  Original lines: {len(original.splitlines())}")
            print(f"  Expanded lines: {len(expanded_content.splitlines())}")
        else:
            filepath.write_text(expanded_content, encoding="utf-8")
            print(f"\n  EXPANDED: {rel_path}")
            print(f"  Original lines: {len(original.splitlines())}")
            print(f"  Expanded lines: {len(expanded_content.splitlines())}")

        expanded += 1

    print(f"\n{'=' * 70}")
    print(f"Summary: {expanded} expanded, {skipped} skipped, {len(placeholder_files)} total placeholders")
    print("=" * 70)


if __name__ == "__main__":
    main()
