# {{ title }}

**arXiv:** [{{ arxiv_id }}]({{ paper_url }}) · **Published:** {{ published }} · **Category:** {{ primary_category }} · **Importance:** {{ importance }}/5 · **AI confidence:** {{ confidence }}

**Tags:** {{ tags }}

> **TL;DR.** {{ tldr }}

## Visual explainer

{{ visual_explainer_block }}

<!--
When visual_explainer.status == generated, visual_explainer_block must use the committed WebP delivery asset and include all three reader-facing lines:

![Conceptual explainer for {{ title }}](../assets/visuals/{{ paper_id }}.webp)

**How to read this figure.** {{ visual_reading_guide }}

**Compared with.** {{ visual_compared_with }}

**Do not over-read.** {{ visual_caveat }}

The PNG master remains at ../assets/visuals/masters/{{ paper_id }}.png and is not embedded in the paper page.

When the visual is pending or needs regeneration, do not embed a missing/invalid bitmap. Keep the page understandable with a concise sentence pointing to the grounded brief at ../assets/visuals/prompts/{{ paper_id }}.md.
-->

## Problem

{{ problem }}

## Core idea

{{ core_idea }}

## Agent loop

`{{ agent_loop }}`

## Retrieval design

{{ retrieval_design }}

## Compared to what

{{ compared_to }}

## Evidence

{{ evidence }}

## Why it matters

{{ why_it_matters }}

## Limitations / questions

{{ limitations }}

**Curator take:** **{{ importance }}/5**. {{ curator_take }}

<details>
<summary><strong>Evidence & provenance</strong></summary>

{{ provenance_summary }}

Visual grounding follows [`VISUALS.md`](../VISUALS.md); the auditable grounding brief lives at `../assets/visuals/prompts/{{ paper_id }}.md`.

</details>
