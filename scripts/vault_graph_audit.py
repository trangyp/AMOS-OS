#!/usr/bin/env python3
"""
AMOS Vault Graph Auditor — Knowledge graph integrity analysis.

Parses an Obsidian vault into a directed graph (files = nodes, wikilinks = edges)
and reports structural health metrics inspired by SOTA knowledge graph tools:

  - obra/knowledge-graph: Louvain communities, PageRank, bridge nodes, paths
  - yanxue06/obsidian-mcp: Graph-aware traversal, backlink rewriting
  - Rajveerx11/obsidian-graph-intelligence: Orphan detection, cluster discovery
  - Data-Wise/obsidian-cli-ops: Hub detection, broken links, centrality
  - Android-Tipster/vault-weaver: Missing backlinks, duplicate detection, gaps

Usage:
  python3 scripts/vault_graph_audit.py                    # full audit
  python3 scripts/vault_graph_audit.py --json              # JSON output
  python3 scripts/vault_graph_audit.py --orphans           # list orphans only
  python3 scripts/vault_graph_audit.py --broken            # list broken links only
  python3 scripts/vault_graph_audit.py --hubs              # list hub nodes only
  python3 scripts/vault_graph_audit.py --path A B          # find paths A->B
"""

import argparse
import json
import re
import sys
from collections import defaultdict, Counter
from pathlib import Path

try:
    import yaml
except ImportError:
    print("ERROR: PyYAML required. Install: pip install pyyaml", file=sys.stderr)
    sys.exit(2)


# ── Graph Builder ────────────────────────────────────────────────────────────

WL_RE = re.compile(r"\[\[([^\]|#\n]+?)(?:#[^\]|]*)?(?:\|[^\]\n]*)?\]\]")


class VaultGraph:
    """Directed graph of an Obsidian vault: nodes = files, edges = wikilinks."""

    def __init__(self, vault_path: Path, exclude_dirs: set = None):
        self.vault_path = vault_path
        self.exclude_dirs = exclude_dirs or {".obsidian", ".git", "node_modules"}
        self.nodes = {}           # stem -> Path
        self.edges = defaultdict(set)  # src_stem -> set(target_stems)
        self.backlinks = defaultdict(set)  # target_stem -> set(src_stems)
        self.broken_links = []     # (src_path, target)
        self.all_files = []
        self._build()

    def _should_exclude(self, path: Path) -> bool:
        parts = path.relative_to(self.vault_path).parts
        return any(p in self.exclude_dirs for p in parts)

    def _build(self):
        # Collect all markdown files
        for f in self.vault_path.rglob("*.md"):
            if self._should_exclude(f):
                continue
            self.all_files.append(f)
            self.nodes[f.stem] = f

        # Parse wikilinks
        for f in self.all_files:
            try:
                text = f.read_text(encoding="utf-8", errors="replace")
            except Exception:
                continue
            src_stem = f.stem
            for m in WL_RE.finditer(text):
                target = m.group(1).strip()
                if not target:
                    continue
                if target in self.nodes:
                    self.edges[src_stem].add(target)
                    self.backlinks[target].add(src_stem)
                else:
                    # Check if file exists with .md extension
                    target_path = self.vault_path / f"{target}.md"
                    if target_path.exists():
                        self.edges[src_stem].add(target)
                        self.backlinks[target].add(src_stem)
                    else:
                        self.broken_links.append((str(f.relative_to(self.vault_path)), target))

    # ── Metrics ──────────────────────────────────────────────────────────────

    def orphans(self) -> list[str]:
        """Nodes with no incoming links (no backlinks)."""
        return sorted([s for s in self.nodes if s not in self.backlinks or not self.backlinks[s]])

    def hubs(self, top_n: int = 20) -> list[tuple[str, int]]:
        """Nodes ranked by incoming link count (PageRank-like)."""
        counts = [(s, len(self.backlinks[s])) for s in self.nodes]
        return sorted(counts, key=lambda x: -x[1])[:top_n]

    def sinks(self, top_n: int = 20) -> list[tuple[str, int]]:
        """Nodes with many outgoing links but few incoming."""
        results = []
        for s in self.nodes:
            out_count = len(self.edges.get(s, set()))
            in_count = len(self.backlinks.get(s, set()))
            if out_count > 5 and in_count == 0:
                results.append((s, out_count))
        return sorted(results, key=lambda x: -x[1])[:top_n]

    def density(self) -> float:
        """Graph density = edges / (nodes * (nodes-1))."""
        n = len(self.nodes)
        if n < 2:
            return 0.0
        total_edges = sum(len(targets) for targets in self.edges.values())
        return total_edges / (n * (n - 1))

    def avg_links(self) -> float:
        """Average outgoing links per node."""
        if not self.nodes:
            return 0.0
        total = sum(len(t) for t in self.edges.values())
        return total / len(self.nodes)

    def connected_components(self) -> list[set[str]]:
        """Find weakly connected components via BFS."""
        visited = set()
        components = []
        for node in self.nodes:
            if node in visited:
                continue
            # BFS (treat edges as undirected)
            queue = [node]
            component = set()
            while queue:
                current = queue.pop(0)
                if current in visited:
                    continue
                visited.add(current)
                component.add(current)
                # Forward edges
                for target in self.edges.get(current, set()):
                    if target not in visited:
                        queue.append(target)
                # Backward edges
                for src in self.backlinks.get(current, set()):
                    if src not in visited:
                        queue.append(src)
            components.append(component)
        return sorted(components, key=len, reverse=True)

    def find_paths(self, start: str, end: str, max_depth: int = 5) -> list[list[str]]:
        """Find all simple paths from start to end (DFS, max_depth)."""
        if start not in self.nodes or end not in self.nodes:
            return []
        paths = []
        def dfs(current, path, depth):
            if depth > max_depth:
                return
            if current == end:
                paths.append(path[:])
                return
            for target in self.edges.get(current, set()):
                if target not in path:
                    dfs(target, path + [target], depth + 1)
        dfs(start, [start], 0)
        return paths

    def summary(self) -> dict:
        components = self.connected_components()
        largest = components[0] if components else set()
        return {
            "total_nodes": len(self.nodes),
            "total_edges": sum(len(t) for t in self.edges.values()),
            "broken_links": len(self.broken_links),
            "orphan_nodes": len(self.orphans()),
            "density": round(self.density(), 6),
            "avg_links_per_node": round(self.avg_links(), 2),
            "connected_components": len(components),
            "largest_component_size": len(largest),
            "largest_component_pct": round(100 * len(largest) / max(len(self.nodes), 1), 1),
        }


# ── CLI ──────────────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(description="AMOS Vault Graph Auditor")
    parser.add_argument("vault", nargs="?", default=".", help="Vault directory")
    parser.add_argument("--json", action="store_true", help="JSON output")
    parser.add_argument("--orphans", action="store_true", help="List orphan nodes")
    parser.add_argument("--broken", action="store_true", help="List broken links")
    parser.add_argument("--hubs", action="store_true", help="List hub nodes")
    parser.add_argument("--sinks", action="store_true", help="List sink nodes")
    parser.add_argument("--components", action="store_true", help="List connected components")
    parser.add_argument("--path", nargs=2, metavar=("START", "END"), help="Find paths")
    parser.add_argument("--top", type=int, default=20, help="Top N for hubs/sinks")
    args = parser.parse_args()

    vault = Path(args.vault)
    graph = VaultGraph(vault)

    if args.orphans:
        orphans = graph.orphans()
        if args.json:
            json.dump(orphans, sys.stdout, indent=2)
            print()
        else:
            print(f"=== Orphan Nodes ({len(orphans)}) ===")
            for o in orphans[:50]:
                print(f"  {o}")
            if len(orphans) > 50:
                print(f"  ... and {len(orphans) - 50} more")
        return

    if args.broken:
        if args.json:
            json.dump(graph.broken_links, sys.stdout, indent=2)
            print()
        else:
            print(f"=== Broken Wikilinks ({len(graph.broken_links)}) ===")
            for src, target in graph.broken_links[:50]:
                print(f"  {src} -> [[{target}]]")
            if len(graph.broken_links) > 50:
                print(f"  ... and {len(graph.broken_links) - 50} more")
        return

    if args.hubs:
        hubs = graph.hubs(args.top)
        if args.json:
            json.dump(hubs, sys.stdout, indent=2)
            print()
        else:
            print(f"=== Hub Nodes (top {len(hubs)}) ===")
            for stem, count in hubs:
                print(f"  {stem}: {count} incoming links")
        return

    if args.sinks:
        sinks = graph.sinks(args.top)
        if args.json:
            json.dump(sinks, sys.stdout, indent=2)
            print()
        else:
            print(f"=== Sink Nodes ({len(sinks)}) ===")
            for stem, count in sinks:
                print(f"  {stem}: {count} outgoing, 0 incoming")
        return

    if args.components:
        comps = graph.connected_components()
        if args.json:
            json.dump([list(c) for c in comps[:20]], sys.stdout, indent=2)
            print()
        else:
            print(f"=== Connected Components ({len(comps)}) ===")
            for i, c in enumerate(comps[:20]):
                print(f"  Component {i+1}: {len(c)} nodes")
        return

    if args.path:
        start, end = args.path
        paths = graph.find_paths(start, end)
        if args.json:
            json.dump(paths, sys.stdout, indent=2)
            print()
        else:
            print(f"=== Paths: {start} -> {end} ({len(paths)} found) ===")
            for p in paths[:10]:
                print(f"  {' -> '.join(p)}")
        return

    # Default: full summary
    s = graph.summary()
    if args.json:
        json.dump(s, sys.stdout, indent=2)
        print()
    else:
        print(f"=== Vault Graph Audit ===")
        print(f"  Nodes:              {s['total_nodes']}")
        print(f"  Edges:              {s['total_edges']}")
        print(f"  Broken links:       {s['broken_links']}")
        print(f"  Orphan nodes:       {s['orphan_nodes']}")
        print(f"  Density:            {s['density']}")
        print(f"  Avg links/node:     {s['avg_links_per_node']}")
        print(f"  Components:         {s['connected_components']}")
        print(f"  Largest component:  {s['largest_component_size']} ({s['largest_component_pct']}%)")
        print()
        print(f"  Top 5 Hubs:")
        for stem, count in graph.hubs(5):
            print(f"    {stem}: {count} incoming")
        print()
        print(f"  Top 5 Sinks:")
        for stem, count in graph.sinks(5):
            print(f"    {stem}: {count} outgoing, 0 incoming")


if __name__ == "__main__":
    main()
