#!/usr/bin/env python3
"""
Strip blank lines from inside YAML frontmatter blocks in all .md files.
A frontmatter block starts with --- on line 1 and ends with the next ---.
Blank lines within that block are removed.
"""

import os

VAULT_ROOT = "/Users/mac/Documents/AMOS_OS"

def strip_frontmatter_blanks(filepath):
    """Remove blank lines from inside frontmatter. Returns True if changed."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if not content.startswith('---\n'):
        return False
    
    lines = content.split('\n')
    
    # Find closing ---
    closing = None
    for i in range(1, len(lines)):
        if lines[i].strip() == '---':
            closing = i
            break
    
    if closing is None:
        return False
    
    fm_lines = lines[1:closing]
    body_lines = lines[closing:]
    
    # Remove blank lines from frontmatter
    new_fm_lines = [l for l in fm_lines if l.strip() != '']
    
    if new_fm_lines == fm_lines:
        return False
    
    new_lines = ['---'] + new_fm_lines + body_lines
    new_content = '\n'.join(new_lines)
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_content)
    return True

if __name__ == '__main__':
    fixed = 0
    skipped = 0
    errors = 0
    
    for dp, _, fns in os.walk(VAULT_ROOT):
        if '.git' in dp or 'node_modules' in dp:
            continue
        for fn in fns:
            if not fn.endswith('.md'):
                continue
            p = os.path.join(dp, fn)
            try:
                if strip_frontmatter_blanks(p):
                    fixed += 1
                else:
                    skipped += 1
            except Exception as e:
                errors += 1
                if errors <= 5:
                    print(f"  ERROR: {p}: {e}")
    
    print(f"\nDone. Fixed {fixed} files. Skipped {skipped}. Errors: {errors}.")
