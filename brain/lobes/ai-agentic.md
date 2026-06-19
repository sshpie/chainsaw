# AI and Agentic lobe

## What this lobe is for
Load this lobe when the target or deliverable is a model or an agent, not infrastructure: standing up LLM/agent stacks, auditing them for bias and privacy leakage, attacking decision boundaries, mapping agent trust boundaries, or reasoning about decoding, sampling, and randomness from first principles. It is the toolbox for when the thing under assessment reasons, decides, or acts rather than just listens on a port.

## The through-line
A model or agent produces candidates; verification produces findings. Every book here states the same NuClide tenet in its own dialect: privacy is probabilistic not binary (a 60%-vs-50% membership-inference edge is a real breach, #20); out-of-distribution splits expose the 0.95-to-0.76 collapse a clean internal metric hides (#27); the harness, not the LLM call, is where reliability lives (#38); agency is bounded by five constraints and the foothold is wherever one is mis-set (#40). Trusting a single metric, a single fairness test, or a single decoding default is the vulnerability, not the verification.

## Operating moves
- Run the nine-lesson failure taxonomy as a literal probe-checklist against any model before trusting a metric; force an OOD split across the dimension that varies in deployment (#27).
- Membership inference with shadow models needs no original training data; an attack model at ~60% is a finding (#20).
- HopSkipJump (IBM ART) for query-only black-box evasion; AIF360 four-fifths/disparate-impact gate for bias; always run two explainers, LIME and SHAP can both be cloaked (#20).
- Map a target agent to Sense-Reason-Plan-Act-Memory; the memory backend is often an unauth vector DB that routes straight to aimap; the absence of a Human-in-the-Loop gate on an irreversible tool is a critical-class finding (#39).
- Fingerprint the framework from artifacts (ADK/CrewAI/LangGraph tokens) and read the A2A Agent card unauth to enumerate tool reach without exercising it (#39).
- The subagent description is appended to the system prompt: an untrusted skill or malicious description is a live prompt-injection vector; scope MCP with a per-task .mcp.json (#38).
- Decompose autonomy by protocol (MCP/ANP/A2A/ACP) and confirm rollback plus decision logging exists; absence is "surface open, oversight not exercised" (#40).
- Apply the next-bit-test lens to any token/key/nonce generator: statistically-good MT19937/LCG is not a CSPRNG, reachable seed equals forgeable token (#3).
- temperature=0 for code and security analysis; Mistral offline on Ollama:11434 for log triage you cannot send to a hosted API (#41).

## How the books interlock
Start at #40 for vocabulary and autonomy postures, deepen into #39 for the named patterns and where they break, and use #38 for the live harness mechanics; #41 instantiates all three on an auditable open-weight stack. #20 and #27 are the audit-and-mitigate loop over any model those agents wrap, with #3 supplying the sampling and randomness math under decoding, differential privacy, and shadow-model perturbation. #21 is a citation index, not a method source.

## Collective lift from other lobes
- #24 Securing AI Systems (defensive) is the hardening mirror for every offense in #20 and every failure mode in #27: attack with this lobe, structure the fix with #24.
- #42 From Day Zero to Zero Day and #12 Open Source Fuzzing Tools (offensive) drive the agent tool-use layer and the decision boundary as a fuzzing target, validating that a model-surfaced finding is real, not hallucinated.
- #2 The Philosophy of Cybersecurity (philosophy) supplies the falsifiability discipline and the law-over-markets impact register; #34 Privilege Escalation (offensive) turns the inter-agent JSON contract into a confused-deputy chain.

## Reach for the lobe when
- The target is a model: bias audit, membership inference, evasion, poisoning, extraction.
- The target is an agent: tool registry, memory backend, HITL gates, MCP/A2A surface.
- You are building or fingerprinting an LLM/agent stack (Claude Code, Mistral, ADK/CrewAI/LangGraph).
- You need to reason about decoding, sampling, entropy, or a weak token/nonce generator.
- A reported accuracy looks too clean and needs an OOD split before you trust it.
