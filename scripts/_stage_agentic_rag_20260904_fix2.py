from pathlib import Path

p = Path("tests/test_validate_reading.py")
s = p.read_text(encoding="utf-8")
s = s.replace("2026-09-03T01:27:39Z", "2026-09-04T01:53:15Z")
s = s.replace("falls outside 2026-08-05—2026-09-03", "falls outside 2026-08-06—2026-09-04")
p.write_text(s, encoding="utf-8")
