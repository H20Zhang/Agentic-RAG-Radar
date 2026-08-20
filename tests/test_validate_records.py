from copy import deepcopy
import json
from pathlib import Path
import sys
import unittest


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import validate


LEGACY = {
    "id": "arxiv:legacy",
    "published": "2026-08-12",
    "provenance": {"full_text_checked": True},
}


EXPLICIT_LEGACY = {
    **LEGACY,
    "published_at": "2026-08-12",
    "first_seen_at": None,
    "radar_published_at": None,
    "time_provenance": "legacy_unknown",
    "map_delta": "early_signal",
}


class CanonicalTimeContractTest(unittest.TestCase):
    def test_untouched_legacy_record_does_not_need_fabricated_timestamps(self):
        self.assertEqual([], validate.time_contract_errors(LEGACY))

    def test_complete_explicit_legacy_bundle_preserves_date_and_null_radar_times(self):
        self.assertEqual([], validate.time_contract_errors(EXPLICIT_LEGACY))

    def test_partial_explicit_legacy_bundle_is_rejected(self):
        for missing in (
            "published_at",
            "first_seen_at",
            "radar_published_at",
            "time_provenance",
            "map_delta",
        ):
            with self.subTest(missing=missing):
                record = deepcopy(EXPLICIT_LEGACY)
                del record[missing]
                errors = validate.time_contract_errors(record)
                self.assertTrue(any("partial" in error and missing in error for error in errors), errors)

    def test_explicit_legacy_bundle_requires_publication_date_parity(self):
        record = deepcopy(EXPLICIT_LEGACY)
        record["published_at"] = "2026-08-11"
        errors = validate.time_contract_errors(record)
        self.assertTrue(any("published_at" in error and "published" in error for error in errors), errors)

    def test_explicit_legacy_bundle_rejects_non_null_radar_times(self):
        for field in ("first_seen_at", "radar_published_at"):
            with self.subTest(field=field):
                record = deepcopy(EXPLICIT_LEGACY)
                record[field] = "2026-08-20T00:00:00Z"
                errors = validate.time_contract_errors(record)
                self.assertTrue(any("legacy_unknown" in error and field in error for error in errors), errors)

    def test_post_cutover_record_requires_all_times_map_status_and_full_text(self):
        record = deepcopy(LEGACY)
        record["radar_published_at"] = "2026-08-20T01:00:00Z"
        errors = validate.time_contract_errors(record)
        for field in ("published_at", "first_seen_at", "map_delta", "time_provenance"):
            self.assertTrue(any(field in error for error in errors), field)

        record.update(
            published_at="2026-08-12T00:00:00Z",
            first_seen_at="2026-08-20T00:30:00Z",
            map_delta="early_signal",
            time_provenance="native_v2",
        )
        record["provenance"]["full_text_checked"] = False
        errors = validate.time_contract_errors(record)
        self.assertTrue(any("full_text_checked" in error for error in errors))

    def test_timestamp_order_is_publication_then_discovery_then_radar_acceptance(self):
        record = deepcopy(LEGACY)
        record.update(
            published_at="2026-08-21T00:00:00Z",
            first_seen_at="2026-08-20T00:30:00Z",
            radar_published_at="2026-08-20T01:00:00Z",
            map_delta="early_signal",
            time_provenance="native_v2",
        )
        errors = validate.time_contract_errors(record)
        self.assertTrue(any("published_at <= first_seen_at <= radar_published_at" in error for error in errors))

    def test_native_v2_timestamps_require_strict_utc_and_cutover(self):
        record = deepcopy(LEGACY)
        record.update(
            published_at="2026-08-12T00:00:00+00:00",
            first_seen_at="2026-08-20T00:30:00Z",
            radar_published_at="2026-08-19T23:59:59Z",
            map_delta="early_signal",
            time_provenance="native_v2",
        )
        errors = validate.time_contract_errors(record)
        self.assertTrue(any("published_at" in error and "full UTC" in error for error in errors), errors)
        self.assertTrue(any("cutover" in error for error in errors), errors)

    def test_schema_encodes_all_three_record_shapes_and_rejects_partial_bundle(self):
        import jsonschema

        schema = json.loads((ROOT / "data" / "paper.schema.json").read_text(encoding="utf-8"))
        validator = jsonschema.Draft202012Validator(schema)
        repository_record = json.loads((ROOT / "data" / "papers" / "2608.16185.json").read_text(encoding="utf-8"))
        self.assertEqual([], list(validator.iter_errors(repository_record)))

        implicit = deepcopy(repository_record)
        for field in ("published_at", "first_seen_at", "radar_published_at", "time_provenance", "map_delta"):
            implicit.pop(field, None)
        self.assertEqual([], list(validator.iter_errors(implicit)))

        native = deepcopy(repository_record)
        native.update(
            published_at="2026-08-17T00:00:00Z",
            first_seen_at="2026-08-20T00:30:00Z",
            radar_published_at="2026-08-20T01:00:00Z",
            time_provenance="native_v2",
            map_delta="early_signal",
        )
        self.assertEqual([], list(validator.iter_errors(native)))

        partial = deepcopy(repository_record)
        partial.pop("map_delta")
        self.assertNotEqual([], list(validator.iter_errors(partial)))

    def test_direction_keys_are_unique_stable_tokens_and_require_native_v2(self):
        native = deepcopy(LEGACY)
        native.update(
            published_at="2026-08-12T00:00:00Z",
            first_seen_at="2026-08-20T00:30:00Z",
            radar_published_at="2026-08-20T01:00:00Z",
            time_provenance="native_v2",
            map_delta="early_signal",
            direction_keys=["rag-native-signal"],
        )
        self.assertEqual([], validate.time_contract_errors(native))

        for name, value in (
            ("not-a-list", "rag-native-signal"),
            ("empty", []),
            ("duplicate", ["rag-native-signal", "rag-native-signal"]),
            ("free-form", ["RAG native signal"]),
        ):
            with self.subTest(name=name):
                mutated = deepcopy(native)
                mutated["direction_keys"] = value
                errors = validate.time_contract_errors(mutated)
                self.assertTrue(any("direction_keys" in error for error in errors), errors)

        implicit = deepcopy(LEGACY)
        implicit["direction_keys"] = ["rag-native-signal"]
        errors = validate.time_contract_errors(implicit)
        self.assertTrue(
            any("direction_keys" in error and "native_v2" in error for error in errors),
            errors,
        )

        explicit = deepcopy(EXPLICIT_LEGACY)
        explicit["direction_keys"] = ["rag-native-signal"]
        errors = validate.time_contract_errors(explicit)
        self.assertTrue(
            any("direction_keys" in error and "forbidden" in error for error in errors),
            errors,
        )

    def test_schema_encodes_optional_native_direction_keys(self):
        import jsonschema

        schema = json.loads((ROOT / "data" / "paper.schema.json").read_text(encoding="utf-8"))
        validator = jsonschema.Draft202012Validator(schema)
        self.assertIn("direction_keys", schema["properties"])

        repository_record = json.loads(
            (ROOT / "data" / "papers" / "2608.16185.json").read_text(encoding="utf-8")
        )
        native = deepcopy(repository_record)
        native.update(
            published_at="2026-08-17T00:00:00Z",
            first_seen_at="2026-08-20T00:30:00Z",
            radar_published_at="2026-08-20T01:00:00Z",
            time_provenance="native_v2",
            map_delta="early_signal",
            direction_keys=["rag-native-signal"],
        )
        self.assertEqual([], list(validator.iter_errors(native)))

        explicit = deepcopy(repository_record)
        explicit["direction_keys"] = ["rag-native-signal"]
        self.assertTrue(list(validator.iter_errors(explicit)))

        implicit = deepcopy(repository_record)
        for field in (
            "published_at",
            "first_seen_at",
            "radar_published_at",
            "time_provenance",
            "map_delta",
        ):
            implicit.pop(field)
        implicit["direction_keys"] = ["rag-native-signal"]
        self.assertTrue(list(validator.iter_errors(implicit)))

    def test_post_cutover_time_cannot_claim_legacy_unknown_provenance(self):
        record = deepcopy(LEGACY)
        record.update(
            published_at="2026-08-12T00:00:00Z",
            first_seen_at="2026-08-20T00:30:00Z",
            radar_published_at="2026-08-20T01:00:00Z",
            map_delta="early_signal",
            time_provenance="legacy_unknown",
        )
        errors = validate.time_contract_errors(record)
        self.assertTrue(any("legacy_unknown" in error for error in errors))

    def test_post_cutover_time_provenance_must_be_native_v2_and_schema_rejects_null(self):
        record = deepcopy(LEGACY)
        record.update(
            published_at="2026-08-12T00:00:00Z",
            first_seen_at="2026-08-20T00:30:00Z",
            radar_published_at="2026-08-20T01:00:00Z",
            map_delta="early_signal",
            time_provenance=None,
        )
        errors = validate.time_contract_errors(record)
        self.assertTrue(any("time_provenance=native_v2" in error for error in errors))

        schema = json.loads((ROOT / "data" / "paper.schema.json").read_text(encoding="utf-8"))
        self.assertNotIn(None, schema["properties"]["time_provenance"]["enum"])


if __name__ == "__main__":
    unittest.main()
