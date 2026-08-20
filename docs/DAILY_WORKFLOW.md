# Daily Research-Maintenance Workflow

This is the authoritative orchestration contract for Agentic RAG Radar. The recurring scheduler should stay short and point here.

## Transaction

One run is one idempotent transaction:

`preflight → discover → independent judgment → canonical update → evidence note → relationship update → derive Chinese/English reader surfaces → editorial review → conditional synthesis/visual work → validate → log → notify only if material`

An empty discovery day is successful when the repository remains correct.

## 1. Preflight

Read `CURATION.md`, `COMPACTION.md`, `VISUALS.md`, `docs/EDITORIAL_STANDARD.md`, the current README pair, Research Library pair, taxonomy/schema, relevant categories/paper notes, and recent run logs.

Repair deterministic drift before adding work. Reader-surface drift is a correctness problem, but do not create changes merely because a scheduled run occurred.

## 2. Discovery and independent judgment

Use overlapping windows rather than strict day boundaries. Search beyond the literal phrase `agentic RAG`: adaptive/active retrieval, query formulation, direct corpus interaction, evidence localization, retrieval planning, search agents, deep research, verifier-guided retrieval, stateful search, GraphRAG agents, retrieval policy/RL, and adjacent information-seeking work.

When independent roles/subtasks are supported, separate:

- broad discovery;
- inclusion/taxonomy judgment;
- full-paper research analysis;
- skeptical evidence/baseline/resource review;
- reader-surface/editorial judgment.

Do not accept a paper to keep the feed busy. Relevance and importance are separate.

## 3. Canonical-first publication

For accepted work:

`canonical JSON → evidence note → category/research-line relationship → reader projections`

`data/papers/*.json` remains canonical. `papers/README.md` remains a compact generated chronology, not a prose surface.

Preserve negative results, matched-baseline weaknesses, resource mismatches, historical predecessors, and the strongest alternative explanation.

## 4. Research Explainer Standard

Current/high-visibility notes must resolve:

`Research delta → Problem → Mechanism → Closest comparison → Decisive evidence → What remains unproven → Field-map consequence → Related reading`

Use the information/control-placement lens where it helps: what is precomputed, what becomes observable after evidence arrives, what state persists, and where offline/online cost is paid.

## 5. Bilingual publication

Chinese is primary.

- `README.md` is Simplified Chinese default; `README.en.md` is the complete English counterpart.
- Research Library and current high-value public narrative should have both languages.
- A material interpretation correction updates both language variants in the same transaction.
- English is rewritten naturally from the same semantic judgment; it is not a shortened translation.
- Keep paper titles, benchmarks, metrics, model names, tool/protocol names, and canonical technical terms in English when useful for precision/search.

During migration, bilingual backfill priority is: current Latest/Reading Path papers → current category/field-map anchors → older high-importance notes. Do not rewrite the full archive for cosmetic uniformity.

## 6. README projection

Public order:

`Latest Papers → What’s Changing → Field Map → Reading Paths → Research Library → Scope / Maintenance`

Keep roughly 6–8 high-signal Latest entries. Importance >=4/5 or field-map-changing work may receive a causal evidence fold. The fold is a causal compression, not copied note prose.

Keep entry and navigation surfaces direct and list-like. Do not add reading-time promises, methodology manifestos, prose that merely restates an adjacent table, or identical label wrappers around every item. Name a fold by the mechanism, evidence, or limitation it contains.

Field Map changes only when a real design axis changes. Reading Paths change only when a better conceptual route becomes available.

## 7. Historical discoverability

Time is one view, not the archive key. Every durable/high-importance work should be reachable through at least one non-temporal route: research problem, research line/design tension, controlled tag, or curated index.

Weekly/monthly/yearly synthesis answers what changed; it must never be the only way to find old work.

## 8. Editorial review

Apply `docs/EDITORIAL_STANDARD.md` after the research judgment is stable. Review recent neighboring notes together so repeated sentence skeletons are visible. In Chinese, keep canonical names and standard acronyms where useful, but use Chinese sentence structure and watch especially for machine-translated English syntax and empty transitions.

Editorial lint should target pattern density, not ban individual words.

## 9. Visual isolation

Per-paper visuals remain isolated from the long maintenance context. A visual is research compression, not decoration. Follow `VISUALS.md`; do not expose incomplete rendering state on public pages.

## 10. Compaction gate

Update weekly/monthly/yearly synthesis only when a new paper/correction changes a field thesis, tension, evidence bar, or a period boundary requires a new artifact. Re-ground load-bearing claims in canonical records/full-text notes rather than recursively summarizing old digests.

## 11. Validation and log

Validate canonical/schema/visual state plus public reader contracts:

- Chinese default + English counterpart exist and cross-link;
- same Latest paper identities, importance, and primary links across languages;
- section order and Latest bounds are preserved;
- all current Latest items resolve to canonical records and notes;
- historical high-value work remains reachable outside weekly digests;
- no scheduler/schema/upload internals leak to public surfaces;
- bilingual high-visibility facts do not drift;
- generated paper index, taxonomy, links, and visual references remain consistent.

Write one compact provenance log at `runs/daily/YYYY/MM/DD.md`.

## Notification gate

Notify only for a newly accepted paper, meaningful correction/reclassification, field-level synthesis change, meaningful visual repair/backfill, or an exact blocker requiring attention. Otherwise finish silently.

## Scheduled cadence

The current recurring task runs Monday–Friday. Monday should use a wider discovery window to absorb weekend releases and indexing lag. Keep a single writer responsible for the transaction unless the repository architecture is deliberately redesigned for transactional concurrency.
