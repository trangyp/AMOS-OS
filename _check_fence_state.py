#!/usr/bin/env python3
"""Properly track code fence state to find real unclosed code blocks.

Handles:
- Triple backtick fences (```...```)
- Tilde fences (~~~...~~~)
- Indented fences (4+ spaces or tab + ```/~~~)
- 4+ backtick fences (counted as open/close pairs)
- Fences with language tags
- Fences inside other fenced blocks (nested not supported by CommonMark,
  but we track the opening fence and match its closing fence)
"""
import sys
import re
from pathlib import Path

FENCE_RE = re.compile(r'^(\s*)(`{3,}|~{3,})\s*(.*?)\s*$')

def check_file(filepath):
    """Return (line_number_of_open_fence, None) if unclosed, else (None, None)."""
    try:
        lines = filepath.read_text(encoding='utf-8', errors='replace').splitlines()
    except Exception:
        return None, None

    in_fence = False
    fence_char = None
    fence_len = 0
    fence_indent = 0
    open_line = None

    for i, line in enumerate(lines, 1):
        if in_fence:
            # Check if this line closes the fence
            m = FENCE_RE.match(line)
            if m:
                indent, chars, info = m.group(1), m.group(2), m.group(3)
                # Closing fence must match char, be at least as long, and have empty info
                if chars[0] == fence_char and len(chars) >= fence_len and not info.strip():
                    # Also check indent is not more than 3 spaces more than opening (CommonMark)
                    if len(indent) <= fence_indent + 3:
                        in_fence = False
                        fence_char = None
                        fence_len = 0
                        open_line = None
            continue

        # Not in fence: check for opening fence
        m = FENCE_RE.match(line)
        if m:
            indent, chars, info = m.group(1), m.group(2), m.group(3)
            # Only backticks and tildes of length >= 3 start a fence
            # Indent must be 0-3 spaces (CommonMark)
            if len(indent.expandtabs(4)) <= 3:
                in_fence = True
                fence_char = chars[0]
                fence_len = len(chars)
                fence_indent = len(indent.expandtabs(4))
                open_line = i

    if in_fence:
        return open_line, None
    return None, None


def main():
    root = Path(sys.argv[1] if len(sys.argv) > 1 else '.')
    files = list(root.rglob('*.md'))
    # Exclude .git
    files = [f for f in files if '.git' not in f.parts]

    issues = []
    for f in files:
        open_line, _ = check_file(f)
        if open_line is not None:
            issues.append((str(f), open_line))

    print(f"Scanned {len(files)} .md files")
    print(f"\n=== REAL UNCLOSED CODE BLOCKS: {len(issues)} ===")
    for path, line in sorted(issues):
        print(f"  {path} — opens at line {line}, never closes")

    # Also accept specific files as args to check just those
    if len(sys.argv) > 2:
        print("\n=== SPECIFIC FILE CHECK ===")
        for arg in sys.argv[2:]:
            f = Path(arg)
            if f.exists():
                open_line, _ = check_file(f)
                status = f"UNCLOSED (opens at {open_line})" if open_line else "OK"
                print(f"  {arg}: {status}")


if __name__ == '__main__':
    main()
