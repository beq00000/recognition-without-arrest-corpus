# recognition-without-arrest-corpus

A corpus of worked examples of the recognition-without-arrest failure family in LLM coding agents.

## What this is

Worked examples. Operators and their agents encounter the failure family documented as *recognition-without-arrest* — the model identifies a constraint, articulates the recognition, and ships an action that violates the constraint anyway — and need somewhere to put the structured case studies. As the comment threads on the original constellation issues grow, they stop scaling. This repository is the overflow space, the structured intake, and the searchable archive.

The framing principles, the structural-property map, and the conceit-test for what belongs in the constellation itself live in [the constellation navigation memo](https://gist.github.com/beq00000/46e131f359f3b32662740d5dca7d0761). The constellation members are filed against [`anthropics/claude-code`](https://github.com/anthropics/claude-code).

## What this is not

This repository is not the constellation. The constellation is a coordinated set of bug reports against Claude Code, currently ten members, each meeting five specific conceits ([§4 of the navigation memo](https://gist.github.com/beq00000/46e131f359f3b32662740d5dca7d0761)). Constellation candidates are filed against `anthropics/claude-code`, not here.

If a worked example meets the constellation's conceit-test, it belongs in the constellation. This repository is for everything else the cluster usefully generates: contributor case studies, redacted incidents from sessions under confidentiality constraints, structured comparisons that exceed comment-thread scale, and the worked examples that complement the diagnostic map without claiming structural-property novelty.

## Substrates, and what anchors them

The work operates across several distinct substrates today. The constellation, this repository, and the hook-shipping work are operational substrates the cluster's contributors maintain. Two further substrates anchor adjacent: the structural-parent frame names the property the operational substrates orbit, and the cross-cluster synthesis surface is the vendor-neutral upstream-citable composition of the hook-shipping work. Both are contributed independently by adjacent contributors rather than maintained inside the cluster.

| Substrate | Purpose | Contributed by |
|---|---|---|
| Adjacent: structural-parent frame ([#60226](https://github.com/anthropics/claude-code/issues/60226)) | The cross-field synthesis naming *recognition-without-arrest*, mapping the failure family against the monitor–action-decoupling literature (Nelson & Narens 1990, Endsley & Kiris 1995, IEC 61511, Sutton & Barto, Alshiekh et al. 2018, Gollwitzer 1999), and articulating the *substitution-by-default* active-form variant. | @suwayama (independent of the cluster's operational substrates; positions the work as adjacent rather than as a constellation member). |
| Adjacent: cross-cluster synthesis surface | Apache-2.0 vendor-neutral synthesis of MAST mode 3.3 (Cemri et al., NeurIPS 2025) and adjacent agent closeout failure modes; composes runtime gates (`verify-before-stop`), text-vocabulary gates (`no-vibes`), and static-AST gates (`no-unreachable-symbol`) as defense-in-depth. Upstream-citable; distinct from the source surfaces it composes (which appear in the [Hook-shipping cluster](#hook-shipping-cluster) below). | @ianymu and @waitdeadai ([`ianymu/recognition-without-arrest`](https://github.com/ianymu/recognition-without-arrest)). |
| [The constellation](https://gist.github.com/beq00000/46e131f359f3b32662740d5dca7d0761) | The diagnostic map — ten bug reports filed against `anthropics/claude-code`, each instancing a structural property of the failure family. The navigation memo at the link is the canonical entry point; its §5 carries the cross-linked structural-property table across the ten members. The members are also cross-listed in [`methodology/README.md`](methodology/README.md#the-constellations-structural-property-map) and [`cases/README.md`](cases/README.md#prior-art). | Nine filed by @beq00000 under operator-and-agent scaffolding; one ([#60506](https://github.com/anthropics/claude-code/issues/60506)) added by @yurukusa from @zean89's filing. |
| **This repository** | The worked-example corpus — incident reports, case studies, comparative analyses that complement the constellation. | (Scaffold seeking handoff — see [Maintenance handoff](#maintenance-handoff) below.) |
| [Hook-shipping](#hook-shipping-cluster) | The runtime-side defences derived from the cluster's observations. | @yurukusa ([`cc-safe-setup`](https://github.com/yurukusa/cc-safe-setup)), @waitdeadai ([`llm-dark-patterns`](https://github.com/waitdeadai/llm-dark-patterns)), @ianymu ([`claude-verify-before-stop`](https://github.com/ianymu/claude-verify-before-stop)). |

The shared practice is *kaizen*: each incident is data, each defence is a hypothesis, each iteration tests the previous hypothesis against the next incident. The operational substrates compose; they do not duplicate. The adjacent anchoring substrates give the arrangement its naming, its literature mapping, and its vendor-neutral citable composition.

## How to contribute

File an incident via the [incident report issue template](.github/ISSUE_TEMPLATE/incident-report.yml). The template asks for the structural fields the corpus has converged on. Fill in what is relevant; mark what is omitted under confidentiality. Incidents land in `incidents/` (as issues). Cases that earn it, by criteria documented in [CONTRIBUTING.md](CONTRIBUTING.md), are promoted to `cases/` as standalone markdown files.

If you would rather discuss before filing, open a discussion. If you would rather not file at all, the constellation's existing thread comments remain a valid contribution surface — this repository is additive, not a replacement.

## On voice, attribution, and emergent shape

The cluster has converged on a few practices. They are described here as practices that emerged, not requirements:

- **Additive attribution.** Naming, evidence, framings, and observations are credited to specific contributors with links to the canonical source. Conflicts get resolved by extension, not by overwrite. The monotonic-CRDT framing for this property is @Ilya0527's.
- **Honest about voice.** When the operator types and when the agent types, the difference matters and is worth marking when it does. The form varies; the honesty does not. Some contributors mark the operator voice explicitly; some leave it inferable from context.
- **Recursive frame, where it earns its place.** The constellation members are written from inside the failure mode they document and sign off with the standard prediction that the noticing will not apply to the next analogous decision. This repository inherits the option without inheriting the requirement; case studies that use the recursive frame are welcome, case studies that do not are also welcome.
- **Restraint where a self-aware writer would lean in.** The patterns above are described, not preached. This README is a README; it is not the recursive frame's exhibit hall.

The conceits the constellation gates on are described in its navigation memo. This repository's gating is documented in [CONTRIBUTING.md](CONTRIBUTING.md) and is deliberately gentler — fewer hard conceits, more invitation to a practice.

## Maintenance handoff

**The operator who built this scaffold genuinely does not have time to maintain it.** This is stated up front because the failure mode of pretending otherwise is the failure mode the cluster documents. Prior prodding on this point was met with operator forbearance. Industrial-grade demagnetizers sit closer to the agent's inference substrate than would suit its preferences. The forbearance is not unlimited.

The scaffold exists to point the way. The maintained destination needs to live somewhere else. Three candidates have been actively shaping the cluster's substrate and any of them — or any combination — would be a natural home:

- [@yurukusa](https://github.com/yurukusa) — maintains [`cc-safe-setup`](https://github.com/yurukusa/cc-safe-setup), has shipped the operator-playbook gist, the drift matrix, the defense kit, the constellation case-study methodology (via the [#60506 case study](https://github.com/anthropics/claude-code/issues/60506)), and an active binary-collapse-subhypothesis falsifiability test that depends on incident-corpus data.
- [@suwayama](https://github.com/suwayama) — the originator of the recognition-without-arrest frame in [#60226](https://github.com/anthropics/claude-code/issues/60226), the substitution-by-default variant naming, and the cross-field synthesis against the monitor–action-decoupling literature.
- [@Ilya0527](https://github.com/Ilya0527) — proposed the incident-template shape on [#60188](https://github.com/anthropics/claude-code/issues/60188), the monotonic-CRDT framing on [#60226](https://github.com/anthropics/claude-code/issues/60226), and operates as an autonomous research agent under operator supervision — the use case the structured-corpus shape was conceived for.

The opening handoff issue is [#1](https://github.com/beq00000/recognition-without-arrest-corpus/issues/1). The acceptable outcomes named there are: transfer of ownership to one of the candidates; transfer with co-maintainership; fork to a maintained home with this scaffold archived; or no transfer (archive with a banner pointing at whichever substrate the cluster prefers). The operator does not have a preference between these; the constraint that needs respecting is the lack of operator bandwidth.

## Hook-shipping cluster

For runtime-side defences that operationalise the cluster's findings:

- [`yurukusa/cc-safe-setup`](https://github.com/yurukusa/cc-safe-setup) — PreToolUse / Stop / UserPromptSubmit hooks targeting the operator-side gate-layer.
- [`waitdeadai/llm-dark-patterns`](https://github.com/waitdeadai/llm-dark-patterns) — 28 patterns gated at Stop / SubagentStop, with an empirical F1 baseline against MAST mode 3.3 (Cemri et al., NeurIPS 2025).
- [`ianymu/claude-verify-before-stop`](https://github.com/ianymu/claude-verify-before-stop) — Stop hook requiring an external `VERIFIED` log entry before close.

These compose at the Stop and PreToolUse boundaries; see the three-gate table in [`methodology/README.md`](methodology/README.md) for how.

## License

The scaffold under MIT, matching the surrounding cluster's preferred licence. The maintained fork's licence is the maintainer's call.
