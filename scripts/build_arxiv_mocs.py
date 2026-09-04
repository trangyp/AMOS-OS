#!/usr/bin/env python3
"""
build_arxiv_mocs.py
Generates canonical AMOS Year MOCs (Maps of Content) for all years in the ArXiv Vault
(/Users/mac/Desktop/_Arxiv/Arvix) and links them into ARXIV_RSCF_KNOWLEDGE_NODE.md.
"""

import os
from pathlib import Path

VAULT_PATH = Path('/Users/mac/Desktop/_Arxiv/Arvix')
ROOT_NODE = VAULT_PATH / 'ARXIV_RSCF_KNOWLEDGE_NODE.md'

def generate_moc_for_year(year_dir: Path):
    year_str = year_dir.name
    moc_file = year_dir / f"MOC_{year_str}.md"
    
    # Collect all markdown files in year_dir excluding existing MOC files
    md_files = []
    for f in sorted(year_dir.rglob('*.md')):
        if f.name.startswith('MOC_') or f.name == 'MOC.md':
            continue
        # Relative path within year directory or vault
        rel_to_vault = f.relative_to(VAULT_PATH)
        # Clean title from stem
        stem = f.stem
        md_files.append((stem, f.name, str(rel_to_vault)))
    
    total_papers = len(md_files)
    
    # Create MOC content
    content_lines = [
        "---",
        f"title: {year_str} MOC",
        "type: knowledge-compendium",
        f"source: 11_KNOWLEDGE/_arxiv_md/{year_str}",
        f"artifact_id: AMOS-KNOWLEDGE-MOC-{year_str}-MASTER",
        f"canonical_name: MOC_{year_str}",
        "status: CANONICAL",
        "conclusion_class: CANONICAL",
        "amos_core_target: v4.4",
        "origin_architect: Trang Phan",
        "steward: Trang Phan",
        "version: 2.0.0",
        "created: '2026-09-03'",
        "updated: '2026-09-03'",
        "plane: 11_KNOWLEDGE",
        "domain: knowledge-base",
        "tags:",
        "  - amos-os",
        "  - knowledge-compendium",
        "  - knowledge-base",
        "  - domain-mastery",
        "  - rscf/claim",
        "  - rscf/state/canonical",
        "  - 00-home",
        "  - 00-root-moc",
        "  - 11-knowledge-moc",
        "aliases:",
        f"  - {year_str} MOC",
        f"  - MOC_{year_str}",
        "---",
        "",
        f"# {year_str} MOC — ArXiv Research Corpus",
        "",
        f"> **Kiến trúc sư trưởng:** Trang Phan & Hệ thống AMOS OS  ",
        f"> **Plane:** `11_KNOWLEDGE/_arxiv_md/{year_str}/MOC_{year_str}.md`  ",
        f"> **Trạng thái:** `CANONICAL` (Kho Tri Thức Chuẩn Tắc Toàn Hệ Thống)  ",
        f"> **Tổng số công trình nghiên cứu:** {total_papers}  ",
        "",
        "---",
        "",
        "## Điều Hướng Hệ Thống",
        "- [[ARXIV_RSCF_KNOWLEDGE_NODE|ArXiv Corpus Root Knowledge Node]]",
        "",
        f"## Danh Mục Công Trình Nghiên Cứu {year_str}",
        ""
    ]
    
    # Organize papers: if there are subdirectories (months), group them
    subdirs = sorted([d for d in year_dir.iterdir() if d.is_dir() and not d.name.startswith('.')])
    if subdirs:
        for sdir in subdirs:
            s_files = [f for f in sorted(sdir.rglob('*.md')) if not f.name.startswith('MOC')]
            if not s_files:
                continue
            content_lines.append(f"### Phân đoạn {sdir.name} ({len(s_files)} papers)")
            for sf in s_files:
                content_lines.append(f"- [[{sf.stem}|{sf.stem.replace('_', ' ')}]]")
            content_lines.append("")
    else:
        for stem, name, rel in md_files:
            content_lines.append(f"- [[{stem}|{stem.replace('_', ' ')}]]")
        content_lines.append("")
        
    content_lines.extend([
        "---",
        "RSCF-NODE",
        f"node_id: arxiv-moc-{year_str}",
        "node_type: moc",
        "domain: KNOWLEDGE",
        f"path: {year_str}/MOC_{year_str}.md",
        "RSCF-RELATIONS:",
        "  - PARENT_OF: [[ARXIV_RSCF_KNOWLEDGE_NODE]]"
    ])
    for stem, _, _ in md_files[:20]: # Link top 20 direct relations in RSCF frontmatter
        content_lines.append(f"  - CONTAINS_PAPER: [[{stem}]]")
    content_lines.append("claim_class: AMOS_MODEL")
    content_lines.append("")
    
    moc_file.write_text("\n".join(content_lines), encoding="utf-8")
    print(f"Generated MOC for {year_str} ({total_papers} papers) -> {moc_file.name}")

def update_root_node(years):
    lines = [
        "---",
        'title: "Arvix ArXiv Article Corpus — AMOS-RSCF Knowledge Node"',
        "type: knowledge",
        "source: .",
        "tags:",
        "  - arxiv",
        "  - rscf",
        "  - amos/knowledge",
        "  - vault",
        "---",
        "",
        "# Arvix ArXiv Article Corpus — AMOS-RSCF Knowledge Node",
        "",
        "## Summary",
        "",
        "This node represents the full Arvix vault: 66,067 arXiv article notes, one file per paper, organized by year from 2007 through 2026, plus a `misc/` directory. Each note is ingested as a source-candidate evidence record and is available for AMOS RSCF linkage.",
        "",
        "## Year Maps of Content (MOCs)",
        ""
    ]
    
    for y in years:
        lines.append(f"- [[MOC_{y}|MOC {y} — ArXiv {y} Research Corpus]]")
        
    lines.extend([
        "",
        "## Scope",
        "",
        "- Years: 2007–2026",
        "- Total notes: 66,067",
        "- Path: `.`",
        "",
        "---",
        "RSCF-NODE",
        "node_id: arvix-corpus-rscf-knowledge-node",
        "node_type: knowledge",
        "domain: KNOWLEDGE",
        "path: ARXIV_RSCF_KNOWLEDGE_NODE.md",
        "RSCF-RELATIONS:"
    ])
    
    for y in years:
        lines.append(f"- RELATED_TO: [[MOC_{y}]]")
        
    lines.append("claim_class: AMOS_MODEL")
    lines.append("")
    
    ROOT_NODE.write_text("\n".join(lines), encoding="utf-8")
    print(f"Updated root node {ROOT_NODE} with {len(years)} Year MOC links.")

def main():
    years = [p for p in sorted(VAULT_PATH.iterdir()) if p.is_dir() and not p.name.startswith('.') and (p.name.isdigit() or p.name == 'misc')]
    year_names = []
    for y in years:
        generate_moc_for_year(y)
        year_names.append(y.name)
    update_root_node(year_names)
    print(f"Successfully processed all {len(years)} years.")

if __name__ == "__main__":
    main()
