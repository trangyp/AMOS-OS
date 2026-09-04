#!/usr/bin/env python3
"""
_vault_mdformat_fix.py — Apply mdformat-obsidian formatting fixes across the vault.

Fixes applied (matching the manual edits the user started):
1. Unquote YAML title values: title: "Foo" → title: Foo
2. Remove trailing empty code blocks: ```\n```\n at end of file
3. Remove blank lines between tags list and rscf: key in frontmatter
4. Unquote schema_version: "1.0" → 1.0
5. Remove trailing whitespace on all lines
6. Ensure single trailing newline

Usage:
  python3 _vault_mdformat_fix.py [--dry-run] [--vault-dir DIR]
"""

import argparse
import re
import sys
from pathlib import Path
from collections import defaultdict


def unquote_yaml_titles(content: str) -> tuple[str, int]:
    """Unquote YAML title values: title: "Foo" → title: Foo"""
    count = 0
    def replacer(m):
        nonlocal count
        count += 1
        return f"title: {m.group(1)}"
    # Match title: "..." or title: '...' (only in frontmatter)
    new_content = re.sub(r'^title:\s*"([^"]+)"\s*$', replacer, content, flags=re.MULTILINE)
    new_content = re.sub(r"^title:\s*'([^']+)'\s*$", replacer, new_content, flags=re.MULTILINE)
    return new_content, count


def remove_trailing_empty_codeblocks(content: str) -> tuple[str, int]:
    """Remove trailing empty code blocks: ```\n```\n at end of file"""
    count = 0
    # Match trailing ``` followed by optional whitespace/newline then ``` 
    pattern = r'\n```\s*\n```\s*$'
    while re.search(pattern, content):
        content = re.sub(pattern, '\n', content)
        count += 1
    # Also match standalone trailing ```
    pattern2 = r'\n```\s*\n```\s*\n*$'
    if re.search(pattern2, content):
        content = re.sub(pattern2, '\n', content)
        count += 1
    return content, count


def fix_blank_line_before_rscf(content: str) -> tuple[str, int]:
    """Remove blank lines between tags list and rscf: key in frontmatter"""
    count = 0
    # Match: last tag line\n\nrscf: → last tag line\nrscf:
    pattern = r'(\n  - [^\n]+\n)\n+(rscf:)'
    def replacer(m):
        nonlocal count
        count += 1
        return f"{m.group(1)}{m.group(2)}"
    new_content = re.sub(pattern, replacer, content)
    return new_content, count


def unquote_schema_version(content: str) -> tuple[str, int]:
    """Unquote schema_version: "1.0" → 1.0"""
    count = 0
    def replacer(m):
        nonlocal count
        count += 1
        return f"schema_version: {m.group(1)}"
    new_content = re.sub(r'^schema_version:\s*"([^"]+)"\s*$', replacer, content, flags=re.MULTILINE)
    new_content = re.sub(r"^schema_version:\s*'([^']+)'\s*$", replacer, new_content, flags=re.MULTILINE)
    return new_content, count


def remove_trailing_whitespace(content: str) -> tuple[str, int]:
    """Remove trailing whitespace on all lines"""
    count = 0
    lines = content.split('\n')
    new_lines = []
    for line in lines:
        stripped = line.rstrip()
        if stripped != line:
            count += 1
        new_lines.append(stripped)
    return '\n'.join(new_lines), count


def ensure_single_trailing_newline(content: str) -> tuple[str, int]:
    """Ensure exactly one trailing newline"""
    count = 0
    stripped = content.rstrip('\n')
    if stripped != content:
        count = 1
    return stripped + '\n', count


def fix_file(filepath: Path, dry_run: bool = False) -> dict:
    """Apply all fixes to a single file."""
    try:
        content = filepath.read_text(encoding="utf-8")
    except Exception as e:
        return {"file": str(filepath), "error": str(e)}

    original = content
    fixes = {}

    # Apply fixes in order
    content, n = unquote_yaml_titles(content)
    if n: fixes["unquote_titles"] = n

    content, n = remove_trailing_empty_codeblocks(content)
    if n: fixes["remove_trailing_codeblocks"] = n

    content, n = fix_blank_line_before_rscf(content)
    if n: fixes["fix_blank_before_rscf"] = n

    content, n = unquote_schema_version(content)
    if n: fixes["unquote_schema_version"] = n

    content, n = remove_trailing_whitespace(content)
    if n: fixes["remove_trailing_whitespace"] = n

    content, n = ensure_single_trailing_newline(content)
    if n: fixes["fix_trailing_newline"] = n

    if content != original and not dry_run:
        filepath.write_text(content, encoding="utf-8")

    return {"file": str(filepath), "fixes": fixes, "changed": content != original}


def main():
    parser = argparse.ArgumentParser(description="Apply mdformat-obsidian fixes to vault files")
    parser.add_argument("--dry-run", action="store_true", help="Don't write changes, just report")
    parser.add_argument("--vault-dir", default=str(__import__("pathlib").Path(__file__).resolve().parents[2]), help="Vault directory")
    parser.add_argument("--pattern", default="**/*.md", help="Glob pattern for files")
    args = parser.parse_args()

    vault = Path(args.vault_dir)
    total_files = 0
    changed_files = 0
    fix_counts = defaultdict(int)

    # Process all .md files
    for filepath in sorted(vault.glob(args.pattern)):
        # Skip .obsidian/, .git/, node_modules/
        rel = str(filepath.relative_to(vault))
        if any(part in rel for part in ['.obsidian/', '.git/', 'node_modules/', '.trash/']):
            continue

        total_files += 1
        result = fix_file(filepath, dry_run=args.dry_run)

        if result.get("error"):
            continue

        if result["changed"]:
            changed_files += 1
            for fix_name, count in result["fixes"].items():
                fix_counts[fix_name] += count
            if not args.dry_run:
                print(f"  FIXED: {rel} — {result['fixes']}")

    print()
    print(f"Total files scanned: {total_files}")
    print(f"Files changed:       {changed_files}")
    print(f"Fixes applied:")
    for fix_name, count in sorted(fix_counts.items()):
        print(f"  {fix_name}: {count}")

    if args.dry_run:
        print("\n(dry run — no files written)")


if __name__ == "__main__":
    main()
