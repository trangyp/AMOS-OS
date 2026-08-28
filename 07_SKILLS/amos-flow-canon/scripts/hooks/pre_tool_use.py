#!/usr/bin/env python3
"""PreToolUse hook for amos-flow-canon."""
import sys, re
from pathlib import Path

SKILL_DIR = Path(__file__).parent.parent
SKILL_MD = SKILL_DIR / "SKILL.md"

def main():
    if not SKILL_MD.exists():
        print("BLOCK: SKILL.md not found")
        return 1
    content = SKILL_MD.read_text(encoding='utf-8')
    if not content.startswith("---\n"):
        print("BLOCK: SKILL.md missing frontmatter")
        return 1
    if not re.search(r'^description:', content, re.MULTILINE):
        print("BLOCK: Missing description field")
        return 1
    return 0

if __name__ == "__main__":
    sys.exit(main())
