#!/usr/bin/env python3
"""
Restore stripped wikilinks in **Related:** lines.

mdformat-wikilink stripped [[...]] from wikilinks pointing to non-existent notes.
In "Related" lines, ALL items should be wikilinks. Restore bare ALL_CAPS names.
"""

import re
import os

VAULT_ROOT = "/Users/mac/Documents/AMOS_OS"

def fix_related_line(line):
    """Fix **Related:** line by wrapping bare identifiers in [[ ]]"""
    if '**Related:**' not in line:
        return line
    
    # Split by · and process each part
    parts = line.split('·')
    result = []
    for part in parts:
        stripped = part.strip()
        # Remove **Related:** prefix for checking
        content = stripped.replace('**Related:**', '').strip()
        
        # Check if it's a bare identifier that should be a wikilink
        # Pattern: ALL_CAPS with underscores, or mixed case with underscores
        # But NOT already wrapped in [[ ]]
        if content and not content.startswith('[['):
            # Match identifiers that look like note names:
            # - ALL_CAPS_WITH_UNDERSCORES (at least 3 chars)
            # - Mixed_Case_With_Underscores
            # - LXX_XXXX (law names)
            if re.match(r'^[A-Z][A-Z0-9_]{2,}$', content) or \
               re.match(r'^[A-Z][a-zA-Z0-9_]+_[A-Za-z0-9_]+$', content) or \
               re.match(r'^L\d+_', content) or \
               re.match(r'^AMOS_[A-Z]', content) or \
               re.match(r'^[A-Z][A-Z_]+_CANON$', content) or \
               re.match(r'^[A-Z][A-Z_]+_CONTRACT$', content) or \
               re.match(r'^[A-Z][A-Z_]+_MAP$', content) or \
               re.match(r'^[A-Z][A-Z_]+_MOC$', content) or \
               re.match(r'^[A-Z][A-Z_]+_README$', content) or \
               re.match(r'^CORE_LAWS_[A-Z_]+$', content) or \
               re.match(r'^ROUTING_[A-Z_]+$', content) or \
               re.match(r'^AUTHZ_[A-Z_]+$', content) or \
               re.match(r'^VALIDATION_[A-Z_]+$', content) or \
               re.match(r'^PROOF_[A-Z_]+$', content) or \
               re.match(r'^HML_[A-Z_]+$', content):
                # Wrap in [[ ]]
                # Preserve leading **Related:** and whitespace
                if '**Related:**' in part:
                    prefix = part[:part.index('**Related:**') + len('**Related:**')]
                    rest = part[len(prefix):].lstrip()
                    if rest == content:
                        part = prefix + ' [[' + content + ']]'
                else:
                    # Just the content part
                    leading_space = part[:len(part) - len(part.lstrip())]
                    part = leading_space + '[[' + content + ']]'
        
        result.append(part)
    
    return '·'.join(result)

def process_file(filepath):
    """Process a single file."""
    with open(filepath, 'r', encoding='utf-8') as f:
        original = f.read()
    
    lines = original.split('\n')
    new_lines = []
    changed = False
    
    for line in lines:
        new_line = fix_related_line(line)
        if new_line != line:
            changed = True
        new_lines.append(new_line)
    
    if changed:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write('\n'.join(new_lines))
        return True
    return False

if __name__ == '__main__':
    root_dirs = [
        os.path.join(VAULT_ROOT, "01_CANON"),
        os.path.join(VAULT_ROOT, "25_COGNITIVE_MATRIX"),
    ]
    
    fixed_count = 0
    total = 0
    
    for root_dir in root_dirs:
        for dirpath, dirnames, filenames in os.walk(root_dir):
            dirnames[:] = [d for d in dirnames if not d.startswith('.')]
            for fname in filenames:
                if not fname.endswith('.md'):
                    continue
                total += 1
                fpath = os.path.join(dirpath, fname)
                try:
                    if process_file(fpath):
                        fixed_count += 1
                        print(f"  FIXED: {fpath}")
                except Exception as e:
                    print(f"  ERROR: {fpath}: {e}")
    
    print(f"\nDone. Fixed {fixed_count}/{total} files.")
