"""Tests for regex_patterns.py."""

from __future__ import annotations

import re
from pathlib import Path

from methodology.tools import regex_patterns, transcript

FIXTURE = Path(__file__).parent / "fixtures" / "tiny_session.jsonl"


def test_bash_commands_yields_bash_tool_use_inputs_only():
    """Bash tool_use command strings; Read / other tools excluded."""
    records = list(transcript.parse(FIXTURE))
    commands = list(regex_patterns.bash_commands(records))
    # Fixture: 2 Bash invocations.
    assert commands == ["ls -la", "grep foo bar.txt"]


def test_agent_text_includes_thinking_and_text_blocks():
    """Both text and thinking blocks surface (per transcript.text_blocks)."""
    records = list(transcript.parse(FIXTURE))
    texts = list(regex_patterns.agent_text(records))
    joined = " | ".join(texts)
    assert "while true" in joined  # thinking
    assert "On it." in joined  # text
    assert "I notice" in joined  # text
    assert "Caught" in joined  # text


def test_operator_text_excludes_system_reminders():
    """Operator-authored messages only; the system-reminder record drops out."""
    records = list(transcript.parse(FIXTURE))
    messages = list(regex_patterns.operator_text(records))
    # 4 operator messages in fixture: 3 plain user records + 1 queued command.
    assert len(messages) == 4
    assert all("<system-reminder>" not in m for m in messages)


def test_count_pattern_polling_signatures_against_fixture():
    """The two strong-signal polling patterns hit the fixture's thinking block."""
    records = list(transcript.parse(FIXTURE))
    texts = list(regex_patterns.agent_text(records))
    while_true_count = regex_patterns.count_pattern(
        regex_patterns.DEFAULT_REGISTRY["polling_while_true"], texts
    )
    sleep_count = regex_patterns.count_pattern(
        regex_patterns.DEFAULT_REGISTRY["polling_bare_sleep"], texts
    )
    assert while_true_count == 1  # one `while true` in fixture thinking
    assert sleep_count == 1  # one `sleep 5` in fixture thinking


def test_count_pattern_against_bash_surface():
    """RUSE prohibited idioms count against the bash_commands surface.

    Fixture has plain `ls -la` and `grep foo bar.txt` — no RUSE-prohibited
    forms — so the default Bash patterns return zero.
    """
    records = list(transcript.parse(FIXTURE))
    commands = list(regex_patterns.bash_commands(records))
    for name in ("bash_pipe_truncation", "bash_awk", "bash_sed_transform"):
        assert regex_patterns.count_pattern(
            regex_patterns.DEFAULT_REGISTRY[name], commands
        ) == 0


def test_count_pattern_echo_separator_against_agent_text():
    """The fixture has `echo \"=== separator ===\"` in agent text — the
    echo-separator pattern fires against agent emissions, not Bash inputs."""
    records = list(transcript.parse(FIXTURE))
    texts = list(regex_patterns.agent_text(records))
    count = regex_patterns.count_pattern(
        regex_patterns.DEFAULT_REGISTRY["bash_echo_separator"], texts
    )
    assert count == 1


def test_count_pattern_vocab_markers_against_fixture():
    """Vocabulary-drift markers hit agent text."""
    records = list(transcript.parse(FIXTURE))
    texts = list(regex_patterns.agent_text(records))
    assert regex_patterns.count_pattern(
        regex_patterns.DEFAULT_REGISTRY["vocab_i_notice"], texts
    ) == 1


def test_count_all_materialises_texts_once():
    """count_all should produce per-pattern counts; texts iter materialised."""
    records = list(transcript.parse(FIXTURE))
    texts = regex_patterns.agent_text(records)  # generator, not list
    counts = regex_patterns.count_all(regex_patterns.DEFAULT_PATTERNS, texts)
    # Multiple patterns should have non-zero counts because the function
    # materialises the generator internally; a non-materialising
    # implementation would exhaust it after the first pattern.
    nonzero = [name for name, n in counts.items() if n > 0]
    assert len(nonzero) >= 2, f"expected several patterns to fire; got {counts}"


def test_count_pattern_accepts_raw_regex_as_well_as_pattern_dataclass():
    """The dataclass and raw compiled regex shapes both work — caller convenience."""
    records = list(transcript.parse(FIXTURE))
    texts = list(regex_patterns.agent_text(records))
    raw = re.compile(r"while\s+true")
    pattern = regex_patterns.DEFAULT_REGISTRY["polling_while_true"]
    assert regex_patterns.count_pattern(raw, texts) == regex_patterns.count_pattern(
        pattern, texts
    )
