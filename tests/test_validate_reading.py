from copy import deepcopy
import json
from pathlib import Path
import re
import sys
import unittest


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import validate_reading
import validate_public


def repository_inputs() -> tuple[str, str, list[dict[str, object]]]:
    zh = (ROOT / "README.md").read_text(encoding="utf-8")
    en = (ROOT / "README.en.md").read_text(encoding="utf-8")
    records = [
        json.loads(path.read_text(encoding="utf-8"))
        for path in sorted((ROOT / "data" / "papers").glob("*.json"))
    ]
    return zh, en, records


def native_record(
    identity: str,
    radar_time: str,
    map_delta: str = "early_signal",
    *,
    direction_keys: tuple[str, ...] = ("rag-native-signal",),
) -> dict[str, object]:
    return {
        "id": f"arxiv:{identity}",
        "arxiv_id": identity,
        "published": "2026-08-01",
        "published_at": "2026-08-01T00:00:00Z",
        "first_seen_at": "2026-08-19T00:00:00Z",
        "radar_published_at": radar_time,
        "time_provenance": "native_v2",
        "map_delta": map_delta,
        "direction_keys": list(direction_keys),
        "urls": {"paper": f"https://arxiv.org/abs/{identity}"},
        "provenance": {"full_text_checked": True},
    }


def english_direction(
    *, state: str = "new_signal", supports: tuple[str, ...] = ("2608.90001",),
    map_key: str = "rag-native-signal", prior: str = "none",
) -> str:
    support_value = ",".join(supports) if supports else "none"
    visible = " · ".join(f"[{item}](#entry-{item})" for item in supports) or "**none**"
    heading = "RAG native signal" if map_key == "rag-native-signal" else map_key.replace("-", " ")
    return (
        f'- **`{state}` · {heading}.** '
        f'<!-- timefirst:direction key="{map_key}" state="{state}" supports="{support_value}" '
        'confidence="high" implication="require-native-v2-times-for-period-claims" '
        f'timing="radar_published_at" synthesized="2026-08-26T01:35:00Z" prior="{prior}" -->\n'
        f'  Supports: {visible}; confidence: **high**; timing basis: `radar_published_at`; '
        'Exact synthesis time: `2026-08-26T01:35:00Z` (UTC); Research-design implication '
        '(require native v2 times for period claims): native acceptance controls the window; '
        f'prior map evidence: {"[Field Map](#field-map)" if prior == "field-map" else "`none`"}.'
    )


class RagTimelineAdapterTest(unittest.TestCase):
    def test_only_fixed_timeline_records_are_explicitly_migrated(self):
        _, _, records = repository_inputs()
        migrated = {
            record.get("arxiv_id")
            for record in records
            if record.get("time_provenance") == "legacy_unknown"
        }
        self.assertEqual(set(validate_reading.LEGACY_TIMELINE_COMPATIBILITY_IDS), migrated)
        for record in records:
            if record.get("arxiv_id") in migrated:
                self.assertEqual(record["published"], record["published_at"])
                self.assertIsNone(record["first_seen_at"])
                self.assertIsNone(record["radar_published_at"])
                self.assertNotIn("direction_keys", record)

    def test_rag_aliases_are_visible_comment_safe_and_unique(self):
        zh, en, _ = repository_inputs()
        self.assertEqual([], validate_reading.validate_rag_aliases(zh, en))
        for alias in validate_reading.RAG_ALIASES:
            anchor = f'<a id="{alias}"></a>'
            with self.subTest(alias=alias, mutation="hidden"):
                errors = validate_reading.validate_rag_aliases(
                    zh.replace(anchor, f"<!-- {anchor} -->", 1), en
                )
                self.assertTrue(any("missing RAG compatibility alias" in error for error in errors), errors)
            with self.subTest(alias=alias, mutation="duplicate"):
                errors = validate_reading.validate_rag_aliases(
                    zh.replace(anchor, anchor + anchor, 1), en
                )
                self.assertTrue(any("duplicate RAG compatibility alias" in error for error in errors), errors)

    def test_comment_hidden_benchmark_rag_route_is_rejected(self):
        zh, _, _ = repository_inputs()
        route = validate_reading.FAMILY_ROUTES["Agentic RAG evaluation"]
        mutated = zh.replace(f"]({route})", f"](https://example.com/wrong)\n<!-- [decoy]({route}) -->", 1)
        errors: list[str] = []
        validate_reading.family_routes(mutated, "README.md", errors)
        self.assertTrue(any("Agentic RAG evaluation" in error for error in errors), errors)

    def test_visible_family_routes_have_exact_cardinality(self):
        zh, _, _ = repository_inputs()
        route = validate_reading.FAMILY_ROUTES["Agentic RAG evaluation"]
        duplicated = zh + f"\n[duplicate evaluation route]({route})\n"
        errors: list[str] = []
        validate_reading.family_routes(duplicated, "README.md", errors)
        self.assertTrue(any("exactly one canonical Agentic RAG evaluation" in error for error in errors), errors)

    def test_repository_periods_are_structured_by_radar_acceptance(self):
        zh, en, records = repository_inputs()
        errors = validate_reading.validate_rag_timeline(zh, en, records)
        self.assertEqual([], errors)
        for text in (zh, en):
            periods = text[text.index('<a id="periods"></a>'):text.index('<a id="field-map"></a>')]
            self.assertEqual(4, periods.count('state="reinforced"'))
            self.assertEqual(28, periods.count('state="new_signal"'))
            self.assertEqual(2, periods.count('supports="2608.17889,2608.18613"'))
            self.assertRegex(periods, r"\(#entry-2608\.")

    def test_legacy_record_cannot_support_a_rolling_direction(self):
        zh, en, records = repository_inputs()
        for language, text in (("zh", zh), ("en", en)):
            if language == "zh":
                old = "支撑：[D2-ScaleAgent](#entry-2608.16417)；"
                new = "支撑：[LENS](#entry-2608.16185)；"
            else:
                old = "Supports: [D2-ScaleAgent](#entry-2608.16417);"
                new = "Supports: [LENS](#entry-2608.16185);"
            mutated = text.replace(old, new, 1).replace(
                'supports="2608.16417"', 'supports="2608.16185"', 1
            )
            errors = validate_reading.validate_rag_timeline(
                mutated if language == "zh" else zh,
                mutated if language == "en" else en,
                records,
            )
            self.assertTrue(any("legacy context is not support" in error for error in errors), errors)

    def test_direction_metadata_can_live_on_continuation_but_duplicate_is_rejected(self):
        zh, en, records = repository_inputs()
        marker = "<!-- timefirst:direction"
        start = zh.index(marker)
        end = zh.index("-->", start) + 3
        metadata = zh[start:end]
        moved = zh[:start] + "\n  " + metadata + zh[end:]
        self.assertEqual([], validate_reading.validate_rag_timeline(moved, en, records))
        duplicated = zh[:end] + "\n  " + metadata + zh[end:]
        errors = validate_reading.validate_rag_timeline(duplicated, en, records)
        self.assertTrue(any("exactly one stable direction metadata block" in error for error in errors), errors)

    def test_orphan_direction_metadata_before_visible_item_is_rejected_in_both_languages(self):
        zh, en, records = repository_inputs()
        for language, text in (("README.md", zh), ("README.en.md", en)):
            with self.subTest(language=language):
                section = validate_reading._section(text, "last-7-days", "last-30-days")
                self.assertIsNotNone(section)
                assert section is not None
                metadata = validate_reading.DIRECTION_COMMENT_RE.search(section)
                self.assertIsNotNone(metadata)
                assert metadata is not None
                mutated = metadata.group(0) + "\n" + section
                errors: list[str] = []
                validate_reading._parse_direction_items(
                    language,
                    "last-7-days",
                    mutated,
                    validate_reading.EXPECTED_PERIOD_WINDOWS["last-7-days"],
                    records,
                    errors,
                )
                self.assertTrue(any("orphan" in error.lower() for error in errors), errors)

    def test_duplicate_visible_direction_field_is_rejected(self):
        zh, en, records = repository_inputs()
        mutated = en.replace("Supports:", "Supports: Aside Supports:", 1)
        errors = validate_reading.validate_rag_timeline(zh, mutated, records)
        self.assertTrue(any("exactly one visible supports" in error for error in errors), errors)

    def test_emphasis_split_visible_labels_cannot_bypass_cardinality(self):
        zh, en, records = repository_inputs()
        cases = (
            ("README.en.md", en.replace(
                "confidence: **medium**;",
                "confidence: **medium**; Aside confi**dence**: **low**;",
                1,
            )),
            ("README.md", zh.replace(
                "置信度：**medium**；",
                "置信度：**medium**；旁注：置信**度**：**low**；",
                1,
            )),
        )
        for language, mutated in cases:
            with self.subTest(language=language):
                errors = validate_reading.validate_rag_timeline(
                    mutated if language == "README.md" else zh,
                    mutated if language == "README.en.md" else en,
                    records,
                )
                self.assertTrue(
                    any("exactly one visible confidence" in error for error in errors),
                    errors,
                )

    def test_emphasis_split_state_cannot_hide_a_second_visible_state(self):
        zh, en, records = repository_inputs()
        cases = (
            ("README.en.md", en.replace(
                '<a id="last-30-days"></a>',
                "  Aside: **`rein**forced**` · durable claim.**\n\n"
                '<a id="last-30-days"></a>',
                1,
            )),
            ("README.md", zh.replace(
                '<a id="last-30-days"></a>',
                "  旁注：**`rein**forced**` · 已确立方向。**\n\n"
                '<a id="last-30-days"></a>',
                1,
            )),
        )
        for language, mutated in cases:
            with self.subTest(language=language):
                errors = validate_reading.validate_rag_timeline(
                    mutated if language == "README.md" else zh,
                    mutated if language == "README.en.md" else en,
                    records,
                )
                self.assertTrue(
                    any("exactly one visible state" in error for error in errors),
                    errors,
                )

    def test_zero_support_direction_rejects_durable_claims_anywhere_in_block(self):
        zh, en, records = repository_inputs()
        cases = (
            ("README.en.md", en.replace(
                '<a id="last-30-days"></a>',
                "  This is an established durable trend.\n\n"
                '<a id="last-30-days"></a>',
                1,
            )),
            ("README.md", zh.replace(
                '<a id="last-30-days"></a>',
                "  这是已确立并强化的趋势。\n\n"
                '<a id="last-30-days"></a>',
                1,
            )),
        )
        for language, mutated in cases:
            with self.subTest(language=language):
                errors = validate_reading.validate_rag_timeline(
                    mutated if language == "README.md" else zh,
                    mutated if language == "README.en.md" else en,
                    records,
                )
                self.assertTrue(
                    any("fewer than two" in error for error in errors),
                    errors,
                )

    def test_low_support_claim_scan_ignores_markdown_link_and_image_destinations(self):
        zh, en, records = repository_inputs()
        cases = (
            (
                "README.en.md",
                en.replace(
                    '<a id="last-30-days"></a>',
                    "  [background **evidence**](https://example.com/durable-(systems) "
                    '"established trend") and '
                    "![architecture](https://example.com/reinforced-system.png "
                    '"trend diagram").\n\n'
                    '<a id="last-30-days"></a>',
                    1,
                ),
            ),
            (
                "README.md",
                zh.replace(
                    '<a id="last-30-days"></a>',
                    "  [背景证据](https://example.com/趋势 \"已确立趋势\")与"
                    "![架构](https://example.com/强化.png \"趋势图\")。\n\n"
                    '<a id="last-30-days"></a>',
                    1,
                ),
            ),
        )
        for language, mutated in cases:
            with self.subTest(language=language):
                errors = validate_reading.validate_rag_timeline(
                    mutated if language == "README.md" else zh,
                    mutated if language == "README.en.md" else en,
                    records,
                )
                self.assertFalse(
                    any("fewer than two" in error for error in errors),
                    errors,
                )

    def test_low_support_claim_scan_distinguishes_url_quotes_from_link_titles(self):
        zh, en, records = repository_inputs()
        links = (
            "[background](https://example.com/it's-a-durable-link)",
            '[background](https://example.com/a-"durable"-link)',
            r'[background](https://example.com/a-\"durable\"-link)',
            "[background](https://example.com/it's-a-(durable)-link "
            "'established trend')",
        )
        for link in links:
            with self.subTest(link=link):
                mutated = en.replace(
                    '<a id="last-30-days"></a>',
                    f"  {link}.\n\n<a id=\"last-30-days\"></a>",
                    1,
                )
                errors = validate_reading.validate_rag_timeline(
                    zh,
                    mutated,
                    records,
                )
                self.assertFalse(
                    any("fewer than two" in error for error in errors),
                    errors,
                )

    def test_low_support_claim_scan_keeps_visible_link_labels_and_image_alt_text(self):
        zh, en, records = repository_inputs()
        cases = (
            (
                "README.en.md",
                en.replace(
                    '<a id="last-30-days"></a>',
                    "  [durable trend](https://example.com/background).\n\n"
                    '<a id="last-30-days"></a>',
                    1,
                ),
            ),
            (
                "README.md",
                zh.replace(
                    '<a id="last-30-days"></a>',
                    "  ![已确立趋势](https://example.com/background.png)。\n\n"
                    '<a id="last-30-days"></a>',
                    1,
                ),
            ),
        )
        for language, mutated in cases:
            with self.subTest(language=language):
                errors = validate_reading.validate_rag_timeline(
                    mutated if language == "README.md" else zh,
                    mutated if language == "README.en.md" else en,
                    records,
                )
                self.assertTrue(
                    any("fewer than two" in error for error in errors),
                    errors,
                )

    def test_repository_entries_resolve_to_full_text_canonical_records_and_note_pairs(self):
        zh, en, records = repository_inputs()
        self.assertEqual([], validate_reading.validate_rag_timeline(zh, en, records))

    def test_missing_chinese_deep_note_link_is_rejected(self):
        zh, en, records = repository_inputs()
        target = " · [中文深读](papers/2608.16185.zh.md)"
        zh = zh.replace(target, "", 1)
        en = en.replace(target.replace("中文深读", "Chinese deep note"), "", 1)
        errors = validate_reading.validate_rag_timeline(zh, en, records)
        self.assertTrue(any("2608.16185" in error and "deep-note" in error for error in errors))

    def test_mismatched_deep_note_identity_is_rejected(self):
        zh, en, records = repository_inputs()
        zh = zh.replace("papers/2608.16185.zh.md", "papers/2608.16370.zh.md", 1)
        errors = validate_reading.validate_rag_timeline(zh, en, records)
        self.assertTrue(any("2608.16185" in error and "correspond" in error for error in errors))

    def test_entry_without_full_text_provenance_is_rejected(self):
        zh, en, records = repository_inputs()
        mutated = deepcopy(records)
        record = next(item for item in mutated if item.get("arxiv_id") == "2608.16185")
        record["provenance"]["full_text_checked"] = False
        errors = validate_reading.validate_rag_timeline(zh, en, mutated)
        self.assertTrue(any("2608.16185" in error and "full_text_checked" in error for error in errors))

    def test_visible_map_status_must_match_canonical_record(self):
        zh, en, records = repository_inputs()
        mutated = deepcopy(records)
        record = next(item for item in mutated if item.get("arxiv_id") == "2608.16185")
        record["map_delta"] = "none"
        errors = validate_reading.validate_rag_timeline(zh, en, mutated)
        self.assertTrue(any("2608.16185" in error and "map_delta" in error for error in errors))

    def test_seven_day_synthesis_rejects_out_of_window_support(self):
        records = [native_record("2608.90001", "2026-08-13T23:59:59Z")]
        errors: list[str] = []
        validate_reading._parse_direction_items(
            "README.en.md", "last-7-days", english_direction(),
            validate_reading.EXPECTED_PERIOD_WINDOWS["last-7-days"], records, errors,
        )
        self.assertTrue(any("last-7-days" in error and "2608.90001" in error for error in errors), errors)

    def test_post_cutover_entry_displays_radar_publication_date(self):
        zh, en, records = repository_inputs()
        mutated = deepcopy(records)
        record = next(item for item in mutated if item.get("arxiv_id") == "2608.16185")
        record.update(
            published_at="2026-08-17T00:00:00Z",
            first_seen_at="2026-08-18T00:00:00Z",
            radar_published_at="2026-08-20T01:00:00Z",
            time_provenance="native_v2",
        )
        errors = validate_reading.validate_rag_timeline(zh, en, mutated)
        self.assertTrue(any("2608.16185" in error and "displayed date" in error for error in errors))

    def test_in_window_post_cutover_canonical_record_cannot_be_omitted(self):
        zh, en, records = repository_inputs()
        synthetic = deepcopy(records[0])
        synthetic.update(
            id="arxiv:2608.99999",
            arxiv_id="2608.99999",
            title="Synthetic post-cutover record",
            published="2026-08-19",
            published_at="2026-08-19T00:00:00Z",
            first_seen_at="2026-08-20T00:15:00Z",
            radar_published_at="2026-08-19T03:00:00Z",
            time_provenance="native_v2",
            map_delta="early_signal",
        )
        synthetic["provenance"]["full_text_checked"] = True
        errors = validate_reading.validate_rag_timeline(zh, en, records + [synthetic])
        self.assertTrue(any("2608.99999" in error and "missing from timeline" in error.lower() for error in errors))

    def test_same_day_post_cutover_records_use_full_timestamp_order(self):
        zh, en, records = repository_inputs()
        mutated = deepcopy(records)
        lens = next(item for item in mutated if item.get("arxiv_id") == "2608.16185")
        compression = next(item for item in mutated if item.get("arxiv_id") == "2608.16370")
        for record, stamp in (
            (lens, "2026-08-19T01:00:00Z"),
            (compression, "2026-08-19T02:00:00Z"),
        ):
            record.update(
                published_at="2026-08-17T00:00:00Z",
                first_seen_at="2026-08-20T00:30:00Z",
                radar_published_at=stamp,
                time_provenance="native_v2",
            )
        errors = validate_reading.validate_rag_timeline(zh, en, mutated)
        self.assertTrue(any("timestamp order" in error.lower() for error in errors), errors)

    def test_repository_direction_items_are_bilingually_paired(self):
        zh, en, records = repository_inputs()
        errors = validate_reading.validate_rag_timeline(zh, en, records)
        self.assertFalse(any("direction" in error.lower() for error in errors), errors)

    def test_one_paper_cannot_be_labeled_reinforced(self):
        records = [native_record("2608.90001", "2026-08-19T01:00:00Z", "reinforces")]
        errors: list[str] = []
        section = english_direction(state="reinforced", prior="field-map")
        validate_reading._parse_direction_items(
            "README.en.md", "last-30-days", section,
            validate_reading.EXPECTED_PERIOD_WINDOWS["last-30-days"], records, errors,
        )
        self.assertTrue(any("reinforced" in error and "two distinct" in error for error in errors))

    def test_direction_support_regrouping_between_languages_is_rejected(self):
        zh, en, records = repository_inputs()
        en = en.replace('state="reinforced"', 'state="revised"', 1)
        en = en.replace("`reinforced`", "`revised`", 1)
        errors = validate_reading.validate_rag_timeline(zh, en, records)
        self.assertTrue(any("direction parity" in error.lower() for error in errors), errors)

    def test_duplicate_direction_support_is_rejected(self):
        records = [native_record("2608.90001", "2026-08-19T01:00:00Z")]
        errors: list[str] = []
        section = english_direction(supports=("2608.90001", "2608.90001"))
        validate_reading._parse_direction_items(
            "README.en.md", "last-30-days", section,
            validate_reading.EXPECTED_PERIOD_WINDOWS["last-30-days"], records, errors,
        )
        self.assertTrue(any("duplicate support" in error.lower() for error in errors))

    def test_support_order_is_preserved_between_metadata_and_visible_field(self):
        records = [
            native_record("2608.90001", "2026-08-19T01:00:00Z"),
            native_record("2608.90002", "2026-08-19T02:00:00Z", "reinforces"),
        ]
        section = english_direction(
            state="reinforced", supports=("2608.90002", "2608.90001"), prior="field-map"
        ).replace(
            "[2608.90002](#entry-2608.90002) · [2608.90001](#entry-2608.90001)",
            "[2608.90001](#entry-2608.90001) · [2608.90002](#entry-2608.90002)",
        )
        errors: list[str] = []
        validate_reading._parse_direction_items(
            "README.en.md", "last-30-days", section,
            validate_reading.EXPECTED_PERIOD_WINDOWS["last-30-days"], records, errors,
        )
        self.assertTrue(any("support order" in error for error in errors), errors)

    def test_support_after_synthesis_cutoff_is_rejected(self):
        records = [native_record("2608.90001", "2026-08-26T01:35:01Z")]
        errors: list[str] = []
        validate_reading._parse_direction_items(
            "README.en.md", "last-7-days", english_direction(),
            validate_reading.EXPECTED_PERIOD_WINDOWS["last-7-days"], records, errors,
        )
        self.assertTrue(any("accepted after direction synthesized" in error for error in errors), errors)

    def test_new_signal_requires_early_signal_map_delta(self):
        records = [native_record("2608.90001", "2026-08-19T01:00:00Z", "reinforces")]
        errors: list[str] = []
        validate_reading._parse_direction_items(
            "README.en.md", "last-30-days", english_direction(),
            validate_reading.EXPECTED_PERIOD_WINDOWS["last-30-days"], records, errors,
        )
        self.assertTrue(any("map_delta=early_signal" in error for error in errors), errors)

    def test_durable_direction_requires_prior_field_map_evidence(self):
        records = [
            native_record("2608.90001", "2026-08-19T01:00:00Z"),
            native_record("2608.90002", "2026-08-19T02:00:00Z", "reinforces"),
        ]
        errors: list[str] = []
        validate_reading._parse_direction_items(
            "README.en.md", "last-30-days",
            english_direction(state="reinforced", supports=("2608.90002", "2608.90001")),
            validate_reading.EXPECTED_PERIOD_WINDOWS["last-30-days"], records, errors,
        )
        self.assertTrue(any("independent prior Field Map" in error for error in errors), errors)

    def test_period_supports_must_carry_the_exact_direction_key(self):
        direction_key = "rag-shared-direction"
        records = [
            native_record(
                "2608.90001",
                "2026-08-19T01:00:00Z",
                direction_keys=(direction_key,),
            ),
            native_record(
                "2608.90002",
                "2026-08-19T02:00:00Z",
                "reinforces",
                direction_keys=("rag-other-direction",),
            ),
        ]
        errors: list[str] = []
        validate_reading._parse_direction_items(
            "README.en.md",
            "last-30-days",
            english_direction(
                state="reinforced",
                supports=("2608.90001", "2608.90002"),
                map_key=direction_key,
                prior="field-map",
            ),
            validate_reading.EXPECTED_PERIOD_WINDOWS["last-30-days"],
            records,
            errors,
        )
        self.assertTrue(
            any(
                "2608.90002" in error
                and "direction_keys" in error
                and direction_key in error
                for error in errors
            ),
            errors,
        )

    def test_period_supports_with_the_same_direction_key_pass(self):
        direction_key = "rag-shared-direction"
        records = [
            native_record(
                "2608.90001",
                "2026-08-19T01:00:00Z",
                direction_keys=(direction_key,),
            ),
            native_record(
                "2608.90002",
                "2026-08-19T02:00:00Z",
                "reinforces",
                direction_keys=(direction_key,),
            ),
        ]
        errors: list[str] = []
        validate_reading._parse_direction_items(
            "README.en.md",
            "last-30-days",
            english_direction(
                state="reinforced",
                supports=("2608.90001", "2608.90002"),
                map_key=direction_key,
                prior="field-map",
            ),
            validate_reading.EXPECTED_PERIOD_WINDOWS["last-30-days"],
            records,
            errors,
        )
        self.assertEqual([], errors)

    def test_split_and_retirement_directions_with_bound_map_evidence_pass(self):
        for state in ("splits", "retires"):
            with self.subTest(state=state):
                direction_key = f"rag-{state}-direction"
                records = [
                    native_record(
                        "2608.90001",
                        "2026-08-19T01:00:00Z",
                        state,
                        direction_keys=(direction_key,),
                    )
                ]
                errors: list[str] = []
                items = validate_reading._parse_direction_items(
                    "README.en.md",
                    "last-30-days",
                    english_direction(
                        state=state,
                        supports=("2608.90001",),
                        map_key=direction_key,
                        prior="field-map",
                    ),
                    validate_reading.EXPECTED_PERIOD_WINDOWS["last-30-days"],
                    records,
                    errors,
                )

                self.assertEqual([], errors)
                self.assertEqual(state, items[0][1])

    def test_split_and_retirement_direction_gates_reject_invalid_evidence(self):
        for state in ("splits", "retires"):
            direction_key = f"rag-{state}-direction"
            identity = "2608.90001"

            cases = {
                "zero-support": (
                    [],
                    (),
                    "field-map",
                    f"labeled {state} requires canonical support",
                ),
                "prior-none": (
                    [
                        native_record(
                            identity,
                            "2026-08-19T01:00:00Z",
                            state,
                            direction_keys=(direction_key,),
                        )
                    ],
                    (identity,),
                    "none",
                    "durable direction requires independent prior Field Map evidence",
                ),
                "wrong-direction-key": (
                    [
                        native_record(
                            identity,
                            "2026-08-19T01:00:00Z",
                            state,
                            direction_keys=("rag-other-direction",),
                        )
                    ],
                    (identity,),
                    "field-map",
                    f"direction_keys must include {direction_key}",
                ),
                "outside-window": (
                    [
                        native_record(
                            identity,
                            "2026-07-20T01:00:00Z",
                            state,
                            direction_keys=(direction_key,),
                        )
                    ],
                    (identity,),
                    "field-map",
                        "falls outside 2026-07-28—2026-08-26",
                ),
                "post-cutoff": (
                    [
                        native_record(
                            identity,
                            "2026-08-26T01:35:01Z",
                            state,
                            direction_keys=(direction_key,),
                        )
                    ],
                    (identity,),
                    "field-map",
                    "accepted after direction synthesized=2026-08-26T01:35:00Z",
                ),
                "incompatible-map-delta": (
                    [
                        native_record(
                            identity,
                            "2026-08-19T01:00:00Z",
                            "early_signal",
                            direction_keys=(direction_key,),
                        )
                    ],
                    (identity,),
                    "field-map",
                    f"requires at least one native support with map_delta={state}",
                ),
            }
            for name, (records, supports, prior, fragment) in cases.items():
                with self.subTest(state=state, case=name):
                    errors: list[str] = []
                    validate_reading._parse_direction_items(
                        "README.en.md",
                        "last-30-days",
                        english_direction(
                            state=state,
                            supports=supports,
                            map_key=direction_key,
                            prior=prior,
                        ),
                        validate_reading.EXPECTED_PERIOD_WINDOWS["last-30-days"],
                        records,
                        errors,
                    )
                    self.assertTrue(
                        any(fragment in error for error in errors), errors
                    )

    def test_split_retirement_state_drift_is_rejected_as_bilingual_parity(self):
        zh, en, records = repository_inputs()
        zh = zh.replace(
            'state="reinforced"', 'state="splits"', 1
        ).replace("`reinforced`", "`splits`", 1)
        en = en.replace(
            'state="reinforced"', 'state="retires"', 1
        ).replace("`reinforced`", "`retires`", 1)

        errors = validate_reading.validate_rag_timeline(zh, en, records)

        self.assertTrue(any("direction parity drift" in error for error in errors), errors)

    def test_one_paper_trend_claim_on_continuation_is_rejected(self):
        records = [native_record("2608.90001", "2026-08-19T01:00:00Z")]
        errors: list[str] = []
        validate_reading._parse_direction_items(
            "README.en.md", "last-30-days", english_direction() + "\n  This is a trend.",
            validate_reading.EXPECTED_PERIOD_WINDOWS["last-30-days"], records, errors,
        )
        self.assertTrue(any("trend/趋势 claim" in error for error in errors), errors)

    def test_direction_requires_confidence_and_design_implication_contracts(self):
        zh, en, records = repository_inputs()
        zh = zh.replace('confidence="medium"', '', 1).replace('implication="make-evidence-path-operations-explicit"', '', 1)
        errors = validate_reading.validate_rag_timeline(zh, en, records)
        self.assertTrue(any("confidence" in error.lower() for error in errors))
        self.assertTrue(any("implication" in error.lower() for error in errors))


class ReaderAttentionTest(unittest.TestCase):
    SHORT_LABELS = {
        "2608.22767": "EARM",
        "2608.23045": "NIS-Agent",
        "2608.23417": "SkillAlchemy",
        "2608.23265": "EvoWiki",
        "2608.22752": "Compaction Cliff",
        "2608.22751": "Risk-Aware Reranking",
        "2608.20627": "AgenticRAG-FP",
        "2608.20771": "CAS",
        "2608.21690": "Scroll",
        "2608.21808": "MCite-RL",
        "2608.22132": "SSE-Bio",
        "2608.22479": "GTA-RAG",
        "2608.23252": "ASCP",
        "2608.19652": "StateMem",
        "2608.18613": "CTIFoundry",
        "2608.17889": "VisDocAgentBench",
        "2608.16502": "ToolScout",
        "2608.16417": "D2-ScaleAgent",
        "2608.16185": "LENS",
        "2608.16370": "Context Compression Cost",
        "2608.15191": "RAAC",
        "2608.12888": "ReFind",
        "2608.11967": "LoongReflect",
        "2608.12282": "VAKRA",
    }

    def test_english_category_routes_use_the_english_research_map(self):
        en = (ROOT / "README.en.md").read_text(encoding="utf-8")
        self.assertNotIn("](categories/README.md)", en)
        self.assertGreaterEqual(en.count("](categories/README.en.md)"), 2)

    def test_bilingual_status_is_directly_after_depth_navigation_before_timeline(self):
        observed: list[tuple[str, str]] = []
        for filename, marker, pattern in (
            (
                "README.md",
                "[30 秒：最新时间线]",
                r"\*\*状态：\*\* 最后更新：\*\*(\d{4}-\d{2}-\d{2})\*\* · "
                r"最后合成：\*\*(\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z)（UTC）\*\*",
            ),
            (
                "README.en.md",
                "[30 sec: Timeline]",
                r"\*\*Status:\*\* Last updated: \*\*(\d{4}-\d{2}-\d{2})\*\* · "
                r"Last synthesized: \*\*(\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z) \(UTC\)\*\*",
            ),
        ):
            with self.subTest(filename=filename):
                text = (ROOT / filename).read_text(encoding="utf-8")
                nav_start = text.index(marker)
                nav_end = text.index("\n", nav_start)
                timeline_start = text.index('<a id="timeline"></a>', nav_end)
                status = text[nav_end:timeline_start].strip()
                match = re.fullmatch(pattern, status)
                self.assertIsNotNone(match, status)
                if match is not None:
                    observed.append((match.group(1), match.group(2)))
        self.assertEqual(2, len(observed))
        if len(observed) == 2:
            self.assertEqual(observed[0], observed[1])

    def test_status_position_and_parity_are_enforced_by_public_validation(self):
        zh, en, records = repository_inputs()
        errors = validate_reading.validate_rag_timeline(
            zh,
            en.replace("Last updated: **2026-08-26**", "Last updated: **2026-08-25**", 1),
            records,
        )
        self.assertTrue(any("reader status parity" in error.lower() for error in errors), errors)

    def test_timeline_uses_short_labels_and_expanded_canonical_title_links(self):
        zh, en, records = repository_inputs()
        record_by_id = {str(record["arxiv_id"]): record for record in records}
        for filename, text in (("README.md", zh), ("README.en.md", en)):
            for identity, label in self.SHORT_LABELS.items():
                with self.subTest(filename=filename, identity=identity):
                    start = text.index(f'<a id="entry-{identity}"></a>')
                    end = text.find('<a id="entry-', start + 1)
                    if end < 0:
                        end = text.index('<a id="periods"></a>', start)
                    chunk = text[start:end]
                    summary = chunk[:chunk.index("</summary>")]
                    record = record_by_id[identity]
                    title = str(record["title"])
                    primary = str(record["urls"]["paper"])
                    self.assertRegex(summary, rf"\d{{4}}-\d{{2}}-\d{{2}} · {re.escape(label)} ·")
                    self.assertNotIn(title, validate_reading.strip_html_comments(summary))
                    self.assertIn(f"[{title}]({primary})", validate_reading.strip_html_comments(chunk))

    def test_full_summary_title_and_generic_primary_label_are_rejected(self):
        zh, en, records = repository_inputs()
        record = next(item for item in records if item.get("arxiv_id") == "2608.16185")
        title = str(record["title"])
        primary = str(record["urls"]["paper"])
        full_summary = en.replace(" · LENS ·", f" · {title} ·", 1)
        errors = validate_reading.validate_rag_timeline(zh, full_summary, records)
        self.assertTrue(any("short canonical label" in error.lower() for error in errors), errors)

        generic_link = en.replace(f"[{title}]({primary})", f"[Paper]({primary})", 1)
        errors = validate_reading.validate_rag_timeline(zh, generic_link, records)
        self.assertTrue(any("canonical title link" in error.lower() for error in errors), errors)

    def test_public_validator_reads_canonical_title_from_expanded_primary_link(self):
        _, en, records = repository_inputs()
        errors: list[str] = []
        validate_public.timeline_records(en, records, "README.en.md", errors)
        self.assertFalse(any("title" in error.lower() for error in errors), errors)

        record = next(item for item in records if item.get("arxiv_id") == "2608.16185")
        title = str(record["title"])
        primary = str(record["urls"]["paper"])
        mutated = en.replace(f"[{title}]({primary})", f"[Paper]({primary})", 1)
        errors = []
        validate_public.timeline_records(mutated, records, "README.en.md", errors)
        self.assertTrue(any("canonical title link" in error.lower() for error in errors), errors)

    def test_every_timeline_area_prefix_resolves_to_field_map_axis_vocabulary(self):
        zh, en, records = repository_inputs()
        self.assertEqual(
            validate_reading._field_map_axes(zh),
            validate_reading._field_map_axes(en),
        )
        for filename, text in (("README.md", zh), ("README.en.md", en)):
            field_map = validate_reading._section(text, "field-map", "reading-paths")
            self.assertIsNotNone(field_map)
            assert field_map is not None
            axes = set(re.findall(r"^\| \*\*([^*]+)\*\* \|", field_map, flags=re.M))
            timeline = validate_reading._section(text, "timeline", "periods")
            self.assertIsNotNone(timeline)
            assert timeline is not None
            areas = re.findall(
                r"<summary>.*? · .*? · (.*?)\s*<!--\s*timefirst:area=",
                timeline,
            )
            self.assertEqual(len(self.SHORT_LABELS), len(areas))
            for area in areas:
                with self.subTest(filename=filename, area=area):
                    prefix, separator, subproblem = area.partition("→")
                    self.assertIn(prefix.strip(), axes)
                    if separator:
                        self.assertTrue(subproblem.strip())

        malformed = en.replace(" · Evidence materialization <!--", " · Evidence staging <!--", 1)
        errors = validate_reading.validate_rag_timeline(zh, malformed, records)
        self.assertTrue(any("field map axis" in error.lower() for error in errors), errors)

        hidden_axis = en.replace(
            "| Axis | Question | Current tension |",
            "<!--\n| **Evidence staging** | hidden | hidden |\n-->\n"
            "| Axis | Question | Current tension |",
            1,
        ).replace(" · Evidence materialization <!--", " · Evidence staging <!--", 1)
        errors = validate_reading.validate_rag_timeline(zh, hidden_axis, records)
        self.assertTrue(any("field map axis" in error.lower() for error in errors), errors)

        vocabulary_drift = en.replace(
            "| **Evidence materialization** |",
            "| **Evidence staging** |",
            1,
        ).replace(" · Evidence materialization <!--", " · Evidence staging <!--", 1)
        errors = validate_reading.validate_rag_timeline(zh, vocabulary_drift, records)
        self.assertTrue(any("axis vocabulary drift" in error.lower() for error in errors), errors)

    def test_bilingual_visible_axis_prefix_parity_is_per_timeline_entry(self):
        zh, en, records = repository_inputs()
        mutated = zh.replace(
            " · Evidence materialization <!-- timefirst:area=evidence-materialization -->",
            " · Resource accounting <!-- timefirst:area=evidence-materialization -->",
            1,
        )
        errors = validate_reading.validate_rag_timeline(mutated, en, records)
        self.assertTrue(
            any("visible field map axis parity" in error.lower() for error in errors),
            errors,
        )

        translated_subproblem = zh.replace(
            "State persistence → progress control",
            "State persistence → 进展控制",
            1,
        )
        self.assertEqual(
            [],
            validate_reading.validate_rag_timeline(
                translated_subproblem,
                en,
                records,
            ),
        )


if __name__ == "__main__":
    unittest.main()
