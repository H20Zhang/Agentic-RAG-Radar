# Maintainer Guide

This page collects repository-maintenance details that are intentionally kept out of the audience-facing README.

## Source of truth

- `data/papers/*.json` — canonical structured paper records.
- `papers/*.md` — researcher-facing paper notes derived from the records and source reading.
- `papers/README.md` — deterministic Curated Paper Index generated from canonical records.
- `categories/*.md` — Agent-edited research-problem views derived from accepted evidence.
- `assets/visuals/` — generated conceptual explainers and their grounding briefs.
- `digests/weekly/`, `digests/monthly/`, and `digests/yearly/` — higher-level research synthesis.
- Git commit history — atomic publication and correction provenance. Public Daily Agent run logs are forbidden; operational state stays in ignored `.radar-private/` artifacts.

## Public reader model

The root `README.md` is the primary reader-facing research surface. Its substantive order is:

1. **Latest Timeline** — every currently projected accepted record in compact scan/expand form;
2. **7-day / 30-day Changes** — exact-window direction changes with evidence and confidence;
3. **Field Map** — durable, evidence-gated problem and design structure;
4. **Reading Paths** — how to learn a research question efficiently;
5. **Research Library** — complete chronology and alternate problem/category routes.

Operational details such as scheduling, generation mechanics, validation rules, visual backfill state, internal prompts, and run provenance must stay out of the public README.

They must also stay out of standalone public run files. Validation rejects any file under `runs/daily/`; accepted outcomes are represented only in canonical/derived research surfaces and commit history.

## Maintenance contracts

- [`../CURATION.md`](../CURATION.md) — inclusion, independent review, evidence, and skeptical-QC rules.
- [`../COMPACTION.md`](../COMPACTION.md) — weekly/monthly/yearly synthesis and anti-summary-drift rules.
- [`../VISUALS.md`](../VISUALS.md) — visual explainer grounding, dual-asset, and reader-explanation requirements.
- [`../taxonomy.yaml`](../taxonomy.yaml) — controlled research taxonomy and orthogonal tags.
- [`../data/paper.schema.json`](../data/paper.schema.json) — structured paper-record schema.
- [`DAILY_WORKFLOW.md`](DAILY_WORKFLOW.md) — orchestration contract for the recurring maintenance transaction once present.

## Generate repetition; validate judgment

Deterministic surfaces should be generated from canonical data when possible. Research judgment remains an explicit Agent editorial act after full-text and skeptical review; it is never inferred from counts or metadata.

Generated/derived:

- Curated Paper Index.

Agent-edited but validated:

- README theses and Reading Paths;
- category Current signal / Current tension / Next decisive evidence;
- paper research notes;
- weekly/monthly/yearly synthesis.

Do not auto-generate a field thesis or category conclusion from metadata merely to reduce maintenance work.

## Validation

Before completing a maintenance run:

1. check the generated paper index against canonical records;
2. validate canonical records and visual assets;
3. validate public surface order, links, canonical/deep-note synchronization, and Timeline disclosures;
4. correct upstream/downstream research synthesis when a material paper correction changes the conclusion.

Reader-facing link failures and synchronization drift are correctness problems, not cosmetic cleanup.
