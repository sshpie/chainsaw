# Engram

A loadable, collective brain built from 45 books, read cover to cover, with
their **full text kept available** as the substance. The distilled cards,
lobes, and framework are the map on top. The books are the territory.

Engram is not a reading list and not a pile of summaries. It is one brain,
built so the books reinforce each other. You load it as context and it makes
every skill sharper, because every part feeds every other part.

> Working name. Rename the repo freely; nothing depends on the word "engram."

## The one claim

Using the 45 books as a collective improves every single skill each of them
teaches. They are not applied one at a time. They compound.

```
creative writing   <-->  vulnerability research
hacking / exploit  <-->  leadership
creative thinking  <-->  software programming
        ...and every other pair, both directions. they all help each other.
```

The creative-writing books sharpen how you tell the story of a finding. The
exploit books sharpen how a leader thinks about risk and pressure. The drawing
and photography books sharpen recon, because recon is trained observation. The
conversation and persuasion books sharpen disclosure. The randomness book
sharpens fuzzing. None of this works if you read one book and shelve it. It
works when the whole brain is loaded and the parts talk.

## How it thinks (like a brain)

A human brain does not look up one fact and stop. Small traces of information,
engrams, fire together and brew. A melody loosens a stuck function. A sketch
unlocks a recon angle. Distant parts prime each other, and the answer comes
from the combination, not the lookup.

Engram works that way. Each card is a small unit, a trace, and it points at the
full book behind it. Loading one fires its neighbors through the chain links,
which are the synapses. Distant domains are wired to prime each other on
purpose: music to programming, drawing to recon, exploitation to leadership.
The brain is most useful when you let an unrelated part brew with the task.

## Full context, no shortcuts

The full text of all 45 books is in the brain. We did not replace the books
with summaries, because a summary pre-decides what matters before we have any
evidence of what matters. When a task pulls a book, it pulls the full text. The
card just tells you which book and where to look.

We keep everything now because we do not yet know what works and what does not.
Usage carves the brain over time: what fires in real research earns its keep,
what never fires gets a pruning decision, later, on evidence, not opinion. See
USAGE.md.

## Flat weight (no best book)

Every book counts the same. There is no flagship, no core, no tier. A lobe with
two books is not lesser than a lobe with eleven; that is domain size, not
importance. They improve each other equally and in every direction, so the
brain is a full mesh, not a hub with spokes. Nothing here ranks the 45.

## How it was built

Same construction the wardrobe used on the cyber-pathway tool catalog: take a
catalog, distill each item into a small composable unit, then assemble units
into task-shaped sets on demand. There the units were outfits. Here they are
cards over full books. You do not load the whole library; you pull the books
the task calls for and chain them across racks.

```
45 books read in full
   -> full text retained (books/)                        THE SUBSTANCE
   -> per-book synthesis (read-proof + structure)        the read layer
      -> per-book BRAIN CARD (map: which book, when, what it chains with)
         -> 6 LOBE doctrines (how each domain acts as one capability)
            -> 1 FRAMEWORK (the collective doctrine, always-on)
```

## Architecture

```
THE TERRITORY (substance)        THE MAP (navigation)            THE LOADER (context)
books/  x45                      FRAMEWORK.md  (always-on)       load/SKILL.md
  full text of every book          the collective doctrine         /engram <task> -> picks the
  the part that helps may be      brain/INDEX.md                    book(s) from the map, loads
  the part no summary kept          signal -> lobe -> book          their FULL TEXT, brews
                                    + the chain map (synapses)
syntheses/  x45                  brain/lobes/*.md  x6             load/AGENT.md
  proof-of-read + structure        through-line + moves +          a think-tank subagent,
  per book                         collective lift per domain      grounded in the full brain
                                 brain/cards/*.md  x45
                                   reach-for-when / principles /  CLAUDE.md
                                   moves / chains / watch-out      drop the repo into a project,
                                   (the index into full text)      framework self-loads
```

## The six lobes

All 45 books placed, no overlap. Lobes keep token weight sane; they do not wall
the books off. The framework and the chain links cross every wall.

```
offensive   (11): 12 15 17 25 30 32 34 35 42 43 44
defensive   (10): 13 16 24 26 28 29 31 33 36 37
ai-agentic   (8): 03 20 21 27 38 39 40 41
craft-code   (6): 04 06 07 08 18 23
human        (8): 05 09 10 11 14 19 22 45
philosophy   (2): 01 02
```

## How to load the brain

1. FRAMEWORK.md is always-on. Read it first. It is the operating system.
2. Read brain/INDEX.md. Match the task to its lobe(s) and books by signal.
3. Load the FULL TEXT of the one to three books the task names, from books/.
   The card says which book and which sections; the book is what you read.
4. Follow the synapses. Each card points at sibling books, including across
   lobes. Pull their full text when the task touches them.
5. For a hard problem, deliberately load one DISTANT book the task would not
   obviously call for, the way music helps programming. State why.
6. Brew, then act. The answer comes from the combination of full contexts.

```
$ /engram map attack surface on an unknown industrial protocol
  map says: offensive (44, 42, 30) + defensive (26, 31, 28) + craft (07) + human (19)
  loads:    the FULL TEXT of the books the task actually needs, brews them
```

## Provenance and boundary

Built by Nuclide (Nick + Claude) from the "Research-N" O'Reilly Learning
playlist, 45 books read in full. The full texts and syntheses are copyrighted
and stay local (see .gitignore); they are never published. The publishable
layer is the map: README, FRAMEWORK, cards, lobes, INDEX, loader.

## Repo map

```
README.md            this file
FRAMEWORK.md         the collective doctrine (always-on)
USAGE.md             the growth model: keep everything, prune by usage
books/               full text of all 45 books            (local only)
syntheses/           per-book read-proof + structure      (local only)
brain/
  INDEX.md           router: signal -> lobe -> book, plus the chain map
  lobes/             6 lobe doctrines
  cards/             45 navigation cards (index into full text)
load/
  SKILL.md           the /engram loader skill
  AGENT.md           the think-tank subagent
CLAUDE.md            repo-level self-loader
```
