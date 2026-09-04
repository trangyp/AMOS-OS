#!/usr/bin/env python3
"""Expand thin architectural MOCs on GDrive by:
1. Fixing wrong H1 titles (should match the MOC name, not a random file in the dir)
2. Adding actual file listings with descriptions extracted from each file's H1 or frontmatter title
3. Adding missing Invariants/Gaps sections if absent

Operates on the Google Drive vault (authoritative).
Only modifies MOCs that have < 1200 chars of body content.
"""
import os, re, sys

VAULT = "/Users/mac/Library/CloudStorage/GoogleDrive-phanqtrang@gmail.com/My Drive/_AMOS_OS"
SKIP_DIRS = {'.obsidian', '.git', '.trash', 'node_modules', '.devin', '.agents', '.claude', 'copilot', 'scripts'}

def parse_fm(text):
    """Extract title from frontmatter."""
    if not text.startswith('---'):
        return None, text
    end = text.find('\n---', 3)
    if end < 0:
        return None, text
    fm = text[3:end]
    body = text[end+4:]
    title = None
    for line in fm.splitlines():
        if line.startswith('title:'):
            title = line[6:].strip().strip('"').strip("'")
    # Also get H1 from body
    h1_match = re.match(r'^#\s+(.+)$', body.strip(), re.M)
    h1 = h1_match.group(1).strip() if h1_match else None
    return {'title': title, 'h1': h1}, body

def get_file_description(filepath):
    """Get a short description from a file's frontmatter title or H1."""
    try:
        t = open(filepath, encoding='utf-8', errors='replace').read()
    except Exception:
        return None
    fm, body = parse_fm(t)
    title = (fm or {}).get('title')
    h1_match = re.match(r'^#\s+(.+)$', body.strip(), re.M)
    h1 = h1_match.group(1).strip() if h1_match else None
    # Get first paragraph after H1
    lines = body.strip().splitlines()
    first_para = []
    found_h1 = False
    for line in lines:
        if line.startswith('# ') and not found_h1:
            found_h1 = True
            continue
        if found_h1 and line.strip() and not line.startswith('#') and not line.startswith('---'):
            first_para.append(line.strip())
            if len(first_para) >= 3:
                break
    desc = ' '.join(first_para)[:200]
    return title or h1, desc

def list_dir_files(dir_path, moc_name):
    """List .md files in directory (excluding the MOC itself and subdirectories)."""
    files = []
    try:
        for f in sorted(os.listdir(dir_path)):
            if f.startswith('.') or not f.endswith('.md'):
                continue
            if f == moc_name:
                continue
            fp = os.path.join(dir_path, f)
            if os.path.isdir(fp):
                continue
            files.append((f, fp))
    except Exception:
        pass
    return files

def list_subdirs(dir_path):
    """List subdirectories that contain .md files."""
    subdirs = []
    try:
        for d in sorted(os.listdir(dir_path)):
            if d.startswith('.') or d in SKIP_DIRS:
                continue
            dp = os.path.join(dir_path, d)
            if not os.path.isdir(dp):
                continue
            # Check if it has any .md files
            has_md = any(f.endswith('.md') for f in os.listdir(dp))
            if has_md:
                subdirs.append((d, dp))
    except Exception:
        pass
    return subdirs

def expand_moc(moc_path):
    """Expand a single architectural MOC. Returns True if modified."""
    try:
        t = open(moc_path, encoding='utf-8', errors='replace').read()
    except Exception:
        return False

    fm, body = parse_fm(t)
    dir_path = os.path.dirname(moc_path)
    moc_name = os.path.basename(moc_path)
    dir_name = os.path.basename(dir_path)

    # Check if already well-expanded (has Files section with actual entries)
    has_files = re.search(r'## Files\s*\n\s*-\s+\[\[', body)
    if has_files:
        return False

    # List actual files
    files = list_dir_files(dir_path, moc_name)
    subdirs = list_subdirs(dir_path)

    # Build file listing
    file_lines = []
    for fname, fpath in files:
        info = get_file_description(fpath)
        if info:
            title, desc = info
            if desc:
                file_lines.append(f"- [[{os.path.relpath(fpath, VAULT).replace(os.sep, '/')}|{title}]] — {desc}")
            else:
                file_lines.append(f"- [[{os.path.relpath(fpath, VAULT).replace(os.sep, '/')}|{title}]]")
        else:
            file_lines.append(f"- [[{os.path.relpath(fpath, VAULT).replace(os.sep, '/')}|{fname[:-3]}]]")

    subdir_lines = []
    for dname, dp in subdirs:
        # Find sub-MOC
        sub_moc = None
        for f in os.listdir(dp):
            if '_MOC' in f and f.endswith('.md'):
                sub_moc = f
                break
        rel = os.path.relpath(dp, VAULT).replace(os.sep, '/')
        if sub_moc:
            subdir_lines.append(f"- [[{rel}/{sub_moc[:-3]}|{dname}]] — subdirectory with {sum(1 for f in os.listdir(dp) if f.endswith('.md'))} notes")
        else:
            subdir_lines.append(f"- `{dname}/` — subdirectory with {sum(1 for f in os.listdir(dp) if f.endswith('.md'))} notes")

    # Build the replacement content
    # Find or create ## Files section
    files_section = "## Files\n\n"
    if file_lines:
        files_section += '\n'.join(file_lines) + '\n'
    else:
        files_section += "_(no standalone .md files in this directory)_\n"

    if subdir_lines:
        files_section += f"\n## Subdirectories\n\n" + '\n'.join(subdir_lines) + '\n'

    # Add Invariants if missing
    invariants_section = ""
    if '## Invariants' not in body:
        invariants_section = """
## Invariants

- All listed files belong to the same directory scope.
- No file is promoted to canon status merely by being listed.
- Parent/child MOC links must remain acyclic.
- This MOC is navigation only; it does not own implementation authority.

## Gaps

- Files listed here reflect the current directory inventory; missing `SKILL.md`, `CONTRACT.md`, or `README.md` files are recorded as `UNKNOWN/GAP` unless a governing artifact exists.
"""

    # Add Related section
    parent_rel = ""
    if '## Related' not in body:
        # Find parent MOC
        parent_dir = os.path.dirname(dir_path)
        parent_moc_name = os.path.basename(parent_dir) + '_MOC.md'
        parent_moc_path = os.path.join(parent_dir, parent_moc_name)
        if os.path.exists(parent_moc_path):
            parent_rel = os.path.relpath(parent_moc_path, VAULT).replace(os.sep, '/')[:-3]
            parent_section = f"\n## Related\n\n- [[{parent_rel}|{os.path.basename(parent_dir)} MOC]]\n"
        else:
            parent_section = ""

    # Now reconstruct: find "## Files" or end of Purpose/MECE section
    # Strategy: replace everything from "## Files" onward, or append after MECE scope

    # Find existing ## Files
    files_match = re.search(r'## Files', body)
    if files_match:
        # Replace from ## Files to end (but preserve trailing parent links)
        before = body[:files_match.start()]
        # Find trailing separator links
        after = body[files_match.start():]
        # Extract trailing links after last ____
        trail_match = re.search(r'\n_{5,}.*$', after, re.S)
        trail = trail_match.group(0) if trail_match else ''
        new_body = before.rstrip() + '\n\n' + files_section
        if invariants_section:
            new_body += invariants_section
        if parent_section:
            new_body += parent_section
        if trail:
            new_body += '\n' + trail
    else:
        # No ## Files section — find insertion point after MECE scope or Purpose
        mece_match = re.search(r'## MECE scope', body)
        if mece_match:
            # Find end of MECE section (next ## or end)
            after_mece = body[mece_match.end():]
            next_section = re.search(r'\n## ', after_mece)
            if next_section:
                insert_pos = mece_match.end() + next_section.start()
                before = body[:insert_pos]
                after = body[insert_pos:]
                new_body = before.rstrip() + '\n\n' + files_section
                if invariants_section:
                    new_body += invariants_section
                if parent_section:
                    new_body += parent_section
                new_body += '\n' + after
            else:
                new_body = body.rstrip() + '\n\n' + files_section
                if invariants_section:
                    new_body += invariants_section
                if parent_section:
                    new_body += parent_section
        else:
            # Just append
            new_body = body.rstrip() + '\n\n' + files_section
            if invariants_section:
                new_body += invariants_section
            if parent_section:
                new_body += parent_section

    # Reconstruct full file
    new_t = t[:t.find('\n---', 3)+4] + new_body

    try:
        open(moc_path, 'w', encoding='utf-8').write(new_t)
        return True
    except Exception as e:
        print(f"  ERROR: {moc_path}: {e}", file=sys.stderr)
        return False

def main():
    # Find all MOCs (non-skill) that are thin
    skip = SKIP_DIRS
    mocs_to_expand = []

    for dp, dn, fn in os.walk(VAULT):
        dn[:] = [d for d in dn if d not in skip and not d.startswith('.tagmigrate')]
        for f in fn:
            if '_MOC' in f and f.endswith('.md'):
                p = os.path.join(dp, f)
                # Skip skill MOCs
                if '/07_SKILLS/' in p:
                    continue
                # Skip archive
                if '/24_ARCHIVE/' in p:
                    continue
                try:
                    t = open(p, encoding='utf-8', errors='replace').read()
                except Exception:
                    continue
                fm, body = parse_fm(t)
                bl = len(body.strip())
                # Check if it has actual file listings
                has_files = re.search(r'## Files\s*\n\s*-\s+\[\[', body)
                if bl < 1500 and not has_files:
                    mocs_to_expand.append(p)

    print(f"Found {len(mocs_to_expand)} thin architectural MOCs to expand", file=sys.stderr)

    fixed = 0
    for i, p in enumerate(mocs_to_expand):
        rel = os.path.relpath(p, VAULT)
        try:
            if expand_moc(p):
                fixed += 1
                print(f"  [{fixed}] {rel}")
        except Exception as e:
            print(f"  ERROR: {rel}: {e}", file=sys.stderr)

    print(f"\nDone: {fixed} expanded out of {len(mocs_to_expand)}")

if __name__ == '__main__':
    main()
