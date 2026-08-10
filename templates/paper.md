# {{ title }}

**arXiv:** [{{ arxiv_id }}]({{ paper_url }}) · **Published:** {{ published }} · **Category:** {{ primary_category }} · **Importance:** {{ importance }}/5 · **AI confidence:** {{ confidence }}

**Tags:** {{ tags }}

> **TL;DR.** {{ tldr }}

## Visual explainer

> AI-generated conceptual explainer; **not** a reproduction of the paper's original figure.

![Conceptual explainer for {{ title }}](../assets/visuals/{{ paper_id }}.png)

**What to notice.** {{ visual_takeaway }}

**Compared with.** {{ visual_compared_with }}

**Grounding.** {{ visual_grounding }}

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

---

### Provenance & visual audit

- Paper claims and curator inference must be distinguishable.
- Never infer experimental superiority from an abstract alone.
- `Compared to what` should identify the nearest design point, not a generic RAG baseline.
- The visual must follow [`VISUALS.md`](../VISUALS.md) and be regenerated if a full-paper read changes the interpreted mechanism.
- Store/review the image-generation grounding note at `../assets/visuals/prompts/{{ paper_id }}.md`.
