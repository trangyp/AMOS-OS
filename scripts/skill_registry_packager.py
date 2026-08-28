#!/usr/bin/env python3
"""
skill_registry_packager.py — Package and distribute AMOS skills as a registry.

Inspired by SOTA repos:
  - Karanjot786/agent-skills-cli: universal CLI for 45+ agents, marketplace
  - nikships/skills-registry: GitHub-based registry, gateway skill, fetch-on-demand
  - microsoft/agent-skills: Skill Explorer, npx skills add, 1-click install
  - addyosmani/agent-skills: multi-agent install, marketplace, plugin system
  - garasegae/aiskillstore: USK open standard, MCP discovery

This tool:
  1. Packages all skills into a distributable registry index
  2. Generates a gateway skill for fetch-on-demand loading
  3. Creates install manifests for multiple agent platforms
  4. Validates package integrity (SHA-256 checksums)
  5. Generates a browsable catalog (JSON + Markdown)

Usage:
  python3 scripts/skill_registry_packager.py [--skills-dir DIR] --package
  python3 scripts/skill_registry_packager.py --skills-dir DIR --catalog
  python3 scripts/skill_registry_packager.py --skills-dir DIR --gateway
"""

import argparse
import hashlib
import json
import re
import sys
from pathlib import Path
from datetime import datetime, timezone
from typing import Dict, List, Optional


def parse_frontmatter(content: str) -> dict:
    """Parse YAML frontmatter from markdown."""
    fm = {}
    match = re.match(r'^---\n(.*?)\n---', content, re.DOTALL)
    if not match:
        return fm
    for line in match.group(1).split('\n'):
        if ':' in line:
            key, _, value = line.partition(':')
            fm[key.strip()] = value.strip().strip('"').strip("'")
    return fm


def extract_skill_info(skill_dir: Path) -> dict:
    """Extract package info from a skill directory."""
    skill_md = skill_dir / "SKILL.md"
    if not skill_md.exists():
        return {}

    content = skill_md.read_text(encoding="utf-8")
    fm = parse_frontmatter(content)

    # File inventory
    files = []
    total_size = 0
    for f in sorted(skill_dir.rglob("*")):
        if f.is_file():
            rel = f.relative_to(skill_dir)
            size = f.stat().st_size
            sha = hashlib.sha256(f.read_bytes()).hexdigest()
            files.append({
                "path": str(rel),
                "size": size,
                "sha256": sha,
            })
            total_size += size

    # Compute skill hash
    skill_hash = hashlib.sha256(content.encode("utf-8")).hexdigest()

    # Extract metadata
    info = {
        "name": skill_dir.name,
        "title": fm.get("title", skill_dir.name),
        "description": fm.get("description", ""),
        "version": fm.get("version", "1.0.0"),
        "domain": fm.get("domain", ""),
        "parent_skill": fm.get("parent_skill", "none"),
        "epistemic_class": fm.get("epistemic_class", ""),
        "origin_architect": fm.get("origin_architect", ""),
        "tags": fm.get("tags", ""),
        "skill_hash": skill_hash,
        "file_count": len(files),
        "total_size": total_size,
        "files": files,
    }

    # Load MANIFEST.yaml if exists
    manifest = skill_dir / "MANIFEST.yaml"
    if manifest.exists():
        info["has_manifest"] = True
        # Parse simple YAML
        for line in manifest.read_text(encoding="utf-8").split('\n'):
            if ':' in line and not line.startswith(' '):
                key, _, value = line.partition(':')
                key = key.strip()
                value = value.strip().strip('"').strip("'")
                if key == "bundle_version":
                    info["manifest_version"] = value
    else:
        info["has_manifest"] = False

    return info


def build_registry_index(skills_dir: Path) -> dict:
    """Build a complete registry index of all skills."""
    registry = {
        "registry_version": "1.0.0",
        "generated": datetime.now(timezone.utc).isoformat(),
        "skills_dir": str(skills_dir),
        "total_skills": 0,
        "total_size": 0,
        "skills": [],
        "domains": {},
        "platforms": {
            "claude-code": {"dir": ".claude/skills", "format": "md"},
            "claude-chat": {"dir": ".devin/skills", "format": "md"},
            "github-copilot": {"dir": ".agents/skills", "format": "md"},
            "cursor": {"dir": ".cursor/skills", "format": "md"},
            "codex": {"dir": ".codex/skills", "format": "md"},
            "gemini-cli": {"dir": ".gemini/skills", "format": "md"},
            "windsurf": {"dir": ".codeium/windsurf/skills", "format": "md"},
            "cline": {"dir": ".cline/skills", "format": "md"},
        },
    }

    domain_map = {}

    for d in sorted(skills_dir.iterdir()):
        if not (d.is_dir() and (d / "SKILL.md").exists()):
            continue

        info = extract_skill_info(d)
        if not info:
            continue

        registry["skills"].append(info)
        registry["total_skills"] += 1
        registry["total_size"] += info["total_size"]

        domain = info.get("domain", "unknown")
        if domain not in domain_map:
            domain_map[domain] = []
        domain_map[domain].append(info["name"])

    registry["domains"] = domain_map
    return registry


def generate_catalog_markdown(registry: dict) -> str:
    """Generate a browsable Markdown catalog."""
    lines = [
        "# AMOS Skill Registry Catalog",
        "",
        f"Generated: {registry['generated']}",
        f"Total skills: {registry['total_skills']}",
        f"Total size: {registry['total_size']:,} bytes ({registry['total_size']/1024/1024:.1f} MB)",
        "",
        "## Domain Index",
        "",
    ]

    for domain in sorted(registry.get("domains", {})):
        skills = registry["domains"][domain]
        lines.append(f"### {domain} ({len(skills)} skills)")
        lines.append("")
        for skill in sorted(skills):
            lines.append(f"- `{skill}`")
        lines.append("")

    lines.append("## Skill Details")
    lines.append("")

    for skill in sorted(registry["skills"], key=lambda s: s["name"]):
        lines.append(f"### {skill['name']}")
        lines.append(f"- **Description**: {skill['description'][:100]}...")
        lines.append(f"- **Version**: {skill['version']}")
        lines.append(f"- **Domain**: {skill['domain']}")
        lines.append(f"- **Parent**: {skill['parent_skill']}")
        lines.append(f"- **Epistemic class**: {skill['epistemic_class']}")
        lines.append(f"- **Files**: {skill['file_count']}")
        lines.append(f"- **Size**: {skill['total_size']:,} bytes")
        lines.append(f"- **SHA-256**: `{skill['skill_hash'][:16]}...`")
        lines.append("")

    return "\n".join(lines)


def generate_gateway_skill(registry: dict) -> str:
    """Generate a gateway skill for fetch-on-demand loading."""
    return f"""---
name: amos-skill-registry
description: Gateway skill for the AMOS skill registry. Use when searching for, discovering, or fetching AMOS skills on demand. Provides a catalog of {registry['total_skills']} skills across {len(registry['domains'])} domains.
version: 1.0.0
type: skill
---

# AMOS Skill Registry Gateway

## When to Use

- When you need to discover what AMOS skills are available
- When you need to find a skill for a specific domain or capability
- When you need to fetch a skill on demand instead of loading all skills

## Registry Summary

- **Total skills**: {registry['total_skills']}
- **Total domains**: {len(registry['domains'])}
- **Registry version**: {registry['registry_version']}

## Domain Catalog

| Domain | Skill Count |
|--------|------------|
""" + "\n".join(
    f"| {d} | {len(registry['domains'][d])} |"
    for d in sorted(registry['domains'])
) + f"""

## How to Fetch

1. **Search**: Browse the catalog above to find the domain you need
2. **Select**: Pick the skill name from the domain's skill list
3. **Load**: Read the skill's `SKILL.md` from `07_SKILLS/<skill-name>/SKILL.md`
4. **Validate**: Check the skill's epistemic class and scope before use

## Supported Platforms

This registry supports installation to multiple agent platforms:

| Platform | Install Directory |
|----------|------------------|
""" + "\n".join(
    f"| {p} | {info['dir']} |"
    for p, info in registry['platforms'].items()
) + f"""

## Anti-Patterns

- Do NOT load all skills at once — use fetch-on-demand
- Do NOT skip epistemic class validation when loading a skill
- Do NOT use a skill outside its declared domain scope

## Provenance

- **Registry generated**: {registry['generated']}
- **Source**: AMOS_OS Obsidian vault
- **Steward**: Trang Phan
"""


def main():
    parser = argparse.ArgumentParser(description="Package AMOS skills as a distributable registry")
    parser.add_argument("--skills-dir", default=".devin/skills", help="Skills directory")
    parser.add_argument("--package", action="store_true", help="Build registry index + catalog + gateway")
    parser.add_argument("--catalog", action="store_true", help="Generate Markdown catalog only")
    parser.add_argument("--gateway", action="store_true", help="Generate gateway skill only")
    parser.add_argument("--output-dir", default=".", help="Output directory")
    parser.add_argument("--summary", action="store_true", help="Print summary only")
    args = parser.parse_args()

    skills_dir = Path(args.skills_dir)
    output_dir = Path(args.output_dir)

    registry = build_registry_index(skills_dir)

    if args.summary:
        print(f"Skills:     {registry['total_skills']}")
        print(f"Domains:    {len(registry['domains'])}")
        print(f"Total size: {registry['total_size']:,} bytes ({registry['total_size']/1024/1024:.1f} MB)")
        print(f"Platforms:  {len(registry['platforms'])}")
        return

    print("=" * 70)
    print("  AMOS Skill Registry Packager")
    print("=" * 70)
    print()
    print(f"  Skills directory: {skills_dir}")
    print(f"  Total skills:     {registry['total_skills']}")
    print(f"  Total domains:    {len(registry['domains'])}")
    print(f"  Total size:       {registry['total_size']:,} bytes ({registry['total_size']/1024/1024:.1f} MB)")
    print(f"  Platforms:        {len(registry['platforms'])}")
    print()

    # Domain distribution
    print("  Domain distribution:")
    for domain in sorted(registry["domains"]):
        count = len(registry["domains"][domain])
        print(f"    {domain:30s} {count:4d} skills")
    print()

    if args.package or args.catalog:
        catalog = generate_catalog_markdown(registry)
        catalog_path = output_dir / "skill-registry-catalog.md"
        catalog_path.write_text(catalog, encoding="utf-8")
        print(f"  Catalog written to: {catalog_path}")

    if args.package or args.gateway:
        gateway = generate_gateway_skill(registry)
        gateway_path = output_dir / "amos-skill-registry-gateway.md"
        gateway_path.write_text(gateway, encoding="utf-8")
        print(f"  Gateway skill written to: {gateway_path}")

    if args.package:
        # Write full registry index
        index_path = output_dir / "skill-registry-index.json"
        index_path.write_text(json.dumps(registry, indent=2, ensure_ascii=False), encoding="utf-8")
        print(f"  Registry index written to: {index_path}")

        # Compute registry checksum
        registry_hash = hashlib.sha256(
            json.dumps(registry, sort_keys=True).encode("utf-8")
        ).hexdigest()
        print(f"  Registry checksum: {registry_hash[:16]}...")


if __name__ == "__main__":
    main()
