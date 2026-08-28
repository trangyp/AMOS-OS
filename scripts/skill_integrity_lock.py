#!/usr/bin/env python3
"""
AMOS Skill Integrity Lock — Generate lock files with SHA-256 content hashes
for reproducible installs and tamper detection.

Inspired by SOTA repos:
  - luisalima/skills-lock: Lock file with pinned commits, content hashes, --frozen CI
  - agentskills/agentskills#358: Provenance attestation (SHA-256 digest + Ed25519 sig)
  - snapsynapse/skill-provenance: Version identity, staleness, SHA-256 integrity
  - mcyork/skillseal: GPG/SSH signing, multi-key attestation, trust store
  - vercel-labs/skills#559: .agents/manifest.json with versioned skill entries

Generates:
  1. skills-lock.json — per-skill SHA-256 hashes, versions, file counts
  2. Per-skill skill_digest — deterministic hash over full skill directory
  3. Drift detection — compare current state against a lock file

Usage:
  python3 scripts/skill_integrity_lock.py                    # generate lock file
  python3 scripts/skill_integrity_lock.py --verify            # verify against lock
  python3 scripts/skill_integrity_lock.py --drift             # show drift report
  python3 scripts/skill_integrity_lock.py --json              # JSON output
  python3 scripts/skill_integrity_lock.py --skill amos-foo    # single skill hash
"""

import argparse
import hashlib
import json
import os
import sys
import time
from pathlib import Path

try:
    import yaml
except ImportError:
    print("ERROR: PyYAML required. Install: pip install pyyaml", file=sys.stderr)
    sys.exit(2)


# ── Hashing ──────────────────────────────────────────────────────────────────

def sha256_file(path: Path) -> str:
    """Compute SHA-256 hash of a file."""
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(8192), b""):
            h.update(chunk)
    return h.hexdigest()


def skill_digest(skill_dir: Path) -> str:
    """
    Compute deterministic SHA-256 over the full skill directory.
    Per agentskills/agentskills#358 algorithm:
      for each regular file f in skill_dir, sorted lexicographically by relpath:
          digest_input += relpath + 0x00 + sha256(file_content) + 0x0A
      skill_digest = "sha256-" + base64url(sha256(digest_input))
    """
    h = hashlib.sha256()
    files = []
    for f in skill_dir.rglob("*"):
        if not f.is_file():
            continue
        # Exclude .git, dotfiles, SKILL.sig
        rel = f.relative_to(skill_dir)
        if str(rel).startswith(".git") or rel.name.startswith(".") or rel.name == "SKILL.sig":
            continue
        files.append((str(rel), f))

    for relpath, filepath in sorted(files, key=lambda x: x[0]):
        file_hash = sha256_file(filepath)
        h.update(relpath.encode("utf-8"))
        h.update(b"\x00")
        h.update(file_hash.encode("utf-8"))
        h.update(b"\x0a")

    import base64
    digest = "sha256-" + base64.urlsafe_b64encode(h.digest()).decode("ascii").rstrip("=")
    return digest


def parse_frontmatter(text: str) -> dict:
    """Extract YAML frontmatter from markdown."""
    if not text.startswith("---"):
        return {}
    parts = text.split("---", 2)
    if len(parts) < 3:
        return {}
    try:
        fm = yaml.safe_load(parts[1])
        return fm if isinstance(fm, dict) else {}
    except yaml.YAMLError:
        return {}


# ── Lock File Generator ──────────────────────────────────────────────────────

def generate_lock_entry(skill_dir: Path) -> dict:
    """Generate a lock file entry for a single skill."""
    sm = skill_dir / "SKILL.md"
    if not sm.exists():
        return None

    text = sm.read_text(encoding="utf-8", errors="replace")
    fm = parse_frontmatter(text)

    # Count files by type
    file_count = 0
    total_size = 0
    file_hashes = {}
    for f in skill_dir.rglob("*"):
        if not f.is_file():
            continue
        rel = str(f.relative_to(skill_dir))
        if rel.startswith(".git") or rel.startswith("."):
            continue
        file_count += 1
        total_size += f.stat().st_size
        file_hashes[rel] = sha256_file(f)

    return {
        "name": fm.get("name", skill_dir.name),
        "version": fm.get("version", "unknown"),
        "schema_version": fm.get("schema_version", "unknown"),
        "steward": fm.get("steward", "unknown"),
        "skill_digest": skill_digest(skill_dir),
        "file_count": file_count,
        "total_size_bytes": total_size,
        "skill_md_hash": sha256_file(sm),
        "file_hashes": file_hashes,
    }


def generate_lock_file(skills_dir: Path, exclude_prefix: str = "00_") -> dict:
    """Generate a complete lock file."""
    lock = {
        "$schema": "https://amos.ai/schemas/skills-lock.json",
        "version": "1.0.0",
        "generated_at": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        "skills_dir": str(skills_dir),
        "total_skills": 0,
        "skills": {},
    }

    for sd in sorted(skills_dir.iterdir()):
        if not sd.is_dir() or sd.name.startswith(exclude_prefix):
            continue
        entry = generate_lock_entry(sd)
        if entry:
            lock["skills"][entry["name"]] = entry
            lock["total_skills"] += 1

    return lock


# ── Verification ─────────────────────────────────────────────────────────────

def verify_against_lock(skills_dir: Path, lock_file: Path, exclude_prefix: str = "00_") -> dict:
    """Verify current skills against a lock file."""
    if not lock_file.exists():
        return {"error": "Lock file not found", "path": str(lock_file)}

    lock = json.loads(lock_file.read_text(encoding="utf-8"))
    results = {
        "total_locked": len(lock.get("skills", {})),
        "matched": 0,
        "mismatched": 0,
        "missing": 0,
        "extra": 0,
        "details": [],
    }

    locked_skills = lock.get("skills", {})
    current_skills = set()

    for sd in sorted(skills_dir.iterdir()):
        if not sd.is_dir() or sd.name.startswith(exclude_prefix):
            continue
        sm = sd / "SKILL.md"
        if not sm.exists():
            continue
        text = sm.read_text(encoding="utf-8", errors="replace")
        fm = parse_frontmatter(text)
        name = fm.get("name", sd.name)
        current_skills.add(name)

        if name not in locked_skills:
            results["extra"] += 1
            results["details"].append({"skill": name, "status": "EXTRA", "message": "Not in lock file"})
            continue

        locked = locked_skills[name]
        current_digest = skill_digest(sd)

        if current_digest == locked["skill_digest"]:
            results["matched"] += 1
        else:
            results["mismatched"] += 1
            # Find which files changed
            changed_files = []
            for f in sd.rglob("*"):
                if not f.is_file():
                    continue
                rel = str(f.relative_to(sd))
                if rel.startswith(".git") or rel.startswith("."):
                    continue
                current_hash = sha256_file(f)
                if rel in locked.get("file_hashes", {}):
                    if current_hash != locked["file_hashes"][rel]:
                        changed_files.append(rel)
                else:
                    changed_files.append(f"{rel} (new)")
            results["details"].append({
                "skill": name,
                "status": "MISMATCH",
                "changed_files": changed_files[:10],
            })

    # Check for missing skills
    for name in locked_skills:
        if name not in current_skills:
            results["missing"] += 1
            results["details"].append({"skill": name, "status": "MISSING"})

    return results


# ── CLI ──────────────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(description="AMOS Skill Integrity Lock")
    parser.add_argument("--skills-dir", default=".devin/skills", help="Skills directory")
    parser.add_argument("--lock-file", default="skills-lock.json", help="Lock file path")
    parser.add_argument("--skill", default=None, help="Hash a single skill")
    parser.add_argument("--verify", action="store_true", help="Verify against lock file")
    parser.add_argument("--drift", action="store_true", help="Show drift report")
    parser.add_argument("--json", action="store_true", help="JSON output")
    parser.add_argument("--output", "-o", default=None, help="Output file path")
    args = parser.parse_args()

    skills_dir = Path(args.skills_dir)
    lock_file = Path(args.lock_file)

    if args.skill:
        sd = skills_dir / args.skill
        if not sd.exists():
            print(f"ERROR: Skill {args.skill} not found", file=sys.stderr)
            sys.exit(1)
        entry = generate_lock_entry(sd)
        if args.json:
            json.dump(entry, sys.stdout, indent=2)
            print()
        else:
            print(f"=== Skill Integrity: {entry['name']} ===")
            print(f"  Version:        {entry['version']}")
            print(f"  Schema version: {entry['schema_version']}")
            print(f"  Steward:        {entry['steward']}")
            print(f"  Skill digest:   {entry['skill_digest']}")
            print(f"  SKILL.md hash:  {entry['skill_md_hash']}")
            print(f"  File count:     {entry['file_count']}")
            print(f"  Total size:     {entry['total_size_bytes']:,} bytes")
        return

    if args.verify or args.drift:
        results = verify_against_lock(skills_dir, lock_file)
        if args.json:
            json.dump(results, sys.stdout, indent=2)
            print()
        else:
            mode = "Drift Report" if args.drift else "Verification"
            print(f"=== Skill Integrity {mode} ===")
            print(f"  Total locked:   {results['total_locked']}")
            print(f"  Matched:        {results['matched']}")
            print(f"  Mismatched:     {results['mismatched']}")
            print(f"  Missing:        {results['missing']}")
            print(f"  Extra:          {results['extra']}")
            if results["details"]:
                print()
                for d in results["details"][:20]:
                    if d["status"] == "MISMATCH":
                        print(f"  [MISMATCH] {d['skill']}: {len(d.get('changed_files', []))} files changed")
                        for cf in d.get("changed_files", [])[:5]:
                            print(f"    - {cf}")
                    else:
                        print(f"  [{d['status']}] {d['skill']}")
        sys.exit(1 if results["mismatched"] > 0 or results["missing"] > 0 else 0)

    # Default: generate lock file
    lock = generate_lock_file(skills_dir)

    output_path = Path(args.output) if args.output else lock_file
    output_path.write_text(json.dumps(lock, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    if args.json:
        json.dump(lock, sys.stdout, indent=2, sort_keys=True)
        print()
    else:
        print(f"=== Skill Integrity Lock Generated ===")
        print(f"  Lock file:      {output_path}")
        print(f"  Total skills:   {lock['total_skills']}")
        print(f"  Generated at:   {lock['generated_at']}")
        print()
        print(f"  Top 5 by file count:")
        sorted_skills = sorted(lock["skills"].values(), key=lambda x: -x["file_count"])
        for s in sorted_skills[:5]:
            print(f"    {s['file_count']:4d} files  {s['name']}")
        print()
        print(f"  All skills have skill_digest: {all('skill_digest' in s for s in lock['skills'].values())}")


if __name__ == "__main__":
    main()
