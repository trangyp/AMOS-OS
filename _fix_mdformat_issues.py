#!/usr/bin/env python3
"""
Fix issues introduced by mdformat on AMOS_OS vault files:

1. ___ thematic breaks (3+ underscores) and long underscore lines → ---
2. Stripped wikilinks: [[K_ATOMIC_MULTI_RSCF]], [[AMOS_FRACTAL_KNOWLEDGE_NETWORK]], [[PROOF_CAPSULE]]
3. LaTeX \( \) inline math delimiters stripped to ( )
4. Escaped asterisks inside former LaTeX: p^\* → p^*
"""

import re
import os
import sys

VAULT_ROOT = "/Users/mac/Documents/AMOS_OS"

# ─── 1. Thematic break fix: ___ (any length ≥ 3) → --- ───

def fix_thematic_breaks(content):
    """Convert ___ and long underscore lines back to ---"""
    # Match lines that are only underscores (3 or more)
    content = re.sub(r'^_{3,}$', '---', content, flags=re.MULTILINE)
    return content

# ─── 2. Restore stripped wikilinks ───

# Map of bare names that should be [[name]] wikilinks
# These were stripped by mdformat because the target notes don't exist
STRIPPED_WIKILINKS = [
    "K_ATOMIC_MULTI_RSCF",
    "AMOS_FRACTAL_KNOWLEDGE_NETWORK",
    "AMOS_CORE_RUNTIME_LINEAGE",
    "PROOF_CAPSULE",
]

def restore_wikilinks(content):
    """Restore [[name]] syntax for known stripped wikilinks.
    
    Only restore when the bare name appears:
    - In regular text (not inside backticks or code blocks)
    - Not already wrapped in [[ ]]
    - Not part of a longer identifier
    """
    lines = content.split('\n')
    in_code_block = False
    result = []
    
    for line in lines:
        # Track code block state
        stripped = line.lstrip()
        if stripped.startswith('```'):
            in_code_block = not in_code_block
            result.append(line)
            continue
        
        if in_code_block:
            # Inside code blocks, restore wikilinks that were originally there
            # (some code blocks had [[...]] as display text)
            for name in STRIPPED_WIKILINKS:
                # Only restore if not already in [[ ]]
                # Pattern: standalone name not preceded by [[ and not followed by ]]
                line = re.sub(
                    r'(?<!\[\[)(' + re.escape(name) + r')(?!\]|\w)',
                    r'[[\1]]',
                    line
                )
            result.append(line)
            continue
        
        # Outside code blocks: restore wikilinks but not inside inline code
        # Split by backticks to identify inline code segments
        parts = re.split(r'(`[^`]+`)', line)
        for i, part in enumerate(parts):
            if part.startswith('`') and part.endswith('`'):
                # Inside inline code - restore wikilinks that were originally [[...]]
                for name in STRIPPED_WIKILINKS:
                    part = re.sub(
                        r'(?<!\[\[)(' + re.escape(name) + r')(?!\]|\w)',
                        r'[[\1]]',
                        part
                    )
                parts[i] = part
            else:
                # Regular text - restore wikilinks
                for name in STRIPPED_WIKILINKS:
                    # Don't restore if already inside [[ ]]
                    part = re.sub(
                        r'(?<!\[\[)(' + re.escape(name) + r')(?!\]|\w)',
                        r'[[\1]]',
                        part
                    )
                parts[i] = part
        
        result.append(''.join(parts))
    
    return '\n'.join(result)

# ─── 3. Restore LaTeX \( \) inline math delimiters ───

def restore_latex_inline(content):
    """Restore \( ... \) LaTeX inline math delimiters.
    
    mdformat stripped \( and \) leaving plain ( ).
    We need to identify which parentheses were LaTeX delimiters.
    
    Heuristic: parentheses containing:
    - Single capital letter: (C), (T), (R)
    - Capital letter with subscript: (R_A), (E_a), (Tx_k)
    - Capital letter with superscript: (p^*)
    - Function notation with capitals: (L(C)), (R_T)
    - Comma-separated math: (r_1,r_2)
    
    But NOT:
    - Regular prose parentheses
    - Parentheses in code blocks
    """
    
    # Pattern for LaTeX-like content inside parentheses
    # Matches: (X) where X is a math expression with capitals, underscores, carets
    # Must be careful not to match regular prose
    
    lines = content.split('\n')
    in_code_block = False
    result = []
    
    # Patterns that strongly indicate LaTeX math:
    # 1. Single capital letter: (C), (T), (R), (A), (I), (U), (F), (D), (S), (E)
    # 2. Capital with subscript: (R_A), (E_a), (Tx_k), (I_T), (R_T)
    # 3. Capital with superscript: (p^*), (p^\*)
    # 4. Function with capital: (L(C)), (D(C))
    # 5. Math comma list: (r_1,r_2)
    
    latex_patterns = [
        # Single capital letter in parentheses (not part of a word)
        r'(?<!\w)\(([A-Z])\)(?!\w)',
        # Capital letter with subscript: (X_y) or (Xy_z)
        r'(?<!\w)\(([A-Z][a-z]?_\w+)\)(?!\w)',
        # Capital letter with superscript: (X^...) 
        r'(?<!\w)\(([A-Z][a-z]?\^[\\]*\w+)\)(?!\w)',
        # Lowercase with subscript/superscript: (p^*), (p^\*), (r_1,r_2)
        r'(?<!\w)\(([a-z]_\w+(?:,\w+)*)\)(?!\w)',
        r'(?<!\w)\(([a-z]\^[\\]*\w+)\)(?!\w)',
        # Function notation: (L(C)), (D(C))
        r'(?<!\w)\(([A-Z]\([A-Z]\))\)(?!\w)',
        # Multiple capitals with subscripts: (r_1,r_2)
        r'(?<!\w)\(([a-z]_\d,[a-z]_\d)\)(?!\w)',
    ]
    
    for line in lines:
        stripped = line.lstrip()
        if stripped.startswith('```'):
            in_code_block = not in_code_block
            result.append(line)
            continue
        
        if in_code_block:
            result.append(line)
            continue
        
        # Skip lines that are inside $$ block math (those are fine)
        # Skip frontmatter
        if line.strip() == '---' and (len(result) == 0 or result[-1].strip() == ''):
            result.append(line)
            continue
        
        # Apply LaTeX restoration, but not inside inline code
        parts = re.split(r'(`[^`]+`)', line)
        for i, part in enumerate(parts):
            if part.startswith('`') and part.endswith('`'):
                continue  # Don't modify inline code
            # Also skip if it looks like a URL or file path
            if part.startswith('http') or part.startswith('/'):
                continue
            
            for pattern in latex_patterns:
                part = re.sub(pattern, r'\\(\1\\)', part)
            parts[i] = part
        
        result.append(''.join(parts))
    
    return '\n'.join(result)

# ─── 4. Fix escaped asterisks in former LaTeX ───

def fix_escaped_asterisks(content):
    """Fix p^\* → p^* (mdformat escaped * inside former LaTeX)"""
    # Only in specific context: after ^
    content = re.sub(r'\^\\\*', '^*', content)
    return content

# ─── Main ───

def process_file(filepath):
    """Process a single file with all fixes."""
    with open(filepath, 'r', encoding='utf-8') as f:
        original = f.read()
    
    content = original
    
    # Apply fixes
    content = fix_thematic_breaks(content)
    content = restore_wikilinks(content)
    content = restore_latex_inline(content)
    content = fix_escaped_asterisks(content)
    
    if content != original:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        return True
    return False

def find_files_with_issues(root_dirs):
    """Find all .md files that might have issues."""
    files = set()
    
    for root_dir in root_dirs:
        for dirpath, dirnames, filenames in os.walk(root_dir):
            # Skip hidden directories
            dirnames[:] = [d for d in dirnames if not d.startswith('.')]
            for fname in filenames:
                if fname.endswith('.md'):
                    files.add(os.path.join(dirpath, fname))
    
    return sorted(files)

if __name__ == '__main__':
    # Process all files in the affected directories
    root_dirs = [
        os.path.join(VAULT_ROOT, "01_CANON"),
        os.path.join(VAULT_ROOT, "25_COGNITIVE_MATRIX"),
    ]
    
    files = find_files_with_issues(root_dirs)
    print(f"Scanning {len(files)} files...")
    
    fixed_count = 0
    for f in files:
        try:
            if process_file(f):
                fixed_count += 1
                print(f"  FIXED: {f}")
        except Exception as e:
            print(f"  ERROR: {f}: {e}", file=sys.stderr)
    
    print(f"\nDone. Fixed {fixed_count}/{len(files)} files.")
