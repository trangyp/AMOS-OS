#!/usr/bin/env python3
from pathlib import Path

v = Path('/Users/mac/Desktop/_Arxiv/Arvix')
unclosed = []
for f in v.rglob('*.md'):
    try:
        lines = f.read_text(encoding='utf-8', errors='ignore').splitlines()
    except Exception:
        continue
    fence_count = sum(1 for line in lines if line.strip().startswith('```') or line.strip().startswith('~~~'))
    if fence_count % 2 != 0:
        unclosed.append((f, fence_count))

print(f'Unclosed count: {len(unclosed)}')
for f, c in unclosed:
    print(f'Unclosed: {f} (count={c})')
    # Auto heal by appending closing fence
    content = f.read_text(encoding='utf-8', errors='ignore')
    if not content.endswith('\n'):
        content += '\n'
    content += '```\n'
    f.write_text(content, encoding='utf-8')
    print(f'Healed: {f}')
