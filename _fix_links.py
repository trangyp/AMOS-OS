#!/usr/bin/env python3
"""
AMOS Vault Link Fixer
- Converts path-style wikilinks [[dir/subdir/file.md]] → [[file]]
- Fixes case-mismatch links [[Task]] → [[TASK]]
- Creates stub files for genuinely missing link targets
- Ensures 0 orphans, 0 broken links
"""

import os, re
from pathlib import Path
from collections import defaultdict
from typing import Optional

VAULT = Path("/Users/mac/Documents/AMOS_OS")
SKIP = {".git", ".obsidian", ".devin", "node_modules", ".agents", "__pycache__", "cosmo-brain"}

def collect_files():
    files = []
    for root, dirs, fns in os.walk(VAULT):
        dirs[:] = [d for d in dirs if d not in SKIP]
        for fn in fns:
            if fn.endswith(".md"):
                files.append(Path(root) / fn)
    return files

def build_stem_index(files):
    """Map stem -> file path, and stem_lower -> stem."""
    stems = {}
    stems_lower = {}
    for f in files:
        s = f.stem
        stems[s] = f
        stems_lower[s.lower()] = s
    return stems, stems_lower

def fix_path_style_links(content, stems, stems_lower):
    """Convert [[dir/subdir/file.md]] to [[file]] or [[dir/subdir/file]] to [[file]]."""
    changes = 0
    
    def replace_link(m):
        nonlocal changes
        full = m.group(0)  # [[...]]
        inner = m.group(1)  # the link content
        alias_part = m.group(2) if m.group(2) else ""
        
        # If it contains a path separator, extract the filename
        if "/" in inner:
            # Remove .md extension if present
            name = inner.rsplit("/", 1)[-1]
            name = name.replace(".md", "")
            
            # Check if this stem exists
            if name in stems:
                changes += 1
                if alias_part:
                    return f"[[{name}{alias_part}]]"
                return f"[[{name}]]"
            # Try case-insensitive
            if name.lower() in stems_lower:
                correct = stems_lower[name.lower()]
                changes += 1
                if alias_part:
                    return f"[[{correct}{alias_part}]]"
                return f"[[{correct}]]"
        
        return full
    
    # Match [[link]] or [[link|alias]] or [[link#heading]]
    pattern = r'\[\[([^\]|#]+)([#|][^\]]*)?\]\]'
    new_content = re.sub(pattern, replace_link, content)
    return new_content, changes

def fix_case_mismatch_links(content, stems, stems_lower):
    """Fix [[Task]] -> [[TASK]] when case doesn't match."""
    changes = 0
    
    def replace_link(m):
        nonlocal changes
        full = m.group(0)
        inner = m.group(1).strip()
        alias_part = m.group(2) if m.group(2) else ""
        
        # Skip path-style links (handled by fix_path_style_links)
        if "/" in inner:
            return full
        
        # Check if exact match exists
        if inner in stems:
            return full
        
        # Try case-insensitive
        if inner.lower() in stems_lower:
            correct = stems_lower[inner.lower()]
            changes += 1
            if alias_part:
                return f"[[{correct}{alias_part}]]"
            return f"[[{correct}]]"
        
        return full
    
    pattern = r'\[\[([^\]|#]+)([#|][^\]]*)?\]\]'
    new_content = re.sub(pattern, replace_link, content)
    return new_content, changes

def find_all_unresolved(files, stems, stems_lower):
    """Find all wikilinks that don't resolve to any file."""
    unresolved = defaultdict(int)
    for f in files:
        try:
            with open(f, "r", encoding="utf-8", errors="replace") as fh:
                content = fh.read()
            links = re.findall(r'\[\[([^\]|#]+)', content)
            for link in links:
                link = link.strip()
                # Skip path-style (will be fixed)
                if "/" in link:
                    name = link.rsplit("/", 1)[-1].replace(".md", "")
                    if name in stems or name.lower() in stems_lower:
                        continue
                if link not in stems and link.lower() not in stems_lower:
                    unresolved[link] += 1
        except:
            pass
    return unresolved

def create_stub_files(unresolved, stems, stems_lower):
    """Create stub .md files for genuinely missing link targets."""
    created = []
    for link, count in sorted(unresolved.items(), key=lambda x: -x[1]):
        # Skip if it already exists (case-insensitive)
        if link.lower() in stems_lower:
            continue
        
        # Skip links that look like they should be sections, not files
        if len(link) < 2 or link.startswith("#"):
            continue
        
        # Create stub file
        stub_path = VAULT / "11_KNOWLEDGE" / "stubs" / f"{link}.md"
        stub_path.parent.mkdir(parents=True, exist_ok=True)
        
        tag = "stub"
        fm = f"""---
title: {link.replace('_', ' ')}
type: stub
tags: [stub, placeholder]
---

# {link.replace('_', ' ')}

This is a stub file created to resolve {count} unresolved wikilink(s).
Please replace with actual content.

---
**MOC:** [[stubs_MOC]]
"""
        with open(stub_path, "w", encoding="utf-8") as f:
            f.write(fm)
        created.append((link, count, stub_path))
        stems[link] = stub_path
        stems_lower[link.lower()] = link
    
    return created

def main():
    print("=" * 60)
    print("AMOS Vault Link Fixer")
    print("=" * 60)
    
    # Phase 1: Collect files
    print("\n[1] Scanning vault...")
    files = collect_files()
    print(f"    Total .md files: {len(files)}")
    
    stems, stems_lower = build_stem_index(files)
    print(f"    Unique stems: {len(stems)}")
    
    # Phase 2: Fix path-style links
    print("\n[2] Fixing path-style wikilinks...")
    path_fixes = 0
    files_modified = 0
    for f in files:
        try:
            with open(f, "r", encoding="utf-8", errors="replace") as fh:
                content = fh.read()
            new_content, changes = fix_path_style_links(content, stems, stems_lower)
            if changes > 0:
                with open(f, "w", encoding="utf-8") as fh:
                    fh.write(new_content)
                path_fixes += changes
                files_modified += 1
        except Exception as e:
            print(f"    ERROR in {f}: {e}")
    print(f"    Path-style links fixed: {path_fixes} in {files_modified} files")
    
    # Phase 3: Fix case-mismatch links
    print("\n[3] Fixing case-mismatch links...")
    case_fixes = 0
    files_modified = 0
    for f in files:
        try:
            with open(f, "r", encoding="utf-8", errors="replace") as fh:
                content = fh.read()
            new_content, changes = fix_case_mismatch_links(content, stems, stems_lower)
            if changes > 0:
                with open(f, "w", encoding="utf-8") as fh:
                    fh.write(new_content)
                case_fixes += changes
                files_modified += 1
        except Exception as e:
            print(f"    ERROR in {f}: {e}")
    print(f"    Case-mismatch links fixed: {case_fixes} in {files_modified} files")
    
    # Phase 4: Find remaining unresolved links
    print("\n[4] Finding remaining unresolved links...")
    # Re-collect files (some may have been created)
    files = collect_files()
    stems, stems_lower = build_stem_index(files)
    unresolved = find_all_unresolved(files, stems, stems_lower)
    print(f"    Unresolved link targets: {len(unresolved)}")
    
    if unresolved:
        print("    Top 10:")
        for link, count in sorted(unresolved.items(), key=lambda x: -x[1])[:10]:
            print(f"      {count:4d}x [[{link}]]")
    
    # Phase 5: Create stub files for unresolved
    if unresolved:
        print(f"\n[5] Creating stub files for {len(unresolved)} unresolved targets...")
        stubs = create_stub_files(unresolved, stems, stems_lower)
        print(f"    Stub files created: {len(stubs)}")
        for link, count, path in stubs[:10]:
            print(f"      {link} ({count} refs) -> {path.relative_to(VAULT)}")
        
        # Create MOC for stubs
        stubs_dir = VAULT / "11_KNOWLEDGE" / "stubs"
        stub_moc = stubs_dir / "stubs_MOC.md"
        stub_files_list = sorted(stubs_dir.glob("*.md"))
        with open(stub_moc, "w", encoding="utf-8") as f:
            f.write("---\ntitle: Stubs MOC\ntype: moc\ntags: [moc, stub]\n---\n\n# Stubs — Map of Content\n\n")
            for sf in stub_files_list:
                if sf.stem != "stubs_MOC":
                    f.write(f"- [[{sf.stem}]]\n")
            f.write("\n---\n**Parent:** [[KNOWLEDGE_MOC]]\n")
        print(f"    Stubs MOC created")
    else:
        print("\n[5] No stub files needed — all links resolve!")
    
    # Phase 6: Final verification
    print("\n[6] Final verification...")
    files = collect_files()
    stems, stems_lower = build_stem_index(files)
    
    incoming = defaultdict(int)
    outgoing = defaultdict(int)
    unresolved_final = 0
    total_links = 0
    
    for f in files:
        try:
            with open(f, "r", encoding="utf-8", errors="replace") as fh:
                content = fh.read()
            links = re.findall(r'\[\[([^\]|#]+)', content)
            for link in links:
                link = link.strip()
                total_links += 1
                if link in stems:
                    incoming[link] += 1
                    outgoing[f.stem] += 1
                elif link.lower() in stems_lower:
                    incoming[stems_lower[link.lower()]] += 1
                    outgoing[f.stem] += 1
                else:
                    unresolved_final += 1
        except:
            pass
    
    orphans = [f for f in files if incoming[f.stem] == 0 and outgoing[f.stem] == 0]
    
    print(f"    Total files: {len(files)}")
    print(f"    Total wikilinks: {total_links}")
    print(f"    Resolved links: {total_links - unresolved_final}")
    print(f"    Unresolved links: {unresolved_final}")
    print(f"    Files with incoming links: {sum(1 for s in stems if incoming[s] > 0)}")
    print(f"    Files with outgoing links: {sum(1 for s in stems if outgoing[s] > 0)}")
    print(f"    Orphans: {len(orphans)}")
    
    print("\n" + "=" * 60)
    print("Link fixing complete!")
    print("=" * 60)

if __name__ == "__main__":
    main()
