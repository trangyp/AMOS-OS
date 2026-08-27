#!/usr/bin/env python3
"""
AMOS Knowledge Directory Filename Normalizer
- Converts filenames to ASCII UPPER_SNAKE_CASE
- Strips Vietnamese diacritics, emojis, special characters
- Removes decorative terms (FINAL, COMPLETE, OMEGA, etc.)
- Handles collisions by appending numeric suffix
- Generates a rename manifest
"""

import os
import re
import sys
import json
import unicodedata
from pathlib import Path

BASE_DIR = Path("/Users/mac/Documents/AMOS_OS/11_KNOWLEDGE")

# Decorative terms to strip (as whole tokens, case-insensitive)
# Only terms explicitly listed in AMOS Naming Standard §2 and §32
DECORATIVE_TERMS = {
    "FINAL", "COMPLETE", "ULTIMATE", "OMEGA", "SUPREME", "INFINITY",
    "INFINITE", "PERFECT", "ULTRA", "MAXIMUM", "LATEST", "BEST",
    "NEW",
}

# But don't strip if it would leave the name too short or meaningless
MIN_TOKENS_AFTER_STRIP = 1

# Files to skip entirely
SKIP_FILES = {".DS_Store", "_rename_script.py", "_rename_manifest.json", "_rename_collisions.txt"}


def strip_diacritics(text: str) -> str:
    """Remove accents/diacritics, convert to closest ASCII."""
    # Handle Vietnamese precomposed characters that don't decompose with NFD
    vietnamese_map = {
        'Đ': 'D', 'đ': 'D',
        'Ơ': 'O', 'ơ': 'O',
        'Ư': 'U', 'ư': 'U',
        'Ǎ': 'A', 'ǎ': 'A',
        'Ǐ': 'I', 'ǐ': 'I',
        'Ǒ': 'O', 'ǒ': 'O',
        'Ǔ': 'U', 'ǔ': 'U',
        'Ǧ': 'G', 'ǧ': 'G',
        'Ǩ': 'K', 'ǩ': 'K',
        'Ň': 'N', 'ň': 'N',
        'Ș': 'S', 'ș': 'S',
        'Ț': 'T', 'ț': 'T',
        'Æ': 'AE', 'æ': 'AE',
        'Ø': 'O', 'ø': 'O',
        'Þ': 'TH', 'þ': 'TH',
        'Ð': 'D', 'ð': 'D',
        'Œ': 'OE', 'œ': 'OE',
        'ẞ': 'SS', 'ß': 'SS',
        'Ł': 'L', 'ł': 'L',
        'Ø': 'O',
    }
    for vn_char, replacement in vietnamese_map.items():
        text = text.replace(vn_char, replacement)

    # NFD decomposition separates base chars from combining marks
    normalized = unicodedata.normalize("NFD", text)
    # Keep only non-combining characters
    ascii_text = "".join(c for c in normalized if unicodedata.category(c) != "Mn")
    return ascii_text


def remove_emojis_and_non_ascii(text: str) -> str:
    """Remove emojis and non-ASCII characters, replace with space."""
    result = []
    for c in text:
        cp = ord(c)
        # Keep basic ASCII printable + extended space chars
        if cp < 128:
            result.append(c)
        elif c in ("\u2014", "\u2013", "\u2019", "\u2018", "\u201c", "\u201d"):
            # Convert smart quotes/dashes to ASCII
            replacements = {
                "\u2014": "-", "\u2013": "-",
                "\u2019": "'", "\u2018": "'",
                "\u201c": '"', "\u201d": '"',
            }
            result.append(replacements.get(c, " "))
        elif unicodedata.category(c).startswith(("Sm", "So", "Pf", "Pi")):
            # Math symbols, other symbols, final/initial quotes -> space
            result.append(" ")
        else:
            result.append(" ")
    return "".join(result)


def normalize_filename(filename: str) -> str:
    """
    Normalize a filename to ASCII UPPER_SNAKE_CASE.
    Returns the new filename (with extension preserved).
    """
    # Skip special files
    if filename in SKIP_FILES:
        return filename

    # Split name and extension
    name, ext = os.path.splitext(filename)
    ext = ext.lower()  # Normalize extension to lowercase

    # If no extension or non-md extension, keep as-is for ext
    if not ext:
        ext = ".md"  # Default extension for extensionless files

    # Step 1: Strip diacritics (Vietnamese etc.)
    name = strip_diacritics(name)

    # Step 2: Remove emojis and non-ASCII
    name = remove_emojis_and_non_ascii(name)

    # Step 3: Replace various separators with underscore
    # Handle: spaces, hyphens (but not within version numbers), periods in name
    # First, protect version-like patterns (v1, v2.0, etc.)
    name = re.sub(r'(?<=\w)[-](?=\w)', '_', name)  # hyphens between word chars -> _
    # Replace standalone dashes (em-dash, en-dash already converted) and spaces
    name = name.replace(' ', '_')
    name = name.replace('.', '_')
    name = name.replace(',', '_')
    name = name.replace('(', '_')
    name = name.replace(')', '_')
    name = name.replace('[', '_')
    name = name.replace(']', '_')
    name = name.replace('{', '_')
    name = name.replace('}', '_')
    name = name.replace('&', '_AND_')
    name = name.replace('+', '_PLUS_')
    name = name.replace('/', '_')
    name = name.replace('\\', '_')
    name = name.replace(':', '_')
    name = name.replace(';', '_')
    name = name.replace('!', '_')
    name = name.replace('?', '_')
    name = name.replace('"', '_')
    name = name.replace("'", '_')
    name = name.replace('*', '_')
    name = name.replace('#', '_')
    name = name.replace('@', '_AT_')
    name = name.replace('%', '_PCT_')
    name = name.replace('=', '_EQ_')
    name = name.replace('<', '_')
    name = name.replace('>', '_')
    name = name.replace('|', '_')
    name = name.replace('~', '_')
    name = name.replace('^', '_')
    name = name.replace('`', '_')
    # Remove trademark/copyright symbols
    name = name.replace('™', '')
    name = name.replace('®', '')
    name = name.replace('©', '')

    # Step 3.5: Handle remaining special symbols before uppercase
    name = name.replace('×', '_X_')
    name = name.replace('∅', '_EMPTY_')
    name = name.replace('π', '_PI_')
    name = name.replace('→', '_TO_')
    name = name.replace('←', '_FROM_')
    name = name.replace('↔', '_BIDIR_')
    name = name.replace('√', '_SQRT_')
    name = name.replace('∞', '_INF_')
    name = name.replace('≈', '_APPROX_')
    name = name.replace('≠', '_NEQ_')
    name = name.replace('≤', '_LE_')
    name = name.replace('≥', '_GE_')

    # Step 4: Convert to uppercase
    name = name.upper()

    # Step 5: Collapse multiple underscores
    name = re.sub(r'_+', '_', name)

    # Step 5.5: Clean up dash-underscore patterns (from em-dashes)
    # Replace _-_ with single underscore, and remove leading/trailing dashes
    name = name.replace('_-_', '_')
    name = name.replace('--', '_')
    name = re.sub(r'^[-_]+', '', name)
    name = re.sub(r'[-_]+$', '', name)
    # Re-collapse underscores after dash cleanup
    name = re.sub(r'_+', '_', name)
    name = name.strip('_')

    # Step 6: Strip leading/trailing underscores
    name = name.strip('_')

    # Step 7: Split into tokens and strip decorative terms
    tokens = name.split('_')
    original_tokens = list(tokens)

    # Strip decorative terms
    filtered_tokens = [t for t in tokens if t not in DECORATIVE_TERMS]

    # Don't strip if it would leave no tokens
    if len(filtered_tokens) < MIN_TOKENS_AFTER_STRIP or not filtered_tokens:
        filtered_tokens = tokens  # Keep original if stripping would empty it

    # Also remove tokens that are just numbers attached to decorative words
    # e.g. "V2", "V3" etc. are fine to keep
    # But "2", "3" standalone after stripping decorative might be confusing
    # Let's keep them - they might be version numbers

    tokens = filtered_tokens

    # Step 8: Rejoin
    name = '_'.join(tokens)

    # Step 9: Clean up any remaining issues
    name = re.sub(r'_+', '_', name)
    name = name.strip('_')

    # Step 10: Handle empty name
    if not name:
        name = "UNNAMED"

    # Step 11: Truncate if too long (filesystem limit ~255 chars)
    max_name_len = 200  # Leave room for extension and collision suffix
    if len(name) > max_name_len:
        name = name[:max_name_len].rsplit('_', 1)[0]  # Cut at word boundary
        name = name.strip('_')

    return f"{name}{ext}"


def collect_files(base_dir: Path) -> list[tuple[str, Path]]:
    """Collect all files in all subdirectories."""
    all_files = []
    for entry in sorted(base_dir.iterdir()):
        if entry.is_dir():
            for f in sorted(entry.iterdir()):
                if f.is_file() and f.name not in SKIP_FILES:
                    all_files.append((entry.name, f))
        elif entry.is_file() and entry.name not in SKIP_FILES:
            # Files directly in base dir (not in subdirectories)
            all_files.append((".", entry))
    return all_files


def check_collisions(renames: dict[tuple[str, str], str], no_change: list[tuple[str, str]]) -> dict[str, list[tuple[str, str]]]:
    """Check for collisions in the proposed new names, including existing conformant files."""
    # Set of names that already exist (conformant files not being renamed)
    conformant_keys = {f"{sd}/{n}" for sd, n in no_change}

    # Group all proposed targets (including conformant ones that match)
    target_map = {}  # target_key -> list of (subdir, old_name) that want it
    for (subdir, old_name), new_name in renames.items():
        key = f"{subdir}/{new_name}"
        if key not in target_map:
            target_map[key] = []
        target_map[key].append((subdir, old_name))

    # Also check if any rename target matches a conformant file
    for (subdir, old_name), new_name in renames.items():
        key = f"{subdir}/{new_name}"
        if key in conformant_keys and old_name != new_name:
            # This rename target collides with an existing conformant file
            if key not in target_map:
                target_map[key] = []
            # Mark the conformant file as the "owner" of the base name
            if ("EXISTING", key) not in target_map[key]:
                target_map[key].insert(0, ("EXISTING", key))

    # Find collisions (more than one claimant for a target)
    collisions = {}
    for key, claimants in target_map.items():
        if len(claimants) > 1:
            collisions[key] = claimants

    return collisions


def resolve_collisions(renames: dict[tuple[str, str], str], collisions: dict, no_change: list[tuple[str, str]]) -> dict[tuple[str, str], str]:
    """Resolve collisions by appending numeric suffixes."""
    resolved = dict(renames)
    # Track all names that will be taken after resolution
    taken = {f"{sd}/{n}" for sd, n in no_change}
    # Also track resolved rename targets
    for (sd, old), new in resolved.items():
        taken.add(f"{sd}/{new}")

    for key, claimants in collisions.items():
        subdir = key.rsplit('/', 1)[0]
        base_new = key.rsplit('/', 1)[1]
        name, ext = os.path.splitext(base_new)

        for sd, old_name in claimants:
            if old_name == "EXISTING":
                # The existing conformant file keeps its name
                continue
            # Find a unique name
            counter = 2
            while True:
                candidate = f"{name}_{counter}{ext}"
                candidate_key = f"{sd}/{candidate}"
                if candidate_key not in taken:
                    break
                counter += 1
            # Update resolved and taken
            old_key = f"{sd}/{resolved[(sd, old_name)]}"
            taken.discard(old_key)
            resolved[(sd, old_name)] = candidate
            taken.add(f"{sd}/{candidate}")

    return resolved


def main():
    dry_run = "--dry-run" in sys.argv or "-n" in sys.argv

    print(f"Mode: {'DRY RUN' if dry_run else 'EXECUTE'}")
    print(f"Base directory: {BASE_DIR}")
    print()

    # Collect all files
    all_files = collect_files(BASE_DIR)
    print(f"Total files found: {len(all_files)}")

    # Generate proposed new names
    renames = {}
    no_change = []
    for subdir, filepath in all_files:
        old_name = filepath.name
        new_name = normalize_filename(old_name)
        if old_name == new_name:
            no_change.append((subdir, old_name))
        else:
            renames[(subdir, old_name)] = new_name

    print(f"Files needing rename: {len(renames)}")
    print(f"Files already conformant: {len(no_change)}")
    print()

    # Check collisions (including against existing conformant files)
    collisions = check_collisions(renames, no_change)
    if collisions:
        print(f"Collisions detected: {len(collisions)}")
        for key, files in sorted(collisions.items()):
            print(f"  {key}:")
            for sd, old in files:
                print(f"    <- {sd}/{old}")
        print()

    # Resolve collisions
    if collisions:
        renames = resolve_collisions(renames, collisions, no_change)
        print("Collisions resolved with numeric suffixes.")
        print()

    # Re-check collisions after resolution
    collisions2 = check_collisions(renames, no_change)
    if collisions2:
        print(f"WARNING: Unresolvable collisions remain: {len(collisions2)}")
        for key, files in collisions2.items():
            print(f"  {key}: {files}")

    # Show sample renames
    print("\n=== Sample renames (first 50) ===")
    for i, ((subdir, old_name), new_name) in enumerate(sorted(renames.items())):
        if i >= 50:
            print(f"  ... and {len(renames) - 50} more")
            break
        print(f"  {subdir}/{old_name}")
        print(f"    -> {new_name}")

    # Generate manifest
    manifest = {
        "total_files": len(all_files),
        "files_renamed": len(renames),
        "files_unchanged": len(no_change),
        "collisions_detected": len(collisions),
        "renames": [
            {
                "subdir": sd,
                "old_name": old,
                "new_name": new,
                "old_path": f"{sd}/{old}",
                "new_path": f"{sd}/{new}",
            }
            for (sd, old), new in sorted(renames.items())
        ],
        "unchanged": [
            {"subdir": sd, "name": old}
            for sd, old in sorted(no_change)
        ],
    }

    manifest_path = BASE_DIR / "_rename_manifest.json"
    with open(manifest_path, "w", encoding="utf-8") as f:
        json.dump(manifest, f, indent=2, ensure_ascii=False)
    print(f"\nManifest written to: {manifest_path}")

    if dry_run:
        print("\n=== DRY RUN COMPLETE - no files were renamed ===")
        return

    # Execute renames
    print("\n=== EXECUTING RENAMES ===")
    success = 0
    errors = []
    for (subdir, old_name), new_name in sorted(renames.items()):
        if subdir == ".":
            old_path = BASE_DIR / old_name
            new_path = BASE_DIR / new_name
        else:
            old_path = BASE_DIR / subdir / old_name
            new_path = BASE_DIR / subdir / new_name

        try:
            if new_path.exists():
                # Don't overwrite existing files
                errors.append(f"Target exists: {new_path}")
                continue
            old_path.rename(new_path)
            success += 1
        except Exception as e:
            errors.append(f"{old_path} -> {new_path}: {e}")

    print(f"Successfully renamed: {success}")
    if errors:
        print(f"Errors: {len(errors)}")
        for e in errors[:20]:
            print(f"  {e}")

    print("\n=== RENAME COMPLETE ===")


if __name__ == "__main__":
    main()
