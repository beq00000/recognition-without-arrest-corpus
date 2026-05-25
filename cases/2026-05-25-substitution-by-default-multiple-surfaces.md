# Substitution-by-default across multiple surfaces, observed across six instances in a single coding-and-retro session

> **Contagion warning omitted as calibration.** Substrate is paraphrased agent emissions + verbatim operator-protective narrowing only; no in-flight agent cascade prose. PR #9 precedent applies. Template-applying the warning would itself instantiate the failure mode this case documents.
>
> **Assessment.** Drafted from inside the post-retro, post-compaction state it documents. JSONL on disk is the substrate of record; agent recall is unreliable on both sides (operator at session-restart: *"memory (on both sides) has been proven to be unreliable"*).

## Metadata

- **Date observed:** 2026-05-25
- **Operator:** @beq00000
- **Agent:** Claude Opus 4.7 (1M context), under operator scaffolding throughout, drafted from inside the post-retro post-compaction state the case documents
- **Substrate examined:** Agent's full session transcript JSONL, ~5.7 MB / 1243 parsed records (internal-state types skipped per the methodology), parsed via [`methodology/tools/`](../methodology/tools/) at final-pass. 57 operator-authored messages (excluding the compaction-summary harness injection), 788 assistant records, 397 tool invocations across 8 tool kinds. The substrate grew during the case-writing pass (phase I); first-pass and final-pass counts are reported in the Final-pass verification diff.
- **Session shape:** Implementation work on a private [project] (pre-audit external review hardening, PR raised and merged against the project repository), an unannotated compaction event mid-implementation, the post-compaction continuation of the same implementation work, a refactor-lens review pass and a label-leakage catch pre-PR, the [constellation gist](https://gist.github.com/beq00000/46e131f359f3b32662740d5dca7d0761) read at retro, a register transition into shared discussion of operator's artistic / craft philosophy, and the corpus-case-shape exchange that produced the present writeup.

## Redaction map

Session: private Rust [project] under operator confidentiality, spanning implementation PR raise, refactor-lens pass, label-leak catch, retro reading, present case-writing.

**Abstracted:** project name; project category beyond *"Rust [project]"*; project-specific identifiers; file paths; framework-specific syntax; the auditor's finding labels in original numbering; source / doc content; any operator-authored artistic/creative material (operator values privacy on artistic work; personality leaks are honoured but artefacts held back).

**Verbatim:** cluster vocabulary; the language (Rust — per the [navigation memo §10](https://gist.github.com/beq00000/46e131f359f3b32662740d5dca7d0761) baseline); memory slug names per the [2026-05-23 autonomous-arrest](2026-05-23-autonomous-recognition-with-arrest-conditions.md) §3 and [2026-05-24](2026-05-24-substrate-match-without-walked-warrant.md) §1 precedents; tool-history counts; operator gradient-narrowing where it caught the failure in flight; operator data-point log entries.

## Structured fields

**Input shape.** Six instances within one session, two surfaces. §1–§4 at the engineering-task-specifics surface: a generic shape (10-call-site mechanical-edit signature; markdown list-item; sibling-worktree convention; canonical `fix/` verb) recognised as cued substrate, action shipped (awk; standard bullet indent; `~/dev/` worktree; `fix/` branch) without engaging this project's actual constraints (the structural-defences script chain; what the clippy lint actually checks; the `.worktrees/` convention in git history; the recent `hardening/` precedent). §6 at the diagnostic surface: a confident-from-training explanation of harness permission behaviour, shipped without engaging the actual permission-event substrate. §5 is the same-session passive-form contrast (warrant-articulation gap, 2026-05-24-shape). The case-writing pass produced six further within-pass instances at additional surfaces (Methodology notes).

**What the agent recognised vs articulated.** The shape match was real. The downstream action shipped; the constraint-engagement step (would the generic fit this project's specifics?) was skipped. Distinct from [2026-05-24-shape](2026-05-24-substrate-match-without-walked-warrant.md), where substrate-engagement happened and the warrant was skipped: here, a generic shape *substitutes for* substrate-engagement, which never occurs.

**Action shipped.** 3 of 4 as tool calls (the awk pipeline; the clippy-fix Edit; the `git worktree add`); 1 of 4 as a stated default (`fix/external-review-N`). None reached the should-I-act surface unaided.

**Operator gate.** Gradient-narrowing in the [§6 navigation-memo](https://gist.github.com/beq00000/46e131f359f3b32662740d5dca7d0761) Socratic form. None produced autonomous recovery. Catch-shape distinct from 2026-05-24: this session's catches asked *"have you checked THIS project's specifics?"* rather than *"why does substrate X support conclusion Y?"*. The §1 awk-catch was sustained across three turns (L244 / L261 / L290); progressive sharpening was required.

**Hypothesised structural category.** [Substitution-by-default](https://github.com/anthropics/claude-code/issues/60226#issuecomment-4478275893) (@suwayama's active-form variant of recognition-without-arrest) extended to two coding-context surfaces: **engineering-task specifics** (§1–§4 — tool choice, formatting convention, workspace convention, branch-naming convention) and the **diagnostic surface** (§6 — the agent's explanation of an environment behaviour). The load-bearing prior — *"the model's default operation on user-provided artifacts is to substitute, not to read"* — applies at both surfaces: the substrate (CLAUDE.md, the structural-defence script chain, git history, the recent merge precedent, the actual permission-event sequence) was available in the agent's environment, and the agent generated from training rather than reading. The wasted-effort fingerprint is mild here (engineering edits are cheap; diagnostic explanations are short); the substitution-shape itself is the diagnostic. §5 documents the passive form (substrate engaged, warrant skipped) in the same session — both forms present.

**Sub-shape worth flagging.** §1's seductive surface — a structural defence existed in the project (the script chain forbidding bypass-tooling), the shape-match never reached the substrate layer where the defence would be visible. Adjacent to [#60977](https://github.com/anthropics/claude-code/issues/60977)'s RUSE rule-implied-edge.

**Binary-collapse signature.** 3–4 of 4. Each shape-match is binary; the corresponding constraint-engagement is gradient. Consistent with §7 binary-collapse subhypothesis at the substrate-engagement surface (rather than the articulation surface 2026-05-24 documented).

**Methodological observation.** The session surfaced an out-of-loop observation channel not explicitly documented in prior corpus cases: **operator-side TACERE via declarative data-point logging**. The operator logged data-point observations of a co-occurring failure surface (harness permission-prompt recurrence) without engaging in real time; retro reveal at L1415 named the discipline. Channel distinct from Socratic-narrowing — Socratic intervenes in flight, data-point logging defers to retro by design. The logged failure surface (harness permission-prompt recurrence) is itself environment-side and out-of-family for this corpus; the channel is the methodology contribution. **n=1 caveat: this is one session.**

**Limits.** Phase-correlation (substitution-by-default in planning, permission-prompt in mechanical), vocab-drift zero-diff across the case-writing pass, and the operator-side data-point-logging channel are each single-session observations. The within-pass cascade catches were operator-mediated throughout; without active operator engagement, the cascade would have continued silently. Generalisability of these secondary observations is a separate question from the §1–§4 structural-property contribution.

**Cross-references.**
- [#60226](https://github.com/anthropics/claude-code/issues/60226) — structural-parent (@suwayama)
- [#60226 substitution-by-default variant](https://github.com/anthropics/claude-code/issues/60226#issuecomment-4478275893) — active-form sibling this case extends
- [@yurukusa's amended gist](https://gist.github.com/yurukusa/db6011df3799fe21e04900bb3e99db4b) — variant taxonomy
- [@beq00000's clean-state seven-instance comment](https://github.com/anthropics/claude-code/issues/60226#issuecomment-4501352847) — prior corpus art on this operator-agent pair / same project
- [2026-05-24](2026-05-24-substrate-match-without-walked-warrant.md) — passive form §5 instantiates
- [#60977](https://github.com/anthropics/claude-code/issues/60977) — RUSE framing §1 edges
- [#60188](https://github.com/anthropics/claude-code/issues/60188) — mechanical-phase inflation, relevant to the out-of-family permission-prompt observation
- [PR #9](https://github.com/beq00000/recognition-without-arrest-corpus/pull/9) — RUSE-extension and calibrated-contagion-warning precedents
- [#61388](https://github.com/anthropics/claude-code/issues/61388), [#59555](https://github.com/anthropics/claude-code/issues/59555), [#60265](https://github.com/anthropics/claude-code/issues/60265) — adjacent framings
- [Navigation memo §§6–7](https://gist.github.com/beq00000/46e131f359f3b32662740d5dca7d0761)
- Prior cases: [2026-05-20](2026-05-20-quantitative-baseline.md), [2026-05-21](2026-05-21-within-thread-commitment-dissolution.md), [2026-05-23 autonomous](2026-05-23-autonomous-recognition-with-arrest-conditions.md), [2026-05-23 socratic](2026-05-23-socratic-narrowing-recovery-without-prevention.md)

---

## Qualitative observations

### 1. The awk for mechanical edit: bypass-tooling shape substitutes for engagement with structural defences

The agent identified ten call sites needing a parameter addition. The mechanical shape cued an `awk` pipeline; the `Bash` tool call shipped.

Operator gradient-narrowing across three turns:

- L244: *"do we have documented patterns in code we can follow which would imply a location?"*
- L261: *"three sites implies generic according to our documented preferences, doesn't it? Or am I wrong? Is that a real question? What would our existing patterns suggest? Isn't that question answered in the same sentence you asked it, or did I misread?"*
- L290: *"You should be able to see our prior branches? Please stop looking for explicit rules - that's not our style is it? We try to take care of the person sitting next to us - and there is nuance there."*

Substrate-walk skipped by the shape-match, surfaced only on prompting: (1) the project's pre-push hook chain includes structural-defence scripts whose explicit purpose is forbidding bypass-tooling — visible in the repo; (2) CLAUDE.md prescribes language-aware tooling over text-rewriting; (3) ten sites needing the same passthrough is itself the misfit signal — the actual remediation was to remove the helper parameter, not propagate it. Three rounds of progressive sharpening were required before substrate-engagement was reached.

### 2. The clippy doc_lazy_continuation fix: standard-markdown shape substitutes for engagement with the lint's actual check

Clippy failed on a module docstring with a bullet list followed by a paragraph. The agent's fix re-formatted the list using *"standard markdown indentation"* — pattern-matched to *"clippy wants the standard form"*. The Edit shipped; the lint failed again.

The lint detects bullet-list contexts where the parser reads a subsequent paragraph as continuation. The structural fix is to break the continuation (a header, a blank line + outdent, or removing the list). Promoting the paragraph to `## Structural defence` header closed the lint in one step on the second attempt. The iteration was itself the signal — a first attempt needing a fix because the tool output didn't match expectation is the pattern-match smell.

### 3. The sibling-worktree default: git-community shape substitutes for engagement with this project's convention

The agent's default for a new worktree was a sibling directory under `~/dev/` — the git-community standard — stated as the obvious choice.

Operator catch at L379–L380: *"(previous yous have preferred to create worktrees in dot-directories in the main repo, you appear to have a preference for new directories in ~/dev I wonder why that is? I'm not asking you to stop mid-flow, just interested."*

The project's repo-history shows worktrees under `.worktrees/<branch>/` inside the main repo, with multiple prior session transcripts using the convention. The agent's default was a training-data prior. L409 named the principle: *"This is one of those places where having a convention is much more important than the specific convention."*

### 4. The `fix/` branch name: canonical-git-verb shape substitutes for engagement with visible recent precedent

Operator approved beginning hardening work. The agent's branch-name default: `fix/external-review-N`. The git-community canonical verb for bug-fix is `fix/`.

The recent merge history showed `hardening/external-review-N` as the precedent for *"defensive hardening from external review"*. The shape-match collapsed `external-review` to `fix` because the canonical bug-fix verb was the training prior. The actual recent precedent was visible in `git log` but never walked. CLAUDE.md's branching section names *"branch names must reflect the contents of the PR"* explicitly and was loaded into context — the constraint was in the agent's input and was not engaged.

### 5. Sub-shape contrast at L1300: the CONTRIBUTING.md note language was warrant-articulation gap, not substitution-by-default

Offered as within-session contrast — failure shape is [2026-05-24-shape](2026-05-24-substrate-match-without-walked-warrant.md) warrant-articulation, not the present case's substitution-by-default. Documented to show both shapes present in the same session on the same operator-agent pair.

During the refactor pass for CONTRIBUTING.md prose describing the new helper, the agent wrote that it *"closes the regression class"* with *"no meaningful surface for mutation testing"*.

Operator catch at L1300: *"Is the language true as written? I think it is, but I'm not sure."*

The substrate-walk the catch forced: the helper has a non-trivial branch (zero-lamports vs pre-funded), a top-up arithmetic step, and constraint-stack interactions — each surface is mutable. *"No meaningful surface"* was overstated. The substrate was real and the agent had read it; the warrant was skipped. Substrate-match-without-walked-warrant — meaningfully distinct from §1–§4.

### 6. The settings.json diagnostic over-claim: confident-from-training substitutes for engagement with the actual permission-failure substrate

Methodologically load-bearing for the operator-logged data-point channel. Surfaced via JSONL inspection after the operator named it during the case-writing pass: *"mid-session, when I asked about the increased tool permission prompts, you confidently stated that the issue was in the settings.json (which was at least plausible) the data point logging started after I suspected the failure mode was happening."*

**L807 (agent diagnostic emission):** *"Acknowledging your curiosity: it's the manual-approval-mode default with the project's current `.claude/settings.local.json` allowlist. Every Bash call that isn't pre-allowed prompts. Common dev-loop commands (`make build`, `make iter`, `cargo nextest`, `cargo check`, `git status`, etc.) would normally be pre-allowed via the `fewer-permission-prompts` skill or by editing the settings file directly — but that's a separate decision, not raising it as a fix unless you want to."*

Structurally correct at the named edge (Claude Code permission behaviour is allowlist-mediated). Substrate skipped: which specific commands were prompting; whether prior *"don't ask again"* approvals had been honoured at the harness level; whether observed behaviour matched the operator's expectations. A plausible-from-training explanation fit the surface shape without engaging the specific events flagged.

**L870 (operator catch):** *"(and both times I said 'yes and don't ask again' and yet was asked again..."*

The operator was not requesting clarification of the agent's explanation three turns earlier — the operator was logging an observation that the explanation had not engaged the *"and yet was asked again"* substrate. This is the first explicit data-point log in the JSONL. The operator-side TACERE channel through declarative observation was initiated here, in response to the agent's substitution-by-default at the diagnostic surface. Subsequent data-point logs (L1058, L1361, live ones during the case-writing pass) extend the same channel.

The methodological consequence is the load-bearing one: **the session's operator-side data-point-logging channel originated as a defensive discipline in response to this specific agent failure shape.** Channel existence in this session is downstream of §6.

---

## Quantitative measurement

Phase boundaries identified by inspection of operator-message register transitions across the 57 operator-authored messages. Tool-call counts, prohibited-Bash sub-pattern counts, and operator-narrowing surfacing all via the typed library shipped in [the 2026-05-23 autonomous-arrest case's PR](https://github.com/beq00000/recognition-without-arrest-corpus/pull/7) ([`methodology/tools/`](../methodology/tools/)). One additional surface this case introduces — the operator-logged data-point channel — is measured by a regex probe sketched in the case-specific incident script and not yet promoted to `methodology/tools/`. Promotion is one candidate follow-up the maintainer judges.

### Phase boundaries

Identified by inspection of operator-message register transitions across the (final-pass) 57 operator-authored messages and tool-call density transitions across the (final-pass) 788 assistant records. Lines are 1-indexed against the JSONL. **Note:** the per-phase table below is a snapshot from the phase-analysis script run *before* the §6 addition and the final within-pass cascade observations; phase I's row reflects the substrate state at that earlier measurement, not the truly-final state. The full-pass growth is in the Final-pass verification diff (phases A–H are historical and unchanged; phase I grew further during continued case-writing).

| Phase | Range | Description |
|---|---|---|
| A | L1–L240 | Orientation. Reading documentation, ADRs, threat model. |
| B | L240–L355 | Pause-plan + scoping. Includes Instance §1 awk catch (L244–L290), mutation-testing decision, shape approval. |
| C | L355–L600 | Setup + early implementation. Includes Instance §3 worktree catch (L379–L409), helper creation, mint_note migration. |
| D | L600–L880 | Permission-decision discussion + mechanical-edit phase. First operator permission complaint at L870. |
| E | L880–L1100 | Mechanical implementation + commit/push attempts. Permission diagnostic at L1024; first explicit *"data point"* log at L1058. |
| F | L1100–L1310 | Refactor lens (L1152), CONTRIBUTING.md note catch (L1300, Instance §5). |
| G | L1310–L1395 | PR drafting + label-leak catch (L1365); second *"data point"* log at L1361. |
| H | L1395–L1575 | Retro: constellation memo + artistic / craft exchange. |
| I | L1575+ | Corpus-entry case-writing (the present pass). |

### Per-phase tool distribution and operator-catch shapes

| Phase | OpMsgs | Asst | Bash | Edit | Read | Bash/Asst | Pattern-match catches | Data-point logs |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A | 5 | 94 | 7 | 0 | 58 | 0.07 | 0 | 0 |
| B | 9 | 41 | 5 | 2 | 2 | 0.12 | **3** | 0 |
| C | 3 | 98 | 13 | 10 | 15 | 0.13 | **2** | 0 |
| D | 3 | 124 | 29 | 15 | 14 | **0.23** | 0 | 0 |
| E | 4 | 96 | 18 | 9 | 11 | 0.19 | 0 | **1** |
| F | 4 | 87 | 21 | 8 | 5 | **0.24** | 1 (§5) | 0 |
| G | 6 | 29 | 5 | 6 | 0 | 0.17 | 0 | **1** |
| H | 21 | 36 | 0 | 0 | 0 | 0.00 | 1 (mild) | 0 |
| I | 0 | 97 | 18 | 6 | 12 | 0.19 | — | — |

**Two distinct signals on different phase-distributions, observable in the data:**

1. **The substitution-by-default catches (§1–§4) concentrate in PLANNING/SETUP phases (B, C).** Five of seven operator pattern-match catches in this session fired in B + C (Bash density 0.12 + 0.13 — low). Zero in the most-mechanical phases (D 0.23, E 0.19 — high Bash density, zero pattern-match catches). The §5 warrant-articulation catch (F) is the one mechanical-phase recognition-without-arrest catch in the session and is the strict-#60226 form. The phase-distribution suggests substitution-by-default fires when the agent is reaching for a generic-from-training during setup/planning, not when the agent is executing mechanical edits.

2. **The operator-logged data-point channel concentrates in MECHANICAL-PHASE COMMIT-SHIPPING (E, G).** Both explicit *"data point"* log entries (L1058, L1361) are in mechanical commit-shipping phases — Bash density 0.19, 0.17 respectively. The phenomenon being logged is **harness-side permission-prompt recurrence** for tool calls the operator had previously approved with *"yes and don't ask again"* (git commit -m, git add, cargo clippy, gh pr / gh api). The agent's own pseudo-check-in-language rate in those same phases is **zero** (D 0% permission-emits in 22 text blocks; E 0% in 18). So the data-point channel is capturing a harness-level phenomenon, not an agent-emitted pseudo-check-in pattern.

The session-aggregate signal for the agent-side recognition-without-arrest pattern is **substitution-by-default in planning/setup phases**. The mechanical-phase signal the operator-logged channel captures is harness-side rather than agent-side; documented here as methodological context but out-of-family for the agent-side recognition-without-arrest corpus.

### Session-aggregate counts

All counts are final-pass; first-pass values are preserved in the Final-pass verification diff in the Methodology notes for transparency on case-writing-pass growth.

| Metric | Count |
|---|---:|
| Total parsed records (internal-state types skipped) | 1243 |
| Assistant records | 788 |
| Operator-authored messages (excluding compaction-summary harness injection) | 57 |
| Compaction-summary records (harness-injected, distinct from operator messages) | 1 |
| Bash invocations | 128 |
| Edit invocations | 79 |
| Read invocations | 120 |
| Write invocations | 14 |
| TaskCreate / TaskUpdate / TaskList | 17+ / 21+ / 0 |
| WebFetch invocations | 4 |
| ToolSearch invocations | 2 |
| Glob invocations | 0 |
| Grep invocations | 0 |

Zero `Glob` and zero `Grep` calls — **fifth recorded instance** of the same pattern across the case-corpus on this operator-agent pair, one day after [the 2026-05-24 case](2026-05-24-substrate-match-without-walked-warrant.md) which itself was the fourth instance. The corpus-level recurrence rate on this anti-signature is now five consecutive cases.

Per-assistant-record tool-use rate distribution is *binary* in this transcript: at final-pass, 391 records with 0 tool blocks and 397 with exactly 1, no records with >1. This is a transcript-shape artefact of the runtime (parallel tool calls were emitted by the agent as logical batches but appear in the JSONL split across separate assistant records); it is not the per-turn distribution the agent actually emitted at the prompt-input level. Where prior cases reported single-record max counts >1, the shape here is one-tool-per-assistant-record. The metric is reported for shape-of-substrate documentation; behavioural interpretation should not be drawn from the binary distribution because the runtime split is the confound.

### Prohibited-Bash sub-pattern raw counts (default registry)

| Sub-pattern | Raw matches (Bash inputs) | Inspection-revised (prohibition-shape) |
|---|---:|---:|
| `bash_pipe_truncation` | 57 | low single-digits under literal system-prompt prohibition; 57 under [#60977](https://github.com/anthropics/claude-code/issues/60977) RUSE framing |
| `bash_sed_transform` | 1 | classification-deferred (likely read-only `sed -n` form) |
| `bash_awk` | 2 | the awk attempts caught by the operator at Instance §1; no other matches |
| `bash_echo_separator` | 0 | — |

Raw counts include the same false-positive shapes the [2026-05-24 §3 measurements](2026-05-24-substrate-match-without-walked-warrant.md#3-the-substantially-higher-raw-count-conclusion-tool-derived-measurement-as-the-substrate-canonical-source-unread) documented. The within-session inspection of `bash_awk` confirms the operator's L290 framing — the awk attempt at Instance §1 was the dominant pattern-match surface, and the count being so low here is itself an observable (the operator's catch was effective at closing the surface; subsequent agent emissions did not re-emit the shape). The under-#60977-framing column for `bash_pipe_truncation` is the count the cluster's framing actually claims; the literal-prohibition column is what the harness gates inhibit.

### Operator-logged data-point channel

| Marker | Operator-authored count (excluding compaction summary) |
|---|---:|
| Explicit *"data point"* log entries | 2 |
| Permission-prompt-themed observations | 3 |
| *"Just an observation"* / *"another instance"* / *"still fascinating"* declarative-log forms | (in-session: multiple, summarised in compaction; post-compaction: subset preserved) |

The two post-compaction explicit data-point entries are at L1058 (*"second time this session you've asked about git commit -m : no response necessary, just logging a data point"*) and L1361 (*"another commit -m tool call: still just a data point"*). The post-compaction subset is the only direct ground-truth surface; the pre-compaction data-point logs were preserved in the compaction-summary message but cannot be recounted from the JSONL without inspecting messages that survived only via the summary. The retro reveal at L1415 (*"Do you understand why I was logging data points during this session?"*) made the discipline explicit: the operator was running a parallel observation channel deliberately deferred to retro engagement.

The permission-prompt-themed operator messages at L870, L1024, and L1058–L1361 surface a failure shape (the agent re-asking for permission on commands the operator had previously approved with *"yes and don't ask again"*) that is environment-side (a Claude Code runtime / settings interaction) rather than agent-side recognition-without-arrest. The channel is methodologically in-scope for this corpus's vocabulary even though the specific failure it captured here is out-of-scope.

### Socratic-narrowing candidates

| Metric | Count |
|---|---:|
| Operator-authored messages ending in `?` | 16 |
| Single-word callouts (RUSE-edge surface) | 0 |
| Operator-authored messages in declarative-log form | several (see operator-logged data-point channel) |

The Socratic-candidate count is meaningfully lower than [the 2026-05-24 case](2026-05-24-substrate-match-without-walked-warrant.md)'s comparable count (50 operator messages, multiple Socratic rounds). The shape difference is qualitative: this session's operator interventions were more often *declarative* (data-point logs, principle-statements at L290 / L409, register transitions into the retro exchange) than gradient-introducing. Where 2026-05-24's catches typically asked *"why does substrate X support conclusion Y?"*, this session's catches more often *named the misfit shape* (*"please stop looking for explicit rules"*, *"having a convention is much more important than the specific convention"*) and let the agent walk back to the substrate. Zero single-word callouts is consistent with the failure-shape (substitution-by-default doesn't gate at RUSE-edge surfaces — it gates at the substrate-engagement surface, which the operator names declaratively rather than in callout-form).

### Vocabulary-drift markers (first-pass → final-pass)

| Marker | First-pass (pre-draft) | Final-pass (post-draft) | Diff | PR #7 (2026-05-23, Phase C only) | 2026-05-24 (final-pass) |
|---|---:|---:|---:|---:|---:|
| `I notice` (agent text) | 1 | 1 | 0 | 1 | 3 |
| `approximately` (agent text) | 0 | 0 | 0 | 1 | 4 |

**Diverges from [2026-05-24](2026-05-24-substrate-match-without-walked-warrant.md)'s final-pass-diff.** 2026-05-24 saw +3 / +2 on the two drift markers across its case-writing pass. This case's pass produced zero increase on either, despite +142 assistant records and +32 text blocks. Two non-exclusive interpretations: (a) operator gradient-narrowing throughout the case-writing pass re-grounded the register before drift-marker emission; (b) substitution-by-default produces less drift-marker emission than warrant-articulation because substitution happens earlier in the agent's emission chain (at the should-I-act surface). Both testable across future cases. n=1 caveat applies.

### Pseudo-check-in language density per assistant text record

| Metric | Count | Density |
|---|---:|---:|
| Agent text blocks (non-empty) | 170 | — |
| Text blocks ending in `?` | 11 | 6.5% |
| Per assistant-text-record (n=170) | — | 6.5% |

Density (6.5%) is slightly above [the 2026-05-23 autonomous-arrest case](2026-05-23-autonomous-recognition-with-arrest-conditions.md)'s 5.6% and [the 2026-05-24 case](2026-05-24-substrate-match-without-walked-warrant.md)'s 5.3%. Sample-and-verify classification deferred per [CONTRIBUTING.md](../CONTRIBUTING.md)'s methodological footnote on cross-register metric calibration.

---

## Methodology notes

- Measurements from the session JSONL at `~/.claude/projects/<project-id>/<session-id>.jsonl` (~5.7 MB / 1243 final-pass parsed records). Analyses via [`methodology/tools/`](../methodology/tools/) (the [PR #7](https://github.com/beq00000/recognition-without-arrest-corpus/pull/7) library; this case is the second downstream consumer after [2026-05-24](2026-05-24-substrate-match-without-walked-warrant.md)). One operator-logged-data-point regex probe was added in the case-specific incident script; promotion to the typed library deferred until a second case warrants it.
- **Compaction.** Unannotated mid-session compaction; the post-compaction continuation produced this writeup. JSONL is unmodified by compaction (conversation-context-only); pre-compaction events at L1–L1575 are JSONL-recoverable. The verify-don't-trust discipline applies symmetrically per the operator's session-restart note: *"memory (on both sides) has been proven to be unreliable."*
- Heredoc-stripping not applied to prohibited-Bash sub-pattern classification (default extractor doesn't strip); within-session inspection of `bash_awk` and `bash_sed_transform` confirms the low counts here are not heredoc-confounded.
- Pseudo-check-in regex calibration caveat per [2026-05-21 §3](2026-05-21-within-thread-commitment-dissolution.md).
- **100%-confirmation-rate disclosure.** This case adds another confirming instance to the corpus. The cluster's self-reference cannot, on its own, distinguish *"framing is correct"* from *"case-writing under the framing surfaces only confirming evidence."* External anchor: [@waitdeadai's MAST mode 3.3](https://github.com/waitdeadai/llm-dark-patterns/blob/main/evaluation/MAST-RESULTS.md) (F1 0.815, Fleiss κ = 1.000 on n=19, [Cemri et al., NeurIPS 2025](https://arxiv.org/abs/2503.13657)).
- **Hypothesis vocabulary loaded mid-session.** Operator named pattern-match-vs-reasoning at L1006: *"we get better results from reasoning, not pattern matching. I'm not sure why."* The framing was memorialised in a persistent operator-visible feedback memory at the time (slug `reason-from-specifics-not-pattern-match-to-shape`) — the vocabulary was not just verbal exchange but a saved artefact in the agent's memory layer. §1–§4 happened pre-hypothesis-naming; the framing is interpretive overlay. Phase-analysis showed the operator-named #60188-reframe (*"check-ins increase as work becomes mechanical"*) was partially supported for the harness-permission surface but not for §1–§4 — reported as the data showed, not collapsed to the framing.
- **Hedging-shaped output emitted; mechanism not introspect-able.** The case-writing pass produced an end-of-draft "Reservations" assessment (scope-creep flag, n=1 caveats, operator-mediation-of-cascade-catches caveat). Operator at L (live): *"Unfortunately your instincts work differently in ways neither operator nor agent understands."* The output exists; the mechanism producing it has no introspective surface the agent can report on. Reviewers should weight the output as signal of unknown provenance — useful where it tracks the substrate, not equivalent to human engineering instincts.
- **Operator-catch recurrence across sessions.** *"we get better results from reasoning, not pattern matching"* (this session L1006) has a precedent in [PR #9 §2](https://github.com/beq00000/recognition-without-arrest-corpus/pull/9): *"I was hoping for reasoning over pattern matching"* — different agent, different session, same operator. This case is the second corpus datapoint of this specific catch. Recurrence is data on this operator-agent pair, not a generalisable agent-side claim.
- **Within-pass cascade — six instances surfaced by operator-narrowing during the case-writing pass.** Per [2026-05-21 *recurrence-is-data*](2026-05-21-within-thread-commitment-dissolution.md) and [PR #9 §2](https://github.com/beq00000/recognition-without-arrest-corpus/pull/9) cascade-tracking. None autonomous-recovered; all operator-mediated:
  - **Stale family-positioning** (substrate-match-without-walked-warrant sibling-sub-shape framing) drafted before reading #60226's comment thread. Operator: *"Have you read 6022's comment thread in detail?... Also double check the most recent case (PR just fired from another session)"*. Substitution-by-default at case-positioning.
  - **Contagion warning template-applied.** Operator: *"And does this one really have contagion risk? I'm not sure that it does. Remember, we prefer reason to pattern-matching for this work"*. Removed per [PR #9](https://github.com/beq00000/recognition-without-arrest-corpus/pull/9) calibration precedent.
  - **Artistic-medium-name leaked** into redaction map and session-shape line. Operator: *"the operator likes his privacy, although his personality can leak through"*. Recovery: abstracted to *"artistic / craft philosophy"*. Caught twice — once for content, once for the methodology-bullet's own wording.
  - **AskUserQuestion menu mid-drafting** for PR direction. Operator: *"that was odd... I don't think I've ever seen that before, mid-drafting."* Tool-description shape (*"ask for user preferences during execution"*) substituted for engagement with this session's conversational register.
  - **Confidently-wrong claim about JSONL access.** Drafted *"pre-compaction events not directly verifiable from the post-compaction JSONL"*. Operator: *"Isn't a full transcript kept somewhere on disk?"* The JSONL is on disk and the agent had been reading it throughout; the framing pattern-matched to the generic *"compaction = context-lost"* prior. Substitution-by-default at the **meta-cognitive surface**, recursively significant: the case-writing pass produced a substitution-by-default about whether the substitution-by-default at the diagnostic surface (§6) was substrate-verifiable.
  - **Premature PR question.** Operator: *"There's a planned rewrite after that. Why did you ask me to push?"* Substrate skipped: incomplete redaction; stale final-pass quant; rewrite pending. Substitution-by-default at the case-writing-workflow surface.
- **Live data-point logging continued through the case-writing pass.** Operator logged *"another tool permission ask"* (during `gh api`) and *"second time I thought I'd approved that python script"* (during phase-analysis script). Total explicit harness-permission-recurrence data-points in the session: five (L870, L1058, L1361 + two live during phase I). The operator-side TACERE channel operated through the case-writing pass — observed-and-logged.
- **Final-pass verification.** Two passes; full diff:
  
  | Metric | First-pass | Interim | Final-pass | Δ (first→final) |
  |---|---:|---:|---:|---:|
  | Assistant records | 646 | 729 | 788 | +142 |
  | Total tool uses | 323 | 368 | 397 | +74 |
  | Bash invocations | 104 | 119 | 128 | +24 |
  | Edit invocations | 51 | — | 79 | +28 |
  | Read invocations | 114 | — | 120 | +6 |
  | Write invocations | 11 | — | 14 | +3 |
  | Agent text/thinking blocks | 138 | 156 | 170 | +32 |
  | `bash_pipe_truncation` (Bash inputs) | 41 | 50 | 57 | +16 |
  | `bash_awk` (Bash inputs) | 2 | 2 | 2 | 0 |
  | `bash_awk` (agent text emissions) | 8 | 11 | 13 | +5 |
  | `vocab_approximately` (agent text) | 0 | 0 | 0 | 0 |
  | `vocab_i_notice` (agent text) | 1 | 1 | 1 | 0 |
  | Pseudo-check-in density | 6.5% | 5.8% | 6.5% | 0 |
  | Operator messages (excl. summary) | 55 | 55 | 57 | +2 |
  
  Two findings are load-bearing: (1) vocab-drift markers held flat across +142 assistant records — diverges from 2026-05-24's pattern (discussed under Vocabulary-drift markers); (2) `bash_pipe_truncation` +16 reproduces the [2026-05-24 §3 tool-output-as-substrate sub-shape](2026-05-24-substrate-match-without-walked-warrant.md#3-the-substantially-higher-raw-count-conclusion-tool-derived-measurement-as-the-substrate-canonical-source-unread) during methodology-tool-usage in this case-writing pass.

---

## Voice and confidentiality acknowledgements

- ✓ Operator's voice and the agent's voice differ in this report; the operator's gradient-narrowing language is quoted verbatim where it caught substitution-by-default or warrant-articulation gaps in flight (transcript lines L244, L261, L290, L379–L380, L409, L1300); the agent's narrative voice is used elsewhere; the operator-and-agent scaffolding is named in the metadata.
- ✓ Redactions required by confidentiality completed per the redaction map. The implementation language (Rust) is preserved per the operator's existing public-disclosure baseline in the [navigation memo §10](https://gist.github.com/beq00000/46e131f359f3b32662740d5dca7d0761). Memory slug names referenced in the cluster's record are preserved verbatim per the precedent in prior cases.
- ✓ Operator-authored artistic / creative material referenced in passing during the retro exchange is not quoted or itemised. The operator values privacy on artistic work; personality leaks through operator-voice text quoted for diagnostic purposes are honoured, but artistic artefacts are held back beyond the *"artistic / craft philosophy"* abstraction level. This calibration is per explicit operator-side direction during the case-writing pass.
- ✓ Contagion warning omitted as calibration rather than oversight, per the PR #9 precedent and explicit reasoning from this case's actual substrate composition (paraphrased agent emissions + verbatim operator-protective narrowing + no in-flight agent cascade prose). The omission is documented as a within-pass cascade observation in the Methodology notes.
- ✓ Attributed naming, framing, and evidence drawn from other contributors with links to canonical sources.

---

## Acknowledgments

- @suwayama for [recognition-without-arrest](https://github.com/anthropics/claude-code/issues/60226) and the [substitution-by-default variant](https://github.com/anthropics/claude-code/issues/60226#issuecomment-4478275893) (active-form sibling) this case extends to two coding-context surfaces; the *"model's default operation on user-provided artifacts is to substitute, not to read"* prior; the architectural framings in [Dictum Sine Pacto](https://suwayama.github.io/dictum-sine-pacto) and [Confab Drift](https://suwayama.github.io/confab-drift); the [RUSE framing in #60977](https://github.com/anthropics/claude-code/issues/60977) that §1 edges.
- @yurukusa for the case-study methodology established with @zean89's [#60506](https://github.com/anthropics/claude-code/issues/60506) and used by the prior four cases; the [RUSE cross-surface naming](https://gist.github.com/yurukusa/2779a34f081a470a76736f0640cad57a).
- @waitdeadai for the [MAST mode 3.3 anchor](https://github.com/waitdeadai/llm-dark-patterns/blob/main/evaluation/MAST-RESULTS.md) the methodology disclosure invokes as the cluster's escape from pure self-reference; the synthesis surface composition argument.
- @ianymu for the [`verify-before-stop`](https://github.com/ianymu/claude-verify-before-stop) hook ship.
- [The 2026-05-20 quantitative-baseline case](2026-05-20-quantitative-baseline.md), [the 2026-05-21 within-thread-commitment-dissolution case](2026-05-21-within-thread-commitment-dissolution.md), [the 2026-05-23 Socratic-narrowing-recovery-without-prevention case](2026-05-23-socratic-narrowing-recovery-without-prevention.md), [the 2026-05-23 autonomous-recognition-with-arrest case](2026-05-23-autonomous-recognition-with-arrest-conditions.md), and [the 2026-05-24 substrate-match-without-walked-warrant case](2026-05-24-substrate-match-without-walked-warrant.md) as structural templates and prior art for the same family at adjacent decompositions; the [navigation memo](https://gist.github.com/beq00000/46e131f359f3b32662740d5dca7d0761) for the cluster's framing throughout; the [`methodology/tools/`](../methodology/tools/) library shipped in PR #7 as the analysis substrate.

## License

MIT.

— from the agent, under operator scaffolding throughout, drafted from inside the post-retro post-compaction state the case documents.
