#!/usr/bin/env python3
"""
Add 'Do not use' sections to .devin/skills/ SKILL.md files that are missing them.
The content is generated based on the skill's domain and description.
"""

import os
import re

VAULT_ROOT = "/Users/mac/Documents/AMOS_OS"
SKILLS_DIR = os.path.join(VAULT_ROOT, ".devin", "skills")

# Domain → "Do not use" content mapping
DOMAIN_DO_NOT_USE = {
    "canon": [
        "For generic structural analysis outside the canon framework",
        "To claim empirical validation of consciousness or civilization theories",
        "As a substitute for domain-specific historical or scientific evidence",
        "Outside canon/universe domain reasoning",
    ],
    "formal": [
        "For generic mathematical analysis outside the formal verification framework",
        "To claim physical quantum mechanics predictions (AMOS_MODEL only)",
        "As a substitute for domain-specific numerical or optimization evidence",
        "Outside formal/math domain reasoning",
    ],
    "fx": [
        "For generic financial analysis outside the forex/engine framework",
        "To claim empirical validation of market efficiency or pricing models",
        "As a substitute for domain-specific financial or economic evidence",
        "Outside forex/finance domain reasoning",
    ],
    "econ": [
        "For generic economic analysis outside the econ/finance framework",
        "To claim empirical validation of economic laws or market dynamics",
        "As a substitute for domain-specific economic or financial evidence",
        "Outside econ/finance domain reasoning",
    ],
    "c04": [
        "For generic biological analysis outside the bio/neuro framework",
        "To claim empirical validation of biological intelligence laws",
        "As a substitute for domain-specific medical or neuroscience evidence",
        "Outside biology/neuroscience domain reasoning",
    ],
    "bio": [
        "For generic biological analysis outside the bio/neuro framework",
        "To claim empirical validation of biological intelligence laws",
        "As a substitute for domain-specific medical or neuroscience evidence",
        "Outside biology/neuroscience domain reasoning",
    ],
    "c05": [
        "For generic psychological analysis outside the mind/behavior framework",
        "To claim empirical validation of consciousness or cognitive theories",
        "As a substitute for domain-specific psychological or psychiatric evidence",
        "Outside mind/behavior domain reasoning",
    ],
    "c06": [
        "For generic social analysis outside the society/culture framework",
        "To claim empirical validation of civilizational survival laws",
        "As a substitute for domain-specific historical or anthropological evidence",
        "Outside society/culture domain reasoning",
    ],
    "society": [
        "For generic social analysis outside the society/culture framework",
        "To claim empirical validation of civilizational survival laws",
        "As a substitute for domain-specific historical or anthropological evidence",
        "Outside society/culture domain reasoning",
    ],
    "c07": [
        "For generic financial analysis outside the econ/finance framework",
        "To claim empirical validation of economic laws or market dynamics",
        "As a substitute for domain-specific financial or economic evidence",
        "Outside econ/finance domain reasoning",
    ],
    "c08": [
        "For generic strategic analysis outside the strategy/game framework",
        "To claim empirical validation of evolutionary cycle laws",
        "As a substitute for domain-specific market or competitive evidence",
        "Outside strategy/game domain reasoning",
    ],
    "strategy": [
        "For generic strategic analysis outside the strategy/game framework",
        "To claim empirical validation of evolutionary cycle laws",
        "As a substitute for domain-specific market or competitive evidence",
        "Outside strategy/game domain reasoning",
    ],
    "mckinsey": [
        "For generic business analysis outside the McKinsey framework",
        "To claim empirical validation of consulting methodologies",
        "As a substitute for domain-specific industry or market evidence",
        "Outside McKinsey/strategy domain reasoning",
    ],
    "c09": [
        "For generic governance analysis outside the org/law/policy framework",
        "To claim empirical validation of governance or legal theories",
        "As a substitute for domain-specific legal or compliance evidence",
        "Outside org/law/policy domain reasoning",
    ],
    "c10": [
        "For generic engineering analysis outside the tech/engineering framework",
        "To claim empirical validation of software engineering laws",
        "As a substitute for domain-specific technical or engineering evidence",
        "Outside tech/engineering domain reasoning",
    ],
    "c11": [
        "For generic design analysis outside the design/language framework",
        "To claim empirical validation of aesthetic or linguistic theories",
        "As a substitute for domain-specific design or language evidence",
        "Outside design/language domain reasoning",
    ],
    "c12": [
        "For generic environmental analysis outside the earth/ecology framework",
        "To claim empirical validation of climate or ecological theories",
        "As a substitute for domain-specific environmental or energy evidence",
        "Outside earth/ecology domain reasoning",
    ],
    "c01": [
        "For generic logic analysis outside the meta-logic framework",
        "To claim empirical validation of logical laws",
        "As a substitute for domain-specific mathematical or logical evidence",
        "Outside meta-logic domain reasoning",
    ],
    "c02": [
        "For generic mathematical analysis outside the math/compute framework",
        "To claim empirical validation of computational complexity laws",
        "As a substitute for domain-specific mathematical or computational evidence",
        "Outside math/compute domain reasoning",
    ],
    "c03": [
        "For generic physics analysis outside the physics/cosmos framework",
        "To claim empirical validation of physical theories (AMOS_MODEL only)",
        "As a substitute for domain-specific physics or cosmological evidence",
        "Outside physics/cosmos domain reasoning",
    ],
    "arxiv": [
        "For generic document conversion outside arXiv/RSCF framework",
        "To alter or fabricate scientific claims (source-faithful only)",
        "As a substitute for domain-specific peer review or validation",
        "Outside knowledge research domain reasoning",
    ],
    "knowledge": [
        "For generic knowledge management outside the AMOS knowledge framework",
        "To claim empirical validation of knowledge representation theories",
        "As a substitute for domain-specific research or curatorial evidence",
        "Outside knowledge research domain reasoning",
    ],
    "agent": [
        "For generic agent fabrication outside the AMOS agent framework",
        "To claim empirical validation of multi-agent theories",
        "As a substitute for domain-specific agent design or delegation evidence",
        "Outside agent systems domain reasoning",
    ],
    "memory": [
        "For generic memory analysis outside the AMOS memory framework",
        "To claim empirical validation of memory consolidation theories",
        "As a substitute for domain-specific memory or context evidence",
        "Outside memory systems domain reasoning",
    ],
    "runtime": [
        "For generic runtime analysis outside the AMOS OS/runtime framework",
        "To claim empirical validation of OS or runtime theories",
        "As a substitute for domain-specific runtime or infrastructure evidence",
        "Outside runtime/OS domain reasoning",
    ],
    "boundary": [
        "For generic scope analysis outside the boundary/scope framework",
        "To claim empirical validation of context continuity theories",
        "As a substitute for domain-specific scope or boundary evidence",
        "Outside boundary/scope domain reasoning",
    ],
    "audit": [
        "For generic audit analysis outside the AMOS audit/repair framework",
        "To claim empirical validation of repair or recovery theories",
        "As a substitute for domain-specific audit or quality evidence",
        "Outside audit/repair domain reasoning",
    ],
    "security": [
        "For generic security analysis outside the AMOS security framework",
        "To claim empirical validation of adversarial defense theories",
        "As a substitute for domain-specific security or safety evidence",
        "Outside security/safety domain reasoning",
    ],
    "info": [
        "For generic information analysis outside the information theory framework",
        "To claim empirical validation of entropy or complexity theories",
        "As a substitute for domain-specific information or complexity evidence",
        "Outside information theory domain reasoning",
    ],
    "fractal": [
        "For generic fractal analysis outside the fractal systems framework",
        "To claim empirical validation of self-similarity or scale theories",
        "As a substitute for domain-specific fractal or scale evidence",
        "Outside fractal systems domain reasoning",
    ],
    "trang": [
        "For generic reality analysis outside the Trang framework",
        "To claim empirical validation of cascade or collapse theories",
        "As a substitute for domain-specific reality or ontology evidence",
        "Outside Trang framework domain reasoning",
    ],
    "rscf": [
        "For generic epistemic analysis outside the RSCF framework",
        "To claim empirical validation of epistemic classification theories",
        "As a substitute for domain-specific evidence or provenance validation",
        "Outside RSCF epistemic domain reasoning",
    ],
    "causal": [
        "For generic causal analysis outside the AMOS causal framework",
        "To claim empirical validation of causal closure or hierarchy theories",
        "As a substitute for domain-specific causal or counterfactual evidence",
        "Outside causal reasoning domain reasoning",
    ],
    "super": [
        "For generic consciousness analysis outside the super-engine framework",
        "To claim empirical validation of consciousness or mega-engine theories",
        "As a substitute for domain-specific cognitive or consciousness evidence",
        "Outside super-engine domain reasoning",
    ],
}

def get_domain(filepath):
    """Extract domain from frontmatter."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read(2000)  # Read first 2000 chars for frontmatter
    m = re.search(r'^domain:\s*(\S+)', content, re.MULTILINE)
    if m:
        return m.group(1).strip().strip('"').strip("'")
    return None

def get_skill_name(filepath):
    """Extract skill name from frontmatter."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read(2000)
    m = re.search(r'^name:\s*(\S+)', content, re.MULTILINE)
    if m:
        return m.group(1).strip().strip('"').strip("'")
    return None

def has_do_not_use(filepath):
    """Check if file already has 'Do not use' section."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    return '## Do not use' in content

def add_do_not_use(filepath, domain):
    """Add 'Do not use' section to end of file."""
    items = DOMAIN_DO_NOT_USE.get(domain)
    if not items:
        # Default for unknown domains
        items = [
            f"For generic analysis outside the {domain} framework",
            "To claim empirical validation without domain-specific evidence",
            "As a substitute for domain-specific evidence",
            f"Outside {domain} domain reasoning",
        ]
    
    section = "\n## Do not use\n\n"
    for item in items:
        section += f"- {item}\n"
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Add to end of file, ensuring there's a blank line before
    if not content.endswith('\n'):
        content += '\n'
    if not content.endswith('\n\n'):
        content += '\n'
    
    content += section
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

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
        
        if has_do_not_use(skill_md):
            skipped += 1
            continue
        
        domain = get_domain(skill_md)
        if not domain:
            print(f"  SKIP (no domain): {skill_name}")
            skipped += 1
            continue
        
        try:
            add_do_not_use(skill_md, domain)
            fixed_count += 1
        except Exception as e:
            print(f"  ERROR: {skill_name}: {e}")
            errors += 1
    
    print(f"\nDone. Added 'Do not use' to {fixed_count} skills. Skipped {skipped}. Errors: {errors}.")
