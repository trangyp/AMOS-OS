#!/usr/bin/env python3
"""
AMOS Skill Dependency Graph — Topological sort, cycle detection, routing analysis.

Parses skill frontmatter to build a dependency graph, then provides:
  - Topological sort (Kahn's algorithm) for execution ordering
  - Cycle detection (DFS-based) for dependency loops
  - Orphan skill detection (no dependencies, no dependents)
  - Hub skill detection (many dependents)
  - Routing analysis (which skills route to which)

Inspired by SOTA repos:
  - nexus-agents/skill-dependency-graph.ts: Kahn's algorithm, cycle detection
  - context4ai/agent-graph: Work-contract layer, fact-grounded routes
  - varunreddy/SkillMesh: Retrieval-gated routing (top-K selection)
  - Dranser/skills-graph: 5-layer graph (discovery, routing, execution, dep, conflict)
  - KonstantinData/skill-centric-agent-system: Sealed Runtime Agent Profile

Usage:
  python3 scripts/skill_dependency_graph.py                    # full analysis
  python3 scripts/skill_dependency_graph.py --json              # JSON output
  python3 scripts/skill_dependency_graph.py --topo              # topological sort
  python3 scripts/skill_dependency_graph.py --cycles            # cycle detection
  python3 scripts/skill_dependency_graph.py --orphans           # orphan skills
  python3 scripts/skill_dependency_graph.py --hubs              # hub skills
  python3 scripts/skill_dependency_graph.py --routing           # routing analysis
"""

import argparse
import json
import re
import sys
from collections import defaultdict, deque
from pathlib import Path

try:
    import yaml
except ImportError:
    print("ERROR: PyYAML required. Install: pip install pyyaml", file=sys.stderr)
    sys.exit(2)


# ── Graph Builder ────────────────────────────────────────────────────────────

def parse_frontmatter(text: str) -> dict:
    """Extract YAML frontmatter from markdown."""
    if not text.startswith("---"):
        return {}
    parts = re.split(r"^---\s*$", text, 2, flags=re.MULTILINE)
    if len(parts) < 3:
        return {}
    try:
        fm = yaml.safe_load(parts[1])
        return fm if isinstance(fm, dict) else {}
    except yaml.YAMLError:
        return {}


def extract_routing_targets(text: str) -> list[str]:
    """Extract skill names that this skill routes to (from body text)."""
    targets = []
    # Look for "routes to" patterns in SKILL.md body
    patterns = [
        r"(?:routes? to|delegates? to|dispatches? to)\s+`?(amos-[\w-]+)`?",
        r"(?:routes? to|delegates? to|dispatches? to)\s+`?(arxiv-[\w-]+)`?",
        r"(?:routes? to|delegates? to|dispatches? to)\s+`?(mckinsey-[\w-]+)`?",
    ]
    for pat in patterns:
        for m in re.finditer(pat, text, re.IGNORECASE):
            targets.append(m.group(1))
    return list(set(targets))


class SkillDependencyGraph:
    """Directed graph of skill dependencies and routing relationships."""

    def __init__(self, skills_dir: Path, exclude_prefix: str = "00_"):
        self.skills_dir = skills_dir
        self.exclude_prefix = exclude_prefix
        self.nodes = {}           # skill_name -> {frontmatter, path, routing_targets}
        self.dependencies = defaultdict(set)  # skill -> set(dependency skills)
        self.dependents = defaultdict(set)    # skill -> set(skills that depend on it)
        self.routing = defaultdict(set)       # skill -> set(skills it routes to)
        self._build()

    def _build(self):
        for sd in sorted(self.skills_dir.iterdir()):
            if not sd.is_dir() or sd.name.startswith(self.exclude_prefix):
                continue
            sm = sd / "SKILL.md"
            if not sm.exists():
                continue

            text = sm.read_text(encoding="utf-8", errors="replace")
            fm = parse_frontmatter(text)
            name = fm.get("name", sd.name)

            self.nodes[name] = {
                "frontmatter": fm,
                "path": str(sm),
                "version": fm.get("version", "unknown"),
                "schema_version": fm.get("schema_version", "unknown"),
                "steward": fm.get("steward", "unknown"),
                "tags": fm.get("tags", []),
            }

            # Extract dependencies from frontmatter
            deps = fm.get("dependencies", [])
            if isinstance(deps, list):
                for dep in deps:
                    if isinstance(dep, str):
                        self.dependencies[name].add(dep)
                        self.dependents[dep].add(name)

            parent = fm.get("parent_skill")
            if parent and isinstance(parent, str):
                self.dependencies[name].add(parent)
                self.dependents[parent].add(name)

            # Extract routing targets from body
            routing_targets = extract_routing_targets(text)
            for target in routing_targets:
                if target in self.nodes or target in [d.name for d in self.skills_dir.iterdir()]:
                    self.routing[name].add(target)

    # ── Topological Sort (Kahn's algorithm) ──────────────────────────────────

    def topological_sort(self) -> tuple[list[str], list[str]]:
        """Return (sorted_order, nodes_in_cycles)."""
        in_degree = {n: 0 for n in self.nodes}
        adj = defaultdict(set)

        for skill, deps in self.dependencies.items():
            for dep in deps:
                if dep in self.nodes:
                    adj[dep].add(skill)
                    in_degree[skill] += 1

        queue = deque([n for n in self.nodes if in_degree[n] == 0])
        order = []

        while queue:
            node = queue.popleft()
            order.append(node)
            for neighbor in adj[node]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)

        in_cycles = [n for n in self.nodes if n not in order]
        return order, in_cycles

    # ── Cycle Detection (DFS) ────────────────────────────────────────────────

    def detect_cycles(self) -> list[list[str]]:
        """Detect all cycles using DFS."""
        WHITE, GRAY, BLACK = 0, 1, 2
        color = {n: WHITE for n in self.nodes}
        cycles = []

        def dfs(node, path):
            color[node] = GRAY
            for dep in self.dependencies.get(node, set()):
                if dep not in self.nodes:
                    continue
                if color[dep] == GRAY:
                    # Found a cycle
                    cycle_start = path.index(dep) if dep in path else 0
                    cycles.append(path[cycle_start:] + [dep])
                elif color[dep] == WHITE:
                    dfs(dep, path + [dep])
            color[node] = BLACK

        for node in self.nodes:
            if color[node] == WHITE:
                dfs(node, [node])

        return cycles

    # ── Analysis ─────────────────────────────────────────────────────────────

    def orphans(self) -> list[str]:
        """Skills with no dependencies and no dependents."""
        return sorted([
            n for n in self.nodes
            if not self.dependencies.get(n) and not self.dependents.get(n)
        ])

    def hubs(self, top_n: int = 20) -> list[tuple[str, int]]:
        """Skills ranked by number of dependents."""
        counts = [(n, len(self.dependents.get(n, set()))) for n in self.nodes]
        return sorted(counts, key=lambda x: -x[1])[:top_n]

    def routing_hubs(self, top_n: int = 20) -> list[tuple[str, int]]:
        """Skills that route to the most other skills."""
        counts = [(n, len(self.routing.get(n, set()))) for n in self.nodes if self.routing.get(n)]
        return sorted(counts, key=lambda x: -x[1])[:top_n]

    def summary(self) -> dict:
        order, in_cycles = self.topological_sort()
        cycles = self.detect_cycles()
        return {
            "total_skills": len(self.nodes),
            "total_dependencies": sum(len(d) for d in self.dependencies.values()),
            "total_routing_edges": sum(len(r) for r in self.routing.values()),
            "orphan_skills": len(self.orphans()),
            "cycles_detected": len(cycles),
            "nodes_in_cycles": len(in_cycles),
            "topological_order_length": len(order),
            "schema_versions": len(set(n["schema_version"] for n in self.nodes.values())),
            "skill_versions": len(set(n["version"] for n in self.nodes.values())),
            "stewards": len(set(n["steward"] for n in self.nodes.values())),
        }


# ── CLI ──────────────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(description="AMOS Skill Dependency Graph")
    parser.add_argument("path", nargs="?", default=None, help="Specific skill to analyze")
    parser.add_argument("--skills-dir", default=".devin/skills", help="Skills directory")
    parser.add_argument("--json", action="store_true", help="JSON output")
    parser.add_argument("--topo", action="store_true", help="Topological sort")
    parser.add_argument("--cycles", action="store_true", help="Cycle detection")
    parser.add_argument("--orphans", action="store_true", help="Orphan skills")
    parser.add_argument("--hubs", action="store_true", help="Hub skills")
    parser.add_argument("--routing", action="store_true", help="Routing analysis")
    parser.add_argument("--top", type=int, default=20, help="Top N for hubs")
    args = parser.parse_args()

    skills_dir = Path(args.skills_dir)
    graph = SkillDependencyGraph(skills_dir)

    if args.topo:
        order, in_cycles = graph.topological_sort()
        if args.json:
            json.dump({"order": order, "in_cycles": in_cycles}, sys.stdout, indent=2)
            print()
        else:
            print(f"=== Topological Sort ({len(order)} ordered, {len(in_cycles)} in cycles) ===")
            for i, skill in enumerate(order[:30]):
                print(f"  {i+1:3d}. {skill}")
            if len(order) > 30:
                print(f"  ... and {len(order) - 30} more")
            if in_cycles:
                print(f"\n  In cycles: {', '.join(in_cycles[:10])}")
        return

    if args.cycles:
        cycles = graph.detect_cycles()
        if args.json:
            json.dump(cycles, sys.stdout, indent=2)
            print()
        else:
            print(f"=== Cycles Detected ({len(cycles)}) ===")
            for c in cycles[:10]:
                print(f"  {' -> '.join(c)}")
        return

    if args.orphans:
        orphans = graph.orphans()
        if args.json:
            json.dump(orphans, sys.stdout, indent=2)
            print()
        else:
            print(f"=== Orphan Skills ({len(orphans)}) ===")
            for o in orphans[:30]:
                print(f"  {o}")
        return

    if args.hubs:
        hubs = graph.hubs(args.top)
        if args.json:
            json.dump(hubs, sys.stdout, indent=2)
            print()
        else:
            print(f"=== Hub Skills (top {len(hubs)}) ===")
            for name, count in hubs:
                print(f"  {name}: {count} dependents")
        return

    if args.routing:
        routing = graph.routing_hubs(args.top)
        if args.json:
            json.dump(routing, sys.stdout, indent=2)
            print()
        else:
            print(f"=== Routing Hubs (top {len(routing)}) ===")
            for name, count in routing:
                print(f"  {name}: routes to {count} skills")
        return

    # Default: full summary
    s = graph.summary()
    if args.json:
        json.dump(s, sys.stdout, indent=2)
        print()
    else:
        print(f"=== Skill Dependency Graph ===")
        print(f"  Total skills:          {s['total_skills']}")
        print(f"  Total dependencies:    {s['total_dependencies']}")
        print(f"  Total routing edges:   {s['total_routing_edges']}")
        print(f"  Orphan skills:         {s['orphan_skills']}")
        print(f"  Cycles detected:       {s['cycles_detected']}")
        print(f"  Nodes in cycles:       {s['nodes_in_cycles']}")
        print(f"  Topo order length:     {s['topological_order_length']}")
        print(f"  Schema versions:       {s['schema_versions']}")
        print(f"  Skill versions:        {s['skill_versions']}")
        print(f"  Stewards:              {s['stewards']}")
        print()
        print(f"  Top 5 Hub Skills:")
        for name, count in graph.hubs(5):
            print(f"    {name}: {count} dependents")
        print()
        print(f"  Top 5 Routing Hubs:")
        for name, count in graph.routing_hubs(5):
            print(f"    {name}: routes to {count} skills")


if __name__ == "__main__":
    main()
