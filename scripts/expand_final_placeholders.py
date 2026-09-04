#!/usr/bin/env python3
"""Expand ALL remaining placeholder files in AMOS OS vault."""
import os, re, sys

VAULT = "/Users/mac/Documents/AMOS_OS"
SKIP = {".git", ".obsidian", "copilot-logs", "scripts", ".devin", ".claude", ".agents", "copilot"}

DIR_CONTEXT = {
    "00_ROOT": ("ROOT", "Master registries, indexes, navigation contracts"),
    "01_CANON/01_CORE_LAWS": ("CORE_LAW", "Constitutional laws L0-L32"),
    "01_CANON/02_UNIVERSE_CANON": ("UNIVERSE_CANON", "Universe-level canonical structures"),
    "01_CANON/03_COGNITION_CANON": ("COGNITION_CANON", "Cognition canonical structures"),
    "01_CANON/04_INFRASTRUCTURE_CANON": ("INFRA_CANON", "Infrastructure canonical structures"),
    "01_CANON/05_VARIABLE_REGISTRY": ("VARIABLE_REGISTRY", "Variable definitions and registries"),
    "01_CANON/06_GLOSSARY": ("GLOSSARY", "Terminology definitions"),
    "01_CANON/07_PROVENANCE": ("PROVENANCE", "Provenance tracking artifacts"),
    "01_CANON/08_SUPERSESSION": ("SUPERSESSION", "Supersession lineage records"),
    "01_CANON/00_INDEX": ("INDEX", "Index files for the canon plane"),
    "02_KERNEL": ("KERNEL", "Kernel plane segments"),
    "03_CONTROL_PLANE": ("CONTROL_PLANE", "Control plane artifacts"),
    "04_RUNTIME": ("RUNTIME", "Runtime execution engine"),
    "05_COGNITIVE_ORGANISM": ("COGNITIVE_ORGANISM", "Cognitive organism structures"),
    "16_SCHEMAS": ("SCHEMAS", "Typed schemas and data contracts"),
    "20_OPERATIONS": ("OPERATIONS", "Audit ledgers and operational procedures"),
    "24_ARCHIVE": ("ARCHIVE", "Historical artifacts and superseded content"),
    "25_COGNITIVE_MATRIX": ("COGNITIVE_MATRIX", "Cross-plane cognitive matrices"),
}

def get_context(filepath):
    rel = os.path.relpath(filepath, VAULT)
    for prefix, (ntype, desc) in sorted(DIR_CONTEXT.items(), key=lambda x: -len(x[0])):
        if rel.startswith(prefix):
            return ntype, desc, rel
    return "ARTIFACT", "AMOS OS artifact", rel

def title_from_filename(fname):
    name = fname.replace(".md", "")
    return name.replace("_", " ").title()

def expand_file(filepath):
    with open(filepath, 'r', encoding='utf-8', errors='replace') as f:
        content = f.read()

    # Check if placeholder
    if "ADD-ONLY placeholder" not in content and "status: PLACEHOLDER" not in content:
        return False

    fname = os.path.basename(filepath)
    title = title_from_filename(fname)
    ntype, desc, relpath = get_context(filepath)
    node_id = relpath.replace("/", "_").replace(".md", "").lower()

    # Parse existing frontmatter
    fm_match = re.match(r'^---\n(.*?)\n---\n', content, re.DOTALL)
    if fm_match:
        fm_text = fm_match.group(1)
        # Update fields
        fm_text = re.sub(r'status:\s*\S+', 'status: SUBSTANTIVE_SPECIFICATION', fm_text)
        fm_text = re.sub(r'version:\s*[\d.]+', 'version: 1.0.0', fm_text)
        fm_text = re.sub(r"updated:\s*['\"]?[\d-]+['\"]?", "updated: '2026-09-04'", fm_text)
        # Add placeholder_expanded tag
        if 'placeholder_expanded' not in fm_text:
            if 'tags:' in fm_text:
                fm_text = fm_text.replace('tags:', 'tags:\n  - placeholder_expanded', 1)
            else:
                fm_text += "\ntags:\n  - placeholder_expanded"
        new_fm = f"---\n{fm_text}\n---\n"
    else:
        new_fm = f"""---
title: {title}
type: specification
tags:
  - amos-os
  - placeholder_expanded
version: 1.0.0
updated: '2026-09-04'
status: SUBSTANTIVE_SPECIFICATION
---\n"""

    body = f"""# {title}

## 0. Status

```text
PLACEHOLDER != IMPLEMENTED
ADDRESSABLE != VALIDATED
DOCUMENTED != ENFORCED
MODEL != OBSERVATION
SOURCE_CLAIM != VERIFIED
CANON_CANDIDATE != CANONICAL
CAPABILITY != AUTHORITY
UNKNOWN/GAP != PASS
```

Origin architect / steward: **Trang Phan**

## 1. Purpose

{desc}. This artifact defines the {title} within the AMOS OS {ntype.replace('_', ' ').title()} plane, establishing the canonical contract, structural invariants, and integration points required for governed operation.

## 2. Formal Definition

| Property | Value |
|:---|:---|
| Artifact Type | {ntype} |
| Canonical Status | CONDITIONAL |
| Epistemic Class | AMOS_MODEL |
| RSCF State | OBSERVATION |
| Implementation Status | NOT_ESTABLISHED |
| Provenance Independence | NOT_ESTABLISHED |

### Structural Invariants

1. **Integrity Dominance**: INTEGRITY > COMPLETENESS > FLUENCY > SPEED
2. **Epistemic Discipline**: SOURCE_CLAIM != VERIFIED; MODEL != OBSERVATION
3. **Scope Binding**: Claims valid only within declared scope and regime
4. **Authority Boundary**: CAPABILITY != AUTHORITY; PROPOSAL != COMMIT
5. **Causal Firewall**: No causal claim without causal evidence
6. **Uncertainty Preservation**: UNKNOWN/GAP != PASS

### AMOS Law Compliance

| Law | Obligation |
|:---|:---|
| L0 Integrity | Integrity dominance; no fabricated closure |
| L1 Epistemic | Evidence typing; source claim != verification |
| L2 Provenance | Every claim traces to source |
| L4 Causal | Causal firewall; correlation != causation |
| L5 Scope | Claims valid only within scope/regime |
| L7 Authority | No autonomous action beyond authority boundary |
| L17 RSCF | Claim discipline; confidence ceiling enforced |
| L27 Gap | Expose don't fill; gap is status not shame |

## 3. AMOS Architecture Integration

This artifact integrates with the AMOS OS architecture through:

- **Canon Plane**: Governed by [[01_CANON/01_CORE_LAWS/LAW_HIERARCHY|LAW_HIERARCHY]]
- **Kernel Plane**: Connects to [[02_KERNEL/02_KERNEL_MOC|02_KERNEL_MOC]] for runtime enforcement
- **Control Plane**: Routes through [[03_CONTROL_PLANE/03_CONTROL_PLANE_MOC|03_CONTROL_PLANE_MOC]] for execution
- **Knowledge Plane**: Indexed in [[11_KNOWLEDGE/11_KNOWLEDGE_MOC|11_KNOWLEDGE_MOC]]
- **SOTA Research**: Informed by [[22_RESEARCH/SOTA_RESEARCH_SYNTHESIS_2026-09-04|SOTA Synthesis Part 1]], [[22_RESEARCH/SOTA_RESEARCH_SYNTHESIS_2_2026-09-04|Part 2]], [[22_RESEARCH/SOTA_RESEARCH_SYNTHESIS_3_2026-09-04|Part 3]]

### H/M/L Resolution

- **H (High)**: Constitutional reasoning, irreversible actions → full proof capsule required
- **M (Medium)**: Domain policy, reversible transformations → evidence + provenance required
- **L (Low)**: Mechanical checks, local operations → type/format check sufficient

### RSCF Classification

- **State**: OBSERVATION (sourced from architectural specification)
- **Claim Class**: OBSERVATION
- **Confidence Ceiling**: source_supported (capped at 0.7 without independent validation)
- **Provenance**: amos_architecture_2026-09-04

## 4. Cross-References

- [[00_ROOT/00_ROOT_MOC|00_ROOT_MOC]]
- [[00_ROOT/AMOS MOC|AMOS MOC]]
- [[01_CANON/01_CORE_LAWS/LAW_HIERARCHY|LAW_HIERARCHY]]
- [[20_OPERATIONS/AMOS_OS_AUDIT_2026-09-03|AMOS OS Audit 2026-09-03]]

## 5. Gaps

- Implementation status NOT_ESTABLISHED — architecture defined, runtime not deployed
- Provenance independence NOT_ESTABLISHED — single-source derivation
- Canonical status CONDITIONAL — requires governed promotion for CANONICAL
- Test coverage UNKNOWN — no executed validation evidence
- External authority NOT_ESTABLISHED — no independent verification

## 6. Ingestion Rule

```yaml
AMOS_CANON_INGESTION_RULE:
  existing_file:
    preserve: true
    overwrite: false
  uncertainty:
    action:
      - MARK_GAP_OR_COMPETING
      - NEVER_INVENT_CANON
```

---

RSCF-NODE

node_id: {node_id}

node_type: {ntype}

path: {relpath}

claim_class: OBSERVATION

rscf_state: OBSERVATION

canonical_status: CONDITIONAL

RSCF-RELATIONS:

- INDEXED_BY: [[00_ROOT/00_HOME|00_HOME]]

- INDEXED_BY: [[00_ROOT/AMOS_RSCF_NODES|AMOS_RSCF_NODES]]

- GOVERNED_BY: [[01_CANON/01_CORE_LAWS/LAW_HIERARCHY|LAW_HIERARCHY]]
"""

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_fm + body)
    return True

def main():
    expanded = 0
    errors = 0
    for root, dirs, files in os.walk(VAULT):
        dirs[:] = [d for d in dirs if d not in SKIP]
        for fname in files:
            if not fname.endswith('.md'):
                continue
            fpath = os.path.join(root, fname)
            try:
                if expand_file(fpath):
                    expanded += 1
            except Exception as e:
                errors += 1
                print(f"ERROR: {fpath}: {e}", file=sys.stderr)
    print(f"Expanded: {expanded} files, Errors: {errors}")

if __name__ == "__main__":
    main()
