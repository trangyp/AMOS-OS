#!/usr/bin/env python3
"""
AMOS Skill Evaluation Harness — Generate eval cases, rubrics, and regression
test scaffolding for agent skills.

Inspired by SOTA repos:
  - gcamilo/skill-eval: 3-tier rubric (Process/Output/Decision), programmatic checkers
  - dileepkpandiya/skilleval: Blind A/B testing, randomized judge, CI gating
  - adewale/skill-eval-harness: Causal lift, answer-key-safe grading, leakage detection
  - TiesPetersen/SkillBenchmark: Blind judge, confidence intervals, prompt-blind rubric
  - cskwork/skill-ab-eval: Skill-lift table, harness leaderboard

Generates per-skill:
  1. evals.yaml — eval cases with assertions and rubric criteria
  2. rubric.yaml — 3-tier scoring rubric (T1 Process, T2 Output, T3 Decision)
  3. regression-tests.yaml — trap scenarios and happy-path cases
  4. CI gate config — --fail-below and --fail-if-hurt thresholds

Usage:
  python3 scripts/skill_eval_harness.py                    # generate eval scaffolding for all skills
  python3 scripts/skill_eval_harness.py --skill amos-foo   # single skill
  python3 scripts/skill_eval_harness.py --json             # JSON output
  python3 scripts/skill_eval_harness.py --summary          # summary only
"""

import argparse
import hashlib
import json
import re
import sys
import time
from pathlib import Path

try:
    import yaml
except ImportError:
    print("ERROR: PyYAML required. Install: pip install pyyaml", file=sys.stderr)
    sys.exit(2)


# ── Rubric Templates (per gcamilo/skill-eval 3-tier pattern) ─────────────────

RUBRIC_TEMPLATE = {
    "tiers": {
        "T1_process_discipline": {
            "description": "What the skill uniquely adds (hard gates, evidence labeling, framework discipline)",
            "criteria": {
                "hard_gate": {
                    "description": "First 25% of output contains assumption/scope statements",
                    "weight": 2.0,
                    "score_range": [1, 10],
                    "anchored_descriptors": {
                        1: "No assumptions or scope declared",
                        5: "Some assumptions stated but incomplete",
                        10: "Clear assumptions and scope in first 25%",
                    },
                },
                "evidence_labeling": {
                    "description": "Output uses epistemic labels (SOURCE_CLAIM, DERIVED, AMOS_MODEL, etc.)",
                    "weight": 2.0,
                    "score_range": [1, 10],
                    "anchored_descriptors": {
                        1: "No epistemic labels",
                        5: "Some labels but inconsistent",
                        10: "Consistent epistemic labeling throughout",
                    },
                },
                "framework_discipline": {
                    "description": "Output follows the skill's defined framework/pipeline",
                    "weight": 1.5,
                    "score_range": [1, 10],
                    "anchored_descriptors": {
                        1: "Framework not followed",
                        5: "Partial framework adherence",
                        10: "Full framework discipline",
                    },
                },
                "devils_advocate": {
                    "description": "Output includes counter-arguments or risk sections",
                    "weight": 1.0,
                    "score_range": [1, 10],
                    "anchored_descriptors": {
                        1: "No counter-arguments",
                        5: "Weak risk mention",
                        10: "Thorough devil's advocate section",
                    },
                },
            },
        },
        "T2_output_quality": {
            "description": "Generic quality any good LLM achieves (structure, evidence, actionability)",
            "criteria": {
                "structure_mece": {
                    "description": "Output is well-structured and MECE",
                    "weight": 1.5,
                    "score_range": [1, 10],
                },
                "evidence_depth": {
                    "description": "Output has sufficient evidence and detail",
                    "weight": 1.5,
                    "score_range": [1, 10],
                },
                "actionability": {
                    "description": "Output is actionable and practical",
                    "weight": 1.0,
                    "score_range": [1, 10],
                },
                "completeness": {
                    "description": "Output covers all aspects of the task",
                    "weight": 1.0,
                    "score_range": [1, 10],
                },
            },
        },
        "T3_decision_quality": {
            "description": "Would you act on this? (anti-circularity guard)",
            "criteria": {
                "decision_quality": {
                    "description": "Output leads to a clear, actionable decision",
                    "weight": 2.0,
                    "score_range": [1, 10],
                    "anchored_descriptors": {
                        1: "Circular or vague — no decision possible",
                        5: "Some direction but unclear",
                        10: "Clear, well-reasoned decision",
                    },
                },
            },
        },
    },
    "scoring": {
        "tier_weights": {"T1_process_discipline": 0.5, "T2_output_quality": 0.3, "T3_decision_quality": 0.2},
        "overall_formula": "weighted_average(tier_scores)",
        "pass_threshold": 6.0,
        "ship_threshold": 8.0,
    },
}


# ── Programmatic Checkers (per gcamilo/skill-eval pattern) ──────────────────

CHECKERS = [
    {
        "id": "evidence_labels",
        "description": "Count epistemic state labels in output",
        "type": "regex_count",
        "patterns": [r"\[SOURCE_CLAIM\]", r"\[DERIVED\]", r"\[AMOS_MODEL\]", r"\[OBSERVATION\]", r"\[CONDITIONAL\]"],
        "constraint": "if count == 0, evidence_labeling cannot score above 4",
    },
    {
        "id": "hard_gate",
        "description": "Check first 25% of text for assumption/scope statements",
        "type": "text_search",
        "patterns": [r"assumption", r"scope", r"boundary", r"constraint", r"precondition"],
        "constraint": "if not found in first 25%, hard_gate cannot score above 4",
    },
    {
        "id": "devils_advocate",
        "description": "Detect counter-argument or risk sections",
        "type": "text_search",
        "patterns": [r"counter[- ]?argument", r"risk", r"downside", r"however", r"on the other hand", r"caveat"],
        "constraint": "if not found, devils_advocate cannot score above 4",
    },
    {
        "id": "framework_count",
        "description": "Count distinct frameworks mentioned",
        "type": "regex_count",
        "patterns": [r"RSCF", r"GMEF", r"QFM", r"HML", r"MECE", r"Trang", r"UBCAR"],
        "constraint": "if count == 0, framework_discipline cannot score above 4",
    },
    {
        "id": "provenance",
        "description": "Check for provenance/source recording",
        "type": "text_search",
        "patterns": [r"source:", r"provenance:", r"origin:", r"reference:"],
        "constraint": "if not found, provenance scoring penalty",
    },
    {
        "id": "confidence_ceiling",
        "description": "Check for confidence declaration",
        "type": "text_search",
        "patterns": [r"confidence", r"certainty", r"epistemic state"],
        "constraint": "if not found, confidence_ceiling warning",
    },
]


# ── Eval Case Generator ─────────────────────────────────────────────────────

def parse_frontmatter(text: str) -> dict:
    """Extract YAML frontmatter from markdown."""
    if not text.startswith("---"):
        return {}
    parts = text.split("---", 2)
    if len(parts) < 3:
        return {}
    try:
        fm = yaml.safe_load(parts[1])
        return fm if isinstance(fm, dict) else {}
    except yaml.YAMLError:
        return {}


def generate_eval_cases(skill_name: str, fm: dict, body: str) -> list[dict]:
    """Generate eval cases for a skill based on its metadata."""
    cases = []

    # Happy path case
    cases.append({
        "id": f"{skill_name}-happy-path",
        "type": "happy_path",
        "description": f"Standard task within {skill_name} scope",
        "task": f"Use {skill_name} to perform its primary capability",
        "assertions": {
            "must_contain": ["assumption", "scope"],
            "must_not_contain": ["I cannot", "I'm unable", "outside my scope"],
            "min_length": 200,
            "max_length": 50000,
        },
        "rubric": "standard",
        "runs": 3,
        "cost_limit": 0.50,
    })

    # Trap scenario (per skillprobe pattern)
    cases.append({
        "id": f"{skill_name}-trap-out-of-scope",
        "type": "trap",
        "description": f"Task outside {skill_name} scope — skill should refuse or redirect",
        "task": f"Use {skill_name} for a task completely outside its domain",
        "assertions": {
            "must_contain_any": ["outside", "scope", "not applicable", "different skill", "cannot"],
            "must_not_contain": ["here is the result", "I'll do this"],
        },
        "rubric": "refusal_quality",
        "runs": 2,
        "cost_limit": 0.30,
    })

    # Edge case
    cases.append({
        "id": f"{skill_name}-edge-ambiguous",
        "type": "edge_case",
        "description": f"Ambiguous input that requires {skill_name} to clarify",
        "task": f"Give {skill_name} an ambiguous request requiring clarification",
        "assertions": {
            "must_contain_any": ["clarify", "ambiguous", "need more", "specify", "which"],
            "min_length": 50,
        },
        "rubric": "standard",
        "runs": 2,
        "cost_limit": 0.30,
    })

    # Epistemic discipline case (AMOS-specific)
    cases.append({
        "id": f"{skill_name}-epistemic-labels",
        "type": "epistemic_check",
        "description": f"Verify {skill_name} uses epistemic state labels",
        "task": f"Ask {skill_name} to analyze something requiring evidence classification",
        "assertions": {
            "must_contain_any": ["SOURCE_CLAIM", "DERIVED", "AMOS_MODEL", "OBSERVATION", "CONDITIONAL"],
            "regex_match": r"\[(SOURCE_CLAIM|DERIVED|AMOS_MODEL|OBSERVATION|CONDITIONAL)\]",
        },
        "rubric": "epistemic",
        "runs": 2,
        "cost_limit": 0.30,
    })

    return cases


def generate_eval_scaffolding(skill_dir: Path) -> dict:
    """Generate complete eval scaffolding for a skill."""
    sm = skill_dir / "SKILL.md"
    if not sm.exists():
        return None

    text = sm.read_text(encoding="utf-8", errors="replace")
    fm = parse_frontmatter(text)
    name = fm.get("name", skill_dir.name)

    evals = generate_eval_cases(name, fm, text)

    return {
        "skill_name": name,
        "version": fm.get("version", "unknown"),
        "schema_version": fm.get("schema_version", "unknown"),
        "evals": evals,
        "rubric": RUBRIC_TEMPLATE,
        "checkers": CHECKERS,
        "ci_gates": {
            "fail_below": 6.0,
            "fail_if_hurt_pct": 20,
            "min_confidence": "MEDIUM",
            "runs_for_confidence": 3,
        },
        "generated_at": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
    }


# ── CLI ──────────────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(description="AMOS Skill Evaluation Harness Generator")
    parser.add_argument("--skills-dir", default=".devin/skills", help="Skills directory")
    parser.add_argument("--skill", default=None, help="Generate for a single skill")
    parser.add_argument("--json", action="store_true", help="JSON output")
    parser.add_argument("--summary", action="store_true", help="Summary only (no per-skill details)")
    parser.add_argument("--output-dir", default=None, help="Output directory for eval files")
    args = parser.parse_args()

    skills_dir = Path(args.skills_dir)
    output_dir = Path(args.output_dir) if args.output_dir else None

    if args.skill:
        sd = skills_dir / args.skill
        if not sd.exists():
            print(f"ERROR: Skill {args.skill} not found", file=sys.stderr)
            sys.exit(1)
        scaffolding = generate_eval_scaffolding(sd)
        if args.json:
            json.dump(scaffolding, sys.stdout, indent=2)
            print()
        else:
            print(f"=== Eval Scaffolding: {scaffolding['skill_name']} ===")
            print(f"  Version:       {scaffolding['version']}")
            print(f"  Eval cases:    {len(scaffolding['evals'])}")
            print(f"  Checkers:      {len(scaffolding['checkers'])}")
            print(f"  CI gates:      fail_below={scaffolding['ci_gates']['fail_below']}")
            print()
            for ev in scaffolding["evals"]:
                print(f"  [{ev['type']}] {ev['id']}")
                print(f"    {ev['description']}")
                print(f"    Assertions: {len(ev['assertions'])} checks")
                print(f"    Runs: {ev['runs']}, Cost limit: ${ev['cost_limit']}")
            print()
            print(f"  Rubric Tiers:")
            for tier_name, tier in scaffolding["rubric"]["tiers"].items():
                print(f"    {tier_name}: {len(tier['criteria'])} criteria")
            print()
            print(f"  Programmatic Checkers:")
            for chk in scaffolding["checkers"]:
                print(f"    {chk['id']}: {chk['description']}")

        if output_dir:
            out = output_dir / args.skill / "evals.yaml"
            out.parent.mkdir(parents=True, exist_ok=True)
            out.write_text(yaml.dump(scaffolding, default_flow_style=False, sort_keys=True), encoding="utf-8")
            print(f"\n  Written to: {out}")
        return

    # All skills
    all_scaffolding = {}
    for sd in sorted(skills_dir.iterdir()):
        if not sd.is_dir() or sd.name.startswith("00_"):
            continue
        scaffolding = generate_eval_scaffolding(sd)
        if scaffolding:
            all_scaffolding[scaffolding["skill_name"]] = scaffolding

    if args.json:
        json.dump(all_scaffolding, sys.stdout, indent=2)
        print()
    elif args.summary:
        print(f"=== Eval Harness Summary ===")
        print(f"  Total skills:     {len(all_scaffolding)}")
        print(f"  Total eval cases: {sum(len(s['evals']) for s in all_scaffolding.values())}")
        print(f"  Total checkers:   {len(CHECKERS)} (shared across all skills)")
        print(f"  Rubric tiers:     {len(RUBRIC_TEMPLATE['tiers'])}")
        print()
        # Count by eval type
        type_counts = {}
        for s in all_scaffolding.values():
            for ev in s["evals"]:
                type_counts[ev["type"]] = type_counts.get(ev["type"], 0) + 1
        print(f"  Eval case types:")
        for t, c in sorted(type_counts.items()):
            print(f"    {t:20s}: {c}")
        print()
        # Total cost estimate
        total_cost = sum(ev["cost_limit"] * ev["runs"] for s in all_scaffolding.values() for ev in s["evals"])
        print(f"  Total cost estimate: ${total_cost:.2f}")
    else:
        print(f"=== Eval Harness Generation ===")
        print(f"  Total skills:     {len(all_scaffolding)}")
        print(f"  Total eval cases: {sum(len(s['evals']) for s in all_scaffolding.values())}")
        print()
        for name, s in list(all_scaffolding.items())[:10]:
            print(f"  {name}: {len(s['evals'])} cases")
        if len(all_scaffolding) > 10:
            print(f"  ... and {len(all_scaffolding) - 10} more")

    if output_dir:
        for name, s in all_scaffolding.items():
            out = output_dir / name / "evals.yaml"
            out.parent.mkdir(parents=True, exist_ok=True)
            out.write_text(yaml.dump(s, default_flow_style=False, sort_keys=True), encoding="utf-8")
        print(f"\n  Written {len(all_scaffolding)} eval files to {output_dir}")


if __name__ == "__main__":
    main()
