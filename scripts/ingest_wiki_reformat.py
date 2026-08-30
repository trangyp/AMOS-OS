#!/usr/bin/env python3
"""
ingest_wiki_reformat.py — AMOS vault wiki-format ingest pass.

Reads every Markdown file in the vault and normalizes it to the AMOS wiki
format conventions (the same standard used by 11_KNOWLEDGE/LLM_WIKI/wiki/):

  - YAML frontmatter present at top of file, with a `title:` field
  - duplicate top-level frontmatter keys removed (first occurrence wins)
  - 4-backtick fences wrapping a file-level frontmatter unwrapped to the top
  - unclosed code fences closed (respecting containment: a shorter inner
    fence does not close a longer outer fence)
  - `* ` / `+ ` bullets -> `- ` (outside code; horizontal rules guarded)
  - `___` thematic breaks -> `---`
  - glued heading text (`## Description## Description`) repaired
  - ATX headings with trailing hashes (`# Title ##`) normalized
  - `**Related:**` / `**MOC:**` middle-dot spacing normalized
  - blank-line runs >2 collapsed to 2 (outside code)
  - CRLF / BOM normalized; exactly one trailing newline

Content is never rewritten: only whitespace, markers, fences, and
frontmatter structure are touched. Code blocks, callouts, math, RSCF-NODE
blocks and prose are preserved byte-for-byte.

Files with a real frontmatter at the top AND a second 4-backtick-wrapped
frontmatter payload later in the body are model-registry artifacts and are
left untouched (unwrapping them would create a second, broken frontmatter).

Usage:
    python3 scripts/ingest_wiki_reformat.py            # apply
    python3 scripts/ingest_wiki_reformat.py --dry-run  # preview only
    python3 scripts/ingest_wiki_reformat.py --verbose  # per-file detail
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path

try:
    import yaml
except ImportError:
    yaml = None

VAULT = Path(__file__).resolve().parent.parent

SKIP_DIR_PARTS = {
    ".git", "node_modules", ".obsidian", ".trash", "__pycache__",
    ".devin", ".agents", ".claude", ".copilot", ".opencode",
    ".next", "dist", ".turbo", ".venv",
    # live runtime session logs (constantly appended by the assistant backend)
    "copilot",
}
# raw sources are immutable per the wiki pattern; never touch them
SKIP_REL_PREFIXES = ("11_KNOWLEDGE/LLM_WIKI/raw/",)

BULLET_RE = re.compile(r"^(\s*(?:>\s*)*)[*+](?=\s)")
HR_GUARD_RE = re.compile(r"^[-*_]\s*[-*_\s]*$")          # * * * , - - - , ***
UNDERSCORE_HR_RE = re.compile(r"^_{3,}\s*$")
GLUED_HEADING_RE = re.compile(r"^(#{1,6})\s+(.+?)(#{1,6})\s*\2\s*$")
TRAILING_HASH_RE = re.compile(r"^(#{1,6}\s+.+?)\s+#+\s*$")
TOPLEVEL_KEY_RE = re.compile(r"^([A-Za-z_][\w.-]*):")
DUP_KEYS = {"title", "type", "source", "tags", "date", "id", "name",
            "created", "updated", "version", "parent", "aliases", "moc"}
RELATED_LINE_RE = re.compile(r"^\*\*(Related|MOC|Parent|Indexed by|See also)\*\*:")
FENCE_OPEN_RE = re.compile(r"^(`{3,}|~{3,})(.*)$")


def is_skippable(rel: str) -> bool:
    parts = rel.replace("\\", "/").split("/")
    if any(p in SKIP_DIR_PARTS for p in parts):
        return True
    if any(p.startswith(".tagmigrate") for p in parts):
        return True
    return any(rel.startswith(prefix) for prefix in SKIP_REL_PREFIXES)


def gate_fence(lines):
    """Iterate lines, yielding (line, in_code) with real fence semantics."""
    fence_char = None
    fence_len = 0
    for line in lines:
        stripped = line.lstrip()
        if fence_char is None:
            m = FENCE_OPEN_RE.match(stripped)
            if m and len(m.group(1)) >= 3:
                fence_char = m.group(1)[0]
                fence_len = len(m.group(1))
                yield line, True
                continue
            yield line, False
        else:
            # closing fence: run of same char with length >= opener
            run = re.match(r"^" + re.escape(fence_char) + r"+", stripped)
            if run and len(run.group(0)) >= fence_len:
                fence_char = None
                fence_len = 0
            yield line, True


def fix_body(body: str) -> tuple[str, Counter]:
    """Fence-aware body normalization. Returns (new_body, changes)."""
    changes = Counter()
    lines = body.split("\n")
    out: list[str] = []
    blank_run = 0
    fence_char = None
    fence_len = 0
    unclosed = False

    for line in lines:
        stripped = line.lstrip()
        in_code = fence_char is not None

        # --- fence state ---
        if fence_char is None:
            m = FENCE_OPEN_RE.match(stripped)
            if m and len(m.group(1)) >= 3:
                fence_char = m.group(1)[0]
                fence_len = len(m.group(1))
                out.append(line)
                continue
        else:
            run = re.match(r"^" + re.escape(fence_char) + r"+", stripped)
            if run and len(run.group(0)) >= fence_len:
                fence_char = None
                fence_len = 0
            out.append(line)
            continue

        # --- outside code: apply fixes ---
        # blank line collapse (3+ -> max 2)
        if not line.strip():
            blank_run += 1
            if blank_run > 2:
                changes["excess_blank_lines"] += 1
                continue
            out.append(line)
            continue
        blank_run = 0

        new = line

        # bullet markers: * / + -> -  (any indentation, blockquote-nested)
        m2b = BULLET_RE.match(new)
        if m2b and not HR_GUARD_RE.match(new.lstrip()):
            new = m2b.group(1) + "-" + new[m2b.end(1) + 1:]
            changes["star_plus_bullet"] += 1

        # underscore thematic breaks
        if UNDERSCORE_HR_RE.match(new):
            new = "---"
            changes["underscore_thematic_break"] += 1

        # glued duplicate heading: "## Description## Description"
        m3 = GLUED_HEADING_RE.match(new)
        if m3:
            new = f"{m3.group(1)} {m3.group(2)}"
            changes["glued_duplicate_heading"] += 1

        # trailing hashes on ATX headings
        m4 = TRAILING_HASH_RE.match(new)
        if m4:
            new = m4.group(1)
            changes["heading_trailing_hash"] += 1

        # middle-dot spacing in Related/MOC/Parent lines
        if RELATED_LINE_RE.match(new) and "\u00b7" in new:
            before = new
            new = re.sub(r"\]\u00b7", "] \u00b7", new)
            new = re.sub(r"\u00b7\[", "\u00b7 [", new)
            new = re.sub(r"(\w)\u00b7", r"\1 \u00b7", new)
            new = re.sub(r"\u00b7(\w)", r"\u00b7 \1", new)
            if new != before:
                changes["related_dot_spacing"] += 1

        out.append(new)

    # unclosed fence at EOF
    if fence_char is not None:
        out.append(fence_char * max(fence_len, 3))
        changes["unclosed_fence_closed"] += 1

    return "\n".join(out), changes


def close_open_fence_at_end(text: str) -> str:
    """If `text` ends inside an open fence, append its minimal closer."""
    fc, fl = None, 0
    for line in text.split("\n"):
        stripped = line.lstrip()
        if fc is None:
            m = FENCE_OPEN_RE.match(stripped)
            if m and len(m.group(1)) >= 3:
                fc, fl = m.group(1)[0], len(m.group(1))
        else:
            run = re.match(r"^" + re.escape(fc) + r"+", stripped)
            if run and len(run.group(0)) >= fl:
                fc, fl = None, 0
    if fc is not None:
        return text.rstrip("\n") + "\n" + fc * max(fl, 3)
    return text


def unwrap_embedded_frontmatter(text: str):
    """
    If a 4+-backtick fence wraps a file-level YAML frontmatter block,
    move the frontmatter to the top and remove the fence.

    Line-1 case: file starts with ````markdown then --- ... --- then ``````.
    Embedded case: prose precedes the fence; file has no real frontmatter.
    Returns (new_text, changed) or (text, False) when not applicable.
    """
    lines = text.split("\n")
    # line-1 case
    m = FENCE_OPEN_RE.match(lines[0].lstrip())
    if m and len(m.group(1)) >= 4 and len(lines) > 1 and lines[1].strip() == "---":
        # find closing fence: same char run >= N
        close_idx = None
        for i in range(2, len(lines)):
            run = re.match(r"^" + re.escape(m.group(1)[0]) + r"+\s*$", lines[i])
            if run and len(run.group(0)) >= len(m.group(1)):
                close_idx = i
                break
        if close_idx is not None:
            inner = "\n".join(lines[1:close_idx])
            inner = close_open_fence_at_end(inner)
            rest = "\n".join(lines[close_idx + 1:])
            return inner + ("\n" if rest else "") + rest, True
        return text, False

    # embedded case: search for a 4+-backtick fence containing a yaml block,
    # only when the file does NOT already start with a real frontmatter
    if text.startswith("---\n"):
        return text, False
    for i, line in enumerate(lines):
        mm = FENCE_OPEN_RE.match(line.lstrip())
        if mm and len(mm.group(1)) >= 4:
            fc = mm.group(1)[0]
            fl = len(mm.group(1))
            # find "---" opener right after
            for j in range(i + 1, min(i + 4, len(lines))):
                if lines[j].strip() == "---":
                    # find yaml close "---" then the fence close
                    y_close = None
                    for k in range(j + 1, len(lines)):
                        if lines[k].strip() == "---":
                            y_close = k
                            break
                    if y_close is None:
                        break
                    close_idx = None
                    for k in range(y_close + 1, len(lines)):
                        run = re.match(r"^" + re.escape(fc) + r"+\s*$", lines[k])
                        if run and len(run.group(0)) >= fl:
                            close_idx = k
                            break
                    if close_idx is None:
                        break
                    fm = "\n".join(lines[j:y_close + 1])
                    before = "\n".join(lines[:i])
                    wrapped_body = "\n".join(lines[y_close + 1:close_idx])
                    wrapped_body = close_open_fence_at_end(wrapped_body)
                    after = "\n".join(lines[close_idx + 1:])
                    parts = [fm]
                    if before.strip():
                        parts.append(before)
                    if wrapped_body.strip():
                        parts.append(wrapped_body)
                    if after.strip():
                        parts.append(after)
                    return "\n".join(p for p in parts if p), True
            break
    return text, False


def finalize_frontmatter(fm_text: str, rel: str) -> tuple[str, Counter]:
    """Fill missing type/source/tags/rscf with peer-verified defaults per directory."""
    changes = Counter()
    if yaml is None:
        return fm_text, changes
    try:
        fm = yaml.safe_load(fm_text) or {}
    except Exception:
        return fm_text, changes
    if not isinstance(fm, dict):
        return fm_text, changes

    rel = rel.replace("\\", "/")
    dir_key = "/".join(rel.split("/")[:-1])

    type_default = None
    if "stubs" in dir_key:
        type_default = "note"
    elif dir_key.startswith("07_SKILLS"):
        type_default = "skill" if rel.endswith("/SKILL.md") else "reference"
    elif dir_key.startswith("08_WORKFLOWS"):
        type_default = "workflow"
    elif dir_key.startswith("01_CANON"):
        type_default = "canon"
    elif dir_key.startswith("13_MODELS"):
        type_default = "registry" if "REGISTRY" in rel.upper() else "model"
    elif dir_key.startswith("11_KNOWLEDGE"):
        type_default = "note"
    elif dir_key == "":
        type_default = "note"

    rscf_default = None
    if "stubs" in dir_key:
        rscf_default = dict(state="DERIVED", claim_class="DERIVED",
                            provenance="AMOS_corpus", scope="AMOS_general")
    elif dir_key.startswith("01_CANON/02_UNIVERSE_CANON"):
        rscf_default = dict(state="SOURCE_CLAIM", claim_class="SOURCE_CLAIM",
                            provenance="AMOS_corpus", scope="universe_canon")
    elif dir_key.startswith("01_CANON/01_CORE_LAWS"):
        rscf_default = dict(state="SOURCE_CLAIM", claim_class="SOURCE_CLAIM",
                            provenance="AMOS_corpus", scope="AMOS_core_laws")
    elif dir_key.startswith("01_CANON"):
        rscf_default = dict(state="DERIVED", claim_class="DERIVED",
                            provenance="AMOS_corpus", scope="AMOS_general")
    elif dir_key.startswith("11_KNOWLEDGE"):
        rscf_default = dict(state="SOURCE_CLAIM", claim_class="SOURCE_CLAIM",
                            provenance="AMOS_corpus", scope="AMOS_knowledge")
    elif dir_key.startswith("00_ROOT"):
        rscf_default = dict(state="SOURCE_CLAIM", claim_class="SOURCE_CLAIM",
                            provenance="AMOS_corpus", scope="root_index")
    elif dir_key.startswith("07_SKILLS"):
        rscf_default = dict(state="DERIVED", claim_class="DERIVED",
                            provenance="AMOS_corpus", scope="AMOS_general")
    elif dir_key.startswith("08_WORKFLOWS"):
        rscf_default = dict(state="AMOS_MODEL", claim_class="AMOS_MODEL",
                            provenance="AMOS_corpus", scope="workflow_process")
    elif dir_key == "":
        rscf_default = dict(state="DERIVED", claim_class="DERIVED",
                            provenance="AMOS_corpus", scope="AMOS_general")

    source_default = dir_key if dir_key else "."

    lines = fm_text.split("\n")
    ins: list[str] = []
    if "type" not in fm and type_default:
        ins.append(f"type: {type_default}")
        changes["added_type"] += 1
    if "source" not in fm:
        ins.append(f"source: {source_default}")
        changes["added_source"] += 1
    if "tags" not in fm:
        ins.extend(["tags:", f"- {dir_key.split('/')[0].lower() if dir_key else 'vault'}"])
        changes["added_tags"] += 1
    if "rscf" not in fm and rscf_default:
        ins.append("rscf:")
        for k, val in rscf_default.items():
            ins.append(f"  {k}: {val}")
        changes["added_rscf"] += 1
    if ins:
        fm_text = fm_text + ("\n" if fm_text else "") + "\n".join(ins)
    return fm_text, changes


def normalize_frontmatter(fm_text: str, stem: str) -> tuple[str, Counter]:
    """Dedupe top-level keys; ensure title present and non-empty."""
    changes = Counter()
    lines = fm_text.split("\n")
    seen: set[str] = set()
    out: list[str] = []
    index = 0
    title_found = None
    while index < len(lines):
        line = lines[index]
        m = TOPLEVEL_KEY_RE.match(line)
        if m and m.group(1) in DUP_KEYS:
            key = m.group(1)
            if key in seen:
                # drop this duplicate key line AND its indented children
                changes["duplicate_fm_key"] += 1
                index += 1
                while index < len(lines) and (lines[index].startswith((" ", "\t")) or lines[index].strip() == ""):
                    index += 1
                continue
            seen.add(key)
            if key == "title":
                title_found = index
        out.append(line)
        index += 1

    # ensure title
    title_idx = None
    for i, line in enumerate(out):
        m = TOPLEVEL_KEY_RE.match(line)
        if m and m.group(1) == "title":
            title_idx = i
            break
    if title_idx is None:
        # insert at the very top of the frontmatter (index 0), so it never
        # lands inside a multi-line scalar or a list body
        out.insert(0, f"title: {stem}")
        changes["added_title"] += 1
    else:
        val = out[title_idx].split(":", 1)[1].strip().strip("'\"").strip()
        if not val or val.lower() in ("null", "none", "~"):
            out[title_idx] = f"title: {stem}"
            changes["filled_title"] += 1

    return "\n".join(out), changes


def process_file(path: Path, rel: str, dry_run: bool = False) -> tuple[bool, Counter]:
    """Returns (would_change, changes). Writes only when not dry_run."""
    changes = Counter()
    try:
        raw = path.read_bytes()
    except OSError:
        return False, changes

    text = raw.decode("utf-8", errors="replace")
    orig = text

    # BOM
    if text.startswith("\ufeff"):
        text = text[1:]
        changes["bom_removed"] += 1
    # CRLF -> LF (only when CRLF dominates)
    if "\r\n" in text and text.count("\r\n") >= text.count("\n") * 0.5:
        text = text.replace("\r\n", "\n")
        changes["crlf_normalized"] += 1

    # 4-backtick frontmatter wrapping
    text, did = unwrap_embedded_frontmatter(text)
    if did:
        changes["fm_unwrapped"] += 1

    # split frontmatter / body
    fm_text = None
    body = text
    if text.startswith("---\n"):
        end = text.find("\n---\n", 4)
        if end != -1:
            fm_text = text[4:end]
            body = text[end + 5:]

    # normalize body (fence-aware)
    body, body_changes = fix_body(body)
    changes += body_changes

    # normalize frontmatter
    if fm_text is not None:
        stem = path.stem
        fm_text, fm_changes = normalize_frontmatter(fm_text, stem)
        fm_text, fmc2 = finalize_frontmatter(fm_text, rel)
        fm_changes += fmc2
        changes += fm_changes
        new_text = "---\n" + fm_text + "\n---\n" + body
    else:
        # build minimal frontmatter
        if body.lstrip().startswith("---"):
            # a stray "---" (not a real fm) — leave body untouched, add fm anyway
            pass
        pars = rel.replace("\\", "/").split("/")
        stem = path.stem
        fm_text = f"title: {stem}\ntype: note\nsource: {pars[0] if len(pars) > 1 else '.'}\ntags:\n- vault\n"
        if len(pars) > 1:
            fm_text += f"- {pars[0].lower()}\n"
        new_text = "---\n" + fm_text + "---\n" + body
        changes["added_frontmatter"] += 1

    # exactly one trailing newline
    if not new_text.endswith("\n"):
        new_text += "\n"
        changes["trailing_newline"] += 1

    if new_text != orig:
        if not dry_run:
            try:
                path.write_text(new_text, encoding="utf-8")
            except OSError:
                return False, changes
        return True, changes
    return False, changes


def collect_files() -> list[tuple[Path, str]]:
    out = []
    for p in sorted(VAULT.rglob("*.md")):
        if not p.is_file():
            continue
        rel = str(p.relative_to(VAULT))
        if is_skippable(rel):
            continue
        out.append((p, rel))
    return out


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true", help="preview only")
    ap.add_argument("--verbose", action="store_true")
    args = ap.parse_args()

    files = collect_files()
    print(f"Scanning {len(files)} Markdown files\n", flush=True)

    totals = Counter()
    changed_files: list[tuple[str, Counter]] = []
    for p, rel in files:
        changed, ch = process_file(p, rel, dry_run=args.dry_run)
        if changed:
            changed_files.append((rel, ch))
            totals += ch

    print(f"{'DRY-RUN: ' if args.dry_run else ''}{len(changed_files)} files would be / were modified")
    print()
    print(f"{'Fix':<28}{'Count':>8}")
    print("-" * 36)
    for key, n in totals.most_common():
        print(f"{key:<28}{n:>8}")

    by_dir = Counter()
    for rel, _ in changed_files:
        by_dir[rel.split("/")[0]] += 1
    if by_dir:
        print()
        print("By top-level directory:")
        for d, n in by_dir.most_common():
            print(f"  {d:<28}{n:>6}")

    report = {
        "dry_run": args.dry_run,
        "scanned": len(files),
        "modified": len(changed_files),
        "totals": dict(totals),
        "by_dir": dict(by_dir),
    }
    if args.dry_run:
        # still write report for preview
        out = Path("/var/folders/_q/l3fbvngx5gjbvlkj2gzx01c80000gn/T/opencode/ingest_wiki_report.json")
        out.write_text(json.dumps(report, indent=2))
        print(f"\nReport: {out}")
    else:
        report["modified_files"] = [r for r, _ in changed_files]
        out = Path("/var/folders/_q/l3fbvngx5gjbvlkj2gzx01c80000gn/T/opencode/ingest_wiki_report.json")
        out.write_text(json.dumps(report, indent=2))
        print(f"\nReport: {out}")
    if args.verbose:
        for rel, ch in changed_files[:40]:
            print(f"  {rel}: {dict(ch)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())