#!/usr/bin/env python3
import os
import re
import json
import yaml
from pathlib import Path
from collections import defaultdict

vault = Path('/Users/mac/Library/CloudStorage/GoogleDrive-phanqtrang@gmail.com/My Drive/_AMOS_OS')
exclude_dirs = {'.git', '.obsidian', '.gemini', '.copilot', '.claude', '.devin', '.opencode', '.agents', 'scripts'}

all_files = {}        # stem.lower() -> list of Path
rel_paths_lower = {}  # rel_path.lower() -> Path
all_md_files = []

for root, dirs, files in os.walk(vault):
    dirs[:] = [d for d in dirs if not d.startswith('.') and d not in exclude_dirs]
    for fn in files:
        if fn.startswith('.'):
            continue
        p = Path(root) / fn
        rel_p = str(p.relative_to(vault))
        rel_paths_lower[rel_p.lower()] = p
        stem = p.stem.lower()
        all_files.setdefault(stem, []).append(p)
        if fn.endswith('.md'):
            all_md_files.append((p, rel_p))

print(f"Total MD files found: {len(all_md_files)}")

unclosed_fences = []
frontmatter_errors = []
broken_links = defaultdict(list)
total_links = 0
wl_re = re.compile(r"\[\[([^\]|#\n]+?)(?:#[^\]|]*)?(?:\|[^\]\n]*)?\]\]")

for p, rel_p in all_md_files:
    try:
        content = p.read_text(encoding='utf-8', errors='replace')
        lines = content.splitlines()
        in_code = False
        for line in lines:
            if line.strip().startswith('```'):
                in_code = not in_code
        if in_code:
            unclosed_fences.append(rel_p)
            
        if content.startswith('---'):
            parts = content.split('---', 2)
            if len(parts) < 3:
                frontmatter_errors.append((rel_p, 'Unclosed YAML frontmatter'))
            else:
                try:
                    yaml.safe_load(parts[1])
                except Exception as ye:
                    frontmatter_errors.append((rel_p, f'YAML parse error: {ye}'))
        
        clean = re.sub(r'```.*?```', '', content, flags=re.DOTALL)
        links = wl_re.findall(clean)
        for target in links:
            total_links += 1
            t_clean = target.strip()
            if not t_clean or t_clean.startswith('http') or t_clean.startswith('file:'):
                continue
            t_stem = Path(t_clean).stem.lower()
            t_rel = t_clean.lower()
            if t_stem in all_files or t_rel in rel_paths_lower or f"{t_rel}.md" in rel_paths_lower or f"{t_stem}.md" in all_files:
                continue
            broken_links[t_clean].append(rel_p)
    except Exception as e:
        frontmatter_errors.append((rel_p, str(e)))

print(f"Unclosed code fences: {len(unclosed_fences)}")
for uf in unclosed_fences:
    print('  [FENCE]', uf)

print(f"Frontmatter errors: {len(frontmatter_errors)}")
for fe in frontmatter_errors[:20]:
    print(f"  [FM_ERR] {fe[0]}: {fe[1]}")

print(f"Total wikilinks: {total_links}")
print(f"Distinct broken targets: {len(broken_links)}")
for bt in sorted(broken_links.keys(), key=lambda k: len(broken_links[k]), reverse=True)[:25]:
    print(f"  [BROKEN LINK] '{bt}' -> referenced in {len(broken_links[bt])} files")
