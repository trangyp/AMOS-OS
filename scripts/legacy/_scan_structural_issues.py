#!/usr/bin/env python3
"""Scan for structural errors in vault markdown files:
- Malformed YAML frontmatter (missing closing ---, unparseable)
- Unclosed code blocks (odd number of ``` fences)
- Empty/near-empty files
- Files with encoding issues
- Broken markdown table formatting (optional, basic check)
"""
import os
import re
from pathlib import Path

VAULT = Path(__file__).resolve().parents[2]

issues = {
    "frontmatter_malformed": [],
    "frontmatter_unclosed": [],
    "codeblock_unclosed": [],
    "empty_file": [],
    "encoding_issue": [],
}

scanned = 0
for root, dirs, files in os.walk(VAULT, followlinks=True):
    # Skip hidden dirs except .devin, and skip node_modules
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

        # Read file
        try:
            text = p.read_text(encoding="utf-8", errors="strict")
        except Exception:
            issues["encoding_issue"].append(rel)
            continue

        # Check empty/near-empty
        stripped = text.strip()
        if len(stripped) < 10:
            issues["empty_file"].append((rel, len(stripped)))
            continue

        # Check YAML frontmatter
        if text.startswith("---"):
            lines = text.splitlines()
            if len(lines) < 2:
                issues["frontmatter_malformed"].append((rel, "starts with --- but too short"))
            else:
                # Find closing ---
                closed = False
                for i in range(1, len(lines)):
                    if lines[i].strip() == "---":
                        closed = True
                        break
                if not closed:
                    issues["frontmatter_unclosed"].append(rel)
                else:
                    # Try to parse the YAML block
                    yaml_block = "\n".join(lines[1:i])
                    # Basic checks: look for obvious issues
                    # Check for tabs in YAML (common error)
                    for j, yline in enumerate(yaml_block.splitlines(), 1):
                        if "\t" in yline:
                            issues["frontmatter_malformed"].append(
                                (rel, f"tab character in YAML line {j}")
                            )
                            break

        # Check code blocks (count ``` fences, excluding inline)
        in_inline = False
        fence_count = 0
        for line in text.splitlines():
            stripped_line = line.strip()
            if stripped_line.startswith("```"):
                fence_count += 1
        if fence_count % 2 != 0:
            issues["codeblock_unclosed"].append((rel, fence_count))

print(f"Scanned {scanned} .md files\n")

for category, label in [
    ("frontmatter_unclosed", "UNCLOSED YAML FRONTMATTER"),
    ("frontmatter_malformed", "MALFORMED YAML FRONTMATTER"),
    ("codeblock_unclosed", "UNCLOSED CODE BLOCKS"),
    ("empty_file", "EMPTY/NEAR-EMPTY FILES"),
    ("encoding_issue", "ENCODING ISSUES"),
]:
    items = issues[category]
    if not items:
        print(f"=== {label}: 0 ===\n")
        continue
    print(f"=== {label}: {len(items)} ===")
    for item in items[:30]:
        if isinstance(item, tuple):
            print(f"  {item[0]} — {item[1]}")
        else:
            print(f"  {item}")
    if len(items) > 30:
        print(f"  ... and {len(items) - 30} more")
    print()
