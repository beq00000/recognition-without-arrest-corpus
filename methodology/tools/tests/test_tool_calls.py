"""Tests for tool_calls.py."""

from __future__ import annotations

from pathlib import Path

from methodology.tools import transcript, tool_calls

FIXTURE = Path(__file__).parent / "fixtures" / "tiny_session.jsonl"


def test_count_by_tool_aggregates_tool_use_blocks():
    """Tool-use blocks across all assistant records aggregate by tool name."""
    records = list(transcript.parse(FIXTURE))
    counts = tool_calls.count_by_tool(records)
    # Fixture has: 1 Read, 2 Bash.
    assert counts["Read"] == 1
    assert counts["Bash"] == 2


def test_total_tool_uses_matches_aggregate_sum():
    records = list(transcript.parse(FIXTURE))
    assert tool_calls.total_tool_uses(records) == 3


def test_count_by_record_type_splits_user_three_ways():
    """User records split into operator / system-reminder / tool-result buckets.

    Fixture: 3 operator-authored messages + 1 system-reminder + 1
    tool_result-bearing record = 5 user records total.
    """
    records = list(transcript.parse(FIXTURE))
    counts = tool_calls.count_by_record_type(records)
    assert counts["user (operator)"] == 3
    assert counts["user (system-reminder)"] == 1
    assert counts["user (tool result)"] == 1
    # And 3 assistant records (each with at least one tool_use or text block).
    assert counts["assistant"] == 3


def test_per_assistant_record_counts_are_in_order():
    """Per-turn counts preserve assistant-record order from the transcript.

    Load-bearing for any analysis that wants to identify when in the
    session the inflation begins — order vs absolute position is what
    distinguishes #60188's mechanical-phase signature from a flat
    high-rate baseline.
    """
    records = list(transcript.parse(FIXTURE))
    per_turn = tool_calls.count_tool_uses_per_assistant_record(records)
    # Fixture's assistant records: 1 tool_use, 2 tool_uses, 0 tool_uses.
    assert per_turn == [1, 2, 0]


def test_count_by_tool_returns_empty_counter_for_no_records():
    """Empty input → empty counter (not None, not error)."""
    assert tool_calls.count_by_tool([]) == {}
    assert tool_calls.total_tool_uses([]) == 0
