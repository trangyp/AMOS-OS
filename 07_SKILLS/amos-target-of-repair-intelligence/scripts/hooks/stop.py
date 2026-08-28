#!/usr/bin/env python3
"""
Stop hook for amos-target-of-repair-intelligence.
Fires at turn end. Gates completion until validation passes.
Per Claude Code best practices (2026): run tests before allowing turn to end.
"""
import sys
from pathlib import Path

SKILL_DIR = Path(__file__).parent.parent

def main():
    # Run the skill's validation script
    validate = SKILL_DIR / "scripts" / "validate.py"
    if validate.exists():
        import subprocess
        result = subprocess.run([sys.executable, str(validate)], capture_output=True, text=True)
        if result.returncode != 0:
            print("BLOCK: Skill validation failed")
            print(result.stdout)
            return 1
    return 0

if __name__ == "__main__":
    sys.exit(main())
