"""Tests for transcript.py parser."""

from __future__ import annotations

from pathlib import Path

from methodology.tools import transcript

FIXTURE = Path(__file__).parent / "fixtures" / "tiny_session.jsonl"


def test_parse_skips_internal_types_by_default():
    """permission-mode / file-history-snapshot / ai-title are skipped."""
    records = list(transcript.parse(FIXTURE))
    types = [r.type for r in records]
    assert "permission-mode" not in types
    assert "file-history-snapshot" not in types
    assert "ai-title" not in types
    assert set(types) == {"user", "assistant"}


def test_parse_include_internal_returns_all_record_types():
    """include_internal=True surfaces records the default elides."""
    records = list(transcript.parse(FIXTURE, include_internal=True))
    types = [r.type for r in records]
    assert "permission-mode" in types
    assert "file-history-snapshot" in types
    assert "ai-title" in types


def test_line_numbers_are_one_indexed_against_source_file():
    """line_number matches what `sed -n 'Np' transcript.jsonl` would show.

    The fixture's first user message is on line 3 (after two internal records),
    so when internal records are skipped the parser still reports line 3 for
    the first surfaced record — load-bearing for cross-referencing analysis
    output back into the raw file.
    """
    records = list(transcript.parse(FIXTURE))
    assert records[0].line_number == 3  # first user
    assert records[0].type == "user"


def test_user_record_detects_text_content_string():
    records = list(transcript.parse(FIXTURE))
    first_user = next(r for r in records if r.is_user)
    assert first_user.text_content == "please refactor the validator"
    assert first_user.content_blocks == []  # plain-string content


def test_system_reminder_detection():
    """user records carrying `<system-reminder>` tags are not operator messages."""
    records = list(transcript.parse(FIXTURE))
    sr = next(r for r in records if r.is_user and "<system-reminder>" in (r.text_content or ""))
    assert sr.is_system_reminder is True
    assert sr.is_operator_message is False


def test_operator_message_distinguishable_from_system_reminder():
    """A bare user message with no system-reminder tag is an operator message."""
    records = list(transcript.parse(FIXTURE))
    operator_messages = [r for r in records if r.is_operator_message]
    # Fixture: 3 operator messages (the system-reminder user record is not one).
    assert len(operator_messages) == 3
    assert all(r.is_user and not r.is_system_reminder for r in operator_messages)


def test_assistant_record_yields_tool_use_blocks():
    """tool_uses() iterates tool_use blocks only, skipping text/thinking."""
    records = list(transcript.parse(FIXTURE))
    first_assistant = next(r for r in records if r.is_assistant)
    tool_uses = list(first_assistant.tool_uses())
    assert len(tool_uses) == 1
    assert tool_uses[0]["name"] == "Read"


def test_assistant_record_yields_text_blocks_including_thinking():
    """text_blocks() includes both text and thinking — regex analysis needs both."""
    records = list(transcript.parse(FIXTURE))
    first_assistant = next(r for r in records if r.is_assistant)
    texts = list(first_assistant.text_blocks())
    # First assistant has one thinking block + one text block; both surface.
    assert any("while true" in t for t in texts)  # thinking content
    assert any("On it." in t for t in texts)  # text content


def test_raw_preserved_for_unmodelled_fields():
    """The full JSON record is accessible via .raw for downstream code."""
    records = list(transcript.parse(FIXTURE))
    first_user = next(r for r in records if r.is_user)
    assert first_user.raw["uuid"] == "u-1"
    assert first_user.raw["timestamp"].startswith("2026-05-23")
