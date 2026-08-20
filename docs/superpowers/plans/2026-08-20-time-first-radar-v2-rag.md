# Agentic RAG Radar Time-First v2 Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Make Agentic RAG Radar a time-first, inline-expandable research radar whose Daily Scheduled Agent owns discovery through publication and period/map synthesis.

**Architecture:** Reuse the family protocol/parser from Benchmark Radar, retain RAG's rich canonical and visual systems, and change only the public projection and maintenance contract. Existing paper notes remain the evidence layer; Timeline is the compact scan/expand layer; period synthesis and the research-question map stay distinct.

**Tech Stack:** Markdown, Python 3.12, `unittest`, JSON Schema, Pillow, GitHub Actions.

**Spec:** `https://github.com/H20Zhang/Agent-Benchmark-Radar/blob/main/docs/superpowers/specs/2026-08-20-agent-maintained-time-first-radar-v2-design.md`

## Global Constraints

- Daily Scheduled Agent is the only writer; internal candidates and failures are not public inventory.
- Public order is `Latest Timeline → 7-day / 30-day synthesis → Field Map → Reading Paths → Library`.
- Timeline has no fixed item cap; every current record is a compact `<details>` disclosure.
- Current legacy cards use honest paper-date order; future cards use `radar_published_at` without overwriting research chronology.
- Strong retrieval claims separate evidence coverage, interface, harness, policy, model, state, and realized resources.
- A single work is at most `early_signal` unless independent evidence supports a durable map change.
- Preserve canonical paper records, paper-index generation, notes, visuals, taxonomy, and compactions.
- Chinese/English identity, dates/order, evidence scope, map status, and primary links remain paired.

---

### Task 1: Apply the v2 family contract to Agentic RAG Radar

**Files:**
- Create: `docs/RADAR_AGENT_PROTOCOL.md`
- Modify: `docs/DAILY_WORKFLOW.md`
- Modify: `CURATION.md`
- Modify: `COMPACTION.md`
- Modify: `data/paper.schema.json`
- Modify: `README.md`
- Modify: `README.en.md`
- Create: `scripts/timefirst_contract.py`
- Create: `tests/test_timefirst_contract.py`
- Modify: `scripts/validate_reading.py`
- Modify: `scripts/validate_public.py`
- Modify: `scripts/build_paper_index.py`
- Modify: `.github/workflows/validate.yml`

**Interfaces:**
- Consumes verbatim: shared protocol, parser, and generic parser fixtures from merged Benchmark v2.
- Stable aliases: `timeline`, `latest`, `latest-papers`, `periods`, `changes`, `whats-changing`, `last-7-days`, `last-30-days`, `field-map`, `research-map`, `reading-paths`, `library`.
- Routes evaluation intent to `Agent-Benchmark-Radar#benchmark-rag`.

- [ ] **Step 1: Copy generic validator/tests and verify RED**

Copy the merged Benchmark `scripts/timefirst_contract.py` and generic fixture tests without semantic changes. Add the real README-pair assertion:

```python
def test_repository_readmes_satisfy_contract(self):
    self.assertEqual([], validate_pair(
        (ROOT / "README.md").read_text(encoding="utf-8"),
        (ROOT / "README.en.md").read_text(encoding="utf-8"),
    ))
```

Run: `python -m unittest discover -s tests -v`

Expected: repository assertion fails on missing Timeline/period anchors and compact disclosures.

- [ ] **Step 2: Convert the six current cards into Timeline disclosures**

Co-locate `<a id="timeline"></a><a id="latest"></a><a id="latest-papers"></a>` before Timeline. Keep all six canonical identities and paper dates in descending order. Convert each current card to `entry-<arxiv-id>` plus one `<details>` summary with date, title, RAG problem/category, and current Research delta. The open body uses exact paired labels `问题/证据/限制/地图/链接` and `Question/Evidence/Caveat/Map/Links`, reusing the current mechanism, decisive evidence, negative boundary, cost, visual, paper, and note links. Use `early_signal` per record unless independent evidence in the current map justifies another token.

Add one migration notice: legacy cards are ordered by paper date because historic Radar acceptance timestamps were not stored; post-cutover cards use `radar_published_at`.

- [ ] **Step 3: Make the direction layer explicitly temporal**

Co-locate `<a id="periods"></a><a id="changes"></a><a id="whats-changing"></a>` after Timeline. Add:

- `last-7-days` with `2026-08-14—2026-08-20`;
- `last-30-days` with `2026-07-22—2026-08-20`.

Reuse the existing three strong direction judgments—evidence materialization, retained/progress state, and interface/harness controls—but identify which are `new_signal` or `reinforced`, list supporting record identities, confidence, and research-design implication. Keep direct links to current weekly/monthly/yearly compactions.

Co-locate `<a id="field-map"></a><a id="research-map"></a>` before the stable field map. Preserve Reading Paths and Library. Update top navigation to Timeline → periods → Field Map → paths → Library and point the evaluation route to `Agent-Benchmark-Radar#benchmark-rag`.

- [ ] **Step 4: Install shared protocol and RAG adapter**

Copy `docs/RADAR_AGENT_PROTOCOL.md` verbatim from Benchmark v2. Rewrite `docs/DAILY_WORKFLOW.md` as the RAG adapter: source lanes, identity/version gate, four scope questions, full-text evidence coverage, interface/harness/state/resource decomposition, skeptical audit, Timeline projection, period boundaries, map gate, visual isolation, bilingual atomicity, validation, and silent no-change exit.

Update `CURATION.md` and `COMPACTION.md` for agent-only normal operation, private candidates, non-recursive evidence, exact rolling/closed periods, and correction propagation.

Extend `data/paper.schema.json` (which has `additionalProperties: false`) with optional `published_at`, `first_seen_at`, `radar_published_at`, `time_provenance`, and enum `map_delta`. Do not bulk-fill legacy timestamps. Require `provenance.full_text_checked=true` only for new post-cutover map-eligible records; preserve validity of existing records.

- [ ] **Step 5: Update every public validator/generator and verify GREEN**

Make `scripts/validate_reading.py` call shared `validate_pair` and remove its `6–8` cap. Update `scripts/validate_public.py` to recognize `entry-*` Timeline disclosures and the new H2 order instead of its stale English-only `Latest Papers/What's Changing/Reading Paths/Research Map` assumptions; keep canonical note, visual, map, and link checks. Update `scripts/build_paper_index.py` navigation links to standard `#timeline/#periods/#reading-paths/#field-map` anchors.

Update `.github/workflows/validate.yml` to run unit tests and `validate_public.py` after existing checks. Run:

```bash
python -m unittest discover -s tests -v
python scripts/build_paper_index.py
python scripts/build_paper_index.py --check
python scripts/validate.py
python scripts/validate_reading.py
python scripts/validate_public.py
```

Expected: generated index is byte-stable; all tests and validators exit 0 with pristine output.

- [ ] **Step 6: Self-review and commit**

Check current identities/visuals/notes remain reachable; no fixed cap or public candidate state remains; every disclosure has the five semantic fields; period windows and map tokens match across languages; all generated navigation uses stable anchors; no component gain is attributed through an unmatched interface/harness.

Commit:

```bash
git add docs/superpowers/plans/2026-08-20-time-first-radar-v2-rag.md docs/RADAR_AGENT_PROTOCOL.md docs/DAILY_WORKFLOW.md CURATION.md COMPACTION.md data/paper.schema.json README.md README.en.md scripts/timefirst_contract.py tests/test_timefirst_contract.py scripts/validate_reading.py scripts/validate_public.py scripts/build_paper_index.py papers/README.md .github/workflows/validate.yml
git commit -m "Add agent-maintained time-first RAG radar"
```
