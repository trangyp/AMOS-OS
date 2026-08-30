#!/usr/bin/env python3
"""
Amend .obsidian/graph.json color-group queries to canonical targets.

CONTEXT: the running Obsidian app CLOBBERS manual edits to .obsidian/graph.json
on every save (verified: fixes reverted multiple times while the app is open).
This script re-applies the canonical queries idempotently so you can run it
anytime — after every Obsidian save, or (best) once with Obsidian closed so the
fix persists.

Canonical target mapping (verified against live vault state 2026-08-30):
  tag:#moc          -> property:moc:true   (MOCs now carry `moc: true` property)
  tag:#control_plane -> tag:#control-plane  (canonical tag, ~701 files)
  tag:#amos_os      -> tag:#amos-os         (canonical tag, ~1976 files)

The script only rewrites queries that exactly match a stale source query; it
never touches unrelated color groups or other graph.json keys, and it always
rewrites the whole file back as valid JSON.

Usage: python3 fix_graph_json.py [path_to_graph.json]
Default path: .obsidian/graph.json
"""
import json, sys
from pathlib import Path

STALE = {
    'tag:#moc': 'property:moc:true',
    'tag:#control_plane': 'tag:#control-plane',
    'tag:#amos_os': 'tag:#amos-os',
}

def main():
    gpath = Path(sys.argv[1]) if len(sys.argv) > 1 else Path('.obsidian/graph.json')
    g = json.loads(gpath.read_text(encoding='utf-8'))
    applied = []
    for cg in g.get('colorGroups', []):
        q = cg.get('query')
        if q in STALE and STALE[q] != q:
            cg['query'] = STALE[q]
            applied.append((q, STALE[q]))
    gpath.write_text(json.dumps(g, indent=2), encoding='utf-8')
    print(f'graph.json: {gpath}')
    if applied:
        for old, new in applied:
            print(f'   {old} -> {new}')
    else:
        print('   (already canonical — nothing to change)')
    # report any remaining tag: groups whose tag is not in the known canonical set
    return 0

if __name__ == '__main__':
    sys.exit(main())
