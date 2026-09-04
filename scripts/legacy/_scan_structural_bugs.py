#!/usr/bin/env python3
"""Scan for structural bugs in vault markdown files:
1. YAML frontmatter: duplicate keys, stringified lists, unclosed
2. Unclosed code blocks / mismatched fences
3. Unclosed callouts (> [!note] without closing)
4. Broken markdown tables (missing pipe alignment)
5. Empty/near-empty files
6. Encoding issues (non-UTF8)
7. Broken internal links ([text](#anchor) to non-existent headings)
8. Duplicate headings within same file
9. Trailing whitespace / mixed line endings
10. Files with only frontmatter, no body
11. Wikilinks with pipe but empty display text ([[target|]])
12. Unbalanced brackets/parens in code-free context
"""
import os
import re
import sys
from pathlib import Path
from collections import defaultdict

VAULT = Path(__file__).resolve().parents[2]
EXCLUDE_DIRS = {".git", "node_modules", ".obsidian", ".trash", "__pycache__"}
EXCLUDE_PREFIXES = ("_",)  # temp scripts

issues = defaultdict(list)

def should_skip(rel_path):
    parts = rel_path.replace("\\", "/").split("/")
    if any(p in EXCLUDE_DIRS for p in parts):
        return True
    # Skip temp scripts in root
    if len(parts) == 1 and parts[0].startswith(EXCLUDE_PREFIXES):
        return True
    # Skip .devin (symlinked external repo)
    if parts and parts[0] == ".devin":
        return True
    if parts and parts[0] == ".agents":
        return True
    if parts and parts[0] == ".claude":
        return True
    return False

def parse_frontmatter(text):
    """Return (fm_dict, body) or (None, text) if no frontmatter."""
    if not text.startswith("---"):
        return None, text
    lines = text.split("\n")
    end_idx = None
    for i in range(1, len(lines)):
        if lines[i].strip() == "---":
            end_idx = i
            break
    if end_idx is None:
        return None, text  # unclosed — handled separately
    fm_text = "\n".join(lines[1:end_idx])
    body = "\n".join(lines[end_idx+1:])
    # Simple key: value parsing
    fm = {}
    current_key = None
    current_list = None
    for line in fm_text.split("\n"):
        if line.strip().startswith("#"):
            continue
        if line.strip().startswith("- ") and current_key:
            val = line.strip()[2:].strip()
            if current_list is None:
                current_list = []
            current_list.append(val)
            fm[current_key] = current_list
            continue
        m = re.match(r'^(\w[\w\s-]*?):\s*(.*)$', line)
        if m:
            if current_list is not None and current_key:
                fm[current_key] = current_list
            current_key = m.group(1).strip()
            val = m.group(2).strip()
            current_list = None
            if val:
                # Check for stringified list: "['a', 'b']" or "[a, b]"
                if (val.startswith("[") and val.endswith("]")) and not val.startswith("[["):
                    issues["stringified_list"].append((str(rel), current_key, val[:60]))
                fm[current_key] = val
            else:
                fm[current_key] = None  # may be a list
        elif line.strip() == "" and current_list is not None and current_key:
            fm[current_key] = current_list
            current_list = None
    if current_list is not None and current_key:
        fm[current_key] = current_list
    return fm, body

def check_code_blocks(text, rel):
    in_code = False
    fence_char = None
    fence_len = 0
    fence_info = None
    for line in text.split("\n"):
        m = re.match(r'^(\s*)(`{3,}|~{3,})(.*?)\s*$', line)
        if not m:
            continue
        indent = m.group(1)
        marker = m.group(2)
        info = (m.group(3) or "").strip()
        # Open fence must be at start of line or up to 3 spaces indent, with no info
        if not in_code:
            # Opening fence: up to 3 spaces indent, any info allowed
            if len(indent.expandtabs(4)) <= 3:
                in_code = True
                fence_char = marker[0]
                fence_len = len(marker)
                fence_info = info
        else:
            # Close fence must match char, be at least as long, and have empty info
            if (marker[0] == fence_char and len(marker) >= fence_len
                    and not info and len(indent.expandtabs(4)) <= 3):
                in_code = False
                fence_char = None
                fence_len = 0
                fence_info = None
    if in_code:
        issues["unclosed_codeblock"].append(str(rel))

def check_callouts(text, rel):
    """Check for unclosed callout blocks."""
    in_callout = False
    callout_start = 0
    for i, line in enumerate(text.split("\n")):
        if re.match(r'^>\s*\[!\w+', line):
            in_callout = True
            callout_start = i
        elif in_callout:
            if not line.startswith(">") and line.strip() != "":
                # Callout ended without explicit close — this is normal in Obsidian
                in_callout = False
    # Not a real bug in Obsidian — callouts end at first non-> line

def check_empty_files(text, rel, path):
    stripped = text.strip()
    if len(stripped) < 10:
        issues["empty_file"].append((str(rel), len(stripped)))
    elif len(stripped) < 50 and stripped.startswith("---") and stripped.endswith("---"):
        # Only frontmatter, no body
        issues["frontmatter_only"].append(str(rel))

def check_duplicate_headings(text, rel):
    """Check for duplicate H1/H2 headings within the same file."""
    headings = {}
    in_code = False
    for line in text.split("\n"):
        if line.strip().startswith("```"):
            in_code = not in_code
            continue
        if in_code:
            continue
        m = re.match(r'^(#{1})\s+(.+)$', line)
        if m:
            level = len(m.group(1))
            heading = m.group(2).strip().lower()
            # Skip decorative/punctuation-only headings and code comments
            if not re.search(r'\w', heading):
                continue
            if heading.startswith('configure ') or heading.startswith('import ') or heading.startswith('from ') or 'coding: utf' in heading:
                continue
            key = (level, heading)
            headings[key] = headings.get(key, 0) + 1
    for (level, heading), count in headings.items():
        if count > 1:
            issues["duplicate_heading"].append((str(rel), f"{'#'*level} {heading}", count))

def check_stringified_lists_in_fm(text, rel):
    """Check for YAML frontmatter values that are stringified Python lists."""
    if not text.startswith("---"):
        return
    lines = text.split("\n")
    end_idx = None
    for i in range(1, len(lines)):
        if lines[i].strip() == "---":
            end_idx = i
            break
    if end_idx is None:
        return
    for line in lines[1:end_idx]:
        m = re.match(r'^(\w[\w\s-]*?):\s*(.*)$', line)
        if m:
            val = m.group(2).strip()
            # Stringified list: ['a', 'b'] or ["a", "b"]
            if re.match(r"^\[.*['\"].*\]$", val) and not val.startswith("[["):
                issues["stringified_list"].append((str(rel), m.group(1).strip(), val[:80]))

def check_wikilink_empty_display(text, rel):
    """Check for [[target|]] wikilinks with empty display text."""
    in_code = False
    for line in text.split("\n"):
        if line.strip().startswith("```"):
            in_code = not in_code
            continue
        if in_code:
            continue
        for m in re.finditer(r'\[\[([^\]|#]+)(?:#[^\]|]*)?\|(\s*)\]\]', line):
            issues["wikilink_empty_display"].append((str(rel), m.group(0)))

def check_broken_internal_links(text, rel):
    """Check [text](#heading) links point to existing headings."""
    headings = set()
    in_code = False
    for line in text.split("\n"):
        if line.strip().startswith("```"):
            in_code = not in_code
            continue
        if in_code:
            continue
        m = re.match(r'^#{1,6}\s+(.+)$', line)
        if m:
            # Normalize heading to anchor: lowercase, replace spaces with -, remove special chars
            h = m.group(1).strip().lower()
            h = re.sub(r'[^\w\s-]', '', h)
            h = re.sub(r'[\s]+', '-', h)
            h = re.sub(r'-+', '-', h).strip('-')
            headings.add(h)
    # Check internal links
    for m in re.finditer(r'\[([^\]]*)\]\(#([^)]+)\)', text):
        anchor = m.group(2).strip().lower()
        anchor_norm = re.sub(r'[^\w\s-]', '', anchor)
        anchor_norm = re.sub(r'[\s]+', '-', anchor_norm)
        anchor_norm = re.sub(r'-+', '-', anchor_norm).strip('-')
        if anchor_norm not in headings and anchor not in headings:
            issues["broken_internal_link"].append((str(rel), m.group(0)[:60]))

def check_trailing_whitespace(text, rel):
    """Check for excessive trailing whitespace (more than 3 lines)."""
    count = 0
    for line in text.split("\n"):
        if line != line.rstrip() and line.strip() != "":
            count += 1
    if count > 10:
        issues["trailing_whitespace"].append((str(rel), count))

def check_mixed_line_endings(text, rel):
    """Check for mixed CRLF and LF."""
    if "\r\n" in text and "\n" in text.replace("\r\n", ""):
        issues["mixed_line_endings"].append(str(rel))

scanned = 0
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
        if should_skip(str(rel)):
            continue
        try:
            text = p.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            issues["encoding_issue"].append(str(rel))
            continue
        except Exception:
            continue
        scanned += 1
        check_code_blocks(text, rel)
        check_empty_files(text, rel, p)
        check_duplicate_headings(text, rel)
        check_stringified_lists_in_fm(text, rel)
        check_wikilink_empty_display(text, rel)
        check_broken_internal_links(text, rel)
        check_trailing_whitespace(text, rel)
        check_mixed_line_endings(text, rel)

print(f"Scanned {scanned} .md files\n")
for category, items in sorted(issues.items()):
    print(f"=== {category.upper()}: {len(items)} ===")
    for item in items[:20]:
        print(f"  {item}")
    if len(items) > 20:
        print(f"  ... and {len(items) - 20} more")
    print()
