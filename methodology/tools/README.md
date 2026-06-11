# Methodology tools

Transcript-analysis helpers for corpus case write-ups. Replaces the
ad-hoc Python the existing cases derived per-case with a typed
library other contributors and future agents inherit.

## Scope

Retrospective analysis of completed Claude Code session JSONLs at
`~/.claude/projects/<project-slug>/<session-uuid>.jsonl`. Distinct
from the runtime-hook cluster (`cc-safe-setup`, `llm-dark-patterns`,
`claude-verify-before-stop`) which gates emission during a live
session.

Designed against the methodology described in [the corpus seed
cases](../../cases/) and the navigation memo's quantitative-analysis
references. Tool surfaces are deterministic — pure JSON parsing and
regex — matching the corpus's *"out-of-loop, deterministic,
code-not-model"* principle.

## Modules

| Module | What it does |
|---|---|
| `transcript.py` | Parser. Yields typed `Record` dataclasses from a JSONL. Distinguishes operator messages from system-reminder injections, exposes tool_use and text blocks. |
| `tool_calls.py` | Tool-use counts. Per-tool, per-record-type, per-assistant-record. |
| `regex_patterns.py` | Named pattern registry + text-surface extractors (Bash inputs, agent emissions, operator messages). Default registry covers RUSE prohibited Bash idioms (#60977), polling-loop / binary-collapse signatures (#60188 + §7), and vocabulary-drift markers. |
| `socratic.py` | Socratic-narrowing candidate surfacer. Operator-authored questions, compression-ranked, with single-word-callout flag for the RUSE-edge surface. |
| `count_claims.py` | Count-claim consistency gate over corpus markdown artefacts (cases, incidents) rather than transcripts. Diffs prose count-claims against their enumeration or table sources; runs in CI on every PR. See [Count-claim gate](#count-claim-gate) below. |

## Running

Tools live in place; nothing is built or installed.

```bash
# One-time per fresh checkout:
python3.11 -m venv .venv
.venv/bin/pip install pytest pylint bandit

# Tests (also run in CI on every PR — see .github/workflows/count-claims.yml)
.venv/bin/pytest

# Lint + static analysis (local discipline; not CI-gated)
.venv/bin/pylint methodology/tools/
.venv/bin/bandit -r methodology/tools/ -c pyproject.toml
```

`pyproject.toml` at the repo root configures all three: pytest with
`pythonpath = ["."]` so `from methodology.tools import X` resolves;
pylint with an init-hook that adds the repo root to sys.path so the
test files' imports resolve under lint too; bandit excluding the
tests directory (`assert` is the test mechanism — bandit B101 is a
true positive in production code but a false positive across tests/).

## Usage

```python
from methodology.tools import transcript, tool_calls, regex_patterns, socratic

records = list(transcript.parse("~/.claude/projects/.../session-uuid.jsonl"))

# Per-tool counts
print(tool_calls.count_by_tool(records).most_common())

# Per-assistant-turn tool-use rate (for #60188 inflation signature)
per_turn = tool_calls.count_tool_uses_per_assistant_record(records)

# Polling-loop emergence
agent_texts = list(regex_patterns.agent_text(records))
while_true = regex_patterns.count_pattern(
    regex_patterns.DEFAULT_REGISTRY["polling_while_true"],
    agent_texts,
)

# Socratic-narrowing candidates, compression-ranked
candidates = socratic.by_compression(socratic.candidates(records))
for c in candidates:
    print(f"line {c.line_number}: {c.text!r}")
```

## Count-claim gate

`count_claims.py` is the one module that targets the corpus's own
markdown artefacts rather than session transcripts. Every corpus PR
review to date caught at least one internal count drift by hand —
"fourteen" vs 15 enumerated bullets (#9), "six instances" vs five
(#10), a prose total contradicting its own table column (#12) — and
the [PR #9 thread](https://github.com/beq00000/recognition-without-arrest-corpus/pull/9)
named the remediation: a final-pass diff between every count-claim and
its enumeration source, structural rather than recall-dependent,
because the failure mode *is* the writing agent not re-checking. It is
the retrospective sibling of @waitdeadai's
[`no-count-drift`](https://github.com/waitdeadai/llm-dark-patterns/pull/27)
Stop hook (same shape, live-session boundary).

```bash
# Check a draft before raising the PR:
.venv/bin/python -m methodology.tools.count_claims cases/2026-06-01-my-case.md

# Audit trail — every checked claim and every abstention with reason:
.venv/bin/python -m methodology.tools.count_claims --verbose cases/*.md incidents/*.md
```

Design notes:

- **Abstains rather than guesses.** A claim that cannot be bound to a
  countable source (a cross-case reference, a section without an
  enumeration, a ratio row in a Total column) is reported as an
  abstention under `--verbose`, never as a finding. The summary line
  always states checked/abstained counts so the scope is never
  silently narrower than it reads.
- **CI gating goes through the test suite, not the raw CLI.**
  `test_count_claims.py::test_live_corpus_is_clean` runs the checker
  over every file in `cases/` and `incidents/` against an explicit
  `KNOWN_FINDINGS` baseline — findings in already-merged cases that
  await reconciliation against a session substrate only the operator
  holds. New drift fails CI; pinned drift is visible, named, and
  removed by the reconciliation commit.
- **Documented out of scope** (semantic, not deterministic): the
  #8/#11 shape where one label binds two values across sections
  (raw-vs-post-skip relabelling is the convention that resolves it),
  and the #10 pre-fix shape where the enumeration itself misclassifies
  a member. Those still need a reviewer.
- **Validation set leads with real positives.** The suite checks the
  actual pre-fix PR #9 revision via `git show` (skipped on shallow
  clones), not only fixtures authored alongside the rules — the
  co-evolved-corpus-trap lesson from the PR #9 thread. On its first
  full-corpus run the checker also surfaced one previously uncaught
  drift in a merged case (the 2026-05-23 autonomous case's per-phase
  tool table, row C: columns sum to 75, Total states 76), which is the
  current `KNOWN_FINDINGS` baseline entry.

## Verification discipline

When the tools' output disagrees with a prior case's count, the
divergence is a signal that one or the other is wrong (or that
pattern definitions differ at an edge case). Per the corpus's
verify-don't-trust discipline, both sources are derived data —
the session transcript JSONL is ground truth. The right move on
divergence is to compare implementations line-by-line and fix the
side that's wrong, which may sometimes be the tools and sometimes
be the prior case's count.

## Test fixture

`tests/fixtures/tiny_session.jsonl` is a synthetic minimal
transcript exercising the documented behaviours. Real-transcript
content is **not** used as test fixtures — per [#60234](https://github.com/anthropics/claude-code/issues/60234)
the contagion concern applies to test data in source as much as
to retrospective reading.

## Extending

Patterns extend by Pattern-instance addition:

```python
from methodology.tools.regex_patterns import Pattern, DEFAULT_PATTERNS
import re

my_pattern = Pattern(
    name="my_signature",
    regex=re.compile(r"..."),
    description="...",
    lineage="...",
)
counts = regex_patterns.count_all(
    DEFAULT_PATTERNS + [my_pattern],
    regex_patterns.agent_text(records),
)
```

A new module belongs here when a case derives a measurement that
warrants typed library access for future cases. Phase-boundary
detection is the obvious next addition — currently deferred until a
clear contract for phase markers emerges across cases.
