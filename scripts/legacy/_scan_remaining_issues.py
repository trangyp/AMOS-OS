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

VAULT = Path(__file__).resolve().parents[2]

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

# Resolve .devin wikilinks against the real AMOS source package
# .devin/ itself is a regular directory; skills/agents/workflows are symlinks to the repo.
REPO_ROOT = None
repo_stems = {}
repo_rel_md_paths = {}
repo_rel_json_paths = {}
_devin_link = VAULT / ".devin"
_skills_link = _devin_link / "skills"
try:
    if _skills_link.is_symlink():
        _skills_real = _skills_link.resolve()
        _repo_dotdevin = _skills_real.parent
        REPO_ROOT = _repo_dotdevin.parent
        if REPO_ROOT.is_dir():
            for _scan_root in (REPO_ROOT / "docs", REPO_ROOT / "_00_Cosmo brain", REPO_ROOT / "cosmo-brain"):
                if not _scan_root.is_dir():
                    continue
                for _rroot, _dirs, _files in os.walk(_scan_root, followlinks=True):
                    if "node_modules" in _rroot:
                        continue
                    for _fn in _files:
                        _p = Path(_rroot) / _fn
                        if _fn.endswith(".md"):
                            try:
                                _rel = _p.relative_to(REPO_ROOT)
                            except ValueError:
                                continue
                            repo_stems.setdefault(_p.stem.lower(), []).append(_p)
                            repo_rel_md_paths[str(_rel).lower()] = _p
                        elif _fn.endswith(".json"):
                            try:
                                _rel = _p.relative_to(REPO_ROOT)
                            except ValueError:
                                continue
                            repo_rel_json_paths[str(_rel).lower()] = _p
except Exception:
    REPO_ROOT = None

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
    if parts and parts[0] in (".devin", ".git", ".agents", ".claude", ".obsidian", "copilot", "node_modules"):
        return False
    return True

def resolve_wikilink(target: str, source_path: Path) -> bool:
    """Try to resolve a wikilink target. Returns True if resolvable."""
    if not target or target.startswith("http"):
        return True  # external or empty

    # Convention placeholders / non-wikilink artifacts
    if target in ("...", "none") or "dangerouslysetinnerhtml" in target.lower():
        return True

    key_plain = target.lower()
    key_underscore = target.lower().replace(" ", "_").replace("-", "_")
    base = target.rsplit("/", 1)[-1]
    if base.lower().endswith(".md"):
        base = base[:-3]
    base_plain = base.lower()
    base_underscore = base.lower().replace(" ", "_").replace("-", "_")

    for k in (base_underscore, base_plain, key_underscore, key_plain):
        if k in all_files_any or k in all_md_files or k in all_json_files:
            return True

    # 4. Full relpath lookup (with and without .md)
    for d in (rel_md_paths, rel_json_paths):
        for k in (key_plain, key_plain + ".md", key_underscore, key_underscore + ".md"):
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

        # 5b. Vault-root relative path
        try:
            resolved = (VAULT / target).resolve()
            if resolved.exists():
                return True
            resolved2 = (VAULT / (target + ".md")).resolve()
            if resolved2.exists():
                return True
        except Exception:
            pass

    # 6. .devin skill shorthand: [[skill-name]] -> .devin/skills/skill-name/SKILL.md
    if (VAULT / ".devin" / "skills" / target / "SKILL.md").is_file():
        return True

    # 7. For .devin files, also resolve against the real source-package root
    #    (covers [[docs/moc/...]] and [[Memory — ...]] links in references/*.md)
    if REPO_ROOT and source_path.is_relative_to(VAULT / ".devin"):
        for k in (base_underscore, base_plain, key_underscore, key_plain):
            if k in repo_stems:
                return True
        for d in (repo_rel_md_paths, repo_rel_json_paths):
            for k in (key_plain, key_plain + ".md", key_underscore, key_underscore + ".md"):
                if k in d:
                    return True
        if "/" in target:
            try:
                resolved = (REPO_ROOT / target).resolve()
                if resolved.exists():
                    return True
                resolved2 = (REPO_ROOT / (target + ".md")).resolve()
                if resolved2.exists():
                    return True
            except Exception:
                pass

    # 8. Naming-variant fallbacks for stale .devin wikilinks
    if REPO_ROOT and source_path.is_relative_to(VAULT / ".devin"):
        for suffix in ("_root4", "_root", "_MOC", "_CANON", "-agent"):
            if target.endswith(suffix):
                alt = target[:-len(suffix)]
                alt_keys = {alt.lower(), alt.lower().replace(" ", "_").replace("-", "_"), alt.lower().replace("-", "_")}
                if any(k in all_files_any or k in all_md_files or k in all_json_files or k in repo_stems for k in alt_keys):
                    return True
                # [[X_root4]] -> [[X_root]] (root note with numbered alias)
                if suffix == "_root4" and (alt + "_root").lower() in repo_stems:
                    return True
                if (VAULT / ".devin" / "agents" / f"amos-{alt}-agent.json").is_file() or (VAULT / ".devin" / "agents" / f"{alt}-agent.json").is_file():
                    return True
                if (VAULT / ".devin" / "skills" / alt / "SKILL.md").is_file():
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
        if any(part.startswith(".") and part not in (".devin", ".github") for part in parts):
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
            # Handles single, double, and multi-backtick inline code
            line = re.sub(r'`+[^`]*`+', lambda m: ' ' * len(m.group(0)), raw_line)
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
