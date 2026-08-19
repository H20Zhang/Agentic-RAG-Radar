# Reader Experience and Maintenance Workflow — Implementation Plan

This plan implements the approved design in `../specs/2026-08-19-reader-experience-and-workflow-design.md`.

## Commit 1 — Repair reader/visual contracts

Align `templates/paper.md`, `assets/visuals/README.md`, `docs/MAINTENANCE.md`, and the public digest archive language with the live dual-asset visual contract and current reader vocabulary.

## Commit 2 — Add the Curated Paper Index

Add deterministic `scripts/build_paper_index.py`, generate `papers/README.md`, and wire the root README/research-map navigation to the index. The index is derived only from canonical JSON.

## Commit 3 — Add public-surface validation

Add `scripts/validate_public.py`, connect it to CI together with the existing schema/visual validator and index drift check, then fix reader-facing drift surfaced by those checks.

## Commit 4 — Align the research surfaces

Normalize category navigation and research-map language, update `papers/anchors.md`, and re-ground the rolling 2026 synthesis through W34 around materialization placement, progress observability, recoverability, and lifecycle work.

## Commit 5 — Make the daily workflow the scheduler contract

Add `docs/DAILY_WORKFLOW.md` and update the single recurring automation to weekdays at 09:20 Asia/Shanghai with a short orchestration prompt. Keep compaction conditional and isolate per-paper visual generation from the long maintenance context.

## Verification

Before finishing, require:

```bash
python scripts/build_paper_index.py --check
python scripts/validate.py
python scripts/validate_public.py
```

Also verify that the single recurring automation is enabled, weekday-only, exact-scheduled, and points to `docs/DAILY_WORKFLOW.md`.
