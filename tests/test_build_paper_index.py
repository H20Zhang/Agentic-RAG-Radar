from pathlib import Path
import sys
import unittest


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import build_paper_index


class PaperIndexNavigationTest(unittest.TestCase):
    def test_generated_navigation_uses_time_first_stable_anchors(self):
        rendered = build_paper_index.render()
        for target in (
            "../README.md#timeline",
            "../README.md#periods",
            "../README.md#reading-paths",
            "../README.md#field-map",
        ):
            self.assertIn(target, rendered)
        self.assertNotIn("#latest-papers", rendered)
        self.assertNotIn("#whats-changing", rendered)


if __name__ == "__main__":
    unittest.main()
