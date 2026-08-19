# Daily Research-Maintenance Workflow

This is the orchestration contract for the single recurring maintenance task that keeps Agentic RAG Radar current and internally consistent.

Deep domain rules remain authoritative in [`../CURATION.md`](../CURATION.md), [`../COMPACTION.md`](../COMPACTION.md), [`../VISUALS.md`](../VISUALS.md), [`../taxonomy.yaml`](../taxonomy.yaml), and the structured paper schema. This file defines **execution order and gates** so the scheduler prompt can stay short and stable.

## Principle

One run is one idempotent maintenance transaction:

`self-heal → discover → judge → update canonical truth → derive reader surfaces → optionally synthesize/visualize → validate → log → notify only if material`

Do not create work merely because a scheduled run occurred. An empty discovery day is a successful run when the repository remains correct.

## Phase 1 — Preflight and self-heal

Before discovery, read the public and maintenance contracts, relevant category/paper/digest surfaces, and recent daily logs.

Check deterministic and reader-facing consistency first:

```bash
python scripts/build_paper_index.py --check
python scripts/validate.py
python scripts/validate_public.py
```

If drift exists, repair it before adding new papers. Reader-surface drift is a correctness problem, not cosmetic cleanup.

## Phase 2 — Overlapping discovery and independent judgment

Search high-signal scholarly sources beyond the literal phrase `agentic RAG`, including adaptive/active retrieval, retrieval planning, iterative/interleaved search, query reformulation/decomposition, verifier-guided retrieval, tool-using RAG, GraphRAG agents, retrieval policy/RL, search agents, and agentic information seeking.

Use an overlapping window rather than a strict day boundary:

- **Monday:** approximately 96 hours, absorbing weekend publications and source-index lag;
- **Tuesday–Friday:** approximately 48 hours.

When independent roles/subtasks are supported, discovery, inclusion/taxonomy, research reading, and skeptical evidence review should form judgments independently before synthesis.

Do not accept a paper to keep the feed busy. Inclusion still requires substantive external information acquisition **and** meaningful agent/controller/policy control over whether, what, where, how, or how much to retrieve.

## Phase 3 — Canonical-first publication

For every accepted paper, update in this order:

```text
canonical JSON
→ researcher-facing paper note
→ grounded visual brief + accurate visual status
→ primary category page
→ Latest Papers / Reading Paths only when reader value warrants it
→ regenerate Curated Paper Index
```

`data/papers/*.json` is canonical. `papers/README.md` is generated and must never be hand-edited.

Keep relevance separate from importance. Preserve negative results, matched-baseline weaknesses, resource mismatches, historical predecessors, and the strongest alternative explanation.

## Phase 4 — Visual isolation

Per-paper image generation must be isolated from the long repository-maintenance context.

Each image-generation invocation receives only:

1. the named paper's grounded research note;
2. its grounded visual brief;
3. the visual contract in `VISUALS.md`.

Generate exactly one named paper per invocation. Do not pass the whole daily-maintenance prompt into the image context; this is a deliberate guard against repository-dashboard or multi-paper drift.

A visual is complete only after the PNG master and same-resolution WebP pass QC, are committed, and required paper/README explanations are synchronized. Failed generation remains internal status and must not leak onto the public README.

## Phase 5 — Compaction gate

Weekly/monthly/yearly synthesis is **conditional**, not a daily side effect.

Update a compaction only when at least one is true:

- a newly accepted paper changes a thesis, tension, anchor, or evidence bar;
- a meaningful correction/reclassification changes prior interpretation;
- a week/month/year boundary requires a new rolling or finalized artifact;
- stale synthesis is discovered during preflight.

When synthesis changes, re-ground load-bearing claims in canonical paper records/full-text notes rather than recursively summarizing older digests.

Prefer one important tension over several weak trends.

## Phase 6 — Derive and validate

After canonical/research edits:

```bash
python scripts/build_paper_index.py
python scripts/build_paper_index.py --check
python scripts/validate.py
python scripts/validate_public.py
```

All three validation surfaces must agree before the run is considered complete:

- generated Curated Paper Index;
- canonical schema/visual contract;
- public reader surfaces and links.

Do not claim successful CI unless the check is actually observable.

## Phase 7 — Compact archival log

Write one compact log at:

```text
runs/daily/YYYY/MM/DD.md
```

Record only material discovery decisions, accepted/deferred/rejected edge cases, meaningful corrections, visual outcomes/blockers, compaction actions, and validation status. Do not duplicate paper notes or digest prose.

## Notification gate

Notify the user only for:

- a newly accepted paper;
- a meaningful correction or reclassification;
- a meaningful weekly/monthly/yearly synthesis change;
- successful meaningful visual repair/backfill;
- an exact workflow blocker requiring attention.

Otherwise finish silently.

## Scheduled cadence

The recurring task runs **Monday–Friday at 09:20 Asia/Shanghai** as one exact-scheduled transaction.

Weekends have no routine maintenance run. Monday's wider overlap absorbs weekend publications and indexing lag. This avoids empty weekend work while keeping a single writer responsible for discovery, canonical updates, derived surfaces, synthesis gates, and validation.

Do not split discovery, visuals, compaction, and validation into competing scheduled writers unless the repository architecture is deliberately redesigned for transactional concurrency.
