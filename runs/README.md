# Curation Run Archive

This directory stores **archival provenance**, not the primary reading interface.

Daily maintenance logs are nested by date:

```text
runs/daily/YYYY/MM/DD.md
```

A daily log records what the curator actually did: discovery window, accepted papers, deferred/rejected edge cases, meaningful corrections, visual backfill status, and whether compaction changed. It should remain compact and auditable.

## Why keep daily logs?

Canonical paper records tell us the current truth; run logs preserve **decision history**:

- when a paper was first noticed or accepted;
- why a borderline paper was held out;
- when a classification/evidence interpretation changed;
- whether visual generation failed or was deferred;
- which weekly/monthly compaction was triggered by the run.

This is useful for debugging the curator without forcing readers to browse hundreds of daily files.

## Reading hierarchy

- **Primary:** [`../README.md`](../README.md) + [`../digests/`](../digests/) — current research map and compactions.
- **Paper detail:** [`../papers/`](../papers/) + [`../data/papers/`](../data/papers/) — researcher notes and canonical records.
- **Archive:** `runs/daily/` — raw curation provenance only.

Daily logs should never become a second paper database or repeat long research notes.