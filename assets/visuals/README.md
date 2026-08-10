# Visual Explainers

This directory stores the rendered **GPT-image-gen** explainers used by Agentic RAG Radar.

The source of truth is not the bitmap itself. Every paper record stores the visual question, research takeaway, nearest comparison, grounding status, intended image path, and prompt/grounding brief.

## Current contract

For every accepted paper:

```text
data/papers/<id>.json
papers/<id>.md
assets/visuals/prompts/<id>.md
assets/visuals/<id>.png       # required once status=generated
```

`status=pending` or `needs_regeneration` means the grounded brief exists but image generation/commit still needs to run. CI validates the brief and paper card even before the PNG exists; it requires the PNG once the record is marked `generated`.

## Backfill priority

1. Current/latest accepted papers.
2. Design anchors used by weekly/monthly reading paths.
3. Weekly/monthly synthesis figures when they add genuine explanatory value.

Do not spend image-generation budget on decorative repo banners before paper explainers are complete.

See [`../../VISUALS.md`](../../VISUALS.md) for the full visual and skeptical-QC protocol.
