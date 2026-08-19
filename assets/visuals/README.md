# Visual Explainers

This directory stores the rendered conceptual explainers used by Agentic RAG Radar. The bitmap is a teaching surface; the grounded research interpretation remains auditable through the canonical paper record and prompt brief.

## Asset contract

For every accepted paper, the grounding brief exists at:

```text
assets/visuals/prompts/<paper-id>.md
```

A completed visual has two committed binary assets:

```text
assets/visuals/masters/<paper-id>.png  # canonical high-quality master
assets/visuals/<paper-id>.webp         # README/paper-page delivery copy
```

The WebP must preserve the PNG master's pixel dimensions. The normal minimum width is 1536 px. Do not repair a thumbnail by upscaling it; regenerate from the grounded brief when the high-resolution source is unavailable.

## Status semantics

The canonical `data/papers/<id>.json` record is the source of truth.

- `pending` — the paper record and grounded brief exist, but no QC-passing dual-asset visual has been committed.
- `needs_regeneration` — a previous visual is invalid, outdated, low-resolution, or no longer matches the grounded interpretation.
- `generated` — the PNG master and same-resolution WebP are committed and verified, and required paper/README embeds plus figure-reading explanations are synchronized.

A visual must not be marked `generated` merely because a bitmap exists.

## Reader-facing explanation

When a generated visual appears on a paper page, the WebP is followed immediately by:

- **How to read this figure.** The paper-specific flow and intended research delta.
- **Compared with.** The nearest baseline or design point.
- **Do not over-read.** The strongest caveat or causal interpretation the figure must not imply.

The same compact explanation appears inside the README 60-second fold when that paper is currently visible in Latest Papers.

## Backfill priority

1. Current/latest accepted papers.
2. Design anchors and papers used by active reading paths.
3. Remaining accepted-paper explainers.
4. Weekly/monthly/yearly synthesis visuals only after paper-level visual health is good.

Do not spend image-generation budget on decorative repo banners, dashboards, status boards, or multi-paper collages while paper explainers remain incomplete.

See [`../../VISUALS.md`](../../VISUALS.md) for the full generation, grounding, dual-asset, and skeptical-QC protocol.
