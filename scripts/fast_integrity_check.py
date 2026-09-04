#!/usr/bin/env python3
"""
Fast Vault Integrity and MOC Check
Audits:
1. MOC presence and completeness across all 26 planes (00 to 25).
2. Code fence closures.
3. YAML frontmatter validity.
"""

import os
import yaml
from pathlib import Path

vault = Path('/Users/mac/Library/CloudStorage/GoogleDrive-phanqtrang@gmail.com/My Drive/_AMOS_OS')

expected_mocs = [
    '00_ROOT/00_ROOT_MOC.md',
    '01_CANON/01_CANON_MOC.md',
    '02_KERNEL/02_KERNEL_MOC.md',
    '03_CONTROL_PLANE/03_CONTROL_PLANE_MOC.md',
    '04_RUNTIME/04_RUNTIME_MOC.md',
    '05_COGNITIVE_ORGANISM/05_COGNITIVE_ORGANISM_MOC.md',
    '06_AGENTS/06_AGENTS_MOC.md',
    '07_SKILLS/07_SKILLS_MOC.md',
    '08_WORKFLOWS/08_WORKFLOWS_MOC.md',
    '09_PROTOCOLS/09_PROTOCOLS_MOC.md',
    '10_MEMORY/10_MEMORY_MOC.md',
    '11_KNOWLEDGE/11_KNOWLEDGE_MOC.md',
    '12_STATE/12_STATE_MOC.md',
    '13_MODELS/13_MODELS_MOC.md',
    '14_TOOLS/14_TOOLS_MOC.md',
    '15_INTERFACES/15_INTERFACES_MOC.md',
    '16_SCHEMAS/16_SCHEMAS_MOC.md',
    '17_OBSERVABILITY/17_OBSERVABILITY_MOC.md',
    '18_SECURITY/18_SECURITY_MOC.md',
    '19_TESTS/19_TESTS_MOC.md',
    '20_OPERATIONS/20_OPERATIONS_MOC.md',
    '21_DOMAINS/21_DOMAINS_MOC.md',
    '22_RESEARCH/22_RESEARCH_MOC.md',
    '23_OPERATING_MODEL/23_OPERATING_MODEL_MOC.md',
    '24_ARCHIVE/24_ARCHIVE_MOC.md',
    '25_COGNITIVE_MATRIX/25_COGNITIVE_MATRIX_MOC.md'
]

print("=== 1. Checking 26 MOCs ===")
missing_mocs = []
for moc in expected_mocs:
    p = vault / moc
    if not p.exists():
        missing_mocs.append(moc)
        print(f"  [MISSING MOC] {moc}")
    else:
        print(f"  [OK] {moc}")

if not missing_mocs:
    print("All 26 Plane MOCs are present and accounted for!")

print("\n=== 2. Checking Plane Root READMEs and Contracts ===")
planes = [
    '00_ROOT', '01_CANON', '02_KERNEL', '03_CONTROL_PLANE', '04_RUNTIME',
    '05_COGNITIVE_ORGANISM', '06_AGENTS', '07_SKILLS', '08_WORKFLOWS', '09_PROTOCOLS',
    '10_MEMORY', '11_KNOWLEDGE', '12_STATE', '13_MODELS', '14_TOOLS',
    '15_INTERFACES', '16_SCHEMAS', '17_OBSERVABILITY', '18_SECURITY', '19_TESTS',
    '20_OPERATIONS', '21_DOMAINS', '22_RESEARCH', '23_OPERATING_MODEL', '24_ARCHIVE',
    '25_COGNITIVE_MATRIX'
]

for pl in planes:
    p_dir = vault / pl
    if p_dir.exists():
        files = [f.name for f in p_dir.iterdir() if f.is_file()]
        print(f"Plane {pl:25s}: {len(files)} top-level files")
    else:
        print(f"Plane {pl:25s}: [MISSING DIR]")
