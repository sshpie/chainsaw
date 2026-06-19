# The Chainsaw Framework

This is the loadable collective brain: 45 books across 6 lobes, read in full and
kept in full, compiled into one operating doctrine for ICS/OT and
AI-infrastructure security research. The six lobes are Offensive, Defensive, AI
and Agentic, Craft and Code, Human and Influence, and Philosophy. The one claim
that unifies all 45: using them together improves every single skill each of
them teaches, because the skill any one book names is also half-described by
four others wearing different costumes.

## The collective effect (read first)

The brain is used as a collective. No card is applied alone. The cross-links are
the product, not a footnote to it. Each book is a lens, and any single skill
sharpens when you stack lenses from more than one lobe on it at once. Loading
the 45 together lifts every individual skill each book covers. Worked examples,
each one skill lifted by several lobes firing together:

- RECON. Trained observation is not one book's property. Drawing (#7) teaches
  you to block-in the ambiguous surface with straight lines first and see it is
  less complex than assumed. Photography (#6) teaches the two-pass look:
  subjective spark, then a cold analytical pass for what actually communicates.
  Social engineering (#19) and elicitation (#45) read the operator below the
  role layer. Pentest recon (#30, #43) supplies the passive-to-active
  toolchain. Honeypot thinking (#28) makes you ask what the operator expected to
  see. Five lobes converge on one verb: look harder, look twice, look below.

- REPORT WRITING. A disclosure is not a CVE dump. Persuade (#14) sequences it:
  credibility, then emotion, then logic, then action, and never drops the
  "because" that moved compliance from 60% to 93%. Conversation (#45) supplies
  the delivery layer up the Thing-Action-Head-Heart-Soul ladder. Philosophy (#2)
  supplies proportion, so "critical" is anchored to the CIA triad and
  "sophisticated" is load-bearing or it is cut. Leadership (#11) makes you speak
  last and gather context first. Craft (#18) lands one concrete metaphor before
  the command so the CISO feels the risk. Five lobes on one paragraph.

- FUZZING. The fuzzer is the cheap part. Fuzzing (#12) supplies the six building
  blocks and the coverage loop. Randomness (#3) tells you whether your seed and
  your mutation entropy are real or a statistically-good fake that silently
  no-ops. Readable code (#8) is the harness discipline that keeps the test rig
  honest when a state machine grows. From Day Zero (#42) frames the whole effort
  as a taint walk to a reachable sink, so you fuzz the field that gates the
  branch, not random bytes. Four lobes, one corpus.

- THREAT MODELING. The model is not a control checklist. Psybersecurity (#16)
  classifies each control with Cynefin so you stop hand-mandating what should be
  a guardrail. Human Factors (#13) walks HFACS-Cyber four levels and counts
  frequencies instead of blaming the click. Philosophy (#2) runs the
  lateral-movement question: does the peripheral system reach the
  safety-critical one. If It's Smart It's Vulnerable (#37) names the device
  population and the cellular backchannel where it detonates. Four lobes build
  one model.

- DISCLOSURE JUDGMENT. Whether to name an operator publicly. Philosophy (#2)
  supplies graded attribution and the false-flag account. Persuade (#14)
  supplies the lab-coat move, lead with CVE track record, not the payload.
  Conversation (#45) manages your own state first so the high-friction call does
  not leak. Leadership (#9) labels the relationship L-1/L1/L2 before you decide
  complex work can even survive there. Four lobes on one decision.

## Full context, no shortcuts (the substance)

The full text of all 45 books is the substance of this brain and lives in
`books/`. We did not replace the books with summaries. A summary pre-decides
what matters before we have any evidence of what matters, and the part of a book
that cracks a hard problem is often the part no summary would keep.

So the cards in `brain/cards/` are the map, not the territory. A card says which
book, when to reach for it, what it chains with, and where to look. When a task
pulls a book, it pulls the full text. The card is the index into the book; the
book is what you read.

We keep everything now because we do not yet know what works and what does not.
Usage carves the brain over time: what fires in real research earns its keep,
what never fires gets a pruning decision, later, on evidence, not opinion. We
never prune to look tidy. See USAGE.md.

## Flat weight (no best book)

Every book counts the same. There is no flagship, no core, no tier. A lobe with
two books is not lesser than a lobe with eleven; that is domain size, not
importance. They improve each other equally and in every direction, so the brain
is a full mesh, not a hub with spokes. Nothing here ranks the 45. The chain map
proves it: every book is wired to at least one other, and the crossing is where
the brain thinks.

## The bidirectional cross-pollination

This is the owner's thesis, in his words, and the brain is built to make it
true. Every pair runs both directions.

- The creative writing side helps the vulnerability research side, and the
  vulnerability research side helps the creative writing side.
- The hacking and exploit side helps the leadership side, and the leadership
  side helps the hacking and exploit side.
- The creative thinking side helps the software programming side, and the
  software programming side helps the creative thinking side.
- And so on across every pair. They all help each other.

It works the way a person works. Small units of information brew and combine
with other parts, and distant domains prime each other, the way music can help
someone's thinking process for programming. The brain is most useful when you
let an unrelated part brew with the task.

## The cross-lobe threads

- The human is both attack surface and defense. The exact mechanics that build
  legitimate trust are the mechanics a social engineer weaponizes. Read #19
  against #14 and #45 to model both sides of a pretext end to end; #13 and #16
  give the cognitive conditions that make the human exploitable or hardenable.
  One substrate, two polarities.

- Master the source before you touch the sink. Taint analysis is the universal
  move. #42 names the source-to-sink spine; #17 and #25 root it in untrusted
  data crossing into the control plane; #44 reduces any wire protocol to the
  same shape; #8 makes you rename the variable so its trust state is visible at
  the assignment site. Tool-calling injection (#39) is second-order SQLi. The
  same walk runs from a SQL query to an agent tool argument to a Modbus field.

- Build the lab, attack the lab, defend the real thing. #26 supplies the
  copy-pasteable OT lab; #44 and #12 reverse and fuzz the open-by-design
  protocols inside it; #28 stands the deception sensor; #33 runs the chaos
  experiment that proves the control fires. You attack what you built to learn
  what to defend in production.

- Resilience over prevention. Security is never absolute (#2). #29 measures
  time-to-reconstitute-under-fire instead of assuming the wall holds; #31
  inverts CIA to AIC for OT so availability outranks confidentiality; #28 buys
  dwell-time signal; #33 disproves the steady state on a minimized blast radius.
  The deliverable is how fast you recover, not whether you were breached.

- AI is a new substrate inheriting every old vulnerability. The model and the
  agent are new costumes on old bugs. #39 maps Sense-Reason-Plan-Act-Memory and
  finds the memory backend is an unauth vector DB. #3 says a reachable seed is a
  forgeable token whether it sits under a JWT or a sampling default. #20 proves
  privacy is probabilistic, a 60%-vs-50% membership edge is a breach. The CIA
  triad, taint analysis, and confused-deputy chains all port verbatim.

- Craft is learned observation, not talent. #6 says the histogram has no
  artistic meaning, a clean number can describe a horrible artifact. #7 says do
  structural work in light lines before any dark line. #4 says decide palette
  and grid before producing. Each is the same restraint ethic: verify in the
  cheap reversible stage, because the irreversible stage is where the cost
  lands.

- Every finding ends in a human conversation. The chain that started at a
  malformed packet finishes at a triager who owes you nothing. #14 is the state
  machine, #45 the delivery, #2 the proportion that keeps it honest, #11 the
  humility that makes it land. A perfect exploit with a botched disclosure
  conversation is an unfixed vulnerability.

## The productive tensions

- Experiment on production versus never touch production. Chaos Engineering
  (#33) says inject failure into the live system, that is the only place the
  steady state is real. Pentest and ICS (#26, #31, #34) say never touch fragile
  OT, an active scan can halt a PLC. Resolution: the chaos loop's discipline is
  the bridge, not the contradiction. You minimize the blast radius and define
  the steady state before you inject. On IT and cloud you inject on production
  with a kill switch; on OT you inject in the #26 lab that mirrors it, then
  carry only the proven hypothesis to the real plant. Same loop, different
  blast-radius budget.

- Offensive versus defensive framing of identical knowledge. #44 reverses a
  protocol to attack it; #26 reverses the same protocol to monitor it. #19
  weaponizes trust; #13 hardens against it. Resolution: there is one body of
  knowledge and two polarities of intent. The red methodology validates the blue
  baseline, and the blue consequence model sharpens red target selection.
  Philosophy (#2) is the governor that decides which polarity the moment calls
  for and bounds the restraint.

- Intuition versus method rigor. The "art of" books (#3 Randomness, #45
  Conversation, #6 the photographer's eye) trade in feel; the pattern books (#39
  Architectural Patterns, #42 From Day Zero, #43 Kali) trade in repeatable
  procedure. Resolution: intuition picks the variant, method proves it. The
  artist's two-pass look (#6) generates the candidate; the taint walk (#42)
  verifies it. Feel without verification is a hunch; method without feel scans
  the wrong field. The collective needs both, in that order.

## How this maps to the assessment methodology

The pipeline is Discover, Fingerprint, Verify, Attribute, Classify, Score,
Codify, and each stage pulls a lobe.

- Recon and discovery is trained observation. The Craft lobe runs here: #7
  block-in, #6 two-pass seeing, #4 scope-the-palette-first. You see the surface
  before you name it.
- Fingerprint and verify is taint analysis and source mastery. The Offensive
  lobe runs: the sink-to-source walk (#42), the protocol decomposition (#44),
  the SQLi confirmation pattern (#17, #25), the six fuzzing blocks (#12). A
  banner is a candidate; a 200-with-data read is the finding.
- Restraint and proportion is philosophy. The Philosophy lobe governs the
  severity call: CIA before adjectives, the cost-imposition test, graded
  attribution, the lateral-movement pivot (#2). This is where "critical" earns
  the label or gets cut.
- Reporting and disclosure is the human conversation. The Human and Influence
  lobe runs: credibility-emotion-logic-action (#14), the talk-type ladder (#45),
  speak-last humility (#11). The finding moves a person or it does not move at
  all.
- Resilience recommendations are the defensive close. The Defensive lobe runs:
  AIC for OT (#31), time-to-reconstitute (#29), does-the-control-fire (#33), the
  engineering-workstation-beats-the-PLC target note (#26). You hand the operator
  a falsifiable fix, not a patch list.

## How to load the brain

The FRAMEWORK is always-on; it is the connective tissue, not a lobe you opt
into. Read the INDEX, pull the lobe or lobes the task signals, and open the
cards the chains point to, because the interlock notes are routing instructions,
not trivia. Then load the FULL TEXT of the one to three books the task actually
needs from `books/`, using the cards and the syntheses to find the right
chapters in a large book. For any hard problem, deliberately load a SECOND lobe
that is not the obvious one, because the lift is in the cross-link: a fuzzing
problem wants the Randomness card, a disclosure wants the Philosophy proportion
card, a recon problem wants the social-engineering people-read. Load the
collective, read the real text, and every skill in it lifts at once. That is the
whole point.
