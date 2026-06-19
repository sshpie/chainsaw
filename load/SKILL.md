---
name: chainsaw
description: Load the collective brain (45 books, full text) as context for a task. Use when working on vulnerability research, tool-building, writing, leadership, design, or any task that would be sharper for cross-domain priming. Routes the task to its books via the cards, then loads the FULL TEXT of the ones it needs and brews distant parts in.
---

# Chainsaw loader

Chainsaw is a collective brain built from 45 books, read in full. The full text
of every book is the substance and lives in `books/`. The cards are the map: a
small unit per book that says when to reach for it, what it chains with, and
where to look. The card is the index. The book is what you read.

It works like a brain, not a filing cabinet: small traces fire together and
brew, and distant domains prime each other on purpose. Your job when this skill
runs is to route to the right books and load their real text, not stop at a
summary.

Default brain location: `/home/cowboy/chainsaw` (adjust if cloned elsewhere).

## How to load (associative recall, not lookup)

1. **Always load the doctrine.** Read `FRAMEWORK.md`. It is the operating
   system: the collective effect, the cross-lobe threads, the tensions, and
   the map to the assessment method.

2. **Read the router.** Read `brain/INDEX.md`. Match the task to its lobe(s) and
   the specific book numbers by signal.

3. **Open the cards as the index.** Read the cards in `brain/cards/` the task
   names. The card tells you which book, when it applies, and where to look.
   The card is not the answer. It is the pointer.

4. **Load the full text.** For the one to three books the task actually needs,
   read the real text from `books/NN_*.txt`. If a book is large, use the card
   and the synthesis in `syntheses/synthesis_NN_*.md` to find the right
   chapters, then read those sections in full. Never substitute the card for
   the book when the book is what the task is about.

5. **Follow the synapses.** Each card has a `Chains with` list. When the task
   touches a chained book, including one in another lobe, pull its full text
   too.

6. **Prime with a distant part.** Deliberately pull ONE book the task would not
   obviously call for, the way music helps programming. Recon gets a craft book
   (trained observation). An exploit chain gets a human book (the operator is a
   source). A disclosure call gets a philosophy book (proportion). Load its
   real text, and state which distant part you pulled and why.

7. **Brew, then act.** Synthesize across the loaded full texts before
   answering. The answer comes from the combination, not from any single card.

## Token discipline

Never load all 45 full texts at once; the corpus is millions of words. Load the
framework (always), the index, the cards that route you, and then the FULL TEXT
of only the one to three books the task and its chains call for, plus one
priming book. That is the whole brain working at a sane weight: full context
where it matters, the map everywhere else.

## Why full text, not just cards

A card pre-decides what matters. The part of a book that cracks a hard problem
may be the part no summary kept. We keep every full text for exactly this
reason, and we prune by usage over time, never by guessing up front. See
USAGE.md.

## When NOT to use

Trivial mechanical edits, or tasks with no skill the 45 books touch. The brain
is for work that gets sharper when distant parts combine.
