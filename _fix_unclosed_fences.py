#!/usr/bin/env python3
"""Fix unclosed code blocks by removing stray fences or adding missing closing fences.

Strategy:
1. For each file with an unclosed fence, find the opening fence line.
2. If the opening fence is at/near the end of file (last 10 lines) and the content
   after it doesn't look like code, remove the stray fence.
3. If the opening fence wraps content that looks like code (indented, contains code-like
   patterns), add a closing fence at the end.
4. Verify each fix by re-running the fence state checker.
"""
import sys
import re
from pathlib import Path

sys.path.insert(0, '.')
from _check_fence_state import check_file, FENCE_RE


def is_stray_trailing_fence(lines, open_line_idx):
    """Check if the fence at open_line_idx (0-based) is a stray trailing fence.

    A stray trailing fence is one where:
    - It's near the end of the file (within last 10 lines)
    - The content after it (if any) is short and doesn't look like code
    """
    total = len(lines)
    # If the fence is in the last 10 lines
    if open_line_idx >= total - 10:
        # Check content after the fence
        after = lines[open_line_idx + 1:]
        # If there's no content or just whitespace/short footer, it's stray
        non_empty_after = [l for l in after if l.strip()]
        if len(non_empty_after) <= 3:
            return True
    return False


def is_mid_file_stray_fence(lines, open_line_idx):
    """Check if a fence in the middle of the file is stray.

    A mid-file stray fence is one where the content after it (until EOF) is clearly
    prose (Markdown headings, bullet points, wikilinks, etc.) and not code.
    """
    after = lines[open_line_idx + 1:]
    if not after:
        return True

    # Check if content after looks like prose
    prose_indicators = 0
    code_indicators = 0
    for line in after:
        stripped = line.strip()
        if not stripped:
            continue
        # Prose indicators
        if stripped.startswith('#') or stripped.startswith('- ') or stripped.startswith('* '):
            prose_indicators += 1
        elif stripped.startswith('**') or stripped.startswith('> '):
            prose_indicators += 1
        elif '[[' in stripped or '---' == stripped:
            prose_indicators += 1
        elif stripped.startswith('|') or stripped.startswith('!['):
            prose_indicators += 1
        # Code indicators
        elif re.match(r'^[a-z_]+\(', stripped) or stripped.endswith(';') or stripped.endswith('{') or stripped.endswith('}'):
            code_indicators += 1
        elif re.match(r'^\s{4,}\S', line) and not stripped.startswith('-'):
            code_indicators += 1

    return prose_indicators > code_indicators


def fix_file(filepath, dry_run=False):
    """Fix a single file. Returns (action, description) where action is 'removed', 'added_close', or 'skipped'."""
    lines = filepath.read_text(encoding='utf-8', errors='replace').splitlines()
    open_line, _ = check_file(filepath)
    if open_line is None:
        return 'skipped', 'already balanced'

    open_idx = open_line - 1  # Convert to 0-based

    # Check if it's a stray trailing fence
    if is_stray_trailing_fence(lines, open_idx):
        if dry_run:
            return 'would_remove', f'stray trailing fence at line {open_line}'
        # Remove the stray fence line
        new_lines = lines[:open_idx] + lines[open_idx + 1:]
        filepath.write_text('\n'.join(new_lines) + '\n', encoding='utf-8')
        # Verify
        ol2, _ = check_file(filepath)
        if ol2 is None:
            return 'removed', f'stray fence at line {open_line}'
        else:
            return 'partial', f'removed line {open_line} but still unclosed at {ol2}'

    # Check if it's a mid-file stray fence
    if is_mid_file_stray_fence(lines, open_idx):
        if dry_run:
            return 'would_remove', f'mid-file stray fence at line {open_line}'
        # Remove the stray fence line
        new_lines = lines[:open_idx] + lines[open_idx + 1:]
        filepath.write_text('\n'.join(new_lines) + '\n', encoding='utf-8')
        # Verify
        ol2, _ = check_file(filepath)
        if ol2 is None:
            return 'removed', f'mid-file stray fence at line {open_line}'
        else:
            return 'partial', f'removed line {open_line} but still unclosed at {ol2}'

    # Otherwise, add a closing fence at the end
    if dry_run:
        return 'would_add_close', f'add closing fence after line {open_line}'
    new_lines = lines + ['```']
    filepath.write_text('\n'.join(new_lines) + '\n', encoding='utf-8')
    ol2, _ = check_file(filepath)
    if ol2 is None:
        return 'added_close', f'added closing fence at end (opened at line {open_line})'
    else:
        return 'partial', f'added closing fence but still unclosed at {ol2}'


def main():
    dry_run = '--dry-run' in sys.argv
    root = Path('.')
    files = [f for f in root.rglob('*.md') if '.git' not in f.parts]

    # Find all files with unclosed fences
    issue_files = []
    for f in files:
        ol, _ = check_file(f)
        if ol is not None:
            issue_files.append(f)

    print(f"Found {len(issue_files)} files with unclosed code blocks")
    if dry_run:
        print("(DRY RUN — no changes will be made)")
    print()

    removed = 0
    added_close = 0
    partial = 0
    skipped = 0

    for f in sorted(issue_files):
        action, desc = fix_file(f, dry_run=dry_run)
        if action in ('removed', 'would_remove'):
            removed += 1
        elif action in ('added_close', 'would_add_close'):
            added_close += 1
        elif action == 'partial':
            partial += 1
        elif action == 'skipped':
            skipped += 1
        print(f"  [{action:14s}] {f} — {desc}")

    print(f"\nSummary: {removed} fences removed, {added_close} closing fences added, {partial} partial, {skipped} skipped")


if __name__ == '__main__':
    main()
