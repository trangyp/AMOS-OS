#!/usr/bin/env python3
"""
PreToolUse hook for amos-llm-wiki.
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

def main():
    if not check_skill_exists():
        return 1
    if not check_description_present():
        return 1
    return 0

if __name__ == "__main__":
    sys.exit(main())
