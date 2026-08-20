# Agentic RAG Daily Agent Adapter

[`RADAR_AGENT_PROTOCOL.md`](RADAR_AGENT_PROTOCOL.md) is the authoritative family contract. This file supplies the Agentic RAG source lanes, acceptance questions, evidence decomposition, canonical paths, and validation commands. The recurring scheduler is a thin launcher. The Daily Agent orchestrator is the only writer.

## Frozen run and source lanes

At preflight freeze the protocol version, run ID, repository head, Asia/Shanghai local time, rolling 7-day and 30-day windows, last closed ISO week/calendar month, and enabled lanes. Use overlapping discovery windows, wider after weekends or source outages.

Assign independent, read-only scouts to:

- arXiv `cs.IR`, `cs.CL`, `cs.AI`, and adjacent recent/cross-list feeds;
- proceedings and scholarly indexes for retrieval, search, and information-seeking systems;
- author/project repositories and release notes for protocol, artifact, or version changes;
- backward/forward citation and sibling-Radar leads when they identify a primary source.

Search concepts, not only the phrase “agentic RAG”: adaptive/active retrieval, query planning, direct corpus interaction, evidence localization/materialization, retrieval budgeting/stopping, deep research, verifier-guided retrieval, stateful search, GraphRAG agents, retrieval-policy learning, cross-source tools, and adjacent memory/search work.

Lane failure is private run evidence. Other lanes continue, but a candidate never becomes public merely because another lane was unavailable. Ephemeral candidate state is written only under the git-ignored `.radar-private/runs/<run_id>.json` path or kept in agent memory.

## Identity and scope gates

The Identity Resolver canonicalizes arXiv, DOI, venue, title/version changes, code/project repository, dataset, and protocol release before any importance judgment. Never merge by title similarity alone.

The Domain Judge answers four questions in order:

1. Is external retrieval, search, or context acquisition substantive?
2. Does an agent/controller/policy materially control whether, what, where, how, or how much information is acquired?
3. Is that control part of the research contribution rather than implementation glue?
4. Against the closest static, adaptive, and historical design point, is the smallest claimed delta identifiable?

If questions 1–3 are not clearly yes, reject or keep the candidate private. Relevance and importance remain separate.

## Full-text evidence contract

No Timeline item is accepted from an abstract. A Full-Text Reader records primary-source locations for:

- mechanism and the external-information loop: `search → inspect → continue/redirect/stop`;
- closest meaningful comparison and what was actually held fixed;
- decisive and negative evidence, including evidence coverage/validity;
- offline and online costs: construction/update work, calls, inspected/retrieved tokens, latency, controller/probe compute, and model calls;
- strongest limitation and alternative explanation.

For every strong gain, decompose:

`evidence coverage × corpus observability × retrieval interface × harness/delivery × environment state × agent state × policy × realized resources × model × training protocol`

A gain is not assigned to policy when interface, harness, available evidence, state, model, or realized budget changed without a matched control. Author claims remain labeled as claims.

The Skeptical Reviewer independently states the strongest control mismatch, missing evidence, negative boundary, historical alternative, and publication ceiling. It may lower the ceiling but may not invent facts.

## Canonical-first transaction

Accepted work is written in this order:

1. `data/papers/<identity>.json` with canonical identity, provenance, full-text status, and v2 time/map fields for post-cutover records;
2. paired deep notes `papers/<identity>.md` and `papers/<identity>.zh.md`;
3. category and research-line relationships;
4. grounded visual contract, with incomplete render state isolated from public pages;
5. Chinese/English Timeline and period projections;
6. closed digest if a boundary is due;
7. Field Map only if the map gate passes;
8. atomic commit history; never create a public operational or daily-run file.

Discovery, identity resolution, scope judgment, full-text reading, skeptical audit, canonical update, and Timeline projection form one validated transaction. Candidate state that has not crossed the publication gate remains in `.radar-private/runs/<run_id>.json` or agent memory; it is not public inventory.

The v2 canonical adapter is all-or-none. Once any of `published_at`, `first_seen_at`, `radar_published_at`, `time_provenance`, or `map_delta` is present, the record carries the complete explicit-legacy or native-v2 bundle. Native timestamps are strict UTC and ordered `published_at <= first_seen_at <= radar_published_at`; explicit legacy preserves `published_at=published`, null discovery/Radar times, and `time_provenance=legacy_unknown`. A native-v2 record used as rolling-period support also declares `direction_keys`, a non-empty list of unique lowercase stable tokens. `direction_keys` itself requires the complete native-v2 bundle; explicit and implicit legacy records never carry it.

## Timeline, periods, and map

The root projection order is:

`Latest Timeline → 7-day / 30-day Changes → Field Map → Reading Paths → Research Library`

Place one Last updated / Last synthesized status directly after depth navigation and immediately before Timeline, which remains the first substantive feed. Timeline has no fixed count cap. Include every native-v2 acceptance whose `radar_published_at` is in the current 30-day window and no later than the exact public synthesis cutoff shared with both rolling periods, ordered by the full timestamp; legacy compatibility entries with unknown Radar acceptance time stay under the migration notice and retain honest paper-date order. Each `entry-*` has one compact `<details>` summary with date, short canonical label, exact canonical Field Map axis prefix (use `axis → subproblem` only when needed), and delta. Its expanded Links field uses the complete canonical title for the primary-paper link. Both README languages keep those surfaces paired and link both local deep notes.

Keep navigation and list surfaces direct and compact. Do not add a methodology manifesto, prose that merely restates an adjacent table, or redundant wrappers around the required Timeline fields. Let the collapsed summary name the mechanism or limitation directly; the expanded body carries the audit detail.

Each rolling period states exactly one visible inclusive window and the exact UTC synthesis timestamp shared with the Timeline cutoff. The synthesizer re-reads canonical JSON and deep notes inside each window; weekly prose is never summarized into monthly prose. Each direction block owns exactly one stable metadata comment and exactly one visible state, ordered canonical supports field, `low | medium | high` confidence, `radar_published_at` timing basis, exact UTC synthesis field, research-design implication witness, and prior-map field. Every cited support under direction key `K` must carry exact `K` in canonical `direction_keys`; prose grouping alone is not binding. A one-record direction can only be an `early_signal`-backed `new_signal`; `reinforced` needs two distinct in-window native supports bound to the block key plus independent prior Field Map evidence; `no_material_change` has zero support and `prior=none`. A single work is never a trend.

Use `radar_published_at` alone for rolling support and reject records accepted after the exact synthesis cutoff. Legacy records remain useful Field Map context but are **not rolling support** when their Radar acceptance time is unknown.

Every accepted v2 record receives one `map_delta`:

`none | early_signal | reinforces | revises | splits | retires`

`early_signal` may change Timeline/period synthesis but not a durable map node. Durable changes require independent evidence and the smallest reversible edit with the prior claim named.

On the first successful run after Monday 00:00 local time, ensure an immutable digest for the previous complete ISO week. On the first successful run of a new month, ensure one for the previous complete calendar month. Boundary identities are idempotent. Separate weekly/monthly writers remain disabled.

## Bilingual and visual atomicity

Chinese and English are projections of one judgment. Identity, date/order, evidence scope, decisive result, caveat, map token, period windows, and primary/local links must remain paired. Semantic contract comments carry shared judgment keys; visible witness phrases keep decisive evidence and caveats load-bearing.

Visual generation remains isolated per paper and follows `VISUALS.md`. A pending or invalid visual never leaks its internal status to Timeline. A visual cannot raise a paper's publication ceiling.

## Publication and validation

Immediately before publication, recheck remote head. If it moved, abort the write transaction, re-read affected canonical state, re-render, revalidate, and retry once; never force-push. Commit all material canonical, bilingual, digest, and map changes atomically. Do not create a file under `runs/daily/` or any other public operational-run path; validator-enforced absence replaces natural-language leakage checks.

Run:

```bash
python -m unittest discover -s tests -v
python scripts/build_paper_index.py
python scripts/build_paper_index.py --check
python scripts/validate.py
python scripts/validate_reading.py
python scripts/validate_public.py
git diff --check
```

Any identity ambiguity, unavailable full text, bilingual drift, unresolved local link, stale generated index, invalid time/map semantics, or validator failure aborts publication. If no material research change exists, validate and exit silently without a content commit or notification.
