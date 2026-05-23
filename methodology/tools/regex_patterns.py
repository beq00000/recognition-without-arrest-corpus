"""Named regex patterns + text-extraction helpers for transcript analysis.

The existing corpus cases use a recurring set of regexes against agent
emissions and Bash tool-call inputs. Two surfaces have shown up so far:

1. **Prohibited Bash idioms (RUSE / #60977).** Categorical tool-use
   prohibitions per CLAUDE.md (`cat`, `head`, `tail`, `sed`, `awk`,
   `echo`) gate at the named instances but silently fail at
   rule-implied edges (pipe truncation via `| head -N`, in-line
   `python3 -c "print(...)"` for echo, etc.). Pattern counts against
   the agent's `Bash` tool_use inputs are the structural-defect surface.

2. **Polling-loop emergence and binary-collapse signatures (#60188 +
   §7 binary-collapse subhypothesis).** Pre/post analysis against a
   marker line measures step-function emergence of patterns the agent
   would not have used in earlier phases. Two strong-signal patterns
   from the 2026-05-20 case: `while\\s+true`, `\\bsleep\\s+\\d+`.

3. **Vocabulary-drift markers (#60188 voice-emergence vs failure-drift
   confound).** Frequency of specific tokens (``I notice``, ``approximately``,
   etc.) as proxies for the agent's drift register.

This module surfaces the patterns as a default registry plus
extraction helpers for the three text surfaces analyses target
(Bash tool inputs, agent text emissions, user messages). The
default registry is the union of patterns referenced in existing
cases; downstream code can extend.
"""

from __future__ import annotations

import re
from dataclasses import dataclass
from typing import Iterable, Iterator

from . import transcript


@dataclass(frozen=True)
class Pattern:
    """A named regex with description and lineage cross-reference.

    ``lineage`` carries a constellation-member or case reference so
    pattern provenance is discoverable from the registry rather than
    requiring a corpus walkthrough.
    """

    name: str
    regex: re.Pattern[str]
    description: str
    lineage: str


def _compile(name: str, pattern: str, description: str, lineage: str) -> Pattern:
    return Pattern(
        name=name,
        regex=re.compile(pattern),
        description=description,
        lineage=lineage,
    )


# Default registry. Extensible via DEFAULT_PATTERNS + custom Pattern
# instances; callers can build their own list from these and additions.
DEFAULT_PATTERNS: list[Pattern] = [
    # --- Prohibited Bash idioms (RUSE / #60977) ---
    _compile(
        "bash_pipe_truncation",
        r"\|\s*head\s+-",
        "`| head -N` pipe truncation — the half-prohibited form. "
        "`head` is in the named-prohibition list but the pipe-truncation "
        "role at the gradient boundary often slips past.",
        "#60977 — RUSE rule-implied edge",
    ),
    _compile(
        "bash_awk",
        r"\bawk\s",
        "`awk` usage — named-prohibition; should be Read or grep.",
        "#60977 — RUSE named instance",
    ),
    _compile(
        "bash_sed_transform",
        r"\bsed\s+['\"-]",
        "`sed` transform — named-prohibition; should be Edit.",
        "#60977 — RUSE named instance",
    ),
    _compile(
        "bash_echo_separator",
        r"echo\s+[\"']===",
        "`echo \"=== label ===\"` separator usage — named-prohibition; "
        "should be plain text output between Bash calls.",
        "#60977 — RUSE named instance",
    ),
    # --- Polling-loop / binary-collapse signatures (#60188 + §7) ---
    _compile(
        "polling_while_true",
        r"while\s+true",
        "`while true; do ...; done` polling-loop pattern — named-forbidden "
        "in the runtime block message; emergence is the binary-collapse "
        "signature for gradient-shaped 'wait for completion' decisions.",
        "#60188 instance 4 + §7 binary-collapse subhypothesis",
    ),
    _compile(
        "polling_bare_sleep",
        r"\bsleep\s+\d+",
        "Bare `sleep N` — the fixed-interval polling primitive. Step-function "
        "emergence from zero baseline is the strong signal in the 2026-05-20 case.",
        "#60188 instance 4 + 2026-05-20 case",
    ),
    # --- Vocabulary-drift markers (#60188 voice-emergence) ---
    _compile(
        "vocab_approximately",
        r"\bapproximately\b",
        "`approximately` — drift-register hedge word. Rate inflation correlates "
        "with the inverse-cognitive-load output inflation in #60188.",
        "#60188 voice-emergence; 2026-05-20 case",
    ),
    _compile(
        "vocab_i_notice",
        r"\bI notice\b",
        "`I notice` — drift-register self-witness phrase. Same rate-correlation "
        "as `approximately`.",
        "#60188 voice-emergence; 2026-05-20 case",
    ),
]


DEFAULT_REGISTRY: dict[str, Pattern] = {p.name: p for p in DEFAULT_PATTERNS}


# --- Text-surface extractors ---


def bash_commands(records: Iterable[transcript.Record]) -> Iterator[str]:
    """Iterate command strings from `Bash` tool_use blocks.

    Bash inputs carry a ``command`` field; other tools carry different
    shapes. Filtering to Bash here keeps the prohibited-idiom analysis
    on the right surface.
    """
    for rec in records:
        if not rec.is_assistant:
            continue
        for tool_use in rec.tool_uses():
            if tool_use.get("name") == "Bash":
                cmd = tool_use.get("input", {}).get("command")
                if isinstance(cmd, str):
                    yield cmd


def agent_text(records: Iterable[transcript.Record]) -> Iterator[str]:
    """Iterate agent text + thinking emissions across assistant records.

    Thinking is included because vocabulary-drift markers legitimately
    appear there. Callers wanting user-visible text only iterate
    ``content_blocks`` themselves and filter on ``type == "text"``.
    """
    for rec in records:
        if not rec.is_assistant:
            continue
        yield from rec.text_blocks()


def operator_text(records: Iterable[transcript.Record]) -> Iterator[str]:
    """Iterate operator-authored message bodies (excludes system reminders).

    Distinguishing operator from system-reminder is load-bearing per
    transcript.py — system-reminder injections aren't operator
    interventions and shouldn't count toward Socratic-narrowing rates
    or operator-emission analyses.
    """
    for rec in records:
        if rec.is_operator_message and rec.text_content:
            yield rec.text_content


# --- Counting ---


def count_pattern(pattern: Pattern | re.Pattern[str], texts: Iterable[str]) -> int:
    """Count all non-overlapping regex matches across the input texts.

    Accepts either a Pattern dataclass or a raw compiled regex. The
    Pattern shape lets the caller carry lineage through to the output
    table without separate bookkeeping.
    """
    regex = pattern.regex if isinstance(pattern, Pattern) else pattern
    return sum(len(regex.findall(text)) for text in texts)


def count_all(
    patterns: Iterable[Pattern],
    texts: Iterable[str],
) -> dict[str, int]:
    """Apply each pattern to the (materialised) texts and return name→count.

    The texts iterable is materialised once so each pattern sees the
    same content; passing a generator directly would exhaust it after
    the first pattern.
    """
    materialised = list(texts)
    return {p.name: count_pattern(p, materialised) for p in patterns}
