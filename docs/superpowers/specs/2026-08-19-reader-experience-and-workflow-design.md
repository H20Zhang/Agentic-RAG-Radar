# Reader Experience and Maintenance Workflow Design

## Goal

Make Agentic RAG Radar easier to use as a research artifact while reducing synchronization drift across public surfaces.

The target reader journey is:

`latest work -> field movement -> reading path -> research map -> complete curated index -> paper-level evidence`

The target maintenance model is:

`canonical records -> deterministic derived indexes + validated human-edited synthesis`

The repository should remain a skeptical living survey, not become a dashboard, generated website, or exhaustive keyword feed.

## Non-goals

- Do not replace the root README with generated content.
- Do not auto-generate research theses, reading paths, category tensions, or compactions from metadata.
- Do not add GitHub Pages, a frontend/search UI, visitor counters, star-count badges, or decorative banners.
- Do not claim complete historical coverage where curation is incomplete.
- Do not widen the inclusion policy merely to make the paper index look comprehensive.
- Do not expose scheduler mechanics, backfill queues, prompt internals, or provenance logs on public reader surfaces.

## 1. Reader information architecture

The root README remains the primary landing page. Its substantive reading order stays:

1. **Latest Papers** — the newest important accepted papers and their skeptical 60-second folds.
2. **What's Changing** — weekly/monthly/yearly field movement and the current synthesis.
3. **Reading Paths** — minimal sequences for learning a research question rather than replaying chronology.
4. **Research Map** — durable anchors plus problem-oriented field structure.

Add a fifth destination to navigation, but not another large homepage section:

5. **Curated Paper Index** — a complete index of papers accepted by this radar.

Use the public name **Curated Paper Index**, not “All Papers,” because the repository is intentionally selective and does not claim exhaustive coverage of all Agentic RAG literature.

The index lives at:

```text
papers/README.md
```

README should link to it from the top navigation and from the end of Research Map.

## 2. Curated Paper Index

`papers/README.md` is generated deterministically from `data/papers/*.json`.

It serves four research use cases:

- find a paper already curated by the radar;
- scan recent accepted work without the richer homepage folds;
- browse the archive by year/month;
- jump from chronology to research-problem pages.

The page begins with links to the six research-problem categories, followed by chronology.

### Chronology

Current year:

- group papers by publication month;
- show newest month first;
- show newest paper first within each month.

Historical years:

- show year headings in descending order;
- use compact sections to avoid turning the page into a long unstructured feed.

### Paper row

Each paper entry should expose only canonical reader-useful fields:

```text
Published date · title · category · importance
Research delta
Evidence basis
Paper · Research note · Code/Project when verified
```

`Research delta` comes from `visual_explainer.takeaway`, because that field already stores the smallest grounded design change the radar wants to teach.

`Evidence basis` is derived from provenance:

- `full-text reviewed` when `provenance.full_text_checked == true`;
- `abstract-level` otherwise.

Do not expose internal visual status, discovery source, pending work, or schema metadata.

## 3. Deterministic generation boundary

Add:

```text
scripts/build_paper_index.py
```

The script reads canonical paper JSON and writes `papers/README.md`.

Supported modes:

```bash
python scripts/build_paper_index.py
python scripts/build_paper_index.py --check
```

`--check` renders expected output in memory and fails when the committed index differs.

The script must be deterministic:

- no network calls;
- no LLM-generated prose;
- stable sorting;
- stable category labels from `taxonomy.yaml` or an equivalent single source of truth;
- no timestamps that cause meaningless diffs.

Human-edited research surfaces remain human-edited:

- root README theses and reading paths;
- category tensions and decisive evidence;
- paper research notes;
- weekly/monthly/yearly synthesis.

The design principle is:

> Generate repetition; validate judgment.

## 4. Public-surface validator

Add:

```text
scripts/validate_public.py
```

This complements, rather than replaces, `scripts/validate.py`.

### Root README checks

Validate that:

- the first substantive H2 is `Latest Papers`;
- section order is `Latest Papers -> What's Changing -> Reading Paths -> Research Map`;
- top navigation links resolve to those sections and to `papers/README.md`;
- every paper visible in Latest Papers has a canonical record and paper note;
- Latest Papers are in non-increasing publication-date order;
- every Latest paper has exactly one `Understand this paper in 60 seconds` fold;
- each fold includes Problem, Core mechanism, Compared with, Evidence to remember, and Open question;
- method papers with a meaningful loop include Agent loop/control flow;
- if a Latest paper has `visual_explainer.status == generated`, its WebP and figure-reading explanation are embedded before Problem;
- README does not expose internal statuses such as `pending`, `needs_regeneration`, backfill, renderer failure, or scheduler mechanics.

### Paper-note checks

Every accepted paper note should contain:

- TL;DR;
- Problem;
- Core idea;
- Agent loop/control flow where applicable;
- Retrieval design;
- Compared to what;
- Evidence;
- Why it matters;
- Limitations/questions.

Generated visuals must continue to satisfy the existing master/WebP contract and reader explanation rules.

### Category checks

For each canonical paper:

- its primary category page exists;
- that category page links to the paper note.

Each category page should expose a consistent research-facing skeleton:

- Core question;
- Current signal or current design anchors;
- Current tension;
- What would count as meaningful progress / Next decisive evidence;
- navigation back to Research Map and Curated Paper Index.

The validator should not require identical prose structure where a sparse category benefits from a shorter page.

### Link checks

Validate repository-relative Markdown links on public surfaces, at minimum:

- `README.md`;
- `papers/README.md`;
- `papers/*.md`;
- `categories/*.md`;
- `digests/README.md` and current primary weekly/monthly/yearly reports;
- `CONTRIBUTING.md`.

Only validate local repository paths; external URLs are not re-fetched in CI.

### Drift checks

Fail when:

- `papers/README.md` is stale relative to canonical JSON;
- old primary public names such as `Start Here` or root-level `Research Compactions` reappear;
- paper template or visual-directory documentation contradicts the active visual contract.

## 5. Research-surface consistency pass

### README

Keep the current reader order and skeptical density.

Add `Curated Paper Index` to the compact top navigation and one link after the Research Map.

Do not add another large homepage table duplicating the index.

Review the bottom sections for duplicated explanation. Keep only reader-useful material:

- how to interpret paper cards;
- inclusion boundary;
- why the radar is different from a keyword feed;
- contribution entry point.

Maintenance details remain collapsed or moved to maintainer docs.

### Categories

`categories/README.md` becomes the canonical **Research Map** landing page rather than “Browse Agentic RAG by Research Problem.”

It should open with the current field-level decomposition and let readers choose one research problem quickly.

Individual category pages should converge on a common reader contract:

```text
Core question
Current signal / anchors
Current tension
Next decisive evidence
Paper details / boundaries
Navigation
```

Do not force empty or sparse categories to imitate dense categories.

### Digests

Rename the public archive language from **Research Compactions** to **What's Changing** or **Research Synthesis Archive** depending on context.

`digests/README.md` should no longer say “Start here.” It should explain that this is the historical synthesis archive behind the homepage What's Changing section.

Weekly/monthly/yearly filenames and internal protocol terminology may remain unchanged; the public vocabulary should be reader-facing.

### Yearly map

Re-ground the rolling 2026 map through current W34 evidence.

It must incorporate the newer durable distinction:

`precompute/materialize/retain <-> defer/localize/reacquire`

and explicitly include:

- evidence-materialization placement;
- progress observability;
- state recoverability/reacquisition cost;
- lifecycle accounting across offline and online work.

Do not merely append W34 paragraphs; rewrite the year-level abstraction where necessary.

### Anchors

Update `papers/anchors.md` so it matches the current field map, including materialization placement and recoverability rather than stopping at the older adaptivity-placement framing.

## 6. Template and documentation repair

The current `templates/paper.md` and `assets/visuals/README.md` predate the dual-asset visual contract and must be repaired.

### Paper template

The template should:

- use the canonical WebP delivery path rather than a single PNG;
- support the PNG master path in metadata/documentation rather than embedding it;
- require `How to read this figure`, `Compared with`, and `Do not over-read` beneath a generated visual;
- keep public notes understandable when the visual is not generated;
- use current paper-section names matching validation.

### Visual directory README

Update the documented asset contract to:

```text
assets/visuals/masters/<id>.png
assets/visuals/<id>.webp
assets/visuals/prompts/<id>.md
```

and align status semantics with `VISUALS.md` and `scripts/validate.py`.

### Maintainer documentation

Update `docs/MAINTENANCE.md` so its public-surface model matches the final information architecture:

- Latest Papers;
- What's Changing;
- Reading Paths;
- Research Map;
- Curated Paper Index.

## 7. CI contract

Update `.github/workflows/validate.yml` to run:

```bash
python scripts/build_paper_index.py --check
python scripts/validate.py
python scripts/validate_public.py
```

Install only dependencies actually required.

The public validator should produce actionable failures with file/path/context rather than one generic error.

CI should not fetch external websites or depend on volatile network state.

## 8. Daily workflow contract

Add:

```text
docs/DAILY_WORKFLOW.md
```

This file becomes the operational entry point for the recurring research-maintenance task. Existing deep contracts remain authoritative for their domains; DAILY_WORKFLOW orchestrates them instead of duplicating every detail into the scheduler prompt.

### Run phases

#### Phase 1 — Preflight and self-heal

Read the public/maintenance contracts and recent run logs, then execute or reason through:

```text
build_paper_index --check
validate.py
validate_public.py
```

Fix deterministic/public-surface drift before adding new papers.

#### Phase 2 — Discovery and independent judgment

Use overlapping scholarly search windows and independent discovery/inclusion/reader/skeptic judgments when supported.

Recommended overlap:

- Monday: approximately 96 hours to absorb the weekend and source-index lag;
- Tuesday-Friday: approximately 48 hours.

Do not accept papers merely to make every run non-empty.

#### Phase 3 — Canonical-first publication

For accepted papers, update in order:

```text
canonical JSON -> paper note -> grounded visual brief/status -> category -> Latest/Reading Paths if materially warranted -> generated Curated Paper Index
```

The index is never hand-edited.

#### Phase 4 — Visual isolation

Per-paper image generation must run in an isolated task/context containing only:

- the named paper's grounded note;
- its visual brief;
- the visual contract.

Do not feed the entire repository-maintenance prompt into the image-generation context. This directly addresses prior repository-dashboard drift.

Each invocation generates exactly one named paper visual.

#### Phase 5 — Compaction gate

Do not rewrite weekly/monthly/yearly synthesis merely because a daily run occurred.

Update a compaction only when:

- a new paper changes a thesis/tension/evidence bar;
- a meaningful correction changes prior interpretation;
- a time boundary requires a new rolling/final artifact.

Weekly/monthly/yearly remain research products, not scheduler side effects.

#### Phase 6 — Validation, log, notification

Regenerate the index, run all validators, then write one compact daily log.

Notify the user only for:

- newly accepted paper;
- meaningful correction/reclassification;
- meaningful synthesis change;
- successful meaningful visual repair/backfill;
- exact blocker.

Silent success remains the default.

## 9. Scheduled task design

Keep **one** recurring automation rather than splitting discovery, compaction, visuals, and validation into independent schedulers. One task preserves a single canonical maintenance transaction and prevents overlapping writes.

### Schedule

Use:

- **Monday-Friday**;
- **09:20 Asia/Shanghai**;
- exact schedule.

Rationale: the run should happen after the normal overnight scholarly update window while remaining early enough for a morning research brief. Weekends do not need routine empty maintenance runs; Monday's larger overlap absorbs weekend publications/index lag.

### Scheduler prompt

The scheduler prompt should be short and stable:

> Maintain H20Zhang/Agentic-RAG-Radar according to docs/DAILY_WORKFLOW.md and the repository contracts it references. Execute one complete idempotent maintenance transaction: preflight/self-heal, overlapping discovery and skeptical curation, canonical-first updates, isolated per-paper visual work when possible, conditional compaction, generated paper-index refresh, validation, compact run log, and notify only for material changes or exact blockers.

Do not duplicate CURATION/COMPACTION/VISUALS/schema details in the automation prompt. Keeping those rules in versioned repository docs allows the workflow to evolve without scheduler-prompt drift.

## 10. Implementation sequence

Use small auditable commits to main where reliable.

### Commit group 1 — Repair contracts

- `templates/paper.md`;
- `assets/visuals/README.md`;
- `docs/MAINTENANCE.md`;
- public digest naming cleanup where purely terminological.

### Commit group 2 — Curated Paper Index

- `scripts/build_paper_index.py`;
- generated `papers/README.md`;
- README/category navigation to the index.

### Commit group 3 — Public validator + CI

- `scripts/validate_public.py`;
- workflow integration;
- fix public-surface issues surfaced by the validator.

### Commit group 4 — Research surface alignment

- `categories/README.md` and relevant category-page structure/navigation;
- `digests/README.md`;
- `papers/anchors.md`;
- re-grounded rolling 2026 yearly map;
- README bottom-section cleanup if still needed.

### Commit group 5 — Daily workflow + automation

- `docs/DAILY_WORKFLOW.md`;
- update the single recurring automation to weekdays at 09:20 Asia/Shanghai with the short orchestration prompt.

## 11. Success criteria

The redesign is complete when:

- a returning reader reaches Latest Papers immediately;
- a researcher can move directly from a new paper to current field movement, a reading path, a research problem, or the full curated index;
- every accepted canonical paper is discoverable from the Curated Paper Index and its primary category;
- the index cannot silently drift from canonical data;
- README/category/note/public-link drift is caught by CI;
- paper/visual templates match the live dual-asset contract;
- the rolling yearly map reflects current durable evidence rather than an older monthly snapshot;
- the daily task is one idempotent transaction with deterministic preflight and conditional synthesis;
- image generation is isolated from long repository-maintenance context;
- scheduler rules live primarily in versioned repository documentation rather than a giant automation prompt.
