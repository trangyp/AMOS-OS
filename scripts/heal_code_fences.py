#!/usr/bin/env python3
import os
from pathlib import Path

vault = Path('.').resolve()
fixed_files = []

for root, dirs, files in os.walk(vault):
    rel_parts = Path(root).relative_to(vault).parts
    if any(p.startswith('.') or p.startswith('.tagmigrate') or p == 'node_modules' for p in rel_parts):
        continue
    for fn in files:
        if fn.endswith('.md'):
            p = Path(root) / fn
            try:
                content = p.read_text(encoding='utf-8')
            except Exception as e:
                print(f"Error reading {p}: {e}")
                continue
            
            lines = content.splitlines()
            in_code = False
            for line in lines:
                if line.strip().startswith('```'):
                    in_code = not in_code
            
            if in_code:
                # Add closing code fence
                if not content.endswith('\n'):
                    content += '\n'
                content += '```\n'
                p.write_text(content, encoding='utf-8')
                fixed_files.append(str(p.relative_to(vault)))

print(f"Successfully auto-healed code fences in {len(fixed_files)} Markdown files.")
for f in fixed_files[:10]:
    print(f"  Fixed: {f}")
if len(fixed_files) > 10:
    print(f"  ... and {len(fixed_files) - 10} more.")
