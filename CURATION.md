# Daily Curation Protocol

This repository is maintained as a **research radar**, not a keyword dump. Daily maintenance should optimize for **high recall during discovery, high precision at publication, and explicit skepticism before synthesis**.

## Independent roles

Each run should use independent parallel roles whenever the execution environment supports them. Roles should form judgments separately before the editor synthesizes them.

| Role | Responsibility | Failure it should prevent |
|---|---|---|
| **Discovery** | Search a broad overlapping recent window across arXiv and other high-signal scholarly sources; expand beyond the literal phrase `agentic RAG`. | Missing papers because authors use different terminology. |
| **Inclusion Judge & Taxonomy** | Decide whether retrieval is genuinely agent-controlled and assign the primary category + orthogonal tags. | Scope creep into ordinary RAG or generic agents. |
| **Research Reader** | Read deeply enough to identify the actual control loop, nearest design point, evidence, limitations, and the one mechanism worth teaching. | Abstract paraphrases masquerading as research analysis. |
| **Visual Explainer** | Convert the verified mechanism into one original GPT-image-gen teaching figure with an auditable grounding brief. | Decorative or paper-copy visuals that do not improve understanding. |
| **Evidence Auditor / Skeptical Reviewer** | Challenge inclusion, novelty, importance, baseline quality, matched budgets, unsupported claims, duplicate versions, links, and visual overstatement. Construct the strongest alternative explanation. | LLM agreement bias and inflated “agentic” causal claims. |
| **Research Editor** | Produce the final paper card / compaction only after seeing the independent judgments. | Verbosity, paper-by-paper concatenation, and conclusions without consequences. |

The skeptical role should not summarize the other roles. It should actively try to falsify the proposed interpretation.

## Discovery policy

Use an overlapping lookback window rather than a strict calendar-day query. Candidate queries should cover terms such as:

- agentic RAG / agentic retrieval / agentic search
- adaptive or active retrieval
- retrieval planning / query decomposition / query reformulation
- iterative search / interleaved retrieval and reasoning
- verifier- or critic-guided retrieval
- tool-using RAG / retrieval routing
- GraphRAG agents / graph retrieval agents
- retrieval policy learning / RL for retrieval
- agentic information seeking

Deduplicate by canonical paper identity (prefer arXiv ID when available), not title string alone.

## Inclusion gate

Ask four questions in order:

1. Is external retrieval/search/context acquisition a substantive component?
2. Does an agent/controller/policy materially control retrieval behavior?
3. Is that control part of the research contribution rather than implementation glue?
4. Compared with the nearest static/adaptive design point, is the claimed delta identifiable?

If (1)–(3) are not clearly yes, reject or hold for review. A paper can be highly relevant yet low importance.

## Analysis standard

For every accepted paper, record:

- **TL;DR** — one-sentence research delta.
- **Problem** — the concrete limitation in prior systems.
- **Core Idea** — the mechanism or abstraction introduced.
- **Agent Loop** — what the model observes, chooses, retrieves, updates, repeats, and how it stops.
- **Retrieval Design** — available operations, granularity, routing, state, and stopping behavior.
- **Compared to What** — nearest design points and the actual delta.
- **Evidence** — datasets, metrics, baselines, ablations, budgets, negative results, and what the experiments do *not* establish.
- **Why It Matters** — what research/system decision changes if the claim is true.
- **Limitations / Questions** — assumptions or missing tests that could change the conclusion.
- **AI Confidence** — high / medium / low.

Do not claim experimental superiority from an abstract alone. Set `provenance.full_text_checked` accurately.

## Causal-attribution checklist

Agentic RAG papers often change multiple variables at once. Before attributing a gain to an agent policy, explicitly ask whether it may instead come from:

`substrate × operation set × state × policy × budget × base model`

Useful checks include:

- same retrieval primitive, fixed vs adaptive policy;
- same calls/tokens/latency budget;
- explicit state vs raw history/reasoning trace;
- strong lexical/sparse as well as dense baselines;
- component ablations that isolate interface, state, routing, and learning.

Negative results and baseline reversals should be preserved because they often change the research conclusion more than another positive headline.

## GPT-image visual standard

Every accepted paper must have a `visual_explainer` contract in its canonical record and an auditable grounding brief under `assets/visuals/prompts/`.

**GPT-image-gen is the preferred renderer.** Follow [`VISUALS.md`](VISUALS.md): one visual, one research question; minimal image text; original conceptual explanation; no reproduction or stylistic copy of the paper figure.

The visual status is explicit:

- `pending` — research card + grounding brief exist; PNG still needs generation/commit;
- `needs_regeneration` — an old or newly-invalid visual should be replaced;
- `generated` — PNG exists and CI should require it.

The skeptical reviewer separately audits the figure: does it invent an edge, make causality look stronger than the evidence, hide a budget confound, or choose an unfair baseline? A beautiful misleading image is worse than no image.

Existing accepted papers with pending visuals are a **backfill queue** and take priority over decorative repo graphics.

## Scoring

`relevance ∈ [0,1]` measures topical fit. `importance ∈ {1,...,5}` measures estimated research significance.

- **5 — Field-shaping:** changes an abstraction, benchmark, or dominant research direction with unusually strong evidence.
- **4 — Important:** clear reusable idea or strong evidence likely to influence follow-up work.
- **3 — Solid:** meaningful contribution but narrower delta or evidence.
- **2 — Incremental:** valid but limited novelty, evidence, or scope.
- **1 — Peripheral:** included for completeness; little expected research impact.

Do not reward a paper for recency or fashionable naming.

## Update policy

Prefer small auditable changes on `main` when reliable. For every accepted paper:

1. create/update the canonical JSON record;
2. create/update the researcher-facing paper card;
3. create/update the visual grounding brief and generated asset status;
4. refresh README Latest/Notable views and the relevant research-problem category page when the field view changes;
5. propagate meaningful corrections upward into weekly/monthly compactions.

Each run also writes **one compact archival provenance log** under `runs/daily/YYYY/MM/DD.md`. The log records accepted/deferred candidates, meaningful corrections, visual/workflow status, and compaction actions. It must not repeat full paper notes or become another primary feed.

Never fabricate code/project links, benchmark results, full-text analysis, or visual components. See [`COMPACTION.md`](COMPACTION.md) for weekly/monthly synthesis and anti-summary-drift rules, and [`runs/README.md`](runs/README.md) for run-log retention.