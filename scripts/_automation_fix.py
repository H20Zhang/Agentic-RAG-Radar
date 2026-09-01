from pathlib import Path

p = Path(__file__).with_name('_automation_sep1.py')
s = p.read_text(encoding='utf-8')

old = '[SIRA](papers/2605.06647.md) → [ReFind](papers/2608.12888.zh.md) → [LENS](papers/2608.16185.zh.md) → [ASCP](papers/2608.23252.zh.md)'
new = '[SIRA](papers/2605.06647.md) → [ReFind](papers/2608.12888.md) → [LENS](papers/2608.16185.md) → [ASCP](papers/2608.23252.zh.md)'
if s.count(old) != 1:
    raise SystemExit(f'expected one stale matcher, found {s.count(old)}')
s = s.replace(old, new, 1)

old = '            "image_path": None,'
new = '            "image_path": f"assets/visuals/{identity}.webp",'
if s.count(old) != 1:
    raise SystemExit(f'expected one pending image_path template, found {s.count(old)}')
s = s.replace(old, new, 1)

old = '        code="https://github.com/ielab/ITER",'
new = '        code=None,'
if s.count(old) != 1:
    raise SystemExit(f'expected one unavailable ITER code URL, found {s.count(old)}')
s = s.replace(old, new, 1)

old = '[Paper](https://arxiv.org/abs/2608.27912) · [Code](https://github.com/ielab/ITER)'
new = '[Paper](https://arxiv.org/abs/2608.27912)'
if s.count(old) != 1:
    raise SystemExit(f'expected one ITER English note code link, found {s.count(old)}')
s = s.replace(old, new, 1)

old = '            links = f"[{r[\'title\']}]({r[\'urls\'][\'paper\']}) · [Code]({r[\'urls\'][\'code\']}) · [英文深读](papers/{identity}.md) · [中文深读](papers/{identity}.zh.md)"'
new = '            links = f"[{r[\'title\']}]({r[\'urls\'][\'paper\']}) · [英文深读](papers/{identity}.md) · [中文深读](papers/{identity}.zh.md)"'
if s.count(old) != 2:
    raise SystemExit(f'expected two Chinese code-bearing timeline templates, found {s.count(old)}')
s = s.replace(old, new, 1)

old = '            links = f"[{r[\'title\']}]({r[\'urls\'][\'paper\']}) · [Code]({r[\'urls\'][\'code\']}) · [English deep note](papers/{identity}.md) · [Chinese deep note](papers/{identity}.zh.md)"'
new = '            links = f"[{r[\'title\']}]({r[\'urls\'][\'paper\']}) · [English deep note](papers/{identity}.md) · [Chinese deep note](papers/{identity}.zh.md)"'
if s.count(old) != 2:
    raise SystemExit(f'expected two English code-bearing timeline templates, found {s.count(old)}')
s = s.replace(old, new, 1)

p.write_text(s, encoding='utf-8')
