#!/usr/bin/env python3
"""Governed infra README filler — pass 2 of the Cognitive Matrix placeholder campaign.

Fills ONLY the 5 remaining package-README stubs in 05–09 (MATRIX_INFRASTRUCTURE_
PLACEHOLDER class, <1.6KB). Never touches large contract specs (10_ROUTING/
ROUTING_POLICY.md, BINDING_RULES.md, PROMOTION_GATES.md etc.) — those are
PROPOSED_SPECIFICATION artifacts whose own status strings are authoritative.
Idempotent; emits receipt to 07_COVERAGE/.
"""
import os, json

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
STAMP = "2026-08-26"

SUBSYSTEMS = {
    "05_CELL_REGISTRY": (
        "Cell Registry",
        "The Cell Registry is the addressable inventory of Cognitive Matrix cells: "
        "each cell binds one (primitive × lifecycle-operation × control-plane) triple "
        "to a stable identifier. The registry answers 'what cells exist and what state "
        "is each in' without asserting that any cell is implemented or validated.",
        [
            "CELL_EXISTS != CELL_IMPLEMENTED",
            "REGISTRY_ENTRY != VALIDATED_CELL",
            "Registry completeness does not imply matrix semantic completeness",
        ],
        ["05 registry enumerates cells; 06 defines their contracts",
         "07 coverage consumes registry counts",
         "08 gap registry records missing/unbound cells"],
    ),
    "06_CELL_CONTRACTS": (
        "Cell Contracts",
        "Cell Contracts define the per-cell obligations a registered cell must satisfy "
        "before any promotion beyond UNKNOWN/GAP: typed inputs/outputs, invariants, "
        "authority bindings, evidence requirements. A contract is an obligation "
        "statement, never proof of satisfaction.",
        [
            "CONTRACT_DEFINED != CONTRACT_SATISFIED",
            "CAPABILITY != AUTHORITY",
            "Evidence requirements listed != evidence collected",
        ],
        ["05 registry addresses the cell each contract belongs to",
         "11 validation judges contract satisfaction evidence"],
    ),
    "07_COVERAGE": (
        "Coverage Model",
        "Coverage measures which declared Matrix addresses carry filled contracts vs "
        "placeholders vs executable implementations vs validation evidence — as four "
        "distinct axes that are never merged into one number.",
        [
            "COVERAGE_COUNTED != QUALITY_VALIDATED",
            "Contract coverage axis != implementation coverage axis != validation coverage axis",
            "100% contract coverage does not close implementation or validation gaps",
        ],
        ["01–04 packages supply the declared address space",
         "08 structural gaps consume coverage deltas"],
    ),
    "08_STRUCTURAL_GAPS": (
        "Structural Gap Registry",
        "The Gap Registry records every declared-but-unfilled or filled-but-unvalidated "
        "Matrix surface with priority and promotion path. Gaps stay visible by design: "
        "UNKNOWN/GAP must remain distinguishable from PASS at every layer.",
        [
            "GAP_REGISTERED != GAP_CLOSED",
            "GAP_PRIORITY ordering is DERIVED judgment, not measured fact",
            "Closing a documentation gap does not close its implementation/validation siblings",
        ],
        ["07 coverage supplies gap candidates",
         "11 promotion gates govern gap closure claims"],
    ),
    "09_DEPENDENCY_GRAPH": (
        "Dependency Graph",
        "The Dependency Graph captures directed edges between Matrix surfaces so that "
        "invalidation propagates locally (descendants only) instead of globally. Edge "
        "presence is a structural claim; edge correctness requires validation evidence.",
        [
            "EDGE_DECLARED != EDGE_VALIDATED",
            "Cycles in the dependency graph are defects",
            "Invalidation follows descendants only; unrelated state is preserved",
        ],
        ["01–04 package dependencies feed edges",
         "10 routing and 11 validation consume invalidation semantics"],
    ),
}

TEMPLATE = """---
tags: ['cognitive_matrix', '{slug}', 'readme', 'contract_filled']
---

# {dir} — {name} Contract Overview

**Package:** `{dir}`
**Class:** `COGNITIVE_MATRIX_INFRASTRUCTURE_CONTRACT`
**Epistemic class:** `DERIVED / MODEL EXTENSION`
**Status:** `CONTRACT_FILLED / NOT_IMPLEMENTED / NOT_VALIDATED`
**Filled by:** governed generator `12_GENERATORS/fill_infra_readmes.py` · **Date:** `{stamp}`

## Scope

{definition}

## Hard boundaries

```text
{bounds}
```

## Dependency position

{deps}

## RSCF completion state

```yaml
claim_class: DERIVED
evidence: []            # no measured evidence at this layer
provenance:
  - AMOS canon corpus reconstruction
scope: cognitive_matrix_infrastructure_package_contract
regime: architecture-contract
freshness: {stamp}
dependencies: []
competing: []
falsifiers: []
confidence_ceiling: 0.6   # contract-only status: no implementation, no validation
```

## Gap matrix

| Surface | Status |
|---|---|
| Definition/contract | FILLED (this pass) |
| Executable implementation | UNKNOWN/GAP |
| Validation evidence | UNKNOWN/GAP |
| Authority binding | UNKNOWN/GAP |
| Runtime integration | UNKNOWN/GAP |

```text
CONTRACT_FILLED != IMPLEMENTED
DOCUMENTED != EXECUTABLE
MODEL != VERIFIED
UNKNOWN/GAP != PASS
```

---

[[COGNITIVE_MATRIX_MOC]] · [[00_ROOT/00_ROOT_MOC.md|AMOS MOC]]

---
RSCF-NODE
node_id: {slug}_infrastructure_readme
node_type: note
path: 25_COGNITIVE_MATRIX/{dir}/{dir}_COGNITIVE_MATRIX_README.md
claim_class: DERIVED
"""


def main():
    filled = skipped = 0
    for d, (name, definition, bounds, deps) in SUBSYSTEMS.items():
        path = os.path.join(ROOT, d, f"{d.split('_', 1)[1].upper()}_COGNITIVE_MATRIX_README.md")
        text = open(path).read()
        if "PLACEHOLDER / UNVALIDATED" not in text:
            skipped += 1
            continue
        slug = d.split("_", 1)[1].lower()
        body = TEMPLATE.format(dir=d, name=name, slug=slug, stamp=STAMP,
                               definition=definition,
                               bounds="\n".join(bounds),
                               deps="\n".join(f"- {x}" for x in deps))
        with open(path, "w") as fh:
            fh.write(body)
        filled += 1
    receipt = {
        "date": STAMP,
        "generator": "25_COGNITIVE_MATRIX/12_GENERATORS/fill_infra_readmes.py",
        "filled": filled,
        "skipped_already_filled": skipped,
        "status": "INFRA_README_FILL_PASS_2",
        "untouched_authoritative_specs": [
            "10_ROUTING/ROUTING_POLICY.md", "10_ROUTING/BINDING_RULES.md",
            "10_ROUTING/ROUTING_AUDIT.md", "10_ROUTING/ROUTING_COGNITIVE_MATRIX_README.md",
            "11_VALIDATION/PROMOTION_GATES.md", "11_VALIDATION/VALIDATION_EVIDENCE.md",
            "11_VALIDATION/VALIDATION_LEVELS.md", "11_VALIDATION/VALIDATION_COGNITIVE_MATRIX_README.md",
        ],
        "boundaries": ["NOT implemented", "NOT validated", "DERIVED/MODEL only"],
    }
    print(json.dumps(receipt, indent=1))
    with open(os.path.join(ROOT, "07_COVERAGE", "INFRA_FILL_RECEIPT.json"), "w") as fh:
        json.dump(receipt, fh, indent=1)


if __name__ == "__main__":
    main()
