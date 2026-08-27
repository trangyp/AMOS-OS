#!/usr/bin/env python3
"""
AMOS Vault Normalizer
- Adds frontmatter (title, type, tags) to every .md file missing it
- Creates MOC (Map of Content) files for every directory that has .md files
- Links every file to its parent directory MOC (no orphans)
- Links every MOC to its parent MOC (hierarchical navigation)
- Builds a root index linking all top-level MOCs
"""

import os
import re
import json
from pathlib import Path
from collections import defaultdict
from typing import Optional

VAULT = Path("/Users/mac/Documents/AMOS_OS")
SKIP_DIRS = {".git", ".obsidian", ".devin", "node_modules", ".agents", "__pycache__", "cosmo-brain"}
MOC_SUFFIX = "_MOC"
ROOT_MOC_NAME = "AMOS_HOME"

def should_skip(path: Path) -> bool:
    parts = path.parts
    for skip in SKIP_DIRS:
        if skip in parts:
            return True
    return False

def get_title_from_filename(filepath: Path) -> str:
    name = filepath.stem
    name = name.replace("_", " ").replace("-", " ")
    return name

def get_dir_tag(dirpath: Path) -> str:
    """Generate a tag from the directory path."""
    rel = dirpath.relative_to(VAULT)
    parts = rel.parts
    if not parts or parts[0] == ".":
        return "vault"
    # Use the last directory name as the tag
    tag = parts[-1].lower().replace(" ", "-").replace("_", "-")
    # Clean up
    tag = re.sub(r"[^a-z0-9-]", "", tag)
    if not tag:
        tag = "vault"
    return tag

def has_frontmatter(filepath: Path) -> bool:
    try:
        with open(filepath, "r", encoding="utf-8", errors="replace") as f:
            first_line = f.readline()
            return first_line.strip() == "---"
    except:
        return False

def has_tags_in_frontmatter(filepath: Path) -> bool:
    try:
        with open(filepath, "r", encoding="utf-8", errors="replace") as f:
            content = f.read(2000)
            if not content.startswith("---"):
                return False
            end = content.find("---", 3)
            if end == -1:
                return False
            fm = content[3:end]
            return "tags:" in fm or "tag:" in fm
    except:
        return False

def add_frontmatter(filepath: Path) -> bool:
    """Add frontmatter to a file that doesn't have it."""
    title = get_title_from_filename(filepath)
    dir_tag = get_dir_tag(filepath.parent)
    fm = f"""---
title: {title}
type: note
tags: [note, {dir_tag}]
---

"""
    try:
        with open(filepath, "r", encoding="utf-8", errors="replace") as f:
            content = f.read()
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(fm + content)
        return True
    except Exception as e:
        print(f"ERROR adding frontmatter to {filepath}: {e}")
        return False

def ensure_tags_in_frontmatter(filepath: Path) -> bool:
    """Ensure frontmatter has a tags field."""
    try:
        with open(filepath, "r", encoding="utf-8", errors="replace") as f:
            content = f.read()
        if not content.startswith("---"):
            return False
        end_idx = content.find("---", 3)
        if end_idx == -1:
            return False
        fm = content[3:end_idx]
        if "tags:" in fm or "tag:" in fm:
            return False  # Already has tags
        # Add tags before closing ---
        dir_tag = get_dir_tag(filepath.parent)
        new_fm = fm.rstrip() + f"\ntags: [note, {dir_tag}]\n"
        new_content = "---" + new_fm + "---" + content[end_idx + 3:]
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(new_content)
        return True
    except Exception as e:
        print(f"ERROR ensuring tags in {filepath}: {e}")
        return False

def get_moc_path(dirpath: Path) -> Path:
    """Get the expected MOC file path for a directory."""
    if dirpath == VAULT:
        return VAULT / f"{ROOT_MOC_NAME}.md"
    dir_name = dirpath.name
    # For numbered dirs, keep the number
    moc_name = f"{dir_name}{MOC_SUFFIX}.md"
    return dirpath / moc_name

def moc_exists(dirpath: Path) -> Optional[Path]:
    """Check if a MOC file exists for this directory. Return its path or None."""
    if dirpath == VAULT:
        root_moc = VAULT / f"{ROOT_MOC_NAME}.md"
        if root_moc.exists():
            return root_moc
        # Also check 00_ROOT_MOC
        alt = VAULT / "00_ROOT" / "00_ROOT_MOC.md"
        if alt.exists():
            return alt
        return None
    # Check for existing MOC patterns
    patterns = [
        f"*{MOC_SUFFIX}.md",
        "MOC*.md",
        "00_INDEX*.md",
        "INDEX*.md",
        "README.md",
    ]
    for pattern in patterns:
        matches = list(dirpath.glob(pattern))
        if matches:
            return matches[0]
    return None

def get_md_files(dirpath: Path) -> list[Path]:
    """Get all .md files directly in this directory (not subdirs)."""
    files = []
    try:
        for item in dirpath.iterdir():
            if item.is_file() and item.suffix == ".md":
                # Skip MOC files themselves
                if MOC_SUFFIX in item.name or item.name.startswith("MOC") or item.name == "README.md":
                    continue
                if item.name.startswith("00_INDEX") or item.name.startswith("INDEX"):
                    continue
                files.append(item)
    except PermissionError:
        pass
    return files

def get_subdirs_with_md(dirpath: Path) -> list[Path]:
    """Get subdirectories that contain .md files (recursively)."""
    subdirs = []
    try:
        for item in dirpath.iterdir():
            if item.is_dir() and not should_skip(item):
                # Check if this subdir or any descendant has .md files
                has_md = any(item.rglob("*.md"))
                if has_md:
                    subdirs.append(item)
    except PermissionError:
        pass
    return subdirs

def create_moc(dirpath: Path, parent_moc: Optional[Path]) -> Path:
    """Create a MOC file for a directory."""
    moc_path = get_moc_path(dirpath)
    if dirpath == VAULT:
        moc_path = VAULT / f"{ROOT_MOC_NAME}.md"
    
    dir_name = dirpath.name if dirpath != VAULT else "AMOS OS"
    title = f"{dir_name} MOC"
    dir_tag = get_dir_tag(dirpath)
    
    lines = []
    lines.append("---")
    lines.append(f"title: {title}")
    lines.append("type: moc")
    lines.append(f"tags: [moc, {dir_tag}]")
    lines.append("---")
    lines.append("")
    lines.append(f"# {dir_name} — Map of Content")
    lines.append("")
    
    # List files in this directory
    files = get_md_files(dirpath)
    if files:
        lines.append("## Files")
        lines.append("")
        for f in sorted(files):
            link = f.stem
            lines.append(f"- [[{link}]]")
        lines.append("")
    
    # List subdirectory MOCs
    subdirs = get_subdirs_with_md(dirpath)
    if subdirs:
        lines.append("## Subdirectories")
        lines.append("")
        for sd in sorted(subdirs):
            sd_moc = moc_exists(sd)
            if sd_moc:
                link = sd_moc.stem
                lines.append(f"- [[{link}]]")
        lines.append("")
    
    # Link to parent MOC
    if parent_moc:
        lines.append("---")
        lines.append(f"**Parent:** [[{parent_moc.stem}]]")
    lines.append("")
    
    content = "\n".join(lines)
    with open(moc_path, "w", encoding="utf-8") as f:
        f.write(content)
    
    return moc_path

def has_link_to_moc(filepath: Path, moc_path: Path) -> bool:
    """Check if a file already links to the MOC."""
    moc_link = f"[[{moc_path.stem}]]"
    try:
        with open(filepath, "r", encoding="utf-8", errors="replace") as f:
            content = f.read()
        return moc_link in content
    except:
        return False

def add_link_to_moc(filepath: Path, moc_path: Path) -> bool:
    """Add a link to the parent MOC at the bottom of the file."""
    moc_link = f"[[{moc_path.stem}]]"
    try:
        with open(filepath, "r", encoding="utf-8", errors="replace") as f:
            content = f.read()
        # Check if link already exists
        if moc_link in content:
            return False
        # Add at the end
        footer = f"\n\n---\n**MOC:** {moc_link}\n"
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content.rstrip() + footer)
        return True
    except Exception as e:
        print(f"ERROR adding link to {filepath}: {e}")
        return False

def collect_all_md_files() -> list[Path]:
    """Collect all .md files in the vault, excluding skip dirs."""
    files = []
    for root, dirs, filenames in os.walk(VAULT):
        root_path = Path(root)
        if should_skip(root_path):
            dirs.clear()
            continue
        # Filter dirs in-place
        dirs[:] = [d for d in dirs if d not in SKIP_DIRS]
        for fn in filenames:
            if fn.endswith(".md"):
                files.append(root_path / fn)
    return files

def collect_all_dirs_with_md() -> list[Path]:
    """Collect all directories that directly contain .md files."""
    dirs = set()
    for root, d, filenames in os.walk(VAULT):
        root_path = Path(root)
        if should_skip(root_path):
            d.clear()
            continue
        d[:] = [x for x in d if x not in SKIP_DIRS]
        if any(fn.endswith(".md") for fn in filenames):
            dirs.add(root_path)
    return sorted(dirs)

def main():
    print("=" * 60)
    print("AMOS Vault Normalizer")
    print("=" * 60)
    
    # Phase 1: Collect all .md files
    print("\n[1] Scanning vault...")
    all_files = collect_all_md_files()
    print(f"    Total .md files: {len(all_files)}")
    
    # Phase 2: Add frontmatter to files missing it
    print("\n[2] Adding frontmatter to files without it...")
    fm_added = 0
    for f in all_files:
        if not has_frontmatter(f):
            if add_frontmatter(f):
                fm_added += 1
    print(f"    Frontmatter added: {fm_added}")
    
    # Phase 3: Ensure tags in frontmatter
    print("\n[3] Ensuring tags in frontmatter...")
    tags_added = 0
    for f in all_files:
        if has_frontmatter(f) and not has_tags_in_frontmatter(f):
            if ensure_tags_in_frontmatter(f):
                tags_added += 1
    print(f"    Tags added: {tags_added}")
    
    # Phase 4: Create MOCs for all directories
    print("\n[4] Creating MOC files for directories...")
    mocs_created = 0
    mocs_existing = 0
    
    all_dirs = collect_all_dirs_with_md()
    print(f"    Directories with .md files: {len(all_dirs)}")
    
    # Build MOC hierarchy top-down
    # Sort by depth (shallowest first)
    all_dirs_sorted = sorted(all_dirs, key=lambda d: len(d.relative_to(VAULT).parts))
    
    moc_map = {}  # dirpath -> moc_path
    
    for dirpath in all_dirs_sorted:
        existing = moc_exists(dirpath)
        if existing:
            moc_map[dirpath] = existing
            mocs_existing += 1
        else:
            # Find parent MOC
            parent_dir = dirpath.parent
            parent_moc = moc_map.get(parent_dir)
            if parent_dir != VAULT and not parent_moc:
                # Try to find parent MOC
                parent_moc = moc_exists(parent_dir)
                if parent_moc:
                    moc_map[parent_dir] = parent_moc
            
            # Create MOC
            new_moc = create_moc(dirpath, parent_moc)
            moc_map[dirpath] = new_moc
            mocs_created += 1
    
    print(f"    MOCs already existing: {mocs_existing}")
    print(f"    MOCs created: {mocs_created}")
    print(f"    Total MOCs: {len(moc_map)}")
    
    # Phase 5: Link every file to its parent MOC
    print("\n[5] Linking files to parent MOCs...")
    links_added = 0
    for f in all_files:
        parent_dir = f.parent
        moc = moc_map.get(parent_dir)
        if moc and f != moc:  # Don't link MOC to itself
            if add_link_to_moc(f, moc):
                links_added += 1
    print(f"    Links to MOCs added: {links_added}")
    
    # Phase 6: Update all MOCs with complete file listings
    print("\n[6] Updating MOC file listings...")
    mocs_updated = 0
    for dirpath, moc_path in moc_map.items():
        if dirpath == VAULT:
            continue
        # Rebuild MOC content
        files = get_md_files(dirpath)
        subdirs = get_subdirs_with_md(dirpath)
        
        # Don't rebuild existing user-created MOCs, just append missing links
        try:
            with open(moc_path, "r", encoding="utf-8", errors="replace") as f:
                content = f.read()
        except:
            continue
        
        modified = False
        for f in sorted(files):
            link = f"[[{f.stem}]]"
            if link not in content:
                # Add to end
                if "## Files" not in content:
                    content += "\n## Files\n\n"
                content += f"- {link}\n"
                modified = True
        
        for sd in sorted(subdirs):
            sd_moc = moc_map.get(sd) or moc_exists(sd)
            if sd_moc:
                link = f"[[{sd_moc.stem}]]"
                if link not in content:
                    if "## Subdirectories" not in content:
                        content += "\n## Subdirectories\n\n"
                    content += f"- {link}\n"
                    modified = True
        
        if modified:
            try:
                with open(moc_path, "w", encoding="utf-8") as f:
                    f.write(content)
                mocs_updated += 1
            except Exception as e:
                print(f"    ERROR updating {moc_path}: {e}")
    print(f"    MOCs updated: {mocs_updated}")
    
    # Phase 7: Verify - check for orphans
    print("\n[7] Verification — checking for orphans...")
    # Re-scan all files
    all_files = collect_all_md_files()
    
    # Build link graph
    all_stems = {f.stem for f in all_files}
    incoming_links = defaultdict(int)
    outgoing_links = defaultdict(int)
    
    for f in all_files:
        try:
            with open(f, "r", encoding="utf-8", errors="replace") as fh:
                content = fh.read()
            # Find all wikilinks
            links = re.findall(r'\[\[([^\]|]+)', content)
            for link in links:
                link = link.strip()
                if link in all_stems:
                    incoming_links[link] += 1
                    outgoing_links[f.stem] += 1
        except:
            pass
    
    orphans = []
    for f in all_files:
        stem = f.stem
        if incoming_links[stem] == 0 and outgoing_links[stem] == 0:
            orphans.append(f)
    
    print(f"    Total files: {len(all_files)}")
    print(f"    Files with incoming links: {sum(1 for s in all_stems if incoming_links[s] > 0)}")
    print(f"    Files with outgoing links: {sum(1 for s in all_stems if outgoing_links[s] > 0)}")
    print(f"    Orphans (no links in or out): {len(orphans)}")
    if orphans:
        print("    First 20 orphans:")
        for o in orphans[:20]:
            print(f"      {o.relative_to(VAULT)}")
    
    # Phase 8: Fix remaining orphans by linking them to their MOC
    if orphans:
        print(f"\n[8] Fixing {len(orphans)} remaining orphans...")
        fixed = 0
        for f in orphans:
            parent_dir = f.parent
            moc = moc_map.get(parent_dir) or moc_exists(parent_dir)
            if moc and f != moc:
                if add_link_to_moc(f, moc):
                    fixed += 1
                    # Also add link from MOC to this file
                    try:
                        with open(moc, "r", encoding="utf-8", errors="replace") as fh:
                            moc_content = fh.read()
                        link = f"[[{f.stem}]]"
                        if link not in moc_content:
                            moc_content += f"- {link}\n"
                            with open(moc, "w", encoding="utf-8") as fh:
                                fh.write(moc_content)
                    except:
                        pass
        print(f"    Orphans fixed: {fixed}")
    
    print("\n" + "=" * 60)
    print("Normalization complete!")
    print("=" * 60)

if __name__ == "__main__":
    main()
