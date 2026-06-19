# Growth model: keep everything, prune by usage

We do not know yet what works. So we keep all 45 books in full, and we let real
research carve the brain over time. This is the opposite of guessing up front
which books matter. Nothing is pruned by opinion. Things are pruned by evidence
of disuse.

## The rule

1. Start with everything. All 45 full texts are loaded and available. No book
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

When a book sits in "watch" across many sessions with no fire, raise it for a
pruning decision. Until then, it stays. Right now, everything stays.
