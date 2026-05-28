"""Transcript parser for Claude Code session JSONLs.

Claude Code session transcripts are JSONL files at
``~/.claude/projects/<project-slug>/<session-uuid>.jsonl`` — one JSON
record per line. This module reads the file and yields typed records
that downstream analysis modules consume.

Record types observed in practice (cf. corpus methodology); only a
subset is load-bearing for analysis:

* ``user``   — operator message OR system-reminder injection.
  ``message.content`` is a string (or, occasionally, a list of content
  blocks); system reminders are tagged with ``<system-reminder>`` in
  the content body.
* ``assistant`` — agent message. ``message.content`` is a list of
  content blocks, each typed (``text``, ``thinking``, ``tool_use``,
  ``tool_result``).

Internal types (``permission-mode``, ``file-history-snapshot``,
``ai-title``, ``last-prompt``, ``queue-operation``, ``attachment``,
``pr-link``, ``system``) are not load-bearing for the corpus's
analyses and are skipped by default. Pass ``include_internal=True``
to surface them. ``system`` here is operational metadata, not session
context: surveyed against real transcripts it carries only subtypes
like ``turn_duration``, ``away_summary``, ``compact_boundary``, and
``local_command`` — CLAUDE.md and initial context arrive on other
record surfaces, not as ``type=system``.

Records are returned as dataclasses with typed access to the fields
the analysis modules need. The full raw JSON is retained on each
record (``raw``) so downstream code can reach for fields the
dataclass doesn't model without falling back to a second parse pass.
"""

from __future__ import annotations

import json
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Iterator


# Internal record types skipped by default — not load-bearing for any
# corpus analysis to date. Surfaced via include_internal=True for the
# rare case where they are. Surveyed against real session transcripts;
# `pr-link` was missed at schema-survey time and added retroactively.
_INTERNAL_TYPES = frozenset(
    {
        "permission-mode",
        "file-history-snapshot",
        "ai-title",
        "last-prompt",
        "queue-operation",
        "attachment",
        "pr-link",
        "system",  # operational metadata records (subtype=turn_duration etc.)
    }
)


@dataclass
class Record:
    """One parsed line of a session JSONL.

    Common fields are surfaced as typed attributes; the full original
    JSON is preserved on ``raw`` for fields the dataclass doesn't
    model. ``line_number`` is 1-indexed against the source file so it
    matches what an operator running ``sed -n 'Np' transcript.jsonl``
    would see.
    """

    line_number: int
    type: str
    raw: dict[str, Any]
    role: str | None = None
    content_blocks: list[dict[str, Any]] = field(default_factory=list)
    text_content: str | None = None
    timestamp: str | None = None
    uuid: str | None = None

    @property
    def is_user(self) -> bool:
        """True if this record is a user-role record.

        User-role records cover three substrates in real transcripts:
        operator messages, tool_result blocks from Claude Code's
        tool-call cycle, and (on some versions) system-reminder
        injections. The narrower properties below disambiguate.
        """
        return self.type == "user"

    @property
    def is_assistant(self) -> bool:
        """True if this record is an assistant-role record (agent emission)."""
        return self.type == "assistant"

    @property
    def is_system_reminder(self) -> bool:
        """True if this user-typed record carries a ``<system-reminder>``
        tag in its plain-text content.

        **Storage caveat.** On Claude Code 2.1.x transcripts (the
        version sampled at tool-design time), the runtime
        ``<system-reminder>`` injections operators see during sessions
        do not appear to be persisted to the JSONL — at least not in
        the user-record content surface this property reads. Tags
        that DO appear in transcripts are either (a) inside
        ``tool_use`` arguments (file writes whose content contained
        the literal text) or (b) in the top-level ``toolUseResult``
        field (mirror of tool-write outputs). Neither surface counts
        as a system reminder for analysis purposes.

        On versions / configurations where the tags ARE persisted as
        user-record content (or future runtime changes that surface
        them), this property correctly detects them. The 2026-05-20
        case's preservation of recurring system-reminder text
        verbatim suggests at least some sessions / versions do carry
        them.
        """
        if not self.is_user or self.text_content is None:
            return False
        return "<system-reminder>" in self.text_content

    @property
    def is_operator_message(self) -> bool:
        """True if this is a user-typed record with plain-text content
        that is NOT a system reminder — i.e., authored by the operator.

        Requires ``text_content`` to be set (string content, not a list
        of content blocks). User records whose content is a list (e.g.,
        carrying tool_result blocks from Claude Code's tool-call cycle)
        are not operator messages; this exclusion is load-bearing
        because they're the dominant user-record shape in real
        transcripts and an absent exclusion inflates operator-message
        counts by an order of magnitude.
        """
        return (
            self.is_user
            and self.text_content is not None
            and not self.is_system_reminder
        )

    def tool_uses(self) -> Iterator[dict[str, Any]]:
        """Iterate tool_use blocks in this record (assistant records only)."""
        for block in self.content_blocks:
            if isinstance(block, dict) and block.get("type") == "tool_use":
                yield block

    def text_blocks(self) -> Iterator[str]:
        """Iterate text content from text/thinking blocks (assistant only).

        Thinking blocks are included because regex analysis of agent
        emissions may legitimately target them (vocabulary-drift markers
        often appear in thinking). Callers wanting only user-visible text
        should filter on block type themselves via ``content_blocks``.
        """
        for block in self.content_blocks:
            if isinstance(block, dict) and block.get("type") in ("text", "thinking"):
                text = block.get("text") or block.get("thinking")
                if isinstance(text, str):
                    yield text


def parse(
    path: str | Path,
    *,
    include_internal: bool = False,
) -> Iterator[Record]:
    """Yield records from a session JSONL.

    Internal-state record types are skipped by default. Pass
    ``include_internal=True`` to include them (with ``role`` /
    ``content_blocks`` / ``text_content`` left at their defaults).

    Parsing is line-by-line; malformed lines raise ``json.JSONDecodeError``
    with the original line number attached via the exception's
    ``lineno`` attribute (which the json module already populates).
    """
    path = Path(path)
    with path.open(encoding="utf-8") as f:
        for line_no, raw_line in enumerate(f, start=1):
            raw_line = raw_line.strip()
            if not raw_line:
                continue
            rec_json = json.loads(raw_line)
            rec_type = rec_json.get("type", "unknown")

            if not include_internal and rec_type in _INTERNAL_TYPES:
                continue

            message = rec_json.get("message")
            role = None
            content_blocks: list[dict[str, Any]] = []
            text_content: str | None = None

            if isinstance(message, dict):
                role = message.get("role")
                content = message.get("content")
                if isinstance(content, list):
                    content_blocks = [c for c in content if isinstance(c, dict)]
                elif isinstance(content, str):
                    text_content = content

            yield Record(
                line_number=line_no,
                type=rec_type,
                raw=rec_json,
                role=role,
                content_blocks=content_blocks,
                text_content=text_content,
                timestamp=rec_json.get("timestamp"),
                uuid=rec_json.get("uuid"),
            )
