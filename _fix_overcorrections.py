#!/usr/bin/env python3
"""
Fix over-corrections from the previous LaTeX restoration script:

1. Revert \(...\) inside $$ display math blocks back to (...) 
   - Inside $$ blocks, parentheses are already math mode
   - \(...\) delimiters are ONLY for inline math outside $$ blocks

2. Fix [[L19_PROOF_CAPSULE]]: back to PROOF_CAPSULE: in YAML code blocks
   - YAML keys should not be wikilinks

3. Fix GOVERNANCE_[[L19_PROOF_CAPSULE]]: back to GOVERNANCE_PROOF_CAPSULE:

4. Fix other over-corrected \(...\) inside $$ blocks:
   - \operatorname{Verdicts}\(e_k\) → \operatorname{Verdicts}(e_k)
   - \operatorname{Cause}\(A\) → \operatorname{Cause}(A)
   - \operatorname{Epoch}\(A\) → \operatorname{Epoch}(A)
   - \operatorname{Epoch}\(C\) → \operatorname{Epoch}(C)
   - \operatorname{Consequence}\(C\) → \operatorname{Consequence}(C)
   - Lineage\(K_t\) → Lineage(K_t)
   - t_{commit}\(Tx_k\) → t_{commit}(Tx_k)
   - t_{start}\(Tx_k\) → t_{start}(Tx_k)
   - Snapshot(t_{start}\(Tx_k\)) → Snapshot(t_{start}(Tx_k))
"""

import re
import os

VAULT_ROOT = "/Users/mac/Documents/AMOS_OS"

def fix_math_block_overcorrections(content):
    """Revert \(...\) to (...) inside $$ display math blocks."""
    lines = content.split('\n')
    in_math = False
    result = []
    
    for line in lines:
        # Track $$ math block state
        if '$$' in line:
            # Count $$ on this line
            dollar_count = line.count('$$')
            if dollar_count == 1:
                in_math = not in_math
                # Process the line itself (it might have content before/after $$)
                # But don't modify the $$ line itself
                result.append(line)
                continue
            elif dollar_count == 2:
                # Both $$ on same line - inline math block, don't change state
                result.append(line)
                continue
        
        if in_math:
            # Inside $$ math block - revert \( to ( and \) to )
            line = line.replace(r'\(', '(').replace(r'\)', ')')
        
        result.append(line)
    
    return '\n'.join(result)

def fix_yaml_wikilink_keys(content):
    """Fix [[L19_PROOF_CAPSULE]]: back to PROOF_CAPSULE: in YAML code blocks."""
    lines = content.split('\n')
    in_code = False
    code_lang = None
    result = []
    
    for line in lines:
        stripped = line.lstrip()
        if stripped.startswith('```'):
            if in_code:
                in_code = False
                code_lang = None
            else:
                in_code = True
                code_lang = stripped[3:].strip()
            result.append(line)
            continue
        
        if in_code and code_lang and 'yaml' in code_lang.lower():
            # Fix YAML keys that were wrongly converted to wikilinks
            # Pattern: [[L19_PROOF_CAPSULE]]: → PROOF_CAPSULE:
            line = re.sub(r'\[\[L19_PROOF_CAPSULE\]\]:', 'PROOF_CAPSULE:', line)
            # Pattern: GOVERNANCE_[[L19_PROOF_CAPSULE]]: → GOVERNANCE_PROOF_CAPSULE:
            line = re.sub(r'GOVERNANCE_\[\[L19_PROOF_CAPSULE\]\]:', 'GOVERNANCE_PROOF_CAPSULE:', line)
            # General: any [[...]]: at start of YAML key line → ...:
            line = re.sub(r'^(\s*)\[\[([A-Z0-9_]+)\]\]:', r'\1\2:', line)
        
        result.append(line)
    
    return '\n'.join(result)

def process_file(filepath):
    """Process a single file with all fixes."""
    with open(filepath, 'r', encoding='utf-8') as f:
        original = f.read()
    
    content = original
    content = fix_math_block_overcorrections(content)
    content = fix_yaml_wikilink_keys(content)
    
    if content != original:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
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
