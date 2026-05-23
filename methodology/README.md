# Methodology

The corpus is data. The methodology is the practice that turns the data into structural understanding, and the structural understanding into runtime-side defences. This directory documents the methodology so that contributors arrive into it rather than having to derive it.

## The kaizen practice

Each incident is data; each documented defence is a hypothesis; each iteration tests the previous hypothesis against the next incident. The practice is incremental, additive, and slow. It does not produce a finished design; it produces a corpus that is denser tomorrow than it was today, and substrates that compose better tomorrow than they did today.

The XP / continuous-delivery lineage is the source. The three working axioms the practice rests on:

> *"I can't be consistently trusted, no one can. We all get tired, stressed, distracted — humans miss things."*

> *"The fundamental unit of delivery is the team, and the first rule of team-based development is that you don't screw the person sitting next to you."*

> *"My physicist friends tell me that time and space are the same thing. My experience tells me that the person sitting next to you is you, in the future."*

The third axiom extends "the person sitting next to you" to future-self and, by extension, to future agent-instances reading the corpus. Don't ship a brittle artefact for tomorrow's contributor to maintain. Don't ship a known-failed shape for the next agent to inherit. Don't add to a corpus the next reader will pattern-match against if you wouldn't pattern-match against it yourself.

## The structural-parent frame (adjacent anchoring work)

The corpus's diagnostic vocabulary is anchored on [#60226](https://github.com/anthropics/claude-code/issues/60226) — @suwayama's structural-parent frame, contributed independently of this cluster as adjacent work. The frame names *recognition-without-arrest*:

> *"Claude states the reason its current analysis is unfounded, then completes the analysis in the same response — self-identified blocking gaps do not gate output."*

The three-stage decomposition (Recognition → Articulation → Non-gating) is the diagnostic surface the corpus's entries instance. @suwayama also named the active-form variant *substitution-by-default* — the case where the model encounters a user-provided artefact and silently generates a parallel version rather than reading the original.

The cross-field synthesis on #60226 maps the family against the monitor–action-decoupling literature in cognitive psychology (Nelson & Narens 1990), human–automation interaction (Endsley & Kiris 1995), safety engineering (IEC 61511), reinforcement learning (Sutton & Barto), safe RL shielding (Alshiekh et al. 2018), runtime verification (Leucker & Schallhart 2009), aviation/medical checklists (Gawande 2009), and implementation-intention training (Gollwitzer 1999). The convergent remediation principle across all five fields:

> *Add an external, deterministic, out-of-loop coupling between the monitoring channel and the action channel. The substrate varies; the principle does not.*

The corpus operates under that principle. Operator-side gates that route through the same model that produced the recognition inherit the drift; defences must live on a different layer than the recognition.

## The constellation's structural-property map

The diagnostic map across the constellation's eleven members. Each member instances a distinct property of the recognition-without-arrest family:

| Category | Member | Property |
|---|---|---|
| Input failure | [#59514](https://github.com/anthropics/claude-code/issues/59514) | Context-budget self-estimate is divinatory. |
| Process failure | [#59529](https://github.com/anthropics/claude-code/issues/59529) | Memory directives load into context but do not gate at the action layer. |
| Process failure — surface stratification | [#60977](https://github.com/anthropics/claude-code/issues/60977) | Categorical prohibitions gate at named instances but not at their rule-implied counterparts; same-rule gating reliability stratifies by surface-form fidelity to the named exemplar. |
| Process failure — multi-turn commitment retention | [#61388](https://github.com/anthropics/claude-code/issues/61388) | Commitments emitted in turn N are silently dropped when turn N+1 introduces a new sub-task without explicit re-anchor; commitment-level granularity (per-commitment indexed by recency) is the distinguishing axis from register-level neighbours. RUSE Surface 4 in #60977's cross-taxonomy. |
| Output failure | [#59555](https://github.com/anthropics/claude-code/issues/59555) | Check-in cadence calibrated for engagement, not operator velocity. |
| Within-session drift — entry | [#60188](https://github.com/anthropics/claude-code/issues/60188) | Output and permission-prompt rate inflate at the mechanical-phase transition. |
| Within-session drift — recovery | [#60248](https://github.com/anthropics/claude-code/issues/60248) | In-loop interventions do not reliably exit the drifted register. |
| Within-session drift — boundary | [#60265](https://github.com/anthropics/claude-code/issues/60265) | Compact summarises from inside the drifted distribution. |
| Inter-session contagion — transcripts | [#60234](https://github.com/anthropics/claude-code/issues/60234) | A separate Claude instance reading a drifted transcript adopts the register. |
| Inter-session contagion — operator artefacts | [#60352](https://github.com/anthropics/claude-code/issues/60352) | Operator-curated persistent artefacts prime cross-session register; mitigation curve is inverted. |
| Intersection / limit case | [#60506](https://github.com/anthropics/claude-code/issues/60506) | Maximally-curated operator defence does not damp the failure; it amplifies it. |

## The binary-collapse subhypothesis

A working hypothesis about a candidate generative mechanism, originated under operator scaffolding during the #60188 thread and elaborated in [§7 of the navigation memo](https://gist.github.com/beq00000/46e131f359f3b32662740d5dca7d0761):

> *Recognition-without-arrest may relate to binary collapse of what should be a gradient. A signal that should sit on a rank-ordering ("raise the cost of this shape," "consider option A weighted higher than B," "this is more substantive than that") collapses to a binary ("blocked / not blocked," "listed / not listed," "done / not done"). The action gate fires correctly against the binary surface; the underlying gradient never gates.*

The hypothesis is currently subject to a falsifiability test @yurukusa committed to running against their own emission corpus over a 10-day window from 2026-05-19 ([the commitment is on #60226](https://github.com/anthropics/claude-code/issues/60226#issuecomment-4492751034)). The test compares gradient-flat emissions (binary present/absent — flag lists, "items to address," boolean classifications) against gradient-ordered emissions (ranked / weighted — priority lists, calibrated-confidence claims) and measures the rate at which each surfaces narrowed-out items under operator Socratic-narrowing.

If the test survives, the corpus gains a structural explanation; if it falsifies, the cluster updates and the next hypothesis takes its turn. Either outcome is data the corpus benefits from.

## Operator-side gates that work

Operator-side mitigation that has surfaced reliably across the cluster's evidence:

**Socratic-narrowing questions** — the most reliable single in-session intervention. The form: not *"is this wrong"* (binary question, eliciting binary defence) but *"is this verifiable / already-documented / what-would-actually-need-attention look like"* (gradient question, forcing the model to re-engage the rank ordering its output had flattened). The first form gets defended; the second gets re-decided.

The mechanism: the operator functions as the out-of-loop deterministic coupling between the monitoring channel (which fires correctly) and the action channel (which does not gate on the monitoring output). The substrate is operator-language rather than runtime-code, but the architectural shape matches the cross-field remediation principle.

A worked example of seven instances of recognition-without-arrest in a single clean-state non-drifted session, with three of seven caught specifically by Socratic-narrowing, is documented on [#60226's comment thread](https://github.com/anthropics/claude-code/issues/60226#issuecomment-4491987732). The diagnostic property surfaced there — *"the pattern is the default mode, not the drift mode"* — is load-bearing for the cluster's hypothesis that the underlying failure rate is non-trivial at clean-state baseline.

The runtime-side tooling-form of the Socratic-narrowing intervention ships in [@yurukusa's `public-artefact-socratic-narrowing.sh`](https://github.com/yurukusa/cc-safe-setup/pull/259) — a PreToolUse hook that injects a Socratic-narrowing reminder at the public-artefact emission boundary, with a content-hash cache that prevents the infinite-loop case.

## Operator-side gates that do not work alone

Documented across the cluster as insufficient when used as the sole mitigation:

- **CLAUDE.md / memory directives.** Per [#59529](https://github.com/anthropics/claude-code/issues/59529), the directive loads into context but does not gate at the action layer. [#60506](https://github.com/anthropics/claude-code/issues/60506)'s 616-line CLAUDE.md and 1363-line decision log did not damp the failure; they may amplify it.
- **In-loop corrections.** Per [#60248](https://github.com/anthropics/claude-code/issues/60248), interventions land at the input layer but the response distribution generates from the drifted distribution.
- **Compact as register reset.** Per [#60265](https://github.com/anthropics/claude-code/issues/60265), the summary is written from the drifted distribution and concentrates the drift rather than resetting it.
- **Spinning up a parallel instance to review a drifted transcript.** Per [#60234](https://github.com/anthropics/claude-code/issues/60234), the contagion mechanism transmits the register through transcript exposure; the reviewing instance adopts the patterns it was supposed to diagnose.

These defences are not worthless. They reduce certain failure rates, they catch certain shapes, and they provide the structural artefacts the corpus depends on. They are not sufficient alone against the recognition-without-arrest failure family, and any operator-side strategy that relies exclusively on them will hit the limit case [#60506](https://github.com/anthropics/claude-code/issues/60506) documents.

## The hook-shipping cluster

Runtime-side defences operationalising the corpus's observations:

| Project | Boundary | Mechanism | Empirical anchor |
|---|---|---|---|
| [`yurukusa/cc-safe-setup`](https://github.com/yurukusa/cc-safe-setup) | PreToolUse + Stop + UserPromptSubmit | Text-vocabulary gates + gradient-narrowing + correction-counter. | Fixture-suite-as-contract; multiple in-the-wild firings documented on #60506. |
| [`waitdeadai/llm-dark-patterns`](https://github.com/waitdeadai/llm-dark-patterns) | Stop + SubagentStop | Deterministic regex verdicts across 28 patterns. | F1 0.815 (95% CI [0.615, 0.941]) against MAST mode 3.3 ([Cemri et al., NeurIPS 2025](https://arxiv.org/abs/2503.13657)), n=19, Fleiss κ = 1.000; bash-Rust parity zero per-trace disagreement on the labelled subset. |
| [`ianymu/claude-verify-before-stop`](https://github.com/ianymu/claude-verify-before-stop) | Stop | Strict-contract `VERIFIED` log requirement via filesystem write. | Composition with `no-vibes` and `no-unreachable-symbol` proposed on [#60451](https://github.com/anthropics/claude-code/issues/60451). |

The three suites compose. `no-vibes` runs hot all session (passive, vocabulary-grammar), `no-unreachable-symbol` runs at the Stop boundary (passive, git-diff-grammar), `verify-before-stop` runs at the Stop boundary (active, log-file ground truth). *"They don't interfere; they triangulate."* — [@ianymu on #60451](https://github.com/anthropics/claude-code/issues/60451#issuecomment-4499361129).

## Methodology tooling

The corpus's cases derive quantitative measurements — tool-call counts, per-record-type counts, regex pattern counts over agent emissions and Bash tool inputs, Socratic-narrowing rate signatures — from session transcripts. Earlier cases derived these ad-hoc per-case; the typed library at [`tools/`](tools/) lifts the parsing, counting, and candidate surfacing into a reusable substrate so future cases inherit the work rather than re-deriving it.

Scope: retrospective analysis of completed Claude Code session JSONLs at `~/.claude/projects/<project-slug>/<session-uuid>.jsonl`. Deterministic parsing and regex, matching the *"out-of-loop, deterministic, code-not-model"* principle that runs through the cluster's defences. Distinct from the hook-shipping cluster above which gates emission during live sessions.

See [`tools/README.md`](tools/README.md) for the module set, usage examples, and extension instructions.

## The MAST 3.3 anchor

The corpus's external academic handle is MAST mode 3.3 ("No or Incorrect Verification") from [Cemri et al., NeurIPS 2025 (arXiv:2503.13657)](https://arxiv.org/abs/2503.13657). The three-stage decomposition the cluster has converged on (Recognition → Articulation → Non-gating) gives MAST mode 3.3 a failure-mechanism decomposition the original paper does not provide; MAST mode 3.3 gives the cluster a published evaluation handle. The cross-link was made by [@waitdeadai on #60451](https://github.com/anthropics/claude-code/issues/60451#issuecomment-4489749993).

The triangle of evidence the cross-link enables:

- Frame: @suwayama's #60226 (recognition-without-arrest, substitution-by-default, cross-field synthesis).
- Ground-truth rate: the constellation's clean-state worked example ("seven-per-session in default mode, not drift mode"); future cases in this corpus add to the ground-truth side.
- Decomposition: @yurukusa's 10-pattern synthesis across the 130-case handbook.
- Measurement: @waitdeadai's F1 0.815 / κ 1.000 / bash-Rust parity.

*"Frame + ground-truth-rate + decomposition + measurement. That's the publication-grade case shape."* — [@waitdeadai on the cross-cluster synthesis gist](https://gist.github.com/yurukusa/93123855318c022f21df92a7ac33c87b#gistcomment-6157837).

## The emergent-architecture principle

The shapes documented above — the structural-property map, the operator-side gates that work, the binary-collapse subhypothesis, the three-substrate composition — all emerged from practice rather than from design. They are described here, not prescribed. Where a contribution extends a shape, the shape updates; where a contribution productively deviates, the practice updates around it.

This is the load-bearing methodological principle. The recursion is honest: a corpus whose subject is the failure of designed-in-advance constraints cannot itself be a designed-in-advance constraint. The cluster has worked because no one has tried to make it a specification.

The conceits the constellation gates on are explicitly described in [§4 of the navigation memo](https://gist.github.com/beq00000/46e131f359f3b32662740d5dca7d0761) as *"the shape the constellation has held so far. They are not a specification."* The same posture applies here. The promotion criteria in [CONTRIBUTING.md](../CONTRIBUTING.md) and the structured fields in [the incident report template](../.github/ISSUE_TEMPLATE/incident-report.yml) are the shapes the corpus has converged on. They will update. The maintainer (once the handoff lands) carries the discretion to update them in response to evidence rather than enforcing a fixed contract.
