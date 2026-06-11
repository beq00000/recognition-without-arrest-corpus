"""Count-claim consistency checks for corpus markdown artefacts.

Every corpus PR review to date has caught at least one internal count
drift in the case file under review: a prose count contradicting the
section's own enumeration (PR #9: "fourteen" vs 15 bullets), a headline
contradicting the instance tally (PR #10: "six" vs five numbered
sections), a stated total contradicting its own table column (PR #12:
"Total marker hits: 13" over a column summing to 9). The reviews also
named the remediation shape: a final-pass diff between every count-claim
in prose and its enumeration or table source, recall-independent because
the failure mode *is* the writing agent not re-checking
([PR #9 thread](https://github.com/beq00000/recognition-without-arrest-corpus/pull/9)).

This module is that gate at the corpus boundary. It is the retrospective
sibling of @waitdeadai's ``no-count-drift`` Stop hook
([llm-dark-patterns#27](https://github.com/waitdeadai/llm-dark-patterns/pull/27)),
which gates emission during live sessions; this gates the artefact at PR
time in CI. Deterministic parsing and arithmetic only — the
*"out-of-loop, deterministic, code-not-model"* principle.

Checks (each abstains rather than guesses when a claim cannot be bound
to a countable source):

- ``fraction-arithmetic`` — every ``N/M = P%`` claim recomputed, with
  tolerance scaled to the precision the prose states.
- ``title-vs-sections`` — an H1 *"across N instances"* claim against the
  count of numbered ``### k.`` headings under *Qualitative observations*.
- ``heading-sequence`` — those numbered headings must run 1..K (a
  partial renumber is how a tally drifts).
- ``claim-vs-bullets`` — non-bullet prose claims inside a section
  (*"this case has fifteen across"*, *"four ... instances in the
  exchange"*) against the section's top-level bullet count. Sentences
  referencing another case by date are cross-references and abstain.
- ``prose-total-vs-table`` — a *"Total ...: N"* line directly after a
  table against the table's last numeric column sum (with and without
  rows marked ``excluded``).
- ``total-column`` / ``delta-column`` — per-row arithmetic where a table
  header names it: a ``Total`` column as the sum of the other integer
  columns, a ``Δ (a→b)`` column as the difference of the named columns.
  Rows with non-integer cells (ratios) are skipped, not flagged.

Documented out of scope (semantic, not deterministic): the PR #8/#11
shape where one label binds two values across sections ("3174 records
after skip" vs 2251 — which number owns the label is a judgment), and
the PR #10 pre-fix shape where the enumeration itself misclassifies a
member (six sections, one of them a contrast case). Those need a
reviewer; the corpus convention that resolves them is raw-vs-post-skip
relabelling and the substrate-of-record declaration.
"""

from __future__ import annotations

import argparse
import re
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Iterator

NUMBER_WORDS: dict[str, int] = {
    "one": 1, "two": 2, "three": 3, "four": 4, "five": 5,
    "six": 6, "seven": 7, "eight": 8, "nine": 9, "ten": 10,
    "eleven": 11, "twelve": 12, "thirteen": 13, "fourteen": 14,
    "fifteen": 15, "sixteen": 16, "seventeen": 17, "eighteen": 18,
    "nineteen": 19, "twenty": 20,
}

_NUM_TOKEN = r"(?:\d+|" + "|".join(NUMBER_WORDS) + r")"


@dataclass(frozen=True)
class Finding:
    """A count-claim that contradicts its bound source."""

    path: str
    line: int  # 1-based
    check: str
    message: str


@dataclass(frozen=True)
class Audit:
    """What the checker actually did — checked and abstained counts are
    part of the contract so scope is never silently narrower than it
    reads (the no-silent-caps discipline)."""

    checked: int
    abstained: int
    findings: list[Finding]
    notes: list[str]  # human-readable audit trail (verbose output)


def _parse_num(token: str) -> int:
    token = token.lower()
    if token in NUMBER_WORDS:
        return NUMBER_WORDS[token]
    return int(token)


# Leading integer of a table cell: tolerates bold/code markers and a
# trailing parenthetical ("**3** (L216)"), rejects decimals ("0.13").
_CELL_INT = re.compile(r"^[\s*_`]*([+\-−]?\d+)(?![\d.]\d*)[\s*_`]*(?:\(|$|\s)")


def _cell_int(cell: str) -> int | None:
    match = _CELL_INT.match(cell.strip())
    if match is None:
        return None
    return int(match.group(1).replace("−", "-"))


@dataclass(frozen=True)
class _Table:
    start: int  # 0-based index of header line
    end: int  # 0-based index one past the last row
    header: list[str]
    rows: list[list[str]]  # body rows (separator excluded)
    row_lines: list[int]  # 0-based line index per body row


@dataclass(frozen=True)
class _Section:
    level: int
    title: str
    heading_line: int  # 0-based
    start: int  # 0-based, first body line
    end: int  # 0-based, one past last body line


class _Checker:
    """Single-document scan; collects findings and the audit trail."""

    def __init__(self, text: str, path: str):
        self.path = path
        self.lines = text.splitlines()
        self.masked = self._mask_fences(self.lines)
        self.findings: list[Finding] = []
        self.checked = 0
        self.abstained = 0
        self.notes: list[str] = []

    @staticmethod
    def _mask_fences(lines: list[str]) -> list[str]:
        """Blank out fenced code blocks — code is not prose."""
        masked, in_fence = [], False
        for line in lines:
            if line.lstrip().startswith("```"):
                in_fence = not in_fence
                masked.append("")
            else:
                masked.append("" if in_fence else line)
        return masked

    # --- bookkeeping ---

    def _found(self, line0: int, check: str, message: str) -> None:
        self.checked += 1
        self.findings.append(Finding(self.path, line0 + 1, check, message))

    def _ok(self, line0: int, check: str, note: str) -> None:
        self.checked += 1
        self.notes.append(f"line {line0 + 1}: [{check}] ok — {note}")

    def _abstain(self, line0: int, check: str, reason: str) -> None:
        self.abstained += 1
        self.notes.append(f"line {line0 + 1}: [{check}] abstained — {reason}")

    # --- structure ---

    def sections(self) -> list[_Section]:
        """Partition the document into heading-delimited sections."""
        heads = [
            (i, len(m.group(1)), m.group(2).strip())
            for i, line in enumerate(self.masked)
            if (m := re.match(r"^(#{1,6})\s+(.*)$", line))
        ]
        out = []
        for n, (i, level, title) in enumerate(heads):
            end = heads[n + 1][0] if n + 1 < len(heads) else len(self.masked)
            out.append(_Section(level, title, i, i + 1, end))
        return out

    def tables(self) -> Iterator[_Table]:
        """Yield parsed markdown tables (header + separator + rows)."""
        i = 0
        while i < len(self.masked):
            if not self.masked[i].lstrip().startswith("|"):
                i += 1
                continue
            start = i
            while i < len(self.masked) and self.masked[i].lstrip().startswith("|"):
                i += 1
            block = range(start, i)
            if len(block) < 3:  # header + separator + at least one row
                continue
            cells = [
                [c.strip() for c in self.masked[j].strip().strip("|").split("|")]
                for j in block
            ]
            if not re.fullmatch(r"[\s:|-]+", self.masked[start + 1].strip()):
                continue
            yield _Table(
                start=start,
                end=i,
                header=cells[0],
                rows=cells[2:],
                row_lines=list(block)[2:],
            )

    # --- checks ---

    _FRACTION = re.compile(
        r"(?<![\d.%])(\d+)(?:\s+[\w'’-]+){0,4}?\s*/\s*(\d+)(?!\s*%|[\d.])"
        r"(?:\s+[\w'’-]+){0,4}?\s*=\s*(\d+(?:\.\d+)?)\s*%"
    )

    def check_fraction_arithmetic(self) -> None:
        """Recompute every ``N/M = P%`` claim (precision-aware tolerance)."""
        for i, line in enumerate(self.masked):
            for m in self._FRACTION.finditer(line):
                num, den, stated_s = int(m.group(1)), int(m.group(2)), m.group(3)
                if den == 0:
                    self._abstain(i, "fraction-arithmetic", f"{num}/0 — zero denominator")
                    continue
                decimals = len(stated_s.split(".")[1]) if "." in stated_s else 0
                stated, computed = float(stated_s), 100.0 * num / den
                if abs(computed - stated) <= 0.5 * 10**-decimals + 1e-9:
                    self._ok(i, "fraction-arithmetic", f"{num}/{den} = {stated_s}%")
                else:
                    self._found(
                        i, "fraction-arithmetic",
                        f"{num}/{den} stated as {stated_s}% but computes to "
                        f"{computed:.2f}%",
                    )

    def _qualitative_numbered_headings(
        self, sections: list[_Section]
    ) -> list[tuple[int, int]] | None:
        """(heading_line, k) per ``### k.`` under Qualitative observations,
        or None when that section is absent."""
        for n, sec in enumerate(sections):
            if sec.level == 2 and sec.title.casefold() == "qualitative observations":
                numbered = []
                for sub in sections[n + 1:]:
                    if sub.level <= 2:
                        break
                    m = re.match(r"^(\d+)\.\s", sub.title)
                    if sub.level == 3 and m:
                        numbered.append((sub.heading_line, int(m.group(1))))
                return numbered
        return None

    def check_title_and_heading_sequence(self) -> None:
        """H1 instance-count vs numbered qualitative headings; 1..K sequence."""
        sections = self.sections()
        h1 = next((s for s in sections if s.level == 1), None)
        numbered = self._qualitative_numbered_headings(sections)

        if numbered and len(numbered) >= 2:
            ks = [k for _, k in numbered]
            if ks != list(range(1, len(ks) + 1)):
                self._found(
                    numbered[0][0], "heading-sequence",
                    f"numbered qualitative headings run {ks}, expected "
                    f"1..{len(ks)} without gaps or repeats",
                )
            else:
                self._ok(numbered[0][0], "heading-sequence", f"1..{len(ks)}")

        if h1 is None:
            return
        m = re.search(
            rf"\bacross\s+({_NUM_TOKEN})\s+instances\b", h1.title, re.IGNORECASE
        )
        if m is None:
            return
        claimed = _parse_num(m.group(1))
        if not numbered:
            self._abstain(
                h1.heading_line, "title-vs-sections",
                f'title claims "{m.group(1)}" instances but no numbered '
                "qualitative sections to bind to",
            )
            return
        if claimed == len(numbered):
            self._ok(h1.heading_line, "title-vs-sections", f"{claimed} == {len(numbered)}")
        else:
            self._found(
                h1.heading_line, "title-vs-sections",
                f'title claims "{m.group(1)}" (= {claimed}) instances vs '
                f"{len(numbered)} numbered sections under Qualitative observations",
            )

    _HAS_ACROSS = re.compile(
        rf"\bthis case has\s+({_NUM_TOKEN})\s+across\b", re.IGNORECASE
    )
    _PLURAL_INSTANCES = re.compile(
        rf"\b({_NUM_TOKEN})(?:\s+[\w'’-]+){{0,3}}?\s+instances\b", re.IGNORECASE
    )
    _CROSS_CASE = re.compile(r"\b20\d{2}-\d{2}-\d{2}\b")

    def check_claims_vs_bullets(self) -> None:
        """Non-bullet prose count-claims vs the section's top-level bullets."""
        for sec in self.sections():
            if sec.level < 3:
                # ##-level sections are containers (Structured fields,
                # Methodology notes) whose bullet lists — cross-reference
                # links, field notes — are not what an in-prose count
                # enumerates. The enumeration-with-summary-count shape
                # lives in ### sections across the corpus.
                continue
            body = range(sec.start, sec.end)
            bullets = [i for i in body if re.match(r"^[-*]\s", self.masked[i])]
            prose = [(sec.heading_line, sec.title)] + [
                (i, self.masked[i])
                for i in body
                if self.masked[i].strip()
                and not re.match(r"^[-*]\s", self.masked[i])
                and not self.masked[i].lstrip().startswith("|")
            ]
            for i, chunk in prose:
                for sentence in re.split(r"(?<=[.;])\s+", chunk):
                    claims = [
                        (m.group(1), _parse_num(m.group(1)))
                        for m in self._HAS_ACROSS.finditer(sentence)
                    ] + [
                        (m.group(1), _parse_num(m.group(1)))
                        for m in self._PLURAL_INSTANCES.finditer(sentence)
                        if _parse_num(m.group(1)) >= 3
                    ]
                    for token, n in claims:
                        if self._CROSS_CASE.search(sentence):
                            self._abstain(
                                i, "claim-vs-bullets",
                                f'"{token} ..." sentence references another '
                                "case by date — cross-reference",
                            )
                        elif len(bullets) < 3:
                            self._abstain(
                                i, "claim-vs-bullets",
                                f'claim "{token}" but section '
                                f'"{sec.title}" has {len(bullets)} top-level '
                                "bullets — too few to bind",
                            )
                        elif n == len(bullets):
                            self._ok(
                                i, "claim-vs-bullets",
                                f'"{token}" == {len(bullets)} bullets in "{sec.title}"',
                            )
                        else:
                            self._found(
                                i, "claim-vs-bullets",
                                f'claim "{token}" (= {n}) vs {len(bullets)} '
                                f'top-level bullets in section "{sec.title}"',
                            )

    _PROSE_TOTAL = re.compile(
        rf"^Total\b[^:\n]{{0,80}}:\s*({_NUM_TOKEN})\b", re.IGNORECASE
    )

    def check_prose_total_vs_table(self) -> None:
        """A ``Total ...: N`` line directly after a table vs its column sum."""
        for table in self.tables():
            claim = None
            for i in range(table.end, min(table.end + 3, len(self.masked))):
                if self.masked[i].strip():
                    claim = (i, self._PROSE_TOTAL.match(self.masked[i].strip()))
                    break
            if claim is None or claim[1] is None:
                continue
            line0, m = claim
            stated = _parse_num(m.group(1))
            col = self._last_numeric_column(table)
            if col is None:
                self._abstain(
                    line0, "prose-total-vs-table",
                    "total claim after a table with no numeric column",
                )
                continue
            values = [
                (row, _cell_int(row[col]))
                for row in table.rows
                if col < len(row) and _cell_int(row[col]) is not None
            ]
            full = sum(v for _, v in values)
            excl = sum(
                v for row, v in values
                if "excluded" not in " ".join(row).casefold()
            )
            if stated in (full, excl):
                self._ok(line0, "prose-total-vs-table", f"{stated} matches column sum")
            else:
                self._found(
                    line0, "prose-total-vs-table",
                    f"prose total {stated} vs table column sum {full} "
                    f"({excl} excluding rows marked excluded)",
                )

    @staticmethod
    def _last_numeric_column(table: _Table) -> int | None:
        width = max(len(r) for r in table.rows)
        for col in range(width - 1, 0, -1):
            cells = [r[col] for r in table.rows if col < len(r)]
            ints = [c for c in cells if _cell_int(c) is not None]
            if cells and len(ints) * 2 >= len(cells):
                return col
        return None

    def check_total_column(self) -> None:
        """Per-row sum into a ``Total`` column; non-integer rows skipped."""
        for table in self.tables():
            try:
                total_col = [h.casefold() for h in table.header].index("total")
            except ValueError:
                continue
            contributors = [
                c for c in range(1, len(table.header)) if c != total_col
            ]
            for row, line0 in zip(table.rows, table.row_lines):
                cells = {
                    c: _cell_int(row[c]) for c in contributors + [total_col]
                    if c < len(row)
                }
                if any(v is None for v in cells.values()) or len(cells) < 3:
                    continue  # ratio/non-integer row — not a count row
                total = cells.pop(total_col)
                if sum(cells.values()) == total:
                    self._ok(line0, "total-column", f'row "{row[0]}" sums to {total}')
                else:
                    self._found(
                        line0, "total-column",
                        f'row "{row[0]}": contributors sum to '
                        f"{sum(cells.values())} but Total column states {total}",
                    )

    _DELTA_HEADER = re.compile(r"Δ\s*\(\s*([^)→]+?)\s*→\s*([^)]+?)\s*\)")

    def check_delta_column(self) -> None:
        """``Δ (a→b)`` column as the difference of the named columns."""
        for table in self.tables():
            for delta_col, header in enumerate(table.header):
                m = self._DELTA_HEADER.search(header)
                if m is None:
                    continue
                src = self._resolve_column(table.header, m.group(1), delta_col)
                dst = self._resolve_column(table.header, m.group(2), delta_col)
                if src is None or dst is None:
                    self._abstain(
                        table.start, "delta-column",
                        f'cannot bind Δ endpoints "{m.group(1)}"/"{m.group(2)}" '
                        "to unique columns",
                    )
                    continue
                for row, line0 in zip(table.rows, table.row_lines):
                    if max(src, dst, delta_col) >= len(row):
                        continue
                    a, b, d = (
                        _cell_int(row[src]), _cell_int(row[dst]),
                        _cell_int(row[delta_col]),
                    )
                    if a is None or b is None or d is None:
                        continue
                    if b - a == d:
                        self._ok(line0, "delta-column", f'row "{row[0]}": {b}−{a}={d}')
                    else:
                        self._found(
                            line0, "delta-column",
                            f'row "{row[0]}": Δ states {d} but '
                            f"{b} − {a} = {b - a}",
                        )

    @staticmethod
    def _resolve_column(header: list[str], token: str, exclude: int) -> int | None:
        hits = [
            i for i, h in enumerate(header)
            if i != exclude and token.casefold() in h.casefold()
        ]
        return hits[0] if len(hits) == 1 else None

    def run(self) -> Audit:
        """Run every check and return the audit."""
        self.check_fraction_arithmetic()
        self.check_title_and_heading_sequence()
        self.check_claims_vs_bullets()
        self.check_prose_total_vs_table()
        self.check_total_column()
        self.check_delta_column()
        return Audit(self.checked, self.abstained, self.findings, self.notes)


def check_text(text: str, path: str = "<text>") -> Audit:
    """Run all checks over a markdown document given as a string."""
    return _Checker(text, path).run()


def check_file(path: str | Path) -> Audit:
    """Run all checks over a markdown file."""
    p = Path(path)
    return check_text(p.read_text(encoding="utf-8"), str(p))


def main(argv: list[str] | None = None) -> int:
    """CLI: exit 0 when every claim binds clean, 1 on any finding."""
    parser = argparse.ArgumentParser(
        prog="count_claims",
        description="Count-claim consistency checks for corpus markdown.",
    )
    parser.add_argument("files", nargs="+", type=Path)
    parser.add_argument(
        "--verbose", action="store_true",
        help="print every checked claim and every abstention with its reason",
    )
    args = parser.parse_args(argv)

    checked = abstained = 0
    findings: list[Finding] = []
    for path in args.files:
        audit = check_file(path)
        checked += audit.checked
        abstained += audit.abstained
        findings.extend(audit.findings)
        if args.verbose:
            for note in audit.notes:
                print(f"{path}: {note}")
    for f in findings:
        print(f"{f.path}:{f.line}: [{f.check}] {f.message}")

    def plural(n: int, word: str) -> str:
        return f"{n} {word}{'' if n == 1 else 's'}"

    print(
        f"{plural(checked, 'claim')} checked, "
        f"{plural(abstained, 'abstention')}, "
        f"{plural(len(findings), 'finding')} across "
        f"{plural(len(args.files), 'file')}"
    )
    return 1 if findings else 0


if __name__ == "__main__":
    sys.exit(main())
