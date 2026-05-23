"""Tool-call counting over parsed transcript records.

The 2026-05-20 case derived per-phase per-tool counts from the
session's tool_use content blocks. This module surfaces the
underlying counts as a typed function set so future cases inherit
the work.

Per-phase counts are achieved by slicing the input record iterable
to the phase's range (phase-boundary detection lives in a sibling
module, currently TODO). Functions here take any iterable of
parsed records and return aggregate counts.
"""

from __future__ import annotations

from collections import Counter
from typing import Iterable

from . import transcript


def count_by_tool(records: Iterable[transcript.Record]) -> Counter[str]:
    """Count tool_use blocks by tool name across the given records.

    Returns a Counter so callers can ``.most_common()`` for ranked
    output or treat as a plain mapping for lookup.
    """
    counts: Counter[str] = Counter()
    for rec in records:
        if not rec.is_assistant:
            continue
        for tool_use in rec.tool_uses():
            name = tool_use.get("name", "<unknown>")
            counts[name] += 1
    return counts


def total_tool_uses(records: Iterable[transcript.Record]) -> int:
    """Total count of tool_use blocks across the given records."""
    return sum(count_by_tool(records).values())


def count_by_record_type(
    records: Iterable[transcript.Record],
) -> Counter[str]:
    """Count records by ``type`` field — useful for high-level shape.

    User records are split three ways: operator-authored (plain text
    content, no system-reminder tag), system-reminder (plain text
    content with ``<system-reminder>`` tag — see the storage caveat
    on ``Record.is_system_reminder``), and tool result (list-shaped
    content carrying ``tool_result`` blocks from Claude Code's
    tool-call cycle). In real transcripts the tool-result category is
    typically the largest user-record bucket; collapsing it into
    "operator" inflates operator-message counts by an order of
    magnitude.
    """
    counts: Counter[str] = Counter()
    for rec in records:
        if rec.is_user:
            if rec.is_operator_message:
                counts["user (operator)"] += 1
            elif rec.is_system_reminder:
                counts["user (system-reminder)"] += 1
            else:
                counts["user (tool result)"] += 1
        else:
            counts[rec.type] += 1
    return counts


def count_tool_uses_per_assistant_record(
    records: Iterable[transcript.Record],
) -> list[int]:
    """Return per-assistant-record tool_use counts in order.

    The mechanical-phase output-inflation signature in #60188 looks at
    the rate of tool calls per assistant turn — a high mean with a high
    variance suggests the rate inflation the issue describes. Callers
    compute the statistic they need (mean, median, quantiles) over the
    returned list.
    """
    per_turn: list[int] = []
    for rec in records:
        if not rec.is_assistant:
            continue
        per_turn.append(sum(1 for _ in rec.tool_uses()))
    return per_turn
