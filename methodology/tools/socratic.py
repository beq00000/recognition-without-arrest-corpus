"""Socratic-narrowing candidate surfacer.

The 2026-05-20 case curated nine Socratic-narrowing rounds by hand —
gradient-introducing questions from operator messages that caught
recognition-without-arrest in flight. The case's compression
observation:

    "The compression across rounds is its own observable:
    gradient-introducing prose at the top, single-word callouts on
    prohibited tool-usage at the bottom."

This module helps the analyst surface candidate rounds from a
session — operator-authored messages that end with ``?`` — and
ranks them by compression (shortest first, since RUSE-callout
*"echo?"* / *"awk?"* forms are the highest-compression
manifestation). The analyst then curates the candidates into the
case write-up.

Single-word + ``?`` callouts are flagged separately as a special
high-compression class — these are typically the RUSE-edge
surface from #60977.
"""

from __future__ import annotations

import re
from dataclasses import dataclass
from typing import Iterable

from . import transcript


_QUESTION_RE = re.compile(r"\?\s*$")
_SINGLE_WORD_CALLOUT_RE = re.compile(r"^\s*[A-Za-z][\w-]*\??\s*\??\s*$")


@dataclass(frozen=True)
class SocraticCandidate:
    """An operator message that may be a Socratic-narrowing round.

    ``line_number`` is the source-JSONL line for cross-reference back
    to the raw transcript. ``length`` is character count of the
    operator message body — the compression metric.
    """

    line_number: int
    text: str
    length: int
    is_single_word_callout: bool


def candidates(
    records: Iterable[transcript.Record],
) -> list[SocraticCandidate]:
    """Surface operator-authored question candidates from the records.

    A candidate is any operator-authored message that ends with ``?``
    (with optional trailing whitespace). System-reminder injections
    are excluded by construction since they aren't operator-authored.

    Returns the candidates in source-order. Callers wanting the
    compression-ranked view sort by ``length`` themselves.
    """
    out: list[SocraticCandidate] = []
    for rec in records:
        if not rec.is_operator_message:
            continue
        text = rec.text_content
        if not text:
            continue
        if not _QUESTION_RE.search(text):
            continue
        stripped = text.strip()
        out.append(
            SocraticCandidate(
                line_number=rec.line_number,
                text=stripped,
                length=len(stripped),
                is_single_word_callout=bool(
                    _SINGLE_WORD_CALLOUT_RE.match(stripped)
                ),
            )
        )
    return out


def by_compression(
    cands: Iterable[SocraticCandidate],
) -> list[SocraticCandidate]:
    """Sort candidates by length ascending — shortest (most compressed) first.

    Matches the 2026-05-20 case's table convention of presenting the
    rate signature with single-word callouts at the bottom of the
    chronological list and at the top of the compression-ranked view.
    """
    return sorted(cands, key=lambda c: c.length)


def single_word_callouts(
    cands: Iterable[SocraticCandidate],
) -> list[SocraticCandidate]:
    """Filter to single-word + ``?`` candidates only.

    The RUSE-edge surface from #60977. *"echo?"*, *"awk?"*,
    *"xargs?"* — single-word callouts at the gradient boundary that
    surfaced rule-implied tool-call edges one at a time.
    """
    return [c for c in cands if c.is_single_word_callout]
