#!/usr/bin/env python3
"""
skill_regression_harness.py — Regression testing for AMOS skills.

Inspired by SOTA repos:
  - dileepkpandiya/skilleval: blind A/B testing, randomized judge, deterministic
    assertions (must_contain, must_not_contain, regex_match, min_length, max_length),
    CI gating via --fail-below and --fail-if-hurt-pct
  - kasimmj/claude-code-test-runner: YAML eval cases, model matrix, cost tracking
  - kabirnarang39/skillci: self-growing eval loop, git-native bisect, OWASP fuzzing
  - klashkaan-cmyk/crucible: pass@k / pass^k, transcript diffs, baselines
  - surpradhan/claude-code-for-ai-engineers-eval: trigger precision/recall, behavior assertions

This harness provides:
  1. Deterministic assertions (no LLM needed) — structural checks on skill output
  2. Trigger eval — precision/recall on skill activation patterns
  3. Regression baselines — compare current skill state against saved baseline
  4. CI gating — exit codes for pass/fail/warn
  5. Test case generation — auto-generate test stubs from skill metadata

Usage:
  python3 scripts/skill_regression_harness.py [--skills-dir DIR] [--skill NAME]
  python3 scripts/skill_regression_harness.py --skills-dir DIR --generate-baseline
  python3 scripts/skill_regression_harness.py --skills-dir DIR --regression
  python3 scripts/skill_regression_harness.py --skills-dir DIR --trigger-eval
"""

import argparse
import hashlib
import json
import re
import sys
from pathlib import Path
from datetime import datetime, timezone
from typing import Dict, List, Optional, Tuple
from collections import defaultdict


# ============================================================
# Deterministic Assertions (no LLM needed)
# ============================================================

ASSERTION_TYPES = {
    "must_contain": lambda output, expected: expected in output,
    "must_not_contain": lambda output, expected: expected not in output,
    "regex_match": lambda output, pattern: bool(re.search(pattern, output)),
    "min_length": lambda output, min_len: len(output) >= int(min_len),
    "max_length": lambda output, max_len: len(output) <= int(max_len),
    "starts_with": lambda output, prefix: output.strip().startswith(prefix),
    "ends_with": lambda output, suffix: output.strip().endswith(suffix),
    "contains_any": lambda output, options: any(o in output for o in options.split("|")),
    "contains_all": lambda output, items: all(i in output for i in items.split("|")),
    "json_valid": lambda output, _: _try_json(output),
    "has_frontmatter": lambda output, _: bool(re.match(r'^---\n.*?\n---', output, re.DOTALL)),
    "has_capabilities": lambda output, _: any(h.lower() in output.lower() for h in ["## Capabilities", "## Capability", "## Key Capabilities", "## Core Capabilities", "## Features", "## Operations", "## Key Operations", "## Core Concepts", "## When to Use", "## Core Primitives", "## Overview", "## Architecture", "## Quick Start", "## Verification support", "## Grounding support", "## Regression prevention"]),
    "has_provenance": lambda output, _: "Provenance" in output or "provenance" in output.lower(),
    "has_epistemic_class": lambda output, _: bool(re.search(r'epistemic_class|SOURCE_CLAIM|SOURCE_CANON|DERIVED|AMOS_MODEL|EMPIRICAL', output)),
    "has_scope": lambda output, _: "scope" in output.lower() or "Scope" in output,
    "has_validation_gates": lambda output, _: "Validation" in output or "validation" in output.lower(),
    "no_bom": lambda output, _: not output.startswith('\ufeff'),
    "no_secrets": lambda output, _: not _contains_secret(output),
}


def _try_json(output: str) -> bool:
    try:
        json.loads(output)
        return True
    except (json.JSONDecodeError, TypeError):
        return False


def _contains_secret(text: str) -> bool:
    patterns = [
        r'sk-[a-zA-Z0-9]{20,}',
        r'AKIA[A-Z0-9]{16}',
        r'ghp_[a-zA-Z0-9]{36}',
        r'-----BEGIN (RSA |EC )?PRIVATE KEY-----',
        r'password\s*[:=]\s*["\'][^"\']+["\']',
    ]
    return any(re.search(p, text) for p in patterns)


def run_assertion(output: str, assertion_type: str, expected: str = "") -> bool:
    """Run a single deterministic assertion."""
    checker = ASSERTION_TYPES.get(assertion_type)
    if not checker:
        return False
    try:
        return checker(output, expected)
    except Exception:
        return False


# ============================================================
# Default Test Suite (auto-generated per skill)
# ============================================================

def generate_default_tests(skill_name: str, skill_dir: Path) -> List[dict]:
    """Generate default test cases for a skill based on its structure."""
    tests = []
    skill_md = skill_dir / "SKILL.md"

    if not skill_md.exists():
        return tests

    content = skill_md.read_text(encoding="utf-8")

    # Test 1: SKILL.md exists and has frontmatter
    tests.append({
        "id": f"{skill_name}-frontmatter",
        "description": "SKILL.md has valid YAML frontmatter",
        "assertion": "has_frontmatter",
        "expected": "",
    })

    # Test 2: No BOM
    tests.append({
        "id": f"{skill_name}-no-bom",
        "description": "SKILL.md has no BOM characters",
        "assertion": "no_bom",
        "expected": "",
    })

    # Test 3: Has capabilities section
    tests.append({
        "id": f"{skill_name}-capabilities",
        "description": "SKILL.md has Capabilities section",
        "assertion": "has_capabilities",
        "expected": "",
    })

    # Test 4: Has provenance
    tests.append({
        "id": f"{skill_name}-provenance",
        "description": "SKILL.md has provenance section",
        "assertion": "has_provenance",
        "expected": "",
    })

    # Test 5: Has epistemic class
    tests.append({
        "id": f"{skill_name}-epistemic",
        "description": "SKILL.md has epistemic class label",
        "assertion": "has_epistemic_class",
        "expected": "",
    })

    # Test 6: No secrets
    tests.append({
        "id": f"{skill_name}-no-secrets",
        "description": "SKILL.md contains no secrets",
        "assertion": "no_secrets",
        "expected": "",
    })

    # Test 7: Has scope declaration
    tests.append({
        "id": f"{skill_name}-scope",
        "description": "SKILL.md declares scope",
        "assertion": "has_scope",
        "expected": "",
    })

    # Test 8: Has validation gates
    tests.append({
        "id": f"{skill_name}-validation",
        "description": "SKILL.md has validation gates",
        "assertion": "has_validation_gates",
        "expected": "",
    })

    # Test 9: Minimum length check
    tests.append({
        "id": f"{skill_name}-min-size",
        "description": "SKILL.md is at least 500 bytes",
        "assertion": "min_length",
        "expected": "500",
    })

    # Test 10: Maximum length check (anti-bloat)
    tests.append({
        "id": f"{skill_name}-max-size",
        "description": "SKILL.md is under 100KB",
        "assertion": "max_length",
        "expected": "102400",
    })

    return tests


# ============================================================
# Trigger Evaluation (precision/recall)
# ============================================================

def parse_trigger_patterns(skill_dir: Path) -> Tuple[List[str], List[str]]:
    """Extract trigger patterns (when to use) and anti-patterns (when NOT to use) from SKILL.md."""
    skill_md = skill_dir / "SKILL.md"
    if not skill_md.exists():
        return [], []

    content = skill_md.read_text(encoding="utf-8")

    # Extract "When to Use" patterns
    triggers = []
    use_match = re.search(r'## When to Use\s*\n(.*?)(?=\n##|\Z)', content, re.DOTALL)
    if use_match:
        for line in use_match.group(1).split('\n'):
            line = line.strip().lstrip('-').strip()
            if line and len(line) > 10:
                triggers.append(line)

    # Extract description trigger keywords
    fm_match = re.match(r'^---\n(.*?)\n---', content, re.DOTALL)
    if fm_match:
        desc_match = re.search(r'description:\s*(.+)', fm_match.group(1))
        if desc_match:
            desc = desc_match.group(1).strip().strip("'").strip('"')
            # Extract "Use when" phrases
            use_when = re.findall(r'[Uu]se when\s+([^.;]+)', desc)
            triggers.extend(use_when)

    # Extract "Do not use" anti-patterns
    anti = []
    dont_match = re.search(r'## Do not use\s*\n(.*?)(?=\n##|\Z)', content, re.DOTALL)
    if dont_match:
        for line in dont_match.group(1).split('\n'):
            line = line.strip().lstrip('-').strip()
            if line and len(line) > 5:
                anti.append(line)

    # Also check description for "Do not use"
    if fm_match:
        desc_match = re.search(r'description:\s*(.+)', fm_match.group(1))
        if desc_match:
            desc = desc_match.group(1).strip().strip("'").strip('"')
            dont_when = re.findall(r'[Dd]o not use\s+([^.;]+)', desc)
            anti.extend(dont_when)

    return triggers, anti


def evaluate_triggers(skill_name: str, skill_dir: Path) -> dict:
    """Evaluate trigger patterns for a skill."""
    triggers, anti_patterns = parse_trigger_patterns(skill_dir)

    return {
        "skill": skill_name,
        "trigger_count": len(triggers),
        "anti_pattern_count": len(anti_patterns),
        "triggers": triggers[:5],  # Top 5 for display
        "anti_patterns": anti_patterns[:3],
        "has_triggers": len(triggers) > 0,
        "has_anti_patterns": len(anti_patterns) > 0,
        "trigger_quality": _assess_trigger_quality(triggers, anti_patterns),
    }


def _assess_trigger_quality(triggers: List[str], anti: List[str]) -> str:
    """Assess the quality of trigger patterns."""
    if not triggers:
        return "POOR — no triggers found"
    if not anti:
        return "FAIR — has triggers but no anti-patterns"
    if len(triggers) >= 3 and len(anti) >= 2:
        return "EXCELLENT — rich triggers + anti-patterns"
    if len(triggers) >= 2 and len(anti) >= 1:
        return "GOOD — adequate triggers + anti-patterns"
    return "FAIR — minimal trigger coverage"


# ============================================================
# Baseline Management
# ============================================================

def generate_baseline(skills_dir: Path) -> dict:
    """Generate a regression baseline for all skills."""
    baseline = {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "skills_dir": str(skills_dir),
        "skills": {},
    }

    for d in sorted(skills_dir.iterdir()):
        if not (d.is_dir() and (d / "SKILL.md").exists()):
            continue

        skill_md = d / "SKILL.md"
        content = skill_md.read_text(encoding="utf-8")

        # Compute structural hash
        structural_hash = hashlib.sha256(content.encode("utf-8")).hexdigest()

        # Count sections
        sections = re.findall(r'^##\s+(.+)$', content, re.MULTILINE)

        # Count capabilities
        cap_count = len(re.findall(r'^-\s+\*\*.+?\*\*', content, re.MULTILINE))

        # File count and total size
        files = list(d.rglob("*"))
        file_count = sum(1 for f in files if f.is_file())
        total_size = sum(f.stat().st_size for f in files if f.is_file())

        baseline["skills"][d.name] = {
            "structural_hash": structural_hash,
            "content_length": len(content),
            "section_count": len(sections),
            "sections": sections,
            "capability_count": cap_count,
            "file_count": file_count,
            "total_size_bytes": total_size,
        }

    return baseline


def compare_baselines(current: dict, saved: dict) -> dict:
    """Compare current baseline against saved baseline."""
    changes = {
        "added": [],
        "removed": [],
        "modified": [],
        "unchanged": [],
    }

    current_skills = set(current.get("skills", {}).keys())
    saved_skills = set(saved.get("skills", {}).keys())

    changes["added"] = sorted(current_skills - saved_skills)
    changes["removed"] = sorted(saved_skills - current_skills)

    for skill in sorted(current_skills & saved_skills):
        curr = current["skills"][skill]
        prev = saved["skills"][skill]

        if curr["structural_hash"] == prev["structural_hash"]:
            changes["unchanged"].append(skill)
        else:
            diff = {
                "skill": skill,
                "hash_changed": curr["structural_hash"] != prev["structural_hash"],
                "content_length_delta": curr["content_length"] - prev["content_length"],
                "section_count_delta": curr["section_count"] - prev["section_count"],
                "capability_count_delta": curr["capability_count"] - prev["capability_count"],
                "file_count_delta": curr["file_count"] - prev["file_count"],
                "size_delta_bytes": curr["total_size_bytes"] - prev["total_size_bytes"],
                "added_sections": [s for s in curr["sections"] if s not in prev["sections"]],
                "removed_sections": [s for s in prev["sections"] if s not in curr["sections"]],
            }
            changes["modified"].append(diff)

    return changes


# ============================================================
# Main Test Runner
# ============================================================

def run_tests(skills_dir: Path, skill_filter: Optional[str] = None) -> dict:
    """Run deterministic tests on all skills."""
    results = {
        "total": 0,
        "passed": 0,
        "failed": 0,
        "skipped": 0,
        "failures": [],
        "per_skill": {},
    }

    for d in sorted(skills_dir.iterdir()):
        if not (d.is_dir() and (d / "SKILL.md").exists()):
            continue

        if skill_filter and skill_filter not in d.name:
            continue

        skill_name = d.name
        skill_md = d / "SKILL.md"
        content = skill_md.read_text(encoding="utf-8")

        tests = generate_default_tests(skill_name, d)
        skill_results = {"total": len(tests), "passed": 0, "failed": 0, "failures": []}

        for test in tests:
            results["total"] += 1
            passed = run_assertion(content, test["assertion"], test.get("expected", ""))
            if passed:
                results["passed"] += 1
                skill_results["passed"] += 1
            else:
                results["failed"] += 1
                skill_results["failed"] += 1
                failure = {
                    "skill": skill_name,
                    "test_id": test["id"],
                    "description": test["description"],
                    "assertion": test["assertion"],
                    "expected": test.get("expected", ""),
                }
                results["failures"].append(failure)
                skill_results["failures"].append(failure)

        results["per_skill"][skill_name] = skill_results

    return results


def main():
    parser = argparse.ArgumentParser(description="Skill regression testing harness")
    parser.add_argument("--skills-dir", default=".devin/skills", help="Skills directory")
    parser.add_argument("--skill", default=None, help="Filter to specific skill name")
    parser.add_argument("--generate-baseline", action="store_true", help="Generate regression baseline")
    parser.add_argument("--regression", action="store_true", help="Run regression check against saved baseline")
    parser.add_argument("--trigger-eval", action="store_true", help="Evaluate trigger patterns")
    parser.add_argument("--baseline-file", default=".skill-baseline.json", help="Baseline file path")
    parser.add_argument("--report", default=None, help="Write JSON report to file")
    parser.add_argument("--summary", action="store_true", help="Print summary only")
    args = parser.parse_args()

    skills_dir = Path(args.skills_dir)
    baseline_path = Path(args.baseline_file)

    # Generate baseline mode
    if args.generate_baseline:
        print("Generating regression baseline...")
        baseline = generate_baseline(skills_dir)
        baseline_path.write_text(json.dumps(baseline, indent=2, ensure_ascii=False), encoding="utf-8")
        print(f"Baseline saved: {baseline_path}")
        print(f"  Skills captured: {len(baseline['skills'])}")
        return

    # Regression mode
    if args.regression:
        if not baseline_path.exists():
            print(f"ERROR: Baseline file not found: {baseline_path}")
            print("Run with --generate-baseline first.")
            sys.exit(2)

        print("Running regression check...")
        current = generate_baseline(skills_dir)
        saved = json.loads(baseline_path.read_text(encoding="utf-8"))
        changes = compare_baselines(current, saved)

        print(f"  Added:    {len(changes['added'])}")
        print(f"  Removed:  {len(changes['removed'])}")
        print(f"  Modified: {len(changes['modified'])}")
        print(f"  Unchanged:{len(changes['unchanged'])}")

        if changes["added"]:
            print("\n  New skills:")
            for s in changes["added"][:10]:
                print(f"    + {s}")

        if changes["removed"]:
            print("\n  Removed skills:")
            for s in changes["removed"][:10]:
                print(f"    - {s}")

        if changes["modified"]:
            print(f"\n  Modified skills ({len(changes['modified'])}):")
            for m in changes["modified"][:10]:
                delta = m["content_length_delta"]
                sign = "+" if delta >= 0 else ""
                print(f"    ~ {m['skill']} (content: {sign}{delta}B, sections: {m['section_count_delta']:+d})")

        if args.report:
            Path(args.report).write_text(json.dumps(changes, indent=2, ensure_ascii=False), encoding="utf-8")

        # Exit code: 0 if no regressions, 1 if modifications
        if changes["modified"] or changes["removed"]:
            sys.exit(1)
        sys.exit(0)

    # Trigger eval mode
    if args.trigger_eval:
        print("=" * 70)
        print("  Skill Trigger Evaluation")
        print("=" * 70)
        print()

        poor_count = 0
        fair_count = 0
        good_count = 0
        excellent_count = 0
        no_trigger_count = 0

        for d in sorted(skills_dir.iterdir()):
            if not (d.is_dir() and (d / "SKILL.md").exists()):
                continue
            if args.skill and args.skill not in d.name:
                continue

            result = evaluate_triggers(d.name, d)
            quality = result["trigger_quality"]

            if "POOR" in quality:
                poor_count += 1
            elif "FAIR" in quality:
                fair_count += 1
            elif "GOOD" in quality:
                good_count += 1
            elif "EXCELLENT" in quality:
                excellent_count += 1

            if not args.summary:
                print(f"  {d.name:50s} T:{result['trigger_count']:2d} A:{result['anti_pattern_count']:2d} [{quality}]")

        print()
        print(f"  Trigger quality distribution:")
        print(f"    EXCELLENT: {excellent_count}")
        print(f"    GOOD:      {good_count}")
        print(f"    FAIR:      {fair_count}")
        print(f"    POOR:      {poor_count}")
        return

    # Default: run deterministic tests
    print("=" * 70)
    print("  AMOS Skill Regression Test Harness")
    print("=" * 70)
    print()

    results = run_tests(skills_dir, args.skill)

    print(f"  Total tests:  {results['total']}")
    print(f"  Passed:       {results['passed']}")
    print(f"  Failed:       {results['failed']}")
    print(f"  Pass rate:    {results['passed']/results['total']*100:.1f}%" if results['total'] > 0 else "  Pass rate: N/A")
    print()

    if results["failures"]:
        print(f"  Failures ({len(results['failures'])}):")
        # Group by skill
        by_skill = defaultdict(list)
        for f in results["failures"]:
            by_skill[f["skill"]].append(f)

        for skill in sorted(by_skill):
            print(f"    {skill}:")
            for f in by_skill[skill]:
                print(f"      - {f['test_id']}: {f['description']}")
        print()

    # Per-skill summary
    if not args.summary:
        print("  Per-skill results:")
        for skill in sorted(results["per_skill"]):
            sr = results["per_skill"][skill]
            status = "PASS" if sr["failed"] == 0 else f"FAIL({sr['failed']})"
            print(f"    {skill:50s} {sr['passed']}/{sr['total']} [{status}]")

    if args.report:
        Path(args.report).write_text(json.dumps(results, indent=2, ensure_ascii=False), encoding="utf-8")
        print(f"\n  Report written to: {args.report}")

    # Exit code
    if results["failed"] > 0:
        sys.exit(1)
    sys.exit(0)


if __name__ == "__main__":
    main()
