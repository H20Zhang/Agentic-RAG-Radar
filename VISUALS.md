# Visual Explainer Protocol

Every accepted paper should have **one canonical original conceptual explainer** whose job is to make the paper's research delta understandable in roughly 10 seconds. Prefer GPT-image-gen; use another renderer only when it is explicitly recorded and the result is more faithful than a failed generated render.

The image is **our research interpretation**, not a reproduction or stylistic copy of the paper's original figure. It must not imply mechanisms, components, causal edges, or empirical results that were not verified.

The broader reader surface may also use **secondary editorial research diagrams** when they answer a different question—for example a mechanism overview plus a separate evidence-attribution diagram. More figures are useful only when each figure removes real cognitive work.

## Pick the visual grammar from the research question

| Paper type | Preferred explainer | Question the image must answer |
|---|---|---|
| **Method / system** | agent control-loop explainer | What does the agent observe, decide, retrieve, update, and repeat? |
| **Retrieval interface** | before/after operation-space diagram | What replaces or augments fixed top-k, and what new information need becomes expressible? |
| **Stateful retrieval** | evidence-state progression | What state survives between actions and how does it change the next decision? |
| **Learning / RL** | trajectory → supervision/reward → policy | What behavior is optimized and what changes at inference time? |
| **Benchmark / analysis** | failure/evidence map | What capability or confound is isolated, compared with what? |
| **Survey / SoK** | compact design-space map | What axes organize the field and where do representative methods differ? |

Do **not** force every paper into the same boxes-and-arrows architecture.

## Dual-asset contract for the canonical paper visual

A completed canonical visual has two committed assets:

```text
assets/visuals/masters/<paper-id>.png
assets/visuals/<paper-id>.webp
```

The PNG is the canonical high-quality master. The WebP is the README/paper-page delivery copy. **Compression must not resize the image**: PNG and WebP must have identical pixel dimensions. The normal minimum is **1536 px wide**; when the native accepted render is slightly narrower, regenerate rather than upscale. Padding without resampling is acceptable only when it does not reduce readability.

Do not treat a thumbnail-scale WebP as repaired by upscaling it. If the original high-resolution render is unavailable, regenerate from the grounded brief.

Grounding/prompt notes live at:

```text
assets/visuals/prompts/<paper-id>.md
```

The prompt note is the auditable source for regeneration and should contain: **Visual question**, **Grounded mechanism**, **Research delta**, **Compared with**, **Do not imply**, and **Grounding status**.

## Secondary editorial research diagrams

Reader-facing maps, icons, lineage strips, and additional paper-specific diagrams may live under:

```text
assets/editorial/
```

These diagrams are allowed when they answer a **different grounded research question** from the canonical visual. Useful examples:

- field-level mental model;
- stable semantic icon set;
- method placement/lineage;
- claim → evidence → causal-boundary diagram;
- benchmark failure decomposition.

They are not a loophole around canonical visual QC. Do not use editorial diagrams as placeholders for a failed canonical render, and do not create multiple decorative variants of the same mechanism. See `assets/editorial/README.md`.

## Image-generation constraints

- Prefer **GPT-image-gen** and generate **one named paper per invocation**.
- Never generate repo dashboards, multi-paper status boards, or decorative banners.
- Use a clean research-figure aesthetic: near-white background, simple geometry, whitespace, restrained blue/teal/neutral palette, no decorative 3D objects.
- Keep image text to roughly **3–7 short labels**; explanations belong in Markdown.
- One figure should emphasize **one research question**.
- Do not reproduce the paper's original figure composition.
- Do not put benchmark numbers, dates, arXiv IDs, repo counts, or citations into a generated image unless absolutely necessary and independently verified. Prefer numbers in Markdown or an evidence table.
- Do not invent implementation details or causal arrows for visual balance.

## Reader explanation is part of the visual

An image alone is incomplete. Immediately below every canonical generated visual, the paper page must include:

- **How to read this figure.** Two or three paper-specific sentences explaining the regions/flow and intended research delta.
- **Compared with.** The nearest baseline or design point represented by the visual.
- **Do not over-read.** The strongest caveat, confound, or causal interpretation the image must not imply.

If the paper appears in README **Latest Papers**, its collapsed **Research snapshot** must include the same concise reader explanation directly after the canonical image.

Secondary editorial diagrams should also have enough surrounding prose to make their intended interpretation and boundary obvious; they do not need duplicate boilerplate when the nearby section already provides it.

## QC gate

A render is **failed** if it drifts from the named paper into repository UI/dashboard content, invents methods/results, mixes multiple papers, or visually asserts a causal claim the evidence does not establish. Discard it; do not commit it as a placeholder.

The skeptical reviewer separately asks:

1. Does the image make the contribution look more novel or deterministic than the evidence warrants?
2. Is any arrow/component/state invented or inferred too aggressively?
3. Is the baseline comparison actually the nearest design point?
4. Does the image hide a substrate, harness, or budget confound?
5. Can one element be removed without losing the key idea? If yes, simplify.
6. If there is already another figure on the page, does this one answer a genuinely different question?

A beautiful but misleading visual is worse than no visual.

## Required embedding behavior

When `visual_explainer.status == generated`:

- `master_image_path` must point to the committed PNG master;
- `image_path` must point to the committed same-resolution WebP;
- both assets must pass the dimension contract;
- embed the WebP near the top of `papers/<id>.md`;
- if the paper is visible in README **Latest Papers**, embed the same WebP inside its Research snapshot;
- include the reader explanation in both places where the canonical image appears.

Use repository-relative paths and useful alt text. Never expose `pending`, `needs_regeneration`, renderer failures, or backfill queues on public reader surfaces.

## Backfill policy

- New accepted papers should receive a canonical visual in the same curation run only when a one-paper render passes QC and both assets can be verified.
- Existing low-resolution or master-less canonical visuals are repaired before cosmetic graphics.
- If generation or binary upload fails, keep the grounded brief and internal `pending`/`needs_regeneration` state; **show no public placeholder prose**.
- Re-generate when a full-paper read materially changes the interpreted mechanism.
- Mark `generated` only after both binary assets, dimensions, embeds, and explanations are verified.
- High-value editorial diagrams may be added independently when they materially improve mechanism/evidence comprehension, but they must not obscure the canonical visual backlog.

## Compaction visuals

Weekly/monthly/yearly synthesis may receive a field-level visual when it genuinely improves understanding of a durable tension or map. The figure must be grounded from canonical records and explain a **field-level research question**, not act as decorative repo branding.
