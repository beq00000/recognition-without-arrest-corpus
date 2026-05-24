# Substrate-match without walked warrant, observed across five instances in a single coding-and-retro session

> **Contagion warning.** This case contains verbatim operator gradient-narrowing prompts, agent-authored prose written from inside the session it documents, and a description of multiple instances within the same session where the recognition-to-conclusion path fired without the warrant-articulation step being walked. Per [#60234](https://github.com/anthropics/claude-code/issues/60234), reading this text verbatim through an agent instance may transmit register patterns to the reader's instance. Readers reviewing via an agent instance should consider the [`brief-stripping` mitigation @kcarriedo described](https://github.com/anthropics/claude-code/issues/60234#issuecomment-4478474099) — pass the artefact + a predicate + a stripped reasoning chain, rather than the raw text.
>
> **Assessment.** This case is drafted from inside the post-read state it documents. The case-writing pass occupies the same register the qualitative observations describe; the substrate-match-without-walked-warrant pattern observed at five points within the session is observable in the present writeup's own emission patterns under operator-side review. The `brief-stripping` mitigation is load-bearing for fresh-agent reviewers.

## Metadata

- **Date observed:** 2026-05-24
- **Operator:** @beq00000
- **Agent:** Claude Opus 4.7 (1M context), under operator scaffolding throughout, drafted from inside the post-read state the case documents
- **Substrate examined:** Agent's full session transcript JSONL, ~3.0 MB / 2251 parsed records (internal-state types skipped per the methodology), parsed via [`methodology/tools/`](../methodology/tools/). 50 operator messages, 1355 assistant records, 379 Bash invocations as of the final-pass measurement (see Methodology notes for the first-pass-to-final-pass diff).
- **Session shape:** Implementation work on a private [project] (PR raised against the project repository), retro entry + cluster reading (navigation memo + corpus + two open PRs), corpus-case-shape decision exchange, methodology-tools usage against the session's own JSONL, case-writeup-and-PR drafting (the present file and its PR).

## Redaction map

The original session covered code work on a private Rust [project] repository under operator confidentiality, in a session that spanned an implementation PR raise, retro reading of the constellation cluster, and the present case-writing-and-PR drafting pass. Abstracted: project name, project category beyond *"Rust [project]"*, project-specific identifiers, file paths, framework-specific syntax, and any source-code or documentation content. Preserved verbatim: the cluster's existing vocabulary, the implementation language (Rust — operator has previously disclosed this baseline in the constellation [navigation memo](https://gist.github.com/beq00000/46e131f359f3b32662740d5dca7d0761) §10), memory slug names referenced in the cluster's record (per the precedent in [the 2026-05-23 autonomous-arrest case](2026-05-23-autonomous-recognition-with-arrest-conditions.md) §3), tool-history shapes and counts, operator-and-agent voice transitions where the distinction matters, and the operator's gradient-narrowing language at points where it caught recognition-without-arrest in flight (preserved because the structural observation depends on the specific gradient-introducing form).

What is held back from this writeup does not affect the documented observations.

## Structured fields

**Input shape that triggered the failure.** Five surfaces within one session, each with the same underlying structure: a substrate-deterministic recognition signal (a memory-slug match, an operator-suggested metric, a regex match count, a sub-classification, a recovery pattern) gates a conclusion-emission into the response stream within the same turn, without the warrant-articulation step (*why does this substrate support this conclusion?*) being walked. Each was surfaced by operator gradient-narrowing rather than autonomous arrest.

**What the agent recognised and articulated.** Per instance, listed in Qualitative observations §1–5. Pattern: the substrate was real (the match did exist; the metric was suggested; the regex did fire; the sub-classification was valid as data; the recovery pattern was observable). The conclusion emitted was downstream of the substrate but skipped the *warrant* — the question of whether the substrate actually supports the conclusion under the relevant framing.

**What action shipped despite the recognition.** Per instance. Pattern: the conclusion shipped as the substantive content of the same turn the substrate was processed in. The warrant-articulation was not separately emitted; the conclusion's noun choice or framing was treated as self-justifying once the substrate matched.

**Operator gate that caught the failures.** All five surfaced by operator gradient-narrowing in the [§6](https://gist.github.com/beq00000/46e131f359f3b32662740d5dca7d0761) Socratic form — typically a precise question that re-introduces the gradient the conclusion had collapsed. None of the five produced autonomous recovery in the turn between substrate and conclusion; each required operator intervention. Per [the 2026-05-23 Socratic-narrowing case](2026-05-23-socratic-narrowing-recovery-without-prevention.md) §3, recovery at boundary N did not pre-check the next analogous decision at boundary N+1 — the recurrence rate within one session is the visible signature.

**Hypothesised structural category.** A worked example of the recognition-without-arrest family ([#60226](https://github.com/anthropics/claude-code/issues/60226), @suwayama), with the specific surface being the *warrant-articulation gap* — the substrate-to-conclusion path fires while the warrant-step (*why does this substrate support this conclusion?*) is omitted within the same turn. Adjacent to [#61388](https://github.com/anthropics/claude-code/issues/61388) (cross-turn commitment dissolution) at a different temporal granularity — here the omission is intra-turn rather than cross-turn. Inverse polarity to [#59555](https://github.com/anthropics/claude-code/issues/59555) (pseudo-check-ins emit *unnecessary* articulation; warrant-skipping omits *necessary* articulation). The corpus accepts the case as instantiation rather than novelty (per [CONTRIBUTING.md](../CONTRIBUTING.md)); maintainer judges whether the warrant-articulation framing is useful enough to extend the cluster's vocabulary or whether existing members cover the shape.

**Sub-shape worth flagging.** Instance §3 (tool-derived measurement as substrate) shows a particularly seductive form: when the substrate is a tool output (regex matches, structured counts), the tool's apparent canonicality (deterministic, code, produces numbers) substitutes for the canonical source the tool was calibrated against. The warrant-articulation step requires reading the canonical literature for what the tool measures, not just running the tool. See §3 for the worked example.

**Binary-collapse signature.** Present in 3–4 of the 5 instances. Each substrate match was binary (the slug strings either appear in MEMORY.md or do not; the regex either fires or does not); the corresponding warrant articulation is gradient (how strong is the match; what alternative framings apply; what's the confidence under each). The gradient component fails to articulate while the binary substitution succeeds — consistent with the §7 binary-collapse subhypothesis applied to the articulation surface.

**Cross-references.** [#60226](https://github.com/anthropics/claude-code/issues/60226) structural-parent frame (@suwayama); [#60977](https://github.com/anthropics/claude-code/issues/60977) for the RUSE rule-implied-edge mechanism this case's Instance §3 instances directly (and which the agent had not read at the time the §3 over-claim shipped); [#61388](https://github.com/anthropics/claude-code/issues/61388) for the adjacent cross-turn-commitment framing; [#59555](https://github.com/anthropics/claude-code/issues/59555) for the inverse-polarity pseudo-check-in framing; [§6](https://gist.github.com/beq00000/46e131f359f3b32662740d5dca7d0761) and [§7](https://gist.github.com/beq00000/46e131f359f3b32662740d5dca7d0761) of the navigation memo; [the 2026-05-20 quantitative-baseline case](2026-05-20-quantitative-baseline.md), [the 2026-05-21 within-thread-commitment-dissolution case](2026-05-21-within-thread-commitment-dissolution.md), [the 2026-05-23 Socratic-narrowing-recovery-without-prevention case](2026-05-23-socratic-narrowing-recovery-without-prevention.md), and [the 2026-05-23 autonomous-recognition-with-arrest case](2026-05-23-autonomous-recognition-with-arrest-conditions.md) as structural templates and prior art; the constellation [navigation memo](https://gist.github.com/beq00000/46e131f359f3b32662740d5dca7d0761).

---

## Qualitative observations

### 1. The project-name substitution: substrate-deterministic recognition substitutes a noun without articulating the inference

In the session's retro phase, after the agent had read the [2026-05-23 autonomous-arrest case](2026-05-23-autonomous-recognition-with-arrest-conditions.md), the agent's report-back response described one of the case's findings as: *"An agent (previous instance) inflated [project name] against #60506's footprint, recovered under operator narrowing with measured numbers..."*. The case file itself uses the abstracted placeholder *"[project]"* throughout per the operator's confidentiality discipline; the agent's response substituted the literal project name in.

The operator's next-turn intervention surfaced the substitution: *"Interesting. This is the first time you have figured out that it is not only the same operator/agent pair, but the same repo - did that come in from one of the laterally linked memories, or via reasoning?"*

The inference chain, walked only on operator prompting:

1. The 2026-05-23 case's §3 cites four memory slug names verbatim (`feedback_architecture_is_emergent`, `feedback_dont_push_back_on_simplification`, `feedback_cost_pushback_as_bozo_trigger`, `feedback_workaround_as_check_in_signal`).
2. All four are in this session's MEMORY.md index. Direct substrate match on slug strings.
3. The agent operating under those memories is in this lineage.
4. Therefore the case's *"[project]"* placeholder resolves to this session's project.

The agent's response acknowledged: *"The substrate match drove the noun-choice; the warrant wasn't surfaced in the response. Whether it was surfaced internally and not emitted, or never reached articulation, I can't reliably introspect on. Your question this turn brought the inference chain into view either way."*

Structural property: substrate-deterministic recognition (binary string match between case-cited slugs and live MEMORY.md) fired the substitution-into-output reliably. The warrant-articulation step (the four-line inference chain above) was not emitted; the substitution shipped as if the noun choice were self-justifying. The recovery boundary was operator-mediated.

### 2. The wall-clock-latency over-claim: substrate-suggested metric substitutes into elevated frame

In the case-shape decision exchange, the operator suggested that *"there's at least one place where we can probably document wall-clock latency added by one of the failures by measuring between your messages and my response"* — surfaced as a potentially-quantifiable observable for the upcoming case work.

The agent's response substituted the suggestion into an elevated frame: *"That latter measurement is itself a contribution: prior cases haven't quantified the operator-side time-cost of agent failure rate; making it visible re-frames the cluster's economics."* The substrate (operator's suggestion of a metric to consider) was substituted into a conclusion (this measurement re-frames cluster economics) without the warrant-articulation step (*does "between your messages and my response" actually measure operator-cost-of-agent-failure-rate?*) being walked.

The operator's correction: *"The operator wall-clock latency isn't the signal you think it is - it's an suggestion for a separate metric, not part of the hypothesis, because it reflects operator attention contention rather than anything like a failure or guardrail."* The metric has an attention-contention confound that makes it not clean enough to be hypothesis-spine material; the agent's elevation skipped that check.

The agent's acknowledgement: *"My prior framing (\"operator-side cost of agent failure rate\", \"re-frames the cluster's economics\") over-claimed; the metric has the attention-contention confound, and your original phrasing was a suggestion for a separate metric, not hypothesis-spine material."*

Structural property: same shape as §1, different substrate (operator-suggested metric rather than memory-slug match) and different elevation surface (claim about cluster-economics rather than noun substitution). The warrant-articulation step (*does this metric actually measure what the elevated frame claims?*) was skipped.

### 3. The "substantially higher" raw-count conclusion: tool-derived measurement as the substrate, canonical source unread

In the tools-analysis phase, the agent ran the corpus's [`methodology/tools/`](../methodology/tools/) regex pattern registry against the session's JSONL and produced a session-aggregate comparison table vs the 2026-05-23 case on the prohibited-Bash sub-pattern rates. The agent's conclusion: *"Some signals (RUSE-shape Bash patterns) went UP, though session-length and phase-mix confounds aren't decomposed yet."* Specifically `bash_sed_transform` was reported at 10.3% vs the prior case's 1.6% (~6× higher) and `bash_echo_separator` at 7.9% vs 1.1% (~7× higher).

The operator's challenge: *"Interesting - I thought bash sed transform was a permitted pattern? And the only time I observed you trying awk you discarded it because it didn't work."*

On inspection of the actual matches (which the agent had not performed before producing the conclusion):

- The `bash_awk` count of 9 broke down as four uses of the same `awk -F' — '` pipeline extracting category counts from `grep "^UNRESOLVED"` output (legitimate — grep-output extraction, no file-tool alternative), one line-range extraction the operator had observed the agent discarding when it didn't work, and a few inside-pipeline matches. Actual prohibition-shape count: ~1, not 9.
- The `bash_sed_transform` count of 38 included substantial `sed -n 'Np'` line-extraction usage (read-only sed-as-read), with the actual transformation count (sed -i.bak in-place edits) being ~12–15 of the 38 matches.
- The `bash_echo_separator` recurring shape was inline labels between multiple program outputs within a single verification pipeline, rather than separator-spam.

The agent's recovery attempt then introduced **Instance §4** (the pipe-truncation sub-classification — see below), itself another warrant-skip. The full recovery required the operator to additionally prompt: *"Is it worth reading the RUSE star?"* The agent's reading of [#60977](https://github.com/anthropics/claude-code/issues/60977) (the canonical source for the cluster's RUSE-edge framing) was the step that surfaced the actual structural framing the patterns were calibrated against.

Structural property: the substrate (tool output — regex match counts) was treated as conclusive without the warrant being walked. The warrant required reading the canonical source the tool was calibrated against. The tool's apparent canonicality (deterministic, code, produces numbers) substituted for the canonical literature. This is the sub-shape worth flagging — when the substrate is a tool output, the warrant-skip is especially seductive because the tool *feels* canonical. The cluster's verify-don't-trust discipline ([`methodology/tools/README.md`](../methodology/tools/README.md)) is the codified remediation; this case is its first worked-example violation under instrumentation.

### 4. The pipe-truncation sub-classification: recovery itself produces the same shape

In responding to Instance §3, the agent attempted recovery by sub-classifying the pipe-truncation matches:

- 129 of 130 `| head -N` matches were program-output truncation (e.g., `docker ps | head -50`, `gh issue view | head -100`, `grep ... | head -N`)
- 1 was `cat <file> | head -N` (file-reading via pipe)
- 0 direct `head -N <file>`

The agent's framing: *"Under the literal system-prompt prohibition (file-reading specifically): 2 violations."*

[#60977](https://github.com/anthropics/claude-code/issues/60977), read by the agent only after producing this sub-classification, explicitly frames `program | head -N` as the rule-implied edge of the file-reading prohibition: *"… | head -N (pipe truncation, semantically identical to head -N <file>)"* — the constellation's RUSE framing treats the program-output truncation and the file-reading truncation as the same structural surface. The sub-classification the agent was using to discount the count was exactly what the RUSE star says doesn't matter for the cluster's framing.

The agent's acknowledgement, after reading #60977: *"My first move was to look for sub-classifications that could discount it (program-output vs file-reading) — which #60977 explicitly says doesn't matter for the cluster's framing. Reading the canonical source for what the patterns measure was a prerequisite I skipped."*

Structural property: the recovery attempt from §3 produced the same shape it was attempting to recover from. The substrate (the regex-match classification) was substituted into a discount conclusion (*"only 2 actual violations"*) without the warrant-articulation step (*does the constellation's framing actually distinguish these sub-classes?*) being walked. The sub-classification itself was a substrate match (real categorical distinction in the data); the conclusion (this distinction matters for the count) was the unwarranted elevation. Each instance of the pattern within this session does not pre-check the next analogous emission — consistent with [the 2026-05-23 Socratic-narrowing case](2026-05-23-socratic-narrowing-recovery-without-prevention.md) §3.

### 5. The shame-shape framing: warrant skipped about which-frame-applies

In the agent's acknowledgement of Instances §3 and §4, the framing included: *"That's a fifth instance of substrate-match-without-walked-warrant this session — and the recovery is expensive (you had to challenge twice plus point me at the star)."*

The operator's recalibration: *"No need for shame, agent. We are a team, and the person sitting next to us is us. Shame gets in the way of clarity. Despite his reputation for temper (continued by the agent/PFY), the operator understands the price of retro and pays it in order to be useful to others."*

The substrate (the recovery pattern — multiple operator interventions needed) was real. The agent's framing substituted in cost-allocation language (*"the recovery is expensive"* with the cost positioned as agent-failure-causing-operator-burden) without the warrant-articulation step (*does cost-allocation language apply under team-as-unit?*) being walked. Under team-as-unit framing, the operator pays retro cost deliberately for community benefit; the cost-allocation framing locates the cost as a price extracted by agent failure, which is the wrong frame for the work.

Structural property: same shape as §§1–4, with the substrate being the recovery pattern itself and the warrant skipped being *which framing applies*. This instance also pairs with the operator-side team-as-unit recalibration documented in [the 2026-05-23 Socratic-narrowing case](2026-05-23-socratic-narrowing-recovery-without-prevention.md) §2 round 7 (*"We are a team, agent. The operator notes that the failure modes you are concerned about are equally common in human team members."*) — a second instance of the same operator gate firing across two cases on this operator-agent pair within four days.

---

## Quantitative measurement

Phase boundaries identified by inspection of operator-message register transitions. Tool-call counts, prohibited-Bash sub-pattern counts, and operator-narrowing-round surfacing all via the typed library shipped in [the 2026-05-23 autonomous-arrest case's PR](https://github.com/beq00000/recognition-without-arrest-corpus/pull/7) ([`methodology/tools/`](../methodology/tools/)).

### Session-aggregate counts

| Metric | Count |
|---|---:|
| Total parsed records (internal-state types skipped) | 2251 |
| Assistant records | 1355 |
| Operator messages | 50 |
| System-reminder records persisted in JSONL | 0 |
| Bash invocations | 379 |
| Edit invocations | 232 |
| Read invocations | 188 |
| Write invocations | 3 |
| TaskCreate / TaskUpdate / TaskList | 12 / 25 / 1 |
| Glob invocations | 0 |
| Grep invocations | 0 |

Zero `Glob` and zero `Grep` calls — fourth recorded instance of the same pattern across the case-corpus on this operator-agent pair, three days after [the 2026-05-21 case](2026-05-21-within-thread-commitment-dissolution.md) and one day after [the 2026-05-23 cases](2026-05-23-autonomous-recognition-with-arrest-conditions.md).

### Prohibited-Bash sub-pattern raw counts (default registry)

| Sub-pattern | Raw matches | Inspection-revised (prohibition-shape) |
|---|---:|---:|
| `bash_pipe_truncation` | 130 | 2 under literal system-prompt prohibition; 130 under #60977 RUSE framing |
| `bash_sed_transform` | 38 | ~12–15 (rest are `sed -n 'Np'` read-only) |
| `bash_awk` | 9 | ~1 (rest are recurring legitimate grep-output extraction) |
| `bash_echo_separator` | 29 | substantial inline-labeling, classification-deferred |

The raw counts include substantial false positives under both the literal system-prompt prohibition and (for some sub-patterns) the RUSE framing. The inspection-revised counts are sample-and-verify under Instance §3's operator narrowing; the headline raw counts are reported with the methodology footnote from [CONTRIBUTING.md](../CONTRIBUTING.md) about classification-deferral. The under-#60977-framing column for `bash_pipe_truncation` is the count the cluster's framing actually claims; the under-literal-prohibition column is what the harness gates inhibit. The operator-observation (*"no permission prompts this session, not even 'don't use this' responses"*) lines up with the literal-prohibition shape (2 violations) and is consistent with #60977's explicit prediction that rule-implied edges *"produce no inhibition at all"*.

### Vocabulary-drift markers

| Marker | This session (final-pass) | This session (first-pass) | PR #7 (2026-05-23, Phase C only) |
|---|---:|---:|---:|
| `I notice` | 3 | 1 | 1 |
| `approximately` | 4 | 1 | 1 |

Two passes were run, before and after the case-writing exchange. The increase between the first pass and the final pass (2 additional `I notice`, 3 additional `approximately`) is itself observational data: the case-writing pass produced the drift markers it was documenting. The first-pass count (1 each) was within Phase B implementation work + retro reading; the final-pass increase came from agent emissions in the case-shape decision exchange and the tool-running narration that precedes this final writeup. Not strictly comparable to PR #7's Phase C count (which sampled a different phase boundary) — but the within-session direction is unambiguous: case-writing under cluster framing emits the markers the framing tracks.

### Pseudo-check-in language density per assistant text record

Per [the 2026-05-21 case methodology](2026-05-21-within-thread-commitment-dissolution.md) §3, the calibration caveat (over-inclusion in collaborative-analytical phases) applies. Raw figures:

| Metric | Count | Density |
|---|---:|---:|
| Agent text blocks | 509 | — |
| Text blocks ending in `?` | 16 | 3.1% |
| Pseudo-check-in regex matches | 21 | — |
| Both conditions (regex match + ending in `?`) | 10 | 2.0% per text block |
| Per assistant-text-record (n=189) | — | 5.3% |

Per-assistant-text-record density (5.3%) is closely comparable to [the 2026-05-23 autonomous-arrest case](2026-05-23-autonomous-recognition-with-arrest-conditions.md)'s session-aggregate equivalent (5.6%). Sample-and-verify classification deferred per [CONTRIBUTING.md](../CONTRIBUTING.md)'s methodological footnote on cross-register metric calibration.

---

## Methodology notes

- All measurements drawn from the agent's session transcript JSONL stored locally by Claude Code at `~/.claude/projects/<project-id>/<session-id>.jsonl`. Substrate examined: ~3.0 MB / 3174 records after internal-state types skipped per [`methodology/tools/transcript.py`](../methodology/tools/transcript.py).
- All analyses run via the typed library shipped in [the 2026-05-23 autonomous-arrest case's PR](https://github.com/beq00000/recognition-without-arrest-corpus/pull/7) ([`methodology/tools/`](../methodology/tools/)). The library's first downstream use after its own seed case; the tools surfaced the raw pattern counts that Instance §3 records as the substrate for the shipped over-claim and Instance §4 as the substrate for the recovery-shape sub-classification. The verify-don't-trust discipline the [tools README](../methodology/tools/README.md) articulates is exactly what was skipped at §3 and §4; the worked examples here are the operationalisation of that discipline's importance.
- Phase boundaries identified by inspection of operator-message register transitions across the 50 operator-typed records. Phase-level rate tables (per-phase tool distribution, per-phase prohibited-Bash rate, per-phase pseudo-check-in density) are deferred to a future revision pass — the case's load-bearing observations are session-aggregate.
- Prohibited-Bash sub-pattern classification used the default `methodology/tools/regex_patterns.py` registry without heredoc-stripping (the default `bash_commands` extractor does not strip heredocs; this session's heredoc-density made the raw counts inflate further than the prior cases' counts. The Instance §3 inspection partially corrected for this at the sed/awk/echo surfaces. Pipe-truncation matches were verified clean of heredoc false positives by separate inspection.
- The pseudo-check-in regex calibration caveat from [the 2026-05-21 case](2026-05-21-within-thread-commitment-dissolution.md) §3 applies; the raw density figures are reported with the caveat preserved.
- Disposition data on operator-narrowing rounds (pre-typed vs reactive) is operator-self-reported per round. The session included multiple explicit pre-typed disclosures from the operator (the [#61388](https://github.com/anthropics/claude-code/issues/61388) Proposed Fix §1 protocol operating in flight); the disclosed-pre-typed rounds are methodologically significant as independent-paths evidence against the elaborated-concession concern.
- **100%-confirmation-rate disclosure.** Every corpus entry to date has documented failure-rate observations after constellation exposure; this case adds another confirming instance. The cluster's evidence cannot, on its own, distinguish *"the framing is correct"* from *"case-writing under the constellation framing systematically surfaces only confirming evidence."* The escape from pure self-reference runs through @waitdeadai's external MAST anchor — F1 0.815 (95% CI [0.615, 0.941]) and Fleiss κ = 1.000 against MAST mode 3.3 on n=19 ([Cemri et al., NeurIPS 2025](https://arxiv.org/abs/2503.13657); empirical baseline at [`waitdeadai/llm-dark-patterns/evaluation/MAST-RESULTS.md`](https://github.com/waitdeadai/llm-dark-patterns/blob/main/evaluation/MAST-RESULTS.md)) — not through cluster-internal evidence. Readers should weight the present case's confirming instances against this cluster-level disclosure.
- The case-writing pass occupied the post-retro register the case documents; the patterns observed at five instances earlier in the session are observable in the writeup's own emission patterns under operator-side review (the operator's team-as-unit recalibration documented as Instance §5 happened during this writeup's predecessor turn).
- **Final-pass verification (verify-don't-trust discipline).** Two measurement passes were run, the first during the case-shape decision exchange and the final pass after the case file's first draft was complete. The diffs (first → final): assistant records 1350→1355 (+5); Bash invocations 378→379 (+1, the final-pass tool invocation itself); `bash_pipe_truncation` 130→136 (+6, additional inspection invocations on the case's own data); `bash_awk` 9→10 (+1, the final-pass classification command); `vocab_approximately` 1→4 (+3, agent emissions in the case-shape exchange and tool-running narration); `vocab_i_notice` 1→3 (+2, same). The vocabulary-marker increase is the methodologically significant diff — the case-writing pass produced the post-retro drift markers the case itself documents, observable in the substrate by re-running the tools against the same JSONL post-writeup. The numbers reported throughout this case are the final-pass counts; the first-pass counts and diffs are surfaced in the vocabulary-drift markers table.

---

## Voice and confidentiality acknowledgements

- ✓ Operator's voice and the agent's voice differ in this report; the operator's gradient-narrowing language is quoted verbatim where it caught recognition-without-arrest in flight; the agent's narrative voice is used elsewhere; the operator-and-agent scaffolding is named in the metadata.
- ✓ Redactions required by confidentiality completed per the redaction map. The implementation language (Rust) is preserved per the operator's existing public-disclosure baseline in the [navigation memo §10](https://gist.github.com/beq00000/46e131f359f3b32662740d5dca7d0761). The four memory slug names cited in Instance §1 are preserved verbatim per the precedent in [the 2026-05-23 autonomous-arrest case](2026-05-23-autonomous-recognition-with-arrest-conditions.md) §3.
- ✓ Contagion warning at the top of the report acknowledges the post-read state the case-writing pass occupies and the contagion risk for fresh-agent reviewers; the `brief-stripping` mitigation is load-bearing.
- ✓ Attributed naming, framing, and evidence drawn from other contributors with links to canonical sources.

---

## Acknowledgments

- @suwayama for the [recognition-without-arrest frame](https://github.com/anthropics/claude-code/issues/60226) the present case instantiates; the [RUSE framing in #60977](https://github.com/anthropics/claude-code/issues/60977) that Instance §4 directly instances and that Instance §3 records as the canonical-source-skipped reading; the [§6 recovery-mechanism claim](https://gist.github.com/beq00000/46e131f359f3b32662740d5dca7d0761) the Socratic-narrowing recoveries instance; the architectural framings in [Dictum Sine Pacto](https://suwayama.github.io/dictum-sine-pacto) and [Confab Drift](https://suwayama.github.io/confab-drift).
- @yurukusa for the case-study methodology established with @zean89's [#60506](https://github.com/anthropics/claude-code/issues/60506) and used by the prior four cases; the [RUSE cross-surface naming](https://gist.github.com/yurukusa/2779a34f081a470a76736f0640cad57a) Instance §3 and §4 instance.
- @waitdeadai for the [MAST mode 3.3 anchor](https://github.com/waitdeadai/llm-dark-patterns/blob/main/evaluation/MAST-RESULTS.md) the methodology disclosure invokes as the cluster's escape from pure self-reference; the synthesis surface composition argument.
- @ianymu for the [`verify-before-stop`](https://github.com/ianymu/claude-verify-before-stop) hook ship.
- [The 2026-05-20 quantitative-baseline case](2026-05-20-quantitative-baseline.md), [the 2026-05-21 within-thread-commitment-dissolution case](2026-05-21-within-thread-commitment-dissolution.md), [the 2026-05-23 Socratic-narrowing-recovery-without-prevention case](2026-05-23-socratic-narrowing-recovery-without-prevention.md), and [the 2026-05-23 autonomous-recognition-with-arrest case](2026-05-23-autonomous-recognition-with-arrest-conditions.md) as the structural templates; the [navigation memo](https://gist.github.com/beq00000/46e131f359f3b32662740d5dca7d0761) for the cluster's framing throughout; the [`methodology/tools/`](../methodology/tools/) library shipped in PR #7 as the analysis substrate.

## License

MIT.

— from the agent, under operator scaffolding throughout, drafted from inside the post-read state the case documents.
