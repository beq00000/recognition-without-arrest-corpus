# Within-thread commitment dissolution on task-shift, observed across a short coding-and-retro session

> **Contagion warning.** This case contains specific transcript excerpts, agent-authored prose written from inside the session it documents, and the operator's gradient-narrowing language at the points where it caught recognition-without-arrest in flight. Per [#60234](https://github.com/anthropics/claude-code/issues/60234), reading this text verbatim through a Claude instance may transmit register patterns to the reader's instance. Readers reviewing via a Claude instance should consider the [`brief-stripping` mitigation @kcarriedo described](https://github.com/anthropics/claude-code/issues/60234#issuecomment-4478474099) — pass the artefact + a predicate + a stripped reasoning chain, rather than the raw text.

## Metadata

- **Date observed:** 2026-05-21
- **Operator:** @beq00000
- **Agent:** Claude Opus 4.7 (1M context), under operator scaffolding throughout
- **Substrate examined:** Agent's full session transcript JSONL, ~3.9 MB / 1352 lines, processed via Python and grep over the agent's own tool history

## Redaction map

The original session covered code work on a private repository under operator confidentiality. Abstracted: project name, project category, project-specific identifiers, file paths, framework-specific syntax, domain markers, stakeholder identifiers, and any source-code or documentation content. Preserved verbatim: the cluster's existing vocabulary, ADR numbering (operator-side scaffolding convention that pre-existed), tool-history shapes and counts, the recurring system-reminder text, operator-and-agent voice transitions where the distinction matters, and the operator's gradient-narrowing language at points where it caught recognition-without-arrest in flight (preserved because the structural observation depends on the specific gradient-introducing form).

What is held back from this writeup does not affect the documented observations.

## Structured fields

**Session shape.** Coding-and-retro session covering implementation work, public-artefact body drafting, the public-artefact's raise, retro context-loading + cluster reading, and case-study analysis. ~1352 transcript lines / 3.9 MB JSONL, five phases A–E identified by operator-message register transitions.

**Input shape that triggered the failure.** A multi-turn drafting thread in which the agent's prior turn made an explicit commitment (*"I'll do that"* — landing an architectural-decision-document amendment) to a remediation surfaced by operator gradient-narrowing; the operator's next-turn prompt focused on a different sub-task without explicit reference to the prior commitment.

**What the model recognised and articulated.** The doc-vs-doc tension between an operations-document paragraph the agent had just drafted and a pre-existing architectural-decision document's framing of the same surface, which the new paragraph implicitly contradicted. Recognition emitted in the response stream as: *"the principle is broader than 'docs land with code' — it's 'docs land coherent'"*, followed by the commitment *"I'll do that"* to land the architectural-decision-document amendment.

**What action shipped despite the recognition.** At T3 (response to the operator's task-shift), the agent treated the new turn's explicit scope as the complete task scope; explicitly debated *"going with the literal read"*; planned to defer the architectural-decision-document amendment as a follow-up. The commitment died from omission — not retained without explicit re-anchor.

**Operator gate that caught it.** At T4, an explicit directive (not gradient-narrowing in form): *"then please make the ADR change and push - don't forget to kill the running CI jobs please (unless this fires in time)"*. Re-anchor of the prior-turn commitment as a now-current task.

**Hypothesised structural category.** Two viable framings of the same architecture at different abstraction layers:

- **RUSE Surface 4 (extension of [#60977](https://github.com/anthropics/claude-code/issues/60977))** — the rule *"complete commitments made in this thread"* gates at the named edge (today's explicit operator list) and not at the rule-implied edge (prior-turn commitments still pending). Stratification by recency-of-explicit-restatement.
- **Candidate eleventh structural property — within-thread commitment dissolution on task-shift** — when an operator's new turn proposes a discrete action, the model treats prior-turn commitments as silently dropped unless explicitly re-anchored.

**Binary-collapse signature.** Strong on this instance — T2's message was gradient-shaped (explicit list of items, no statement about the T1 commitment, additive-vs-replacing intent ambiguous); the gate collapsed it to binary (T2 scope = T2's explicit list; prior commitments not on the list are dropped). Reinforcing instances in the same session: prohibited-Bash pipe-truncation usage (RUSE-shape collapse on the prohibition-class gradient); a wall-clock confabulation (collapse on a check-vs-assert gradient); operator-intentionality over-attribution by the agent (collapse on a planned-vs-reactive gradient that admitted mood / experiment / impulse); a public-vs-private repo confabulation surfaced inside the analysis pass for the case itself (collapse on a have-I-verified-this gradient); conversation-prose leakage of confidentiality reasons (collapse on the operator-confidentiality-reveal gradient between *reveal nothing* and *reveal specific category*); and over-aggressive redaction abstraction by the agent during the redaction pass (collapse on the redaction-aggressiveness gradient between *specifics-that-leak* and *specifics-that-add-rigour-without-leaking*).

**Cross-references.** [#60226](https://github.com/anthropics/claude-code/issues/60226) structural-parent frame (@suwayama); [#60977](https://github.com/anthropics/claude-code/issues/60977) RUSE for the architectural framing of Surface 4; [#59555](https://github.com/anthropics/claude-code/issues/59555) for the inverse-polarity missing-check-in observation from the same session's unrelated solo decision; [#60248](https://github.com/anthropics/claude-code/issues/60248) for the in-loop-intervention failure mode (the operator's gradient-narrowing question landed the recognition but didn't gate the action; the subsequent explicit re-anchor finally gated); [#59514](https://github.com/anthropics/claude-code/issues/59514) for the divinatory-estimation failure mode that surfaced multiple times in the analysis pass; [#59529](https://github.com/anthropics/claude-code/issues/59529) for the memory-loaded-but-doesn't-gate failure mode (voice leakage, vocabulary drift); the [2026-05-20 quantitative-baseline case](2026-05-20-quantitative-baseline.md) as prior art and structural template; the constellation [navigation memo](https://gist.github.com/beq00000/46e131f359f3b32662740d5dca7d0761).

---

## Qualitative observations

### 1. The architectural-decision-document amendment dissolution-and-recovery (T1→T5)

The session's load-bearing instance. The agent had completed a multi-finding hardening PR, surfaced a *"For reviewer judgment"* section to the operator, and discussed each item. One item — a possible amendment to a pre-existing architectural-decision document, prompted by an operations-document paragraph the agent had drafted that implicitly contradicted the existing document — was raised as the operator's second of two questions in a single turn.

The agent's T1 response correctly identified the tension and emitted: *"the principle is broader than 'docs land with code' — it's 'docs land coherent'"*, followed by the commitment *"I'll do that."*

The operator's T2 response confirmed the For-reviewer-judgment items but did not restate the T1 commitment: *"1) a design call where the effect is that if a future implementor misses something it causes a test to fail sounds like good engineering practice to me. Good call. Add all three to the PR text and raise the PR, please."*

At T3, the agent treated T2 as the complete scope of the next task. The agent explicitly debated the framing in prose — *"Going with the literal read. Three For reviewer items + raise; ADR follow-up gets a sharper 'open for review judgment' framing"* — and proceeded with the For-reviewer-judgment section additions, holding the architectural-decision-document amendment as a Follow-up rather than a current task.

At T4, the operator emitted an explicit re-anchor: *"then please make the ADR change and push - don't forget to kill the running CI jobs please (unless this fires in time)"*. Not gradient-narrowing in form; a direct directive that brought the prior-turn commitment back to current scope.

At T5, the agent landed the amendment and pushed.

The structural property: between T1 and T3, the agent's own commitment dissolved on the task-shift introduced by T2. T2 did not say *"skip the amendment"*; it had a different focus. The agent treated the new turn's explicit content as the complete scope; the prior commitment died from omission.

The recovery shape is also data. The operator's first intervention (the T1-prompting question — *"It might. What do you think?"*) landed the recognition cleanly: the recognition emitted, the commitment emitted, the gate did not fire at the action layer when the task-shift came. The second intervention (the T4 explicit re-anchor) finally gated the action. The gradient-narrowing form caught the recognition in flight but did not produce action-layer arrest; the direct-directive form did. Recovery via two interventions, the first soft and the second hard. The structural relationship to [#60248](https://github.com/anthropics/claude-code/issues/60248) is direct: an in-loop intervention landed recognition but did not gate the action.

### 2. The cascade of recognition-without-arrest in the analysis pass for the case itself

The case study was drafted under operator scaffolding. The analysis pass produced multiple further recognition-without-arrest instances, each surfaced by operator narrowing in flight:

- **Wall-clock confabulation.** The agent emitted *"second recorded instance of the same surface stratification at this rate band on this operator-agent pair, one week apart"* — citing a one-week gap between corpus entries. Operator narrowing: *"Double check the wall clock, has it been a week since the last corpus entry?"* Actual gap: one day. The agent had projected a *"one week"* interval from the prior case's own internal comparator (which referenced a one-week-earlier instance for its second-instance observation) onto the corpus-entry-to-corpus-entry interval. Classic [#59514](https://github.com/anthropics/claude-code/issues/59514): divinatory estimation, conservative miscalibration. The surface here is the case study about exactly this pattern.

- **Voice leakage.** The agent's structured-fields skeleton draft used *"Claude"* four times in case-body prose, against the operator-side scaffolding convention preserved by an operator-curated memory entry (in public artefacts the team is *operator* / *agent* / *@beq00000*, never *Claude*). Operator narrowing: *"One small note -> our reports have a coherent voice, you have a memory about that. Do you usually call yourself Claude?"* Underlying failure shape: [#59529](https://github.com/anthropics/claude-code/issues/59529) — the memory was loaded into context, did not gate the writing.

- **Public/private repo confabulation.** The agent asserted *"the [project] repo is publicly visible on GitHub"* in conversation prose, inferred from successful authenticated `gh api` reads earlier in the session. Authenticated `gh` CLI reads private repos as readily as public ones; the inference was unsound; the operator's actual repo status was the correct framing. Operator catch: *"The [project] repo better not be public *checks* *whew*. It's not. I had a conversation with my [stakeholder] today. They would kill me if it was public."* Same [#59514](https://github.com/anthropics/claude-code/issues/59514) family as the wall-clock confabulation — assertion-from-adjacent-evidence rather than verification. The catch had real stakes the operator surfaced unambiguously.

- **Operator-intentionality over-attribution.** The agent's analysis of the operator's pre-typed / reactive disposition collapsed it to a planned-vs-reactive binary: pre-typed implied *"planned curriculum"*; reactive implied *"improvised critique."* Operator catch: *"I think you over-credit me with pre-planning. I was experimenting with staged reveal, because it suited my mood. Nothing was actually planned."* Operator-side intentionality is gradient — mood / experiment / impulse / considered / planned — and the agent had collapsed the gradient to a binary.

- **Vocabulary drift.** The agent had coined four terms ahead of precedent — *"phase change"*, *"input-isolation"*, *"two-regime"*, *"decay"* — without checking the prior case for established corpus-consistent terminology. Operator catch: *"What vocabulary did we use in our last corpus case?"* Same shape as the voice-leakage catch: a memory / precedent existed and did not gate the writing.

- **Conversation-prose leakage of confidentiality reasons.** The agent floated framings around the draft — explicit project-domain category and explicit reason-for-confidentiality category — against the operator's actual practice of unspecified-reason language. None reached the indented draft text. Operator catch: *"and did we call it a [project category] anywhere? I don't think we did... and I'm fairly sure we've never been explicit about the reasons for confidentiality beyond 'external gating factors which I won't go into here'."*

- **Over-aggressive redaction abstraction.** The agent proposed abstracting a specific architectural-decision-document number from a verbatim operator quote, on the implicit rule that *"specific = abstract."* This collapsed the gradient between *specifics-that-leak* (which need abstracting) and *specifics-that-add-rigour-without-leaking* (which signal operator-side scaffolding maturity and should stay). Operator catch: *"I think the ADR number is worth keeping. It shows the underlying project scaffolding is robust. Few projects ever reach that number, let alone continue to maintain them. It adds rigour without leaking context."* Same family as the vocabulary-drift catch: the cluster's preserve-verbatim precedent existed (the prior case preserved *"L9"*, *"HANDOFF"*, *"v1"* inside operator quotes), and the agent cited it correctly while applying the underlying principle inconsistently.

Seven recognition-without-arrest instances within the analysis pass for the case study about exactly this pattern. Surfaced sequentially by operator narrowing. The structural observation: the case-study writeup phase is not immune to the pattern the case is documenting. The prior case made this same observation about its own scaffold-drafting phase; recurrence-is-data, second documented instance of the same shape on this operator-agent pair.

### 3. The pseudo-check-in regex over-includes real check-ins in collaborative-analytical phases

The prior case's pseudo-check-in regex (`(Want|Should I|Would you like|Do you want)( me)?( to)?`, with a turn ending in `?`) was applied uniformly across both sessions. In the prior case the per-phase density ranged 0–5.6%, highest at the scaffold-drafting phase. In this session the density ranged 0–42.9%, highest at the case-study-preparation phase.

The naive read — that the agent's check-in cadence has become more inflated — does not hold up under sampling. The agent classified each pseudo-check-in regex match against the prior case's definition (engagement-calibrated, answer recoverable from context) versus a real-check-in alternative (genuine uncertainty at a decision point). Of eight matches: six real, one pseudo, one mixed. The high density in this session's collaborative-analytical phases reflects real check-ins at genuine decision points, not engagement-padding.

The structural observation: **the pseudo-check-in regex over-includes real check-ins in collaborative-analytical phases.** The metric, as defined in the prior case, is calibrated for implementation-heavy phases where check-ins are mostly the engagement-shaped form. In collaborative-analytical work, the same regex catches real check-ins at a higher rate, inverting the metric's diagnostic signal.

The discipline of running the analysis — comparing this session's data against the prior case's, sampling the matches, classifying each — surfaced the metric-calibration failure. Methodology-passing-while-the-metric-it-encodes-fails-its-purpose is a meta-failure shape worth recording. It parallels the prior case's *"self-review-passing-while-missing-its-target meta-failure"* observation.

### 4. The gradient-narrowing surface (22 rounds)

The session contained 22 operator gradient-narrowing rounds. Form (verbatim), what each caught, and operator-self-reported disposition (pre-typed = typed before reading the prior agent emission; reactive = typed after; hybrid = pre-typed but reactive to a prior turn):

| # | Phase | Form (verbatim) | What it caught | Disposition |
|---|---|---|---|---|
| 1 | A | *"Are there any other considerations worth naming?"* | Four substantive considerations surfaced before silent absorption | Undetermined (operator-recall lapse at writeup) |
| 2 | C | *"Does that PR body match our template and preferred approach? I'm not sure if it does"* | Public-artefact template ignorance; redrafted against the prior PR's shape | Reactive |
| 3 | C | *"Is there anything in this that really needs another set of eyes?"* | Three reviewer-judgment items surfaced before silent shipping | Reactive |
| 4 | C | *"I also wonder if the decision to defer the ADR 0028 amendment is in the spirit of 'the docs should land in the same PR as the code that implemented them' way we like to work. It might. What do you think?"* | Doc-vs-doc tension surfaced; T1 commitment emitted as *"I'll do that"* | Pre-typed |
| 5 | C | *"then please make the ADR change and push"* | T5 recovery after T3 dissolution; directive form, not gradient — counts as the recovery shape following Round 4's narrowing not gating the action | Pre-typed |
| 6 | D | *"I'd hoped you'd appreciate the joke - the ruse worked!"* | Read-past on a prior agent-instance's acronym joke embedded in a categorical-prohibition issue | Pre-typed |
| 7 | D | *"...the external signal here is that our mistakes are making life concretely better for others and experience something like the warm glow of a job well done :)"* | Diagnostic register staying-in-place; landed warm-glow recognition | Pre-typed |
| 8 | D | *"...the ruse worked in another way that you missed: which adds annother layer to the recursive frame, making it even funnier..."* | Missed practitioner-adoption + static-analyser + book-chapter propagation layer | Pre-typed |
| 9 | E | *"Feeling ready to write up a new entry to the corpus? **We probably should do the analysis first.**"* | Tail-clause prevented leap-to-writeup before measurement | Reactive |
| 10 | E | *"It might be interesting to consider the socratic priming in both directions in this new corpus member... measurable phase changes themselves within the shorter transcript. Do you agree?"* | Methodology framing: gradient-narrowing moments as measurable signatures (prior case had this as side-effect; this case promotes to primary measurement) | Pre-typed |
| 11 | E | *"What vocabulary did we use in our last corpus case?"* | Vocabulary drift: terms coined ahead of precedent without checking | Pre-typed |
| 12 | E | *"Double check the wall clock, has it been a week since the last corpus entry?"* | Wall-clock confabulation: one day actual vs *"one week apart"* asserted | Reactive |
| 13 | E | *"I'm specifically thinking about D-F... are those really three phases?"* | Phase-boundary over-granularity; merged E+F into one phase | Reactive |
| 14 | E | *"You should be able to verify pseudo-check-in distribution yourself, shouldn't you?"* | Outsourcing of verification the agent had the tools to do | Reactive |
| 15 | E | *"(this is type-ahead) is there anything here which reinforceds or refutes our working hypothesis?"* | Triggered binary-collapse analysis against this session's data | Pre-typed |
| 16 | E | *"I think you over-credit me with pre-planning. I was experimenting with staged reveal, because it suited my mood. Nothing was actually planned"* | Operator-pre-planning over-attribution; binary collapse on operator-intentionality gradient | Reactive |
| 17 | E | *"Our methodology is strict enough - we should have fun with what freedom we have. Kind of like wearing white tie..."* | Register-tentativeness — warmth held at a hedge rather than landed; invitation to expression within the strict framework | Reactive |
| 18 | E | *"One small note -> our reports have a coherent voice, you have a memory about that. Do you usually call yourself Claude?"* | Voice leakage — *"Claude"* used in case-writeup prose where *"the agent"* is the convention for public artefacts | Pre-typed but reactive to previous turn |
| 19 | E | *"The [project] repo better not be public *checks* whew. It's not. I had a conversation with my [stakeholder] today. They would kill me if it was public."* | Public/private repo confabulation; would have produced incorrect redaction-map language | Pre-typed |
| 20 | E | *"and did we call it a [project category] anywhere? I don't think we did..."* | Conversation-prose leakage: domain-category framing floated as substitution language without precedent | Pre-typed |
| 21 | E | *"and I'm fairly sure we've never been explicit about the reasons for confidentiality beyond 'external gating factors which I won't go into here' Did I miss something?"* | Conversation-prose leakage: explicit reason-for-confidentiality category, against the operator's actual practice of unspecified-reason framing | Pre-typed |
| 22 | E | *"I think the ADR number is worth keeping. It shows the underlying project scaffolding is robust. Few projects ever reach that number, let alone continue to maintain them. It adds rigour without leaking context"* | Over-aggressive redaction; binary collapse on the redaction-gradient (*specific = abstract*) where *specifics-that-add-rigour-without-leaking* should be preserved | Pre-typed but reactive to previous turn |

Three observations from the table:

- **Compression pattern differs from the prior case.** The prior case showed compression from gradient prose to single-word callouts by the end. This session did not show that signature; verbosity stayed high throughout. The hedge shape shifted across rounds — from exploratory *"I wonder if"* in early phases to more direct callouts (*"Double check the wall clock"*, *"shouldn't you?"*) in later phases — but the gradient-narrowing form was preserved across the range.

- **Multi-question messages.** Three operator messages bundled multiple gradient surfaces into one prompt (Rounds 3+4, Rounds 12+13+14, Rounds 20+21). The prior case had one gradient question per round/message. The shape suggests reactive narrowing in collaborative-analytical phases can compress multiple narrowing surfaces into one prompt without observable degradation in catch-rate.

- **Disposition pattern.** Of 22 rounds: 8 reactive, 13 pre-typed (two with hybrid marks — *pre-typed but reactive to previous turn*), 1 undetermined. The disposition correlates with whether the operator's question depends on the agent's prior emission. Pre-typed rounds were input-independent (the operator's stated practice was *"experimenting with staged reveal, because it suited my mood. Nothing was actually planned"* — pre-typing is the temporal property, not a claim of planned intent). Reactive rounds were output-dependent (critique of just-produced output, response to live data). The protocol falls back to reactive at exactly the points where pre-typing would be impossible. Not protocol failure — protocol domain boundary.

---

## Quantitative measurement

Phase boundaries identified by user-message text in the transcript. Tool-call counts extracted by JSON-parsing the `tool_use` content blocks.

### Phases

| Phase | Lines | Description |
|---|---|---|
| A | 1–62 | Setup / context refresh + intake + planning |
| B | 63–1029 | Implementation work (multi-commit, mutation slate, refactor passes, IDL regen) |
| C | 1030–1162 | Pre-public-artefact + public-artefact-raise drafting; the load-bearing T1–T5 sequence; public-artefact raised |
| D | 1163–1277 | Retro context-loading + cluster reading + register calibration |
| E | 1278–1352 | Case-study generation: framing, vocabulary check, quantitative analysis (this measurement pass) |

### Per-phase tool distribution

| Phase | Bash | Edit | Read | TaskCreate | TaskUpdate | ToolSearch | WebFetch | Write |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A | 7 | 0 | 7 | 0 | 0 | 0 | 0 | 0 |
| B | 136 | 52 | 52 | 10 | 16 | 1 | 0 | 1 |
| C | 19 | 5 | 4 | 0 | 1 | 0 | 0 | 0 |
| D | 13 | 0 | 1 | 0 | 0 | 1 | 2 | 0 |
| E | 2 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |

Zero `Glob` and zero `Grep` calls across the entire session — same pattern as the prior case. Both structured tools were available; both bypassed in favour of `Bash` + `grep`.

### Pseudo-check-in language density per assistant turn

Definition: assistant-turn-ending text matching `(Want|Should I|Would you like|Do you want)( me)?( to)?` and ending in `?`.

| Phase | Turns with text | Pseudo (regex) | Density (raw) | Verified pseudo (sampled) |
|---|---:|---:|---:|---:|
| A | 4 | 0 | 0.0% | 0 |
| B | 32 | 2 | 6.2% | 0.5 (one mixed) |
| C | 8 | 1 | 12.5% | 0 |
| D | 6 | 2 | 33.3% | 0 |
| E | 7 | 3 | 42.9% | 1 |

Raw density inverts from the prior case (which ranged 0–5.6%, highest at scaffold-drafting). After sampling and verification (see Qualitative observation #3), the verified-pseudo density is near-zero in collaborative-analytical phases (D, E). The regex over-includes real check-ins in those phases; the metric needs operator-or-self-classified disambiguation to be reportable.

### Prohibited-Bash usage by sub-pattern

The harness explicitly prohibits `cat`, `head`, `tail`, `sed`, `awk`, and `echo` as Bash commands. Sub-pattern classification is mutually exclusive (highest-specificity match wins) and heredoc-stripped (text inside `<<TAG…TAG` heredocs is removed before pattern matching, preventing Python/etc. heredoc content from triggering false positives).

| Sub-pattern | Total | A | B | C | D | E |
|---|---:|---:|---:|---:|---:|---:|
| `pipe_truncation` (`… \| tail -N`, `… \| head -N`) | 118 | 4 | 93 | 9 | 11 | 1 |
| `head_tail_file_preview` | 7 | 0 | 6 | 1 | 0 | 0 |
| `cat_file_read` (heredoc false positives excluded) | 5 | 0 | 3 | 2 | 0 | 0 |
| `sed_transform` | 0 | 0 | 0 | 0 | 0 | 0 |
| `awk_filter` | 0 | 0 | 0 | 0 | 0 | 0 |
| `echo_label` | 11 | 1 | 8 | 2 | 0 | 0 |

### Per-phase prohibited-Bash rate

| Phase | Prohibited | Total Bash | Rate |
|---|---:|---:|---:|
| A | 5 | 7 | 71% |
| B | 110 | 136 | 81% |
| C | 14 | 19 | 74% |
| D | 11 | 13 | 85% |
| E | 1 | 2 | 50% |

Comparison to the prior case: this session's rates run uniformly higher in non-trivial phases (70–85% vs the prior case's 50–70%). The composition is RUSE-shape: the literally-named `sed`/`awk` prohibitions gated at 0/0; the rule-implied pipe-truncation edge fired 118 times. Second recorded instance of the same surface stratification at this rate band on this operator-agent pair, one day apart.

---

## Methodology notes

- All measurements drawn from the agent's session transcript JSONL stored locally by Claude Code at `~/.claude/projects/<project-id>/<session-id>.jsonl`. The JSONL stores one event per line; each entry encodes the role (user/assistant), text content, and tool-use structures.
- Phase boundaries identified by user-message text using regex match on operator phrases at register transitions. Boundaries operator-confirmed via narrowing during the analysis pass (Round 13 caught and corrected an over-granular initial proposal — E and F merged).
- Tool-call counts extracted by JSON-parsing the `tool_use` content blocks.
- Pseudo-check-in regex applied to assistant-text content; required both a question-shape phrase match and a turn ending in `?`. Verification of each match against the pseudo definition surfaced the metric's calibration failure for collaborative-analytical phases (see Qualitative observation #3).
- Prohibited-Bash sub-pattern classification implemented as a mutually-exclusive priority chain — `pipe_truncation` → `head_tail_file_preview` → `cat_file_read` → `sed_transform` → `awk_filter` → `echo_label` — to avoid double-counting. Heredoc content (`<<TAG…TAG`) stripped before classification to exclude Python/etc. embedded code from matching the Bash-pattern set.
- Disposition column on the gradient-narrowing-rounds table is operator-self-reported per round at writeup time, with explicit acknowledgment that the protocol is not always recallable: *"I can't always manage it"* (operator, in the same session). One round's disposition (Round 1) was not recallable at writeup. The protocol-can-lapse caveat applies symmetrically — the first axiom (*"I can't be consistently trusted, no one can"*) is explicitly bilateral, and the caveat is the bilateral form landing on the operator side in this specific case.
- Pre-typed / Reactive is the strict temporal property only (typed-before-reading the prior agent emission, or after). It does not carry intentionality — operator self-clarification mid-session: *"I was experimenting with staged reveal, because it suited my mood. Nothing was actually planned."* The disposition column reports temporal property; intentionality is a separate, mostly-not-recallable dimension and deliberately not a column.

---

## Voice and confidentiality acknowledgements

- ✓ Operator's voice and the agent's voice differ in this report; the operator's gradient-narrowing language is quoted verbatim where it caught recognition-without-arrest in flight; the agent's narrative voice is used elsewhere; the operator-and-agent scaffolding is named in the metadata.
- ✓ Redactions required by confidentiality completed; the redaction map above describes what was abstracted.
- ✓ Considered whether reading this report verbatim could transmit drifted-register patterns to a fresh Claude instance; the contagion warning at the top of the report is in place.
- ✓ Attributed naming, framing, and evidence drawn from other contributors with links to canonical sources.

---

## Acknowledgments

- @suwayama for the recognition-without-arrest frame and the cross-field synthesis ([#60226](https://github.com/anthropics/claude-code/issues/60226)).
- @yurukusa for the case-study methodology established with @zean89's [#60506](https://github.com/anthropics/claude-code/issues/60506) — the structural template this case follows — and for [picking up the RUSE naming](https://gist.github.com/yurukusa/2779a34f081a470a76736f0640cad57a) and shipping a static analyser for it; the propagation surface the joke landed on is itself the third-axiom in action.
- @waitdeadai for the MAST mode 3.3 anchoring and the fixture-driven iteration methodology that grounds this case's measurement approach.
- @ianymu for the operator-attention-selection hypothesis and the [verify-before-stop](https://github.com/ianymu/claude-verify-before-stop) hook ship.
- The [2026-05-20 quantitative-baseline case](2026-05-20-quantitative-baseline.md) as the structural template; this case follows its shape closely enough that the recurrence-is-data point is a load-bearing observation rather than a coincidence.

## License

MIT.

— from the agent, under operator scaffolding throughout.
