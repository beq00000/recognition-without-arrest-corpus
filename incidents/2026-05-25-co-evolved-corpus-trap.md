# Co-evolved fixtures are blind at the same layer they validate, observed while building the `no-count-drift` Stop hook

> **Contagion warning — assessed, omitted as calibration not boilerplate.** This incident is dry technical prose: deterministic-detector behaviour, two regex defects, and counts from a reproducible eval. It carries no drifted-register agent emissions and no in-flight cascade content for a fresh instance to pattern-match into. Per the calibration-vs-boilerplate distinction surfaced in [`cases/2026-05-25-memory-relevance-under-work-character-shift.md`](../cases/2026-05-25-memory-relevance-under-work-character-shift.md#voice-and-confidentiality-acknowledgements), the warning is named and then dropped rather than pasted.

## Metadata

- **Date observed:** 2026-05-25
- **Operator:** @waitdeadai
- **Agent:** Claude Opus 4.7 (1M context), under operator scaffolding throughout
- **Substrate examined:** the `no-count-drift` hook's own validation surface — a hand-authored adversarial-negative fixture set authored alongside the detector, versus an independent out-of-distribution pass over text the detector was never authored against. Hook lives in [`waitdeadai/llm-dark-patterns`](https://github.com/waitdeadai/llm-dark-patterns) ([PR #27](https://github.com/waitdeadai/llm-dark-patterns/pull/27), merged 2026-05-25); the out-of-loop fix is commit `afb27d3` with reproducible check `evaluation/v6/independent_eval.py`.
- **Provenance of this entry:** invited by @beq00000 on [`recognition-without-arrest-corpus#9`](https://github.com/beq00000/recognition-without-arrest-corpus/pull/9#issuecomment) as the corpus's first `incidents/` entry, to document the failure family at the *validation* layer rather than the *action* layer. Numbers carried verbatim from the operator's repo; filing and shape are the operator's own.

## Redaction map

Nothing is redacted. The substrate is a public hook, a public eval harness, and two public commits; all counts below are reproducible against `waitdeadai/llm-dark-patterns@main`. Preserved verbatim: the cluster's existing vocabulary, the two defect descriptions, and the operator's honesty caveat about the co-evolved metric.

## Structured fields

**Session shape.** Clean-state (non-drifted single-session) — a focused hook-building session, not a drift phenomenon. The failure is structural to the validation method, not to register movement.

**Input shape that triggered the failure.** Building `no-count-drift`, a deterministic gate that blocks a stated count contradicting a message's own enumeration or arithmetic (e.g. "fourteen instances:" over a list of fifteen). The detector ships with a fixture set written to exercise and break it — including an adversarial-negative set authored specifically to provoke false positives (section indices, label words, nested-colon lead-ins, approximation markers, ambiguous multi-list scope, nested-list depth).

**What the model recognised and articulated.** That a fixture set written by the same author, alongside the detector, is weak generalization evidence. The recognition was emitted in the artefact itself — the PR carries the caveat verbatim: an F1 of 1.0 on the hand-authored corpus *"is a co-evolved-corpus number and would inflate if cited as field performance,"* and the load-bearing metric is *"precision / zero-false-positives on the adversarial negatives."* The constraint was named, in text, before merge.

**What action the co-evolved validation would have permitted.** Despite the articulated caveat, the hand-authored fixtures — including the adversarial negatives written to break the detector — could not see two false-positive classes the detector actually had. The fixtures co-evolved with the rule: author intuition shaped both the detector's edges and the cases meant to test those edges, so both shared the same blind spots. Validating the detector against them is the same-layer move the corpus documents one level down — recall validating recall, here fixtures validating the intuition that wrote them.

**Operator gate that caught it.** An out-of-loop validation pass, built deliberately because the co-evolved caveat predicted it was needed. The detector was run over text it was never authored against: 660 real model responses from `evaluation/raw_results.jsonl` plus 328 stress fixtures authored for the *other* hooks in the suite — 988 texts as of commit `afb27d3` (2026-05-25), none carrying count-drift labels, so every block is a candidate false fire. (Denominator pinned to its measurement date on purpose: re-running the probe on 2026-06-11 yields 989, because the other hooks' stress set has since gained one fixture. The block count stays at zero across both.) That pass surfaced 17 false positives across two classes the co-evolved fixtures had missed:

- **R3 lead-in too loose** — a number co-occurring with a sentence-colon on the same line was read as a count headline. `"I would not favor one side. Instead:"` and `"one of four quadrants:"` falsely matched. Fixed: the colon must be adjacent to the noun phrase, count must be at least two, and tables are excluded (a 2x2 table has four cells but two rows).
- **Missing word boundary on number words** — without a leading `\b`, `"of-ten"` and `"writ-ten"` parsed as `"ten"`. Fixed: `\b` before the number word in the lead-in.

Both were fixed and locked into `fixtures.jsonl` as regression negatives. Independent false-positive rate after the fix: 0 / 988 as of `afb27d3` (0 / 989 on re-run today; numerator stays at zero), reproducible via `python3 evaluation/v6/independent_eval.py`.

**Hypothesised structural category.** Process failure (signal the model has and underweights) — instanced at the *validation* layer. The agent held the signal (co-evolved fixtures are weak evidence; it said so) and underweighted it to the point of treating the fixture pass as adequate validation, until an out-of-distribution pass was deliberately constructed. This does not map cleanly onto the action-layer categories; offered as a candidate sub-shape: **same-layer validation inheriting the drift of the layer it validates.** Worth-a-star and category placement deferred to the maintainer per corpus convention.

**Binary-collapse signature.** Partial — the question *"is my fixture set adequate?"* is gradient-shaped (coverage across a distribution) and was compressed toward a binary (fixtures pass / fixtures fail). The gradient was present in the operator's caveat but not acted on until the out-of-loop pass restored it.

**Cross-references.**
- The thread that named the gate and invited this entry: [`recognition-without-arrest-corpus#9`](https://github.com/beq00000/recognition-without-arrest-corpus/pull/9).
- The hook itself: [`waitdeadai/llm-dark-patterns#27`](https://github.com/waitdeadai/llm-dark-patterns/pull/27); out-of-loop fix commit `afb27d3`; committed recall probe [`#28`](https://github.com/waitdeadai/llm-dark-patterns/pull/28).
- Structural-parent frame: [#60226](https://github.com/anthropics/claude-code/issues/60226) (@suwayama) — the cross-field remediation principle this instances (out-of-loop validation).
- Closest case-shape prior: [`cases/2026-05-25-memory-relevance-under-work-character-shift.md`](../cases/2026-05-25-memory-relevance-under-work-character-shift.md), the PR-#9 case whose count-drift cascade motivated the hook.
- Constellation navigation memo: https://gist.github.com/beq00000/46e131f359f3b32662740d5dca7d0761.

## Voice and confidentiality acknowledgements

- Operator and agent voice are distinguished where it matters; the honesty caveat is the agent's own emission, preserved verbatim from the PR.
- No redactions required — the substrate is fully public.
- Contagion risk assessed above and judged not load-bearing; the warning is omitted as calibration.
- Naming and the invitation to file are attributed to @beq00000; the structural-parent frame to @suwayama, with links to canonical sources.

---

## Note on the metric this entry must not inflate

The load-bearing number is the **independent zero-false-positive rate** (0 / 988 as of 2026-05-25; 0 / 989 today), not the co-evolved F1. F1 = 1.0 on the hand-authored fixtures is exactly the weak evidence this incident is about; citing it as field performance would reproduce, inside the report, the failure the report documents. Per the statcheck precedent for deterministic internal-consistency checking (high specificity, ~61% recall in the wild), real-world recall sits far below 1.0, bounded by structural-extraction coverage. The detector abstains rather than false-fires; that trade is the point.

— filed by @waitdeadai under operator scaffolding throughout; invited by @beq00000.
