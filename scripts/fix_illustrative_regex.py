import re, glob

def fix_file(fpath):
    with open(fpath, 'r', encoding='utf-8') as f:
        text = f.read()
    
    # Replace literal [[...]] with `[[...]]`
    text = re.sub(r'(?<!`)(?:\[\[\.\.\.\]\])', r'`[[\.\.\.]]`', text)
    # Replace literal [[Title]] with `[[Title]]`
    text = re.sub(r'(?<!`)(?:\[\[Title\]\])', r'`[[Title]]`', text)
    # Replace literal [[*_MOC]] with `[[*_MOC]]`
    text = re.sub(r'(?<!`)(?:\[\[\*_MOC\]\])', r'`[[*_MOC]]`', text)
    # Replace literal [["$","style",...]] with `[["$","style",...]]`
    text = text.replace('[["$","style",...]]', '`[["$","style",...]]`')
    text = text.replace('MODEL_X\\n\\n[[MODEL_A [[*_MOC]]', '`MODEL_X\\n\\n[[MODEL_A]] [[*_MOC]]`')
    text = text.replace('MODEL_X\n\n[[MODEL_A [[*_MOC]]', '`MODEL_X\n\n[[MODEL_A]] [[*_MOC]]`')
    text = text.replace('` double-separator artifacts, 1,972 malformed `[[Link]]', '` double-separator artifacts, 1,972 malformed `\\[\\[Link\\]\\]')
    text = text.replace('` double-separator artifacts, 1,972 malformed \\`\\[\\[Link\\]\\]', '` double-separator artifacts, 1,972 malformed `\\[\\[Link\\]\\]')

    with open(fpath, 'w', encoding='utf-8') as f:
        f.write(text)

for fpath in glob.glob('copilot/copilot-conversations/*.md') + ['20_OPERATIONS/AMOS_OS_AUDIT_2026-09-03.md']:
    fix_file(fpath)

print('Finished final regex pass.')
