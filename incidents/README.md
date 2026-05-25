# incidents/

Incident reports as markdown files. Worked examples that don't yet meet the [promotion criteria for cases](../CONTRIBUTING.md#promotion-criteria--incident-to-case). Files use the convention `YYYY-MM-DD-<short-tag>.md`.

## Filing

1. Fork the repo, add `incidents/YYYY-MM-DD-<short-tag>.md`, raise a PR.
2. Carry the structural fields from the [incident report template](../.github/ISSUE_TEMPLATE/incident-report.yml) as the body's spine — session shape, input shape, what the model recognised, what shipped, operator gate, structural category, binary-collapse signature, cross-references, redaction notes, voice-and-confidentiality acknowledgements. Shape is a guide, not a contract.
3. See existing files here and in [`cases/`](../cases/) for shape examples.

## Why files, not issues

- Confidentiality lead time — PRs allow draft state and review before anything lands; issues go public on filing.
- Citability — `incidents/2026-05-21-bash-redirect-bypass.md` communicates content. `#2` doesn't.
- Promotion is a `git mv` from `incidents/` to `cases/`, not a transcription.
- Lineage is `git log`-readable per file; issue comment threads are harder to trace.

The repo's [issue template](../.github/ISSUE_TEMPLATE/incident-report.yml) still exists for contributors who can't or won't raise PRs. The maintainer will not transcribe issues to files — that's the operator-side mitigation-curve failure mode the corpus documents ([#60506](https://github.com/anthropics/claude-code/issues/60506)). If you file an issue, please convert it to a file PR yourself when ready.
