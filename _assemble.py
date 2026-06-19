#!/usr/bin/env python3
# Assemble the chainsaw brain from the distillation workflow's result JSON.
# Usage: python3 _assemble.py <task-output-file>
# Writes: brain/cards/NN_isbn.md (x45), brain/lobes/<key>.md (x6),
#         FRAMEWORK.md, brain/INDEX.md
import sys, os, json, re

ROOT = '/home/cowboy/chainsaw'
CARDS = os.path.join(ROOT, 'brain', 'cards')
LOBESD = os.path.join(ROOT, 'brain', 'lobes')
os.makedirs(CARDS, exist_ok=True)
os.makedirs(LOBESD, exist_ok=True)

def em(s):
    if not isinstance(s, str):
        return s
    return s.replace('—', '-').replace('–', '-')

def emlist(xs):
    return [em(x) for x in xs] if isinstance(xs, list) else []

# ---- load result JSON robustly ----
raw = open(sys.argv[1], encoding='utf-8').read()
try:
    data = json.loads(raw)
except Exception:
    i = raw.find('{')
    data, _ = json.JSONDecoder().raw_decode(raw[i:])
# unwrap if nested under result
if 'cards' not in data and isinstance(data.get('result'), dict):
    data = data['result']

cards = data.get('cards') or []
lobes = data.get('lobes') or []
framework = data.get('framework') or ''

LOBE_NAME = {
    'offensive': 'Offensive', 'defensive': 'Defensive', 'ai-agentic': 'AI and Agentic',
    'craft-code': 'Craft and Code', 'human': 'Human and Influence', 'philosophy': 'Philosophy',
}
LOBE_ORDER = ['offensive','defensive','ai-agentic','craft-code','human','philosophy']
LOBE_LOAD_WHEN = {
    'offensive':  'finding or proving an exploitable path: code review, reverse engineering, fuzzing, web/crypto/cloud/network/privesc',
    'defensive':  'building visibility, resilience, ICS/OT and IoT defense, deception, or securing AI; thinking like the operator',
    'ai-agentic': 'building, grounding, governing, or securing AI/agentic systems; fairness, randomness, NLP',
    'craft-code': 'the maker eye: trained observation, readable code, visual craft, tooling foundations',
    'human':      'reading, persuading, leading, or connecting with people; social engineering; report and disclosure',
    'philosophy': 'proportion and skepticism: deciding what matters and how to think about it',
}

cards = [c for c in cards if isinstance(c, dict) and c.get('n')]
cards.sort(key=lambda c: c['n'])

def card_md(c):
    n = c['n']; isbn = c.get('isbn',''); title = em(c.get('title','')); lobe = c.get('lobe','')
    L = [f'# {n:02d}. {title}', '', f'**ISBN** {isbn}  |  **Lobe** {lobe}', '']
    if c.get('essence'):
        L += [f'> {em(c["essence"])}', '']
    sect = [
        ('Reach for this when', emlist(c.get('reach_for_when'))),
        ('Principles', emlist(c.get('principles'))),
        ('Moves', emlist(c.get('moves'))),
        ('Chains with', emlist(c.get('chains_with'))),
        ('Watch out', emlist(c.get('watch_out'))),
    ]
    for h, xs in sect:
        if xs:
            L += [f'## {h}', ''] + [f'- {x}' for x in xs] + ['']
    return '\n'.join(L).rstrip() + '\n'

written = 0
for c in cards:
    out = os.path.join(CARDS, f'{c["n"]:02d}_{c.get("isbn","x")}.md')
    open(out, 'w', encoding='utf-8').write(card_md(c))
    written += 1

# ---- lobe doctrines ----
lw = 0
for l in lobes:
    key = l.get('key'); md = em(l.get('md') or '')
    if not key or not md:
        continue
    open(os.path.join(LOBESD, f'{key}.md'), 'w', encoding='utf-8').write(md.rstrip() + '\n')
    lw += 1

# ---- framework ----
if framework:
    open(os.path.join(ROOT, 'FRAMEWORK.md'), 'w', encoding='utf-8').write(em(framework).rstrip() + '\n')

# ---- chain map (flat mesh) from chains_with leading integers ----
adj = {c['n']: set() for c in cards}
titles = {c['n']: em(c.get('title','')) for c in cards}
lobeof = {c['n']: c.get('lobe','') for c in cards}
for c in cards:
    for ch in (c.get('chains_with') or []):
        m = re.match(r'\s*(\d{1,2})\b', str(ch))
        if m:
            t = int(m.group(1))
            if t in adj and t != c['n']:
                adj[c['n']].add(t)
# undirected degree (mesh connectivity)
undirected = {n: set(adj[n]) for n in adj}
for n in adj:
    for t in adj[n]:
        undirected.setdefault(t, set()).add(n)
linked = sum(1 for n in undirected if undirected[n])

# ---- INDEX.md ----
I = ['# Chainsaw index', '',
     'The router. Match a task to its lobe by signal, load that lobe and its named cards, then follow the chain map across lobes. The framework is always-on; this index just points.', '',
     '## Route by signal', '']
for k in LOBE_ORDER:
    ns = [c['n'] for c in cards if c.get('lobe') == k]
    if not ns:
        continue
    I.append(f'- **{LOBE_NAME[k]}** ({len(ns)}) -> load when {LOBE_LOAD_WHEN[k]}.')
    I.append(f'  cards: {" ".join(f"{x:02d}" for x in sorted(ns))}')
I += ['', '## Flat weight', '',
      'Every card carries the same weight. The lobes differ in size because domains differ in size, not in importance. Load by what the task and its chains call for, never by rank.', '',
      '## Chain map (the synapses)', '',
      f'{linked} of {len(cards)} books are wired to at least one other. Follow these links across lobe boundaries; that crossing is where the brain thinks.', '']
for c in cards:
    n = c['n']
    outs = sorted(undirected.get(n, set()))
    if outs:
        I.append(f'- **{n:02d}** {titles[n]} [{lobeof[n]}] <-> {" ".join(f"{x:02d}" for x in outs)}')
open(os.path.join(ROOT, 'brain', 'INDEX.md'), 'w', encoding='utf-8').write('\n'.join(I).rstrip() + '\n')

print(f'cards written : {written}/{len(cards)}')
print(f'lobes written : {lw}')
print(f'framework     : {"yes" if framework else "MISSING"} ({len(framework)} chars)')
print(f'chain mesh    : {linked}/{len(cards)} books linked')
miss = [c["n"] for c in cards if not undirected.get(c["n"])]
print(f'unlinked      : {miss if miss else "none"}')
