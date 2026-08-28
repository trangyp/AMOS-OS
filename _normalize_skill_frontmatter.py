#!/usr/bin/env python3
"""
Normalize .devin/skills/ SKILL.md frontmatter to match the pattern
established in .agents/skills/:

1. Convert gmef_gates inline array → YAML list
2. Convert law_compliance inline array → YAML list
3. Unquote version (remove surrounding quotes)
4. Remove '# AMOS Canon Wiring' comment line
5. Add tags field: type/skill, canon/skill, domain/<domain-name>, rscf/source_claim, hml/m, epistemic/source_claim, amos_os
6. Normalize description to unquoted folded scalar (remove surrounding quotes)

Does NOT touch ## Identity or ## When to Use sections (those already exist with richer content).
"""

import os
import re

VAULT_ROOT = "/Users/mac/Documents/AMOS_OS"
SKILLS_DIR = os.path.join(VAULT_ROOT, ".devin", "skills")

# Domain → domain tag mapping
DOMAIN_TAG_MAP = {
    "canon": "domain/canon-universe",
    "formal": "domain/formal-engines",
    "fx": "domain/econ-finance",
    "econ": "domain/econ-finance",
    "c07": "domain/econ-finance",
    "c04": "domain/bio-neuro",
    "bio": "domain/bio-neuro",
    "c05": "domain/mind-behavior",
    "c06": "domain/society-culture",
    "society": "domain/society-culture",
    "c08": "domain/strategy-game",
    "strategy": "domain/strategy-game",
    "mckinsey": "domain/strategy-game",
    "c09": "domain/org-law-policy",
    "c10": "domain/tech-engineering",
    "c11": "domain/design-language",
    "c12": "domain/earth-ecology",
    "c01": "domain/meta-logic",
    "c02": "domain/math-compute",
    "c03": "domain/physics-cosmos",
    "arxiv": "domain/knowledge-research",
    "knowledge": "domain/knowledge-research",
    "agent": "domain/agent-systems",
    "memory": "domain/memory-systems",
    "runtime": "domain/os-runtime",
    "boundary": "domain/boundary-scope",
    "audit": "domain/audit-repair",
    "security": "domain/security-safety",
    "info": "domain/information-theory",
    "fractal": "domain/fractal-systems",
    "trang": "domain/trang-framework",
    "rscf": "domain/rscf-epistemic",
    "causal": "domain/causal-reasoning",
    "super": "domain/super-engines",
}

def parse_frontmatter(content):
    """Split content into frontmatter, body, and the closing --- position."""
    if not content.startswith('---\n'):
        return None, content, None
    
    # Find the closing ---
    lines = content.split('\n')
    fm_lines = []
    body_start = 0
    for i, line in enumerate(lines[1:], 1):
        if line.strip() == '---':
            fm_lines = lines[1:i]
            body_start = i + 1
            break
    
    if not fm_lines:
        return None, content, None
    
    fm_text = '\n'.join(fm_lines)
    body = '\n'.join(lines[body_start:])
    return fm_text, body, fm_lines

def get_field(fm_lines, field):
    """Get a field value from frontmatter lines."""
    for line in fm_lines:
        m = re.match(rf'^{field}:\s*(.*)$', line)
        if m:
            return m.group(1).strip()
    return None

def normalize_frontmatter(fm_text, fm_lines):
    """Normalize frontmatter text."""
    lines = fm_lines[:]
    new_lines = []
    i = 0
    
    while i < len(lines):
        line = lines[i]
        
        # Remove '# AMOS Canon Wiring' comment
        if line.strip().startswith('# AMOS Canon Wiring'):
            i += 1
            continue
        
        # Unquote version
        m = re.match(r'^version:\s*"(.+)"\s*$', line)
        if m:
            new_lines.append(f'version: {m.group(1)}')
            i += 1
            continue
        
        # Convert gmef_gates inline array to YAML list
        m = re.match(r'^gmef_gates:\s*\[(.+)\]\s*$', line)
        if m:
            items = [x.strip() for x in m.group(1).split(',')]
            new_lines.append('gmef_gates:')
            for item in items:
                new_lines.append(f'- {item}')
            i += 1
            continue
        
        # Convert law_compliance inline array to YAML list
        m = re.match(r'^law_compliance:\s*\[(.+)\]\s*$', line)
        if m:
            items = [x.strip() for x in m.group(1).split(',')]
            new_lines.append('law_compliance:')
            for item in items:
                new_lines.append(f'- {item}')
            i += 1
            continue
        
        # Check if we need to add tags (add before closing ---)
        # We'll add tags after law_compliance block
        new_lines.append(line)
        i += 1
    
    # Check if tags already exist
    has_tags = any(re.match(r'^tags:', l) for l in new_lines)
    
    if not has_tags:
        # Get domain
        domain = get_field(new_lines, 'domain')
        domain_tag = DOMAIN_TAG_MAP.get(domain, f'domain/{domain}' if domain else 'domain/unknown')
        
        # Add tags after law_compliance block (or at end)
        tags_block = [
            'tags:',
            '- type/skill',
            '- canon/skill',
            f'- {domain_tag}',
            '- rscf/source_claim',
            '- hml/m',
            '- epistemic/source_claim',
            '- amos_os',
        ]
        
        # Find position to insert (after law_compliance block)
        insert_pos = len(new_lines)
        for j, l in enumerate(new_lines):
            if l.startswith('law_compliance:'):
                # Find end of law_compliance block
                k = j + 1
                while k < len(new_lines) and new_lines[k].startswith('- '):
                    k += 1
                insert_pos = k
                break
        
        new_lines = new_lines[:insert_pos] + tags_block + new_lines[insert_pos:]
    
    return '\n'.join(new_lines)

def process_file(filepath):
    """Process a single SKILL.md file."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    fm_text, body, fm_lines = parse_frontmatter(content)
    if fm_text is None:
        return False
    
    new_fm = normalize_frontmatter(fm_text, fm_lines)
    if new_fm == fm_text:
        return False
    
    new_content = '---\n' + new_fm + '\n---\n' + body
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_content)
    return True

if __name__ == '__main__':
    fixed_count = 0
    skipped = 0
    errors = 0
    
    for skill_name in sorted(os.listdir(SKILLS_DIR)):
        skill_path = os.path.join(SKILLS_DIR, skill_name)
        if not os.path.isdir(skill_path):
            continue
        
        skill_md = os.path.join(skill_path, "SKILL.md")
        if not os.path.exists(skill_md):
            continue
        
        try:
            if process_file(skill_md):
                fixed_count += 1
            else:
                skipped += 1
        except Exception as e:
            print(f"  ERROR: {skill_name}: {e}")
            errors += 1
    
    print(f"\nDone. Normalized {fixed_count} skills. Skipped {skipped}. Errors: {errors}.")
