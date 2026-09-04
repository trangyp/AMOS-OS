#!/usr/bin/env python3
import os
import sys
import json
import re
import yaml
from pathlib import Path
from collections import defaultdict
from concurrent.futures import ThreadPoolExecutor

vault = Path('.').resolve()
exclude_dirs = {'.git', '.obsidian', '.gemini', '.copilot', '.claude', '.devin', '.opencode', '.agents', 'node_modules', 'scripts'}

all_files = {}        # stem.lower() -> list of Path
rel_paths_lower = {}  # rel_path.lower() -> Path
all_md_files = []
broken_canvases = []
broken_json = []

print("1. Indexing file tree...", flush=True)
for root, dirs, files in os.walk(vault):
    dirs[:] = [d for d in dirs if not d.startswith('.') and not d.startswith('.tagmigrate') and d not in exclude_dirs]
    for fn in files:
        if fn.startswith('.'):
            continue
        p = Path(root) / fn
        rel_p = str(p.relative_to(vault))
        rel_paths_lower[rel_p.lower()] = p
        stem = p.stem.lower()
        all_files.setdefault(stem, []).append(p)
        if fn.endswith('.md'):
            all_md_files.append(p)
        elif fn.endswith('.canvas'):
            broken_canvases.append((p, rel_p))
        elif fn.endswith('.json'):
            broken_json.append((p, rel_p))

print(f"Indexed {len(all_files)} unique stems, {len(all_md_files)} markdown files.", flush=True)

# Inspect JSON & Canvas files
invalid_json = []
for p, rel_p in broken_json:
    try:
        with open(p, 'r', encoding='utf-8') as fp:
            json.load(fp)
    except Exception as e:
        invalid_json.append((rel_p, str(e)))

invalid_canvas = []
for p, rel_p in broken_canvases:
    try:
        with open(p, 'r', encoding='utf-8') as fp:
            json.load(fp)
    except Exception as e:
        invalid_canvas.append((rel_p, str(e)))

print("2. Scanning markdown files in parallel...", flush=True)
empty_files = []
unclosed_fences = []
malformed_frontmatter = []
broken_wikilinks = defaultdict(list)
total_wikilinks = 0

WL_RE = re.compile(r"\[\[([^\]|#\n]+?)(?:#[^\]|]*)?(?:\|[^\]\n]*)?\]\]")

def scan_file(p):
    rel_p = str(p.relative_to(vault))
    res = {
        'empty': False,
        'fence_err': False,
        'fm_err': None,
        'broken_links': [],
        'total_links': 0
    }
    try:
        sz = p.stat().st_size
        if sz == 0:
            res['empty'] = True
            return rel_p, res
        content = p.read_text(encoding='utf-8', errors='replace')
        if content.startswith('---'):
            parts = content.split('---', 2)
            if len(parts) < 3:
                res['fm_err'] = 'Unclosed YAML frontmatter'
            else:
                try:
                    yaml.safe_load(parts[1])
                except Exception as ye:
                    res['fm_err'] = f'YAML parse error: {ye}'
        lines = content.splitlines()
        in_code = False
        for line in lines:
            if line.strip().startswith('```'):
                in_code = not in_code
        if in_code:
            res['fence_err'] = True
        
        # Wikilinks: collect non-code lines
        non_code_lines = []
        in_fence = False
        for line in lines:
            if line.strip().startswith('```'):
                in_fence = not in_fence
                continue
            if not in_fence:
                non_code_lines.append(line)
        clean_content = "\n".join(non_code_lines)
        links = WL_RE.findall(clean_content)
        for target in links:
            res['total_links'] += 1
            target_clean = target.strip()
            if not target_clean:
                continue
            target_stem = Path(target_clean).stem.lower()
            target_rel = target_clean.lower()
            if target_stem in all_files or target_rel in rel_paths_lower or f"{target_rel}.md" in rel_paths_lower or f"{target_stem}.md" in all_files:
                continue
            res['broken_links'].append(target_clean)
    except Exception as e:
        res['fm_err'] = f'Read exception: {e}'
    return rel_p, res

with ThreadPoolExecutor(max_workers=32) as executor:
    results = list(executor.map(scan_file, all_md_files))

for rel_p, res in results:
    if res['empty']:
        empty_files.append(rel_p)
    if res['fence_err']:
        unclosed_fences.append(rel_p)
    if res['fm_err']:
        malformed_frontmatter.append((rel_p, res['fm_err']))
    total_wikilinks += res['total_links']
    for bl in res['broken_links']:
        broken_wikilinks[bl].append(rel_p)

print("\n" + "="*60, flush=True)
print("AUDIT SCAN RESULTS", flush=True)
print("="*60, flush=True)
print(f"Total Markdown Files: {len(all_md_files)}")
print(f"Empty Markdown Files: {len(empty_files)}")
for ef in empty_files:
    print(f"  [EMPTY] {ef}")

print(f"\nUnclosed Code Fences: {len(unclosed_fences)}")
for uf in unclosed_fences:
    print(f"  [UNCLOSED FENCE] {uf}")

print(f"\nMalformed / Erroneous Frontmatter: {len(malformed_frontmatter)}")
for mf in malformed_frontmatter:
    print(f"  [FRONTMATTER ERROR] {mf[0]}: {mf[1]}")

print(f"\nBroken JSON Files: {len(invalid_json)}")
for bj in invalid_json:
    print(f"  [BROKEN JSON] {bj[0]}: {bj[1]}")

print(f"\nBroken Canvas Files: {len(invalid_canvas)}")
for bc in invalid_canvas:
    print(f"  [BROKEN CANVAS] {bc[0]}: {bc[1]}")

print(f"\nTotal Wikilinks Evaluated: {total_wikilinks}")
print(f"Distinct Broken / Unresolved Wikilink Targets: {len(broken_wikilinks)}")
top_broken = sorted(broken_wikilinks.items(), key=lambda x: len(x[1]), reverse=True)[:40]
for target, sources in top_broken:
    print(f"  [UNRESOLVED WIKILINK] [[{target}]] (referenced {len(sources)} times, e.g. in {sources[0]})")

print("\nAudit scan complete.", flush=True)
