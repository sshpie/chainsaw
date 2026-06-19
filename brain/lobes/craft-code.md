# Craft and Code lobe

## What this lobe is for
Load when producing or auditing an artifact a second reader must understand: tool source, a finding writeup, a dashboard, an ASCII diagram, a disclosure, a commit. Load it when the task is making something readable, visual, or shippable, and the quality bar is clarity-for-the-reader, not raw function. Not an assessment lobe; it governs how the work reads and ships.

## The through-line
Clarity at small scale is the load-bearing skill, and it is decided in the cheap, reversible stage. Every book here says the same thing in its own medium: the intentionally-placed pixel (4), the histogram that has no artistic meaning (6), the light line before the dark line (7), the name that cannot be misconstrued (8), the metaphor before the command (18). Technique should disappear so the reader responds to the content. Verify in the correctable stage, because a clean number can describe a horrible artifact.

## Operating moves
- Decide palette and tile/grid size BEFORE producing anything; treat it as the scope gate, and mark unused state loudly (neon magenta) so stray refs are caught on sight (4).
- Reuse is the workhorse: palette-swap, ramp-generate, tile-reuse, mirror/rotate to multiply output; snap between loopable atoms instead of interpolating every transition when states explode combinatorially (4).
- Run the two-pass critique: emotional/subjective seeing for spark, then a separate cold analytical pass for whether it communicates; never collapse them (6).
- Apply the histogram test to every metric: ask "could this number be a perfect exposure of a horrible image?" Verify the underlying read, not the summary stat (6).
- Do all structural work in light lines (reversible probes, read-only pivots) before any dark line (irreversible action); the restraint ethic in one mechanic (7).
- Block-in ambiguous surface with straight lines first to expose it is less complex than assumed, then flow real structure over the scaffold (7).
- Trust-state-in-name pass: rename vars holding network input/secrets to carry state (untrusted_, plaintext_, raw_, sanitized_) so mishandling is visible at the assignment site (8).
- Encode danger and units in names (untrustedUrl, hex_id, _ms); devil's-advocate every name; expensive ops get computeX not getX (8).
- Plain-English-first (rubber-duck) before coding; the nouns/verbs reveal the subproblems to extract (8).
- One concrete metaphor per scary concept (locking-your-house, train-station SPOF) so the reader feels the risk before the command (18).
- Grep .git/config and remote URLs for embedded PATs; treat the PAT-in-URL beginner pattern as a credential-leak finding (18).

## How the books interlock
Sequence by stage of the artifact. 7 sets the order and the reversible-first discipline; 6 supplies the seeing-and-verification judgment over it; 4 is the production-economy execution under constraint; 8 is the line-level rulebook for code specifically; 18 lands the work in a versioned repo and supplies the metaphor scaffold for the writeup. 7 and 8 are the tightest pair (light-line-first equals small reversible commits before the dark-line refactor). 4 and 18 cover make-it and ship-it for solo builders.

## Collective lift from other lobes
- 38/39 Agentic Coding and Architectural Patterns [ai-agentic]: the Five Essential Questions (7) ARE a subagent task spec, and 8's naming/control-flow rules are the readability spec for agent output a human verifies fast. The cumulative single-artifact exercise (4) is the iterative-compounding-context pattern.
- 42 From Day Zero to Zero Day and 12 Open Source Fuzzing Tools [offensive]: the histogram-has-no-meaning discipline (6) IS candidate-versus-finding triage; a crash or scan hit is an exposure, verification is the print.
- 20 Practical Fairness and 21 NLP for Software Engineering [ai-agentic]: "the metric is not the meaning" (6) chains to fairness-metric skepticism, and "intelligence at input sets the output ceiling" (6, 8) is rich-context-in determining quality-out.

## Reach for the lobe when
- Writing or auditing tool source, a finding, or a disclosure another reader verifies
- Building dashboard glyphs, severity icons, ASCII box diagrams, the NuClide UI look
- Triaging raw tool output (a metric, a hit, a crash) into a real finding
- Shipping a repo: commits, diffs, PRs, README, GitHub-misconfig enumeration
- Naming variables that hold secrets, network input, or units
- Sequencing investigative work cheap-reversible-first before any irreversible action
