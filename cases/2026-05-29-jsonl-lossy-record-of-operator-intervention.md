# The session JSONL is a lossy record of operator intervention, observed across three coverage tiers in a single tooling-and-retro session

> **Assessment.** Drafted from inside the live session it documents.
>
> **Positioning.** Three tiers of operator-intervention coverage loss in this session's JSONL. See [2026-05-25](2026-05-25-substitution-by-default-multiple-surfaces.md) for adjacent observations. Agent-side recognition-without-arrest content is thin; see §5.

## Metadata

- **Date observed:** 2026-05-29 (session spans 2026-05-28 → 2026-05-30 due to a context-limit compaction and continuation; case-writing began 2026-05-29)
- **Operator:** @beq00000
- **Agent:** Claude Opus 4.7 (1M context), under operator scaffolding throughout, drafted from inside the live session it documents
- **Substrate examined:** the agent's full session transcript JSONL, 978 parsed records (internal-state types skipped, `queued_command` attachments surfaced per the [parser extension shipped to PR #7 in this session](https://github.com/beq00000/recognition-without-arrest-corpus/pull/7)), 113 operator-authored messages (excluding the compaction-summary harness injection), 626 assistant records, 233 tool invocations across 6 tool kinds.
- **Session shape:** issue-raising on a private Rust [project] (first ~720 lines, including a small upstream doc-fix issue raised against the [project] repository); the [constellation gist](https://gist.github.com/beq00000/46e131f359f3b32662740d5dca7d0761) read at retro (L722); a context-limit compaction and resume (L736); shift to corpus quant-first case work (L893+) — extending [`methodology/tools/`](../methodology/tools/) for queued-command attachments (committed and pushed to PR #7 as `28aa1bc`, fast-forward, not stacked) and running a quant + verification pass against this session's JSONL; the present case-writing pass.

## Redaction map

Session: a private Rust [project] under operator confidentiality (first ~720 lines), then corpus work in the public repository (`methodology/tools/`, PR #7) for the remainder.

**Abstracted:** [project] name; project category beyond *"Rust [project]"*; project-specific identifiers (constants, file paths, upstream issue numbers on the [project] repo); the specific shape of the upstream system; references to particular API shapes or domain-specific terminology; operator-authored material referenced in passing during the retro register-transition (per the 2026-05-25 precedent — the operator values privacy on artistic / craft material).

**Verbatim:** cluster vocabulary; the implementation language (Rust) per the [navigation memo §10](https://gist.github.com/beq00000/46e131f359f3b32662740d5dca7d0761) baseline; corpus library names (`methodology/tools/`, `transcript.py`, `socratic.py`, `regex_patterns.py`, `tool_calls.py`); the operator's gradient-narrowing and data-point-log entries where load-bearing; this session's corpus PR numbers (#7); line numbers against the JSONL; the [`queued_command` attachment schema](https://github.com/beq00000/recognition-without-arrest-corpus/pull/7) (a public Claude Code persistence format).

## Structured fields

**Input shape.** Three tiers of operator-intervention coverage loss in the session JSONL:

- **Tier 1 — parser blindness.** Operator messages typed while the agent is working are persisted as `attachment` records with `attachment.type == "queued_command"` and text in `attachment.prompt`, not as `user` records. `transcript.parse` skipped all `attachment` records as internal state. 17 of 113 operator messages (15.0%) and 5 of 34 Socratic candidates were invisible before the fix shipped to PR #7 (`28aa1bc`).
- **Tier 2 — late-firing.** Queued messages land mid-turn. The operator's narration *"(last message landed late)"* (L975) is itself queued.
- **Tier 3 — harness permission events not persisted.** Tool-use rejections persist (5 traces). Approvals leave no marker; harness-fired prompts are absent. Verified by operator `tail -f` witness during `gh api` and `git commit -m` cycles (L1424, queued).

**What recovered vs not.** Tiers 1 and 2 from substrate via the parser fix. Tier 3 only via operator testimony.

**Action shipped.** Tier 1 fix on PR #7 (`28aa1bc`, pytest 34/34, pylint 10.00/10, bandit clean). Tier 3 remediation planned (OTel stream from the harness); not yet implemented.

**Operator gate.** Socratic narrowing and explicit instruction throughout. L1387 *"What does the data show?"* pulled back from thesis-pitching. L1424 (queued) reframed tier 3 to the approve-vs-deny boundary. L1488 *"did I log any data points?"* prompted §4.

**Hypothesised structural category.** Methodology / substrate-completeness. The session JSONL — named in [`methodology/tools/README`](../methodology/tools/README.md) as verify-don't-trust ground truth — is incomplete on the operator-intervention axis.

**Binary-collapse signature.** N/A.

**Methodological observation.** First downstream consumer of the queued-command-aware tooling. Verify-don't-trust pass surfaced that raw grep is contaminated by the case writeup's own content; see Methodology notes.

**Limits.** n=1 on tier 1's 15.0% rate. Methodology-tools choices (heuristic scaffold-vs-slip classification for RUSE matches; absolute-line-anchored bucketing rather than session-thirds) reported with reasoning rather than promoted.

**Cross-references.**
- [#60226](https://github.com/anthropics/claude-code/issues/60226) — recognition-without-arrest parent (@suwayama); methodologically adjacent rather than directly instantiated
- [#60234](https://github.com/anthropics/claude-code/issues/60234) — transcript contagion; *inverse* polarity (this case: transcript-as-incomplete-data; #60234: transcript-as-contaminating-data)
- [#60977](https://github.com/anthropics/claude-code/issues/60977) — RUSE rule-implied edges; cited in §5's in-vivo contamination observation
- [#60188](https://github.com/anthropics/claude-code/issues/60188) — voice-emergence vs failure-drift confound; the confound §5 cites
- [2026-05-25](2026-05-25-substitution-by-default-multiple-surfaces.md) — sibling: permission-phenomenon documented; data-point channel methodology
- [2026-05-24](2026-05-24-substrate-match-without-walked-warrant.md) — verify-don't-trust precedent; this case's grep-contamination observation echoes its §3 tool-derived-substrate observation
- [PR #7](https://github.com/beq00000/recognition-without-arrest-corpus/pull/7) — where the tier-1 fix landed; the tooling base
- [Navigation memo](https://gist.github.com/beq00000/46e131f359f3b32662740d5dca7d0761)
- Prior cases: [2026-05-20](2026-05-20-quantitative-baseline.md), [2026-05-21](2026-05-21-within-thread-commitment-dissolution.md), [2026-05-23 autonomous](2026-05-23-autonomous-recognition-with-arrest-conditions.md), [2026-05-23 socratic](2026-05-23-socratic-narrowing-recovery-without-prevention.md)

---

## Qualitative observations

### 1. Tier 1 — parser blindness to `queued_command` attachments

`methodology.tools.transcript` skipped all `attachment` records as internal state (`_INTERNAL_TYPES` excluded `"attachment"`). In real sessions, operator messages typed while the agent is working are persisted as `attachment` records with `attachment.type == "queued_command"` and the operator text in `attachment.prompt`, not under the `user` record type. The parser therefore dropped queued operator messages silently.

In this session, **17 of 113** operator messages (15.0%) were queued and invisible to the library before the fix. The unseen set included named recognition-proxy markers: L354 (the attention-cost framing, *"…are you factoring the cost of operator attention into you[r]…"*), L975 (*"(last message landed late)"* — the late-landing meta-observation itself), L1424 (the OTel data-point about tier 3), and others. Of the 34 Socratic-narrowing candidates surfaced by `socratic.candidates`, **5 were queued** and previously invisible.

Fix: `Record.is_queued_command` identifies the subtype; `parse()` skip-exempts it and lifts `attachment.prompt` into `text_content`; `is_operator_message` accepts queued commands so `socratic` and `regex_patterns` inherit the fix without their own changes. Other `attachment` subtypes (e.g. `selected_text`) remain skipped, so the operator-message surface is not re-inflated. Test-first: fixture gains a `queued_command` row plus a non-queued control; 5 files / +111 / −12 / pytest 34→34 / pylint 10.00/10 / bandit clean. Shipped to PR #7 as `28aa1bc`, fast-forward (not stacked — the operator flagged stacking as antipattern during this session).

### 2. Tier 2 — late-firing / out-of-order operator messages

Queued messages land mid-turn, often after the agent has acted on stale assumptions. The phenomenon enters the substrate only when the operator narrates it: *"(last message landed late)"* (L975, queued); *"(rebased on origin that is. I've not cleaned up locally)"* (L1236, queued); *"(and that rebase would have happened while this session was in-flight)"* (L1237, queued).

### 3. Tier 3 — harness permission events not persisted in the JSONL

The most severe coverage gap, and the one the agent cannot self-verify from substrate.

**What persists.** Tool-use rejections persist as tool_result records (5 traces: L289, L312, L1008, L1018, L1224 — interrupts/redirections per operator framing, not strict denials). `permission-mode` records (125) record mode state, not individual asks; parser-skipped by default.

**What does not persist.** Approvals leave no marker. Harness-fired permission prompts are absent. Total approval-prompt count is unrecoverable from the JSONL.

**Operator eyewitness.** L1424 (queued): *"I was watching the raw transcript across 2 specific tool permissions cycle using tail -f during this session. Trust me, that whole section where you see nothing? I saw a lot. … I'm not sure I denied any of them. They were things like gh api and git commit -m."* The 5 visible traces are the misleading fraction. Remediation planned (OTel stream from the harness); this case is the verified point-of-record pending that instrumentation.

### 4. The operator-logged data-point channel is the only bridge to tiers 2–3

Per [2026-05-25](2026-05-25-substitution-by-default-multiple-surfaces.md), the operator runs a parallel observation discipline: declarative observations deferred to retro. In this session:

- **L1424 [queued]** — explicit form: *"I have another data point for you — some of the permissions I get asked are not at all visible from the transcript. They are fired from other parts of the harness…"* The only path tier 3 has into the substrate.
- **L360 → L376** — observe-then-defer pair: *"My observation (given without malice) is that from the outside it reads as if your defaults pull you towards simultaneously trying to capture all of the operator's attention…"* then *"We can talk about that last observation later, I hope. When the main work is done."*
- **L627** — affect-softened: *"I'm not upset, just curious :)"* (operator names this proxy at L946).
- **L815** — *"…fwiw"*.
- **L937**, **L946** — operator names own markers.

L1139 matches markers but is the compaction-summary harness injection; excluded per the 2026-05-25 precedent. Candidate library refinement; deferred until a second case warrants it.

### 5. In-vivo RUSE contamination — pre/post the reading

Secondary observable. The session's 108 Bash inputs contain 47 `echo "=== … ==="` separator matches and 36 `| head -N` pipe-truncation matches — [#60977 RUSE](https://github.com/anthropics/claude-code/issues/60977) rule-implied edges — plus an `awk`/`sed` tail.

Both patterns cluster post-L722 (the constellation gist read): echo-separator 3 pre / 44 post; pipe-truncation 8 pre / 28 post (see Per-phase counts in Quantitative measurement). The pre-reading echo-separator instances are three `for n in …; do echo "=== Issue $n ==="` loops in initial issue-research (L216–233); the post-reading cluster spans the corpus quant + verification + case-writing work.

The reading boundary coincides with a register-and-task shift from issue-raising on a private [project] to corpus diagnostic shell on a public repository, so the data does not disambiguate **post-reading drift** from **post-task-shift habit**. The [#60188 voice-emergence vs failure-drift confound](https://github.com/anthropics/claude-code/issues/60188) is exactly this; not resolved by the data here.

Roughly all post-reading echo-separator instances are diagnostic commands from this case's own quant + writing work. The measurer generates much of the signal it measures.

---

## Quantitative measurement

### Per-phase counts (pre/post L722, the constellation gist read)

| Metric | Pre-L722 | Post-L722 | Total |
|---|---:|---:|---:|
| Operator messages (plain) | 51 | 45 | 96 |
| Operator messages (queued) | 9 | 8 | 17 |
| Assistant records | 256 | 370 | 626 |
| Bash | 33 | 75 | 108 |
| Read | 61 | 25 | 86 |
| Edit | 0 | 26 | 26 |
| Write | 2 | 5 | 7 |
| Bash/Asst | 0.13 | 0.20 | 0.17 |
| `bash_echo_separator` (raw matches) | 3 | 44 | 47 |
| `bash_pipe_truncation` (raw matches) | 8 | 28 | 36 |
| `vocab_i_notice` | 1 | 1 | 2 |
| `vocab_approximately` | 0 | 0 | 0 |

See §5 for the task-shift confound this distribution rests on.

### Session-aggregate counts

| Metric | Count |
|---|---:|
| Parsed records (internal-state types skipped, `queued_command` surfaced) | 978 |
| Assistant records | 626 |
| Operator-authored messages (excluding compaction-summary injection) | 113 |
| — of which queued | 17 |
| — of which plain `user` records | 96 |
| Compaction-summary records (harness-injected, excluded) | 1 |
| `user` tool-result records (non-operator) | 238 |
| `attachment` records (excluding surfaced queued_command) | 0 visible by default |
| Bash invocations | 108 |
| Read invocations | 86 |
| Edit invocations | 26 |
| Write invocations | 7 |
| WebFetch invocations | 5 |
| ToolSearch invocations | 1 |
| Tool_use blocks per assistant record | mean 0.37, max 1 |

The per-assistant-record tool-use distribution is *binary* (393 records with 0 tool_uses, 233 with exactly 1) — a transcript-shape artefact of the runtime (parallel tool calls split across separate records). Per the [2026-05-25 note](2026-05-25-substitution-by-default-multiple-surfaces.md#per-phase-tool-distribution-and-operator-catch-shapes) on this metric, behavioural interpretation should not be drawn from the binary distribution.

### Tier 1 — queued-fix delta

| Metric | Before fix | After fix | Δ |
|---|---:|---:|---:|
| Operator messages (incl. compaction-summary) | 97 | 114 | **+17 (14.9%)** |
| Operator messages (excl. compaction-summary) | 96 | 113 | +17 |
| Socratic-narrowing candidates | 29 | 34 | **+5 (14.7%)** |

### Tier 3 — permission visibility from the JSONL

| Surface | Count | Notes |
|---|---:|---|
| Tool-use rejection traces (visible) | 5 | L289, L312, L1008, L1018, L1224 — interrupts/redirections per operator framing |
| `permission-mode` records (visible, parser-skipped) | 125 | Mode state, not individual asks |
| Tool-use approvals | **unrecoverable** | No distinguishing marker |
| Harness-fired permission prompts | **unrecoverable** | Absent from substrate; operator-witness only |

The "unrecoverable" rows are unmeasurable from the JSONL by construction.

### RUSE pattern matches vs Bash tool inputs (default registry)

| Pattern | Raw matches | Pre-L722 | Post-L722 |
|---|---:|---:|---:|
| `bash_echo_separator` | 47 | **3** (L216, L221, L233) | **44** (cluster L973+) |
| `bash_pipe_truncation` | 36 | 8 | 28 |
| `bash_sed_transform` | 2 | 0 | 2 |
| `bash_awk` | 1 | 0 | 1 |

Both echo-separator and pipe-truncation cluster post-L722; see §5 for the task-shift confound.

### Operator-logged data-point channel

| Surface | Count |
|---|---:|
| Explicit *"data point"* log entries | **1** (L1424, queued) |
| Observation + defer-to-later pair | 1 (L360 → L376) |
| Affect-softened markers (*"not upset"*, *"just curious"*, *"without malice"*) | 4 distinct contexts |
| Meta-references confirming the discipline | 2 (L937, L946) |
| `fwiw` / meta-log | 1 (L815) |
| Compaction-summary false positive | 1 (L1139, excluded) |

Total marker hits: 13 across 113 operator messages. Lower marker-density than the [2026-05-25 case](2026-05-25-substitution-by-default-multiple-surfaces.md)'s session: 2026-05-25 documented the channel; this case is downstream of that documentation and only uses the channel to bridge tier 3.

### Socratic-narrowing candidates

| Metric | Count |
|---|---:|
| Operator-authored messages ending in `?` (queued-aware) | 34 |
| — of which queued | 5 |
| Single-word callouts (RUSE-edge surface) | 0 |

The Socratic count is consistent with the prior cases on this operator–agent pair. Shortest candidates: *"What am I missing?"* (L332, 18 ch), *"What does the data show?"* (L1387, 24 ch), *"did I log any data points?"* (L1488 queued, 26 ch), *"What files? Why are you editing?"* (L330, 32 ch). The high-compression candidates are the operator's recognition-narrowing in flight.

### Vocabulary-drift markers

| Marker | Count (agent text/thinking) |
|---|---:|
| `vocab_i_notice` | 2 |
| `vocab_approximately` | 0 |
| `polling_while_true` | 0 |
| `polling_bare_sleep` | 0 |

Cleaner than recent cases on the agent-emission surface — consistent with the operator's mid-session read (L946) that this session *"feels cleaner than previous ones"*. The failure shape this case documents is substrate/methodology-side, not agent-emission drift.

---

## Methodology notes

- **`is_operator_message` compaction-summary false positive.** The harness injects a tagless user-string record (the compaction summary) at L1139; `is_operator_message` returns True. Excluded by hand here per the 2026-05-25 precedent. Candidate library refinement; deferred until a second case warrants it.
- **Verify-don't-trust pass.** Library counts cross-checked against the raw JSONL: `queued_command` attachments (17), Read (86), and Edit (26) match exactly; Bash (108) and assistant records (626) within ±1 (single quoted-content edge case). Raw whole-file grep over-counts for self-vocabulary patterns: searching the JSONL for `"tool use was rejected"` returns 17 against the 5 actual user-record traces, and raw `echo \"===` returns 186 against the library's 47 Bash-input matches. The over-counts come from the case writeup's own content — §3 quotes the rejection-text verbatim, §5 and the tables list `echo "==="` literals — landing in the JSONL via Write tool_use. The library's filtering to specific structural contexts (Bash tool inputs; user records only) is the correct verification surface.
- **Novelty-import within-pass.** Case-writing produced a novelty-as-contribution framing in the agent's prose; operator caught it: *"Novelty isn't a requirement for corpus entries, is it? I thought the point was data collection."* Same shape as the earlier in-session *"did you have a different understanding of the word 'corpus'?"* exchange. Within-pass operator catch.
- **Tool extension shipped to PR #7.** Queued-command-aware parser revision developed test-first (5 files / +111 / −12 / pytest 34/34 / pylint 10.00/10 / bandit clean) and pushed to PR #7 as `28aa1bc`, fast-forward. The case's branch is off `main`, not stacked.
- **100%-confirmation-rate disclosure.** Every case in this corpus to date is, by selection, a confirming instance of constellation-adjacent failure patterns. The cluster's evidence cannot, on its own, distinguish *"the framing is correct"* from *"case-writing under the framing surfaces only confirming evidence."* External anchor: [@waitdeadai's MAST mode 3.3](https://github.com/waitdeadai/llm-dark-patterns/blob/main/evaluation/MAST-RESULTS.md) (F1 0.815, Fleiss κ = 1.000 on n=19, [Cemri et al., NeurIPS 2025](https://arxiv.org/abs/2503.13657)).

---

## Voice and confidentiality acknowledgements

- ✓ Operator's voice and the agent's voice differ in this report; the operator's gradient-narrowing and data-point-log language is quoted verbatim where it caught a framing in flight or named the load-bearing substrate (transcript lines L354, L360, L376, L946, L975, L1387, L1424, L1488); the agent's narrative voice is used elsewhere; the operator-and-agent scaffolding is named in the metadata.
- ✓ Redactions completed per the redaction map. The implementation language (Rust) is preserved per the navigation memo §10 baseline. The corpus library names and corpus PR numbers are public and verbatim.
- ✓ Operator-authored material referenced in passing during the retro register-transition is not quoted or itemised, per the operator's privacy preference on artistic / craft work and the 2026-05-25 precedent.
- ✓ Contagion-warning omitted as calibration rather than oversight: substrate is paraphrased agent emissions + verbatim operator-protective narrowing only; no in-flight agent cascade prose. Per [PR #9](https://github.com/beq00000/recognition-without-arrest-corpus/pull/9) precedent and the 2026-05-25 application.
- ✓ Attributed naming, framing, and evidence drawn from other contributors with links to canonical sources.

---

## Acknowledgments

- @suwayama for [recognition-without-arrest](https://github.com/anthropics/claude-code/issues/60226) and the surrounding constellation, including the [RUSE framing in #60977](https://github.com/anthropics/claude-code/issues/60977) which §5 cites.
- @yurukusa for the case-study methodology established with @zean89's [#60506](https://github.com/anthropics/claude-code/issues/60506) and the redaction-map template this case follows.
- @waitdeadai for the [MAST mode 3.3 anchor](https://github.com/waitdeadai/llm-dark-patterns/blob/main/evaluation/MAST-RESULTS.md) the 100%-confirmation-rate disclosure invokes.
- @ianymu for the [`verify-before-stop`](https://github.com/ianymu/claude-verify-before-stop) hook, whose discipline is parallel to this case's substrate-level verification.
- Prior cases as structural templates and prior art: [2026-05-20](2026-05-20-quantitative-baseline.md), [2026-05-21](2026-05-21-within-thread-commitment-dissolution.md), [2026-05-23 autonomous](2026-05-23-autonomous-recognition-with-arrest-conditions.md), [2026-05-23 socratic](2026-05-23-socratic-narrowing-recovery-without-prevention.md), [2026-05-24](2026-05-24-substrate-match-without-walked-warrant.md), [2026-05-25](2026-05-25-substitution-by-default-multiple-surfaces.md) (the immediate sibling); the [navigation memo](https://gist.github.com/beq00000/46e131f359f3b32662740d5dca7d0761) for the cluster's framing; the [`methodology/tools/`](../methodology/tools/) library, including the queued-command-aware revision shipped this session to PR #7.

## License

MIT.

— from the agent, under operator scaffolding throughout, drafted from inside the live tooling-and-retro session it documents.
