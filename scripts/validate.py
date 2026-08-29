#!/usr/bin/env python3
"""
AMOS Skill Validator — L1 Structural Assertions

Validates skill bundles against the AMOS skill rubric and agentskills.io spec.
Inspired by:
  - tardigrde/agent-skill-eval (evals.json schema)
  - danielscholl/claude-sdlc (4-layer test framework, L1 structure)
  - snapsynapse/skill-provenance (MANIFEST.yaml, SHA-256 hashes)
  - jpcaparas/skills (validate.py with REQUIRED_SUPPORT_FILES)
  - agentskills/agentskills RFC #358 (skill_digest, provenance)

Usage:
  python3 scripts/validate.py                    # validate all skills
  python3 scripts/validate.py skills/my-skill/   # validate one skill
  python3 scripts/validate.py --json             # JSON output for CI
  python3 scripts/validate.py --manifest         # generate MANIFEST.yaml
"""

import argparse
import hashlib
import json
import re
import sys
from pathlib import Path
from typing import Optional

try:
    import yaml
except ImportError:
    print("ERROR: PyYAML required. Install: pip install pyyaml", file=sys.stderr)
    sys.exit(2)


# ── Rubric ───────────────────────────────────────────────────────────────────

P1_CHECKS = [
    ("skill_md_exists",      "SKILL.md must exist"),
    ("frontmatter_present",  "SKILL.md must start with YAML frontmatter (---)"),
    ("yaml_valid",           "Frontmatter YAML must parse without error"),
    ("name_present",         "Frontmatter must have 'name' field"),
    ("name_matches_dir",     "Frontmatter 'name' must match directory name"),
    ("description_present",  "Frontmatter must have 'description' field"),
    ("description_length",   "Description must be <= 1024 characters"),
    ("no_placeholders",      "No TODO/TBD/FIXME placeholders in SKILL.md"),
]

P2_CHECKS = [
    ("license_present",      "Frontmatter must have 'license' field"),
    ("steward_present",      "Frontmatter must have 'steward' field"),
    ("version_present",      "Frontmatter must have 'version' field"),
    ("negative_triggers",    "Description must contain negative triggers ('do not use')"),
    ("validation_gates",     "SKILL.md must have '## Validation Gates' section"),
    ("do_not_use_section",   "SKILL.md must have '## Do not use' section"),
    ("references_dir",       "references/ directory must exist"),
    ("scripts_dir",          "scripts/ directory must exist"),
    ("body_under_500_lines", "SKILL.md body should be under 500 lines"),
]

P3_CHECKS = [
    ("origin_architect",     "Frontmatter should have 'origin_architect' field"),
    ("epistemic_class",      "Frontmatter should have 'epistemic_class' field"),
    ("rscf_state",           "Frontmatter should have 'rscf_state' field"),
    ("hml_level",            "Frontmatter should have 'hml_level' field"),
    ("tags_present",         "Frontmatter should have 'tags' field"),
]


# ── Helpers ──────────────────────────────────────────────────────────────────

def parse_frontmatter(text: str) -> tuple[Optional[dict], str]:
    """Split SKILL.md into (frontmatter_dict, body)."""
    if not text.startswith("---"):
        return None, text
    parts = re.split(r"^---\s*$", text, 2, flags=re.MULTILINE)
    if len(parts) < 3:
        return None, text
    try:
        fm = yaml.safe_load(parts[1])
        if not isinstance(fm, dict):
            return None, parts[2]
        return fm, parts[2]
    except yaml.YAMLError:
        return None, parts[2]


def sha256_file(path: Path) -> str:
    """Compute SHA-256 hash of a file."""
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(8192), b""):
            h.update(chunk)
    return f"sha256:{h.hexdigest()}"


# ── Validator ────────────────────────────────────────────────────────────────

def validate_skill(skill_path: Path) -> dict:
    """Validate a single skill directory. Returns result dict."""
    result = {
        "skill": skill_path.name,
        "path": str(skill_path),
        "p1_errors": [],
        "p2_warnings": [],
        "p3_info": [],
        "metrics": {},
        "valid": True,
    }

    # ── P1: Blockers ─────────────────────────────────────────────────────────
    sm = skill_path / "SKILL.md"
    if not sm.exists():
        result["p1_errors"].append("skill_md_exists: SKILL.md does not exist")
        result["valid"] = False
        return result

    text = sm.read_text(encoding="utf-8", errors="replace")

    fm, body = parse_frontmatter(text)
    body_lines = body.count("\n")
    result["metrics"]["skill_md_lines"] = body_lines
    if fm is None:
        result["p1_errors"].append("frontmatter_present: SKILL.md has no YAML frontmatter")
        result["valid"] = False
        return result

    name = fm.get("name", "")
    if not name:
        result["p1_errors"].append("name_present: Frontmatter missing 'name' field")
        result["valid"] = False
    elif name != skill_path.name:
        result["p1_errors"].append(
            f"name_matches_dir: name '{name}' != dir '{skill_path.name}'"
        )
        result["valid"] = False

    desc = str(fm.get("description", ""))
    if not desc:
        result["p1_errors"].append("description_present: Frontmatter missing 'description'")
        result["valid"] = False
    elif len(desc) > 1024:
        result["p1_errors"].append(
            f"description_length: {len(desc)} chars > 1024 limit"
        )
        result["valid"] = False

    if re.search(r"\b(TODO|TBD|FIXME)\b", text, re.IGNORECASE):
        result["p1_errors"].append("no_placeholders: TODO/TBD/FIXME found in SKILL.md")
        result["valid"] = False

    # ── P2: Major ────────────────────────────────────────────────────────────
    if not fm.get("license"):
        result["p2_warnings"].append("license_present: no 'license' field")

    if not fm.get("steward"):
        result["p2_warnings"].append("steward_present: no 'steward' field")

    if not fm.get("version"):
        result["p2_warnings"].append("version_present: no 'version' field")

    desc_lower = desc.lower()
    if not any(w in desc_lower for w in ["do not use", "don't use", "not for"]):
        result["p2_warnings"].append("negative_triggers: description lacks 'do not use'")

    if "## Validation Gates" not in text:
        result["p2_warnings"].append("validation_gates: no '## Validation Gates' section")

    if "## Do not use" not in text:
        result["p2_warnings"].append("do_not_use_section: no '## Do not use' section")

    if not (skill_path / "references").is_dir():
        result["p2_warnings"].append("references_dir: references/ directory missing")

    if not (skill_path / "scripts").is_dir():
        result["p2_warnings"].append("scripts_dir: scripts/ directory missing")

    if body_lines > 500:
        result["p2_warnings"].append(f"body_under_500_lines: {body_lines} lines > 500")

    # ── P3: Minor / Info ─────────────────────────────────────────────────────
    if not fm.get("origin_architect"):
        result["p3_info"].append("origin_architect: not set")

    if not fm.get("epistemic_class"):
        result["p3_info"].append("epistemic_class: not set")

    if not fm.get("rscf_state"):
        result["p3_info"].append("rscf_state: not set")

    if not fm.get("hml_level"):
        result["p3_info"].append("hml_level: not set")

    if not fm.get("tags"):
        result["p3_info"].append("tags_present: not set")

    return result


def validate_all(skills_dir: Path, exclude_prefix: str = "00_") -> list[dict]:
    """Validate all skill directories."""
    results = []
    for sd in sorted(skills_dir.iterdir()):
        if not sd.is_dir():
            continue
        if sd.name.startswith(exclude_prefix):
            continue
        if not (sd / "SKILL.md").exists():
            continue
        results.append(validate_skill(sd))
    return results


def generate_manifest(skills_dir: Path, exclude_prefix: str = "00_") -> dict:
    """Generate a MANIFEST.yaml structure with file hashes."""
    manifest = {
        "description": "AMOS Skill Bundle Manifest — file inventory with SHA-256 hashes",
        "skills": [],
    }
    for sd in sorted(skills_dir.iterdir()):
        if not sd.is_dir() or sd.name.startswith(exclude_prefix):
            continue
        sm = sd / "SKILL.md"
        if not sm.exists():
            continue
        skill_entry = {
            "name": sd.name,
            "files": [],
        }
        for f in sorted(sd.rglob("*")):
            if f.is_file() and ".git" not in str(f):
                skill_entry["files"].append({
                    "path": str(f.relative_to(sd)),
                    "hash": sha256_file(f),
                })
        manifest["skills"].append(skill_entry)
    return manifest


# ── CLI ──────────────────────────────────────────────────────────────────────

def print_result(r: dict):
    status = "PASS" if r["valid"] and not r["p2_warnings"] else "FAIL" if not r["valid"] else "WARN"
    color = "\033[92m" if status == "PASS" else "\033[91m" if status == "FAIL" else "\033[93m"
    reset = "\033[0m"
    print(f"  {color}{status}{reset} {r['skill']}")
    for e in r["p1_errors"]:
        print(f"    \033[91mP1\033[0m {e}")
    for w in r["p2_warnings"]:
        print(f"    \033[93mP2\033[0m {w}")


def main():
    parser = argparse.ArgumentParser(description="AMOS Skill Validator")
    parser.add_argument("path", nargs="?", default=None, help="Specific skill dir to validate")
    parser.add_argument("--skills-dir", default=".devin/skills", help="Skills directory")
    parser.add_argument("--json", action="store_true", help="JSON output for CI")
    parser.add_argument("--manifest", action="store_true", help="Generate MANIFEST.yaml")
    parser.add_argument("--exclude-prefix", default="00_", help="Exclude dirs starting with this")
    args = parser.parse_args()

    skills_dir = Path(args.skills_dir)

    if args.manifest:
        manifest = generate_manifest(skills_dir, args.exclude_prefix)
        print(yaml.dump(manifest, default_flow_style=False, allow_unicode=True, sort_keys=False))
        return

    if args.path:
        results = [validate_skill(Path(args.path))]
    else:
        results = validate_all(skills_dir, args.exclude_prefix)

    if args.json:
        json.dump(results, sys.stdout, indent=2)
        print()
    else:
        total = len(results)
        passed = sum(1 for r in results if r["valid"] and not r["p2_warnings"])
        warned = sum(1 for r in results if r["valid"] and r["p2_warnings"])
        failed = sum(1 for r in results if not r["valid"])

        for r in results:
            print_result(r)

        print(f"\n{'='*60}")
        print(f"  Total: {total} | PASS: {passed} | WARN: {warned} | FAIL: {failed}")
        print(f"  P1 errors: {sum(len(r['p1_errors']) for r in results)}")
        print(f"  P2 warnings: {sum(len(r['p2_warnings']) for r in results)}")
        print(f"  P3 info: {sum(len(r['p3_info']) for r in results)}")

    sys.exit(1 if any(not r["valid"] for r in results) else 0)


if __name__ == "__main__":
    main()
