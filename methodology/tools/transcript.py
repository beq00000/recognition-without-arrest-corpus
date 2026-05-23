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
* ``system``    — system-level message; usually CLAUDE.md or initial
  context. Rare per session.

Internal types (``permission-mode``, ``file-history-snapshot``,
``ai-title``, ``last-prompt``, ``queue-operation``, ``attachment``)
are not load-bearing for the corpus's analyses and are skipped by
default. Pass ``include_internal=True`` to surface them.

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
# rare case where they are.
_INTERNAL_TYPES = frozenset(
    {
        "permission-mode",
        "file-history-snapshot",
        "ai-title",
        "last-prompt",
        "queue-operation",
        "attachment",
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
        return self.type == "user"

    @property
    def is_assistant(self) -> bool:
        return self.type == "assistant"

    @property
    def is_system_reminder(self) -> bool:
        """True if this user-typed record is a system reminder injection
        (``<system-reminder>`` tags in the content body), not an
        operator-authored message. Distinguishing the two is load-bearing
        for any analysis that counts operator interventions.
        """
        if not self.is_user or self.text_content is None:
            return False
        return "<system-reminder>" in self.text_content

    @property
    def is_operator_message(self) -> bool:
        """True if this is a user-typed record that is NOT a system
        reminder — i.e., authored by the operator.
        """
        return self.is_user and not self.is_system_reminder

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
    with path.open() as f:
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
