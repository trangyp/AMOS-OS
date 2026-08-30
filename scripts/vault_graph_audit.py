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
from typing import Optional

try:
    import yaml
except ImportError:
    print("ERROR: PyYAML required. Install: pip install pyyaml", file=sys.stderr)
    sys.exit(2)


# ── Graph Builder ────────────────────────────────────────────────────────────

WL_RE = re.compile(r"\[\[([^\]|#\n]+?)(?:#[^\]|]*)?(?:\|[^\]\n]*)?\]\]")
MD_RE = re.compile(r"\[[^\]\n]+\]\(([^)\s\n]+)\)")


class VaultGraph:
    """Directed graph of an Obsidian vault: nodes = files (by rel path), edges = wikilinks."""

    def __init__(self, vault_path: Path, exclude_dirs: set = None):
        self.vault_path = vault_path
        self.exclude_dirs = exclude_dirs or {".obsidian", ".git", "node_modules", ".gemini", "copilot", "scripts", ".devin"}
        self.noparse_dirs = {"raw", "_arxiv_md"}
        self.nodes = {}           # rel_path (posix) -> Path
        self.edges = defaultdict(set)  # src_relpath -> set(target_relpaths)
        self.backlinks = defaultdict(set)  # target_relpath -> set(src_relpaths)
        self.broken_links = []     # (src_relpath, target)
        self.ambiguous_links = []  # (src_relpath, target)
        self.all_files = []
        self._nodes_by_stem = defaultdict(list)
        self._nodes_by_title = defaultdict(list)
        self._relpaths_lower = {}
        self._build()

    def _should_exclude(self, path: Path) -> bool:
        parts = path.relative_to(self.vault_path).parts
        return any(p.startswith(".") or p in self.exclude_dirs or ("backup" in p.lower() and "20_OPERATIONS" not in parts) for p in parts)

    def _should_parse_links(self, path: Path) -> bool:
        parts = path.relative_to(self.vault_path).parts
        return not any(p in self.noparse_dirs for p in parts)

    def _build(self):
        # Collect all markdown files
        for f in self.vault_path.rglob("*.md"):
            if self._should_exclude(f):
                continue
            self.all_files.append(f)
            relpath = f.relative_to(self.vault_path).as_posix()
            self.nodes[relpath] = f
            self._nodes_by_stem[f.stem].append(relpath)
            self._relpaths_lower[relpath.lower()] = relpath

        # Parse frontmatter titles for title-based wikilink resolution
        import yaml
        for f in self.all_files:
            relpath = f.relative_to(self.vault_path).as_posix()
            try:
                text = f.read_text(encoding="utf-8", errors="replace")
            except Exception:
                continue
            if text.startswith("---"):
                parts = text.split("---", 2)
                if len(parts) >= 3:
                    try:
                        fm = yaml.safe_load(parts[1]) or {}
                        title = fm.get("title")
                        if isinstance(title, str):
                            self._nodes_by_title[title].append(relpath)
                    except Exception:
                        pass

        # Parse wikilinks and markdown links
        for f in self.all_files:
            try:
                text = f.read_text(encoding="utf-8", errors="replace")
            except Exception:
                continue
            src_relpath = f.relative_to(self.vault_path).as_posix()
            if not self._should_parse_links(f):
                continue

            for m in WL_RE.finditer(text):
                raw_target = m.group(1).strip()
                if not raw_target or raw_target.isdigit():
                    continue
                if re.search(r'[^A-Za-z0-9_\s\-.→:/%]', raw_target):
                    continue
                target = self._resolve_target(src_relpath, raw_target)
                if target:
                    self.edges[src_relpath].add(target)
                    self.backlinks[target].add(src_relpath)
                else:
                    self.broken_links.append((src_relpath, raw_target))

            for m in MD_RE.finditer(text):
                raw_target = m.group(1).strip().split("#")[0].split("?")[0]
                if not raw_target:
                    continue
                # Skip image/embedding links: ![...](...)
                if m.start() > 0 and text[m.start() - 1] == "!":
                    continue
                # Strip optional angle brackets used by some exports.
                if raw_target.startswith("<") and raw_target.endswith(">"):
                    raw_target = raw_target[1:-1]
                if not raw_target:
                    continue
                if raw_target.startswith(("http://", "https://", "mailto:", "//")):
                    continue
                # Only treat internal vault markdown links as graph edges.
                suffix = Path(raw_target).suffix
                if suffix and suffix != ".md":
                    continue
                target = self._resolve_target(src_relpath, raw_target)
                if target:
                    self.edges[src_relpath].add(target)
                    self.backlinks[target].add(src_relpath)
                else:
                    self.broken_links.append((src_relpath, raw_target))

    def _resolve_target(self, src_relpath: str, raw_target: str) -> Optional[str]:
        """Resolve a wikilink or markdown link target to a canonical relative path."""
        raw_target = raw_target.strip()
        if not raw_target:
            return None

        src_path = Path(src_relpath)
        src_dir = src_path.parent
        # Strip .md suffix for stem/title lookups; keep raw_target for path lookups.
        lookup = raw_target[:-3] if raw_target.endswith(".md") else raw_target

        # 1. Path-prefixed or relative link
        if "/" in raw_target or raw_target.endswith(".md"):
            rel_md = raw_target if raw_target.endswith(".md") else raw_target + ".md"
            # Check relative to source note directory first
            src_target = (self.vault_path / src_dir / rel_md).resolve()
            if src_target.is_file() and src_target.is_relative_to(self.vault_path.resolve()):
                return src_target.relative_to(self.vault_path.resolve()).as_posix()
            # Check relative to vault root
            target_path = (self.vault_path / rel_md).resolve()
            if target_path.is_file() and target_path.is_relative_to(self.vault_path.resolve()):
                return target_path.relative_to(self.vault_path.resolve()).as_posix()
            # Case-insensitive fallback
            lower = rel_md.lower()
            if lower in self._relpaths_lower:
                return self._relpaths_lower[lower]

        def _pick(candidates: list[str]) -> Optional[str]:
            if not candidates:
                return None
            if len(candidates) == 1:
                return candidates[0]

            # Prefer the candidate in the same directory as the source note.
            same_dir = [c for c in candidates if Path(c).parent == src_dir]
            if len(same_dir) == 1:
                return same_dir[0]

            # Prefer candidates under the same parent folder, then closest by
            # longest common path prefix and shortest overall path length.
            def score(c: str) -> tuple[int, int, int]:
                c_parts = Path(c).parts
                common = 0
                for a, b in zip(src_path.parts, c_parts):
                    if a == b:
                        common += 1
                    else:
                        break
                # Extra points if the candidate is inside the source directory.
                under_src = 1 if src_dir in Path(c).parents or Path(c).parent == src_dir else 0
                return (under_src, common, -len(c_parts))

            ranked = sorted(candidates, key=score, reverse=True)
            best_score = score(ranked[0])
            top = [c for c in ranked if score(c) == best_score]
            if len(top) == 1:
                return top[0]
            return None  # still ambiguous

        # 2. Title-based resolution
        if lookup in self._nodes_by_title:
            picked = _pick(self._nodes_by_title[lookup])
            if picked:
                return picked

        # 3. Stem-based resolution
        if lookup in self._nodes_by_stem:
            candidates = self._nodes_by_stem[lookup]
            picked = _pick(candidates)
            if picked:
                return picked
            if len(candidates) > 1:
                self.ambiguous_links.append((src_relpath, raw_target))
                return None  # ambiguous stem (e.g. SKILL without a path)

        # 4. Case-insensitive stem fallback
        lower = lookup.lower()
        matched_stems = [s for s in self._nodes_by_stem if s.lower() == lower]
        if len(matched_stems) == 1:
            picked = _pick(self._nodes_by_stem[matched_stems[0]])
            if picked:
                return picked

        # 5. Root-level file check
        target_path = (self.vault_path / f"{lookup}.md").resolve()
        if target_path.exists() and target_path.is_file() and target_path.is_relative_to(self.vault_path.resolve()):
            return target_path.relative_to(self.vault_path.resolve()).as_posix()

        return None

    # ── Metrics ──────────────────────────────────────────────────────────────

    def orphans(self) -> list[str]:
        """Nodes with no incoming links (no backlinks)."""
        return sorted([relpath for relpath in self.nodes if not self.backlinks.get(relpath)])

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
