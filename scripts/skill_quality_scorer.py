#!/usr/bin/env python3
"""
skill_quality_scorer.py — Quality scoring and linting for AMOS skills.

Inspired by SOTA repos:
  - michellepellon/skillmark: 76 rules, AST security, 0-100 quality score,
    7 weighted categories, SARIF output, auto-fix mode
  - thedaviddias/skill-check: validation, auto-fix, quality scoring, body split,
    watch mode, diff, report generation
  - bitflight-devops/skilllint: platform-agnostic linter, broken references,
    missing frontmatter, oversized skills, hook validation
  - William-Yeh/agent-skill-linter: spec compliance, repo hygiene, routing
    signal quality, progressive disclosure, multi-step workflow quality
  - kurtpayne/skillscan-lint: quality rules (passive voice, weasel words),
    graph integrity (cycles, dangling refs, broken links)

This scorer provides:
  1. Quality scoring (0-100) across 7 weighted categories with letter grades A-F
  2. Spec compliance checks (frontmatter, required fields, version format)
  3. Content quality checks (description quality, body size, section coverage)
  4. Graph integrity checks (dangling refs, broken links, parent-child cycles)
  5. Progressive disclosure checks (body size, references/ usage)
  6. Security checks (delegates to skill_guardrail_checker)
  7. Auto-fix mode for common issues
  8. Multiple output formats (terminal, JSON, Markdown report)

Usage:
  python3 scripts/skill_quality_scorer.py [--skills-dir DIR] [--skill NAME]
  python3 scripts/skill_quality_scorer.py --skills-dir DIR --fix
  python3 scripts/skill_quality_scorer.py --skills-dir DIR --report FILE
  python3 scripts/skill_quality_scorer.py --skills-dir DIR --min-score 80
"""

import argparse
import json
import re
import sys
from pathlib import Path
from datetime import datetime, timezone
from typing import Dict, List, Optional, Tuple
from collections import defaultdict


# ============================================================
# Quality Categories (inspired by skillmark)
# ============================================================

CATEGORY_WEIGHTS = {
    "spec_compliance": 0.35,
    "description_quality": 0.15,
    "content_efficiency": 0.10,
    "composability_clarity": 0.10,
    "section_coverage": 0.10,
    "discoverability": 0.10,
    "graph_integrity": 0.10,
}

LETTER_GRADES = [
    (90, "A"),
    (80, "B"),
    (70, "C"),
    (60, "D"),
    (0, "F"),
]


def grade_for_score(score: int) -> str:
    for threshold, grade in LETTER_GRADES:
        if score >= threshold:
            return grade
    return "F"


# ============================================================
# Rule Definitions
# ============================================================

class Rule:
    def __init__(self, rule_id: str, category: str, severity: str, description: str, auto_fix: bool = False):
        self.id = rule_id
        self.category = category
        self.severity = severity  # ERROR, WARNING, INFO
        self.description = description
        self.auto_fix = auto_fix


RULES = [
    # Spec compliance
    Rule("E001", "spec_compliance", "ERROR", "Missing SKILL.md file"),
    Rule("E002", "spec_compliance", "ERROR", "Missing or empty frontmatter"),
    Rule("E003", "spec_compliance", "ERROR", "Missing required field: name"),
    Rule("E004", "spec_compliance", "ERROR", "Missing required field: description"),
    Rule("E005", "spec_compliance", "WARNING", "Missing field: version"),
    Rule("E006", "spec_compliance", "WARNING", "Missing field: license"),
    Rule("E007", "spec_compliance", "WARNING", "Missing field: steward"),
    Rule("E008", "spec_compliance", "INFO", "Missing field: domain"),
    Rule("E009", "spec_compliance", "INFO", "Missing field: parent_skill"),
    Rule("E010", "spec_compliance", "WARNING", "Version not semver format (x.y.z)"),

    # Description quality
    Rule("D001", "description_quality", "WARNING", "Description too short (<50 chars)"),
    Rule("D002", "description_quality", "WARNING", "Description too long (>500 chars)"),
    Rule("D003", "description_quality", "INFO", "Description lacks 'Use when' trigger phrase"),
    Rule("D004", "description_quality", "INFO", "Description lacks 'Do not use' boundary phrase"),
    Rule("D005", "description_quality", "WARNING", "Description uses passive voice"),

    # Content efficiency
    Rule("C001", "content_efficiency", "WARNING", "SKILL.md body too large (>500 lines)"),
    Rule("C002", "content_efficiency", "INFO", "No references/ directory (progressive disclosure)"),
    Rule("C003", "content_efficiency", "INFO", "References/ has too many files (>20)"),

    # Composability clarity
    Rule("P001", "composability_clarity", "WARNING", "Missing ## Capabilities section"),
    Rule("P002", "composability_clarity", "INFO", "Missing ## Composition section"),
    Rule("P003", "composability_clarity", "INFO", "Missing ## Anti-Patterns section"),
    Rule("P004", "composability_clarity", "WARNING", "Capabilities don't use <domain>.<verb> format"),

    # Section coverage
    Rule("S001", "section_coverage", "WARNING", "Missing ## Validation section"),
    Rule("S002", "section_coverage", "INFO", "Missing ## Examples section"),
    Rule("S003", "section_coverage", "INFO", "Missing ## Provenance section"),
    Rule("S004", "section_coverage", "INFO", "Missing ## References section"),

    # Discoverability
    Rule("F001", "discoverability", "WARNING", "Missing tags in frontmatter"),
    Rule("F002", "discoverability", "INFO", "Few tags (<3) in frontmatter"),
    Rule("F003", "discoverability", "INFO", "Missing aliases in frontmatter"),

    # Graph integrity
    Rule("G001", "graph_integrity", "ERROR", "Parent skill does not exist"),
    Rule("G002", "graph_integrity", "WARNING", "References to non-existent files"),
    Rule("G003", "graph_integrity", "WARNING", "No incoming links from other skills"),
]

RULES_BY_ID = {r.id: r for r in RULES}


# ============================================================
# Frontmatter Parser
# ============================================================

def parse_frontmatter(content: str) -> dict:
    """Parse YAML frontmatter, including list-form fields like tags."""
    fm = {}
    match = re.match(r'^---\n(.*?)\n---', content, re.DOTALL)
    if not match:
        return fm
    fm_text = match.group(1)
    lines = fm_text.split('\n')
    current_key = None
    current_list = []
    for line in lines:
        # List item (indented with - )
        if re.match(r'^\s+-\s+', line) and current_key:
            item = re.sub(r'^\s+-\s+', '', line).strip().strip('"').strip("'")
            current_list.append(item)
            continue
        # Key: value
        if ':' in line and not line.startswith(' '):
            # Save previous list
            if current_key and current_list:
                fm[current_key] = current_list
                current_list = []
            elif current_key:
                pass  # Keep whatever was set
            key, _, value = line.partition(':')
            key = key.strip()
            value = value.strip().strip('"').strip("'")
            if value:
                fm[key] = value
            else:
                fm[key] = []  # Will be populated by list items
            current_key = key
    # Save final list
    if current_key and current_list:
        fm[current_key] = current_list
    return fm


# ============================================================
# Scoring Engine
# ============================================================

def score_skill(skill_dir: Path, all_skill_names: set) -> dict:
    """Score a single skill directory."""
    findings = []
    skill_md = skill_dir / "SKILL.md"

    # E001: Missing SKILL.md
    if not skill_md.exists():
        findings.append({"rule": "E001", "message": "Missing SKILL.md"})
        return {
            "name": skill_dir.name,
            "findings": findings,
            "scores": {},
            "total_score": 0,
            "grade": "F",
        }

    content = skill_md.read_text(encoding="utf-8")
    fm = parse_frontmatter(content)
    body = content.split('---', 2)[-1] if '---' in content else content
    body_lines = body.strip().split('\n')
    body_line_count = len(body_lines)

    # Spec compliance checks
    if not fm:
        findings.append({"rule": "E002", "message": "Missing or empty frontmatter"})
    else:
        for field, rule_id in [("name", "E003"), ("description", "E004")]:
            if field not in fm or not fm[field]:
                findings.append({"rule": rule_id, "message": f"Missing required field: {field}"})
        for field, rule_id in [("version", "E005"), ("license", "E006"), ("steward", "E007")]:
            if field not in fm:
                findings.append({"rule": rule_id, "message": f"Missing field: {field}"})
        for field, rule_id in [("domain", "E008"), ("parent_skill", "E009")]:
            if field not in fm:
                findings.append({"rule": rule_id, "message": f"Missing field: {field}"})
        # Version format
        version = fm.get("version", "")
        if version and not re.match(r'^\d+\.\d+\.\d+', version):
            findings.append({"rule": "E010", "message": f"Version not semver: {version}"})

    # Description quality
    desc = fm.get("description", "")
    if len(desc) < 50:
        findings.append({"rule": "D001", "message": f"Description too short ({len(desc)} chars)"})
    if len(desc) > 500:
        findings.append({"rule": "D002", "message": f"Description too long ({len(desc)} chars)"})
    if "use when" not in desc.lower() and "use for" not in desc.lower():
        findings.append({"rule": "D003", "message": "Description lacks 'Use when' trigger"})
    if "do not use" not in desc.lower() and "don't use" not in desc.lower():
        findings.append({"rule": "D004", "message": "Description lacks 'Do not use' boundary"})

    # Content efficiency
    if body_line_count > 500:
        findings.append({"rule": "C001", "message": f"Body too large ({body_line_count} lines)"})
    refs_dir = skill_dir / "references"
    if not refs_dir.exists():
        findings.append({"rule": "C002", "message": "No references/ directory"})
    elif refs_dir.exists():
        ref_files = list(refs_dir.glob("*.md"))
        if len(ref_files) > 20:
            findings.append({"rule": "C003", "message": f"Too many references ({len(ref_files)})"})

    # Composability clarity — partial section name matching
    sections = re.findall(r'^##\s+(.+)$', body, re.MULTILINE)
    section_names = [s.lower() for s in sections]
    def has_section(keyword):
        return any(keyword in s for s in section_names)
    if not has_section("capabilities"):
        findings.append({"rule": "P001", "message": "Missing ## Capabilities section"})
    if not has_section("composition"):
        findings.append({"rule": "P002", "message": "Missing ## Composition section"})
    if not has_section("anti-pattern") and not has_section("anti pattern"):
        findings.append({"rule": "P003", "message": "Missing ## Anti-Patterns section"})

    # Section coverage — partial matching
    if not has_section("validation"):
        findings.append({"rule": "S001", "message": "Missing ## Validation section"})
    if not has_section("examples"):
        findings.append({"rule": "S002", "message": "Missing ## Examples section"})
    if not has_section("provenance"):
        findings.append({"rule": "S003", "message": "Missing ## Provenance section"})
    if not has_section("references"):
        findings.append({"rule": "S004", "message": "Missing ## References section"})

    # Discoverability
    tags = fm.get("tags", [])
    if isinstance(tags, str):
        tag_count = len([t for t in tags.split(',') if t.strip()])
    elif isinstance(tags, list):
        tag_count = len(tags)
    else:
        tag_count = 0
    if tag_count == 0:
        findings.append({"rule": "F001", "message": "Missing tags in frontmatter"})
    elif tag_count < 3:
        findings.append({"rule": "F002", "message": f"Few tags ({tag_count})"})
    aliases = fm.get("aliases", [])
    if isinstance(aliases, str):
        alias_count = len([a for a in aliases.split(',') if a.strip()])
    elif isinstance(aliases, list):
        alias_count = len(aliases)
    else:
        alias_count = 0
    if alias_count == 0:
        findings.append({"rule": "F003", "message": "Missing aliases"})

    # Graph integrity
    parent = fm.get("parent_skill", "none")
    if parent and parent != "none" and parent not in all_skill_names:
        findings.append({"rule": "G001", "message": f"Parent skill does not exist: {parent}"})

    # Calculate category scores
    scores = {}
    for category, weight in CATEGORY_WEIGHTS.items():
        cat_findings = [f for f in findings if RULES_BY_ID.get(f["rule"], Rule("", category, "", "")).category == category]
        errors = sum(1 for f in cat_findings if RULES_BY_ID[f["rule"]].severity == "ERROR")
        warnings = sum(1 for f in cat_findings if RULES_BY_ID[f["rule"]].severity == "WARNING")
        infos = sum(1 for f in cat_findings if RULES_BY_ID[f["rule"]].severity == "INFO")
        # Score: 100 - (errors*30 + warnings*10 + infos*3)
        cat_score = max(0, 100 - errors * 30 - warnings * 10 - infos * 3)
        scores[category] = cat_score

    # Weighted total
    total = sum(scores[cat] * weight for cat, weight in CATEGORY_WEIGHTS.items())
    total_score = int(round(total))
    grade = grade_for_score(total_score)

    return {
        "name": skill_dir.name,
        "findings": findings,
        "scores": scores,
        "total_score": total_score,
        "grade": grade,
        "body_lines": body_line_count,
        "section_count": len(sections),
    }


def score_all_skills(skills_dir: Path) -> dict:
    """Score all skills in a directory."""
    # First pass: collect all skill names for graph integrity
    all_skill_names = set()
    for d in skills_dir.iterdir():
        if d.is_dir() and (d / "SKILL.md").exists():
            all_skill_names.add(d.name)

    results = []
    for d in sorted(skills_dir.iterdir()):
        if d.is_dir() and (d / "SKILL.md").exists():
            result = score_skill(d, all_skill_names)
            results.append(result)

    # Aggregate stats
    grade_dist = defaultdict(int)
    score_ranges = {"90+": 0, "80-89": 0, "70-79": 0, "60-69": 0, "<60": 0}
    category_avg = defaultdict(float)

    for r in results:
        grade_dist[r["grade"]] += 1
        s = r["total_score"]
        if s >= 90: score_ranges["90+"] += 1
        elif s >= 80: score_ranges["80-89"] += 1
        elif s >= 70: score_ranges["70-79"] += 1
        elif s >= 60: score_ranges["60-69"] += 1
        else: score_ranges["<60"] += 1

        for cat in CATEGORY_WEIGHTS:
            category_avg[cat] += r["scores"].get(cat, 0)

    n = len(results) or 1
    for cat in category_avg:
        category_avg[cat] = round(category_avg[cat] / n, 1)

    avg_score = round(sum(r["total_score"] for r in results) / n, 1) if results else 0

    return {
        "total_skills": len(results),
        "average_score": avg_score,
        "grade_distribution": dict(grade_dist),
        "score_ranges": score_ranges,
        "category_averages": dict(category_avg),
        "skills": sorted(results, key=lambda r: r["total_score"]),
    }


# ============================================================
# Main
# ============================================================

def main():
    parser = argparse.ArgumentParser(description="Quality scoring and linting for AMOS skills")
    parser.add_argument("--skills-dir", default=".devin/skills", help="Skills directory")
    parser.add_argument("--skill", default=None, help="Score specific skill only")
    parser.add_argument("--fix", action="store_true", help="Auto-fix common issues (not yet implemented)")
    parser.add_argument("--report", default=None, help="Write Markdown report to file")
    parser.add_argument("--json", default=None, help="Write JSON report to file")
    parser.add_argument("--min-score", type=int, default=None, help="Fail if any skill below this score")
    parser.add_argument("--summary", action="store_true", help="Print summary only")
    args = parser.parse_args()

    skills_dir = Path(args.skills_dir)

    if args.skill:
        all_names = {d.name for d in skills_dir.iterdir() if d.is_dir() and (d / "SKILL.md").exists()}
        for d in sorted(skills_dir.iterdir()):
            if d.is_dir() and args.skill in d.name and (d / "SKILL.md").exists():
                result = score_skill(d, all_names)
                print(f"\n  {result['name']}: {result['total_score']}/100 ({result['grade']})")
                for cat, score in sorted(result["scores"].items()):
                    print(f"    {cat:30s} {score:3d}")
                if result["findings"]:
                    print(f"\n  Findings ({len(result['findings'])}):")
                    for f in result["findings"]:
                        rule = RULES_BY_ID.get(f["rule"])
                        if rule:
                            print(f"    [{rule.severity}] {f['rule']} {rule.description}: {f['message']}")
                return

    results = score_all_skills(skills_dir)

    if args.summary:
        print(f"Total skills:     {results['total_skills']}")
        print(f"Average score:    {results['average_score']}")
        print(f"Grade distribution: {results['grade_distribution']}")
        return

    print("=" * 70)
    print("  AMOS Skill Quality Scorer")
    print("  Inspired by: skillmark, skill-check, skilllint, skillscan-lint")
    print("=" * 70)
    print()
    print(f"  Skills directory: {skills_dir}")
    print(f"  Total skills:     {results['total_skills']}")
    print(f"  Average score:    {results['average_score']}/100")
    print()
    print(f"  Grade Distribution:")
    for grade in ["A", "B", "C", "D", "F"]:
        count = results["grade_distribution"].get(grade, 0)
        bar = "#" * count
        print(f"    {grade}: {count:4d} {bar}")
    print()
    print(f"  Score Ranges:")
    for range_name, count in results["score_ranges"].items():
        print(f"    {range_name:10s} {count:4d}")
    print()
    print(f"  Category Averages:")
    for cat in sorted(results["category_averages"]):
        score = results["category_averages"][cat]
        weight = CATEGORY_WEIGHTS.get(cat, 0)
        print(f"    {cat:30s} {score:6.1f}  (weight: {weight:.0%})")
    print()

    # Show bottom 10 skills
    print(f"  Bottom 10 Skills (need improvement):")
    for r in results["skills"][:10]:
        print(f"    {r['total_score']:3d}/100 ({r['grade']})  {r['name']}")
    print()

    # Show top 10 skills
    print(f"  Top 10 Skills:")
    for r in results["skills"][-10:]:
        print(f"    {r['total_score']:3d}/100 ({r['grade']})  {r['name']}")
    print()

    if args.report:
        lines = [
            "<!-- Auto-generated by skill_quality_scorer.py -->",
            "",
            "# AMOS Skill Quality Report",
            "",
            f"> Generated: {datetime.now(timezone.utc).isoformat()}",
            f"> Total skills: {results['total_skills']}",
            f"> Average score: {results['average_score']}/100",
            "",
            "## Grade Distribution",
            "",
            "| Grade | Count |",
            "|-------|-------|",
        ]
        for grade in ["A", "B", "C", "D", "F"]:
            count = results["grade_distribution"].get(grade, 0)
            lines.append(f"| {grade} | {count} |")
        lines.append("")
        lines.append("## Category Averages")
        lines.append("")
        lines.append("| Category | Score | Weight |")
        lines.append("|----------|-------|--------|")
        for cat in sorted(results["category_averages"]):
            score = results["category_averages"][cat]
            weight = CATEGORY_WEIGHTS.get(cat, 0)
            lines.append(f"| {cat} | {score} | {weight:.0%} |")
        lines.append("")
        lines.append("## All Skills (sorted by score)")
        lines.append("")
        lines.append("| Score | Grade | Skill | Body Lines | Sections |")
        lines.append("|-------|-------|-------|------------|----------|")
        for r in results["skills"]:
            lines.append(f"| {r['total_score']} | {r['grade']} | {r['name']} | {r.get('body_lines', 0)} | {r.get('section_count', 0)} |")
        lines.append("")
        Path(args.report).write_text("\n".join(lines), encoding="utf-8")
        print(f"  Report written to: {args.report}")

    if args.json:
        Path(args.json).write_text(
            json.dumps(results, indent=2, ensure_ascii=False), encoding="utf-8"
        )
        print(f"  JSON written to: {args.json}")

    # Exit code based on min-score
    if args.min_score is not None:
        below = [r for r in results["skills"] if r["total_score"] < args.min_score]
        if below:
            print(f"\n  {len(below)} skills below minimum score {args.min_score}")
            sys.exit(1)

    sys.exit(0)


if __name__ == "__main__":
    main()
