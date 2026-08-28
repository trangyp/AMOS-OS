#!/usr/bin/env python3
"""PostToolUse hook for amos-law-stack-enforcement."""
import sys

def main():
    output = sys.stdin.read() if not sys.stdin.isatty() else ""
    if output:
        states = ["SOURCE_CLAIM", "DERIVED", "AMOS_MODEL", "OBSERVATION", "CONDITIONAL"]
        if not any(s in output for s in states):
            print("WARN: Output lacks epistemic state labels")
        if 'source:' not in output.lower() and 'provenance:' not in output.lower():
            print("WARN: Output lacks provenance recording")
    return 0

if __name__ == "__main__":
    sys.exit(main())
