import glob

# Update 00_ROOT/ALL_FILES_LINK_REGISTRY.md
try:
    with open('00_ROOT/ALL_FILES_LINK_REGISTRY.md', 'r') as f:
        c = f.read()
    c = c.replace('[[.github/copilot-instructions]]', '[[copilot-instructions]]')
    with open('00_ROOT/ALL_FILES_LINK_REGISTRY.md', 'w') as f:
        f.write(c)
    print('Updated ALL_FILES_LINK_REGISTRY.md')
except Exception as e:
    print(f"Error on ALL_FILES_LINK_REGISTRY: {e}")

# Also create root-level copilot-instructions.md or alias
if not glob.glob('copilot-instructions.md') and not glob.glob('03_CONTROL_PLANE/copilot-instructions.md'):
    with open('03_CONTROL_PLANE/copilot-instructions.md', 'w') as f:
        f.write('''---
title: copilot-instructions
type: control_surface
amos_core_target: v4.4
origin_architect: Trang Phan
status: ACTIVE
conclusion_class: GOVERNANCE
rscf:
  state: ACTIVE
  provenance: amos_os_copilot_instructions
  scope: active__AMOS_OS
---

# AMOS OS Copilot Instructions

Copilot execution and governance instructions adhering to the AMOS v4.4 Canonical Contract.
''')

files = glob.glob('copilot/copilot-conversations/*.md') + ['20_OPERATIONS/AMOS_OS_AUDIT_2026-09-03.md']
for fpath in files:
    try:
        with open(fpath, 'r', encoding='utf-8') as f:
            text = f.read()
        
        text = text.replace('[[...]]', '`[[...]]`')
        text = text.replace('[[Title]]', '`[[Title]]`')
        text = text.replace('[[*_MOC]]', '`[[*_MOC]]`')
        text = text.replace('[["$", "style", ...]]', '`[["$", "style", ...]]`')
        text = text.replace('[["$","style",...]]', '`[["$","style",...]]`')
        text = text.replace('[[` to the next `]]', '`[[` to the next `]]`')
        text = text.replace('` double-separator artifacts, 1,972 malformed `[[Link]]', '` double-separator artifacts, 1,972 malformed \\`\\[\\[Link\\]\\]')
        text = text.replace('` double-separator artifacts, 1,972 malformed `\\[\\[Link\\]\\]', '` double-separator artifacts, 1,972 malformed \\`\\[\\[Link\\]\\]')

        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(text)
        print('Cleaned:', fpath)
    except Exception as e:
        print(f"Error on {fpath}: {e}")
