#!/usr/bin/env python3
from __future__ import annotations
import argparse, json, re, subprocess, tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def frontmatter(text: str) -> dict[str, str]:
    lines = text.splitlines()
    if not lines or lines[0].strip() != '---':
        return {}
    out = {}
    for line in lines[1:]:
        if line.strip() == '---':
            break
        if line and not line[:1].isspace() and ':' in line:
            k, v = line.split(':', 1)
            out[k.strip()] = v.strip().strip('"\'')
    return out


def changed(base: str | None) -> set[str] | None:
    if not base:
        return None
    for rev in (f'origin/{base}...HEAD', f'{base}...HEAD'):
        p = subprocess.run(['git','diff','--name-only',rev], cwd=ROOT, text=True,
                           stdout=subprocess.PIPE, stderr=subprocess.DEVNULL)
        if p.returncode == 0:
            return {x for x in p.stdout.splitlines() if x}
    return None


def main_validate(base: str | None) -> int:
    ch = changed(base)
    errors, warnings = [], []
    for root_name in ('07_SKILLS', '.devin/skills'):
        root = ROOT / root_name
        if not root.exists():
            continue
        for f in root.rglob('SKILL.md'):
            rel = f.relative_to(ROOT).as_posix()
            if ch is not None and rel not in ch:
                continue
            raw = f.read_bytes()
            if raw.startswith(b'\xef\xbb\xbf'):
                errors.append((rel, 'UTF-8 BOM'))
            text = raw.decode('utf-8-sig')
            fm = frontmatter(text)
            for key in ('name', 'description'):
                if not fm.get(key):
                    errors.append((rel, f'missing {key} frontmatter'))
            if fm.get('name') and not re.fullmatch(r'[a-z0-9][a-z0-9-]*', fm['name']):
                errors.append((rel, 'skill name must be lowercase kebab-case'))
            if len(text.splitlines()) > 500:
                warnings.append((rel, 'SKILL.md exceeds 500 lines'))
    agents = ROOT / '06_AGENTS'
    if agents.exists():
        for f in agents.rglob('*.json'):
            rel = f.relative_to(ROOT).as_posix()
            try:
                data = json.loads(f.read_text(encoding='utf-8-sig'))
            except Exception as exc:
                errors.append((rel, f'invalid JSON: {exc}'))
                continue
            if ch is not None and rel not in ch:
                continue
            if not data.get('name'):
                errors.append((rel, 'agent name missing'))
            card = data.get('agent_card')
            if isinstance(card, dict) and card.get('protocol') == 'A2A-v1.0':
                warnings.append((rel, 'legacy A2A-v1.0 declaration'))
    workflows = ROOT / '.github/workflows'
    if workflows.exists():
        pat = re.compile(r'\bpython(?:3)?\s+((?:\./)?scripts/[A-Za-z0-9_./-]+\.py)\b')
        for f in workflows.glob('*.y*ml'):
            for ref in pat.findall(f.read_text(encoding='utf-8-sig')):
                ref = ref.removeprefix('./')
                if not (ROOT / ref).is_file():
                    errors.append((f.relative_to(ROOT).as_posix(), f'dead CI script reference: {ref}'))
    for path, msg in warnings:
        print(f'WARN: {path}: {msg}')
    for path, msg in errors:
        print(f'ERROR: {path}: {msg}')
    print(f'AMOS repository validation: errors={len(errors)} warnings={len(warnings)}')
    return 1 if errors else 0


def self_test() -> None:
    assert frontmatter('---\nname: demo-skill\ndescription: x\n---\n') == {'name':'demo-skill','description':'x'}
    assert frontmatter('# x') == {}
    with tempfile.TemporaryDirectory() as td:
        p = Path(td)/'x.json'; p.write_text('{"name":"x"}')
        assert json.loads(p.read_text())['name'] == 'x'
    print('amos_repo_validator self-test: PASS')


if __name__ == '__main__':
    ap = argparse.ArgumentParser()
    ap.add_argument('--base-ref')
    ap.add_argument('--self-test', action='store_true')
    a = ap.parse_args()
    if a.self_test:
        self_test(); raise SystemExit(0)
    raise SystemExit(main_validate(a.base_ref))
