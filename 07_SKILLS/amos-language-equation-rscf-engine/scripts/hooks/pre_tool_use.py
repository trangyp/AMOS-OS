#!/usr/bin/env python3
"""
PreToolUse hook for amos-language-equation-rscf-engine.
Fires BEFORE skill execution. Exits non-zero to block.
Per Skills-vs-MCP-vs-Hooks (2026): deterministic gate the model cannot skip.
"""
import sys
import re
from pathlib import Path

SKILL_DIR = Path(__file__).parent.parent
SKILL_MD = SKILL_DIR / "SKILL.md"

def check_skill_exists():
    """Verify SKILL.md exists and is valid."""
    if not SKILL_MD.exists():
        print("BLOCK: SKILL.md not found")
        return False
    content = SKILL_MD.read_text(encoding='utf-8')
    if not content.startswith("---\n"):
        print("BLOCK: SKILL.md missing frontmatter")
        return False
    return True

def check_description_present():
    """Verify description field exists (required for discovery)."""
    content = SKILL_MD.read_text(encoding='utf-8')
    if not re.search(r'^description:', content, re.MULTILINE):
        print("BLOCK: Missing description field")
        return False
    return True

def check_no_oversized_body():
    """Warn if SKILL.md body exceeds 500 lines (progressive disclosure)."""
    lines = content.split('\n')
    fm_end = 0
    for i, line in enumerate(lines):
        if i > 0 and line.strip() == '---':
            fm_end = i
            break
    body_lines = len(lines) - fm_end - 1
    if body_lines > 500:
        print("WARN: SKILL.md body exceeds 500 lines")
    return True  # Warn only, don't block

def main():
    if not check_skill_exists():
        return 1
    if not check_description_present():
        return 1
    return 0

if __name__ == "__main__":
    sys.exit(main())
