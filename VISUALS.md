# Visual Explainer Protocol

Every accepted paper should have **one original GPT-image-gen conceptual explainer** whose job is to make the paper's research delta understandable in roughly 10 seconds.

The image is **our research interpretation**, not a reproduction or stylistic copy of the paper's original figure. It must not imply mechanisms, components, or empirical results that were not verified.

## Why generated figures, not generic architecture diagrams

A good visual should answer one research question, not decorate the paper card. Different contributions need different visual grammars:

| Paper type | Preferred explainer | Question the image must answer |
|---|---|---|
| **Method / system** | agent control-loop explainer | What does the agent observe, decide, retrieve, update, and repeat? |
| **Retrieval interface** | before/after operation-space diagram | What replaces or augments fixed top-k, and why can the agent express a different information need? |
| **Stateful retrieval** | evidence-state progression | What state survives between retrieval actions and how does it change the next decision? |
| **Learning / RL** | trajectory → supervision/reward → policy | What behavior is optimized and what changes at inference time? |
| **Benchmark / analysis** | failure/evidence map | What capability or confound is isolated, compared with what? |
| **Survey / SoK** | compact design-space map | What axes organize the field and where do representative methods differ? |

Do **not** force every paper into the same boxes-and-arrows architecture.

## Asset convention

Generated images live under:

```text
assets/visuals/<paper-id>.png
```

The grounding/prompt note lives beside the research note or under:

```text
assets/visuals/prompts/<paper-id>.md
```

The prompt note is the auditable source for regeneration. It should contain:

- **Visual question** — the one thing the image explains.
- **Grounded mechanism** — verified components/edges/state that are allowed to appear.
- **Research delta** — what must visually dominate.
- **Compared with** — the nearest baseline/design point.
- **Do not imply** — mechanisms/results that would overstate the evidence.
- **Grounding status** — `full-text` or `abstract-level`.

Static image assets are presentation; these text fields are the research provenance.

## Visual grammar

For most method papers, aim for a wide research explainer with two semantic layers:

```text
LEFT / muted:        prior or static design point
                    Query → fixed retrieval → context → answer

RIGHT / dominant:    paper's changed control surface
                    Query / plan
                        ↓
                    decision / state
                        ↓
                    retrieval operation(s)
                        ↓
                    evidence / observation
                        ↺ feedback into state
                        ↓
                    answer / stop
```

This is a conceptual grammar, not a mandatory layout. A learning paper may be better shown as trajectory/reward/policy; an evaluation paper may need a failure matrix instead.

## Image-generation constraints

- Prefer **GPT-image-gen** as the primary renderer.
- Use a clean research-figure aesthetic: high information density, generous whitespace, simple geometry, restrained palette, no decorative 3D objects.
- Keep text inside the image minimal: ideally **3–7 short labels**. Long explanations belong in Markdown because generated text is less reliable and harder to update.
- Use arrows, grouping, contrast, and icons/shapes to communicate structure; do not rely on color alone.
- One image should emphasize **one delta**. If the prompt tries to explain motivation, architecture, training, benchmark, and results simultaneously, simplify it.
- Do not copy the paper's original figure composition. Build a new conceptual explanation from verified understanding.
- Do not put quantitative gains into the image unless a single result is essential to the conceptual argument and has been verified.
- Do not invent implementation details to make the figure visually balanced.

## Required Markdown around each image

Each paper page should show the image near the top:

```md
![Conceptual explainer for <paper>](../assets/visuals/<paper-id>.png)
```

Then add three compact lines:

- **What to notice:** the single research delta the image is designed to teach.
- **Compared with:** the nearest prior/static design point.
- **Grounding:** full-text checked / abstract-grounded; explicitly state uncertainty.

The research page remains understandable even if the image fails to render.

## QC gate

The skeptical reviewer must challenge the visual separately from the prose:

1. Does the image make the paper look more novel or more deterministic than the evidence warrants?
2. Is any arrow/component/state invented or inferred too aggressively?
3. Is the baseline comparison actually the nearest design point?
4. Would an author of the paper object that a central mechanism is missing or misrepresented?
5. Can one visual element be removed without losing the key idea? If yes, simplify.

A beautiful but misleading visual is worse than no visual.

## Backfill policy

- New accepted papers should receive a visual in the **same curation run** when image generation is available.
- Existing accepted papers with missing visuals are a backfill queue and should be processed before low-importance cosmetic work.
- If image generation fails, keep the paper record and mark the visual as pending; do not fabricate a placeholder that looks authoritative.
- Re-generate a visual when a full-paper read materially changes the interpreted mechanism.

## Weekly / monthly synthesis visuals

Compactions may also receive one GPT-image-gen figure when it materially improves understanding:

- **Weekly:** a tension/cluster map showing how 2–4 papers change different parts of the same control loop.
- **Monthly:** a field map such as `substrate → interface → state/policy → learning/evaluation`, highlighting which layer is gaining attention and where evidence is weak.

Synthesis images must be grounded from canonical paper records, not generated by recursively visualizing previous prose summaries.