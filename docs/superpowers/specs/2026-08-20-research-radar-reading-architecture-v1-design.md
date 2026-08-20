# Research Radar Reading Architecture v1

Date: 2026-08-20

## Problem statement

Agentic RAG Radar already has strong paper notes, category arguments, and temporal compactions, but the root README still asks one surface to perform too many jobs: announce recent papers, teach the field, compare design alternatives, and expose evidence. Important content is therefore repeated, while newcomers encounter a fairly advanced field thesis before receiving a simple mental model.

This design makes the repository a layered research reading system. Canonical research judgment stays centralized; README, paper notes, category pages, the historical library, and compactions become distinct reading projections.

Scope: root README, paper-note editorial contract, historical navigation, category/field-map presentation, compactions, validation, and the recurring workflow that derives public surfaces.

Non-goals: GitHub Pages or a separate website; making the radar exhaustive; flattening all papers into one template; replacing full-paper reading; turning the README into a dashboard.

## Design principles

1. **Scan first, deepen in place.** Readers should see the current signal quickly, but high-value papers must expose a useful 60–90 second explanation directly from README.
2. **One claim, multiple projections.** Different surfaces add different compression or reasoning value; they do not repeat the same paragraph.
3. **Structure is stable; prose is not templated.** The reasoning sequence is standardized while sentence shapes remain natural to the paper.
4. **Time is a view, not the archive key.** Weekly/monthly/yearly explain change. Historical retrieval is organized by research problem, design line, and year.
5. **Compared to what is mandatory.** A method is not interesting in isolation; the reader must see the closest alternative, what changes, and what remains confounded.

## External writing basis

The design follows durable guidance from Google Technical Writing on audience fit, key points at the start, progressive disclosure, and concrete language; Microsoft’s “scanning first, reading second” principle; and NeurIPS checklist/reviewer guidance that claims, experimental support, assumptions, limitations, and significance relative to prior work should align.

Third-party writing skills are references, not runtime dependencies. Public examples such as `writing-clearly-and-concisely`, `ste-plain-writing`, and evidence-backed research-writing skills motivate the local editorial checks. The enforceable standard lives inside this repository.

## Reading architecture

```text
canonical record
  ├─ 30 sec: README scan row
  ├─ 60–90 sec: README fold for high-value work
  ├─ 5–10 min: paper note / evidence audit
  ├─ topic view: Research Library + category argument
  └─ time view: weekly → monthly → yearly compaction
```

The first page should let a reader move from unfamiliar to expert depth without forcing a page change at every step.

## README contract

Use this top-level order:

```text
Latest Papers
What’s Changing
Field Map
Reading Paths
Research Library / Browse All
How to Use This Radar
Scope / About / Contributing
```

Expose compact depth navigation near the title:

`30 sec: Latest · 5 min: Field Map · 15 min: Reading Paths · Browse All`

Before the advanced field thesis, give a one-line beginner mental model:

`need information → search/access evidence → inspect → decide whether/where to search again → answer or act`

Then explain the deeper current thesis: the key variables are where information/evidence is materialized, where adaptivity lives, what state persists, and which lifecycle resources are spent.

### Latest Papers

Keep roughly 6–8 high-signal entries. Visibility is earned by importance and field-map impact, not by filling a recency quota.

Each entry contains title, category/tags, date, importance, links, and one-sentence **Research delta** in the form `previous design → changed variable → consequence`.

Importance >= 4/5, or a paper that materially changes the field map, receives an inline `<details>` explainer. The fold should take roughly 60–90 seconds and cover these information points naturally:

- problem that survives the strongest existing design;
- what actually changed;
- execution/data/control flow;
- closest meaningful comparison;
- decisive evidence;
- strongest unresolved caveat.

Do not mechanically create six tiny headings and do not duplicate the paper note verbatim.

### What’s Changing

Lead with 2–4 field-level shifts using `older assumption → new evidence → research implication`. Weekly/monthly/yearly links follow as supporting temporal views rather than the main story.

### Field Map

Field Map comes before Reading Paths. Use a simple conceptual map first, then the current systems decomposition:

`information need → query/planning → retrieval interface → evidence materialization → inspection/reasoning → control/stop → persistent state → answer/action`

The current deeper axes should remain explicit:

`pre-query compilation ↔ query-time adaptation`

`pre-materialized index/chunks ↔ raw/query-conditioned evidence`

`stateless interaction ↔ persistent/recoverable state`

`local retrieval metric ↔ lifecycle cost / task outcome`

Category pages remain the argument layer for these tensions.

### Reading Paths

Keep three or four paths maximum. Each path begins with a research question and ends with what the reader should understand. Do not use paths as disguised chronological lists.

## Research Explainer Standard

High-visibility notes follow this reasoning contract:

1. **Research delta** — smallest claim that makes the paper worth opening.
2. **Problem** — what fails under the closest reasonable prior design.
3. **Mechanism** — real execution/data/control flow; module names are secondary.
4. **Closest comparison** — closest baseline, what is held fixed, what still changes together.
5. **Decisive evidence** — 1–3 results/ablations that should update belief.
6. **What remains unproven** — strongest alternative explanation, attribution gap, or budget mismatch.
7. **Field-map consequence** — which design axis or causal question changes.
8. **Related reading** — 2–4 papers chosen for contrast or continuation.

For Agentic RAG, add an **information/control placement** lens when useful: what is precomputed, what becomes observable only after evidence arrives, what state survives between actions, and where offline/online cost is paid.

Use wording that distinguishes paper-reported fact, curator interpretation, and open hypothesis.

## Editorial standard

Create a repository-local Research Radar Editor contract. Apply it to README, categories, notes, and compactions.

Preferred prose:

- active voice, concrete verbs, specific system objects;
- one main claim per paragraph and a strong first sentence;
- comparison before praise;
- exact numbers only when they alter interpretation;
- explicit negative results and mismatched-budget caveats;
- direct attribution language such as `the experiment supports the package more strongly than component X`.

Avoid recurring AI-house-style patterns:

- repeated openers like `the important/interesting/meaningful delta is not X`;
- generic praise (`important`, `significant`, `robust`, `powerful`, `novel`) without a comparison/evidence cue;
- decorative symmetry and forced three-part lists;
- vague abstractions when a concrete operation can be named;
- promotional adjectives, emoji-heavy headings, and conclusion paragraphs that merely restate the opening.

A deterministic editorial linter should warn on pattern density, not ban individual words. It should detect repeated sentence skeletons across recent notes, generic judgments with no nearby evidence/comparison, public-surface duplication, and structural drift.

## Research Library

Chronology remains useful, but old papers should be discoverable without knowing the month or week.

Maintain three historical entry points:

- **Browse by Problem** — Planning & Query Formulation; Retrieval Interface & Tool Use; Evidence Materialization; Iterative Reasoning & Verification; State/Memory; Learning & Optimization; Evaluation & Analysis.
- **Browse by Research Line / Design Tension** — e.g. fixed top-k → direct corpus interaction → persistent workspace → latent query-time localization; fixed retrieval policy → adaptive retrieval → progress-aware control; full context → compression → recoverable state.
- **Browse by Year** — compact chronological provenance index.

The existing canonical category index and generated chronological paper index should be reused rather than replaced. The Research Library is the navigation layer that connects them.

Weekly digests must never be the only route to a historical paper.

## Layer responsibilities

- `data/papers/*.json`: canonical metadata, identity, taxonomy, links, evidence/review state.
- `papers/*.md`: evidence layer; mechanism, comparison, evidence, caveats, field consequence.
- `categories/*.md`: argument layer; current design tensions and decisive experiments.
- Research Library/index: historical retrieval layer.
- `digests/*`: temporal synthesis layer.
- root README: judgment/router layer.

No paragraph should be copied unchanged across these surfaces.

## Maintenance workflow

Keep the scheduler thin and the repository contract authoritative.

Each run follows:

`preflight → discover → independent judgment → canonical update → evidence note → relationship/category update → derive reader projections → editorial review → validate → atomic canonical/Timeline/digest projection → material notification`

**No public operational run logs.** `runs/README.md` is static policy only. Accepted outcomes persist in the atomic canonical/Timeline/digest projection and Git commit history; operational traces remain only in ignored `.radar-private/` artifacts or ephemeral Agent memory.

A newly accepted paper does not automatically enter Reading Paths or change Field Map. Those surfaces update only when the research relationship changes.

README folds are reader-facing derived artifacts and may be rewritten for clarity without changing canonical facts.

## Validation

Extend existing validation with:

- README section order and latest-entry bounds;
- fold eligibility and information coverage for high-visibility papers;
- paper-note semantic contract without requiring exact headings;
- every README item resolves to canonical data and a note;
- every historical paper remains reachable through at least one Research Library route;
- no scheduler/schema/upload internals leak to public pages;
- rolling warnings for repeated lead-in phrases and sentence skeletons;
- high-similarity/duplicate paragraph warnings across README/category/note/compaction;
- all existing taxonomy, schema, links, visual, generated-index, and compaction checks remain valid.

Editorial lint is advisory unless a deterministic public contract is violated.

## Migration

1. Rebuild README around Latest → What’s Changing → Field Map → Reading Paths → Research Library.
2. Rewrite current Latest folds to be shorter, causal, and non-duplicative; preserve strong evidence and negative results.
3. Add Research Library navigation over existing categories, design tensions, and chronological paper index.
4. Add the local Research Radar Editor standard and editorial linter.
5. Update `docs/DAILY_WORKFLOW.md` and validation so future daily runs preserve the new architecture.
6. Backfill old high-importance notes only when they sit on a current Reading Path, research line, anchor, or field argument; do not churn the entire archive for cosmetic uniformity.

## Success criteria

A reader should be able to:

- understand what Agentic RAG means at a basic level before seeing advanced placement terminology;
- identify the current field thesis and top changes within 30 seconds;
- understand a high-value paper from README in 60–90 seconds;
- audit its evidence/caveats in one click;
- find old work by research problem or design line without knowing its date;
- read consecutive notes without a repetitive AI-generated house style.

The maintainer should be able to evolve the reading contract through repository files while the recurring scheduler remains short and stable.
