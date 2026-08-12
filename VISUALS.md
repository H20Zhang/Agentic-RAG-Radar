# Visual Explainer Protocol

Every accepted paper should have **one original GPT-image-gen conceptual explainer** whose job is to make the paper's research delta understandable in roughly 10 seconds.

The image is **our research interpretation**, not a reproduction or stylistic copy of the paper's original figure. It must not imply mechanisms, components, causal edges, or empirical results that were not verified.

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

## Asset convention

Prefer a compressed web-friendly asset:

```text
assets/visuals/<paper-id>.webp
```

PNG is acceptable only when conversion/upload to WebP is unavailable. The canonical record's `image_path` is the source of truth; never assume an extension.

Grounding/prompt notes live at:

```text
assets/visuals/prompts/<paper-id>.md
```

The prompt note is the auditable source for regeneration and should contain: **Visual question**, **Grounded mechanism**, **Research delta**, **Compared with**, **Do not imply**, and **Grounding status**.

## Image-generation constraints

- Prefer **GPT-image-gen**.
- Generate **one named paper per invocation**. Never ask one image call to produce a repo dashboard, multi-paper collage, status board, or decorative banner while paper backfill exists.
- Use a clean research-figure aesthetic: simple geometry, whitespace, restrained palette, no decorative 3D objects.
- Keep image text to roughly **3–7 short labels**; explanations belong in Markdown.
- One image should emphasize **one research delta**.
- Do not reproduce the paper's original figure composition.
- Do not put benchmark numbers, dates, arXiv IDs, repo counts, or citations into the generated image unless they are absolutely necessary and independently verified. In practice, prefer to keep all numbers in Markdown.
- Do not invent implementation details or causal arrows for visual balance.

## QC gate

A render is **failed** if it drifts from the named paper into a repository UI/dashboard, invents methods/results, mixes multiple papers, or visually asserts a causal claim that the evidence does not establish. Discard it; do not commit it as a placeholder.

The skeptical reviewer separately asks:

1. Does the image make the contribution look more novel or deterministic than the evidence warrants?
2. Is any arrow/component/state invented or inferred too aggressively?
3. Is the baseline comparison actually the nearest design point?
4. Does the image hide a substrate/budget confound?
5. Can one element be removed without losing the key idea? If yes, simplify.

A beautiful but misleading visual is worse than no visual.

## Required embedding behavior

When `visual_explainer.status == generated` and the committed `image_path` exists:

- embed the image near the top of `papers/<id>.md` under **Visual explainer**;
- if the paper is visible in README **Latest Papers**, also embed the same image near the top of its collapsed **Understand this paper in 60 seconds** block;
- use repository-relative paths and useful alt text;
- keep the paper page understandable if the image fails to render.

Paper-page pattern:

```md
![Conceptual explainer for <paper>](../assets/visuals/<paper-id>.webp)
```

README pattern:

```md
![Conceptual explainer for <paper>](assets/visuals/<paper-id>.webp)
```

Never expose `pending`, `needs_regeneration`, backfill queues, or renderer failures on public README.

## Backfill policy

- New accepted papers should receive a visual in the **same curation run** when a one-paper render passes QC.
- Existing accepted papers with missing visuals are the priority backfill queue before cosmetic/synthesis graphics.
- If generation drifts or fails, keep the grounded brief and `pending` status internally; do not fabricate a placeholder.
- Re-generate when a full-paper read materially changes the interpreted mechanism.
- Mark `generated` only after the binary asset is verified in GitHub and all required embeds point to the exact committed path.

## Compaction visuals

Only after per-paper backfill is healthy may a weekly/monthly/yearly compaction receive one synthesis image. It must be grounded from canonical paper records and explain a **field-level tension or map**, not act as decorative repo branding.
