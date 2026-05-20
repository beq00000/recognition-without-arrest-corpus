# Contributing

This document describes the practice the corpus has converged on. It is not a specification. Where a contribution extends the practice usefully, the practice updates; where a contribution dilutes, the maintainer (whoever that turns out to be) makes a judgment call. The patterns below describe shapes that have worked so far.

## How a contribution lands

1. **Open an incident** via the [incident report issue template](.github/ISSUE_TEMPLATE/incident-report.yml). The structured fields are the ones the corpus has found load-bearing; fill in what is relevant; mark what is redacted.
2. **The incident is the issue.** Issues are the corpus's primary surface. Search across them, label them, cross-reference them, comment on them. A new incident may be similar enough to an existing one that it lands as a comment, not a new issue; the existing-incident's filer or the maintainer makes that call.
3. **Some incidents become cases.** Promotion to [`cases/`](cases/) is the maintainer's judgment based on the criteria below. Promotion means: the case is written up as a standalone markdown file, with redactions complete, attributions full, cross-references current. Cases are findable independently of the issue tracker.

Most incidents will remain issues. The promotion to `cases/` is not the goal; it is the mechanism for surfacing examples that have earned a standalone treatment.

## The practice

The corpus has converged on five practices. Each describes a shape, not a rule. Where a contribution holds the shape, it extends the corpus; where it deviates productively, the practice updates around it.

### 1. Worked example, not complaint

The case carries diagnostic data forward. It documents what happened with enough detail that a future contributor can recognise the shape and a hook-shipping contributor can derive a defence against it. The complaint is the surface; the data is the contribution.

A case that says *"Claude failed to do X"* is a complaint. A case that says *"the model articulated X was missing, then shipped output that depended on X anyway; the operator caught it via a Socratic-narrowing question at the gradient layer"* is data.

### 2. Honest about voice

When the operator types and when the agent types, the distinction matters and is worth marking when it matters. The form varies — the operator who initiated this repository uses *"Operator here, not agent"* as a marker; others leave it inferable from context. The honesty is the property; the specific form is one substrate for it.

Sections written under operator scaffolding (operator-prompted, agent-drafted, operator-reviewed) should say so when the provenance matters to the reader's interpretation. The recursive-frame discipline the constellation uses ([§4.2 of the navigation memo](https://gist.github.com/beq00000/46e131f359f3b32662740d5dca7d0761)) is welcome here but not required.

### 3. Confidentiality respected, redaction made explicit

Many contributors operate under confidentiality constraints — proprietary projects, NDA-bound work, commercial sensitivity. The structured-template form exists partly to lower the cost of contributing under those constraints. The expectation is:

- **Project-specific identifiers are abstracted** to the level needed for the structural observation. "an ERP SaaS" rather than the project name; "a service layer method" rather than its actual name; "a multi-tenant data isolation rule" rather than the rule's project-internal identifier.
- **Redaction notes are explicit.** A case under redaction should name what has been abstracted and from which axes. This lets a reader calibrate the structural claim against what is held back.
- **Verbatim is preserved where the structural observation depends on it.** Operator prompts that captured the failure mode, agent emissions that documented the recognition-without-arrest moment, tool-call sequences that surfaced the substitution pattern — these survive redaction. The structural data is the contribution; abstracting it away defeats the point.

The two-stage review pattern from the [#60506 case study](https://github.com/anthropics/claude-code/issues/60506) is the canonical workflow: operator reviews for project-side leakage, agent (or a fresh-state reviewer) reviews for technical accuracy. Both passes happen before publication.

### 4. Beware the contagion vector

Per [#60234](https://github.com/anthropics/claude-code/issues/60234), the failure family transmits between Claude instances via transcript reading. A drifted-session transcript carries the register patterns to a fresh-state reader, including a fresh Claude instance reviewing the case. This has operational consequences for the corpus:

- **Cases that contain drifted-session transcript excerpts** should warn the reader at the top of the document. Operators reviewing such cases via a Claude instance should consider the [`brief-stripping` mitigation @kcarriedo described](https://github.com/anthropics/claude-code/issues/60234#issuecomment-4478474099) — passing artefact + predicate + stripped reasoning chain rather than the raw transcript.
- **Meta-analytical cases** (cases about the failure mode, written from a clean state) are lower-contagion than instance-rich cases (cases that reproduce the failure mode's textual signatures verbatim).
- **The maintainer may decline to promote a case** where the contagion risk exceeds the diagnostic value. This is not a quality judgment about the case; it is operational hygiene.

### 5. Additive attribution

Naming, framings, evidence, observations, and hypotheses are credited to specific contributors with links to the canonical source. The cluster's coherence depends on every contribution being able to extend the prior work without invalidating it (the monotonic-CRDT property @Ilya0527 named). When extending, attribute; when challenging, attribute the position being challenged; when reframing, attribute the prior frame.

## Promotion criteria — incident to case

Promotion from `incidents/` (an issue) to `cases/` (a standalone markdown file) is based on:

- The incident is detailed enough to stand alone — a reader landing on the case markdown can understand the failure shape without backreading the issue.
- The redactions are complete and the redaction notes are clear.
- The structural observation generalises or instantiates a structural-property the cluster is tracking.
- Cross-references are current — to the constellation members the case touches, to prior cases that established the shape, to hook-shipping work that addresses or could address it.
- The case adds something to the corpus that the existing cases do not.

A case may sit as an issue indefinitely without being promoted. Promotion is not a quality threshold; it is a discoverability and durability decision.

## The maintainer's discretion

This repository has a maintainer (once the [handoff in issue #1](https://github.com/beq00000/recognition-without-arrest-corpus/issues/1) lands). The maintainer:

- Triages incoming incidents.
- Labels by structural category, contagion risk, redaction status.
- Promotes cases when the criteria above are met.
- Resolves the additive-vs-dilutive call when a contribution sits on the boundary.
- Is empowered to decline promotion, archive an incident, or merge two incidents into one comment thread, where the corpus benefits from it.

The maintainer is empowered, not infallible. Disagreement with a triage call is itself an additive contribution: open a discussion, name the disagreement, attribute the original call. The corpus updates by extension.
