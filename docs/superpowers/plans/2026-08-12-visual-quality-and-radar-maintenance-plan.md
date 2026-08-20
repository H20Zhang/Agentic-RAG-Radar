# Visual Quality and Aug 12 Radar Maintenance Plan

## Objective

Implement the approved visual-quality/README-order design while using the daily curation pass to repair important holes in the research map.

## Sequence

1. Update the visual contract, schema, validator, and CI dependency so `generated` means a high-resolution PNG master plus same-dimension WebP display asset and reader-facing figure explanation.
2. Audit current generated visuals. Do not upscale low-resolution assets. Keep any visual that cannot be regenerated and uploaded faithfully in `needs_regeneration` rather than presenting it as complete.
3. Move README `Latest Papers` to the first substantive section, followed by Start Here, anchors/problem map, and Research Compactions.
4. Backfill only papers that materially change the field map. This run prioritizes S2G-RAG (explicit sufficiency/gap state), SPARKLE (adaptive-vs-adaptive learned policy evidence), and budget-aware Active RAG evaluation (utility/calibration/cost).
5. Propagate accepted backfills into canonical records, notes, visual briefs, category pages, compactions, and the digest index. Re-run validation and preserve the accepted transaction in commit history; never create a public Daily Agent run log.

## Verification

- `python scripts/validate.py` must pass in CI with Pillow installed.
- README must contain Latest Papers before Research Compactions and no maintenance/backfill mechanics.
- New accepted papers must have grounded visual briefs but stay pending until a one-paper render passes QC and both binary assets are verified.
- No low-resolution visual may remain marked `generated` merely because the old WebP file exists.
