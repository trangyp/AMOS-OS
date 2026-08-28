#!/usr/bin/env python3
"""Stop hook for amos-7-part-universe-canon."""
import sys
from pathlib import Path

SKILL_DIR = Path(__file__).parent.parent

def main():
    validate = SKILL_DIR / "scripts" / "validate.py"
    if validate.exists():
        import subprocess
        result = subprocess.run([sys.executable, str(validate)], capture_output=True, text=True)
        if result.returncode != 0:
            print("BLOCK: Skill validation failed")
            return 1
    return 0

if __name__ == "__main__":
    sys.exit(main())
