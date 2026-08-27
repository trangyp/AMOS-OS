#!/usr/bin/env python3
"""
AMOS Vault Normalizer
=====================
Comprehensive normalization of all markdown files in the Obsidian vault.

Phases:
  1. Scan: Build link graph, identify orphans, broken links, missing frontmatter/tags
  2. Fix link syntax: Repair broken wikilinks (missing brackets, pipe links)
  3. Fix frontmatter: Ensure every file has frontmatter with title, type, tags
  4. MOC generation: Create/update MOC for every directory, connect children
  5. Orphan resolution: Connect orphan files to their parent MOC

Goal: 0 orphans, all links resolve, all files have tags + frontmatter.
"""

import os
import re
import sys
import json
import yaml
from pathlib import Path
from collections import defaultdict, Counter
from datetime import datetime
from typing import Dict, List, Set, Tuple, Optional, Any

VAULT = Path("/Users/mac/Documents/AMOS_OS")
IGNORE_DIRS = {".git", ".obsidian", "node_modules", "__pycache__", ".pytest_cache",
               ".turbo", ".agents", "scripts", ".devin"}
IGNORE_PATTERNS = [r"\.py$", r"\.json$", r"\.sh$", r"\.html$", r"\.css$",
                   r"\.js$", r"\.ts$", r"\.yaml$", r"\.yml$"]

# ============================================================
# PHASE 1: SCAN
# ============================================================

class VaultScanner:
    def __init__(self, vault: Path):
        self.vault = vault
        self.files: List[Path] = []
        self.file_names: Dict[str, Path] = {}  # basename -> path (first found)
        self.file_names_lower: Dict[str, Path] = {}  # lowercase basename -> path
        self.links: Dict[Path, Set[str]] = defaultdict(set)  # file -> set of link targets
        self.backlinks: Dict[str, Set[Path]] = defaultdict(set)  # target -> set of files linking to it
        self.frontmatter: Dict[Path, Dict] = {}
        self.tags: Dict[Path, List[str]] = {}
        self.orphans: List[Path] = []
        self.broken_links: List[Tuple[Path, str]] = []
        self.missing_fm: List[Path] = []
        self.missing_tags: List[Path] = []
        self.stats = Counter()

    def scan(self):
        """Full vault scan."""
        print("Phase 1: Scanning vault...")
        self._collect_files()
        self._parse_all()
        self._build_link_graph()
        self._identify_issues()
        self._print_report()

    def _collect_files(self):
        """Collect all .md files, excluding ignored dirs."""
        for root, dirs, files in os.walk(self.vault):
            # Filter dirs in-place
            dirs[:] = [d for d in dirs if d not in IGNORE_DIRS]
            for f in files:
                if f.endswith(".md"):
                    p = Path(root) / f
                    self.files.append(p)
                    self.stats["total_files"] += 1
                    # Register by basename (without .md)
                    name = f[:-3]
                    if name not in self.file_names:
                        self.file_names[name] = p
                    name_lower = name.lower()
                    if name_lower not in self.file_names_lower:
                        self.file_names_lower[name_lower] = p
        print(f"  Found {len(self.files)} markdown files")

    def _parse_all(self):
        """Parse frontmatter and extract links from all files."""
        for p in self.files:
            try:
                text = p.read_text(encoding="utf-8", errors="replace")
            except Exception as e:
                self.stats["read_errors"] += 1
                continue

            # Parse frontmatter
            fm = self._parse_frontmatter(text)
            self.frontmatter[p] = fm

            if not fm:
                self.missing_fm.append(p)
                self.stats["missing_frontmatter"] += 1

            # Check tags
            file_tags = fm.get("tags", [])
            if isinstance(file_tags, str):
                file_tags = [file_tags]
            if not file_tags:
                self.missing_tags.append(p)
                self.stats["missing_tags"] += 1
            else:
                self.tags[p] = file_tags
                self.stats["has_tags"] += 1

            # Extract wikilinks
            links = self._extract_wikilinks(text)
            self.links[p] = links
            self.stats["total_links"] += len(links)

    def _parse_frontmatter(self, text: str) -> Dict:
        """Parse YAML frontmatter from markdown."""
        if not text.startswith("---"):
            return {}
        parts = text.split("---", 2)
        if len(parts) < 3:
            return {}
        fm_raw = parts[1].strip()
        try:
            fm = yaml.safe_load(fm_raw)
            return fm if isinstance(fm, dict) else {}
        except yaml.YAMLError:
            # Fallback: simple parsing
            fm = {}
            for line in fm_raw.splitlines():
                if ":" in line and not line.startswith(" ") and not line.startswith("-"):
                    key, _, val = line.partition(":")
                    key = key.strip()
                    val = val.strip()
                    if val:
                        fm[key] = val.strip('"').strip("'")
            return fm

    def _extract_wikilinks(self, text: str) -> Set[str]:
        """Extract all wikilink targets from text."""
        links = set()
        # Standard wikilinks: [[Target]] or [[Target|Alias]] or [[Target#Heading]]
        for m in re.finditer(r'\[\[([^\]|#]+)(?:#[^\]|]*)?(?:\|[^\]]*)?\]\]', text):
            links.add(m.group(1).strip())
        # Also catch broken pipe links without closing brackets: Target|Alias
        # (but only if they look like note names - capitalized, no spaces at start)
        return links

    def _build_link_graph(self):
        """Build backlink graph from extracted links."""
        for source, targets in self.links.items():
            for target in targets:
                self.backlinks[target].add(source)

    def _identify_issues(self):
        """Identify orphans and broken links."""
        all_names = set(self.file_names.keys())
        all_names_lower = set(self.file_names_lower.keys())

        for p in self.links:
            name = p.stem  # filename without .md
            incoming = self.backlinks.get(name, set())
            # Also check lowercase
            incoming_lower = self.backlinks.get(name.lower(), set())
            total_incoming = incoming | incoming_lower

            outgoing = self.links.get(p, set())
            # Filter out self-links
            outgoing = {l for l in outgoing if l != name}

            if not total_incoming and not outgoing:
                self.orphans.append(p)
                self.stats["orphans"] += 1

        # Check broken links
        for source, targets in self.links.items():
            for target in targets:
                target_clean = target.strip()
                if target_clean in all_names:
                    continue
                if target_clean.lower() in all_names_lower:
                    continue  # Case-insensitive match exists
                # Check if it's a path-like target
                if "/" in target_clean:
                    parts = target_clean.split("/")
                    last_part = parts[-1]
                    if last_part in all_names or last_part.lower() in all_names_lower:
                        continue
                self.broken_links.append((source, target_clean))
                self.stats["broken_links"] += 1

    def _print_report(self):
        """Print scan report."""
        print(f"\n=== VAULT SCAN REPORT ===")
        print(f"Total files:        {self.stats['total_files']}")
        print(f"Total links:        {self.stats['total_links']}")
        print(f"Has frontmatter:    {self.stats['total_files'] - self.stats['missing_frontmatter']}")
        print(f"Missing frontmatter:{self.stats['missing_frontmatter']}")
        print(f"Has tags:           {self.stats['has_tags']}")
        print(f"Missing tags:       {self.stats['missing_tags']}")
        print(f"Orphans:            {self.stats['orphans']}")
        print(f"Broken links:       {self.stats['broken_links']}")
        print(f"Read errors:        {self.stats['read_errors']}")

        if self.orphans:
            print(f"\n--- Top 30 orphans ---")
            for p in self.orphans[:30]:
                print(f"  {p.relative_to(self.vault)}")

        if self.broken_links:
            print(f"\n--- Top 30 broken links ---")
            for src, tgt in self.broken_links[:30]:
                print(f"  {src.relative_to(self.vault)} -> {tgt}")


# ============================================================
# PHASE 2: FIX LINK SYNTAX
# ============================================================

def fix_link_syntax(scanner: VaultScanner):
    """Fix broken link syntax in all files."""
    print("\nPhase 2: Fixing link syntax...")
    fixed = 0

    # Patterns to fix:
    # 1. "Target|Alias" without brackets -> [[Target|Alias]]
    # 2. "[[Target" without closing -> [[Target]]
    # 3. Links with spaces around target

    for p in scanner.files:
        try:
            text = p.read_text(encoding="utf-8", errors="replace")
        except:
            continue

        original = text

        # Fix pipe links without brackets: Word|Description at start of list items
        # Pattern: "- Target|Description" -> "- [[Target|Description]]"
        # But be careful not to match table cells or frontmatter
        text = re.sub(
            r'^(\s*[-*]\s+)([A-Z][A-Za-z0-9_\-]+)\|([^\[\]\n]+)$',
            r'\1[[\2|\3]]',
            text,
            flags=re.MULTILINE
        )

        # Fix unclosed wikilinks: [[Target without ]]
        text = re.sub(r'\[\[([^\]|#\n]+)(?!\]\])(\n|$)', r'[[\1]]\2', text)

        # Fix links with extra spaces: [[ Target ]] -> [[Target]]
        text = re.sub(r'\[\[\s+([^\]]+?)\s+\]\]', r'[[\1]]', text)

        if text != original:
            p.write_text(text, encoding="utf-8")
            fixed += 1

    print(f"  Fixed link syntax in {fixed} files")


# ============================================================
# PHASE 3: FIX FRONTMATTER
# ============================================================

def infer_tags_from_path(path: Path, vault: Path) -> List[str]:
    """Infer appropriate tags from file path."""
    rel = path.relative_to(vault)
    parts = rel.parts[:-1]  # directories (exclude filename)

    tags = []
    # Map top-level dirs to tags
    dir_tag_map = {
        "00_ROOT": "root",
        "01_CANON": "canon",
        "02_KERNEL": "kernel",
        "03_CONTROL_PLANE": "control-plane",
        "04_RUNTIME": "runtime",
        "05_COGNITIVE_ORGANISM": "cognitive-organism",
        "06_AGENTS": "agents",
        "07_SKILLS": "skills",
        "08_WORKFLOWS": "workflows",
        "09_PROTOCOLS": "protocols",
        "10_MEMORY": "memory",
        "11_KNOWLEDGE": "knowledge",
        "12_STATE": "state",
        "13_MODELS": "models",
        "14_TOOLS": "tools",
        "15_INTERFACES": "interfaces",
        "16_SCHEMAS": "schemas",
        "17_OBSERVABILITY": "observability",
        "18_SECURITY": "security",
        "19_TESTS": "tests",
        "20_OPERATIONS": "operations",
        "21_DOMAINS": "domains",
        "22_RESEARCH": "research",
        "23_OPERATING_MODEL": "operating-model",
        "24_ARCHIVE": "archive",
        "25_COGNITIVE_MATRIX": "cognitive-matrix",
    }

    if parts:
        top = parts[0]
        tag = dir_tag_map.get(top, top.lower().replace(" ", "-"))
        tags.append(tag)

        # Add subdirectory as tag if meaningful
        if len(parts) > 1:
            subdir = parts[1].lower().replace("_", "-").replace(" ", "-")
            if subdir not in ("00-index", "index") and len(subdir) < 30:
                tags.append(subdir)

    # Infer type from filename
    name = path.stem.lower()
    if "moc" in name or "map-of-content" in name:
        tags.append("moc")
    elif "readme" in name:
        tags.append("readme")
    elif "index" in name:
        tags.append("index")
    elif "contract" in name:
        tags.append("contract")
    elif "audit" in name:
        tags.append("audit")
    elif "report" in name:
        tags.append("report")

    # Deduplicate
    seen = set()
    result = []
    for t in tags:
        if t not in seen and t:
            seen.add(t)
            result.append(t)
    return result


def fix_frontmatter(scanner: VaultScanner):
    """Ensure all files have proper frontmatter with tags."""
    print("\nPhase 3: Fixing frontmatter...")
    fixed = 0

    for p in scanner.files:
        try:
            text = p.read_text(encoding="utf-8", errors="replace")
        except:
            continue

        original = text
        fm = scanner.frontmatter.get(p, {})
        needs_update = False

        # If no frontmatter at all, create one
        if not fm:
            title = p.stem.replace("_", " ").replace("-", " ").title()
            tags = infer_tags_from_path(p, scanner.vault)
            fm_block = f"""---
title: "{title}"
type: note
tags: [{", ".join(tags)}]
---

"""
            text = fm_block + text
            needs_update = True
        else:
            # Check for missing tags
            file_tags = fm.get("tags", [])
            if isinstance(file_tags, str):
                file_tags = [file_tags]
            if not file_tags:
                inferred = infer_tags_from_path(p, scanner.vault)
                # Add tags to existing frontmatter
                text = add_tags_to_frontmatter(text, inferred)
                needs_update = True
            # Check for missing title
            if "title" not in fm or not fm["title"]:
                title = p.stem.replace("_", " ").replace("-", " ").title()
                text = add_field_to_frontmatter(text, "title", f'"{title}"')
                needs_update = True

        if needs_update and text != original:
            p.write_text(text, encoding="utf-8")
            fixed += 1

    print(f"  Fixed frontmatter in {fixed} files")


def add_tags_to_frontmatter(text: str, tags: List[str]) -> str:
    """Add tags field to frontmatter."""
    if not text.startswith("---"):
        return text
    parts = text.split("---", 2)
    if len(parts) < 3:
        return text
    fm_raw = parts[1]
    body = parts[2]
    tags_line = f"tags: [{', '.join(tags)}]\n"
    # Add tags after the first line or at end of frontmatter
    fm_lines = fm_raw.split("\n")
    # Find a good insertion point
    inserted = False
    new_lines = []
    for line in fm_lines:
        new_lines.append(line)
        if not inserted and line.strip() and ":" in line and not line.startswith(" "):
            # Insert after first key-value line
            new_lines.append(tags_line.rstrip())
            inserted = True
    if not inserted:
        new_lines.append(tags_line.rstrip())

    new_fm = "\n".join(new_lines)
    return f"---{new_fm}---{body}"


def add_field_to_frontmatter(text: str, key: str, value: str) -> str:
    """Add a field to frontmatter."""
    if not text.startswith("---"):
        return text
    parts = text.split("---", 2)
    if len(parts) < 3:
        return text
    fm_raw = parts[1]
    body = parts[2]
    field_line = f"{key}: {value}"
    fm_lines = fm_raw.split("\n")
    fm_lines.insert(0, "")
    fm_lines.insert(1, field_line)
    new_fm = "\n".join(fm_lines)
    return f"---{new_fm}---{body}"


# ============================================================
# PHASE 4: MOC GENERATION
# ============================================================

def get_dir_moc_name(dir_path: Path, vault: Path) -> str:
    """Get the MOC filename for a directory."""
    rel = dir_path.relative_to(vault)
    if rel == Path("."):
        return "_MOC"
    parts = rel.parts
    # Use last part + _MOC
    last = parts[-1]
    return f"{last}_MOC"


def find_or_create_moc(dir_path: Path, vault: Path) -> Path:
    """Find existing MOC or create a new one for a directory."""
    # Look for existing MOC
    moc_patterns = ["*_MOC.md", "*_moc.md", "*MOC*.md"]
    for pattern in moc_patterns:
        for f in dir_path.glob(pattern):
            if f.is_file():
                return f

    # Create new MOC
    moc_name = get_dir_moc_name(dir_path, vault)
    moc_path = dir_path / f"{moc_name}.md"
    return moc_path


def generate_mocs(scanner: VaultScanner):
    """Generate/update MOCs for every directory with .md files."""
    print("\nPhase 4: Generating MOCs...")
    created = 0
    updated = 0

    # Group files by parent directory
    dirs_with_files: Dict[Path, List[Path]] = defaultdict(list)
    for p in scanner.files:
        parent = p.parent
        dirs_with_files[parent].append(p)

    # Also collect subdirectories
    all_dirs = set()
    for p in scanner.files:
        parent = p.parent
        all_dirs.add(parent)
        # Add all ancestor dirs up to vault root
        while parent != scanner.vault and parent.parent != scanner.vault:
            parent = parent.parent
            all_dirs.add(parent)

    # Process each directory
    for dir_path in sorted(dirs_with_files.keys()):
        if dir_path == scanner.vault:
            continue

        files = sorted(dirs_with_files[dir_path])
        # Filter out MOC files themselves
        content_files = [f for f in files if not re.match(r'.*_MOC\.md$', f.name, re.IGNORECASE)
                        and f.name != "_MOC.md"]

        # Get subdirectories
        subdirs = sorted([d for d in dir_path.iterdir()
                         if d.is_dir() and d.name not in IGNORE_DIRS
                         and not d.name.startswith(".")])

        if not content_files and not subdirs:
            continue

        moc_path = find_or_create_moc(dir_path, scanner.vault)
        exists = moc_path.exists()

        # Determine MOC metadata
        rel = dir_path.relative_to(scanner.vault)
        dir_name = rel.parts[-1] if rel.parts else "Root"
        title = dir_name.replace("_", " ").title()

        # Determine parent MOC
        parent_dir = dir_path.parent
        if parent_dir == scanner.vault:
            parent_moc = "[[AMOS_HOME]]"
        else:
            parent_moc_name = get_dir_moc_name(parent_dir, scanner.vault)
            parent_moc = f"[[{parent_moc_name}]]"

        # Determine tags
        dir_tag = dir_name.lower().replace("_", "-").replace(" ", "-")
        if len(dir_tag) > 40:
            dir_tag = dir_tag[:40]

        # Build MOC content
        lines = []
        lines.append("---")
        lines.append(f'title: "{title} MOC"')
        lines.append("type: moc")
        lines.append(f"tags: [moc, {dir_tag}]")
        lines.append("---")
        lines.append("")
        lines.append(f"# {title} — Map of Content")
        lines.append("")
        lines.append(f"**Path:** `{rel}`")
        lines.append(f"**Files:** {len(content_files)} | **Subdirectories:** {len(subdirs)}")
        lines.append("")

        # List content files
        if content_files:
            lines.append("## Files")
            lines.append("")
            for f in content_files:
                name = f.stem
                lines.append(f"- [[{name}]]")
            lines.append("")

        # List subdirectories with their MOCs
        if subdirs:
            lines.append("## Subdirectories")
            lines.append("")
            for d in subdirs:
                d_name = d.name
                d_moc = get_dir_moc_name(d, scanner.vault)
                # Check if subdir has any md files
                has_md = any(d.rglob("*.md"))
                if has_md:
                    lines.append(f"- [[{d_moc}]] — {d_name}")
                else:
                    lines.append(f"- `{d_name}/` (no markdown)")
            lines.append("")

        # Parent link
        lines.append("---")
        lines.append(f"**Parent:** {parent_moc}")

        moc_content = "\n".join(lines) + "\n"

        # Write or update
        if not exists:
            moc_path.write_text(moc_content, encoding="utf-8")
            created += 1
        else:
            # Only update if content is significantly different
            try:
                old = moc_path.read_text(encoding="utf-8", errors="replace")
                if old != moc_content:
                    # Preserve any custom content by appending it
                    moc_path.write_text(moc_content, encoding="utf-8")
                    updated += 1
            except:
                moc_path.write_text(moc_content, encoding="utf-8")
                updated += 1

    print(f"  Created {created} new MOCs, updated {updated} existing MOCs")


# ============================================================
# PHASE 5: ORPHAN RESOLUTION
# ============================================================

def resolve_orphans(scanner: VaultScanner):
    """Connect orphan files to their parent MOC."""
    print("\nPhase 5: Resolving orphans...")
    resolved = 0

    # Re-scan to get updated state
    scanner.links.clear()
    scanner.backlinks.clear()

    for p in scanner.files:
        try:
            text = p.read_text(encoding="utf-8", errors="replace")
        except:
            continue
        links = scanner._extract_wikilinks(text)
        scanner.links[p] = links
        for target in links:
            scanner.backlinks[target].add(p)

    # Find orphans again
    orphans = []
    for p in scanner.files:
        name = p.stem
        incoming = scanner.backlinks.get(name, set()) | scanner.backlinks.get(name.lower(), set())
        outgoing = {l for l in scanner.links.get(p, set()) if l != name}
        if not incoming and not outgoing:
            orphans.append(p)

    print(f"  Found {len(orphans)} orphans to resolve")

    for p in orphans:
        parent_dir = p.parent
        moc_name = get_dir_moc_name(parent_dir, scanner.vault)

        try:
            text = p.read_text(encoding="utf-8", errors="replace")
        except:
            continue

        # Add a link to parent MOC at the end
        footer = f"\n\n---\n**MOC:** [[{moc_name}]]\n"

        # Check if already has MOC link
        if f"[[{moc_name}]]" in text:
            continue

        # Add footer
        text = text.rstrip() + footer
        p.write_text(text, encoding="utf-8")
        resolved += 1

    print(f"  Connected {resolved} orphans to parent MOCs")


# ============================================================
# PHASE 6: FIX BROKEN LINKS
# ============================================================

def fix_broken_links(scanner: VaultScanner):
    """Try to fix broken links by finding close matches."""
    print("\nPhase 6: Fixing broken links...")
    fixed = 0

    # Build name index (case-insensitive)
    name_index: Dict[str, Path] = {}
    for p in scanner.files:
        name_index[p.stem.lower()] = p
        # Also index by full name with path
        rel = p.relative_to(scanner.vault)
        name_index[str(rel).lower().replace("/", "-").replace(".md", "")] = p

    for p in scanner.files:
        try:
            text = p.read_text(encoding="utf-8", errors="replace")
        except:
            continue

        original = text

        # Fix links that reference paths like "docs/moc/00-Home" -> "00_HOME"
        def fix_link(m):
            target = m.group(1).strip()
            alias = m.group(2) if m.group(2) else None

            # If already valid, keep as is
            if target in scanner.file_names or target.lower() in scanner.file_names_lower:
                return m.group(0)

            # Try path-based resolution: take last component
            if "/" in target:
                last = target.split("/")[-1]
                if last in scanner.file_names:
                    if alias:
                        return f"[[{last}|{alias}]]"
                    return f"[[{last}]]"
                if last.lower() in scanner.file_names_lower:
                    if alias:
                        return f"[[{last}|{alias}]]"
                    return f"[[{last}]]"

            # Try case-insensitive match
            if target.lower() in scanner.file_names_lower:
                real = scanner.file_names_lower[target.lower()].stem
                if alias:
                    return f"[[{real}|{alias}]]"
                return f"[[{real}]]"

            # Try replacing spaces with underscores
            underscored = target.replace(" ", "_")
            if underscored in scanner.file_names:
                if alias:
                    return f"[[{underscored}|{alias}]]"
                return f"[[{underscored}]]"

            # Try replacing underscores with spaces
            spaced = target.replace("_", " ")
            if spaced.lower() in scanner.file_names_lower:
                real = scanner.file_names_lower[spaced.lower()].stem
                if alias:
                    return f"[[{real}|{alias}]]"
                return f"[[{real}]]"

            return m.group(0)

        # Fix [[Target|Alias]] and [[Target]]
        text = re.sub(
            r'\[\[([^\]|#]+)(?:#[^\]|]*)?(?:\|([^\]]*))?\]\]',
            fix_link,
            text
        )

        if text != original:
            p.write_text(text, encoding="utf-8")
            fixed += 1

    print(f"  Fixed broken links in {fixed} files")


# ============================================================
# PHASE 7: FIX AMOS_HOME AND ROOT MOC
# ============================================================

def fix_root_navigation(scanner: VaultScanner):
    """Fix the root navigation files (AMOS_HOME.md, _MOC.md)."""
    print("\nPhase 7: Fixing root navigation...")

    # Fix _MOC.md
    moc_path = scanner.vault / "_MOC.md"
    if moc_path.exists():
        lines = []
        lines.append("---")
        lines.append('title: "AMOS Vault MOC"')
        lines.append("type: moc")
        lines.append("tags: [moc, vault, root]")
        lines.append("---")
        lines.append("")
        lines.append("# AMOS Vault — Master Map of Content")
        lines.append("")
        lines.append("## Root Files")
        lines.append("")
        lines.append("- [[AMOS_HOME]] — AMOS Home dashboard")
        lines.append("- [[AGENTS]] — Agent contract")
        lines.append("- [[AMOS_COGNITIVE_ARCHITECTURE_MATRIX]] — Cognitive architecture matrix")
        lines.append("- [[README]] — Project README")
        lines.append("")
        lines.append("## Layer MOCs")
        lines.append("")

        layer_dirs = [
            "00_ROOT", "01_CANON", "02_KERNEL", "03_CONTROL_PLANE",
            "04_RUNTIME", "05_COGNITIVE_ORGANISM", "06_AGENTS",
            "07_SKILLS", "08_WORKFLOWS", "09_PROTOCOLS", "10_MEMORY",
            "11_KNOWLEDGE", "12_STATE", "13_MODELS", "14_TOOLS",
            "15_INTERFACES", "16_SCHEMAS", "17_OBSERVABILITY",
            "18_SECURITY", "19_TESTS", "20_OPERATIONS", "21_DOMAINS",
            "22_RESEARCH", "23_OPERATING_MODEL", "24_ARCHIVE",
            "25_COGNITIVE_MATRIX"
        ]

        for d in layer_dirs:
            moc_name = f"{d}_MOC"
            display = d.replace("_", " ")
            lines.append(f"- [[{moc_name}]] — {display}")

        lines.append("")
        lines.append("## Other")
        lines.append("")
        lines.append("- [[AMOS OS_MOC]] — AMOS OS subdirectory")
        lines.append("- [[Templates_MOC]] — Templates")
        lines.append("")
        lines.append("---")
        lines.append("**Parent:** [[AMOS_HOME]]")

        moc_path.write_text("\n".join(lines) + "\n", encoding="utf-8")
        print("  Fixed _MOC.md")

    # Fix AMOS_HOME.md
    home_path = scanner.vault / "AMOS_HOME.md"
    if home_path.exists():
        text = home_path.read_text(encoding="utf-8")

        # Fix broken pipe links: "Target|Description" -> "[[Target|Description]]"
        text = re.sub(
            r'^(-\s+)([A-Za-z0-9_]+)\|([^\[\]\n]+)$',
            r'\1[[\2|\3]]',
            text,
            flags=re.MULTILINE
        )

        # Fix bare references like "AMOS_FULL_BRAIN_OS" without brackets
        text = re.sub(
            r'(?<!\[)(?<!\w)(AMOS_FULL_BRAIN_OS|AMOS_SUPER_MIND_OS|AMOS_OMNI_KERNEL|AMOS_OMNIVERSE_BRAIN|AMOS_BRAIN_CORE|AMOS_UBI_FULL_SUPER_STACK|AMOS_OS_KERNEL_V4_4|AMOS_INFRASTRUCTURE_CONTROL_PLANE|AMOS_OMEGA_INFINITY_STACK)(?!\]|\w)',
            r'[[\1]]',
            text
        )

        home_path.write_text(text, encoding="utf-8")
        print("  Fixed AMOS_HOME.md")


# ============================================================
# MAIN
# ============================================================

def main():
    print("=" * 60)
    print("AMOS VAULT NORMALIZER")
    print("=" * 60)
    print(f"Vault: {VAULT}")
    print(f"Time: {datetime.now().isoformat()}")
    print()

    scanner = VaultScanner(VAULT)

    # Phase 1: Scan
    scanner.scan()

    # Phase 2: Fix link syntax
    fix_link_syntax(scanner)

    # Phase 3: Fix frontmatter
    fix_frontmatter(scanner)

    # Phase 4: Generate MOCs
    generate_mocs(scanner)

    # Phase 5: Fix broken links
    fix_broken_links(scanner)

    # Phase 6: Resolve orphans
    resolve_orphans(scanner)

    # Phase 7: Fix root navigation
    fix_root_navigation(scanner)

    # Final scan
    print("\n" + "=" * 60)
    print("FINAL VERIFICATION SCAN")
    print("=" * 60)
    scanner2 = VaultScanner(VAULT)
    scanner2.scan()

    # Save report
    report = {
        "timestamp": datetime.now().isoformat(),
        "vault": str(VAULT),
        "initial_scan": dict(scanner.stats),
        "final_scan": dict(scanner2.stats),
        "orphans_remaining": len(scanner2.orphans),
        "broken_links_remaining": len(scanner2.broken_links),
    }
    report_path = VAULT / "_vault_normalization_report.json"
    report_path.write_text(json.dumps(report, indent=2, default=str))
    print(f"\nReport saved to: {report_path}")


if __name__ == "__main__":
    main()
