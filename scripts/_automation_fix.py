from pathlib import Path
p = Path(__file__).with_name('_automation_sep1.py')
s = p.read_text(encoding='utf-8')
old = '[SIRA](papers/2605.06647.md) → [ReFind](papers/2608.12888.zh.md) → [LENS](papers/2608.16185.zh.md) → [ASCP](papers/2608.23252.zh.md)'
new = '[SIRA](papers/2605.06647.md) → [ReFind](papers/2608.12888.md) → [LENS](papers/2608.16185.md) → [ASCP](papers/2608.23252.zh.md)'
if s.count(old) != 1:
    raise SystemExit(f'expected one stale matcher, found {s.count(old)}')
p.write_text(s.replace(old, new, 1), encoding='utf-8')
