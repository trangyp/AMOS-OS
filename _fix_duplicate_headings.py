#!/usr/bin/env python3
"""Fix duplicate H1/H2 headings by appending unique suffixes to 2nd+ occurrences."""
import os
import re
from pathlib import Path
from collections import defaultdict

VAULT = Path("/Users/mac/Documents/AMOS_OS")
EXCLUDE_DIRS = {".git", "node_modules", ".obsidian", ".trash", "__pycache__"}


def is_decorative(heading):
    if re.match(r'^[=\-*#]+\s*$', heading):
        return True
    if re.match(r'^[-*]+\s+coding[:\s]', heading, re.I):
        return True
    if heading.startswith('configure ') or heading.startswith('import ') or heading.startswith('from '):
        return True
    return False


def fix_file(path, rel):
    """Fix duplicate headings in a single file. Returns count of fixes."""
    try:
        text = path.read_text(encoding="utf-8")
    except Exception:
        return 0

    lines = text.split("\n")
    # First pass: identify which lines are headings and track duplicates
    heading_lines = {}  # (level, heading_lower) -> list of line indices
    in_code = False
    for i, line in enumerate(lines):
        if line.strip().startswith("```"):
            in_code = not in_code
            continue
        if in_code:
            continue
        m = re.match(r'^(#{1,2})\s+(.+)$', line)
        if m:
            level = len(m.group(1))
            heading = m.group(2).strip()
            heading_lower = heading.lower()
            if is_decorative(heading_lower):
                continue
            key = (level, heading_lower)
            if key not in heading_lines:
                heading_lines[key] = []
            heading_lines[key].append((i, level, heading))

    # Find which need fixing
    fixes = {}  # line_index -> new_heading_text
    for key, occurrences in heading_lines.items():
        if len(occurrences) > 1:
            level = key[0]
            for idx, (line_i, _, original_heading) in enumerate(occurrences[1:], start=2):
                # Append suffix to make unique
                suffix = f" — part {idx}"
                new_heading = f"{'#'*level} {original_heading}{suffix}"
                fixes[line_i] = new_heading

    if not fixes:
        return 0

    # Apply fixes
    for line_i, new_text in fixes.items():
        lines[line_i] = new_text

    new_text = "\n".join(lines)
    path.write_text(new_text, encoding="utf-8")
    return len(fixes)


# Collect files with duplicates
files_with_dups = set()
for root, dirs, files in os.walk(VAULT, followlinks=True):
    dirs[:] = [d for d in dirs if d not in EXCLUDE_DIRS]
    for fn in files:
        if not fn.endswith(".md"):
            continue
        p = Path(root) / fn
        try:
            rel = p.relative_to(VAULT)
        except ValueError:
            continue
        parts = str(rel).replace("\\", "/").split("/")
        if any(x in EXCLUDE_DIRS for x in parts):
            continue
        if parts and parts[0] in (".devin", ".agents", ".claude"):
            continue
        if len(parts) == 1 and parts[0].startswith("_"):
            continue
        try:
            text = p.read_text(encoding="utf-8")
        except Exception:
            continue
        headings = {}
        in_code = False
        for line in text.split("\n"):
            if line.strip().startswith("```"):
                in_code = not in_code
                continue
            if in_code:
                continue
            m = re.match(r'^(#{1,2})\s+(.+)$', line)
            if m:
                level = len(m.group(1))
                heading = m.group(2).strip().lower()
                if is_decorative(heading):
                    continue
                key = (level, heading)
                headings[key] = headings.get(key, 0) + 1
        for (level, heading), count in headings.items():
            if count > 1:
                files_with_dups.add(str(rel))
                break

print(f"Files to fix: {len(files_with_dups)}")

total_fixes = 0
for rel_str in sorted(files_with_dups):
    p = VAULT / rel_str
    n = fix_file(p, rel_str)
    if n > 0:
        print(f"  Fixed {n:3d} in {rel_str}")
        total_fixes += n

print(f"\nTotal fixes: {total_fixes}")
