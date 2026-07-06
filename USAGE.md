# Growth model: keep everything, prune by usage

We do not know yet what works. So we keep all 65 books in full, and we let real
research carve the brain over time. This is the opposite of guessing up front
which books matter. Nothing is pruned by opinion. Things are pruned by evidence
of disuse.

## The rule

1. Start with everything. All 65 full texts are loaded and available. No book
   is privileged, no book is a stub. Flat weight.
2. Use the brain in real work. Each time a card, a book, or a chain actually
   fires and helps, that is a signal it earns its keep.
3. Over time, what never fires gets a hard look. We prune only what usage shows
   we do not need, and only after it has had a fair chance to fire.
4. We never prune to look tidy. A rarely-used book that lands one decisive
   cross-domain insight is worth more than a tidy index.

## Why keep the full text and not just the cards

A summary pre-decides what matters. The card is a map; the full book is the
territory. When a task pulls a book, it pulls the full text, because the part
that helps may be the part no summary kept. We only trust a distillation after
the full context has proven which parts were the load-bearing ones.

## The log (fill in with use)

Track what actually fires. Start empty; let it fill from real sessions.

| date | task | books that fired | cross-domain lift seen | keep / watch |
|------|------|------------------|------------------------|--------------|
| 2026-06-19 | cat-agent-platforms assessment (Shodan -> verify 61 unauth agent hosts) | 02 (philosophy: falsify auth-on-default), 07 (drawing: trained observation -> niche-marker selection over generic dorks), 42 (zero-day: tool-arg-as-sink framing of the loot column / git-diff CVE), 39 (agentic: Sense-Reason-Plan-Act-Memory was literally the target architecture, shaped the /api/settings + memory-read probe plan) | 07->recon: "recon is trained observation" turned a generic title dork into a conjunctive data-layer matcher that refuted 71 catch-all 200s + 3 scanner FPs. 02->severity: refusing to assume PATCHED when the version oracle is the exploit sink itself (indeterminate-by-design, Insight C3). | keep all 4 |
| 2026-06-19 | 101.200.124.170:3000 leaked-upstream LLM-gateway finding (8-lobe brain brew, no probe) | 39 (Agent Router + Tool Registry = the gateway; Execution-Envelope absence = confused deputy), 42 (sink-to-source: connect(.210,11434) sink already firing, source=channel base_url write gated on admin-claim), 24 (control boundary misplaced; lineage-exposure; remediation-for-class), 44 (dual /v1 + /api/* surface; /api/pull = outbound-fetch+disk-write sink), 35 (Aliyun IMDS 100.100.100.200 RAM/STS via SSRF-shaped channel write), 28 (honeypot gate: inference-timing-vs-canned + dual-surface + console-fingerprint discriminators), 02 (CIA-before-adjective; tram lateral-movement test; MEDIUM not critical), 07 (DISTANT primer: block-in -> measured-vs-constructed line of termination) | 07->severity: drawing's line of termination forced an explicit measured(3 edges)-vs-constructed(pivot) partition a pure security frame skips, and gave light-line/dark-line as a literal restraint stage-gate. 03 folded into 02 resolved the likelihood term: default-root-token = forgeable seed = the only control silently no-ops. 44+41: the /v1 facade is a thin skin over Ollama /api/* where /api/pull is a write primitive. | keep all 8 |

| 2026-06-19 | cat-agent-platforms ROUND-2 re-harvest: 5 Shodan-dark platforms re-attacked with primary-source markers (workflow ww0qggyxp derive+refute -> harvest -> wx27niuhh verify). Yield: Letta is NOT dark-by-bind (docker 0.0.0.0:8283); banner-dark-by-construction = Insight C5; +1 AutoGen confirmed (47.109.195.240, auth-off A1); 17 MetaGPT committed-key repos | 07 (drawing: trained observation -> engineer vendor-unique JSON markers from repo HEAD, not freetext; the "marker was wrong, not the population" call), 44 (protocol decomposition: /info vs /openapi.json vs /features fetch-model analysis is WHY Shodan can't see them), 28 (honeypot: the negative-control path became BOTH the AutoGen catch-all discriminator AND the MetaGPT config2.example.yaml placeholder gate), 02 (proportion: adversarially refute the dorks before harvest + REFUSE to codify 5 agent-claimed unverified CVE IDs into the canonical tome) | 07->method: re-running card-07 on a round-1 "Shodan-dark" result reframed a per-platform footnote (localhost bind) into a category structural law (banner-dark by crawler fetch-model). 28->two domains: one discriminator shape (positive marker + control that must NOT echo) served an HTTP catch-all AND a git-commit placeholder echo identically. 02->corpus integrity: skepticism kept unverified CVE numbers out of the tome. | keep 07 44 28 02 |

When a book sits in "watch" across many sessions with no fire, raise it for a
pruning decision. Until then, it stays. Right now, everything stays.

## Corpus growth

| date | event | books | note |
|------|-------|-------|------|
| 2026-06-19 | +9 via `chainsaw add` (elhacker.info source) | 46-54 | Shodan (Matherly), OSINT (Bazzell 11e), Pentesting APIs/Cloud, RE for Beginners (Yurichev), Physical Fault Injection + Side-Channel, Cyberjutsu (McCarty), Practical Malware Analysis (Sikorski), The IDA Pro Book, Hacking: The Art of Exploitation 2e. Distilled by a 9-agent workflow; offensive +7, defensive +2. New books start COLD (unfired); prune-by-usage applies only after a fair chance to fire. |
| 2026-07-05 | +11 via `chainsaw add` (O'Reilly, authed Playwright files-API extraction) | 55-65 | New 7th lobe **bio-compute**: Bioinformatics/Managing Scientific Data (Lacroix), Protein Bioinformatics AI Methods, Introduction to Biological Networks, Biological Computation (Lamm/Unger), Programming Massively Parallel Processors 4e (Hwu/Kirk), Emerging Trends in Computational Biology (BIOCOMP), Computational Intelligence & Pattern Analysis in Bio-Informatics, Meta-heuristic & Evolutionary Algorithms for Engineering Optimization, Structural Bioinformatics with Chimera (Burkowski), Evolutionary Computation with BBO (Ma/Simon), Bio-Inspired Optimization for Medical Data Mining. ~9.07M chars full text, zero fetch errors. Distilled by an 11-agent workflow; 133 cross-lobe synapses added reciprocally (heaviest: every stochastic optimizer to #03 The Art of Randomness). New books start COLD; prune-by-usage applies only after a fair chance to fire. |
