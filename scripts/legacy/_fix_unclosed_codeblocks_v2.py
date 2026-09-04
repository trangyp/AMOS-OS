#!/usr/bin/env python3
"""Find and fix unclosed code blocks in vault markdown files.

Properly tracks ``` fence state (open/close) and identifies files where
the last fence is unclosed. Auto-appends a closing ``` to fix.
"""
import os
import re
from pathlib import Path

VAULT = Path(__file__).resolve().parents[2]

FENCE_RE = re.compile(r'^(\s*)(```+)(.*)$')

unclosed = []
fixed = 0
scanned = 0

for root, dirs, files in os.walk(VAULT, followlinks=True):
    parts = Path(root).relative_to(VAULT).parts
    if any(p in (".git", "node_modules", ".obsidian") for p in parts):
        continue
    for fn in files:
        if not fn.endswith(".md"):
            continue
        p = Path(root) / fn
        try:
            rel = str(p.relative_to(VAULT))
        except ValueError:
            continue
        scanned += 1

        try:
            text = p.read_text(encoding="utf-8", errors="strict")
        except Exception:
            continue

        lines = text.splitlines()
        in_code = False
        fence_marker = None
        last_fence_line = -1

        for i, line in enumerate(lines):
            m = FENCE_RE.match(line)
            if m:
                marker = m.group(2)
                if in_code:
                    # Closing fence — should match opening marker length (>=3)
                    in_code = False
                    fence_marker = None
                else:
                    # Opening fence
                    in_code = True
                    fence_marker = marker
                    last_fence_line = i

        if in_code:
            # Unclosed code block
            unclosed.append((rel, last_fence_line + 1, len(lines)))

            # Auto-fix: append closing ```
            if not text.endswith("\n"):
                text += "\n"
            text += "```\n"

            try:
                p.write_text(text, encoding="utf-8")
                fixed += 1
            except Exception as e:
                print(f"  ERROR writing {rel}: {e}")

print(f"Scanned {scanned} .md files")
print(f"Found {len(unclosed)} files with unclosed code blocks")
print(f"Auto-fixed {fixed} files\n")

if unclosed:
    print("Fixed files (rel_path — unclosed_fence_line / total_lines):")
    for rel, fence_line, total in unclosed[:50]:
        print(f"  {rel} — fence at line {fence_line} / {total} total")
    if len(unclosed) > 50:
        print(f"  ... and {len(unclosed) - 50} more")
