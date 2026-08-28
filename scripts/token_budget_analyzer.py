#!/usr/bin/env python3
"""
AMOS Token Budget Analyzer — Progressive disclosure, context window optimization,
and skill loading budget management.

Inspired by SOTA repos:
  - mirasoth/soothe RFC-105: Budgeted metadata listing (1% context cap), delta-only
  - muratcankoylan/Agent-Skills-for-Context-Engineering: Progressive disclosure
  - jacob-balslev/skill-graph: Zone budgets, 80% compaction rule, persistence hierarchy
  - pjt222/agent-almanac: Token budget management with pruning and progressive disclosure
  - liux297/skill_agent: Skill progressive disclosure with context compression

Analyzes:
  1. Per-skill token cost (frontmatter + body + references + scripts)
  2. Total catalog token cost if all skills loaded at once
  3. Progressive disclosure savings (metadata-only vs full-load)
  4. Context zone allocation (system / skill-injection / working / output)
  5. Skills exceeding per-entry token cap (250 chars per soothe RFC-105)
  6. Skills exceeding body length thresholds (L1/L2/L3 progressive loading)

Usage:
  python3 scripts/token_budget_analyzer.py                    # full analysis
  python3 scripts/token_budget_analyzer.py --json              # JSON output
  python3 scripts/token_budget_analyzer.py --skill amos-foo    # single skill
  python3 scripts/token_budget_analyzer.py --top 20            # top 20 by cost
  python3 scripts/token_budget_analyzer.py --zones             # zone allocation
"""

import argparse
import json
import math
import re
import sys
from pathlib import Path

try:
    import yaml
except ImportError:
    print("ERROR: PyYAML required. Install: pip install pyyaml", file=sys.stderr)
    sys.exit(2)


# ── Token Estimation ─────────────────────────────────────────────────────────

# Approximate tokens-per-character ratio for mixed Markdown/YAML content
# Claude tokenizer: ~4 chars per token for English, ~3 for code-heavy
CHARS_PER_TOKEN = 3.5

# Context window sizes (tokens)
CONTEXT_WINDOWS = {
    "claude-sonnet-4": 200_000,
    "claude-opus-4": 200_000,
    "claude-haiku-4": 200_000,
    "gpt-4o": 128_000,
    "gpt-4-turbo": 128_000,
    "gemini-2-flash": 1_000_000,
    "gemini-2-pro": 2_000_000,
}

# Zone budget allocation (per jacob-balslev/skill-graph pattern)
ZONE_BUDGETS = {
    "system_prompt": 0.10,      # 10% — system instructions, rules
    "skill_injection": 0.15,    # 15% — loaded skill metadata + bodies
    "working_memory": 0.50,     # 50% — conversation, tool outputs, retrieved docs
    "output_buffer": 0.25,      # 25% — response generation space
}

# Per soothe RFC-105: metadata listing capped at 1% of context window
METADATA_LISTING_BUDGET = 0.01

# Per soothe RFC-105: per-entry hard cap of 250 chars
PER_ENTRY_CHAR_CAP = 250

# Progressive loading thresholds (tokens)
L1_THRESHOLD = 500    # L1: name + description only (always loaded)
L2_THRESHOLD = 2000   # L2: + capabilities + operations (loaded on match)
L3_THRESHOLD = 10000  # L3: + full body + references (loaded on invoke)


def estimate_tokens(text: str) -> int:
    """Estimate token count from text length."""
    return max(1, math.ceil(len(text) / CHARS_PER_TOKEN))


def parse_frontmatter(text: str) -> tuple[dict, str]:
    """Extract YAML frontmatter and return (metadata, body)."""
    if not text.startswith("---"):
        return {}, text
    parts = text.split("---", 2)
    if len(parts) < 3:
        return {}, text
    try:
        fm = yaml.safe_load(parts[1])
        return (fm if isinstance(fm, dict) else {}), parts[2]
    except yaml.YAMLError:
        return {}, text


# ── Skill Analyzer ───────────────────────────────────────────────────────────

class SkillTokenAnalyzer:
    """Analyze token costs for a directory of skills."""

    def __init__(self, skills_dir: Path, exclude_prefix: str = "00_"):
        self.skills_dir = skills_dir
        self.exclude_prefix = exclude_prefix
        self.skills = {}  # name -> analysis
        self._analyze_all()

    def _analyze_skill(self, skill_dir: Path) -> dict:
        """Analyze a single skill directory."""
        sm = skill_dir / "SKILL.md"
        if not sm.exists():
            return None

        text = sm.read_text(encoding="utf-8", errors="replace")
        fm, body = parse_frontmatter(text)

        # L1: metadata only (name + description)
        name = fm.get("name", skill_dir.name)
        description = fm.get("description", "")
        l1_text = f"name: {name}\ndescription: {description}"
        l1_tokens = estimate_tokens(l1_text)
        l1_chars = len(l1_text)

        # L2: + capabilities + operations section
        # Extract first ~500 tokens of body for L2
        l2_body = body[:int(L2_THRESHOLD * CHARS_PER_TOKEN)] if body else ""
        l2_text = l1_text + "\n" + l2_body
        l2_tokens = estimate_tokens(l2_text)

        # L3: full SKILL.md
        l3_tokens = estimate_tokens(text)

        # References and scripts
        ref_tokens = 0
        ref_count = 0
        script_tokens = 0
        script_count = 0

        refs_dir = skill_dir / "references"
        if refs_dir.exists():
            for f in refs_dir.rglob("*"):
                if f.is_file() and f.suffix in (".md", ".txt", ".yaml", ".yml"):
                    ref_tokens += estimate_tokens(f.read_text(encoding="utf-8", errors="replace"))
                    ref_count += 1

        scripts_dir = skill_dir / "scripts"
        if scripts_dir.exists():
            for f in scripts_dir.rglob("*"):
                if f.is_file() and f.suffix in (".py", ".sh", ".js", ".ts"):
                    script_tokens += estimate_tokens(f.read_text(encoding="utf-8", errors="replace"))
                    script_count += 1

        total_tokens = l3_tokens + ref_tokens + script_tokens

        # Progressive disclosure level
        if l3_tokens <= L1_THRESHOLD:
            level = "L1-compact"
        elif l3_tokens <= L2_THRESHOLD:
            level = "L2-moderate"
        elif l3_tokens <= L3_THRESHOLD:
            level = "L3-standard"
        else:
            level = "L4-heavy"

        # Check per-entry cap (soothe RFC-105)
        exceeds_cap = l1_chars > PER_ENTRY_CHAR_CAP

        return {
            "name": name,
            "path": str(sm),
            "l1_tokens": l1_tokens,
            "l1_chars": l1_chars,
            "l2_tokens": l2_tokens,
            "l3_tokens": l3_tokens,
            "ref_tokens": ref_tokens,
            "ref_count": ref_count,
            "script_tokens": script_tokens,
            "script_count": script_count,
            "total_tokens": total_tokens,
            "progressive_level": level,
            "exceeds_entry_cap": exceeds_cap,
            "schema_version": fm.get("schema_version", "unknown"),
            "version": fm.get("version", "unknown"),
        }

    def _analyze_all(self):
        for sd in sorted(self.skills_dir.iterdir()):
            if not sd.is_dir() or sd.name.startswith(self.exclude_prefix):
                continue
            analysis = self._analyze_skill(sd)
            if analysis:
                self.skills[analysis["name"]] = analysis

    def summary(self) -> dict:
        total_l1 = sum(s["l1_tokens"] for s in self.skills.values())
        total_l3 = sum(s["l3_tokens"] for s in self.skills.values())
        total_all = sum(s["total_tokens"] for s in self.skills.values())

        # Progressive disclosure savings
        savings = total_l3 - total_l1
        savings_pct = (savings / total_l3 * 100) if total_l3 > 0 else 0

        # Skills exceeding per-entry cap
        over_cap = [s["name"] for s in self.skills.values() if s["exceeds_entry_cap"]]

        # Level distribution
        levels = {}
        for s in self.skills.values():
            lvl = s["progressive_level"]
            levels[lvl] = levels.get(lvl, 0) + 1

        # Heaviest skills
        heaviest = sorted(self.skills.values(), key=lambda x: -x["total_tokens"])[:20]

        return {
            "total_skills": len(self.skills),
            "total_l1_tokens": total_l1,
            "total_l3_tokens": total_l3,
            "total_all_tokens": total_all,
            "progressive_savings_tokens": savings,
            "progressive_savings_pct": round(savings_pct, 1),
            "skills_over_entry_cap": len(over_cap),
            "level_distribution": levels,
            "heaviest_skills": [
                {"name": s["name"], "total_tokens": s["total_tokens"], "level": s["progressive_level"]}
                for s in heaviest
            ],
        }

    def zone_allocation(self, model: str = "claude-sonnet-4") -> dict:
        """Calculate context zone allocation for a given model."""
        window = CONTEXT_WINDOWS.get(model, 200_000)
        zones = {}
        for zone, pct in ZONE_BUDGETS.items():
            zones[zone] = {
                "budget_pct": pct * 100,
                "budget_tokens": int(window * pct),
            }

        # Skill injection budget
        skill_budget = zones["skill_injection"]["budget_tokens"]
        total_l1 = sum(s["l1_tokens"] for s in self.skills.values())

        # How many skills fit in metadata listing budget (1% of window)
        metadata_budget = int(window * METADATA_LISTING_BUDGET)
        avg_l1 = total_l1 / len(self.skills) if self.skills else 0
        skills_in_metadata_budget = int(metadata_budget / avg_l1) if avg_l1 > 0 else 0

        # How many skills fit in full skill injection budget
        skills_in_injection_budget = int(skill_budget / avg_l1) if avg_l1 > 0 else 0

        return {
            "model": model,
            "context_window": window,
            "zones": zones,
            "metadata_listing_budget_tokens": metadata_budget,
            "avg_l1_tokens_per_skill": round(avg_l1, 1),
            "skills_in_metadata_budget": skills_in_metadata_budget,
            "skills_in_injection_budget": skills_in_injection_budget,
            "total_skills": len(self.skills),
            "fits_in_metadata_budget": len(self.skills) <= skills_in_metadata_budget,
        }


# ── CLI ──────────────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(description="AMOS Token Budget Analyzer")
    parser.add_argument("--skills-dir", default=".devin/skills", help="Skills directory")
    parser.add_argument("--skill", default=None, help="Analyze a specific skill")
    parser.add_argument("--json", action="store_true", help="JSON output")
    parser.add_argument("--top", type=int, default=20, help="Top N heaviest skills")
    parser.add_argument("--zones", action="store_true", help="Zone allocation analysis")
    parser.add_argument("--model", default="claude-sonnet-4", help="Model for zone analysis")
    args = parser.parse_args()

    skills_dir = Path(args.skills_dir)
    analyzer = SkillTokenAnalyzer(skills_dir)

    if args.skill:
        s = analyzer.skills.get(args.skill)
        if not s:
            # Try directory name match
            for name, data in analyzer.skills.items():
                if args.skill in name:
                    s = data
                    break
        if not s:
            print(f"ERROR: Skill {args.skill} not found", file=sys.stderr)
            sys.exit(1)
        if args.json:
            json.dump(s, sys.stdout, indent=2)
            print()
        else:
            print(f"=== Token Analysis: {s['name']} ===")
            print(f"  L1 (metadata):     {s['l1_tokens']:6d} tokens ({s['l1_chars']} chars)")
            print(f"  L2 (truncated):    {s['l2_tokens']:6d} tokens")
            print(f"  L3 (full SKILL.md):{s['l3_tokens']:6d} tokens")
            print(f"  References:        {s['ref_tokens']:6d} tokens ({s['ref_count']} files)")
            print(f"  Scripts:           {s['script_tokens']:6d} tokens ({s['script_count']} files)")
            print(f"  TOTAL:             {s['total_tokens']:6d} tokens")
            print(f"  Level:             {s['progressive_level']}")
            print(f"  Exceeds entry cap: {s['exceeds_entry_cap']}")
        return

    if args.zones:
        zone = analyzer.zone_allocation(args.model)
        if args.json:
            json.dump(zone, sys.stdout, indent=2)
            print()
        else:
            print(f"=== Context Zone Allocation ({zone['model']}) ===")
            print(f"  Context window:      {zone['context_window']:,} tokens")
            print()
            print(f"  Zones:")
            for zname, zdata in zone["zones"].items():
                print(f"    {zname:20s}: {zdata['budget_pct']:5.1f}% ({zdata['budget_tokens']:,} tokens)")
            print()
            print(f"  Metadata listing budget (1%): {zone['metadata_listing_budget_tokens']:,} tokens")
            print(f"  Avg L1 tokens per skill:      {zone['avg_l1_tokens_per_skill']}")
            print(f"  Skills in metadata budget:    {zone['skills_in_metadata_budget']}")
            print(f"  Skills in injection budget:   {zone['skills_in_injection_budget']}")
            print(f"  Total skills:                 {zone['total_skills']}")
            print(f"  Fits in metadata budget:      {zone['fits_in_metadata_budget']}")
        return

    s = analyzer.summary()
    if args.json:
        json.dump(s, sys.stdout, indent=2)
        print()
    else:
        print(f"=== Token Budget Analysis ===")
        print(f"  Total skills:            {s['total_skills']}")
        print(f"  Total L1 tokens:         {s['total_l1_tokens']:,} (metadata only)")
        print(f"  Total L3 tokens:         {s['total_l3_tokens']:,} (full SKILL.md)")
        print(f"  Total all tokens:        {s['total_all_tokens']:,} (with refs+scripts)")
        print(f"  Progressive savings:     {s['progressive_savings_tokens']:,} tokens ({s['progressive_savings_pct']}%)")
        print(f"  Skills over entry cap:   {s['skills_over_entry_cap']}")
        print()
        print(f"  Level Distribution:")
        for lvl, count in sorted(s["level_distribution"].items()):
            print(f"    {lvl:15s}: {count}")
        print()
        print(f"  Top {len(s['heaviest_skills'])} Heaviest Skills:")
        for sk in s["heaviest_skills"][:args.top]:
            print(f"    {sk['total_tokens']:6d} tokens  {sk['level']:15s}  {sk['name']}")


if __name__ == "__main__":
    main()
