#!/usr/bin/env python3
from pathlib import Path

v = Path('/Users/mac/Desktop/_Arxiv/Arvix')
for f in v.rglob('*.md'):
    try:
        lines = f.read_text(encoding='utf-8', errors='ignore').splitlines()
    except Exception:
        continue
    fences = [line.strip() for line in lines if line.strip().startswith('```') or line.strip().startswith('~~~')]
    if len(fences) % 2 != 0:
        print(f"File: {f}")
        print(f"Fence count: {len(fences)}, Fences: {fences}")
        # Look at the first fence and match its exact backtick length
        first_fence = fences[0]
        # Count leading backticks or tildes
        char = first_fence[0]
        count = len(first_fence) - len(first_fence.lstrip(char))
        closing = char * count
        content = f.read_text(encoding='utf-8', errors='ignore')
        if not content.endswith('\n'):
            content += '\n'
        content += f"{closing}\n"
        f.write_text(content, encoding='utf-8')
        print(f"Auto-closed with '{closing}'")
