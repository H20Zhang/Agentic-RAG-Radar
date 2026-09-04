from pathlib import Path
import re

CUTOFF = "2026-09-04T01:53:14Z"

# Advance the repository-owned rolling synthesis contract for this accepted transaction.
p = Path("scripts/validate_reading.py")
s = p.read_text(encoding="utf-8")
s = s.replace('SYNTHESIS_TIMESTAMP = "2026-09-03T01:27:38Z"', f'SYNTHESIS_TIMESTAMP = "{CUTOFF}"')
s = s.replace('"last-7-days": (date(2026, 8, 28), date(2026, 9, 3)),', '"last-7-days": (date(2026, 8, 29), date(2026, 9, 4)),')
s = s.replace('"last-30-days": (date(2026, 8, 5), date(2026, 9, 3)),', '"last-30-days": (date(2026, 8, 6), date(2026, 9, 4)),')
p.write_text(s, encoding="utf-8")

# Advance regression fixtures and add the accepted native Timeline identity.
p = Path("tests/test_validate_reading.py")
s = p.read_text(encoding="utf-8")
s = s.replace("2026-09-03T01:27:38Z", CUTOFF)
s = s.replace('en.replace("Last updated: **2026-09-03**", "Last updated: **2026-08-31**", 1)', 'en.replace("Last updated: **2026-09-04**", "Last updated: **2026-08-31**", 1)')
s = s.replace('    SHORT_LABELS = {\n        "2609.00549": "Skill Following",', '    SHORT_LABELS = {\n        "2609.00967": "CoBRA",\n        "2609.00549": "Skill Following",')
s = s.replace('self.assertEqual(27, periods.count(\'state="new_signal"\'))', 'self.assertEqual(28, periods.count(\'state="new_signal"\'))')
p.write_text(s, encoding="utf-8")

# Repair the exact 7-day projection: select whole direction items, rather than prefix ranges.
def whole_direction(section: str, key: str) -> str:
    pattern = re.compile(
        r'^- \*\*`(?:new_signal|reinforced|revised|splits|retires|no_material_change)`.*?(?=^- \*\*`(?:new_signal|reinforced|revised|splits|retires|no_material_change)`|\Z)',
        flags=re.S | re.M,
    )
    for match in pattern.finditer(section):
        block = match.group(0)
        if f'key="{key}"' in block:
            return block.rstrip() + "\n\n"
    raise AssertionError(key)

for filename, start_header, dir_block in [
    (
        "README.md",
        "### 过去 7 天 · 2026-08-29—2026-09-04\n\n",
        '''- **`new_signal` · Counterfactual retrieval routing · 路由目标从 query difficulty 转向同查询的 external-minus-internal 边际效用。** <!-- timefirst:direction key="counterfactual-retrieval-routing" state="new_signal" supports="2609.00967" confidence="medium" implication="intervene-on-route-under-one-policy-and-match-realized-resources" timing="radar_published_at" synthesized="2026-09-04T01:53:14Z" prior="none" -->
  支撑：[CoBRA](#entry-2609.00967)；置信度：**medium**；时间依据：`radar_published_at`；精确合成时间：`2026-09-04T01:53:14Z`（UTC）；研究设计含义（intervene-on-route-under-one-policy-and-match-realized-resources）：固定同一 policy、prompt、tool schema 与查询总体，强制 internal/external route，并匹配 returned evidence、token、调用与 latency 后再估计边际效用；先验地图证据：`none`。

''',
    ),
    (
        "README.en.md",
        "### Last 7 days · 2026-08-29—2026-09-04\n\n",
        '''- **`new_signal` · Counterfactual retrieval routing · routing moves from query difficulty toward same-query external-minus-internal marginal utility.** <!-- timefirst:direction key="counterfactual-retrieval-routing" state="new_signal" supports="2609.00967" confidence="medium" implication="intervene-on-route-under-one-policy-and-match-realized-resources" timing="radar_published_at" synthesized="2026-09-04T01:53:14Z" prior="none" -->
  Supports: [CoBRA](#entry-2609.00967); confidence: **medium**; timing basis: `radar_published_at`; Exact synthesis time: `2026-09-04T01:53:14Z` (UTC); Research-design implication (intervene-on-route-under-one-policy-and-match-realized-resources): hold one policy, prompt, tool schema, and query population fixed; force internal/external routes and match returned evidence, tokens, calls, and latency before estimating marginal utility; prior map evidence: `none`.

''',
    ),
]:
    p = Path(filename)
    s = p.read_text(encoding="utf-8")
    last7_start = s.index(start_header) + len(start_header)
    last7_end = s.index('<a id="last-30-days"></a>', last7_start)
    section = s[last7_start:last7_end]
    rebuilt = dir_block
    for key in (
        "retrieval-invoked-actual-use",
        "interaction-conditioned-retrieval",
        "multimodal-evidence-persistence",
        "proactive-context-management",
    ):
        rebuilt += whole_direction(section, key)
    s = s[:last7_start] + rebuilt + s[last7_end:]

    # Use distinctive visible witnesses required by the Timeline semantic contract.
    s = s.replace(
        'timefirst:evidence=counterfactual-routing~warm-init-mars-ablation',
        'timefirst:evidence=counterfactual-routing~mars-avg-jem',
    )
    s = s.replace(
        'timefirst:caveat=counterfactual-routing~branch-competence-and-budget',
        'timefirst:caveat=counterfactual-routing~token-latency-evidence-volume',
    )
    if filename == "README.md":
        s = s.replace(
            '**证据。** 相同 warm initialization 下，完整 MARS 的 Avg jEM 为 **0.5418**；',
            '**证据。** 相同 warm initialization 下，MARS Avg jEM 为 **0.5418**；',
            1,
        )
        s = s.replace(
            '没有匹配 token、latency、证据量或美元成本。',
            '没有匹配 token / latency / evidence volume（token-latency-evidence-volume budget）或美元成本。',
            1,
        )
    else:
        s = s.replace(
            '**Evidence.** Under the same warm initialization, full MARS reaches **0.5418 Avg jEM**',
            '**Evidence.** Under the same warm initialization, MARS Avg jEM is **0.5418**',
            1,
        )
        s = s.replace(
            'rather than matching tokens, latency, evidence volume, or dollars.',
            'rather than matching token / latency / evidence volume (token-latency-evidence-volume budget) or dollars.',
            1,
        )
    p.write_text(s, encoding="utf-8")
