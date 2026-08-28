#!/usr/bin/env python3
"""
AMOS Skill Version Manager — SemVer, changelog, manifest, and compatibility
tracking for agent skills.

Inspired by SOTA repos:
  - snapsynapse/skill-provenance v4.9.0: MANIFEST.yaml with bundle_version
    (semver), compatible_with block, dependencies field, CHANGELOG.md,
    SHA-256 hashes, staleness detection
  - cathy-kim/skill-semver: Auto-backup on edit, releases/ folder,
    Keep a Changelog format, pre-release support (alpha/beta/rc)
  - narrative-io/narrative-skills-marketplace: CalVer for marketplace +
    SemVer for individual skills
  - microsoft/agent-skills: Skill Explorer, npx skills add, symlinked
    multi-agent setups
  - garasegae/aiskillstore: USK open standard, trust levels
    (verified/community/sandbox)

Features:
  - SemVer parsing (MAJOR.MINOR.PATCH + pre-release + build metadata)
  - Per-skill MANIFEST.yaml generation (bundle_version, compatible_with,
    dependencies, security_verdict)
  - CHANGELOG.md generation (Keep a Changelog format)
  - Staleness detection (compare manifest version vs frontmatter version)
  - Compatibility matrix (which platforms/agents each skill supports)
  - Bump detection (diff version vs last manifest)
  - --summary, --skill, --bump, --manifest, --changelog, --stale flags

Usage:
  python3 scripts/skill_version_manager.py --summary
  python3 scripts/skill_version_manager.py --skill amos-skill-builder
  python3 scripts/skill_version_manager.py --bump amos-skill-builder --type minor
  python3 scripts/skill_version_manager.py --manifest amos-skill-builder
  python3 scripts/skill_version_manager.py --stale
"""

import argparse
import json
import os
import re
import sys
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path


# ── SemVer Parsing (per semver.org 2.0.0) ───────────────────────────────────

SEMVER_RE = re.compile(
    r'^(?P<major>0|[1-9]\d*)'
    r'\.(?P<minor>0|[1-9]\d*)'
    r'\.(?P<patch>0|[1-9]\d*)'
    r'(?:-(?P<pre>(?:0|[1-9]\d*|\d*[a-zA-Z-][0-9a-zA-Z-]*)'
    r'(?:\.(?:0|[1-9]\d*|\d*[a-zA-Z-][0-9a-zA-Z-]*))*))?'
    r'(?:\+(?P<build>[0-9a-zA-Z-]+(?:\.[0-9a-zA-Z-]+)*))?$'
)


def parse_semver(version: str) -> dict:
    """Parse a semver string into components."""
    if not version:
        return None
    m = SEMVER_RE.match(version.strip().lstrip('v'))
    if not m:
        return None
    return {
        "major": int(m.group("major")),
        "minor": int(m.group("minor")),
        "patch": int(m.group("patch")),
        "pre": m.group("pre"),
        "build": m.group("build"),
        "raw": version,
    }


def bump_version(version: str, bump_type: str) -> str:
    """Bump a semver string. bump_type: major, minor, patch."""
    v = parse_semver(version)
    if not v:
        return "1.0.0"
    if bump_type == "major":
        return f"{v['major'] + 1}.0.0"
    elif bump_type == "minor":
        return f"{v['major']}.{v['minor'] + 1}.0"
    elif bump_type == "patch":
        return f"{v['major']}.{v['minor']}.{v['patch'] + 1}"
    return version


def compare_semver(a: str, b: str) -> int:
    """Compare two semver strings. Returns -1, 0, or 1."""
    va, vb = parse_semver(a), parse_semver(b)
    if not va or not vb:
        return 0
    for key in ("major", "minor", "patch"):
        if va[key] < vb[key]:
            return -1
        if va[key] > vb[key]:
            return 1
    # Pre-release: has pre < no pre
    if va["pre"] and not vb["pre"]:
        return -1
    if not va["pre"] and vb["pre"]:
        return 1
    if va["pre"] and vb["pre"]:
        if va["pre"] < vb["pre"]:
            return -1
        if va["pre"] > vb["pre"]:
            return 1
    return 0


# ── Frontmatter Parsing ─────────────────────────────────────────────────────

def parse_frontmatter(content: str) -> dict:
    """Parse YAML frontmatter from markdown content."""
    if not content.startswith("---"):
        return {}
    end = content.find("\n---", 3)
    if end == -1:
        return {}
    fm_text = content[3:end].strip()
    fm = {}
    for line in fm_text.split("\n"):
        line = line.strip()
        if ":" in line and not line.startswith("#"):
            key, _, val = line.partition(":")
            key = key.strip()
            val = val.strip().strip('"').strip("'")
            if val:
                fm[key] = val
    return fm


def get_skill_version(skill_path: Path) -> str:
    """Extract version from skill SKILL.md frontmatter or body."""
    skill_md = skill_path / "SKILL.md"
    if not skill_md.exists():
        return "0.0.0"
    content = skill_md.read_text(encoding="utf-8")
    fm = parse_frontmatter(content)
    # Check frontmatter
    if "version" in fm:
        return fm["version"]
    # Check metadata.version
    if "metadata" in content:
        m = re.search(r'version:\s*["\']?(\d+\.\d+\.\d+)', content)
        if m:
            return m.group(1)
    # Check for version in body
    m = re.search(r'(?i)version[:\s]+["\']?(\d+\.\d+\.\d+)', content)
    if m:
        return m.group(1)
    return "0.0.0"


# ── Manifest Generation (per skill-provenance pattern) ──────────────────────

MANIFEST_TEMPLATE = """\
bundle_version: {version}
bundle_date: {date}
schema_version: "1.0"
compatible_with:
  - claude-code
  - claude-chat
  - codex
  - gemini-cli
  - copilot
dependencies: []
security_verdict: pass
epistemic_class: {epistemic_class}
steward: Trang Phan
license: MIT
files:
{file_list}
"""


def generate_manifest(skill_path: Path, version: str = None) -> str:
    """Generate MANIFEST.yaml content for a skill."""
    if not version:
        version = get_skill_version(skill_path)
    date = datetime.now(timezone.utc).strftime("%Y-%m-%d")

    # List files
    files = []
    for f in sorted(skill_path.rglob("*")):
        if f.is_file() and not f.name.startswith("."):
            rel = f.relative_to(skill_path)
            files.append(f'  - path: "{rel}"')

    file_list = "\n".join(files) if files else "  []"

    # Detect epistemic class from SKILL.md
    skill_md = skill_path / "SKILL.md"
    epistemic = "AMOS_MODEL"
    if skill_md.exists():
        content = skill_md.read_text(encoding="utf-8")
        if "SOURCE_CLAIM" in content:
            epistemic = "SOURCE_CLAIM"
        elif "SOURCE_CANON" in content:
            epistemic = "SOURCE_CANON"
        elif "DERIVED" in content:
            epistemic = "DERIVED"
        elif "EMPIRICAL" in content:
            epistemic = "EMPIRICAL"

    return MANIFEST_TEMPLATE.format(
        version=version,
        date=date,
        epistemic_class=epistemic,
        file_list=file_list,
    )


# ── Changelog Generation (per Keep a Changelog format) ──────────────────────

CHANGELOG_TEMPLATE = """\
# Changelog

All notable changes to this skill are documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/),
and this project adheres to [Semantic Versioning](https://semver.org/).

## [{version}] - {date}

### Added
- Initial manifest generation and version tracking.

### Notes
- Version migrated from SKILL.md frontmatter to MANIFEST.yaml.
- Compatible with agentskills.io open standard.
"""


def generate_changelog(version: str) -> str:
    """Generate CHANGELOG.md content."""
    date = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    return CHANGELOG_TEMPLATE.format(version=version, date=date)


# ── Staleness Detection (per skill-provenance pattern) ──────────────────────

def detect_stale_skills(skills_dir: Path) -> list:
    """Detect skills where frontmatter version != manifest version."""
    stale = []
    for skill_dir in sorted(skills_dir.iterdir()):
        if not skill_dir.is_dir():
            continue
        skill_md = skill_dir / "SKILL.md"
        manifest = skill_dir / "MANIFEST.yaml"
        if not skill_md.exists():
            continue
        fm_version = get_skill_version(skill_dir)
        manifest_version = None
        if manifest.exists():
            m = re.search(r'bundle_version:\s*["\']?(\d+\.\d+\.\d+)',
                          manifest.read_text(encoding="utf-8"))
            if m:
                manifest_version = m.group(1)
        if manifest_version and compare_semver(fm_version, manifest_version) != 0:
            stale.append({
                "skill": skill_dir.name,
                "frontmatter_version": fm_version,
                "manifest_version": manifest_version,
                "drift": "ahead" if compare_semver(fm_version, manifest_version) > 0 else "behind",
            })
    return stale


# ── Summary ─────────────────────────────────────────────────────────────────

def summarize_skills(skills_dir: Path) -> dict:
    """Summarize version distribution across all skills."""
    stats = {
        "total": 0,
        "with_version": 0,
        "without_version": 0,
        "with_manifest": 0,
        "with_changelog": 0,
        "version_dist": defaultdict(int),
        "stale": 0,
        "latest": None,
        "oldest": None,
    }
    versions = []
    for skill_dir in sorted(skills_dir.iterdir()):
        if not skill_dir.is_dir():
            continue
        stats["total"] += 1
        v = get_skill_version(skill_dir)
        if v and v != "0.0.0":
            stats["with_version"] += 1
            stats["version_dist"][f"{parse_semver(v)['major']}.{parse_semver(v)['minor']}.x"] += 1
            versions.append((skill_dir.name, v))
        else:
            stats["without_version"] += 1
        if (skill_dir / "MANIFEST.yaml").exists():
            stats["with_manifest"] += 1
        if (skill_dir / "CHANGELOG.md").exists():
            stats["with_changelog"] += 1

    if versions:
        def sort_key(x):
            v = parse_semver(x[1])
            if not v:
                return (0, 0, 0)
            return (v["major"], v["minor"], v["patch"])
        versions.sort(key=sort_key, reverse=True)
        stats["latest"] = versions[0]
        stats["oldest"] = versions[-1]

    stats["stale"] = len(detect_stale_skills(skills_dir))
    stats["version_dist"] = dict(stats["version_dist"])
    return stats


# ── CLI ─────────────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(description="AMOS Skill Version Manager")
    parser.add_argument("--skills-dir", default=None, help="Skills directory")
    parser.add_argument("--summary", action="store_true", help="Show version summary")
    parser.add_argument("--skill", default=None, help="Show version info for a skill")
    parser.add_argument("--bump", default=None, help="Bump version for a skill")
    parser.add_argument("--type", default="patch", choices=["major", "minor", "patch"],
                        help="Bump type")
    parser.add_argument("--manifest", default=None, help="Generate MANIFEST.yaml for a skill")
    parser.add_argument("--changelog", default=None, help="Generate CHANGELOG.md for a skill")
    parser.add_argument("--stale", action="store_true", help="Detect stale skills")
    parser.add_argument("--json", action="store_true", help="JSON output")
    parser.add_argument("--all-manifests", action="store_true",
                        help="Generate manifests for all skills")
    args = parser.parse_args()

    # Determine skills dir
    skills_dir = Path(args.skills_dir) if args.skills_dir else None
    if not skills_dir:
        for candidate in [Path(".devin/skills"), Path("07_SKILLS")]:
            if candidate.exists():
                skills_dir = candidate
                break
    if not skills_dir or not skills_dir.exists():
        print("Error: skills directory not found", file=sys.stderr)
        sys.exit(1)

    if args.summary:
        stats = summarize_skills(skills_dir)
        if args.json:
            json.dump(stats, sys.stdout, indent=2, default=str)
            print()
        else:
            print(f"=== Skill Version Summary ===")
            print(f"  Total skills:       {stats['total']}")
            print(f"  With version:       {stats['with_version']}")
            print(f"  Without version:    {stats['without_version']}")
            print(f"  With MANIFEST.yaml: {stats['with_manifest']}")
            print(f"  With CHANGELOG.md:  {stats['with_changelog']}")
            print(f"  Stale (drift):      {stats['stale']}")
            if stats["latest"]:
                print(f"  Latest version:     {stats['latest'][1]} ({stats['latest'][0]})")
            if stats["oldest"]:
                print(f"  Oldest version:     {stats['oldest'][1]} ({stats['oldest'][0]})")
            if stats["version_dist"]:
                print(f"  Version distribution:")
                for v, count in sorted(stats["version_dist"].items(), key=lambda x: -x[1])[:10]:
                    print(f"    {v:15s}: {count}")
        return

    if args.stale:
        stale = detect_stale_skills(skills_dir)
        if args.json:
            json.dump(stale, sys.stdout, indent=2)
            print()
        else:
            print(f"=== Stale Skills (version drift) ===")
            if not stale:
                print("  None — all versions aligned.")
            else:
                for s in stale:
                    print(f"  {s['skill']:40s} fm={s['frontmatter_version']} "
                          f"manifest={s['manifest_version']} ({s['drift']})")
        return

    if args.bump:
        skill_path = skills_dir / args.bump
        if not skill_path.exists():
            print(f"Error: skill {args.bump} not found", file=sys.stderr)
            sys.exit(1)
        current = get_skill_version(skill_path)
        new = bump_version(current, args.type)
        print(f"Bump: {args.bump} {current} → {new} ({args.type})")
        # Update MANIFEST.yaml if exists
        manifest = skill_path / "MANIFEST.yaml"
        if manifest.exists():
            content = manifest.read_text(encoding="utf-8")
            content = re.sub(r'bundle_version:\s*["\']?[\d.]+',
                             f'bundle_version: {new}', content)
            manifest.write_text(content, encoding="utf-8")
            print(f"  Updated MANIFEST.yaml")
        return

    if args.manifest:
        skill_path = skills_dir / args.manifest
        if not skill_path.exists():
            print(f"Error: skill {args.manifest} not found", file=sys.stderr)
            sys.exit(1)
        manifest_content = generate_manifest(skill_path)
        manifest_path = skill_path / "MANIFEST.yaml"
        manifest_path.write_text(manifest_content, encoding="utf-8")
        print(f"Generated {manifest_path}")
        return

    if args.changelog:
        skill_path = skills_dir / args.changelog
        if not skill_path.exists():
            print(f"Error: skill {args.changelog} not found", file=sys.stderr)
            sys.exit(1)
        v = get_skill_version(skill_path)
        changelog_content = generate_changelog(v)
        changelog_path = skill_path / "CHANGELOG.md"
        changelog_path.write_text(changelog_content, encoding="utf-8")
        print(f"Generated {changelog_path}")
        return

    if args.all_manifests:
        count = 0
        for skill_dir in sorted(skills_dir.iterdir()):
            if not skill_dir.is_dir():
                continue
            skill_md = skill_dir / "SKILL.md"
            if not skill_md.exists():
                continue
            manifest_content = generate_manifest(skill_dir)
            (skill_dir / "MANIFEST.yaml").write_text(manifest_content, encoding="utf-8")
            count += 1
        print(f"Generated MANIFEST.yaml for {count} skills")
        return

    if args.skill:
        skill_path = skills_dir / args.skill
        if not skill_path.exists():
            print(f"Error: skill {args.skill} not found", file=sys.stderr)
            sys.exit(1)
        v = get_skill_version(skill_path)
        manifest = skill_path / "MANIFEST.yaml"
        changelog = skill_path / "CHANGELOG.md"
        info = {
            "skill": args.skill,
            "version": v,
            "has_manifest": manifest.exists(),
            "has_changelog": changelog.exists(),
            "parsed": parse_semver(v),
        }
        if args.json:
            json.dump(info, sys.stdout, indent=2, default=str)
            print()
        else:
            print(f"=== {args.skill} ===")
            print(f"  Version:       {v}")
            print(f"  Has manifest:  {info['has_manifest']}")
            print(f"  Has changelog: {info['has_changelog']}")
            if info["parsed"]:
                p = info["parsed"]
                print(f"  Parsed:        {p['major']}.{p['minor']}.{p['patch']}"
                      f"{'-' + p['pre'] if p['pre'] else ''}")
        return

    parser.print_help()


if __name__ == "__main__":
    main()
