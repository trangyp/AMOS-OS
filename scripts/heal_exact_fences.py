#!/usr/bin/env python3
import os
import re
from pathlib import Path

vault = Path('/Users/mac/Desktop/_Arxiv/Arvix')
FENCE_PATTERN = re.compile(r'^(```+|~~~+)')
healed = []

for root, dirs, files in os.walk(vault):
    rel_parts = Path(root).relative_to(vault).parts
    if any(p.startswith('.') or p.startswith('.tagmigrate') or p == 'node_modules' for p in rel_parts):
        continue
    for fn in files:
        if fn.endswith('.md'):
            p = Path(root) / fn
            try:
                content = p.read_text(encoding='utf-8')
            except Exception:
                continue
            
            lines = content.splitlines()
            active_fence_char = None
            active_fence_len = 0
            
            for line in lines:
                stripped = line.strip()
                match = FENCE_PATTERN.match(stripped)
                if match:
                    fence_token = match.group(1)
                    char = fence_token[0]
                    flen = len(fence_token)
                    
                    if active_fence_char is None:
                        active_fence_char = char
                        active_fence_len = flen
                    else:
                        if char == active_fence_char and flen >= active_fence_len:
                            active_fence_char = None
                            active_fence_len = 0
            
            if active_fence_char is not None:
                # Add exact closing fence
                closing = active_fence_char * active_fence_len
                if not content.endswith('\n'):
                    content += '\n'
                content += f"{closing}\n"
                p.write_text(content, encoding='utf-8')
                healed.append((str(p.relative_to(vault)), closing))

print(f"Healed {len(healed)} files with exact CommonMark closing fences:")
for fn, closing in healed:
    print(f"  - {fn} (added '{closing}')")
