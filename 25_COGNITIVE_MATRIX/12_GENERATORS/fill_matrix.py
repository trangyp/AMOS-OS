#!/usr/bin/env python3
"""Governed Cognitive Matrix placeholder filler.
Fills PLACEHOLDER / UNVALIDATED files with DERIVED/MODEL-class contract content.
Never claims IMPLEMENTED or VALIDATED. Idempotent: skips already-filled files
unless --force. Emits receipt at 25_COGNITIVE_MATRIX/07_COVERAGE/.
"""
import os, re, sys, json, datetime

ROOT = "/Users/mac/Documents/AMOS_OS/25_COGNITIVE_MATRIX"
STAMP = "2026-08-26"

# file-type -> (title suffix, section builder key)
FTYPE_MAP = {
    "DEFINITION": "Definition", "PURPOSE": "Purpose", "SEMANTICS": "Semantics",
    "INPUT_OUTPUT": "Input/Output", "PRECONDITIONS": "Preconditions",
    "POSTCONDITIONS": "Postconditions", "STATE_TRANSITIONS": "State Transitions",
    "INVARIANTS": "Invariants", "FAILURE_MODES": "Failure Modes",
    "REPAIR": "Repair & Recovery", "DEPENDENCIES": "Dependencies",
    "CONTROL_PLANES": "Control-Plane Requirements", "AGENTS": "Agents",
    "SKILLS": "Skills", "WORKFLOWS": "Workflows", "PROTOCOLS": "Protocols",
    "TESTS": "Tests & Validators", "GAP_MATRIX": "Gap Matrix",
    "PROVENANCE": "Provenance", "RSCF": "RSCF Record", "HML": "H/M/L Applicability",
    "MEMORY": "Memory Contract", "EQUATIONS": "Equations", "VARIABLES": "Variables",
    "OPERATORS": "Operators", "STATE": "State", "README": "Overview",
    "AUTHORITY": "Authority", "SCOPE": "Scope", "POLICIES": "Policies",
    "DECISION_RULES": "Decision Rules", "OBSERVABILITY": "Observability",
    "BOUNDARIES": "Boundaries", "TRANSLATION_RULES": "Translation Rules",
}

def ftype_of(fname):
    base = fname.replace(".md", "")
    for k in sorted(FTYPE_MAP, key=len, reverse=True):
        if base.endswith("_" + k):
            return k
    return None

def load_payloads():
    import payloads_a, payloads_b, payloads_c1, payloads_c2, payloads_d1, payloads_d2, payloads_e, payloads_f
    p = {}
    for mod in (payloads_a, payloads_b, payloads_c1, payloads_c2, payloads_d1, payloads_d2, payloads_e, payloads_f):
        p.update(mod.PAYLOADS)
    return p

def build_body(pkg_id, pkg_name, family, ftype, pl, fname):
    title = FTYPE_MAP.get(ftype, ftype.title())
    d = pl["definition"]
    lines = []
    lines.append(f"# {pkg_id} — {title}\n")
    lines.append(f"**Package:** `{pkg_id}_{pkg_name}`  ")
    lines.append("**Class:** `COGNITIVE_MATRIX_CONTRACT`  ")
    lines.append("**Epistemic class:** `DERIVED / MODEL EXTENSION`  ")
    lines.append(f"**Status:** `CONTRACT_FILLED / NOT_IMPLEMENTED / NOT_VALIDATED`  ")
    lines.append(f"**Filled by:** governed generator `fill_matrix.py` · **Date:** `{STAMP}`\n")
    lines.append("## Scope\n")
    lines.append(pl["scope"])
    if ftype == "DEFINITION":
        lines.append("\n## Definition\n")
        lines.append(d)
        lines.append("\nThis is a **contract-level definition**, not an implementation claim.")
    elif ftype == "PURPOSE":
        lines.append("\n## Purpose\n")
        lines.append(d.split(". ")[0] + ".")
        lines.append(f"\n{pl['purpose']}")
    elif ftype == "SEMANTICS":
        lines.append("\n## Semantics\n")
        lines.append(d)
        lines.append("\n### Semantic rules\n")
        for r in pl["semantics"]:
            lines.append(f"- {r}")
    elif ftype == "INPUT_OUTPUT":
        lines.append("\n## Typed inputs\n")
        for i in pl["inputs"]:
            lines.append(f"- {i}")
        lines.append("\n## Typed outputs\n")
        for o in pl["outputs"]:
            lines.append(f"- {o}")
    elif ftype == "PRECONDITIONS":
        lines.append("\n## Preconditions\n")
        for r in pl["preconditions"]:
            lines.append(f"- {r}")
    elif ftype == "POSTCONDITIONS":
        lines.append("\n## Postconditions\n")
        for r in pl["postconditions"]:
            lines.append(f"- {r}")
    elif ftype == "STATE_TRANSITIONS":
        lines.append("\n## State variables\n")
        for s in pl["state_vars"]:
            lines.append(f"- {s}")
        lines.append("\n## Transitions\n")
        for t in pl["transitions"]:
            lines.append(f"- {t}")
    elif ftype == "INVARIANTS":
        lines.append("\n## Invariants\n")
        for inv in pl["invariants"]:
            lines.append(f"- `INV-{pkg_id}-{inv[0]}`: {inv[1]}")
    elif ftype == "FAILURE_MODES":
        lines.append("\n## Failure modes\n")
        for fm in pl["failure_modes"]:
            lines.append(f"- `FM-{pkg_id}-{fm[0]}`: {fm[1]} → detection: {fm[2]}")
    elif ftype == "REPAIR":
        lines.append("\n## Failure handling\n")
        for fm in pl["failure_modes"]:
            lines.append(f"- On `FM-{pkg_id}-{fm[0]}`: {fm[3]}")
        lines.append("\n## Recovery basin\n")
        lines.append(pl["recovery"])
    elif ftype == "DEPENDENCIES":
        lines.append("\n## Upstream dependencies\n")
        for dep in pl["deps_up"]:
            lines.append(f"- [[{dep}]]")
        lines.append("\n## Downstream dependents\n")
        for dep in pl["deps_down"]:
            lines.append(f"- [[{dep}]]")
        lines.append("\nDependency direction follows the primitive flow order; cycles are defects.")
    elif ftype == "CONTROL_PLANES":
        lines.append("\n## Control-plane binding\n")
        for cp in pl["control_planes"]:
            role = pl["cp_roles"].get(cp, "bound control plane")
            lines.append(f"- [[{cp}]] — {role}")
    elif ftype == "AGENTS":
        lines.append("\n## Agent requirements\n")
        for a in pl["agents"]:
            lines.append(f"- {a}")
        lines.append("\nNo runtime agent is bound yet (`UNKNOWN/GAP` until registered).")
    elif ftype == "SKILLS":
        lines.append("\n## Governing skills\n")
        for s in pl["skills"]:
            lines.append(f"- {s}")
    elif ftype == "WORKFLOWS":
        lines.append("\n## Workflow requirements\n")
        for w in pl["workflows"]:
            lines.append(f"- {w}")
    elif ftype == "PROTOCOLS":
        lines.append("\n## Protocol surface\n")
        for pr in pl["protocols"]:
            lines.append(f"- {pr}")
    elif ftype == "TESTS":
        lines.append("\n## Defined tests (TEST_DEFINED ≠ TEST_EXECUTED)\n")
        for i, t in enumerate(pl["tests"], 1):
            lines.append(f"- `T-{pkg_id}-{i:03d}`: {t} — status `DEFINED`")
        lines.append("\nAll tests remain unexecuted at this layer until a validator binds here.")
    elif ftype == "GAP_MATRIX":
        lines.append("\n## Gap matrix\n")
        lines.append("| Surface | Status |")
        lines.append("|---|---|")
        lines.append("| Definition/contract | FILLED (this pass) |")
        lines.append("| Executable implementation | UNKNOWN/GAP |")
        lines.append("| Validation evidence | UNKNOWN/GAP |")
        lines.append("| Authority binding | UNKNOWN/GAP |")
        lines.append("| Runtime integration | UNKNOWN/GAP |")
    elif ftype == "PROVENANCE":
        lines.append("\n## Provenance\n")
        lines.append(f"- Source class: `DERIVED` — reconstructed from AMOS canon corpus")
        lines.append(f"- Generator: `12_GENERATORS` governed fill pass, `{STAMP}`")
        lines.append("- Canon anchors: DMER four-process architecture, 7-Part Universe Canon, RSCF taxonomy")
        lines.append("- No fabricated SOURCE claims: nothing here is presented as observed data")
    elif ftype == "RSCF":
        lines.append("\n```yaml")
        lines.append("claim_class: DERIVED")
        lines.append("evidence: []   # no measured evidence at this layer")
        lines.append("provenance:")
        lines.append("  - 'AMOS canon corpus reconstruction'")
        lines.append("scope: cognitive_matrix_package_contract")
        lines.append("regime: architecture-contract")
        lines.append(f"freshness: {STAMP}")
        lines.append("dependencies: " + json.dumps([d2 for d2 in pl["deps_up"]]))
        lines.append("competing: []")
        lines.append("falsifiers: []")
        lines.append("confidence_ceiling: 0.6")
        lines.append("```\n")
        lines.append("Confidence ceiling 0.6 reflects contract-only status (no implementation, no validation).")
    elif ftype == "HML":
        lines.append("\n| Scale | Applicability |")
        lines.append("|---|---|")
        lines.append(f"| H | {pl['hml']['H']} |")
        lines.append(f"| M | {pl['hml']['M']} |")
        lines.append(f"| L | {pl['hml']['L']} |")
    else:
        # README, STATE, VARIABLES, OPERATORS, EQUATIONS, MEMORY, AUTHORITY,
        # SCOPE, POLICIES, DECISION_RULES, OBSERVABILITY, BOUNDARIES, TRANSLATION_RULES
        lines.append("\n## Contract content\n")
        lines.append(d)
        extra = {
            "STATE": "\n## State ownership\n\n" + pl["state_ownership"],
            "VARIABLES": "\n## Core variables\n\n" + "\n".join(f"- {v}" for v in pl["variables"]),
            "OPERATORS": "\n## Operators exposed\n\n" + "\n".join(f"- {o}" for o in pl["operators"]),
            "EQUATIONS": "\n## Equations\n\n" + pl["equations"],
            "MEMORY": "\n## Memory interaction\n\n" + pl["memory"],
            "AUTHORITY": "\n## Authority requirements\n\n" + pl["authority"],
            "OBSERVABILITY": "\n## Observability signals\n\n" + pl["observability"],
        }
        if ftype in extra and extra[ftype]:
            lines.append(extra[ftype])
        elif ftype in ("README",):
            lines.append("\n## Package inventory\n")
            lines.append(f"`{pkg_id}_{pkg_name}` is a declared {family} package of the Cognitive Matrix. All artifact types carry filled contracts after this pass; implementation/validation remain open gaps.")
        elif ftype in ("BOUNDARIES",):
            lines.append("\n```text\nPACKAGE SEEDED != PACKAGE COMPLETE\nCONTRACT != IMPLEMENTATION\nIMPLEMENTATION != VALIDATION\nUNKNOWN/GAP != PASS\n```\n")
        elif ftype in ("POLICIES", "DECISION_RULES"):
            lines.append("\n## Rules\n")
            for r in pl["invariants"]:
                lines.append(f"- Enforce: {r[1]}")
        elif ftype in ("TRANSLATION_RULES",):
            lines.append("\n## Translation rules\n")
            lines.append(pl["translation_rules"])
    lines.append("\n## Hard boundaries\n")
    lines.append("```text\nCONTRACT_FILLED != IMPLEMENTED\nDOCUMENTED != EXECUTABLE\nMODEL != VERIFIED\nUNKNOWN/GAP != PASS\n```\n")
    lines.append("---\n")
    lines.append("[[COGNITIVE_MATRIX_MOC]] · [[00_ROOT/00_ROOT_MOC.md|AMOS MOC]]\n")
    lines.append("---")
    lines.append("RSCF-NODE")
    node_id = f"{pkg_id.lower()}_{family.split('_')[-1].lower()}_{ftype.lower()}".replace("scale_", "")
    lines.append(f"node_id: {node_id}")
    lines.append("node_type: note")
    lines.append(f"path: {family}/{pkg_id}_{pkg_name}/{fname}")
    lines.append("claim_class: DERIVED")
    return "\n".join(lines)

def main():
    force = "--force" in sys.argv
    payloads = load_payloads()
    filled = skipped = missing_pkg = 0
    by_family = {}
    for family, dirs in [("01_PRIMITIVES", None), ("02_LIFECYCLE_OPERATIONS", None),
                         ("03_CONTROL_PLANES", None), ("04_SCALES", None)]:
        fdir = os.path.join(ROOT, family)
        for pkg in sorted(os.listdir(fdir)):
            pdir = os.path.join(fdir, pkg)
            if not os.path.isdir(pdir) or pkg == "00_INDEX":
                continue
            m = re.match(r"(L\d+|O\d+|C\d+|[HML])_(.+)", pkg)
            if not m:
                continue
            pid, pname = m.group(1), m.group(2)
            key = pid if pid in payloads else ("SCALE_" + pid if pid in "HML" else None)
            if key is None or key not in payloads:
                missing_pkg += 1
                continue
            pl = payloads[key]
            for fname in sorted(os.listdir(pdir)):
                if not fname.endswith(".md") or fname.startswith("COGNITIVE_MATRIX_" + pid) or "_00_INDEX" in fname:
                    continue
                ft = ftype_of(fname)
                if ft is None:
                    continue
                path = os.path.join(pdir, fname)
                text = open(path).read()
                if not force and "PLACEHOLDER / UNVALIDATED" not in text:
                    skipped += 1
                    continue
                body = build_body(pid, pname, family, ft, pl, fname)
                body += f"\nnode_path_note: {path}\n"
                with open(path, "w") as fh:
                    fh.write(body)
                filled += 1
                fam = by_family.setdefault(family, 0)
                by_family[family] = fam + 1
    receipt = {
        "date": STAMP,
        "generator": "25_COGNITIVE_MATRIX/12_GENERATORS/fill_matrix.py",
        "filled": filled,
        "skipped_already_filled": skipped,
        "packages_without_payload": missing_pkg,
        "by_family": by_family,
        "status": "CONTRACT_FILLED_PASS_1",
        "boundaries": ["NOT implemented", "NOT validated", "DERIVED/MODEL only"],
    }

    # ---- Pass 2: infrastructure subsystems (05-11) keyed by file stem ----
    INFRA_DIRS = ["05_CELL_REGISTRY", "06_CELL_CONTRACTS", "07_COVERAGE",
                  "08_STRUCTURAL_GAPS", "09_DEPENDENCY_GRAPH", "10_ROUTING", "11_VALIDATION"]
    STEM_KEYS = {
        "CELL_INDEX": "CELL_INDEX", "CELL_STATUS_REGISTRY": "CELL_STATUS_REGISTRY",
        "CELL_AUTHORITY": "CELL_AUTHORITY", "CELL_BINDINGS": "CELL_BINDINGS",
        "CELL_EVIDENCE": "CELL_EVIDENCE", "CELL_STATE": "CELL_STATE",
        "COVERAGE_THRESHOLDS": "COVERAGE_THRESHOLDS", "COVERAGE_AUDIT": "COVERAGE_AUDIT",
        "COVERAGE_MODEL": "COVERAGE_MODEL",
        "GAP_PRIORITY": "GAP_PRIORITY", "GAP_REGISTRY": "GAP_REGISTRY", "GAP_PROMOTION": "GAP_PROMOTION",
        "DEPENDENCY_TYPES": "DEPENDENCY_TYPES", "INVALIDATION_RULES": "INVALIDATION_RULES",
        "DEPENDENCY_AUDIT": "DEPENDENCY_AUDIT",
        "ROUTING_POLICY": "ROUTING_POLICY", "BINDING_RULES": "BINDING_RULES", "ROUTING_AUDIT": "ROUTING_AUDIT",
    }
    infra_filled = 0
    for d in INFRA_DIRS:
        dd = os.path.join(ROOT, d)
        if not os.path.isdir(dd):
            continue
        sub = os.path.basename(dd).split("_", 1)[1]
        for fname in sorted(os.listdir(dd)):
            if not fname.endswith(".md"):
                continue
            stem = fname[:-3].upper()
            key = STEM_KEYS.get(stem)
            if key is None or key not in payloads:
                continue
            path = os.path.join(dd, fname)
            text = open(path).read()
            if not force and "PLACEHOLDER / UNVALIDATED" not in text:
                continue
            body = build_body(key, "", d, "DEFINITION", payloads[key], fname)
            body += f"\nnode_path_note: {path}\n"
            with open(path, "w") as fh:
                fh.write(body)
            infra_filled += 1
    receipt["infra_filled"] = infra_filled

    print(json.dumps(receipt, indent=1))
    with open(os.path.join(ROOT, "07_COVERAGE", "FILL_RECEIPT.json"), "w") as fh:
        json.dump(receipt, fh, indent=1)

if __name__ == "__main__":
    main()
