#!/usr/bin/env python3
import os
import json
import re
from pathlib import Path

arxiv_vault = Path('/Users/mac/Desktop/_Arxiv/Arvix')
docs_vault = Path('/Users/mac/Documents/AMOS_OS')

def scan_vault(v_path, name):
    print(f"=== Scanning {name} ({v_path}) ===")
    if not v_path.is_dir():
        print("Directory does not exist!")
        return
    
    total_md = 0
    total_json = 0
    empty_files = []
    unclosed_fences = []
    malformed_frontmatter = []
    raw_markdown_papers = 0
    rscf_normalized_papers = 0
    broken_json = []
    
    for root, dirs, files in os.walk(v_path):
        rel_parts = Path(root).relative_to(v_path).parts
        if any(p.startswith('.') or p.startswith('.tagmigrate') or p == 'node_modules' for p in rel_parts):
            continue
        for fn in files:
            p = Path(root) / fn
            rel_p = str(p.relative_to(v_path))
            if fn.endswith('.md'):
                total_md += 1
                try:
                    content = p.read_text(encoding='utf-8')
                except Exception as e:
                    malformed_frontmatter.append((rel_p, f"Read error: {e}"))
                    continue
                
                if len(content.strip()) == 0:
                    empty_files.append(rel_p)
                    continue
                
                # Check RSCF vs raw
                if 'schema_family: RSCF' in content or 'schema_role: KNOWLEDGE_RSCF' in content:
                    rscf_normalized_papers += 1
                elif fn[0:4].isdigit() and ('.' in fn[0:9] or 'v' in fn[0:9]):
                    raw_markdown_papers += 1
                
                # Check frontmatter
                if content.startswith('---'):
                    parts = content.split('---', 2)
                    if len(parts) < 3:
                        malformed_frontmatter.append((rel_p, "Unterminated frontmatter"))
                
                # Check code fences
                lines = content.splitlines()
                in_code = False
                for line in lines:
                    if line.strip().startswith('```'):
                        in_code = not in_code
                if in_code:
                    unclosed_fences.append(rel_p)
            elif fn.endswith('.json'):
                total_json += 1
                try:
                    with open(p, 'r', encoding='utf-8') as fp:
                        json.load(fp)
                except Exception as e:
                    broken_json.append((rel_p, str(e)))

    print(f"Total MD files: {total_md}")
    print(f"Total JSON files: {total_json}")
    print(f"Empty files: {len(empty_files)}")
    print(f"Unclosed code fences: {len(unclosed_fences)}")
    print(f"Malformed frontmatter: {len(malformed_frontmatter)}")
    print(f"Broken JSON: {len(broken_json)}")
    if 'Arxiv' in name:
        print(f"RSCF Normalized Papers: {rscf_normalized_papers}")
        print(f"Raw Markdown Papers: {raw_markdown_papers}")
    for u in unclosed_fences[:10]:
        print(f"  Unclosed fence: {u}")
    for m in malformed_frontmatter[:5]:
        print(f"  Malformed FM: {m}")
    for e in empty_files[:5]:
        print(f"  Empty file: {e}")

scan_vault(arxiv_vault, 'ArXiv Research Vault')
print()
scan_vault(docs_vault, 'Local Documents AMOS Vault')
