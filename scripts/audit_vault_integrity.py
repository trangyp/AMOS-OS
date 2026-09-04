#!/usr/bin/env python3
import os
import json
import re
from pathlib import Path

vault = Path('.').resolve()

unclosed_fences = []
malformed_frontmatter = []
total_md = 0
total_json = 0
broken_json = []

for root, dirs, files in os.walk(vault):
    rel_parts = Path(root).relative_to(vault).parts
    if any(p.startswith('.') or p.startswith('.tagmigrate') or p == 'node_modules' for p in rel_parts):
        continue
    for fn in files:
        p = Path(root) / fn
        rel_p = str(p.relative_to(vault))
        if fn.endswith('.md'):
            total_md += 1
            try:
                content = p.read_text(encoding='utf-8')
            except Exception as e:
                malformed_frontmatter.append((rel_p, f'Read error: {e}'))
                continue
            
            if content.startswith('---'):
                parts = content.split('---', 2)
                if len(parts) < 3:
                    malformed_frontmatter.append((rel_p, 'Unterminated frontmatter'))
            
            lines = content.splitlines()
            in_code = False
            for line in lines:
                if line.strip().startswith('```'):
                    in_code = not in_code
            if in_code:
                unclosed_fences.append(rel_p)
                
        elif fn.endswith('.json'):
            total_json += 1
            try:
                with open(p, 'r', encoding='utf-8') as fp:
                    json.load(fp)
            except Exception as e:
                broken_json.append((rel_p, str(e)))

print(f"Scanned {total_md} Markdown files and {total_json} JSON files.")
print(f"Malformed frontmatter: {len(malformed_frontmatter)}")
for m in malformed_frontmatter:
    print(f"  FM ERR: {m}")
print(f"Unclosed code fences: {len(unclosed_fences)}")
for u in unclosed_fences:
    print(f"  FENCE ERR: {u}")
print(f"Broken JSON files: {len(broken_json)}")
for b in broken_json:
    print(f"  JSON ERR: {b}")
