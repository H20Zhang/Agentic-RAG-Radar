# Polished Research Editorial Design

## Goal

Make Agentic RAG Radar visually polished enough that researchers can understand the research structure faster **without reducing research depth**.

The target is a **polished research editorial**: the clarity and restraint of a strong systems/ML paper, plus enough visual hierarchy, figures, icons, and editorial framing to make a GitHub research artifact inviting to read.

The governing rule is:

> **Visual polish up; research depth up; UI chrome down; repeated prose down.**

## Reader model

The repository serves four reading depths:

1. **10-second orientation** — what this field map is about and what changed recently.
2. **30-second paper verdict** — why a paper matters, strongest evidence, strongest caveat.
3. **3-minute understanding** — mechanism, nearest design point, evidence attribution, lineage.
4. **deep research note** — matched baselines, ablations, negative results, resource accounting, confounders, and the next decisive experiment.

Aesthetic simplification must never delete levels 3–4.

## Public-surface responsibilities

| Surface | Researcher job |
|---|---|
| `README.md` | Decide what deserves attention now |
| `README.md#whats-changing` | Understand what recent evidence means at week/month/year scales |
| `README.md#reading-paths` | Learn a research question through a deliberate sequence |
| `categories/README.md` | Build a mental model of the live research questions |
| `categories/*.md` | Follow one research argument and its unresolved evidence |
| `papers/README.md` | Find an accepted paper quickly |
| `papers/<id>.md` | Understand and assess one paper deeply |
| `digests/*` | Reconstruct field movement over time |

**README says what matters; synthesis says what it means; map says how to think; index says where to find; paper note says why to believe.**

## Visual language

The public surface should use visual structure aggressively but avoid product-dashboard aesthetics.

### Use

- original research overview diagrams;
- mechanism figures;
- evidence/failure diagrams;
- small restrained icons when they encode a stable concept;
- lineage strips;
- comparison/evidence tables;
- blockquotes/callouts for one high-value research judgment;
- whitespace and concise metadata lines.

### Avoid

- glossy cards;
- status pills;
- star-count badges;
- tag clouds;
- decorative banners;
- multi-color dashboards;
- visual maintenance state;
- repetitive emoji-heavy headings.

### Figure style

Figures should resemble a strong FAST/SOSP/OSDI/SIGMOD/NeurIPS overview figure: white/near-white background, restrained blue/teal/neutral palette, simple geometry, thin lines, 3–7 short labels, high information density, clear anchors for prose, and no invented mechanism or causal edge.

## Multiple-figure policy

More than one figure is encouraged when figures answer **different research questions**.

For an important method/system paper, prefer:

1. **Mechanism overview** — what observes/decides/retrieves/updates.
2. **Evidence or trade-off view** — what the strongest experiment actually establishes and where it does not.

For benchmark/analysis papers, prefer:

1. **Failure/causal decomposition**.
2. **Evaluation matrix / intervention map** when it improves causal understanding.

Do not create multiple decorative variants of the same mechanism. Every figure must eliminate meaningful prose or make a comparison faster to understand.

## Icon policy

Icons are navigation/semantic aids, not decoration. Use a small coherent vocabulary for recurring concepts such as:

- precompute/materialize;
- query-time adaptivity;
- state/retention;
- retrieval interface;
- learning;
- evaluation/causal attribution.

Prefer lightweight repository SVG assets with a shared visual grammar over unrelated emoji.

## README

### Opening

The first screen should contain:

- title without decorative robot emoji;
- one-sentence scope;
- current field thesis;
- compact navigation;
- one field-overview research diagram;
- beginning of Latest Papers.

Move the star CTA to About/Contributing.

### Latest Papers

Each latest paper uses a research-editorial block:

```text
### Short paper name — Full title
*date · area · Importance 4/5 · Full-text reviewed*

**Why it matters.** Smallest research delta.

**Key result.** Strongest evidence or intervention.

**The catch.** Strongest negative/confounder/boundary.

Paper · Deep research note

<details>
<summary>Research snapshot</summary>
Research question · mechanism · nearest design point · evidence & attribution · open question
</details>
```

Do not show code-style tag strings or star glyph ratings in the default scan.

### What's Changing

Show one current synthesis at each time scale:

| Horizon | Question | Current synthesis |
|---|---|---|
| This week | What new evidence changed the map? | one thesis |
| This month | What design space is emerging? | one thesis |
| 2026 YTD | What looks durable? | one thesis |

Link to the archive once.

### Reading Paths

Keep approximately three paths. Each is a research question, 3–5 papers, a deliberate order, and one sentence explaining the conceptual progression.

### Research Map on README

Use a compact preview of the live research questions and link to the full map. Do not duplicate the full taxonomy/category pages.

## Research Map

`categories/README.md` is research-question-first.

Recommended live questions:

1. Where should adaptivity live?
2. When should evidence be materialized?
3. What state should persist?
4. How should retrieval interfaces expose the corpus?
5. What should be learned?
6. What makes an evaluation causal?

For each: current view, key design points, strongest boundary/counterexample, and what would change our mind.

Canonical categories remain below as taxonomy/navigation rather than the primary mental model.

## Paper notes

Paper notes should remain deep and use layered reading.

### 30-second verdict

Immediately below metadata:

- TL;DR;
- **Why this paper matters**;
- **Strongest evidence**;
- **Biggest caveat**.

### Deep structure

Recommended sections:

- Research question
- Research delta
- Mechanism
- Evidence & attribution
- Where it fits
- Open question

Mechanism can contain agent loop, retrieval design, state progression, training trajectory, or failure map as appropriate. Do not force identical subheadings.

### Evidence & attribution

This is the intellectual center. Prefer a compact claim-evidence table when useful:

| Claim | Evidence | Closest control | Assessment |
|---|---|---|---|

Include matched baseline, key ablation/intervention, negative result, resource/harness/model confound, and what is actually identified causally.

### Where it fits

Use explicit lineages such as `SIRA → ReFind → LENS` or `S2G-RAG → RAAC → LoongReflect` when grounded.

### Visuals

If no validated generated visual exists, show **no visual placeholder/status prose**.

For important papers, multiple figures are allowed when each answers a different question. Generated visual blocks require `How to read this figure`, `Compared with`, and `Do not over-read`.

## Paper Index

The generated index is a compact lookup surface. Use chronology tables rather than multi-paragraph entries.

Recommended columns:

| Date | Paper | Area | Importance | Review |

Paper title links to the research note. External paper/code links can be compact inline links. Do not repeat research delta.

## Digest landing

`digests/README.md` is a synthesis archive with one-line theses. Explain weekly/monthly/yearly roles once; avoid mini-essay repetition for each file.

## Validator

Protect the reader contract without enforcing brittle Markdown formatting.

Enforce:

- first substantive section is Latest Papers;
- Latest cards include Why it matters / Key result / The catch;
- no `AI take` or star-glyph importance on primary surfaces;
- no public pending/backfill/renderer/scheduler state;
- paper notes do not display visual placeholder prose;
- generated figures include required reader explanation;
- Research Map is research-question-first;
- Paper Index is deterministic and compact;
- relative links resolve.

Do not enforce identical paper-note mechanism headings or fixed paragraph counts.

## Scheduled maintenance

`docs/DAILY_WORKFLOW.md` adds an editorial gate:

1. Can a researcher identify the delta, evidence, and caveat in <20 seconds?
2. Did the update add a research conclusion or only another item?
3. Did visual structure improve scan speed?
4. Is repeated metadata/prose serving distinct reader jobs?
5. Did any operational state leak publicly?
6. Did the page gain unnecessary badges/tags/chrome?
7. Would another figure explain the mechanism/evidence faster than prose?
8. If adding a figure, does it answer a distinct grounded research question?

Prefer no structural change over aesthetically degraded mechanical updates.

## Implementation scope

Use a short-lived PR and update the coherent reader surface together:

1. README + field-overview SVG + visual grammar.
2. Research Map + semantic SVG icon set.
3. Latest/current paper notes and paper template with deeper layered explanation.
4. Compact generated Paper Index.
5. Synthesis archive landing.
6. Validator + daily editorial gate.

Do not change canonical research claims merely for aesthetics.
