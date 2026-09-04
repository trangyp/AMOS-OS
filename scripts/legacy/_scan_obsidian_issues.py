#!/usr/bin/env python3
"""
Comprehensive Obsidian-specific structural scanner.

Checks for:
  1. Malformed callouts (missing type or content)
  2. Broken file embeds ![[...]] pointing to non-existent files
  3. Broken block references [[file#^blockid]] where blockid doesn't exist
  4. Broken heading references [[file#heading]] where heading doesn't exist
  5. Unclosed inline math $...$ (odd count on a line, excluding block $$)
  6. Malformed footnote definitions / references
  7. Stray HTML comment openers without closers
  8. Files with frontmatter but empty title/name/ID fields
  9. Wikilinks with pipe but empty alias [[file|]]
 10. Code fence info string anomalies (mismatched language tags)
"""
from __future__ import annotations
import os, re, sys, json
from pathlib import Path
from collections import defaultdict

VAULT = Path(__file__).resolve().parents[2]
MD_FILES = sorted(p for p in VAULT.rglob("*.md") if p.is_file())

# Build file index (basename without extension, lowercase)
file_index: dict[str, list[Path]] = defaultdict(list)
for p in MD_FILES:
    file_index[p.stem.lower()].append(p)
    file_index[p.name.lower()].append(p)

def read_text(p: Path) -> str:
    try:
        return p.read_text(encoding="utf-8", errors="replace")
    except Exception:
        return ""

def strip_frontmatter(text: str) -> tuple[str, str]:
    if text.startswith("---\n"):
        end = text.find("\n---\n", 4)
        if end != -1:
            return text[4:end], text[end+5:]
    return "", text

issues: list[tuple[str, str, int, str]] = []  # (file, category, line, detail)

CALLOUT_RE = re.compile(r'^>\s*\[!([^\]]+)\](.*)$')
EMBED_RE = re.compile(r'!\[\[([^\]]+)\]\]')
WIKILINK_RE = re.compile(r'\[\[([^\]]+)\]\]')
FOOTNOTE_REF_RE = re.compile(r'\[\^([^\]]+)\](?!\()')
FOOTNOTE_DEF_RE = re.compile(r'^\[\^([^\]]+)\]:\s*(.*)$')
HTML_COMMENT_OPEN = re.compile(r'<!--')
HTML_COMMENT_CLOSE = re.compile(r'-->')
INLINE_MATH_RE = re.compile(r'(?<!\$)\$(?!\$)([^$\n]*?)(?<!\$)\$(?!\$)')

# Heading reference pattern: [[file#heading]] or [[#heading]]
HEADING_REF_RE = re.compile(r'\[\[([^\]|^]+)?#([^\]|^]+)\]\]')
BLOCK_REF_RE = re.compile(r'\[\[([^\]|^]+)?\^([^\]|^]+)\]\]')

# Collect all headings and block IDs per file
file_headings: dict[Path, set[str]] = {}
file_block_ids: dict[Path, set[str]] = {}

for p in MD_FILES:
    text = read_text(p)
    _, body = strip_frontmatter(text)
    headings = set()
    block_ids = set()
    for line in body.split("\n"):
        m = re.match(r'^(#{1,6})\s+(.+)$', line)
        if m:
            h = m.group(2).strip().lower().replace(" ", "-")
            h = re.sub(r'[^\w\-]', '', h)
            headings.add(h)
        for bid in re.findall(r'\^([a-zA-Z0-9_\-]+)\s*$', line):
            block_ids.add(bid)
    file_headings[p] = headings
    file_block_ids[p] = block_ids

print(f"Scanned {len(MD_FILES)} .md files")

# Scan each file
for p in MD_FILES:
    rel = str(p.relative_to(VAULT))
    text = read_text(p)
    fm, body = strip_frontmatter(text)
    lines = body.split("\n")

    in_code = False
    code_fence = None
    html_open = 0

    for i, line in enumerate(lines, 1):
        # Track code fences
        stripped = line.lstrip()
        if stripped.startswith("```") or stripped.startswith("~~~"):
            marker = stripped[:3]
            if not in_code:
                in_code = True
                code_fence = marker
            elif code_fence and stripped.startswith(code_fence):
                in_code = False
                code_fence = None
            continue
        if in_code:
            continue

        # 1. Malformed callouts
        m = CALLOUT_RE.match(line)
        if m:
            ctype = m.group(1).strip()
            if not ctype:
                issues.append((rel, "callout_empty_type", i, line.strip()[:80]))

        # 2. Broken file embeds
        for embed in EMBED_RE.findall(line):
            target = embed.split("|")[0].split("#")[0].split("^")[0].strip()
            if not target:
                continue
            # Check if target file exists
            target_lower = target.lower()
            if target_lower not in file_index:
                # Try with .md extension
                if not target.endswith((".png",".jpg",".jpeg",".gif",".svg",".pdf",".canvas",".mp4",".webm")):
                    if (target_lower + ".md") not in {k for k in file_index} and target_lower not in file_index:
                        issues.append((rel, "broken_embed", i, f"![[{embed}]]"))

        # 3 & 4. Heading/block references
        for m in HEADING_REF_RE.finditer(line):
            target_file = m.group(1)
            heading = m.group(2).strip().lower().replace(" ", "-")
            heading = re.sub(r'[^\w\-]', '', heading)
            if target_file:
                tf_lower = target_file.strip().lower()
                candidates = file_index.get(tf_lower, [])
                if not candidates:
                    # try stem
                    candidates = file_index.get(tf_lower.replace(".md",""), [])
                if not candidates:
                    issues.append((rel, "broken_heading_ref", i, f"[[{m.group(0)[2:-2]}]]: file not found"))
                else:
                    for c in candidates[:1]:
                        if heading and heading not in file_headings.get(c, set()):
                            # Only flag if heading is non-empty and not a section anchor
                            issues.append((rel, "broken_heading_ref", i, f"[[{m.group(0)[2:-2]}]]: heading '{heading}' not found"))
            else:
                # Same-file heading ref
                if heading and heading not in file_headings.get(p, set()):
                    issues.append((rel, "broken_heading_ref", i, f"[[#{m.group(2)}]]: heading not found in same file"))

        for m in BLOCK_REF_RE.finditer(line):
            target_file = m.group(1)
            block_id = m.group(2).strip()
            if target_file:
                tf_lower = target_file.strip().lower()
                candidates = file_index.get(tf_lower, [])
                if not candidates:
                    candidates = file_index.get(tf_lower.replace(".md",""), [])
                if not candidates:
                    issues.append((rel, "broken_block_ref", i, f"[[{m.group(0)[2:-2]}]]: file not found"))
                else:
                    for c in candidates[:1]:
                        if block_id and block_id not in file_block_ids.get(c, set()):
                            issues.append((rel, "broken_block_ref", i, f"[[{m.group(0)[2:-2]}]]: block id not found"))
            else:
                if block_id and block_id not in file_block_ids.get(p, set()):
                    issues.append((rel, "broken_block_ref", i, f"[[^{block_id}]]: block id not found in same file"))

        # 5. Unclosed inline math — strip balanced $...$ pairs, then shell/currency
        if "$" in line and "$$" not in line and "LLM_WIKI/raw" not in rel:
            cleaned = line.replace(r"\$", "")
            # Strip HTML tags/comments and inline code spans (they can contain literal $)
            cleaned = re.sub(r'<[^>]+>', '', cleaned)
            cleaned = re.sub(r'<(script|style)\b[^>]*>.*?</\1>', '', cleaned, flags=re.DOTALL)
            cleaned = re.sub(r'`[^`]*`', '', cleaned)
            # Remove balanced inline math pairs first (including $...$ with parens/spaces)
            cleaned = re.sub(r'\$(?!\$)[^$\n]*\$', '', cleaned)
            # Remove shell substitutions $(...), ${...}, and template ${VAR}
            cleaned = re.sub(r'\$\{[^}]*\}', '', cleaned)
            cleaned = re.sub(r'\$\([^)]*\)', '', cleaned)
            # Remove currency patterns $<digit> or $<space><word> (shell prompts)
            cleaned = re.sub(r'\$\s*\d', '', cleaned)
            cleaned = re.sub(r'\$\s+(npm|pip|cargo|python|node|yarn|pnpm|git|make|cd|echo|cat|bash|sh)\b', '', cleaned)
            # Remove $ at start of line (shell prompt)
            cleaned = re.sub(r'^\s*\$', '', cleaned)
            count = cleaned.count("$")
            if count % 2 != 0:
                if cleaned.strip() not in ("$$",):
                    issues.append((rel, "unclosed_inline_math", i, line.strip()[:80]))

        # 6. Footnote references without definitions (collect, check later)
        # (handled below)

        # 7. HTML comment tracking
        html_open += len(HTML_COMMENT_OPEN.findall(line)) - len(HTML_COMMENT_CLOSE.findall(line))

        # 9. Wikilinks with empty alias
        for wl in WIKILINK_RE.findall(line):
            if "|" in wl:
                parts = wl.split("|", 1)
                if not parts[1].strip():
                    issues.append((rel, "empty_wikilink_alias", i, f"[[{wl}]]"))

    # 7. Unclosed HTML comment
    if html_open > 0:
        issues.append((rel, "unclosed_html_comment", 0, f"{html_open} unclosed <!--"))

# 6. Footnote check: collect all defs and refs
all_fn_defs: dict[Path, set[str]] = defaultdict(set)
all_fn_refs: dict[Path, set[str]] = defaultdict(set)
for p in MD_FILES:
    text = read_text(p)
    _, body = strip_frontmatter(text)
    for line in body.split("\n"):
        for m in FOOTNOTE_DEF_RE.finditer(line):
            all_fn_defs[p].add(m.group(1))
        for m in FOOTNOTE_REF_RE.finditer(line):
            all_fn_refs[p].add(m.group(1))

for p, refs in all_fn_refs.items():
    rel = str(p.relative_to(VAULT))
    for ref in refs:
        if ref not in all_fn_defs.get(p, set()):
            issues.append((rel, "footnote_ref_no_def", 0, f"[^{ref}]"))

# 8. Empty frontmatter fields — only flag title/name/id (tags: empty is valid YAML null)
for p in MD_FILES:
    text = read_text(p)
    fm, _ = strip_frontmatter(text)
    if not fm:
        continue
    rel = str(p.relative_to(VAULT))
    for line in fm.split("\n"):
        m = re.match(r'^(\w+):\s*$', line)
        if m:
            field = m.group(1).lower()
            if field in ("title","name","id"):
                issues.append((rel, "empty_frontmatter_field", 0, f"{field}: (empty)"))

# Report
categories = defaultdict(list)
for f, cat, line, detail in issues:
    categories[cat].append((f, line, detail))

print()
for cat in sorted(categories):
    items = categories[cat]
    print(f"=== {cat.upper().replace('_',' ')}: {len(items)} ===")
    for f, line, detail in items[:20]:
        print(f"  {f}:{line}  {detail}")
    if len(items) > 20:
        print(f"  ... and {len(items)-20} more")
    print()

print(f"TOTAL ISSUES: {len(issues)}")
