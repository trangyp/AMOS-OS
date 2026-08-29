#!/usr/bin/env python3
"""Scan for remaining broken wikilinks and structural issues in the vault.

Distinguishes:
- Real vault-note wikilinks (in 00_ROOT, 01_CANON, 02_KERNEL, ..., 11_KNOWLEDGE, etc.)
- AMOS-internal skill references (in .devin/) which use conventions like
  [[skill-name-agent]] (JSON agent file) and [[references/sota.md]] (relative path).
"""
import os
import re
from pathlib import Path

VAULT = Path("/Users/mac/Documents/AMOS_OS")

# Collect all files (md + json) for lookup
all_md_files = {}      # stem -> [paths]
all_json_files = {}    # stem -> [paths]
rel_md_paths = {}      # relpath.lower() -> path
rel_json_paths = {}    # relpath.lower() -> path
all_files_any = {}     # stem -> [paths] for any file type

for root, dirs, files in os.walk(VAULT, followlinks=True):
    for fn in files:
        p = Path(root) / fn
        try:
            rel = p.relative_to(VAULT)
        except ValueError:
            continue
        stem = p.stem
        all_files_any.setdefault(stem.lower(), []).append(p)
        if fn.endswith(".md"):
            all_md_files.setdefault(stem.lower(), []).append(p)
            rel_md_paths[str(rel).lower()] = p
        elif fn.endswith(".json"):
            all_json_files.setdefault(stem.lower(), []).append(p)
            rel_json_paths[str(rel).lower()] = p

WIKILINK_RE = re.compile(r'\[\[([^"\|\[\]\{\}#]+?)(?:#[^\]|]*)?(?:\|[^\]]*)?\]\]')

# Vault-note directories (exclude .devin, .git, .agents, .claude, node_modules, _*)
VAULT_NOTE_PREFIXES = (
    "00_ROOT", "01_CANON", "02_KERNEL", "03_CONTROL_PLANE", "04_RUNTIME",
    "05_FRAMEWORKS", "06_DOMAIN_KNOWLEDGE", "07_SKILLS", "08_AGENTS",
    "09_TOOLS", "10_ROUTING", "11_KNOWLEDGE", "12_GENERATORS",
    "21_DOMAINS", "25_COGNITIVE_MATRIX", "99_ARCHIVE",
)

def is_vault_note(rel_path: str) -> bool:
    """True if this file is a real vault note (not a .devin skill internal)."""
    parts = rel_path.replace("\\", "/").split("/")
    if parts and parts[0].startswith("_"):
        return False
    if parts and parts[0] in (".devin", ".git", ".agents", ".claude", ".obsidian", "node_modules"):
        return False
    return True

def resolve_wikilink(target: str, source_path: Path) -> bool:
    """Try to resolve a wikilink target. Returns True if resolvable."""
    if not target or target.startswith("http"):
        return True  # external or empty
    key = target.lower().replace(" ", "_")
    key_plain = target.lower()

    # 1. Basename lookup (any file type — covers -agent JSON files)
    if key in all_files_any or key_plain in all_files_any:
        return True

    # 2. MD basename
    if key in all_md_files or key_plain in all_md_files:
        return True

    # 3. JSON basename (for [[skill-name-agent]] -> skill-name-agent.json)
    if key in all_json_files or key_plain in all_json_files:
        return True

    # 4. Full relpath lookup (with and without .md)
    for d in (rel_md_paths, rel_json_paths):
        for k in (key_plain, key_plain + ".md", key, key + ".md"):
            if k in d:
                return True

    # 5. Relative path resolution (for [[references/sota.md]] inside skill dirs)
    if "/" in target:
        try:
            resolved = (source_path.parent / target).resolve()
            if resolved.exists():
                return True
            # try with .md
            resolved2 = (source_path.parent / (target + ".md")).resolve()
            if resolved2.exists():
                return True
        except Exception:
            pass

    # 6. Path with spaces->underscores
    key2 = target.lower().replace(" ", "_")
    for d in (rel_md_paths, rel_json_paths):
        for k in (key2, key2 + ".md"):
            if k in d:
                return True

    return False

# Scan
broken_vault = {}     # broken wikilinks in vault notes (real issues)
broken_devin = {}      # broken wikilinks in .devin skill files (may be convention)
scanned_vault = 0
scanned_devin = 0

for root, dirs, files in os.walk(VAULT, followlinks=True):
    if "node_modules" in root:
        continue
    for fn in files:
        if not fn.endswith(".md"):
            continue
        p = Path(root) / fn
        try:
            rel = str(p.relative_to(VAULT))
        except ValueError:
            continue
        parts = rel.replace("\\", "/").split("/")
        if any(part.startswith(".") and part not in (".devin",) for part in parts):
            continue
        if "node_modules" in parts:
            continue

        is_devin = parts[0] == ".devin" if parts else False
        if is_devin:
            scanned_devin += 1
        else:
            scanned_vault += 1

        try:
            text = p.read_text(encoding="utf-8", errors="replace")
        except Exception:
            continue

        in_code = False
        for raw_line in text.splitlines():
            if raw_line.strip().startswith("```"):
                in_code = not in_code
                continue
            if in_code:
                continue
            # Strip inline code spans so `[[...]]` literal mentions are not treated as links
            line = re.sub(r'`[^`]*`', lambda m: ' ' * len(m.group(0)), raw_line)
            for m in WIKILINK_RE.finditer(line):
                target = m.group(1).strip()
                if not target or target.startswith("http"):
                    continue
                # Skip obviously non-wikilink strings (JSON-injected artifacts, etc.)
                if len(target) > 80 or target.startswith('"'):
                    continue
                if resolve_wikilink(target, p):
                    continue
                bucket = broken_devin if is_devin else broken_vault
                bucket.setdefault(target, []).append(rel)

print(f"=== VAULT NOTES (real wikilinks) ===")
print(f"Scanned {scanned_vault} .md files")
print(f"Found {len(broken_vault)} unique broken wikilink targets\n")
for target in sorted(broken_vault):
    refs = broken_vault[target]
    print(f"  [[{target}]] — {len(refs)} ref(s)")
    for r in refs[:3]:
        print(f"    in {r}")
    if len(refs) > 3:
        print(f"    ... and {len(refs)-3} more")

print(f"\n=== .DEVIN SKILL FILES (AMOS-internal conventions) ===")
print(f"Scanned {scanned_devin} .md files")
print(f"Found {len(broken_devin)} unique unresolved targets (may be convention, not bugs)\n")
# Only show top 20 by ref count
sorted_devin = sorted(broken_devin.items(), key=lambda x: -len(x[1]))
for target, refs in sorted_devin[:20]:
    print(f"  [[{target}]] — {len(refs)} ref(s)")
    for r in refs[:2]:
        print(f"    in {r}")
    if len(refs) > 2:
        print(f"    ... and {len(refs)-2} more")
if len(sorted_devin) > 20:
    print(f"  ... and {len(sorted_devin)-20} more unresolved targets")
