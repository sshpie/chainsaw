# Chainsaw index

The router. Match a task to its lobe by signal, load that lobe and its named cards, then follow the chain map across lobes. The framework is always-on; this index just points.

## Route by signal

- **Offensive** (18) -> load when finding or proving an exploitable path: OSINT and Shodan recon, code review, reverse engineering, exploit development, fuzzing, web/api/crypto/cloud/network/privesc, side-channel.
  cards: 12 15 17 25 30 32 34 35 42 43 44 46 47 48 49 50 53 54
- **Defensive** (12) -> load when building visibility, resilience, ICS/OT and IoT defense, deception, malware analysis, or securing AI; thinking like the operator.
  cards: 13 16 24 26 28 29 31 33 36 37 51 52
- **AI and Agentic** (8) -> load when building, grounding, governing, or securing AI/agentic systems; fairness, randomness, NLP.
  cards: 03 20 21 27 38 39 40 41
- **Craft and Code** (6) -> load when the maker eye: trained observation, readable code, visual craft, tooling foundations.
  cards: 04 06 07 08 18 23
- **Human and Influence** (8) -> load when reading, persuading, leading, or connecting with people; social engineering; report and disclosure.
  cards: 05 09 10 11 14 19 22 45
- **Philosophy** (2) -> load when proportion and skepticism: deciding what matters and how to think about it.
  cards: 01 02
- **Bio and Compute** (11) -> load when the work is computational biology, bioinformatics, biological networks, biological and GPU-parallel computation, or bio-inspired and evolutionary optimization; algorithms drawn from living systems and the compute that runs them.
  cards: 55 56 57 58 59 60 61 62 63 64 65

## Flat weight

Every card carries the same weight. The lobes differ in size because domains differ in size, not in importance. Load by what the task and its chains call for, never by rank.

## Chain map (the synapses)

65 of 65 books are wired to at least one other. Follow these links across lobe boundaries; that crossing is where the brain thinks.

- **01** Critical Philosophy of Innovation and the Innovator [philosophy] <-> 2 3 4 9 13 14 22 24 27 29 33 37
- **02** The Philosophy of Cybersecurity [philosophy] <-> 1 3 5 6 7 11 16 17 18 19 23 24 25 26 30 31 32 35 36 37 44 46 47 48 50 51 52 53 54
- **03** The Art of Randomness: Randomized Algorithms in the Wild [ai-agentic] <-> 1 2 6 7 10 12 20 21 24 27 32 33 38 41 42 44 46 49 50 56 57 58 59 60 61 62 63 64 65
- **04** Pixel Art for Game Developers [craft-code] <-> 1 6 7 8 18 20 38
- **05** The Art of Coaching [human] <-> 2 6 7 8 9 10 11 13 14 16 19 22 29 38 45
- **06** The Art of Photography: A Personal Approach to Artistic Expression (2nd Edition) [craft-code] <-> 2 3 4 5 7 8 20 21 38 42 45
- **07** The Art and Science of Drawing: Learn to Observe, Analyze, and Draw Any Subject [craft-code] <-> 2 3 4 5 6 8 14 22 33 38 39 49
- **08** The Art of Readable Code [craft-code] <-> 4 5 6 7 18 23 30 35 36 41 55 63
- **09** Humble Leadership, Second Edition: The Power of Relationships, Openness, and Trust [human] <-> 1 5 10 11 16 22 27 33
- **10** The Next Leadership Team: How to Select, Build, and Optimize Your Top Team [human] <-> 3 5 9 11 13 14 20 22 29 38
- **11** The Art of Leadership: Small Things, Done Well [human] <-> 2 5 9 10 14 19 22 29 33 38 40
- **12** Open Source Fuzzing Tools [offensive] <-> 3 13 15 17 18 20 21 25 26 28 30 32 33 35 42 44 49 52 53 54 58 62 63 64
- **13** Human Factors in Cybersecurity [defensive] <-> 1 5 10 12 14 16 17 19 22 23 24 26 27 28 29 31 33 35 36 37 45 51
- **14** Persuade: The Four-Step Process to Influence People and Decisions [human] <-> 1 5 7 10 11 13 16 19 22 35 45
- **15** XSS Attacks: Cross Site Scripting Exploits and Defense [offensive] <-> 12 17 19 25 41 44 48
- **16** Psybersecurity: Human Factors of Cyber Defence [defensive] <-> 2 5 9 13 14 19 22 24 26 27 28 33 42 45 47 51 52
- **17** SQL Injection Strategies: Practical techniques to secure old vulnerabilities against modern attacks [offensive] <-> 2 12 13 15 24 25 26 30 32 39 41 42 44 48 55
- **18** GitHub for Next-Generation Coders: Build your ideas, share your code, and join a community of creators [craft-code] <-> 2 4 8 12 24 33 35 38 42
- **19** The Art of Social Engineering: Uncover the secrets behind the human dynamics in cybersecurity [human] <-> 2 5 11 13 14 15 16 22 24 33 35 37 42 43 45 47 51
- **20** Practical Fairness: Achieving Fair and Secure Data Models [ai-agentic] <-> 3 4 6 10 12 22 24 27 33 41 55 56 60 62 64 65
- **21** NLP for Software Engineering [ai-agentic] <-> 3 6 12 27 41 53 55 56 61 63
- **22** The Power of Humility in Leadership: Influencing as a Role Model [human] <-> 1 5 7 9 10 11 13 14 16 19 20 29 38 39 45
- **23** Windows 7 Resource Kit [craft-code] <-> 2 8 13 24 26 30 32 34 38 44 52
- **24** Securing AI Systems: A Comprehensive Framework for Enterprise Defense [defensive] <-> 1 2 3 13 16 17 18 19 20 23 25 26 27 28 31 32 33 35 36 37 39 41 42 44 46 47 48 50 51 52 55 56 58 59 62 65
- **25** SQL Injection Attacks and Defense (2nd Edition) [offensive] <-> 2 12 15 17 24 26 30 32 34 38 42 44 48 55
- **26** Industrial Cybersecurity, 2nd Edition [defensive] <-> 2 12 13 16 17 23 24 25 28 30 31 32 33 34 35 36 37 41 42 43 44 46 50 51 52 53 54
- **27** AI for Good: Applications in Sustainability, Humanitarian Action, and Health [ai-agentic] <-> 1 3 9 13 16 20 21 24 33 37 38 41 55
- **28** Virtual Honeypots [defensive] <-> 12 13 16 24 26 30 31 33 36 37 42 44 46 50 51 52 54 58
- **29** Becoming Resilient: Staying Connected Under Adversity [defensive] <-> 1 5 10 11 13 22 30 31 33 36 37 45 51
- **30** Penetration Tester's Open Source Toolkit [offensive] <-> 2 8 12 17 23 25 26 28 29 31 32 34 35 42 43 44 46 47 48 49 54
- **31** Industrial Cybersecurity [defensive] <-> 2 13 24 26 28 29 30 33 37 44 46 50
- **32** Hacking Cryptography [offensive] <-> 2 3 12 17 23 24 25 26 30 37 42 44 47 48 49 50 52 53 54 57 58 59 60
- **33** Chaos Engineering [defensive] <-> 1 3 7 9 11 12 13 16 18 19 20 24 26 27 28 29 31 35 37 38 44 46 51 55 57 58 60
- **34** Privilege Escalation Techniques [offensive] <-> 23 25 26 30 35 36 44 50 53 54
- **35** Cloud Penetration Testing [offensive] <-> 2 8 12 13 14 18 19 24 26 30 33 34 36 41 42 43 44 48
- **36** UTM Security with Fortinet [defensive] <-> 2 8 13 24 26 28 29 34 35 37 44
- **37** If It's Smart, It's Vulnerable [defensive] <-> 1 2 13 19 24 26 27 28 29 31 32 33 36 41 42 44 45 46 49 50 51 53 54
- **38** Agentic Coding with Claude Code [ai-agentic] <-> 3 4 5 6 7 10 11 18 22 23 25 27 33 41 45 47
- **39** Agentic Architectural Patterns [ai-agentic] <-> 7 17 22 24 41 48
- **40** Agentic AI For Dummies [ai-agentic] <-> 11 41
- **41** Learn Mistral AI [ai-agentic] <-> 3 8 15 17 20 21 24 26 27 35 37 38 39 40 42
- **42** From Day Zero to Zero Day [offensive] <-> 3 6 12 16 17 18 19 24 25 26 28 30 32 35 37 41 44 47 48 49 50 51 52 53 54 56 62 64 65
- **43** The Ultimate Kali Linux Book, 3rd Edition [offensive] <-> 19 26 30 35 44 46 47 48 54
- **44** Attacking Network Protocols [offensive] <-> 2 3 12 15 17 23 24 25 26 28 30 31 32 33 34 35 36 37 42 43 46 47 48 49 50 51 52 53 54 56 58 63
- **45** The Art of Conversation [human] <-> 5 6 13 14 16 19 22 29 37 38
- **46** Complete Guide to Shodan: Collect, Analyze, Visualize [offensive] <-> 2 3 24 26 28 30 31 33 37 43 44 47
- **47** OSINT Techniques: Resources for Uncovering Online Information (11th Ed.) [offensive] <-> 2 16 19 24 30 32 38 42 43 44 46 55
- **48** Pentesting APIs and Cloud Applications [offensive] <-> 2 15 17 24 25 30 32 35 39 42 43 44
- **49** Reverse Engineering for Beginners [offensive] <-> 3 7 12 30 32 37 42 44 50 52 53 54 59
- **50** Physical Fault Injection and Side-Channel Attacks on Mobile Devices [offensive] <-> 2 3 24 26 28 31 32 34 37 42 44 49 59
- **51** Cyberjutsu: Cybersecurity for the Modern Ninja [defensive] <-> 2 13 16 19 24 26 28 29 33 37 42 44
- **52** Practical Malware Analysis [defensive] <-> 2 12 16 23 24 26 28 32 42 44 49 53 58
- **53** The IDA Pro Book [offensive] <-> 2 12 21 26 32 34 37 42 44 49 52 54
- **54** Hacking: The Art of Exploitation, 2nd Edition [offensive] <-> 2 12 26 28 30 32 34 37 42 43 44 49 53
- **55** Bioinformatics: Managing Scientific Data [bio-compute] <-> 8 17 20 21 24 25 27 33 47 56 57 58 59 60 61 63 65
- **56** Algorithmic and Artificial Intelligence Methods for Protein Bioinformatics [bio-compute] <-> 3 20 21 24 42 44 55 57 59 60 61 62 63 64 65
- **57** Introduction to Biological Networks [bio-compute] <-> 3 32 33 55 56 58 59 60 61 62 63 64 65
- **58** Biological Computation [bio-compute] <-> 3 12 24 28 32 33 44 52 55 57 59 60 61 62 64 65
- **59** Programming Massively Parallel Processors, 4th Edition [bio-compute] <-> 3 24 32 49 50 55 56 57 58 60 61 62 63 64 65
- **60** Emerging Trends in Applications and Infrastructures for Computational Biology, Bioinformatics, and Systems Biology [bio-compute] <-> 3 20 32 33 55 56 57 58 59 61 62 63 65
- **61** Computational Intelligence and Pattern Analysis in Biological Informatics [bio-compute] <-> 3 21 55 56 57 58 59 60 62 63 64 65
- **62** Meta-heuristic and Evolutionary Algorithms for Engineering Optimization [bio-compute] <-> 3 12 20 24 42 56 57 58 59 60 61 63 64 65
- **63** Computational and Visualization Techniques for Structural Bioinformatics Using Chimera [bio-compute] <-> 3 8 12 21 44 55 56 57 59 60 61 62 64
- **64** Evolutionary Computation with Biogeography-based Optimization [bio-compute] <-> 3 12 20 42 56 57 58 59 61 62 63 65
- **65** Bio-Inspired Optimization for Medical Data Mining [bio-compute] <-> 3 20 24 42 55 56 57 58 59 60 61 62 64
