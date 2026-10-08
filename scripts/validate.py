#!/usr/bin/env python3
"""Validate the portable skill and its public distribution boundary (stdlib only)."""
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / 'skills/aiding-academic-style'
SKILL_FILES = {
    'SKILL.md', 'agents/openai.yaml',
    'references/style-fingerprint.md', 'references/papers.md',
    'references/proposals.md', 'references/academic-reports.md',
    'references/academic-examples.md', 'references/paragraph-anatomy.md',
    'references/calibration.md', 'references/sources.md',
    'references/evaluation.md',
}
ROOT_FILES = {'README.md', 'LICENSE', '.gitignore', '.gitattributes', 'scripts/validate.py'}
ALLOWED = ROOT_FILES | {'skills/aiding-academic-style/' + p for p in SKILL_FILES}
EXCLUDED_PARTS = {'.git', '__pycache__', 'dist'}
errors = []
files = [p for p in ROOT.rglob('*') if p.is_file() and not (set(p.relative_to(ROOT).parts) & EXCLUDED_PARTS)]
actual = {p.relative_to(ROOT).as_posix() for p in files}
if actual != ALLOWED:
    errors.append(f'Unexpected/missing release files: extra={sorted(actual - ALLOWED)}, missing={sorted(ALLOWED - actual)}')

entry = (SKILL / 'SKILL.md').read_text(encoding='utf-8')
if not entry.startswith('---\n') or '\n---\n' not in entry[4:]:
    errors.append('SKILL.md needs YAML frontmatter')
else:
    frontmatter = entry.split('---', 2)[1]
    if not re.search(r'^name: aiding-academic-style$', frontmatter, re.M):
        errors.append('Unexpected skill name')
    if not re.search(r'^description: \S', frontmatter, re.M):
        errors.append('Missing skill description')

ui = (SKILL / 'agents/openai.yaml').read_text(encoding='utf-8')
if '$aiding-academic-style' not in ui:
    errors.append('UI default prompt must name the skill')

links_checked = 0
private_patterns = {
    'absolute personal filesystem path': r'(?:[A-Za-z]:[/\\](?:Users|home)[/\\]|/Users/[^/\s]+/|/home/[^/\s]+/)',
    'token-like value': r'(?:gh[pousr]_[A-Za-z0-9]{30,}|github_pat_[A-Za-z0-9_]{40,})',
    'private corpus locator': r'\bD\d{2}\s*p\d+',
}
for path in files:
    relative = path.relative_to(ROOT).as_posix()
    if path.is_symlink():
        errors.append(f'Symlink not allowed in release: {relative}')
    content = path.read_text(encoding='utf-8')
    if path.suffix != '.py':
        for label, pattern in private_patterns.items():
            if re.search(pattern, content):
                errors.append(f'{relative}: {label}')
    if path.suffix != '.md':
        continue
    for link in re.findall(r'\[[^\]]*\]\(([^)]+)\)', content):
        if '://' in link or link.startswith('#'):
            continue
        target = (path.parent / link.split('#')[0]).resolve()
        if not target.is_relative_to(ROOT) or not target.exists():
            errors.append(f'{relative}: broken or external local link {link}')
        links_checked += 1

examples = (SKILL / 'references/academic-examples.md').read_text(encoding='utf-8')
anatomy = (SKILL / 'references/paragraph-anatomy.md').read_text(encoding='utf-8')
if len(re.findall(r'^## \d+\.', examples, re.M)) != 12:
    errors.append('Expected twelve constructed academic examples')
if len(re.findall(r'^## \d+\.', anatomy, re.M)) != 6:
    errors.append('Expected six constructed paragraph analyses')

if errors:
    print('\n'.join(errors), file=sys.stderr)
    sys.exit(1)
print(f'OK: {len(files)} public files, {len(SKILL_FILES)} skill files, {links_checked} local links, 12 examples and 6 paragraph analyses.')
print('This validates packaging and content boundaries, not research claims or author-style similarity.')
