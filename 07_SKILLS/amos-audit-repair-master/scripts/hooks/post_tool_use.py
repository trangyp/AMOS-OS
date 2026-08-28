#!/usr/bin/env python3
"""
PostToolUse hook for amos-audit-repair-master.
Fires AFTER skill execution succeeds. Validates output quality.
Per Skills-vs-MCP-vs-Hooks (2026): deterministic post-execution gate.
"""
import sys
import re
from pathlib import Path

SKILL_DIR = Path(__file__).parent.parent

def check_epistemic_labels(output):
    """Verify output contains epistemic state labels."""
    epistemic_states = ["SOURCE_CLAIM", "DERIVED", "AMOS_MODEL", "OBSERVATION", "CONDITIONAL"]
    has_any = any(state in output for state in epistemic_states)
    if not has_any:
        print("WARN: Output lacks epistemic state labels")
    return True  # Warn only

def check_provenance(output):
    """Verify output records provenance."""
    if 'source:' not in output.lower() and 'provenance:' not in output.lower():
        print("WARN: Output lacks provenance recording")
    return True

def check_confidence_ceiling(output):
    """Verify output declares confidence ceiling."""
    if 'confidence' not in output.lower():
        print("WARN: Output lacks confidence ceiling declaration")
    return True

def main():
    # Read output from stdin (piped by harness)
    output = sys.stdin.read() if not sys.stdin.isatty() else ""
    if output:
        check_epistemic_labels(output)
        check_provenance(output)
        check_confidence_ceiling(output)
    return 0

if __name__ == "__main__":
    sys.exit(main())
