# Offensive lobe

## What this lobe is for
Load this lobe when the task is finding and proving an exploitable path: code review, reverse engineering, fuzzing, web/crypto/cloud/network/privesc attack. Reach for it whenever the goal moves past "is there a surface" to "can I drive untrusted input to a dangerous operation and prove impact with an artifact." It is the data-into-control-plane confusion lobe, from a malformed DNS packet to an agent tool argument.

## The through-line
Every book here is one idea in a different costume: a vulnerability is a reachable, attacker-influenced path from an untrusted source to a dangerous sink, and verification is the load-bearing stage, not discovery. The scanner, the fuzzer, the dork produce candidates; only a verified reach (a triggered crash, a 200-with-data, a recovered byte) produces a finding. #42 names the source-to-sink spine; #17 and #25 name the root cause as untrusted data crossing into the control plane via string concatenation; #44 reduces any wire protocol to the same; #12 proves the input actually touched the code. Trust-the-input is the single failure class, and it generalizes verbatim from SQL to prompt injection.

## Operating moves
- Sink-to-source taint walk: start at a dangerous function, work backward to attacker-controlled input, filter for genuinely reachable, build a minimal deterministic PoC (#42).
- Model a known bug as a CodeQL/Semgrep AST query, sweep the origin repo, then the ecosystem; one bug implies many (#42).
- Apply the six fuzzing building blocks before any mutation: valid data set, per-byte meaning, integrity maintenance (recompute checksum/length), fixed-seed repeatability, malformed-value arsenal, state machine. Skip one and the run silently no-ops (#12).
- Coverage-driven loop: gcc -fprofile-arcs -ftest-coverage, read the HTML for untaken branches, trace back to the gating input bytes, mutate that field (the Freeciv 5.4% -> 15.6% move) (#12).
- Decompose any unknown protocol into content/encoding/transport before analysis; capture passively (Wireshark plus strace/DTrace/ProcMon) and actively (MITM proxy chosen by client cooperation) (#44).
- Confirm SQLi without breaking the page: ' AND 1=1-- vs ' AND 1=2--, then UNION column count via ORDER BY n, then blind binary-search on ASCII(SUBSTRING(...)) (#17, #25).
- Filter recon for XSS: inject ;!--"<XSS>=&{()} and grep View Source for which metacharacters survive before crafting the real vector (#15).
- Hunt the crypto implementation tell, not the math: batch-GCD a harvested key pool for shared primes, scan a signature corpus for reused ECDSA r, flip CBC bytes against a padding oracle (#32).
- Foothold-to-root: find / -perm -u=s against GTFOBins; writable + runs-as-root = code exec (SUID .so, weak service perms, cron over writable script) (#34).
- Cloud first pass from the provider Cloud Shell: prowler aws/azure/gcp, then Pacu/ScoutSuite/Trivy; sort findings EPSS-then-CVSS (#35).
- Full-engagement spine: passive recon -> enumeration -> exploitation -> the AD credential chain (secretsdump, PtH, Kerberoast, BloodHound), every step mapped to MITRE ATT&CK/PTES (#43, #30).

## How the books interlock
Start at #30 or #43 for the engagement lifecycle and toolchain, branch to #42 when the target has no off-the-shelf exploit and you must find the bug. #12 and #44 are the discovery depth (how to fuzz, where to fuzz a protocol parser); #15/#17/#25/#32 are the bug-class playbooks for whatever sink the taint walk lands on; #34 takes any foothold to root and #35 ports the whole discipline to cloud.

## Collective lift from other lobes
- #24 Securing AI Systems and #39 Agentic Architectural Patterns (defensive/agentic): the parameterize-whitelist-canonicalize-least-privilege matrix from #17/#25 maps one-to-one onto safe agent tool interfaces and CaMeL-style data/control separation; tool-calling injection is second-order SQLi.
- #2 The Philosophy of Cybersecurity (philosophy): supplies the disclosure-ethics and rules-of-engagement frame that turns the offensive toolkit into a defensive act and bounds the restraint.
- #37 If It's Smart It's Vulnerable and #26/#31 Industrial Cybersecurity (defensive): name the device population and consequence model where these findings detonate, sharpening target selection and impact framing for ICS/OT and embedded work.

## Reach for the lobe when
- A surface is open and you need to prove a reachable, exploitable path, not just catalog it.
- You have untrusted input crossing into a parser, query, command, or tool call.
- A service speaks a protocol below the HTTP status layer and must be dissected.
- A foothold needs to climb to root/SYSTEM or pivot into the cloud control plane.
- Crypto is in the path and you suspect the implementation, not the algorithm.
- You need to fuzz a target and reason about whether the probe actually touched the code.
