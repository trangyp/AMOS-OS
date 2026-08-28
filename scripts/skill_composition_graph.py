#!/usr/bin/env python3
"""
skill_composition_graph.py — Build a semantic capability graph for skill composition.

Inspired by SOTA repos:
  - jrodeiro5/skillgraph-mcp: semantic skill graph + plan_workflow, progressive disclosure
  - dushshantha/multiclaude: DAG-based task decomposition, parallel worker coordination
  - midego1/claude-orchestrate: tiered model routing, evidence-gated verification
  - sehoon787/my-claude: Boss meta-orchestrator priority routing chain (P0-P4)
  - sashabogi/agent-router: MCP-native multi-agent routing, specialized agent roles

This tool builds a composition graph from skill metadata:
  - Extracts capability tags from SKILL.md frontmatter
  - Maps parent→child skill relationships
  - Identifies composition chains (skill A → skill B → skill C)
  - Detects isolated skills (no composition edges)
  - Generates a DOT graph for visualization
  - Validates composition depth (max 3 per AMOS canon)

Usage:
  python3 scripts/skill_composition_graph.py [--skills-dir DIR] [--dot FILE] [--json FILE]
"""

import argparse
import json
import re
import sys
from pathlib import Path
from datetime import datetime, timezone
from typing import Dict, List, Set, Optional
from collections import defaultdict


def parse_frontmatter(content: str) -> dict:
    """Parse YAML frontmatter from markdown content."""
    fm = {}
    match = re.match(r'^---\n(.*?)\n---', content, re.DOTALL)
    if not match:
        return fm
    fm_text = match.group(1)
    for line in fm_text.split('\n'):
        if ':' in line:
            key, _, value = line.partition(':')
            key = key.strip()
            value = value.strip().strip('"').strip("'")
            if value:
                fm[key] = value
    return fm


def extract_skill_metadata(skill_dir: Path) -> dict:
    """Extract metadata from a skill directory."""
    skill_md = skill_dir / "SKILL.md"
    if not skill_md.exists():
        return {}

    content = skill_md.read_text(encoding="utf-8")
    fm = parse_frontmatter(content)

    # Extract parent skill from frontmatter or body
    parent = fm.get("parent", "") or fm.get("parent_skill", "")
    if not parent:
        # Search in body for Parent: or [[parent]]
        match = re.search(r'\*\*Parent\*\*:\s*`?\[\[([^\]]+)\]\]`?', content)
        if match:
            parent = match.group(1).strip()
        else:
            # Try Composition section
            match = re.search(r'\*\*Parent\*\*:\s*`?(\[\[)?([^\]`]+)(\]\])?`?', content)
            if match:
                parent = match.group(2).strip()

    # Extract capabilities from body
    capabilities = []
    cap_match = re.search(r'## Capabilities\s*\n(.*?)(?=\n##|\Z)', content, re.DOTALL)
    if cap_match:
        for line in cap_match.group(1).split('\n'):
            match = re.match(r'^-\s+\*\*(.+?)\*\*', line)
            if match:
                capabilities.append(match.group(1).strip())

    # Extract domain from tags or name
    domain = fm.get("domain", "")
    tags = fm.get("tags", "")
    if not domain and tags:
        for tag in tags.split(","):
            tag = tag.strip()
            if tag.startswith("domain/"):
                domain = tag.replace("domain/", "")
                break

    # Guess domain from name
    if not domain:
        if skill_dir.name.startswith("amos-c"):
            domain = skill_dir.name[:7]  # e.g., amos-c01
        elif skill_dir.name.startswith("arxiv-"):
            domain = "arxiv"
        elif skill_dir.name.startswith("mckinsey-"):
            domain = "mckinsey"

    return {
        "name": skill_dir.name,
        "parent": parent,
        "domain": domain,
        "capabilities": capabilities,
        "description": fm.get("description", ""),
    }


def build_composition_graph(skills_dir: Path) -> dict:
    """Build the skill composition graph."""
    skills = {}
    if not skills_dir.exists():
        return {"nodes": [], "edges": [], "domains": {}, "stats": {}}

    for d in sorted(skills_dir.iterdir()):
        if d.is_dir() and (d / "SKILL.md").exists():
            meta = extract_skill_metadata(d)
            if meta:
                skills[meta["name"]] = meta

    # Build edges from parent relationships
    edges = []
    for name, meta in skills.items():
        parent = meta.get("parent", "").strip()
        if parent and parent != "none" and parent != "[[none]]":
            # Clean parent name
            parent = parent.replace("[[", "").replace("]]", "").strip()
            # Try to match to actual skill
            if parent in skills:
                edges.append({
                    "source": parent,
                    "target": name,
                    "type": "parent",
                })
            elif parent.endswith("-master") and parent.replace("-master", "") in skills:
                edges.append({
                    "source": parent.replace("-master", ""),
                    "target": name,
                    "type": "parent",
                })

    # Build domain clusters
    domains = defaultdict(list)
    for name, meta in skills.items():
        domain = meta.get("domain", "unknown")
        domains[domain].append(name)

    # Find composition chains (depth > 1)
    children_of = defaultdict(list)
    for edge in edges:
        children_of[edge["source"]].append(edge["target"])

    def find_chain(node, visited=None, depth=0):
        if visited is None:
            visited = set()
        if node in visited or depth > 10:
            return []
        visited.add(node)
        chains = []
        for child in children_of.get(node, []):
            chains.append([node, child])
            for sub in find_chain(child, visited.copy(), depth + 1):
                if sub[0] == child:
                    chains.append([node] + sub)
        return chains

    all_chains = []
    for node in skills:
        chains = find_chain(node)
        for c in chains:
            if len(c) >= 3:  # Only chains of depth >= 2
                all_chains.append(c)

    # Find isolated skills (no parent, no children)
    nodes_with_edges = set()
    for edge in edges:
        nodes_with_edges.add(edge["source"])
        nodes_with_edges.add(edge["target"])
    isolated = [name for name in skills if name not in nodes_with_edges]

    # Check composition depth violations (max 3 per AMOS canon)
    depth_violations = [c for c in all_chains if len(c) > 4]  # chain of 5+ = depth 4+

    stats = {
        "total_skills": len(skills),
        "total_edges": len(edges),
        "total_domains": len(domains),
        "composition_chains": len(all_chains),
        "isolated_skills": len(isolated),
        "depth_violations": len(depth_violations),
        "max_chain_length": max((len(c) for c in all_chains), default=0),
    }

    return {
        "nodes": list(skills.values()),
        "edges": edges,
        "domains": dict(domains),
        "composition_chains": all_chains,
        "isolated_skills": isolated,
        "depth_violations": depth_violations,
        "stats": stats,
    }


def generate_dot(graph: dict) -> str:
    """Generate DOT graph for visualization."""
    lines = ["digraph skill_composition {", "  rankdir=TB;", "  node [shape=box, fontname=\"Helvetica\"];"]

    # Domain clusters
    for domain, skills in graph.get("domains", {}).items():
        lines.append(f'  subgraph "cluster_{domain}" {{')
        lines.append(f'    label="{domain}";')
        lines.append('    style=filled;')
        lines.append('    color=lightgrey;')
        for skill in skills:
            safe = skill.replace("-", "_")
            lines.append(f'    {safe} [label="{skill}"];')
        lines.append("  }")

    # Edges
    for edge in graph.get("edges", []):
        src = edge["source"].replace("-", "_")
        tgt = edge["target"].replace("-", "_")
        lines.append(f'  {src} -> {tgt};')

    lines.append("}")
    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(description="Build skill composition graph")
    parser.add_argument("--skills-dir", default=".devin/skills", help="Skills directory")
    parser.add_argument("--dot", default=None, help="Write DOT graph to file")
    parser.add_argument("--json", default=None, help="Write JSON graph to file")
    parser.add_argument("--summary", action="store_true", help="Print summary only")
    args = parser.parse_args()

    skills_dir = Path(args.skills_dir)
    graph = build_composition_graph(skills_dir)
    stats = graph["stats"]

    if args.summary:
        print(f"Skills:          {stats['total_skills']}")
        print(f"Edges:           {stats['total_edges']}")
        print(f"Domains:         {stats['total_domains']}")
        print(f"Chains (depth≥2):{stats['composition_chains']}")
        print(f"Isolated:        {stats['isolated_skills']}")
        print(f"Depth violations:{stats['depth_violations']}")
        print(f"Max chain length:{stats['max_chain_length']}")
        return

    print("=" * 70)
    print("  AMOS Skill Composition Graph")
    print("=" * 70)
    print()
    print(f"  Skills directory: {skills_dir}")
    print()
    print(f"  Total skills:           {stats['total_skills']}")
    print(f"  Total edges:            {stats['total_edges']}")
    print(f"  Total domains:          {stats['total_domains']}")
    print(f"  Composition chains:     {stats['composition_chains']}")
    print(f"  Isolated skills:        {stats['isolated_skills']}")
    print(f"  Depth violations (>3):  {stats['depth_violations']}")
    print(f"  Max chain length:       {stats['max_chain_length']}")
    print()

    # Domain breakdown
    print("  Domain distribution:")
    for domain in sorted(graph.get("domains", {})):
        count = len(graph["domains"][domain])
        print(f"    {domain:30s} {count:4d} skills")
    print()

    # Composition chains
    if graph.get("composition_chains"):
        print("  Composition chains (depth ≥ 2):")
        for chain in graph["composition_chains"][:10]:
            print(f"    {' → '.join(chain)}")
        if len(graph["composition_chains"]) > 10:
            print(f"    ... and {len(graph['composition_chains']) - 10} more")
        print()

    # Depth violations
    if graph.get("depth_violations"):
        print("  [WARNING] Depth violations (chain > 3):")
        for chain in graph["depth_violations"][:5]:
            print(f"    {' → '.join(chain)}")
        print()

    # Isolated skills
    if graph.get("isolated_skills"):
        print(f"  Isolated skills (no composition edges): {len(graph['isolated_skills'])}")
        for s in graph["isolated_skills"][:10]:
            print(f"    - {s}")
        if len(graph["isolated_skills"]) > 10:
            print(f"    ... and {len(graph['isolated_skills']) - 10} more")
        print()

    # Write DOT
    if args.dot:
        dot_content = generate_dot(graph)
        Path(args.dot).write_text(dot_content, encoding="utf-8")
        print(f"  DOT graph written to: {args.dot}")

    # Write JSON
    if args.json:
        Path(args.json).write_text(
            json.dumps(graph, indent=2, ensure_ascii=False), encoding="utf-8"
        )
        print(f"  JSON graph written to: {args.json}")


if __name__ == "__main__":
    main()
