# Repository Discoverability and Contribution Design

## Goal

Improve the repository's research-facing growth loop without weakening its skeptical curation standard:

`discover → understand value quickly → star/return → suggest high-quality papers`

The optimization should increase qualified discovery and retention, not maximize raw clicks.

## Non-goals

- No decorative badge wall, star-count badge, visitor counter, or vanity metrics.
- No keyword-stuffed README or broad "awesome list" positioning.
- No change to inclusion criteria, taxonomy, paper ranking, or compaction logic.
- No automatic license choice or citation metadata solely for cosmetic completeness.
- No operational/scheduler details on the public README.

## 1. GitHub metadata

Use the following repository description when the GitHub integration exposes a repository-metadata mutation:

> A living research radar for Agentic RAG — latest papers, adaptive retrieval & search agents, skeptical notes, and field-level synthesis.

Recommended topics:

- `agentic-rag`
- `retrieval-augmented-generation`
- `rag`
- `ai-agents`
- `llm-agents`
- `adaptive-retrieval`
- `search-agents`
- `information-retrieval`
- `research-papers`

Do not add narrower topics such as `graphrag` or `deep-research` unless the repository's durable scope shifts toward them.

## 2. README conversion surface

Keep **Latest Papers** as the first substantive section.

Immediately after the existing one-paragraph repository description, add one restrained CTA:

> ⭐ **Star this repo to follow new Agentic RAG papers, skeptical research notes, and field-level synthesis.**

The CTA must remain a single line and must not become its own section. It should not interrupt the existing navigation or current-field-thesis flow.

At the end of README, add one low-friction contribution prompt linking to the paper-suggestion issue template:

> Found an important Agentic RAG paper we missed? [Suggest it](../../issues/new?template=suggest-paper.yml).

Use a repository-relative GitHub issue-template link that works from the README on GitHub; verify the final URL behavior after commit and adjust if needed.

## 3. Paper suggestion issue template

Create `.github/ISSUE_TEMPLATE/suggest-paper.yml` as a GitHub issue form.

The form should require:

- paper title;
- paper URL;
- publication/preprint date if known;
- why external retrieval/search/context acquisition is substantive;
- what the agent/controller materially controls: whether / what / where / how / how many times to retrieve;
- nearest baseline or prior design point;
- submitter's view of the paper's key research delta.

Optional fields may include code/project URL and a short note on negative results/confounders.

The form itself should state that fixed top-k RAG and generic agents with incidental retrieval are usually out of scope. This protects the repository from becoming a generic RAG submission inbox.

## 4. CONTRIBUTING.md

Create a compact researcher-facing `CONTRIBUTING.md` with three purposes:

1. explain what kinds of papers belong in the radar;
2. explain how to suggest a paper or correction;
3. explain the evidence standard for accepted claims.

It should explicitly welcome:

- missed papers that materially change the field map;
- corrections to taxonomy, links, benchmark numbers, or duplicate versions;
- negative results and causal confounders;
- stronger historical or matched baselines.

It should explicitly reject:

- fixed top-k RAG with no meaningful retrieval control;
- generic agents where retrieval is incidental;
- promotional submissions whose evidence cannot be checked.

Keep it concise and research-facing; do not expose scheduler mechanics, internal agent roles, prompt mechanics, or maintenance provenance.

## 5. Public-surface constraints

README remains a lightweight living survey, not a project-operations dashboard.

The new CTA and contribution prompt must satisfy the same test as all README edits: do they help a researcher understand the repository's value or contribute a materially relevant paper/correction? If not, they do not belong there.

No star counters, visitor counters, CI badges, backfill status, or generation-state badges should be added to the README header.

## 6. Validation

Before finishing:

- verify README still has **Latest Papers** as its first substantive section;
- verify the CTA appears once and does not crowd the header;
- verify `CONTRIBUTING.md` and `.github/ISSUE_TEMPLATE/suggest-paper.yml` exist;
- verify the issue-form YAML is syntactically valid enough for GitHub's issue-form schema;
- verify README links to the suggestion flow correctly;
- run/reason against the repository's existing validation contract and avoid touching canonical research records unnecessarily.

## Success criteria

The change is complete when a new visitor can answer, within seconds:

1. what this repository gives them;
2. why it is worth following rather than treating it as another paper list;
3. how to submit a high-quality missed paper or correction;

while the repository still reads first as a research artifact, not a growth-optimized product page.
