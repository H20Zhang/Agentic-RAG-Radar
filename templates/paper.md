# {{ title }}

*Published {{ published }} · {{ primary_category }} · Importance {{ importance }}/5 · {{ review_level }} · Confidence {{ confidence }}*

[Paper]({{ paper_url }}){{ optional_code_project_links }}

> **TL;DR.** {{ tldr }}

| 30-second verdict | |
|---|---|
| **Why this paper matters** | {{ why_it_matters_short }} |
| **Strongest evidence** | {{ strongest_evidence_short }} |
| **Biggest caveat** | {{ biggest_caveat_short }} |

{{ generated_visual_block }}

<!--
When a validated visual is generated, generated_visual_block may contain one or more distinct grounded figures. The canonical visual must use the committed WebP delivery asset:

![Conceptual explainer for {{ title }}](../assets/visuals/{{ paper_id }}.webp)

**How to read this figure.** {{ visual_reading_guide }}

**Compared with.** {{ visual_compared_with }}

**Do not over-read.** {{ visual_caveat }}

Additional editorial figures are allowed only when they answer a distinct research question (for example mechanism vs evidence attribution). Do not show any placeholder or pending-status prose when no figure is ready.
-->

## Research question

{{ research_question }}

## Research delta

{{ research_delta }}

State the **smallest claim that remains novel** after comparison with the closest historical and contemporary design points.

## Mechanism

{{ mechanism }}

**Control flow.** `{{ agent_loop }}`

Explain the relevant retrieval interface, state transition, learning loop, or evaluation intervention here rather than forcing every paper into identical subheadings.

## Evidence & attribution

{{ evidence_analysis }}

When useful, include a compact table:

| Claim | Evidence | Closest control | Assessment |
|---|---|---|---|
| {{ claim }} | {{ evidence }} | {{ control }} | {{ assessment }} |

Keep the strongest negative result, resource/harness/model confound, and what is actually identified causally next to the positive evidence.

## Where it fits

{{ lineage_and_comparison }}

Connect the paper to a useful design lineage or tension, not merely a category label.

## Open question

{{ decisive_open_question }}

End with the experiment or evidence that would most change the current interpretation.

<details>
<summary><strong>Evidence & provenance</strong></summary>

{{ provenance_summary }}

Visual grounding follows [`VISUALS.md`](../VISUALS.md); canonical records live under `../data/papers/`.

</details>
