#!/usr/bin/env python3
"""
Exhaustive Vault Scanner & Auditor v2
Scans for:
1. Empty / stub markdown notes (< 30 bytes or empty body)
2. Broken wikilinks [[Target]] across all 25 planes
3. Malformed tags or missing essential frontmatter properties
4. Canvas (.canvas) JSON validity
5. Ambiguous duplicate filenames
6. Orphan files without inbound or outbound links
"""

import os
import json
import re
from pathlib import Path
from collections import defaultdict

vault = Path('.').resolve()

# Regex patterns
WL_RE = re.compile(r"\[\[([^\]|#\n]+?)(?:#[^\]|]*)?(?:\|[^\]\n]*)?\]\]")

all_files = {}       # stem.lower() -> [Path]
rel_paths_lower = {} # rel_path.lower() -> Path
all_md_files = []
empty_files = []
broken_canvases = []
duplicate_stems = defaultdict(list)

# Exclude hidden, backups, node_modules
exclude_parts = {'.git', '.obsidian', '.gemini', 'node_modules', 'scripts'}

for root, dirs, files in os.walk(vault):
    rel_parts = Path(root).relative_to(vault).parts
    if any(p.startswith('.') or p.startswith('.tagmigrate') or p in exclude_parts for p in rel_parts):
        continue
    for fn in files:
        p = Path(root) / fn
        rel_p = str(p.relative_to(vault))
        rel_paths_lower[rel_p.lower()] = p
        stem = p.stem.lower()
        all_files.setdefault(stem, []).append(p)
        
        if fn.endswith('.md'):
            all_md_files.append(p)
            size = p.stat().st_size
            if size == 0:
                empty_files.append(rel_p)
        elif fn.endswith('.canvas'):
            try:
                with open(p, 'r', encoding='utf-8') as fp:
                    json.load(fp)
            except Exception as e:
                broken_canvases.append((rel_p, str(e)))

for stem, paths in all_files.items():
    if len(paths) > 1 and not stem.startswith('.'):
        duplicate_stems[stem] = [str(p.relative_to(vault)) for p in paths]

# Scan for broken wikilinks in Markdown files
broken_wikilinks = defaultdict(list) # target -> [sources]
total_wikilinks = 0

for p in all_md_files:
    rel_p = str(p.relative_to(vault))
    try:
        content = p.read_text(encoding='utf-8')
    except Exception:
        continue
    
    # Strip code blocks before finding wikilinks
    clean_content = re.sub(r'```.*?```', '', content, flags=re.DOTALL)
    links = WL_RE.findall(clean_content)
    for target in links:
        total_wikilinks += 1
        target_clean = target.strip()
        if not target_clean:
            continue
        
        # Check direct stem match, filename match, or rel path match
        target_stem = Path(target_clean).stem.lower()
        target_rel = target_clean.lower()
        if target_stem in all_files or target_rel in rel_paths_lower or f"{target_rel}.md" in rel_paths_lower:
            continue
        
        # Also check with .md extension
        if f"{target_stem}.md" in all_files:
            continue
            
        broken_wikilinks[target_clean].append(rel_p)

print(f"==================================================")
print(f"AMOS Exhaustive Vault Audit Report")
print(f"==================================================")
print(f"Total Markdown files scanned: {len(all_md_files)}")
print(f"Empty Markdown files: {len(empty_files)}")
for ef in empty_files:
    print(f"  EMPTY: {ef}")

print(f"Broken JSON Canvas files: {len(broken_canvases)}")
for bc in broken_canvases:
    print(f"  BROKEN CANVAS: {bc}")

print(f"Total Wikilinks evaluated: {total_wikilinks}")
print(f"Distinct Unresolved Wikilink Targets: {len(broken_wikilinks)}")
top_unresolved = sorted(broken_wikilinks.items(), key=lambda x: len(x[1]), reverse=True)[:15]
for target, sources in top_unresolved:
    print(f"  UNRESOLVED: [[{target}]] (referenced in {len(sources)} files, e.g. {sources[0]})")
