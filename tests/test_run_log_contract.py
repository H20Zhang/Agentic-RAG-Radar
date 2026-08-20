from pathlib import Path
import subprocess
import sys
import tempfile
import unittest


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import validate_reading


class NoPublicRunLogContractTest(unittest.TestCase):
    def test_authoritative_guidance_preserves_reader_attention_contract(self):
        for path in (
            ROOT / "docs" / "DAILY_WORKFLOW.md",
            ROOT / "docs" / "EDITORIAL_STANDARD.md",
        ):
            text = path.read_text(encoding="utf-8").lower()
            with self.subTest(path=path.relative_to(ROOT)):
                self.assertIn("short canonical label", text)
                self.assertIn("complete canonical title", text)
                self.assertIn("canonical field map axis", text)
                self.assertIn("depth navigation", text)

    def test_rag_guidance_declares_canonical_support_direction_binding(self):
        for path in (
            ROOT / "docs" / "DAILY_WORKFLOW.md",
            ROOT / "CURATION.md",
        ):
            text = path.read_text(encoding="utf-8")
            with self.subTest(path=path.relative_to(ROOT)):
                self.assertIn("direction_keys", text)
                self.assertIn("exact public synthesis cutoff", text)
                self.assertIn("ordered canonical supports", text)
                self.assertIn("prior-map", text)

    def test_authoritative_guidance_uses_radar_acceptance_for_rolling_support(self):
        for path in (
            ROOT / "docs" / "DAILY_WORKFLOW.md",
            ROOT / "COMPACTION.md",
            ROOT / "CURATION.md",
        ):
            text = path.read_text(encoding="utf-8")
            with self.subTest(path=path.relative_to(ROOT)):
                self.assertIn("radar_published_at", text)
                self.assertIn("legacy", text.lower())
                self.assertIn("not rolling support", text.lower())

        shared_protocol = (ROOT / "docs" / "RADAR_AGENT_PROTOCOL.md").read_text(
            encoding="utf-8"
        )
        self.assertIn("radar_published_at", shared_protocol)
        self.assertIn("legacy", shared_protocol.lower())
        self.assertIn("never native window support", shared_protocol.lower())

    def test_versioned_guidance_shares_the_no_public_run_invariant(self):
        workflow_documents = (
            ROOT
            / "docs/superpowers/specs/2026-08-20-research-radar-reading-architecture-v1-design.md",
            ROOT
            / "docs/superpowers/specs/2026-08-19-reader-experience-and-workflow-design.md",
        )
        bilingual_contract = ROOT / "docs/BILINGUAL_PUBLICATION.md"
        documents = (*workflow_documents, bilingual_contract)

        for path in documents:
            text = path.read_text(encoding="utf-8")
            with self.subTest(path=path.relative_to(ROOT)):
                self.assertIn("No public operational run logs", text)
                self.assertIn("runs/README.md", text)
                self.assertIn(".radar-private", text)
                self.assertNotIn("compact log", text)
                self.assertNotIn("Validation, log, notification", text)
                self.assertNotIn("`runs/*` remain single-source", text)

        for path in workflow_documents:
            text = path.read_text(encoding="utf-8")
            with self.subTest(workflow=path.relative_to(ROOT)):
                self.assertIn(
                    "validate → atomic canonical/Timeline/digest projection → material notification",
                    text,
                )

    def test_repository_has_no_public_daily_run_files(self):
        errors = validate_reading.validate_no_public_run_files(
            validate_reading.PUBLIC_OPERATIONAL_RUN_PATHS
        )
        self.assertEqual([], errors)

    def test_any_file_in_a_configured_public_run_path_is_rejected(self):
        with tempfile.TemporaryDirectory() as temporary_directory:
            public_path = Path(temporary_directory) / "future-public-runs"
            public_path.mkdir()
            forbidden = public_path / "2026-08-21.md"
            forbidden.write_text("# Operational state\n", encoding="utf-8")

            errors = validate_reading.validate_no_public_run_files((public_path,))

        self.assertTrue(any(str(forbidden) in error for error in errors), errors)

    def test_broken_symlink_cannot_hide_a_public_run_artifact(self):
        with tempfile.TemporaryDirectory() as temporary_directory:
            public_path = Path(temporary_directory) / "future-public-runs"
            public_path.mkdir()
            forbidden = public_path / "latest.md"
            forbidden.symlink_to(public_path / "missing-target.md")

            errors = validate_reading.validate_no_public_run_files((public_path,))

        self.assertTrue(any(str(forbidden) in error for error in errors), errors)

    def test_configured_public_run_path_cannot_itself_be_a_file(self):
        with tempfile.TemporaryDirectory() as temporary_directory:
            forbidden = Path(temporary_directory) / "daily-run.md"
            forbidden.write_text("# Operational state\n", encoding="utf-8")

            errors = validate_reading.validate_no_public_run_files((forbidden,))

        self.assertTrue(any(str(forbidden) in error for error in errors), errors)

    def test_private_run_artifact_directory_is_git_ignored(self):
        result = subprocess.run(
            ["git", "check-ignore", ".radar-private/runs/example.json"],
            cwd=ROOT,
            text=True,
            capture_output=True,
            check=False,
        )
        self.assertEqual(0, result.returncode, result.stderr)


if __name__ == "__main__":
    unittest.main()
