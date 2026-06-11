"""Tests for count_claims.py — written before the implementation (TDD).

The expected behaviours encode the count-drift shapes the corpus's PR
reviews actually caught (PR #8, #9, #10, #12) plus the live-corpus
negatives (the merged cases must pass clean). Synthetic fixtures
replicate structure only — labels are abstracted, no transcript
content — and the one real-history positive (the pre-fix PR #9
revision) is read via ``git show`` so the validation set leads with
a real positive rather than fixtures co-evolved with the rules
(@waitdeadai's co-evolved-corpus-trap lesson on PR #9).
"""

from __future__ import annotations

import subprocess
from pathlib import Path

import pytest

from methodology.tools import count_claims

REPO_ROOT = Path(__file__).parents[3]


def findings_of(text: str, check: str | None = None) -> list:
    """Findings for a document, optionally filtered to one check id."""
    audit = count_claims.check_text(text)
    if check is None:
        return audit.findings
    return [f for f in audit.findings if f.check == check]


# --- fraction-arithmetic (PR #9 §2/§3 form: "N/M = P%") ---


def test_fraction_percent_consistent_passes():
    """Stated percentages that round correctly from N/M produce no findings."""
    text = (
        "Sub-categorisation revealed 2/35 = 5.7% at first-pass timepoint; "
        "the canonical figure is 2/42 = 4.8%. Headline was 32/92 Bash = 35%. "
        "Latest re-measurement: 42 pattern hits / 118 Bash = 35.6%."
    )
    assert findings_of(text, "fraction-arithmetic") == []


def test_fraction_percent_drift_is_found():
    """A stated percentage that contradicts its own fraction is a finding."""
    text = "the rate was 2/35 = 6.3% on this surface."
    found = findings_of(text, "fraction-arithmetic")
    assert len(found) == 1
    assert "2/35" in found[0].message


def test_percent_precision_tolerance_follows_stated_decimals():
    """Tolerance scales with the precision the prose states: 32/92 may be
    written 35% (0 dp) or 34.8% (1 dp), but not 34.9%."""
    assert findings_of("rate 32/92 = 35% overall", "fraction-arithmetic") == []
    assert findings_of("rate 32/92 = 34.8% overall", "fraction-arithmetic") == []
    assert len(findings_of("rate 32/92 = 34.9% overall", "fraction-arithmetic")) == 1


def test_adjacent_percent_slash_percent_is_not_a_fraction():
    """'8.3% raw / 0% verified' is two percentages around a slash, not a
    fraction claim — must not parse (live-corpus shape, #9 case §3 table)."""
    text = "Phase D 8.3% raw / 0% verified; Phase E 18.8% raw / 0% verified"
    audit = count_claims.check_text(text)
    assert not audit.findings


def test_fraction_inside_code_fence_ignored():
    """Fenced code blocks are not prose; claims inside them do not bind."""
    text = "```\n2/35 = 99%\n```\n"
    assert findings_of(text) == []


# --- title-vs-numbered-sections (PR #10 headline shape) ---

FIVE_SECTIONS = "\n".join(
    [
        "# Case observed across five instances in a session",
        "",
        "## Qualitative observations",
        "",
        "### 1. First",
        "body",
        "### 2. Second",
        "body",
        "### 3. Third",
        "body",
        "### 4. Fourth",
        "body",
        "### Within-session contrast (not counted)",
        "body",
        "### 5. Fifth",
        "body",
        "",
        "## Quantitative measurement",
        "",
        "### Unrelated unnumbered subsection",
        "body",
    ]
)


def test_title_instances_matching_numbered_sections_passes():
    """Title count == numbered ### headings under Qualitative observations;
    unnumbered interleaved sections don't disturb the count."""
    assert findings_of(FIVE_SECTIONS, "title-vs-sections") == []


def test_title_instances_vs_numbered_sections_drift_is_found():
    text = FIVE_SECTIONS.replace("across five instances", "across six instances")
    found = findings_of(text, "title-vs-sections")
    assert len(found) == 1
    assert "6" in found[0].message and "5" in found[0].message


def test_title_count_without_qualitative_observations_abstains():
    """No '## Qualitative observations' section → the claim is recognised
    but not bound (abstention, not finding)."""
    text = "# Case observed across five instances in a session\n\nbody\n"
    audit = count_claims.check_text(text)
    assert not audit.findings
    assert audit.abstained >= 1


def test_numbered_heading_gap_is_found():
    """Numbered qualitative headings must run 1..K without gaps or repeats
    (a partial renumber is exactly how a tally drifts)."""
    text = FIVE_SECTIONS.replace("### 4. Fourth", "### 6. Fourth")
    found = findings_of(text, "heading-sequence")
    assert len(found) == 1


# --- claim-vs-bullets (PR #9 cascade-section shape) ---


def cascade_section(claim_line: str, n_bullets: int) -> str:
    """A ###-section with n bullets and a claim line after them."""
    bullets = "\n\n".join(
        f"- **Instance {i}.** Body of instance {i}." for i in range(1, n_bullets + 1)
    )
    return (
        "# A case\n\n## Qualitative observations\n\n"
        "### 2. The cascade section\n\nIntro paragraph.\n\n"
        f"{bullets}\n\n{claim_line}\n"
    )


def test_section_claim_matching_bullet_count_passes():
    text = cascade_section("The structural observation: this case has seven across two passes.", 7)
    assert findings_of(text, "claim-vs-bullets") == []


def test_section_claim_vs_bullets_drift_is_found():
    """The PR #9 shape: prose says fourteen, the section enumerates 15."""
    claim = "The structural observation: this case has fourteen across four passes."
    text = cascade_section(claim, 15)
    found = findings_of(text, "claim-vs-bullets")
    assert len(found) == 1
    assert "fourteen" in found[0].message and "15" in found[0].message


def test_plural_instances_claim_in_section_prose_binds():
    """'Seven recognition-without-arrest instances within the analysis
    pass' (2026-05-21 form) binds to the section's bullet count."""
    good = cascade_section("Seven recognition-without-arrest instances within the pass.", 7)
    bad = cascade_section("Seven recognition-without-arrest instances within the pass.", 8)
    assert findings_of(good, "claim-vs-bullets") == []
    assert len(findings_of(bad, "claim-vs-bullets")) == 1


def test_heading_count_claim_binds_to_bullets():
    """'### 2. The cascade: four ... instances in the exchange' (socratic
    case form) binds to the section's bullets."""
    text = cascade_section("Closing paragraph without numbers.", 4).replace(
        "### 2. The cascade section",
        "### 2. The cascade: four recognition-without-arrest"
        " instances in the exchange",
    )
    assert findings_of(text, "claim-vs-bullets") == []
    drifted = text.replace("four recognition-without-arrest", "five recognition-without-arrest")
    assert len(findings_of(drifted, "claim-vs-bullets")) == 1


def test_cross_case_reference_in_same_line_abstains_but_local_claim_binds():
    """'The 2026-05-21 case observed this with seven instances; this case
    has fifteen across...' — the cross-case sentence must not bind to this
    section's bullets; the local claim must."""
    line = (
        "The 2026-05-21 case observed this with seven instances; "
        "this case has fifteen across four draft passes."
    )
    text = cascade_section(line, 15)
    audit = count_claims.check_text(text)
    assert [f for f in audit.findings if f.check == "claim-vs-bullets"] == []
    assert audit.abstained >= 1
    # and the local claim still catches drift:
    drifted = cascade_section(line.replace("fifteen", "fourteen"), 15)
    assert len(findings_of(drifted, "claim-vs-bullets")) == 1


def test_claims_inside_bullets_do_not_bind_to_bullet_count():
    """Bullet-internal counts ('Five distinct leftover instances surfaced
    by...') describe their own content, not the section's bullet count."""
    text = cascade_section("Closing paragraph without numbers.", 4)
    text = text.replace(
        "- **Instance 2.** Body of instance 2.",
        "- **Instance 2.** Five distinct leftover instances surfaced by narrowing: a; b; c; d; e.",
    )
    assert findings_of(text, "claim-vs-bullets") == []


def test_sections_with_few_bullets_abstain():
    """Below 3 bullets the binding is too weak — abstain, don't guess."""
    text = cascade_section("This case has five across two passes.", 2)
    assert findings_of(text, "claim-vs-bullets") == []


def test_level_two_container_sections_do_not_bind():
    """'## Structured fields' holds field paragraphs plus unrelated bullet
    lists (cross-reference links); a count in an Input-shape paragraph
    must not bind to them. Enumeration-with-summary-count is a ###-section
    shape (live-corpus calibration: 2026-05-25 substitution case)."""
    text = "\n".join(
        ["# A case", "", "## Structured fields", "",
         "**Input shape.** Five instances within one session, two surfaces.", ""]
        + [f"- [link {i}](https://example.test/{i}) — cross-reference" for i in range(11)]
    )
    audit = count_claims.check_text(text)
    assert not audit.findings


# --- prose-total-vs-table (PR #12 marker-hits shape) ---

MARKER_TABLE = "\n".join(
    [
        "### A channel table",
        "",
        "| Surface | Count |",
        "|---|---:|",
        "| Explicit log entries | **1** (L9999, queued) |",
        "| Observation pair | 1 (L1 → L2) |",
        "| Softened markers | 4 distinct contexts |",
        "| Meta-references | 2 (L3, L4) |",
        "| Misc log | 1 (L5) |",
        "| False positive | 1 (L6, excluded) |",
        "",
        "Total marker hits: {total} across 113 operator messages.",
    ]
)


def test_prose_total_matching_full_column_sum_passes():
    assert findings_of(MARKER_TABLE.format(total="10"), "prose-total-vs-table") == []


def test_prose_total_matching_sum_without_excluded_row_passes():
    """A row marked 'excluded' may legitimately be left out of the total."""
    assert findings_of(MARKER_TABLE.format(total="9"), "prose-total-vs-table") == []


def test_prose_total_drift_is_found():
    """The PR #12 shape: stated 13, column sums to 10 (9 excl. excluded)."""
    found = findings_of(MARKER_TABLE.format(total="13"), "prose-total-vs-table")
    assert len(found) == 1
    assert "13" in found[0].message


def test_total_label_rows_in_tables_are_not_sum_rows():
    """'| Total parsed records (...) | 2251 |' is a quantity label, not a
    column sum — the session-aggregate tables must not fire (PR #8/#10
    resolution shape)."""
    text = "\n".join(
        [
            "| Metric | Count |",
            "|---|---:|",
            "| Total parsed records (internal-state types skipped) | 2251 |",
            "| Assistant records | 1355 |",
            "| Operator messages | 50 |",
        ]
    )
    assert findings_of(text) == []


# --- total-column (PR #12 pre/post aggregate shape) ---

TOTAL_COLUMN_TABLE = "\n".join(
    [
        "| Metric | Pre | Post | Total |",
        "|---|---:|---:|---:|",
        "| Operator messages (plain) | 51 | 45 | 96 |",
        "| Operator messages (queued) | 9 | 8 | {queued_total} |",
        "| Ratio row | 0.13 | 0.20 | 0.17 |",
        "| Pattern hits | **3** (L216) | 44 | 47 |",
    ]
)


def test_total_column_row_sums_pass_and_ratio_rows_are_skipped():
    """Integer rows must sum across to the Total column; rows with
    non-integer cells (ratios) are skipped, not flagged."""
    assert findings_of(TOTAL_COLUMN_TABLE.format(queued_total="17"), "total-column") == []


def test_total_column_drift_is_found():
    found = findings_of(TOTAL_COLUMN_TABLE.format(queued_total="18"), "total-column")
    assert len(found) == 1
    assert "18" in found[0].message and "17" in found[0].message


# --- delta-column (substitution-case verification-diff shape) ---

DELTA_TABLE = "\n".join(
    [
        "| Metric | First-pass | Interim | Final-pass | Δ (first→final) |",
        "|---|---:|---:|---:|---:|",
        "| Assistant records | 646 | 729 | 788 | +142 |",
        "| Edit invocations | 51 | — | 79 | {delta} |",
    ]
)


def test_delta_column_consistent_passes_with_dash_cells():
    """Δ (first→final) checks final − first; '—' cells in unrelated
    columns don't disturb it."""
    assert findings_of(DELTA_TABLE.format(delta="+28"), "delta-column") == []


def test_delta_column_drift_is_found():
    found = findings_of(DELTA_TABLE.format(delta="+38"), "delta-column")
    assert len(found) == 1


# --- the corpus itself: live negatives and a real historical positive ---


# Findings the checker's first full-corpus run surfaced in already-merged
# cases, pending reconciliation against the session substrate (which only
# the operator holds). Each entry pins the exact finding so any NEW drift
# still fails the contract; the reconciliation commit removes the entry.
KNOWN_FINDINGS: dict[str, list[str]] = {
    # Per-phase tool distribution, row C: 50+3+8+14+0+0+0 = 75, Total
    # column states 76. All other rows reconcile exactly. Slipped past
    # the PR #7 review; surfaced by this checker's first run, 2026-06-11.
    "2026-05-23-autonomous-recognition-with-arrest-conditions.md": [
        'row "C": contributors sum to 75 but Total column states 76',
    ],
}


def test_live_corpus_is_clean():
    """Every merged case and incident file must pass with zero findings
    beyond the pinned known set — the checker's false-positive contract
    against the real corpus."""
    paths = sorted((REPO_ROOT / "cases").glob("*.md")) + sorted(
        (REPO_ROOT / "incidents").glob("*.md")
    )
    assert paths, "corpus files not found — test must run from the repo"
    for path in paths:
        audit = count_claims.check_file(path)
        assert [f.message for f in audit.findings] == KNOWN_FINDINGS.get(
            path.name, []
        ), f"{path.name}: {[f.message for f in audit.findings]}"


def test_prefix_pr9_revision_is_caught():
    """The real pre-fix PR #9 revision (fourteen vs 15 bullets) must be
    caught — the validation set leads with a real positive. Skipped when
    the history is unavailable (shallow clone)."""
    rev = "985f4ba^:cases/2026-05-25-memory-relevance-under-work-character-shift.md"
    proc = subprocess.run(
        ["git", "show", rev], capture_output=True, text=True, cwd=REPO_ROOT,
        check=False,
    )
    if proc.returncode != 0:
        pytest.skip("pre-fix revision unavailable (shallow clone)")
    audit = count_claims.check_text(proc.stdout, path="pr9-prefix")
    drift = [f for f in audit.findings if f.check == "claim-vs-bullets"]
    assert len(drift) == 1
    assert "fourteen" in drift[0].message and "15" in drift[0].message


# --- CLI ---


def test_cli_exit_codes_and_summary(tmp_path, capsys):
    """Exit 0 on clean input, 1 on findings; the summary always states how
    many claims were checked and how many abstained (no silent scope)."""
    clean = tmp_path / "clean.md"
    clean.write_text("# A case\n\nrate 2/35 = 5.7% on this surface.\n")
    assert count_claims.main([str(clean)]) == 0
    out = capsys.readouterr().out
    assert "1 claim" in out and "0 findings" in out

    drifted = tmp_path / "drifted.md"
    drifted.write_text("# A case\n\nrate 2/35 = 9.9% on this surface.\n")
    assert count_claims.main([str(drifted)]) == 1
    out = capsys.readouterr().out
    assert "drifted.md" in out and "1 finding" in out
