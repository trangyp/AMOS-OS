#!/usr/bin/env python3
"""Expand thin skill MOCs by injecting Purpose/MECE/Invariants sections
derived from the corresponding SKILL.md frontmatter.

Operates on the Google Drive vault (authoritative).
Only modifies MOCs that lack a '## Purpose' section.
"""
import os, re, sys, glob

VAULT = "/Users/mac/Library/CloudStorage/GoogleDrive-phanqtrang@gmail.com/My Drive/_AMOS_OS"
SKILLS_DIR = os.path.join(VAULT, "07_SKILLS")

def parse_frontmatter(text):
    """Parse YAML frontmatter into a dict (simple key: value parsing)."""
    if not text.startswith('---'):
        return {}, text
    end = text.find('\n---', 3)
    if end < 0:
        return {}, text
    fm_text = text[3:end]
    body = text[end+4:]
    fm = {}
    current_key = None
    current_list = None
    for line in fm_text.splitlines():
        if line.startswith('  - ') and current_key:
            if current_list is None:
                current_list = []
            current_list.append(line[4:].strip().strip('"').strip("'"))
            fm[current_key] = current_list
            continue
        if line.startswith('  ') and current_key:
            # nested dict or continuation
            sub = line.strip()
            if ':' in sub:
                sk, sv = sub.split(':', 1)
                if isinstance(fm.get(current_key), dict):
                    fm[current_key][sk.strip()] = sv.strip().strip('"').strip("'")
                else:
                    fm[current_key] = {sk.strip(): sv.strip().strip('"').strip("'")}
            continue
        if ':' in line and not line.startswith(' '):
            k, v = line.split(':', 1)
            current_key = k.strip()
            v = v.strip()
            if v:
                fm[current_key] = v.strip('"').strip("'")
                current_list = None
            else:
                fm[current_key] = {}
                current_list = None
    return fm, body

def extract_description(fm):
    """Get the description from frontmatter."""
    desc = fm.get('description', '')
    if isinstance(desc, dict):
        desc = str(desc)
    return desc.strip()

def split_use_when(desc):
    """Split description into core purpose and use-when conditions."""
    if not desc:
        return '', ''
    # Find "Use when" boundary
    m = re.search(r'\.\s*Use when\b', desc, re.I)
    if m:
        purpose = desc[:m.start()+1].strip()
        use_when = desc[m.start()+2:].strip()
    else:
        # Try "Do not use" boundary
        m2 = re.search(r'\.\s*Do not use\b', desc, re.I)
        if m2:
            purpose = desc[:m2.start()+1].strip()
            use_when = ''
        else:
            purpose = desc[:300].strip()
            use_when = ''
    return purpose, use_when

def build_expansion(skill_name, fm, moc_path):
    """Build the Purpose/MECE/Invariants/Related sections to inject."""
    desc = extract_description(fm)
    purpose, use_when = split_use_when(desc)
    parent = fm.get('parent_skill', '')
    domain = fm.get('domain', '')
    epistemic = fm.get('epistemic_class', '')
    hml = fm.get('hml_level', '')

    # Truncate purpose for readability
    if len(purpose) > 500:
        purpose = purpose[:497] + '...'

    sections = []

    # Purpose
    sections.append(f"## Purpose\n\n{purpose}" if purpose else "## Purpose\n\nThis skill MOC indexes the canonical skill package and its reference materials within the AMOS OS vault.")

    # MECE scope
    scope_lines = [
        "## MECE scope\n",
        f"- This MOC owns navigation for the `{skill_name}` skill directory.",
        "- It indexes SKILL.md, references/, and any sub-MOCs within the skill folder.",
        "- It does not own implementation authority, canon promotion, or runtime enforcement.",
        "- Parent skill: " + (f"`{parent}`" if parent else "UNKNOWN/GAP"),
        f"- Domain: `{domain}`" if domain else "- Domain: UNKNOWN/GAP",
        f"- Epistemic class: `{epistemic}`" if epistemic else "",
        f"- H/M/L level: `{hml}`" if hml else "",
    ]
    sections.append('\n'.join(s for s in scope_lines if s))

    # Invariants
    sections.append("""## Invariants

- The SKILL.md is the canonical skill specification; this MOC is navigation only.
- No file is promoted to canon status merely by being listed here.
- Reference materials are SOURCE_CLAIM unless separately promoted.
- Parent/child MOC links must remain acyclic.""")

    # Use-when (if available)
    if use_when:
        if len(use_when) > 600:
            use_when = use_when[:597] + '...'
        sections.append(f"## Use when\n\n{use_when}")

    return '\n\n'.join(sections)

def process_moc(moc_path, skill_dir):
    """Process a single skill MOC. Returns True if modified."""
    try:
        t = open(moc_path, encoding='utf-8', errors='replace').read()
    except Exception:
        return False

    # Check if already has Purpose section
    if '## Purpose' in t:
        return False

    # Read SKILL.md
    skill_md_path = os.path.join(skill_dir, 'SKILL.md')
    if not os.path.exists(skill_md_path):
        return False

    try:
        skill_text = open(skill_md_path, encoding='utf-8', errors='replace').read()
    except Exception:
        return False

    fm, _ = parse_frontmatter(skill_text)
    skill_name = fm.get('name', os.path.basename(skill_dir))

    expansion = build_expansion(skill_name, fm, moc_path)

    # Find insertion point: after the header block, before "## Files"
    # The pattern is typically:
    # # Title
    # **Path:** ...
    # **Files:** ...
    #
    # ## Files

    # Insert expansion before "## Files" or "## Subdirectories"
    insert_match = re.search(r'\n## (Files|Subdirectories|Notes)', t)
    if insert_match:
        insert_pos = insert_match.start()
        new_t = t[:insert_pos] + '\n' + expansion + '\n' + t[insert_pos:]
    else:
        # Append before the trailing separator/parent links
        # Find the first "____" separator line
        sep_match = re.search(r'\n_{5,}', t)
        if sep_match:
            insert_pos = sep_match.start()
            new_t = t[:insert_pos] + '\n' + expansion + '\n\n' + t[insert_pos:]
        else:
            new_t = t.rstrip() + '\n\n' + expansion + '\n'

    try:
        open(moc_path, 'w', encoding='utf-8').write(new_t)
        return True
    except Exception as e:
        print(f"  ERROR writing {moc_path}: {e}", file=sys.stderr)
        return False

def main():
    if not os.path.isdir(SKILLS_DIR):
        print(f"ERROR: {SKILLS_DIR} not found", file=sys.stderr)
        sys.exit(1)

    skill_dirs = []
    for d in sorted(os.listdir(SKILLS_DIR)):
        sd = os.path.join(SKILLS_DIR, d)
        if not os.path.isdir(sd):
            continue
        if d.startswith('.') or d in ('skill-registry-catalog.md',):
            continue
        skill_dirs.append((d, sd))

    print(f"Found {len(skill_dirs)} skill directories", file=sys.stderr)
    fixed = 0
    skipped = 0
    errors = 0

    for i, (name, sd) in enumerate(skill_dirs):
        moc_path = os.path.join(sd, f"{name}_MOC.md")
        if not os.path.exists(moc_path):
            skipped += 1
            continue
        try:
            if process_moc(moc_path, sd):
                fixed += 1
                if fixed % 50 == 0:
                    print(f"  ...fixed {fixed} MOCs so far", file=sys.stderr)
            else:
                skipped += 1
        except Exception as e:
            errors += 1
            print(f"  ERROR: {name}: {e}", file=sys.stderr)

    print(f"\nDone: {fixed} expanded, {skipped} skipped, {errors} errors")

if __name__ == '__main__':
    main()
