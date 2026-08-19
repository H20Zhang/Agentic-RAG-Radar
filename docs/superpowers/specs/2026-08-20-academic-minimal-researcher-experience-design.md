# Academic-Minimal Researcher Experience Design

## Goal

Make Agentic RAG Radar feel and behave like a **living research survey that a researcher would bookmark and revisit**, rather than a product README, newsletter, or AI-generated paper feed.

The design target is:

> **80% academic minimalism + 20% editorial research magazine.**

Academic minimalism governs typography, hierarchy, page responsibility, evidence presentation, and restraint. Editorial energy is reserved for the newest papers and the current field-level synthesis, where some freshness and opinion are useful.

The repository should communicate three qualities within the first minute:

1. **Research judgment** — the radar distinguishes novelty, evidence strength, confounders, and prior design points rather than summarizing abstracts.
2. **Information density without UI clutter** — readers can scan quickly without badges, decorative chrome, repetitive metadata, or maintenance state.
3. **A coherent field model** — papers are connected into research questions, lineages, tensions, and falsifiable next experiments.

## Non-goals

- Do not turn the repository into a website, dashboard, newsletter, or card-heavy product UI.
- Do not maximize visual novelty for its own sake.
- Do not add decorative banners, visitor counters, star-count badges, tag clouds, or status badges.
- Do not make every page repeat the same metadata, research delta, and evidence text.
- Do not make category labels the primary field model when a more meaningful research question exists.
- Do not remove skeptical evidence, negative results, or causal caveats merely to make pages look cleaner.
- Do not auto-generate research judgment from metadata.

## 1. Page responsibility model

Every public surface gets one primary job.

| Surface | Primary researcher job | Must not become |
|---|---|---|
| `README.md` | Decide what deserves attention now | exhaustive archive or product landing page |
| `README.md#whats-changing` | Understand what new evidence means at multiple timescales | digest index dump |
| `README.md#reading-paths` | Learn a research question efficiently | generic onboarding |
| `categories/README.md` | Understand the current research design space | taxonomy directory |
| `categories/*.md` | Follow one research question and its live argument | paper list |
| `papers/README.md` | Find an accepted paper quickly | repeated research summaries |
| `papers/<id>.md` | Understand and assess one paper | metadata card or maintenance log |
| `digests/*` | Reconstruct field movement over time | concatenated paper summaries |

The core rule is:

> **README says what matters; synthesis says what it means; map says how to think; index says where to find; paper note says why to believe.**

## 2. Visual and editorial language

### 2.1 Remove product/UI chrome

The public surface should avoid visual patterns that read as product marketing or recommendation feeds:

- remove decorative section emoji from primary H2 headings;
- remove the robot emoji from the repository title;
- move the star CTA away from the first screenful;
- replace star-glyph importance (`★★★★☆`) with restrained textual `Importance 4/5` where importance is useful;
- avoid dense code-style tag strings in Latest Papers;
- avoid repeated bold labels that create a pseudo-dashboard appearance;
- keep tables only when they genuinely improve comparison or scanning.

Emoji may remain in rare utility contexts only if it materially improves navigation, but the default public style is plain text.

### 2.2 Preferred vocabulary

Use researcher-facing labels rather than AI/product language.

Prefer:

- `Research delta`
- `Evidence boundary`
- `Evidence & attribution`
- `Nearest design point`
- `Where it fits`
- `Open question`
- `Full-text reviewed`
- `Importance 4/5`

Avoid on the main research surfaces:

- `AI take`
- recommendation-style star ratings
- `awesome`, `hot`, `trending`, `SOTA` unless directly discussing a paper claim
- maintenance states such as `pending`, `needs_regeneration`, `backfill`

### 2.3 Density principle

The design should be **compact, not sparse**.

Academic minimalism does not mean removing useful evidence. It means removing repeated framing and UI chrome so the remaining research content has more visual weight.

## 3. Root README redesign

The opening should be calm and research-first.

Recommended structure:

```text
# Agentic RAG Radar

A continuously curated research map of adaptive retrieval, search agents,
and retrieval-aware agent systems.

Current thesis. ...

Latest Papers · What's Changing · Reading Paths · Research Map · Paper Index
```

The first screenful should contain only:

- title;
- one-sentence scope;
- current field thesis;
- compact navigation;
- the beginning of Latest Papers.

The star/follow CTA moves to the lower part of the README near About/Contributing.

### 3.1 Latest Papers

Latest Papers remains the first substantive section.

Each paper should have a restrained editorial card:

```text
### LENS — In-Context Search via Latent Evidence Exploration over Dynamic Raw Documents
*17 Aug 2026 · Retrieval & Tool Use · Importance 4/5 · Full-text reviewed*

**Research delta.** Moves evidence materialization from indexing time to query time.

**Evidence boundary.** Better evidence recall/grounding, but ReAct is slightly
better on D500 answer EM; LENS also spends more online compute.

[Paper] · [Research note]

<details>
<summary>Research snapshot</summary>
...
</details>
```

The default scan should answer:

1. What changed?
2. Compared with what?
3. What is the strongest reason not to overclaim?

Tags should not appear in the default Latest scan unless a tag is itself central to the research delta.

### 3.2 Research snapshot fold

Rename `Understand this paper in 60 seconds` to **Research snapshot**.

A snapshot should be shorter and more research-oriented:

- Research question
- Mechanism / control flow
- Nearest design point
- Evidence & attribution
- Open question

Do not repeat the same Research delta / Evidence boundary prose verbatim from the collapsed card.

Generated visuals, when available, remain near the top of the fold only when they genuinely compress the mechanism. A paper without a generated visual should show no visual placeholder or visual-status text.

## 4. What's Changing redesign

The homepage should not enumerate several weekly digests plus month plus year as an archive list.

Instead, expose **one current synthesis at each useful timescale**:

| Horizon | Research question | Current synthesis |
|---|---|---|
| This week | What new evidence changed the map? | one concise thesis |
| This month | What design space is emerging? | one concise thesis |
| 2026 YTD | What looks durable? | one concise thesis |

Each row/entry links to the underlying report.

The section ends with a single link to the synthesis archive.

The intended transition is:

`new papers -> interpretation at multiple timescales`

not:

`new papers -> another chronological list of report files`.

## 5. Reading Paths redesign

Reading Paths stays small: normally three paths.

Each path should be named by a **research question**, not by a broad category.

Each path gives:

- 3–5 papers maximum;
- a deliberate order;
- one sentence describing the conceptual progression;
- optionally one `If you only read three papers` fold for the whole field.

Avoid onboarding language such as `Start Here`.

A path is successful when a researcher can explain why paper B should be read after paper A.

## 6. Research Map redesign

`categories/README.md` becomes a **research-question map**, not primarily a six-category taxonomy table.

The first layer should present 4–6 live questions such as:

1. **Where should adaptivity live?**
2. **When should evidence be materialized?**
3. **What state should persist?**
4. **How should retrieval interfaces expose the corpus?**
5. **What should be learned?**
6. **What makes an evaluation causal?**

Each question should expose:

- Current answer
- Key evidence / design points
- Strongest counterexample or boundary
- What would change our mind

Example:

| Research question | Current answer | Key evidence | What would change our mind? |
|---|---|---|---|
| Where should adaptivity live? | Some control can be compiled before retrieval; other control requires result-conditioned evidence. | SIRA ↔ ReFind | Same substrate/model/budget comparison |

The existing six canonical categories remain useful as navigation/taxonomy and canonical ownership for paper records, but they move below the live research-question map.

### 6.1 Category pages

Each category page should read like a short research memo:

- Core question
- Current answer / signal
- Key design points
- Current tension
- Next decisive evidence
- Relevant papers

Paper lists should support the argument rather than dominate the page.

## 7. Paper-note redesign

Paper notes should feel like a strong researcher's reading notes rather than a fixed metadata template.

Recommended public structure:

```text
# Title

Published ... · Category ... · Importance 4/5 · Full-text reviewed · Confidence high

> TL;DR.

## Research question
## Research delta
## Mechanism
## Evidence & attribution
## Where it fits
## Open question
```

### 7.1 Research question

State the actual question the paper is trying to resolve, not merely the problem statement from the introduction.

### 7.2 Research delta

State the smallest claim that remains novel after comparing with the nearest historical and contemporary design point.

### 7.3 Mechanism

Use the structure appropriate to the paper:

- Agent loop
- Retrieval interface
- State progression
- Training trajectory
- Evaluation/failure map

Do not force every paper into separate `Agent loop` and `Retrieval design` sections when one coherent mechanism section is clearer.

### 7.4 Evidence & attribution

This becomes the intellectual center of the note.

Combine:

- strongest result;
- closest matched baseline;
- key ablation/intervention;
- negative result;
- major resource/harness/model confound;
- what the evidence actually identifies causally.

Avoid separating positive evidence and caveats so far apart that readers retain only the headline.

### 7.5 Where it fits

Explicitly connect the paper into a design lineage or tension, for example:

`SIRA -> ReFind -> LENS`

or

`S2G-RAG -> RAAC -> LoongReflect`.

This is more valuable to a researcher than a generic `Why it matters` paragraph.

### 7.6 Open question

End with one decisive research question or experiment, not a generic list of limitations.

### 7.7 Visual behavior

If `visual_explainer.status != generated`, the public note contains **no Visual explainer section and no pending-status prose**.

If generated, show:

- WebP visual;
- `How to read this figure`;
- `Compared with`;
- `Do not over-read`.

Visual maintenance metadata stays in canonical JSON / prompt briefs only.

## 8. Curated Paper Index redesign

The index should optimize for lookup and scanning, not repeat the research-note content.

Replace multi-paragraph entries with a compact chronology table.

Recommended columns:

| Date | Paper | Area | Importance | Review |
|---|---|---|---:|---|

Paper title links to the research note. An adjacent compact `paper` link may be included where useful.

`Review` uses restrained values such as:

- `Full text`
- `Abstract`

Do not repeat `Research delta` in the index; that responsibility belongs to Latest Papers, Research Map, and paper notes.

For many papers, group by year/month with collapsible historical years if necessary.

## 9. Digest landing redesign

`digests/README.md` should feel like a research synthesis archive.

Its opening explains the three timescales:

- Weekly: local changes and disagreements
- Monthly: rebuilt field map
- Yearly: durable changes and weakened ideas

Show one-line thesis links, not full mini-summaries for every artifact.

The page should emphasize that digests are **interpretation layers**, not paper feeds.

## 10. Research aesthetics for generated visuals

The visual contract remains research-first, but aesthetic guidance becomes stricter.

Preferred figure style:

- white or near-white background;
- restrained blue/teal/neutral palette;
- thin lines and simple geometry;
- strong whitespace;
- one mechanism or comparison per figure;
- 3–7 labels maximum;
- no glossy cards, UI chrome, dashboards, status pills, decorative icons, or product mockups;
- visual hierarchy similar to a strong systems/ML paper overview figure rather than a startup infographic.

A figure should look plausible beside a FAST/SOSP/OSDI/SIGMOD/NeurIPS paper figure while remaining original and easier to read.

## 11. Validator evolution

`validate_public.py` should protect research quality without enforcing one brittle Markdown template.

### Enforce

- first substantive section remains Latest Papers;
- public heading order remains coherent;
- Latest cards contain Research delta and Evidence boundary;
- Latest papers have canonical records and notes;
- no star-glyph importance ratings in primary research surfaces;
- no `AI take` in Latest cards;
- no public `pending`, `needs_regeneration`, backfill, renderer, or scheduler state;
- paper notes expose Research question, Research delta, Evidence & attribution, Where it fits, and Open question;
- generated visuals have the required reader explanation;
- Paper Index is deterministically generated and compact;
- public relative links resolve.

### Do not enforce

- identical mechanism subheadings across every paper;
- the presence of a visual section when no generated visual exists;
- a fixed number of paragraphs or bullet points;
- category pages all having identical density.

The validator protects **reader contract**, not formatting trivia.

## 12. Canonical data and template implications

No schema change is required merely for the editorial redesign.

Existing canonical fields remain sufficient:

- `analysis.tldr`
- `analysis.problem`
- `analysis.core_idea`
- `analysis.agent_loop`
- `analysis.retrieval_design`
- `analysis.compared_to`
- `analysis.evidence`
- `analysis.why_it_matters`
- `analysis.limitations`
- `visual_explainer.takeaway`
- provenance/full-text state

Human-edited notes may reorganize these into the new public structure.

`templates/paper.md` should be updated to the new researcher-facing note shape so future papers do not drift back to the older template.

## 13. Scheduled-maintenance implications

`docs/DAILY_WORKFLOW.md` should add an explicit **editorial quality gate** before publication.

For every public update, ask:

1. Does the newest paper card make the actual delta and evidence boundary obvious in <20 seconds?
2. Did the update change a field-level research question, or only add another item?
3. Is any metadata repeated across README, index, map, and note without serving a different reader task?
4. Did any maintenance/internal state leak onto a public page?
5. Did the update increase UI chrome, tags, badges, or visual noise?
6. Would a researcher learn a comparison or open question they could act on?

The automation should prefer **no public structural change** over a mechanically complete but aesthetically degraded update.

## 14. Implementation sequence

Use a short-lived branch/PR so the editorial redesign can be reviewed as one coherent surface rather than a series of half-migrated main-branch states.

### Phase 1 — Public style foundation

- root README opening and Latest card grammar;
- remove emoji-heavy/product-like headings and first-screen star CTA;
- update terminology (`AI take` -> `Research delta` / `Evidence boundary`);
- update public validator expectations.

### Phase 2 — Research navigation

- redesign What's Changing into three current timescales;
- refine Reading Paths;
- redesign Research Map around live research questions;
- move taxonomy categories to a secondary navigation role.

### Phase 3 — Deep-reading surfaces

- update paper-note template;
- migrate current/high-priority paper notes first;
- remove public visual-pending prose;
- update digest landing.

### Phase 4 — Paper Index

- simplify generator output to compact chronology table;
- keep canonical determinism and `--check` behavior.

### Phase 5 — Maintenance contract

- update `docs/DAILY_WORKFLOW.md` with editorial quality gate;
- ensure scheduled task continues to invoke the versioned workflow rather than duplicating style rules in the automation prompt.

## 15. Success criteria

The redesign is successful when:

- the first screen looks like a serious research artifact, not an AI-product README;
- a researcher can identify the delta and evidence boundary of a new paper in under 20 seconds;
- What's Changing reads as interpretation, not an archive list;
- Research Map is organized first around research questions and falsifiable next evidence, not taxonomy labels;
- paper notes make causal attribution and lineage more prominent than generic summary;
- the paper index supports fast lookup at 100+ papers;
- visual-pending and maintenance state never appear on public research pages;
- the scheduled workflow preserves this aesthetic and information hierarchy over time;
- removing decoration does not remove evidence, disagreement, negative results, or useful research depth.

## 16. Editorial north star

When deciding between two public presentations, choose the one that makes a strong researcher think:

> **“This repository has a point of view, knows what the evidence does and does not establish, and saves me time understanding the field.”**

not:

> “This repository has many papers and a polished dashboard.”
