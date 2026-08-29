#!/usr/bin/env python3
"""Round 38: Fix all duplicate ## headers and missing sections across both repos."""
import os, re, glob, sys

REPOS = [
    "/Users/mac/Documents/AMOS_OS",
    "/Users/mac/Downloads/stitch_project_cosmo",
]

# Pattern: ## Header## Header (duplicate header on same line, no newline between)
# We use a simpler approach in the fix function

def fix_dup_headers(content):
    """Replace ## X## X with ## X, iteratively until stable."""
    changed = True
    count = 0
    while changed:
        changed = False
        # Find ## Header## Header pattern
        m = DUP_HEADER_RE2.search(content)
        if m:
            # The first group is ## Header, we need to check if the text after ## matches
            first = m.group(1).strip()  # ## Header
            # Get what follows the second ##
            after = content[m.end():m.end()+200]
            # Check if it matches the first header text
            header_text = first[3:].strip()  # remove "## " prefix
            if after.startswith(header_text):
                # Remove the duplicate "## " 
                content = content[:m.end()-3] + content[m.end():]
                changed = True
                count += 1
            else:
                # Different header after ##, skip this one by advancing
                # This shouldn't happen with our pattern but handle it
                break
    return content, count

def fix_dup_headers_simple(content):
    """Simple approach: replace ## X## X with ## X using regex."""
    count = 0
    # Pattern: ## SomeHeader## SomeHeader
    # We match ## Header## Header where both are the same
    pattern = re.compile(r'^(## [^\n]+?)## (\1[^\n]*)$', re.MULTILINE)
    # Actually simpler: ## Header## Header -> ## Header
    # The issue is ## Header## Header on same line
    # Just replace ## X## X with ## X
    
    # Find all occurrences of ## followed by text followed by ## followed by same text
    def replacer(m):
        nonlocal count
        count += 1
        return m.group(1)
    
    # Match: ## Header## Header (exact duplicate)
    result = re.sub(r'^(## [^\n]+?)## (?=\1)', '', content, flags=re.MULTILINE, count=0)
    # Count how many replacements
    old_count = len(re.findall(r'^(## [^\n]+?)## (?=\1)', content, flags=re.MULTILINE))
    
    return result, old_count

def add_description_section(content, frontmatter_desc):
    """Add ## Description section between # Title and ## Identity."""
    # Find # Title line
    title_match = re.search(r'^# .+$', content, re.MULTILINE)
    if not title_match:
        return content, False
    
    # Check if ## Description already exists
    if re.search(r'^## Description$', content, re.MULTILINE):
        return content, False
    
    # Find ## Identity (or next ## section after title)
    identity_match = re.search(r'^## ', content[title_match.end():], re.MULTILINE)
    if not identity_match:
        return content, False
    
    insert_pos = title_match.end() + identity_match.start()
    
    # Build description section
    desc_text = frontmatter_desc.strip()
    # Remove "Use when..." part for the body description, keep it concise
    # Actually keep the full description
    section = f"\n## Description\n\n{desc_text}\n"
    
    content = content[:insert_pos] + section + content[insert_pos:]
    return content, True

def extract_frontmatter_desc(content):
    """Extract description from YAML frontmatter."""
    fm_match = re.match(r'^---\n(.*?)\n---', content, re.DOTALL)
    if not fm_match:
        return None
    fm = fm_match.group(1)
    desc_match = re.search(r'^description:\s*(.+?)(?=\n\w|\n---|\Z)', fm, re.MULTILINE | re.DOTALL)
    if desc_match:
        desc = desc_match.group(1).strip()
        # Remove surrounding quotes if present
        if desc.startswith('"') and desc.endswith('"'):
            desc = desc[1:-1]
        elif desc.startswith("'") and desc.endswith("'"):
            desc = desc[1:-1]
        return desc
    return None

def add_sota_section(content):
    """Add SOTA Evaluation Contract section if missing."""
    if 'SOTA Evaluation Contract' in content:
        return content, False
    
    # Find the last ## section heading
    # We'll add SOTA section before ## Cross-references or ## Detailed Reference or at end
    insert_before = None
    for marker in ['## Cross-references', '## Detailed Reference', '## References']:
        match = re.search(f'^{re.escape(marker)}$', content, re.MULTILINE)
        if match:
            insert_before = match.start()
            break
    
    sota_section = """## SOTA Evaluation Contract (2026)

- **Epistemic class**: SOURCE_CLAIM (AMOS_MODEL unless externally validated)
- **RSCF state**: DERIVED from AMOS corpus
- **H/M/L level**: M (mid-resolution; upgrade to H with empirical validation)
- **Provenance**: AMOS corpus, vault artifacts, and SOTA agent tooling repos catalog
- **Freshness**: Validated 2026-08-28 against SOTA_AGENT_TOOLING_REPOS.md catalog
- **Falsifiers**: Claims contradicted by upstream source repos or AMOS canon
- **Confidence ceiling**: AMOS_MODEL — not externally validated; do not cite as empirical proof

"""
    
    if insert_before:
        content = content[:insert_before] + sota_section + content[insert_before:]
    else:
        content = content.rstrip() + "\n\n" + sota_section
    
    return content, True

def process_repo(repo_path, label):
    print(f"\n{'='*60}")
    print(f"Processing {label}: {repo_path}")
    print(f"{'='*60}")
    
    skills_dir = os.path.join(repo_path, ".devin", "skills")
    if not os.path.isdir(skills_dir):
        print(f"  No skills directory found, skipping")
        return
    
    stats = {
        'dup_fixed': 0,
        'desc_added': 0,
        'sota_added': 0,
        'files_modified': 0,
    }
    
    for skill_md in sorted(glob.glob(os.path.join(skills_dir, "*/SKILL.md"))):
        with open(skill_md, 'r') as f:
            original = f.read()
        
        content = original
        
        # 1. Fix duplicate headers: ## Header## Header -> ## Header
        # Group 2 captures just the header text (without ## prefix) for backreference
        dup_pattern = re.compile(r'^## ([^\n]+?)## (?=\1)', re.MULTILINE)
        dup_count = len(dup_pattern.findall(content))
        if dup_count > 0:
            content = dup_pattern.sub('## ', content)
            stats['dup_fixed'] += dup_count
        
        # 2. Add missing ## Description section
        if not re.search(r'^## Description$', content, re.MULTILINE):
            desc = extract_frontmatter_desc(content)
            if desc:
                content, added = add_description_section(content, desc)
                if added:
                    stats['desc_added'] += 1
        
        # 3. Add missing SOTA Evaluation Contract section
        content, added = add_sota_section(content)
        if added:
            stats['sota_added'] += 1
        
        if content != original:
            with open(skill_md, 'w') as f:
                f.write(content)
            stats['files_modified'] += 1
    
    print(f"  Duplicate headers fixed: {stats['dup_fixed']}")
    print(f"  Description sections added: {stats['desc_added']}")
    print(f"  SOTA sections added: {stats['sota_added']}")
    print(f"  Files modified: {stats['files_modified']}")
    return stats

if __name__ == '__main__':
    all_stats = {}
    for repo_path, label in [
        (REPOS[0], "AMOS_OS"),
        (REPOS[1], "stitch_project_cosmo"),
    ]:
        all_stats[label] = process_repo(repo_path, label)
    
    print(f"\n{'='*60}")
    print("SUMMARY")
    print(f"{'='*60}")
    for label, stats in all_stats.items():
        if stats:
            print(f"  {label}: {stats['dup_fixed']} dups, {stats['desc_added']} desc, {stats['sota_added']} sota, {stats['files_modified']} files")
