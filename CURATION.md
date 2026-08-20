# Agentic RAG Curation Contract

This repository is maintained by the scheduled Daily Agent as a research radar, not a keyword dump or a human PR backlog. [`docs/RADAR_AGENT_PROTOCOL.md`](docs/RADAR_AGENT_PROTOCOL.md) controls orchestration; [`docs/DAILY_WORKFLOW.md`](docs/DAILY_WORKFLOW.md) is the RAG adapter. The orchestrator is the only writer and publishes no candidate queue.

## Acceptance gate

Discovery optimizes recall across overlapping source lanes. Publication requires identity resolution, in-scope judgment, primary full-text evidence, skeptical audit, canonical update, and bilingual projection in one transaction.

Ask:

1. Is external information acquisition substantive?
2. Does the agent/controller materially control whether, what, where, how, or how much is acquired?
3. Is that control a research contribution rather than glue?
4. Is the smallest delta identifiable against the closest static, adaptive, and historical design point?

If 1–3 are not clearly yes, do not publish. Ordinary fixed RAG, generic tool use, and agent papers without a retrieval/interface/state contribution stay out. A relevant work may still be low importance.

`BLOCKED`, `DEFERRED`, rejected, duplicate, and abstract-only candidates remain private. Lack of full text or decisive evidence is a retry condition, not a reader-facing status.

## Evidence and attribution

Every accepted record preserves the actual information loop, closest meaningful comparison, decisive evidence, negative result, realized cost, and strongest alternative explanation. Interpret gains through:

`evidence coverage × corpus observability × interface resolution × environment state × harness/delivery × agent state × policy × realized resources × base model × training protocol × historical baseline`

- Evidence validity precedes policy quality.
- Adaptivity has a location; round count is not a capability metric.
- Match backend, surfaced depth, admissible candidates, read/navigation affordances, state, harness, and delivery before crediting policy.
- Account for offline construction/update plus online calls, tokens, latency, controller/probe compute, and model calls.
- Separate reward/credit assignment from tool format, corpus coverage, rollout freshness, teacher information, and budget.

An abstract cannot support superiority. Author claims remain claims. A benchmark failure diagnoses the evaluated trajectory; it does not by itself identify the controller that would repair it.

## Canonical and time contract

Canonical JSON lives under `data/papers/`; paired deep notes live at `papers/<identity>.md` and `papers/<identity>.zh.md`. The v2 time/map contract is all-or-none: once one of `published_at`, `first_seen_at`, `radar_published_at`, `time_provenance`, or `map_delta` appears, the complete explicit-legacy or native-v2 bundle is required. Native-v2 accepted records use three distinct strict-UTC times ordered `published_at <= first_seen_at <= radar_published_at`, plus `time_provenance=native_v2`, `map_delta`, and `provenance.full_text_checked=true`. The fixed compatibility set alone uses honest `published_at=published`, null discovery/Radar times, and `legacy_unknown`; never manufacture legacy Radar acceptance times.

A native-v2 record cited by a rolling direction also carries `direction_keys`, a non-empty list of unique lowercase stable tokens containing the exact block key. This field itself requires the complete native-v2 bundle. Unsupported native records may omit it; explicit and implicit legacy records never carry it, so do not fabricate current support or bulk-migrate legacy records.

Every accepted record receives one map status:

`none | early_signal | reinforces | revises | splits | retires`

One paper can be `early_signal`; it cannot create a trend or silently rewrite a stable map. `reinforces` requires independent evidence. `revises`, `splits`, and `retires` name the old claim, new evidence, and smallest reversible edit.

## Reader projection

The root order is Timeline, exact 7-day/30-day changes, Field Map, Reading Paths, then Library. Timeline has no fixed cap: include every native-v2 acceptance in the current 30-day window whose `radar_published_at` is no later than the exact public synthesis cutoff shared by Timeline and both rolling periods, ordered by full timestamp, then the fixed legacy compatibility set. Its closed summaries are the complete current scan layer; each open body is a 60–90 second evidence-and-caveat layer; deep notes remain the audit layer.

Each period has exactly one visible inclusive window and the exact UTC synthesis timestamp shared with the Timeline cutoff. Every direction binds one metadata block to exactly one visible state, ordered canonical supports field, confidence enum, Radar timing basis, exact synthesis field, implication witness, and prior-map field. Every support under key `K` must include `K` in canonical `direction_keys`; same prose placement is not a shared direction. It re-reads canonical records and notes inside the exact window. Monthly claims are never produced by summarizing weekly prose.

Rolling support is determined only by `radar_published_at` and the exact synthesis cutoff. Legacy paper dates may inform the Field Map but are **not rolling support** when Radar acceptance time is unknown.

Chinese and English share identity, date/order, evidence scope, result, caveat, map status, and primary/local links. A correction updates both in one transaction.

## Visual and scoring policy

Visuals follow `VISUALS.md`. They teach one grounded mechanism and remain isolated from the main transaction until QC passes. Pending or invalid rendering state is internal and never appears on the public reader surface.

`relevance ∈ [0,1]` measures topical fit. `importance ∈ {1,...,5}` measures expected research significance:

- **5 — Field-shaping:** unusually strong evidence changes an abstraction, benchmark, or durable direction.
- **4 — Important:** a reusable idea or evidence base likely to shape follow-up work.
- **3 — Solid:** a meaningful but narrower delta or evidence contribution.
- **2 — Incremental:** valid with limited novelty, evidence, or scope.
- **1 — Peripheral:** retained only when useful for completeness.

Do not reward recency, author reputation, or fashionable naming.

## Atomic update

For a material run, update canonical JSON, paired notes, relationships, safe visual state, Timeline/period projections, due closed digests, and gated map edits; validate; then publish one commit. Commit history is the operational provenance. Never create a public daily-run or operational-log file; private run evidence stays under ignored `.radar-private/`. On no material change, validate and exit silently.

See [`COMPACTION.md`](COMPACTION.md), [`VISUALS.md`](VISUALS.md), and [`runs/README.md`](runs/README.md).
