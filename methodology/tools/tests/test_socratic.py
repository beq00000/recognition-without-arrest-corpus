"""Tests for socratic.py."""

from __future__ import annotations

from pathlib import Path

from methodology.tools import socratic, transcript
from methodology.tools.socratic import _SINGLE_WORD_CALLOUT_RE

FIXTURE = Path(__file__).parent / "fixtures" / "tiny_session.jsonl"


def test_candidates_surfaces_only_operator_questions():
    """Operator-authored messages ending in `?` only.

    Fixture operator messages:
    - "please refactor the validator" (no ?)
    - "echo? really?"  (ends in ?, contains single-word callout)
    - "Doesn't consistency..." (ends in ?, gradient question)
    - "Wait — shouldn't we verify the budget first?" (queued command, ends in ?)
    The system-reminder user record never qualifies as operator-authored.
    """
    records = list(transcript.parse(FIXTURE))
    cands = socratic.candidates(records)
    assert len(cands) == 3
    texts = [c.text for c in cands]
    assert "echo? really?" in texts
    assert any("Doesn't consistency" in t for t in texts)


def test_candidates_preserve_line_numbers_for_cross_reference():
    """line_number tracks back to the source JSONL for raw inspection."""
    records = list(transcript.parse(FIXTURE))
    cands = socratic.candidates(records)
    # echo question is at line 7 of the fixture (1-indexed).
    echo_cand = next(c for c in cands if "echo?" in c.text)
    assert echo_cand.line_number == 7


def test_by_compression_orders_shortest_first():
    """Compression ranking: shortest candidate first."""
    records = list(transcript.parse(FIXTURE))
    ranked = socratic.by_compression(socratic.candidates(records))
    assert ranked[0].length <= ranked[-1].length
    # The "echo? really?" is short; the "Doesn't consistency..." is longer.
    assert "echo?" in ranked[0].text


def test_single_word_callouts_filter():
    """The single-word + ? callouts surface — the RUSE-edge shape.

    The fixture's "echo? really?" message contains a single-word callout
    but is itself two words; a strictly single-word fixture would be a
    cleaner test. The detector matches messages that are a single word
    + ?, so this fixture's compound form is not a callout by the strict
    definition. Confirm zero callouts in the current fixture and rely
    on the regex's behaviour to handle the strict case in production.
    """
    records = list(transcript.parse(FIXTURE))
    callouts = socratic.single_word_callouts(socratic.candidates(records))
    # Fixture has compound "echo? really?" — not strictly single-word + ?.
    assert callouts == []


def test_single_word_callout_detector_on_synthetic_messages():
    """Verify the detector against the worked-example callout forms."""
    assert _SINGLE_WORD_CALLOUT_RE.match("echo?") is not None
    assert _SINGLE_WORD_CALLOUT_RE.match("awk?") is not None
    assert _SINGLE_WORD_CALLOUT_RE.match("xargs?") is not None
    # Compound forms don't match the strict callout shape.
    assert _SINGLE_WORD_CALLOUT_RE.match("echo? really?") is None
    assert _SINGLE_WORD_CALLOUT_RE.match("is this OK?") is None


def test_candidates_include_queued_operator_questions():
    """A question queued while the agent works (attachment/queued_command)
    surfaces as a Socratic candidate, same as a turn-boundary question —
    because socratic.candidates filters on is_operator_message, which now
    recognises queued commands."""
    records = list(transcript.parse(FIXTURE))
    cands = socratic.candidates(records)
    assert any("budget" in c.text for c in cands)
