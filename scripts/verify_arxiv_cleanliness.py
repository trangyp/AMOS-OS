#!/usr/bin/env python3
import os
import re
from pathlib import Path

vault = Path('/Users/mac/Desktop/_Arxiv/Arvix')
total_md = 0
unclosed = []
malformed = []

FENCE_PATTERN = re.compile(r'^(```+|~~~+)')

for root, dirs, files in os.walk(vault):
    rel_parts = Path(root).relative_to(vault).parts
    if any(p.startswith('.') or p.startswith('.tagmigrate') or p == 'node_modules' for p in rel_parts):
        continue
    for fn in files:
        if fn.endswith('.md'):
            total_md += 1
            p = Path(root) / fn
            try:
                content = p.read_text(encoding='utf-8')
            except Exception:
                continue
            if content.startswith('---'):
                parts = content.split('---', 2)
                if len(parts) < 3:
                    malformed.append(str(p.relative_to(vault)))
            
            # CommonMark/GFM code fence state machine
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
                        # Opening fence
                        active_fence_char = char
                        active_fence_len = flen
                    else:
                        # Closing fence must match same char and length >= opening length
                        if char == active_fence_char and flen >= active_fence_len:
                            active_fence_char = None
                            active_fence_len = 0
            
            if active_fence_char is not None:
                unclosed.append(str(p.relative_to(vault)))

print(f"=== Verification Report for ArXiv Vault ===")
print(f"Vault Path: {vault}")
print(f"Total Markdown Files Scanned: {total_md}")
print(f"Unclosed Fences: {len(unclosed)}")
print(f"Malformed Frontmatters: {len(malformed)}")
if unclosed:
    print(f"Unclosed files: {unclosed}")
