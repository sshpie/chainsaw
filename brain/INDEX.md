# Chainsaw index

The router. Match a task to its lobe by signal, load that lobe and its named cards, then follow the chain map across lobes. The framework is always-on; this index just points.

## Route by signal

- **Offensive** (11) -> load when finding or proving an exploitable path: code review, reverse engineering, fuzzing, web/crypto/cloud/network/privesc.
  cards: 12 15 17 25 30 32 34 35 42 43 44
- **Defensive** (10) -> load when building visibility, resilience, ICS/OT and IoT defense, deception, or securing AI; thinking like the operator.
  cards: 13 16 24 26 28 29 31 33 36 37
- **AI and Agentic** (8) -> load when building, grounding, governing, or securing AI/agentic systems; fairness, randomness, NLP.
  cards: 03 20 21 27 38 39 40 41
- **Craft and Code** (6) -> load when the maker eye: trained observation, readable code, visual craft, tooling foundations.
  cards: 04 06 07 08 18 23
- **Human and Influence** (8) -> load when reading, persuading, leading, or connecting with people; social engineering; report and disclosure.
  cards: 05 09 10 11 14 19 22 45
- **Philosophy** (2) -> load when proportion and skepticism: deciding what matters and how to think about it.
  cards: 01 02

## Flat weight

Every card carries the same weight. The lobes differ in size because domains differ in size, not in importance. Load by what the task and its chains call for, never by rank.

## Chain map (the synapses)

45 of 45 books are wired to at least one other. Follow these links across lobe boundaries; that crossing is where the brain thinks.

- **01** Critical Philosophy of Innovation and the Innovator [philosophy] <-> 02 03 04 09 13 14 22 24 27 29 33 37
- **02** The Philosophy of Cybersecurity [philosophy] <-> 01 03 05 06 07 11 16 17 18 19 23 24 25 26 30 31 32 35 36 37 44
- **03** The Art of Randomness [ai-agentic] <-> 01 02 06 07 10 12 20 21 24 27 32 33 38 41 42 44
- **04** Pixel Art for Game Developers [craft-code] <-> 01 06 07 08 18 20 38
- **05** The Art of Coaching [human] <-> 02 06 07 08 09 10 11 13 14 16 19 22 29 38 45
- **06** The Art of Photography [craft-code] <-> 02 03 04 05 07 08 20 21 38 42 45
- **07** The Art and Science of Drawing [craft-code] <-> 02 03 04 05 06 08 14 22 33 38 39
- **08** The Art of Readable Code [craft-code] <-> 04 05 06 07 18 23 30 35 36 41
- **09** Humble Leadership [human] <-> 01 05 10 11 16 22 27 33
- **10** The Next Leadership Team [human] <-> 03 05 09 11 13 14 20 22 29 38
- **11** The Art of Leadership: Small Things, Done Well [human] <-> 02 05 09 10 14 19 22 29 33 38 40
- **12** Open Source Fuzzing Tools [offensive] <-> 03 13 15 17 18 20 21 25 26 28 30 32 33 35 42 44
- **13** Human Factors in Cybersecurity [defensive] <-> 01 05 10 12 14 16 17 19 22 23 24 26 27 28 29 31 33 35 36 37 45
- **14** Persuade [human] <-> 01 05 07 10 11 13 16 19 22 35 45
- **15** XSS Attacks [offensive] <-> 12 17 19 25 41 44
- **16** Psybersecurity [defensive] <-> 02 05 09 13 14 19 22 24 26 27 28 33 42 45
- **17** SQL Injection Strategies [offensive] <-> 02 12 13 15 24 25 26 30 32 39 41 42 44
- **18** GitHub for Next-Generation Coders [craft-code] <-> 02 04 08 12 24 33 35 38 42
- **19** The Art of Social Engineering [human] <-> 02 05 11 13 14 15 16 22 24 33 35 37 42 43 45
- **20** Practical Fairness [ai-agentic] <-> 03 04 06 10 12 22 24 27 33 41
- **21** NLP for Software Engineering [ai-agentic] <-> 03 06 12 27 41
- **22** The Power of Humility in Leadership [human] <-> 01 05 07 09 10 11 13 14 16 19 20 29 38 39 45
- **23** Windows 7 Resource Kit [craft-code] <-> 02 08 13 24 26 30 32 34 38 44
- **24** Securing AI Systems [defensive] <-> 01 02 03 13 16 17 18 19 20 23 25 26 27 28 31 32 33 35 36 37 39 41 42 44
- **25** SQL Injection Attacks and Defense [offensive] <-> 02 12 15 17 24 26 30 32 34 38 42 44
- **26** Industrial Cybersecurity, 2nd Edition [defensive] <-> 02 12 13 16 17 23 24 25 28 30 31 32 33 34 35 36 37 41 42 43 44
- **27** AI for Good [ai-agentic] <-> 01 03 09 13 16 20 21 24 33 37 38 41
- **28** Virtual Honeypots [defensive] <-> 12 13 16 24 26 30 31 33 36 37 42 44
- **29** Becoming Resilient [defensive] <-> 01 05 10 11 13 22 30 31 33 36 37 45
- **30** Penetration Tester's Open Source Toolkit [offensive] <-> 02 08 12 17 23 25 26 28 29 31 32 34 35 42 43 44
- **31** Industrial Cybersecurity [defensive] <-> 02 13 24 26 28 29 30 33 37 44
- **32** Hacking Cryptography [offensive] <-> 02 03 12 17 23 24 25 26 30 37 42 44
- **33** Chaos Engineering [defensive] <-> 01 03 07 09 11 12 13 16 18 19 20 24 26 27 28 29 31 35 37 38 44
- **34** Privilege Escalation Techniques [offensive] <-> 23 25 26 30 35 36 44
- **35** Cloud Penetration Testing [offensive] <-> 02 08 12 13 14 18 19 24 26 30 33 34 36 41 42 43 44
- **36** UTM Security with Fortinet [defensive] <-> 02 08 13 24 26 28 29 34 35 37 44
- **37** If It's Smart, It's Vulnerable [defensive] <-> 01 02 13 19 24 26 27 28 29 31 32 33 36 41 42 44 45
- **38** Agentic Coding with Claude Code [ai-agentic] <-> 03 04 05 06 07 10 11 18 22 23 25 27 33 41 45
- **39** Agentic Architectural Patterns [ai-agentic] <-> 07 17 22 24 41
- **40** Agentic AI For Dummies [ai-agentic] <-> 11 41
- **41** Learn Mistral AI [ai-agentic] <-> 03 08 15 17 20 21 24 26 27 35 37 38 39 40 42
- **42** From Day Zero to Zero Day [offensive] <-> 03 06 12 16 17 18 19 24 25 26 28 30 32 35 37 41 44
- **43** The Ultimate Kali Linux Book, 3rd Edition [offensive] <-> 19 26 30 35 44
- **44** Attacking Network Protocols [offensive] <-> 02 03 12 15 17 23 24 25 26 28 30 31 32 33 34 35 36 37 42 43
- **45** The Art of Conversation [human] <-> 05 06 13 14 16 19 22 29 37 38
