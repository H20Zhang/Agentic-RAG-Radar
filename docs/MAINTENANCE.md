# Maintainer Guide

This page collects repository-maintenance details that are intentionally kept out of the audience-facing README.

## Source of truth

- `data/papers/*.json` — canonical structured paper records.
- `papers/*.md` — researcher-facing paper notes derived from the records and source reading.
- `assets/visuals/` — generated conceptual explainers and their grounding briefs.
- `digests/weekly/` and `digests/monthly/` — higher-level research compactions.
- `runs/daily/` — compact archival provenance for each maintenance run.

## Maintenance contracts

- [`../CURATION.md`](../CURATION.md) — inclusion, multi-role review, evidence and QC rules.
- [`../COMPACTION.md`](../COMPACTION.md) — weekly/monthly synthesis and anti-summary-drift rules.
- [`../VISUALS.md`](../VISUALS.md) — GPT-image-gen visual explainer protocol and grounding requirements.
- [`../taxonomy.yaml`](../taxonomy.yaml) — controlled research taxonomy and orthogonal tags.
- [`../data/paper.schema.json`](../data/paper.schema.json) — structured paper-record schema.

## Editorial separation

The root `README.md` is a public research landing page. It should answer:

1. What changed recently?
2. Which papers are worth reading?
3. How is the field currently organized?
4. Where should a researcher start?

Operational details such as scheduling, file-generation rules, schema mechanics, backfill queues, and agent-role instructions belong here or in the maintenance contracts above, not in the public README.

## Validation

Before completing a maintenance run, check that structured records remain compatible with the schema and that reader-facing links do not point to nonexistent paper notes or visual assets. Corrections should propagate upward when they materially change a weekly/monthly synthesis.
