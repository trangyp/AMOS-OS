#!/usr/bin/env python3
"""Fix unclosed code blocks - stray fence after Related line."""
from pathlib import Path

files = [
    '11_KNOWLEDGE/engine/OMIS_CODING_ENGINE_V1_4_0.md',
    '11_KNOWLEDGE/engine/EV_SUPER_ENGINE.md',
    '11_KNOWLEDGE/engine/CODE_SUPER_ENGINE.md',
    '11_KNOWLEDGE/engine/AUTOMATION_SUPER_ENGINE.md',
    '11_KNOWLEDGE/engine/AMOS_AUTOMATION_ENGINE_V1_0_0.md',
    '11_KNOWLEDGE/engine/AMOS_EV_INFRASTRUCTURE_AGENTS_SUPER_ENGINE_VINFINITY_X100K_GLOBAL_C_REFACTORED_V3.md',
    '11_KNOWLEDGE/kernel/AMOS_AUTOMATION_KERNEL.md',
    '11_KNOWLEDGE/kernel/AMOS_POLICY_GEOSTRATEGY_KERNEL_V0.md',
    '11_KNOWLEDGE/kernel/ORG_GOVERNANCE_KERNEL.md',
    '11_KNOWLEDGE/kernel/AMOS_KERNEL_CONFIG_KERNEL.md',
]

FENCE = chr(96) * 3  # ```

for fpath in files:
    p = Path(fpath)
    if not p.exists():
        print(f'SKIP (not found): {fpath}')
        continue
    text = p.read_text(encoding='utf-8', errors='replace')
    lines = text.split('\n')
    new_lines = []
    fixed = False
    for i, line in enumerate(lines):
        # If this is a bare fence line and nearby context has **Related:**
        if line.strip() == FENCE and i > 0:
            look_back = '\n'.join(lines[max(0, i-5):i])
            if '**Related:**' in look_back and '}' not in line:
                print(f'FIXED {fpath}: removed stray fence at line {i+1}')
                fixed = True
                continue
        new_lines.append(line)

    if fixed:
        p.write_text('\n'.join(new_lines), encoding='utf-8')
    else:
        print(f'NO FIX NEEDED: {fpath}')
