# Visual Quality and README Reading Order Design

## Goal

Make paper visuals genuinely useful at research-reading scale and make the public README optimize first for discovering the newest important papers.

This change has two coupled reader-facing goals:

1. visual explainers remain crisp when embedded in README and paper pages, and each visual is immediately interpretable without opening internal notes;
2. README presents **Latest Papers** before compactions so a returning researcher can first answer “what is new and worth reading?” before moving into field synthesis.

Non-goals: redesigning the taxonomy, changing paper inclusion criteria, adding decorative repo graphics, or exposing maintenance mechanics on the public README.

## 1. Dual visual assets

Every generated paper visual uses two assets:

- `assets/visuals/masters/<paper-id>.png` — canonical lossless/high-quality master produced from the accepted single-paper render;
- `assets/visuals/<paper-id>.webp` — web delivery asset used by README and paper pages.

The WebP must preserve the master pixel dimensions. Compression must not resize the image. The normal target is at least **1536 px wide** with visually lossless/high-quality WebP encoding (approximately quality 95 when lossy encoding is used).

Existing low-resolution visuals must not be upscaled and treated as repaired. If the committed asset is materially below the minimum or lacks a usable master, regenerate the paper visual from its grounded visual brief, then derive the WebP from the accepted master.

## 2. Structured visual explanation

A visual is not considered reader-complete merely because an image is embedded.

For every generated visual, the paper page should contain a compact explanation immediately after the image covering:

- **How to read this figure** — 2–3 paper-specific sentences explaining the visual regions/flow and the intended research delta;
- **Compared with** — the nearest baseline/design point shown or implied by the visual;
- **Do not over-read** — the strongest caveat, confound, or unsupported causal interpretation the figure must not imply.

The README 60-second fold for papers currently visible in **Latest Papers** must include the same reader-facing “How to read this figure” explanation immediately after the image, before Problem/Core mechanism. It should be concise enough to preserve the 60-second reading goal.

Generated-image text remains intentionally sparse (roughly 3–7 short labels). Precision, caveats, benchmark evidence, and causal qualification belong in Markdown rather than inside the image.

## 3. Canonical metadata and validation

Extend `visual_explainer` metadata with a canonical master asset path while keeping `image_path` as the web-facing asset path:

- `master_image_path`: `assets/visuals/masters/<paper-id>.png` for generated visuals;
- `image_path`: `assets/visuals/<paper-id>.webp` for generated visuals.

For `status == generated`, validation must check more than file existence:

- both master PNG and display WebP exist;
- the display WebP is at least 1536 px wide;
- the display WebP has the same pixel dimensions as the master, preventing accidental thumbnail/downsample conversion;
- both paths are repository-relative and consistent with the record.

Pending/regeneration states may retain intended paths without claiming that an asset is visible.

## 4. Existing visual self-heal

Audit all records with `visual_explainer.status == generated`.

A visual enters regeneration if any of the following is true: missing master PNG, display asset below the minimum width, display dimensions differ from the master, or the paper/README reader explanation is missing where required.

Prioritize currently visible Latest Papers first, then remaining generated visuals, then normal pending visual backfill. Each regeneration remains one named paper per GPT-image invocation and must pass the existing skeptical visual QC before commit.

Do not generate synthesis/compaction graphics while paper-level visual repair/backfill remains unhealthy.

## 5. README public reading order

The README should optimize the top of the page for a returning researcher rather than for maintenance chronology.

The substantive section order becomes:

1. **Latest Papers** — first substantive section after the short repository header/update/navigation line;
2. **Start Here** — reading paths for researchers entering the field or following a specific research question;
3. **Design Anchors / Browse by Research Problem** — the durable field map and problem-oriented folds;
4. **Research Compactions** — weekly, monthly, and yearly synthesis after the paper-level and research-map surfaces.

The compaction hierarchy and navigation remain intact; only its prominence/order changes. Weekly/monthly/yearly summaries are still important synthesis artifacts, but they should not displace the newest accepted papers from the first screenful.

README remains strictly reader-facing. Visual resolution checks, master paths, backfill state, generation failures, validator behavior, and scheduler mechanics belong in maintenance documents and structured records, not in public prose.

## 6. Daily maintenance contract

Update the visual-maintenance contract so future daily runs enforce the dual-asset and explanation requirements at ingestion time rather than creating another repair queue.

For every newly accepted paper:

1. ground and generate one single-paper visual;
2. keep the accepted PNG as master;
3. derive a same-dimension high-quality WebP;
4. verify both assets and dimensions;
5. write the paper-specific visual explanation;
6. embed WebP + explanation on the paper page and, if visible in Latest Papers, inside the README 60-second fold;
7. only then mark the visual `generated`.

A failure at any step leaves the visual internally pending/needs-regeneration and must never be represented as successfully visible on README.

## Success criteria

The change is complete when:

- no generated visual used on README is a thumbnail-scale asset;
- every generated visual has a canonical PNG master and same-resolution WebP display copy;
- every visible Latest Papers visual has a concise paper-specific explanation directly beneath it;
- validator catches future accidental downsampling or missing masters;
- README opens with Latest Papers and compactions appear later without losing their weekly/monthly/yearly hierarchy;
- existing public research content remains consistent with canonical records and no operational details leak into README.
