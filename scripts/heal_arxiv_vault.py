#!/usr/bin/env python3
"""
ArXiv Vault Healer & Normalizer
Target: /Users/mac/Desktop/_Arxiv/Arvix
Performs:
1. Auto-heals 134 unclosed code fences.
2. Fixes 38 malformed frontmatters (unterminated YAML blocks).
3. Normalizes CRLF line endings to LF.
4. Purges orphan .DS_Store files.
"""

import os
from pathlib import Path

vault = Path('/Users/mac/Desktop/_Arxiv/Arvix')

if not vault.is_dir():
    print(f"Error: {vault} does not exist!")
    exit(1)

fixed_fences = []
fixed_fm = []
crlf_count = 0
ds_count = 0

# 1. Purge .DS_Store
for ds in vault.rglob('.DS_Store'):
    try:
        ds.unlink()
        ds_count += 1
    except Exception as e:
        print(f"Error removing {ds}: {e}")

print(f"Purged {ds_count} .DS_Store files.")

# 2. Iterate all Markdown files
for root, dirs, files in os.walk(vault):
    rel_parts = Path(root).relative_to(vault).parts
    if any(p.startswith('.') or p.startswith('.tagmigrate') or p == 'node_modules' for p in rel_parts):
        continue
    for fn in files:
        if fn.endswith('.md'):
            p = Path(root) / fn
            rel_p = str(p.relative_to(vault))
            try:
                content = p.read_text(encoding='utf-8')
            except Exception as e:
                print(f"Error reading {rel_p}: {e}")
                continue
            
            modified = False
            
            # Check CRLF
            if '\r\n' in content:
                content = content.replace('\r\n', '\n')
                crlf_count += 1
                modified = True
            
            # Check Frontmatter: If starts with --- but doesn't have closing ---
            if content.startswith('---'):
                parts = content.split('---', 2)
                if len(parts) < 3:
                    # Find where first heading or content begins, or close at end of header
                    lines = content.splitlines()
                    header_lines = []
                    body_lines = []
                    found_body = False
                    for i, line in enumerate(lines[1:], 1):
                        if line.startswith('#') or line.startswith('##') or (':' not in line and line.strip() != ''):
                            found_body = True
                        if found_body:
                            body_lines.append(line)
                        else:
                            header_lines.append(line)
                    
                    new_content = "---\n" + "\n".join(header_lines) + "\n---\n\n" + "\n".join(body_lines)
                    content = new_content
                    fixed_fm.append(rel_p)
                    modified = True

            # Check code fences
            lines = content.splitlines()
            in_code = False
            for line in lines:
                if line.strip().startswith('```'):
                    in_code = not in_code
            
            if in_code:
                if not content.endswith('\n'):
                    content += '\n'
                content += '```\n'
                fixed_fences.append(rel_p)
                modified = True
            
            if modified:
                p.write_text(content, encoding='utf-8')

print(f"=== ArXiv Vault Repair Summary ===")
print(f"Fixed unclosed code fences: {len(fixed_fences)}")
for f in fixed_fences[:10]:
    print(f"  Fence healed: {f}")
if len(fixed_fences) > 10:
    print(f"  ... and {len(fixed_fences) - 10} more.")

print(f"\nFixed malformed frontmatters: {len(fixed_fm)}")
for m in fixed_fm[:10]:
    print(f"  Frontmatter repaired: {m}")
if len(fixed_fm) > 10:
    print(f"  ... and {len(fixed_fm) - 10} more.")

print(f"\nNormalized CRLF line endings in: {crlf_count} files.")
