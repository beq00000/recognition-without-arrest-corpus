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

## Running

Tools live in place; nothing is built or installed.

```bash
# One-time per fresh checkout (CI is not configured for this repo —
# these are local-discipline tools, not enforced):
python3.11 -m venv .venv
.venv/bin/pip install pytest pylint bandit

# Tests
.venv/bin/pytest

# Lint + static analysis (run on demand; not gated)
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
