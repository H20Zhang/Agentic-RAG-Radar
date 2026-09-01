#!/usr/bin/env python3
from __future__ import annotations

import json
import re
from datetime import date, datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SYNTH = "2026-09-01T01:24:01Z"
FIRST_SEEN = "2026-09-01T01:18:08Z"
RADAR_DATE = "2026-09-01"
OLD_SYNTH = "2026-08-28T01:56:45Z"


def write(path: str, content: str) -> None:
    p = ROOT / path
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(content.rstrip() + "\n", encoding="utf-8")


def replace_once(text: str, old: str, new: str, label: str) -> str:
    if text.count(old) != 1:
        raise RuntimeError(f"{label}: expected exactly one occurrence of {old!r}, got {text.count(old)}")
    return text.replace(old, new, 1)


def record(identity: str, *, title: str, authors: list[str], published_at: str,
           venue: str, paper: str, code: str | None, category: str,
           tags: list[str], benchmarks: list[str], importance: int,
           relevance: float, direction: str, visual_type: str,
           visual_question: str, visual_takeaway: str, visual_compare: str,
           tldr: str, problem: str, core_idea: str, agent_loop: str,
           retrieval_design: str, compared_to: list[str], evidence: str,
           why: str, limits: list[str]) -> dict:
    urls = {"paper": paper, "code": code, "project": None}
    return {
        "id": f"arxiv:{identity}",
        "arxiv_id": identity,
        "title": title,
        "authors": authors,
        "first_seen": "2026-09-01",
        "published": "2026-08-28",
        "published_at": published_at,
        "first_seen_at": FIRST_SEEN,
        "radar_published_at": SYNTH,
        "time_provenance": "native_v2",
        "map_delta": "early_signal",
        "direction_keys": [direction],
        "updated": "2026-09-01",
        "venue": venue,
        "urls": urls,
        "primary_category": category,
        "tags": tags,
        "benchmarks": benchmarks,
        "relevance": relevance,
        "importance": importance,
        "visual_explainer": {
            "type": visual_type,
            "question": visual_question,
            "takeaway": visual_takeaway,
            "compared_with": visual_compare,
            "full_text_grounded": True,
            "renderer": "gpt-image-gen",
            "status": "pending",
            "master_image_path": None,
            "image_path": None,
            "prompt_path": f"assets/visuals/prompts/{identity}.md",
            "artifact_path": f"papers/{identity}.md",
        },
        "analysis": {
            "tldr": tldr,
            "problem": problem,
            "core_idea": core_idea,
            "agent_loop": agent_loop,
            "retrieval_design": retrieval_design,
            "compared_to": compared_to,
            "evidence": evidence,
            "why_it_matters": why,
            "limitations": limits,
            "confidence": "medium",
        },
        "provenance": {
            "discovered_via": ["arXiv cs.IR/cs.CL/cs.AI primary-source sweep"],
            "full_text_checked": True,
            "code_link_verified": bool(code),
            "last_reviewed": "2026-09-01",
        },
    }


records = [
    record(
        "2608.27912",
        title="ITER: Interaction-Aware Retrieval for Agentic Search",
        authors=["Haodong Chen", "Shuai Wang", "Yu Yin", "Shengyao Zhuang", "Guido Zuccon", "Teerapong Leelanupab"],
        published_at="2026-08-28T04:36:02Z",
        venue="Preprint; under review",
        paper="https://arxiv.org/abs/2608.27912",
        code="https://github.com/ielab/ITER",
        category="learning_optimization",
        tags=["interaction_aware_retrieval", "dense_retrieval", "trajectory_supervision", "redundancy_negatives", "deep_research_agents", "cross_agent_transfer"],
        benchmarks=["InfoSeek-Eval", "BrowseComp-Plus"],
        importance=4, relevance=0.98, direction="interaction-conditioned-retrieval",
        visual_type="trajectory_learning",
        visual_question="Should a retriever rank by current-query relevance or by marginal evidence utility given the search trajectory?",
        visual_takeaway="Conditioning on the main question and prior sub-queries, plus trajectory-relative negatives, improves same-agent and cross-agent search while keeping the ranked-retrieval interface fixed.",
        visual_compare="LRAT and current-sub-query-only ITER under matched retriever/agent configurations",
        tldr="ITER moves part of search state into the retriever: document utility is defined relative to what the agent has already searched and visited, not only to the current sub-query.",
        problem="Step-local retrievers can repeatedly surface already explored evidence and ignore what remains unresolved in a multi-step search trajectory.",
        core_idea="Encode the main question, current sub-query, and previous sub-queries together, then train with trajectory-relative positives plus redundancy, hard, and weak negatives derived from agent interactions.",
        agent_loop="The agent issues a sub-query, receives ranked results, visits documents, reasons, and searches again; ITER changes only the retriever behind this ranked interface.",
        retrieval_design="A Qwen3-Embedding retriever receives history-conditioned query text. Previously visited relevant documents become redundancy negatives so relevance is discounted when its information has already been consumed.",
        compared_to=["LRAT with the same 0.6B retriever family", "current-sub-query-only ITER", "AgentIR cross-agent transfer"],
        evidence="With Tongyi fixed, LRAT/current-query ITER/default ITER score 72.7/76.7/80.0 on InfoSeek-Eval and 43.4/43.7/46.6 on BrowseComp-Plus; across six agent backbones the default retriever beats LRAT in all 12 task cells, seven significantly.",
        why="It isolates an under-modeled placement decision: trajectory state can shape retrieval ranking itself, so relevance and marginal evidence utility are not the same target.",
        limits=["Training labels are success-conditioned on collected trajectories and an LLM verifier.", "Trajectory collection uses de-duplicated candidate exposure, which may encode an exploration prior not present in ordinary ranked retrieval.", "History-conditioned encoder latency/token cost is not reported, so task gains are not yet a matched resource frontier."],
    ),
    record(
        "2608.28062",
        title="WeAgent-MMSearch: Native Text-Vision Interaction for Multimodal Search Agents",
        authors=["Zongkai Liu", "Hui Zhang", "Liqiang Niu", "Zhen Cao", "Han Li", "Juntao Liu", "Wenchao Chen", "Chengduo Zhao", "Chao Yu", "Fandong Meng"],
        published_at="2026-08-28T08:28:43Z",
        venue="Preprint",
        paper="https://arxiv.org/abs/2608.28062",
        code=None,
        category="retrieval_tool_use",
        tags=["multimodal_search", "image_refeed", "evidence_persistence", "search_harness", "runtime_recovery", "visual_grounding"],
        benchmarks=["MMBrowseComp", "MMSearch", "MMSearch-Plus", "VisTarget-Bench", "SimpleVQA", "VDR-Bench", "LiveVQA", "FVQA"],
        importance=4, relevance=0.99, direction="multimodal-evidence-persistence",
        visual_type="retrieval_interface",
        visual_question="Does an image returned by search remain available to later reasoning/search actions, or disappear after one tool turn?",
        visual_takeaway="Keeping retrieved images model-visible across turns is a causal interface variable: removing only image re-feed drops the eight-task average from 55.97 to 46.89.",
        visual_compare="WeAgent-MMSearch-RL with versus without image re-feed under the same WeAgent-Harness tool interface",
        tldr="WeAgent-MMSearch exposes a clean multimodal harness result: evidence that is retrieved once but not re-fed to later turns behaves differently from persistent visual evidence.",
        problem="Many search harnesses serialize multimodal results into text and drop returned images from later context, making visual acquisition non-persistent across a trajectory.",
        core_idea="Give tool-returned images stable references and re-attach them to later model turns, alongside native web/image/reverse-image/extraction/code tools and bounded runtime recovery.",
        agent_loop="The multimodal agent searches, opens web/image results, receives text plus images, revisits or reverse-searches visual evidence, and synthesizes after a bounded interaction budget.",
        retrieval_design="The key ablation leaves the WeAgent-Harness tool interface intact but removes returned images from subsequent model turns, directly varying visual evidence persistence.",
        compared_to=["same WeAgent-MMSearch-RL without image re-feed", "Hermes harness on frontier models", "Base and SFT stages on VisTarget-Bench"],
        evidence="Across eight tasks, no-image-re-feed versus image-re-feed averages 46.89 versus 55.97; MMBrowseComp moves 13.69→28.13 and VisTarget-Bench 10.44→30.22 under the same trained policy and tool interface.",
        why="It turns evidence lifetime into an interface variable: acquiring a source is not enough if later policy steps cannot inspect the original modality again.",
        limits=["The larger post-training gain bundles harness, data construction, RL, recovery, and evidence persistence.", "Caching mixes freshness and latency semantics, and runtime recovery changes which trajectories survive.", "Budgets are caps rather than matched realized token/tool/latency/dollar accounting; VisTarget-Bench is author-created."],
    ),
    record(
        "2608.28476",
        title="ContextPilot: Teaching Agents for Proactive Context Management via Fine-grained RL",
        authors=["Zhuoshi Pan", "Qizhi Pei", "Junru Lu", "Honglin Lin", "H. Vicky Zhao", "Di Yin", "Xing Sun"],
        published_at="2026-08-28T16:01:08Z",
        venue="EMNLP 2026 Main Track",
        paper="https://arxiv.org/abs/2608.28476",
        code="https://github.com/Tencent/ContextPilot",
        category="learning_optimization",
        tags=["proactive_context_management", "context_editing", "fine_grained_rl", "partial_rollout", "long_term_memory", "deep_search"],
        benchmarks=["NovelQA", "InfiniteBench", "LongMemEval-S", "BrowseComp+", "BrowseComp", "BrowseComp-ZH", "GAIA", "xBench-DeepSearch"],
        importance=4, relevance=0.96, direction="proactive-context-management",
        visual_type="state_progression",
        visual_question="Can the agent learn when to plan, retain, compress, or offload working context instead of passively carrying the whole trajectory?",
        visual_takeaway="Fine-grained context-edit credit improves a fixed SFT policy family, but the headline system also changes tool semantics and training, so component credit stays local to matched ablations.",
        visual_compare="Qwen3-8B SFT/GRPO/context-aware partial rollout/fine-grained credit plus cumulative prompt-only tool-design controls",
        tldr="ContextPilot makes context editing an explicit learned control loop over planning, retrieval, memory, and offloading; its cleanest evidence is the staged RL ablation, not the full-system leaderboard.",
        problem="Long-horizon agents accumulate working context while context-management actions have heterogeneous downstream effects that trajectory-level reward credits too coarsely.",
        core_idea="Extend the context tool surface with planning, long-term memory and soft offloading, then use context/entropy-sensitive partial rollouts and action-level credit assignment around editing decisions.",
        agent_loop="The agent plans, searches/reads, writes memory, compresses or deletes context, checks budget, and continues until answer synthesis; context itself is an editable state surface.",
        retrieval_design="Retrieval is one part of a broader context environment; the research delta is policy placement over which evidence/state remains materialized rather than a new retrieval backend.",
        compared_to=["same Qwen3-8B SFT and GRPO family", "cumulative Qwen3.5-397B prompt-only tool-design variants", "ReAct/ReSum/SUPO/OpenSeeker package baselines"],
        evidence="Qwen3-8B SFT→GRPO→+context-aware rollout→+fine-grained credit ends at 83.88/75.25/64.27/54.18 on NovelQA/InfiniteBench/LongMemEval-S/BrowseComp+, with the final credit step improving all four cells.",
        why="It makes state-retention/offloading policy a first-class adaptive decision, but also demonstrates why context-management gains need tool-surface and training-policy controls separately.",
        limits=["The full method bundles a larger tool surface, SFT data, partial-rollout RL and fine-grained credit.", "Tool-design ablation is cumulative and uses a much larger prompt-only model, so it does not isolate each tool or match the trained policy.", "Compact prompt growth is reported without complete training/inference calls, latency, dollars or FLOPs."],
    ),
]

for rec in records:
    write(f"data/papers/{rec['arxiv_id']}.json", json.dumps(rec, ensure_ascii=False, indent=2))

notes = {
"2608.27912": r'''# ITER: Interaction-Aware Retrieval for Agentic Search

*Published 2026-08-28 · Learning & Optimization · Importance 4/5 · Full text reviewed · Confidence: medium*

[Paper](https://arxiv.org/abs/2608.27912) · [Code](https://github.com/ielab/ITER)

> **TL;DR.** ITER changes the retrieval target from current-query relevance to **marginal evidence utility given the search trajectory**. The strongest controls keep the ranked interface and retriever family fixed: LRAT/current-subquery/default ITER score **72.7/76.7/80.0** on InfoSeek-Eval and **43.4/43.7/46.6** on BrowseComp-Plus. The claim is retriever placement, not a generic planning win.

| 30-second verdict | |
|---|---|
| **Why it matters** | Agent state can live inside retrieval ranking, not only in query reformulation or a planner. |
| **Best evidence** | Same Qwen3-Embedding-0.6B/current-subquery representation: LRAT **72.7/43.4/.602** vs ITER SQ-only **76.7/43.7/.619**; adding MQ+previous subqueries reaches **80.0/46.6/.636**. |
| **Main caveat** | Training trajectories are success-conditioned and collected with de-duplicated candidate exposure; encoder-history cost is not reported. |

## Problem

Multi-step search changes what counts as useful evidence. A document can remain relevant to the current sub-query yet add no information because the agent already inspected it.

## Mechanism

ITER encodes `main question + current sub-query + previous sub-queries`. Training turns later-visited judged-relevant documents into positives, previously visited relevant documents into redundancy negatives, visited irrelevant documents into hard negatives, and unvisited current results into weak negatives.

## Closest comparison

LRAT is the closest trajectory-trained retriever. More importantly, the SQ-only ITER variant uses the same retriever family and current sub-query representation while changing trajectory-relative supervision; the query-input ablation then adds main-question and previous-sub-query context while holding training recipe fixed.

## Decisive evidence

| Claim | Evidence | Control | Reading |
|---|---|---|---|
| trajectory-relative supervision helps | LRAT **72.7/43.4/.602** → ITER SQ-only **76.7/43.7/.619** | same 0.6B family + SQ input | cleaner than the full package |
| interaction history helps ranking | SQ-only **76.7/43.7/.619** → MQ+SQ+PSQ **80.0/46.6/.636** | query-input ablation | prior search directions matter |
| visited text is not automatically useful | adding visited docs gives **77.7/41.1/.541** | same recipe | more trajectory context can hurt |
| transfers across agents | ITER beats LRAT in all **12** backbone×benchmark cells; seven significant | agent fixed, retriever swapped | evidence beyond one teacher agent |

## What remains unproven

The labels come from successful Tongyi trajectories plus an LLM verifier, and collection de-duplicates already returned documents before exposing candidates. That can bake an exploration prior into supervision. Query-encoder input is also longer, while latency/token/dollar cost is missing.

## Field-map consequence

`agent interaction state → retriever ranking → new evidence → next search`.

`early_signal`: **interaction-conditioned retrieval** is a useful placement coordinate, but one retriever study does not change the durable Field Map.

## Related reading

[Agentic-R](2601.11888.md) · [Critic-R](2606.00590.md) · [Training Protocols](2605.27881.md) · [Research Map](../categories/README.en.md)
''',
"2608.28062": r'''# WeAgent-MMSearch: Native Text-Vision Interaction for Multimodal Search Agents

*Published 2026-08-28 · Retrieval & Tool Use · Importance 4/5 · Full text reviewed · Confidence: medium*

[Paper](https://arxiv.org/abs/2608.28062)

> **TL;DR.** WeAgent-MMSearch isolates a simple but consequential harness variable: **does retrieved visual evidence remain model-visible on later turns?** With the same WeAgent-MMSearch-RL policy and tool interface, removing only image re-feed drops the eight-task mean from **55.97 to 46.89**. This is evidence-lifetime credit, not a claim that the whole WeAgent package wins because of retrieval.

| 30-second verdict | |
|---|---|
| **Why it matters** | “Retrieved once” and “available to later reasoning/search” are different evidence states in multimodal trajectories. |
| **Best evidence** | Same policy/tool interface, no re-feed → re-feed: **46.89→55.97** average; MMBrowseComp **13.69→28.13**, VisTarget **10.44→30.22**. |
| **Main caveat** | The broader system bundles data, RL, runtime recovery and caching; budgets are caps, not matched realized cost. |

## Problem

Text-centric search harnesses often drop tool-returned images after the tool turn, so later steps cannot revisit, compare, reverse-search, or ground on the original visual evidence.

## Mechanism

WeAgent-Harness gives retrieved images stable references and re-feeds them to subsequent model turns alongside web search, image search, reverse-image search, page extraction, and code execution. Runtime recovery repairs unambiguous tool-call serialization/parameter failures within fixed turn/call/context/time caps.

## Closest comparison

The decisive ablation is not WeAgent-Harness versus Hermes. It keeps **WeAgent-MMSearch-RL and the WeAgent-Harness tool interface fixed** and removes returned images from subsequent model turns.

## Decisive evidence

| Claim | Evidence | Control | Reading |
|---|---|---|---|
| visual persistence changes outcomes | eight-task avg **46.89→55.97** | same RL policy + same tool interface | clean evidence-lifetime delta |
| effect is largest when target images matter | VisTarget **10.44→30.22**, MMBrowseComp **13.69→28.13** | same ablation | modality persistence is causal here |
| full harness also helps frontier models | Kimi **55.09→58.42**, Gemini Flash **60.95→63.26**, Qwen Plus **49.63→51.58** | Hermes vs WeAgent harness | package-level harness evidence only |
| RL improves post-acquisition use | target match **47.62→87.10** SFT→RL; conditional answer after match **70.0→77.78** | VisTarget diagnostic | separates acquisition from later use |

## What remains unproven

The reported **+19.22** post-training gain changes much more than evidence persistence. Caching trades freshness for repeated-query latency, runtime recovery changes trajectory survival, over-budget trajectories can be excluded, and end-to-end realized tokens/calls/latency/dollars are not matched. VisTarget-Bench is also author-created.

## Field-map consequence

`retrieve image → keep/drop original modality → later search/reasoning → answer`.

`early_signal`: **multimodal evidence persistence** should be an explicit interface/materialization variable. One harness study does not alter the durable map.

## Related reading

[MCite-RL](2608.21808.md) · [VisDocAgentBench](2608.17889.md) · [AWM](2608.25618.md) · [Research Map](../categories/README.en.md)
''',
"2608.28476": r'''# ContextPilot: Teaching Agents for Proactive Context Management via Fine-grained RL

*Published 2026-08-28 · Learning & Optimization · Importance 4/5 · Full text reviewed · Confidence: medium*

[Paper](https://arxiv.org/abs/2608.28476) · [Code](https://github.com/Tencent/ContextPilot)

> **TL;DR.** ContextPilot makes working context an editable state surface and learns credit for context-edit actions. The load-bearing evidence is the staged Qwen3-8B ablation: SFT → GRPO → context-aware partial rollout → fine-grained credit ends at **83.88/75.25/64.27/54.18** on NovelQA/∞Bench/LongMemEval-S/BrowseComp+. The full system still bundles tool design, SFT and RL.

| 30-second verdict | |
|---|---|
| **Why it matters** | Retain/compress/offload decisions can be learned as state-control actions rather than treated as prompt plumbing. |
| **Best evidence** | The final fine-grained-credit step improves all four Qwen3-8B cells, including BrowseComp+ **51.08→54.18**. |
| **Main caveat** | Tool design is cumulative and the full package changes tool surface, demonstrations, rollout policy and credit assignment; complete lifecycle cost is missing. |

## Problem

Long-horizon agents carry expanding working context, while deletion, summarization, memory writes and retrieval have heterogeneous consequences that a single terminal reward can credit poorly.

## Mechanism

ContextPilot exposes planning (`analyzeText/checkBudget/plan`), retrieval (`buildIndex/searchContext/readChunk/readMultiChunks`), memory (`memorize/updateMemory/readMemory`) and offloading (`deleteContext/summarizeContext/compressContext/foldHistory`) actions. RL samples branches around context-sensitive editing decisions and assigns finer action-level advantages.

## Closest comparison

For learning credit, compare the same Qwen3-8B SFT/GRPO family and add entropy-, context-, then fine-grained components. The separate tool-design study is cumulative and uses Qwen3.5-397B-A17B prompt-only, so it is evidence that tool semantics matter, not a matched causal decomposition of the trained system.

## Decisive evidence

| Claim | Evidence | Control | Reading |
|---|---|---|---|
| finer edit credit helps | +Context → +Fine-grained: **83.05→83.88 / 73.94→75.25 / 61.40→64.27 / 51.08→54.18** | same Qwen3-8B training ladder | cleanest algorithm increment |
| entropy alone is unstable | GRPO → +Entropy lowers NovelQA **83.53→82.52** and BrowseComp+ **50.96→49.64** | staged ablation | “more RL machinery” is not enough |
| richer tool surface matters | prompt-only cumulative avg **77.89→80.29→83.08→87.16** | same large model, cumulative tools | tool semantics are a separate factor |
| context can stay smaller | long BrowseComp traces stabilize around **8–10K** input tokens versus ~**30K** by turn 15 for WebExplorer | cross-system trace | useful efficiency signal, not matched cost proof |

## What remains unproven

The headline system changes tool inventory, SFT demonstrations, partial-rollout sampling and credit assignment together. The tool ablation is cumulative on a much larger model. Token plots do not provide complete training compute, calls, latency, dollars, storage/update cost, or matched realized retrieval work.

## Field-map consequence

`persistent working state → edit/retain/offload policy → next retrieval/reasoning → answer`.

`early_signal`: **proactive context management** is a distinct state-policy placement. One package does not revise the durable Field Map.

## Related reading

[Scroll](2608.21690.md) · [Context Compression Cost](2608.16370.md) · [LoongReflect](2608.11967.md) · [Research Map](../categories/README.en.md)
'''
}

notes_zh = {
"2608.27912": r'''# ITER: Interaction-Aware Retrieval for Agentic Search

*发表于 2026-08-28 · 学习与优化 · 重要性 4/5 · 已阅读全文 · 置信度：中*

[论文](https://arxiv.org/abs/2608.27912) · [代码](https://github.com/ielab/ITER)

> **TL;DR。** ITER 把 retrieval target 从“当前 query 相关”推进到“给定已有 search trajectory 后还能带来多少新增 evidence”。最干净的控制保持 ranked interface 与 retriever family 不变：LRAT / current-subquery ITER / default ITER 在 InfoSeek-Eval 为 **72.7/76.7/80.0**，BrowseComp-Plus 为 **43.4/43.7/46.6**。应给 retriever placement 记功，而不是笼统归因给 planning。

| 30 秒判断 | |
|---|---|
| **为什么重要** | Agent state 不只可以进入 planner/query rewrite，也可以直接改变 retrieval ranking 的 utility 定义。 |
| **最强证据** | 同 Qwen3-Embedding-0.6B、同 SQ 输入：LRAT **72.7/43.4/.602** → ITER SQ-only **76.7/43.7/.619**；再加入 MQ+previous subqueries 达 **80.0/46.6/.636**。 |
| **最大限制** | 训练 trajectory 是 success-conditioned，candidate exposure 还做了 de-dup；history encoder 成本未报告。 |

## Problem

multi-step search 中，document 即便仍与当前 sub-query 相关，也可能因为 Agent 已经看过而没有新的 marginal utility。

## Mechanism

ITER 编码 `main question + current sub-query + previous sub-queries`；随后把之后访问且判为 relevant 的文档作 positive，把已访问 relevant 文档作 redundancy negative、已访问 irrelevant 文档作 hard negative、当前返回但未访问文档作 weak negative。

## Closest comparison

最近控制是 LRAT 与 SQ-only ITER：前者是已有 trajectory-trained retriever，后者保持当前 sub-query representation 与 retriever family，主要改变 trajectory-relative supervision。query-input ablation 再固定训练 recipe，逐步加入 MQ 与 PSQ。

## Decisive evidence

| 主张 | 证据 | 最近控制 | 判断 |
|---|---|---|---|
| trajectory-relative supervision 有用 | LRAT **72.7/43.4/.602** → ITER SQ-only **76.7/43.7/.619** | 同 0.6B family + SQ | 比 full package 更干净 |
| history 会改变 ranking | SQ-only → MQ+SQ+PSQ：**76.7/43.7/.619 → 80.0/46.6/.636** | query-input ablation | past search direction 有信息 |
| 不是 history 越多越好 | 加 visited docs 后 **77.7/41.1/.541** | 同 recipe | 原文 evidence 反而可能干扰 |
| 可跨 agent transfer | 六个 backbone × 两个 benchmark 共 12 格都胜 LRAT，7 格显著 | agent fixed, retriever swapped | 不只拟合一个 teacher |

## What remains unproven

labels 来自成功 Tongyi trajectories 与 LLM verifier；trajectory collection 还会先移除已返回文档再展示新候选，这可能把 exploration prior 写进 supervision。query encoder 输入变长，但 latency/token/dollar 成本没有配平。

## Field-map consequence

`agent interaction state → retriever ranking → new evidence → next search`。

这是 `early_signal`：**interaction-conditioned retrieval** 是值得单独比较的 placement coordinate；单篇 retriever study 不改 durable Field Map。

## Related reading

[Agentic-R](2601.11888.md) · [Critic-R](2606.00590.md) · [Training Protocols](2605.27881.md) · [Research Map](../categories/README.md)
''',
"2608.28062": r'''# WeAgent-MMSearch: Native Text-Vision Interaction for Multimodal Search Agents

*发表于 2026-08-28 · 检索与工具使用 · 重要性 4/5 · 已阅读全文 · 置信度：中*

[论文](https://arxiv.org/abs/2608.28062)

> **TL;DR。** WeAgent-MMSearch 隔离出一个很容易被忽略的 harness 变量：**search 返回的 image 在后续 turns 里还看不看得到？** 同一个 WeAgent-MMSearch-RL policy、同一个 tool interface，只去掉 image re-feed，八任务平均从 **55.97 降到 46.89**。这个增量应归给 evidence lifetime，而不是整个 WeAgent package 的 retrieval/planning。

| 30 秒判断 | |
|---|---|
| **为什么重要** | “已经检索到”与“后续 reasoning/search 仍能访问原始 modality”是两个不同 evidence state。 |
| **最强证据** | same policy/tool interface：no re-feed → re-feed **46.89→55.97**；MMBrowseComp **13.69→28.13**，VisTarget **10.44→30.22**。 |
| **最大限制** | 更大的 post-training gain 同时改变 data、RL、runtime recovery 与 cache；resource budget 只是 cap，不是 matched realized cost。 |

## Problem

很多 multimodal search harness 会把 tool result 文本化，并在下一轮丢掉原图；Agent 因而不能继续 revisit、compare、reverse-search 或基于原始视觉证据判断。

## Mechanism

WeAgent-Harness 给返回 image 稳定引用，并在后续 model turns 重新附上；action space 还包括 web search、image search、reverse-image search、page extraction 与 code execution。runtime recovery 在固定 turns/calls/context/time budget 内修复明确的 serialization/parameter error。

## Closest comparison

最关键不是 WeAgent-Harness vs Hermes，而是 **同一 WeAgent-MMSearch-RL + 同一 WeAgent-Harness tool interface**，只把 returned images 从后续 turns 移除。

## Decisive evidence

| 主张 | 证据 | 最近控制 | 判断 |
|---|---|---|---|
| visual evidence persistence 会改变结果 | 八任务 avg **46.89→55.97** | same RL policy + tool interface | 最干净的 evidence-lifetime delta |
| target-image 任务更敏感 | VisTarget **10.44→30.22**，MMBrowseComp **13.69→28.13** | 同 ablation | modality persistence 在这里是 causal factor |
| full harness 也提升 frontier model | Kimi **55.09→58.42**，Gemini Flash **60.95→63.26**，Qwen Plus **49.63→51.58** | Hermes vs WeAgent | 只能给 package-level harness credit |
| RL 同时改善找到图之后的使用 | target match **47.62→87.10**；match 后 answer **70.0→77.78** | VisTarget diagnostic | acquisition 与 use 可拆开 |

## What remains unproven

论文的 **+19.22** post-training gain 同时改变 harness、data construction、RL、recovery 等多项机制。cache 还引入 freshness/latency trade-off，recovery 改变 trajectory survival；完整 realized tokens/calls/latency/dollars 未匹配。VisTarget-Bench 也是作者自建 benchmark。

## Field-map consequence

`retrieve image → keep/drop original modality → later search/reasoning → answer`。

这是 `early_signal`：应把 **multimodal evidence persistence** 作为显式 interface/materialization variable；单篇 harness study 不改 durable map。

## Related reading

[MCite-RL](2608.21808.zh.md) · [VisDocAgentBench](2608.17889.zh.md) · [AWM](2608.25618.zh.md) · [Research Map](../categories/README.md)
''',
"2608.28476": r'''# ContextPilot: Teaching Agents for Proactive Context Management via Fine-grained RL

*发表于 2026-08-28 · 学习与优化 · 重要性 4/5 · 已阅读全文 · 置信度：中*

[论文](https://arxiv.org/abs/2608.28476) · [代码](https://github.com/Tencent/ContextPilot)

> **TL;DR。** ContextPilot 把 working context 变成可编辑 state，并给 context-edit actions 更细粒度 credit。最有归因价值的是 Qwen3-8B staged ablation：SFT → GRPO → context-aware partial rollout → fine-grained credit 最终在 NovelQA/∞Bench/LongMemEval-S/BrowseComp+ 达到 **83.88/75.25/64.27/54.18**。full system 仍然同时改变 tool design、SFT 与 RL。

| 30 秒判断 | |
|---|---|
| **为什么重要** | retain/compress/offload 可以成为 learned state-control action，而不是 prompt plumbing。 |
| **最强证据** | 最后一层 fine-grained credit 在四个 Qwen3-8B cell 都提升，其中 BrowseComp+ **51.08→54.18**。 |
| **最大限制** | tool design 是 cumulative ablation；完整 package 改了 tool surface、demonstration、rollout policy 与 credit assignment，lifecycle cost 不全。 |

## Problem

long-horizon agent 的 working context 会不断增长，而 delete、summarize、memory write、retrieval 对最终结果的影响差异很大，terminal reward 很难准确分配 credit。

## Mechanism

ContextPilot 暴露 planning（`analyzeText/checkBudget/plan`）、retrieval（`buildIndex/searchContext/readChunk/readMultiChunks`）、memory（`memorize/updateMemory/readMemory`）和 offloading（`deleteContext/summarizeContext/compressContext/foldHistory`）动作，并围绕 context-sensitive edits 做 partial rollout 与 action-level advantage estimation。

## Closest comparison

学习机制的最近控制是同一 Qwen3-8B SFT/GRPO family，逐步加入 entropy、context-aware rollout 和 fine-grained credit。另一个 tool-design study 是 Qwen3.5-397B-A17B prompt-only cumulative setup，因此只说明 tool semantics 本身重要，不能用于给小模型 trained package 做 component attribution。

## Decisive evidence

| 主张 | 证据 | 最近控制 | 判断 |
|---|---|---|---|
| finer edit credit 有增量 | +Context → +Fine-grained：**83.05→83.88 / 73.94→75.25 / 61.40→64.27 / 51.08→54.18** | 同 Qwen3-8B ladder | 最干净 algorithm increment |
| entropy alone 不稳定 | GRPO → +Entropy：NovelQA **83.53→82.52**，BrowseComp+ **50.96→49.64** | staged ablation | “更多 RL”本身不是解释 |
| 更丰富 tool surface 有贡献 | prompt-only cumulative avg **77.89→80.29→83.08→87.16** | 同大模型、逐步加 tools | tool semantics 是独立 factor |
| context 可以更紧凑 | BrowseComp 长 trajectory 约 **8–10K** input tokens 稳定，而 WebExplorer turn 15 约 **30K** | cross-system trace | efficiency signal，不是 matched cost proof |

## What remains unproven

headline system 同时改变 tool inventory、SFT demonstrations、partial-rollout sampling 与 credit assignment；tool ablation 又是大模型 cumulative setup。token plot 也没有给完整 training compute、calls、latency、dollars、storage/update lifecycle cost。

## Field-map consequence

`persistent working state → edit/retain/offload policy → next retrieval/reasoning → answer`。

这是 `early_signal`：**proactive context management** 是独立的 state-policy placement；单个 package 不修改 durable Field Map。

## Related reading

[Scroll](2608.21690.zh.md) · [Context Compression Cost](2608.16370.zh.md) · [LoongReflect](2608.11967.zh.md) · [Research Map](../categories/README.md)
'''
}

for identity, text in notes.items(): write(f"papers/{identity}.md", text)
for identity, text in notes_zh.items(): write(f"papers/{identity}.zh.md", text)

prompts = {
"2608.27912": "# Visual brief — ITER\n\nCreate a clean research figure about interaction-conditioned retrieval, not a generic agent architecture. Show the same ranked-search loop with current sub-query only versus main question + current sub-query + previous sub-queries; mark previously visited relevant documents as redundancy negatives and unread useful evidence as positives. Include LRAT 72.7/43.4/.602, ITER SQ-only 76.7/43.7/.619, and default 80.0/46.6/.636 for InfoSeek SR / BrowseComp+ SR / BrowseComp+ recall. Show the negative boundary that adding visited document text drops BrowseComp+ to 41.1 and recall to .541. Mark the causal boundary: trajectories are success-conditioned, collection de-duplicates candidate exposure, and encoder history cost is unreported.",
"2608.28062": "# Visual brief — WeAgent-MMSearch\n\nCreate a clean research figure about visual evidence lifetime in a search harness. Show search returning an image, then two otherwise identical later-turn paths: one drops the image after the tool turn and one re-feeds the original modality via a stable reference so later steps can inspect/reverse-search/compare it. Include the same-policy/tool-interface ablation 46.89 without image re-feed versus 55.97 with re-feed across eight tasks, plus MMBrowseComp 13.69→28.13 and VisTarget 10.44→30.22. Mark that the broader post-training package also changes data, RL, runtime recovery and cache semantics, and budgets are caps rather than matched realized cost.",
"2608.28476": "# Visual brief — ContextPilot\n\nCreate a clean research figure about proactive context-state control. Show a long-horizon loop where the agent can plan, retrieve/read, write/update memory, compress/summarize/delete/fold context, then continue. Highlight the matched Qwen3-8B training ladder SFT → GRPO → context-aware partial rollout → fine-grained credit, ending at 83.88/75.25/64.27/54.18 on NovelQA/InfiniteBench/LongMemEval-S/BrowseComp+. Show that entropy-only is unstable and that the tool-design ablation is cumulative on Qwen3.5-397B, so tool semantics and learning credit are separate factors. Mark incomplete training/inference token/tool/latency/dollar accounting.",
}
for identity, text in prompts.items(): write(f"assets/visuals/prompts/{identity}.md", text)

# Category projections.
cat = (ROOT / "categories/learning-optimization.md").read_text(encoding="utf-8")
marker = "## Current papers\n\n"
addition = """## Current papers\n\n\n### [ContextPilot](../papers/2608.28476.md) — ★★★★☆\n\n**Design point:** learn proactive working-context edits across planning, retrieval, memory, and offloading, with context-sensitive partial rollouts and action-level credit. **Boundary:** the full result bundles the tool surface, SFT data, rollout policy, and credit assignment; complete lifecycle cost is unmatched.\n\n### [ITER](../papers/2608.27912.md) — ★★★★☆\n\n**Design point:** make retriever utility trajectory-relative by conditioning on prior searches and demoting already consumed relevant evidence. **Boundary:** supervision is success-conditioned, candidate exposure is de-duplicated during collection, and longer encoder-input cost is unreported.\n\n"""
cat = replace_once(cat, marker, addition, "learning category")
write("categories/learning-optimization.md", cat)

cat = (ROOT / "categories/retrieval-tool-use.md").read_text(encoding="utf-8")
addition = """## Current papers\n\n\n### [WeAgent-MMSearch](../papers/2608.28062.md) — ★★★★☆\n\n**Design point:** preserve tool-returned images as model-visible evidence across later search/reasoning turns. **Boundary:** the clean image re-feed ablation isolates evidence lifetime, while the broader harness/post-training package also changes recovery, data, RL, and cache semantics.\n\n"""
cat = replace_once(cat, marker, addition, "retrieval category")
write("categories/retrieval-tool-use.md", cat)

# Library: update research lines without turning it into a second timeline.
lib = (ROOT / "library/README.en.md").read_text(encoding="utf-8")
lib = replace_once(lib,
    "[SIRA](../papers/2605.06647.md) → [DCI](../papers/2605.05242.md) → [ReFind](../papers/2608.12888.md) → [LENS](../papers/2608.16185.md)",
    "[SIRA](../papers/2605.06647.md) → [ITER](../papers/2608.27912.md) → [WeAgent-MMSearch](../papers/2608.28062.md) → [ContextPilot](../papers/2608.28476.md)", "library en line")
lib = replace_once(lib,
    "Adaptivity placement and evidence-materialization time are separate design decisions. SIRA compiles some retrieval decisions before retrieval; DCI and ReFind preserve raw substrates; LENS delays the evidence boundary itself until query time.",
    "Adaptivity placement and evidence lifetime are separate design decisions. SIRA compiles retrieval intent before access; ITER moves trajectory state into retriever ranking; WeAgent-MMSearch keeps returned visual evidence available across turns; ContextPilot learns which working state to retain or offload.", "library en prose")
write("library/README.en.md", lib)

lib = (ROOT / "library/README.md").read_text(encoding="utf-8")
lib = replace_once(lib,
    "[SIRA](../papers/2605.06647.md) → [DCI](../papers/2605.05242.md) → [ReFind](../papers/2608.12888.zh.md) → [LENS](../papers/2608.16185.zh.md)",
    "[SIRA](../papers/2605.06647.md) → [ITER](../papers/2608.27912.zh.md) → [WeAgent-MMSearch](../papers/2608.28062.zh.md) → [ContextPilot](../papers/2608.28476.zh.md)", "library zh line")
lib = replace_once(lib,
    "自适应位置与证据形成时机是两个不同的设计决策。SIRA 在执行检索前预先编排一部分决策；DCI 和 ReFind 保留原始载体；LENS 则把证据边界的确定进一步推迟到查询时。",
    "自适应位置与 evidence lifetime 是两个不同的设计决策。SIRA 在访问前编排 retrieval intent；ITER 把 trajectory state 放进 retriever ranking；WeAgent-MMSearch 让返回的视觉证据跨 turn 保持可见；ContextPilot 再学习哪些 working state 应保留或 offload。", "library zh prose")
write("library/README.md", lib)

# Timeline entries.
def timeline_entry(identity: str, lang: str) -> str:
    r = next(x for x in records if x["arxiv_id"] == identity)
    if identity == "2608.27912":
        label, axis, sub, area = "ITER", "Adaptivity placement", "interaction-conditioned retrieval", "interaction-conditioned-retrieval"
        if lang == "zh":
            one = "把 trajectory history 放进 retriever：ranking 目标从当前 query relevance 变成相对于已探索 evidence 的 marginal utility。"
            q = "在 ranked interface 不变时，retriever 是否应该显式知道 Agent 已经搜过什么、看过什么？"
            ev = "同 Qwen3-Embedding-0.6B family：LRAT / ITER SQ-only / default ITER 在 InfoSeek-Eval 为 **72.7/76.7/80.0**，BrowseComp-Plus 为 **43.4/43.7/46.6**；六个 agent backbone 的 12 个 task cell 中 default ITER 全部胜 LRAT。"
            caveat = "success-conditioned trajectory + LLM verifier；collection de-duplicates candidate exposure，且 history-conditioned encoder 的 token/latency 成本未报告。"
            mapline = "`early_signal`：interaction-conditioned retrieval 值得作为独立 placement variable，但单篇 retriever work 不改 durable map。"
            links = f"[{r['title']}]({r['urls']['paper']}) · [Code]({r['urls']['code']}) · [英文深读](papers/{identity}.md) · [中文深读](papers/{identity}.zh.md)"
            fields = ("问题。", "证据。", "限制。", "地图。", "链接。")
        else:
            one = "Moves trajectory history into the retriever: ranking targets marginal evidence utility given what the agent already explored, not current-query relevance alone."
            q = "With the ranked interface fixed, should the retriever know what the agent has already searched and consumed?"
            ev = "Same Qwen3-Embedding-0.6B family: LRAT / ITER SQ-only / default ITER score **72.7/76.7/80.0** on InfoSeek-Eval and **43.4/43.7/46.6** on BrowseComp-Plus; default ITER beats LRAT in all 12 cells across six agent backbones."
            caveat = "Success-conditioned trajectories plus an LLM verifier; collection de-duplicates candidate exposure, and history-encoder token/latency cost is unreported."
            mapline = "`early_signal`: interaction-conditioned retrieval is a useful placement variable; one retriever study does not change the durable map."
            links = f"[{r['title']}]({r['urls']['paper']}) · [Code]({r['urls']['code']}) · [English deep note](papers/{identity}.md) · [Chinese deep note](papers/{identity}.zh.md)"
            fields = ("Question.", "Evidence.", "Caveat.", "Map.", "Links.")
    elif identity == "2608.28062":
        label, axis, sub, area = "WeAgent-MMSearch", "Evidence materialization", "multimodal evidence persistence", "multimodal-evidence-persistence"
        if lang == "zh":
            one = "把 tool-returned image 的跨 turn 可见性变成显式 harness variable，而不是把“搜到图”视为一次性 observation。"
            q = "visual evidence 被 retrieval 返回后，后续 search/reasoning 是否仍能访问原始 modality？"
            ev = "同 WeAgent-MMSearch-RL、同 WeAgent-Harness tool interface，只移除 image re-feed：八任务平均 **55.97→46.89**；MMBrowseComp **28.13→13.69**，VisTarget **30.22→10.44**。"
            caveat = "更大的 full-system gain 同时改变 data、RL、runtime recovery 与 cache；budget 是 cap，不是 matched realized cost。"
            mapline = "`early_signal`：multimodal evidence persistence 应作为独立 materialization/interface variable；单篇 harness study 不改 durable map。"
            links = f"[{r['title']}]({r['urls']['paper']}) · [英文深读](papers/{identity}.md) · [中文深读](papers/{identity}.zh.md)"
            fields = ("问题。", "证据。", "限制。", "地图。", "链接。")
        else:
            one = "Makes cross-turn visibility of tool-returned images an explicit harness variable instead of treating a found image as a one-shot observation."
            q = "After retrieval returns visual evidence, can later search/reasoning steps still access the original modality?"
            ev = "Same WeAgent-MMSearch-RL and WeAgent-Harness tool interface, removing only image re-feed: eight-task average **55.97→46.89**; MMBrowseComp **28.13→13.69** and VisTarget **30.22→10.44**."
            caveat = "The larger package also changes data, RL, runtime recovery and caching; budgets are caps rather than matched realized cost."
            mapline = "`early_signal`: multimodal evidence persistence is an independent materialization/interface variable; one harness study does not change the durable map."
            links = f"[{r['title']}]({r['urls']['paper']}) · [English deep note](papers/{identity}.md) · [Chinese deep note](papers/{identity}.zh.md)"
            fields = ("Question.", "Evidence.", "Caveat.", "Map.", "Links.")
    else:
        label, axis, sub, area = "ContextPilot", "State persistence", "proactive context management", "proactive-context-management"
        if lang == "zh":
            one = "把 working context 当成可编辑 state：Agent 主动决定 plan、retain、compress、offload，并对关键 edit action 做细粒度 RL credit。"
            q = "long-horizon search 中，哪些 state 应继续 materialize，哪些应 offload，以及这个 policy 能否被独立训练？"
            ev = "Qwen3-8B staged ablation 中 +Context → +Fine-grained 在 NovelQA/∞Bench/LME-S/BC+ 从 **83.05/73.94/61.40/51.08** 到 **83.88/75.25/64.27/54.18**，四格均提升。"
            caveat = "full method 同时扩展 tool surface、SFT、partial rollout 与 credit；tool ablation 又是大模型 cumulative setup，完整 lifecycle cost 未配平。"
            mapline = "`early_signal`：proactive context management 是 state-policy placement；单个 package 不改 durable Field Map。"
            links = f"[{r['title']}]({r['urls']['paper']}) · [Code]({r['urls']['code']}) · [英文深读](papers/{identity}.md) · [中文深读](papers/{identity}.zh.md)"
            fields = ("问题。", "证据。", "限制。", "地图。", "链接。")
        else:
            one = "Treats working context as editable state: the agent plans, retains, compresses, or offloads, with fine-grained RL credit around key edit actions."
            q = "In long-horizon search, which state should remain materialized, what should be offloaded, and can that policy be trained separately?"
            ev = "In the Qwen3-8B staged ablation, +Context → +Fine-grained moves NovelQA/∞Bench/LME-S/BC+ from **83.05/73.94/61.40/51.08** to **83.88/75.25/64.27/54.18**, improving all four cells."
            caveat = "The full method expands tool surface, SFT, partial rollouts and credit together; the tool ablation is cumulative on a larger model, and complete lifecycle cost is unmatched."
            mapline = "`early_signal`: proactive context management is a state-policy placement; one package does not change the durable Field Map."
            links = f"[{r['title']}]({r['urls']['paper']}) · [Code]({r['urls']['code']}) · [English deep note](papers/{identity}.md) · [Chinese deep note](papers/{identity}.zh.md)"
            fields = ("Question.", "Evidence.", "Caveat.", "Map.", "Links.")
    return f'''<a id="entry-{identity}"></a>\n<details><summary>{RADAR_DATE} · {label} · {axis} → {sub} <!-- timefirst:area={area} --> — {one} <!-- timefirst:delta={area} --></summary>\n\n**{fields[0]}** {q} <!-- timefirst:question={area} -->\n\n**{fields[1]}** {ev} <!-- timefirst:evidence={area}~matched-control -->\n\n**{fields[2]}** {caveat} <!-- timefirst:caveat={area}~resource-boundary -->\n\n**{fields[3]}** {mapline}\n\n**{fields[4]}** {links}\n\n</details>\n\n'''


def update_timeline(path: str, lang: str) -> None:
    text = (ROOT / path).read_text(encoding="utf-8")
    if lang == "zh":
        old_status = f"**状态：** 最后更新：**2026-08-28** · 最后合成：**{OLD_SYNTH}（UTC）**"
        new_status = f"**状态：** 最后更新：**{RADAR_DATE}** · 最后合成：**{SYNTH}（UTC）**"
    else:
        old_status = f"**Status:** Last updated: **2026-08-28** · Last synthesized: **{OLD_SYNTH} (UTC)**"
        new_status = f"**Status:** Last updated: **{RADAR_DATE}** · Last synthesized: **{SYNTH} (UTC)**"
    text = replace_once(text, old_status, new_status, f"{path} status")
    marker = '<a id="entry-2608.25618"></a>'
    addition = "".join(timeline_entry(i, lang) for i in ("2608.27912", "2608.28062", "2608.28476"))
    text = replace_once(text, marker, addition + marker, f"{path} timeline")
    write(path, text)

update_timeline("README.md", "zh")
update_timeline("README.en.md", "en")

# Rolling period projections: filter old blocks by the new exact Radar-acceptance windows, then prepend new signals.
def all_record_times() -> dict[str, date]:
    out = {}
    for p in (ROOT / "data/papers").glob("*.json"):
        r = json.loads(p.read_text(encoding="utf-8"))
        stamp = r.get("radar_published_at")
        if r.get("time_provenance") == "native_v2" and isinstance(stamp, str):
            out[str(r.get("arxiv_id", r.get("id")))] = datetime.strptime(stamp, "%Y-%m-%dT%H:%M:%SZ").date()
    return out
TIMES = all_record_times()


def direction_block(identity: str, lang: str) -> str:
    if identity == "2608.27912":
        key, heading, label, implication = "interaction-conditioned-retrieval", "Interaction conditioned retrieval", "ITER", "separate-retriever-history-from-query-policy"
        zh_head = "Interaction conditioned retrieval · trajectory state 进入 retriever ranking。"
        en_head = "Interaction conditioned retrieval · trajectory state enters retriever ranking."
        zh_imp = "固定 agent、ranked interface 与 retriever backbone，分别改变 query history representation 和 trajectory-relative supervision，并报告 encoder/token/latency 成本"
        en_imp = "hold the agent, ranked interface, and retriever backbone fixed while varying history representation and trajectory-relative supervision, then report encoder/token/latency cost"
    elif identity == "2608.28062":
        key, heading, label, implication = "multimodal-evidence-persistence", "Multimodal evidence persistence", "WeAgent-MMSearch", "separate-evidence-acquisition-from-cross-turn-visibility"
        zh_head = "Multimodal evidence persistence · 搜到视觉证据与后续还能访问它是两件事。"
        en_head = "Multimodal evidence persistence · acquiring visual evidence and keeping it visible later are different states."
        zh_imp = "固定 policy、tool inventory、returned results 与预算，只切换原始 modality 的跨 turn 可见性，再分别测 acquisition、later use 与完整资源"
        en_imp = "hold policy, tool inventory, returned results, and budget fixed; vary only cross-turn visibility of the original modality and score acquisition, later use, and full resources separately"
    else:
        key, heading, label, implication = "proactive-context-management", "Proactive context management", "ContextPilot", "separate-context-tool-surface-from-edit-policy"
        zh_head = "Proactive context management · working context 本身成为可学习的 state-control surface。"
        en_head = "Proactive context management · working context becomes a learned state-control surface."
        zh_imp = "固定 tool inventory、SFT data、rollout budget 与 base model，分别改变 edit policy、partial-rollout selection 和 credit assignment，并计入 retention/offloading 成本"
        en_imp = "hold tool inventory, SFT data, rollout budget, and base model fixed while varying edit policy, partial-rollout selection, and credit assignment, including retention/offloading cost"
    head = zh_head if lang == "zh" else en_head
    if lang == "zh":
        details = f"支撑：[{label}](#entry-{identity})；置信度：**medium**；时间依据：`radar_published_at`；精确合成时间：`{SYNTH}`（UTC）；研究设计含义（{implication}）：{zh_imp}；先验地图证据：`none`。"
    else:
        details = f"Supports: [{label}](#entry-{identity}); confidence: **medium**; timing basis: `radar_published_at`; Exact synthesis time: `{SYNTH}` (UTC); Research-design implication ({implication}): {en_imp}; prior map evidence: `none`."
    return f'- **`new_signal` · {head}** <!-- timefirst:direction key="{key}" state="new_signal" supports="{identity}" confidence="medium" implication="{implication}" timing="radar_published_at" synthesized="{SYNTH}" prior="none" -->\n  {details}\n\n'


def filter_period(text: str, lang: str, anchor: str, next_anchor: str, start: date, end: date, new_ids: tuple[str, ...]) -> str:
    sm = f'<a id="{anchor}"></a>'
    em = f'<a id="{next_anchor}"></a>'
    s, e = text.index(sm), text.index(em, text.index(sm) + len(sm))
    sec = text[s:e]
    sec = sec.replace(OLD_SYNTH, SYNTH)
    sec = re.sub(r"2026-08-22—2026-08-28", f"{start.isoformat()}—{end.isoformat()}", sec)
    sec = re.sub(r"2026-07-30—2026-08-28", f"{start.isoformat()}—{end.isoformat()}", sec)
    blocks = list(re.finditer(r"(?ms)^- \*\*.*?(?=^- \*\*|\Z)", sec))
    if not blocks:
        raise RuntimeError(f"no direction blocks in {anchor}")
    prefix = sec[:blocks[0].start()]
    kept = []
    suffix = ""
    for idx, m in enumerate(blocks):
        block = m.group(0)
        meta = re.search(r'state="([^"]+)" supports="([^"]*)"', block)
        if not meta:
            continue
        state, support_s = meta.groups()
        ids = [x for x in support_s.split(",") if x and x != "none"]
        valid = bool(ids) and all(i in TIMES and start <= TIMES[i] <= end for i in ids)
        if state == "reinforced" and len(set(ids)) < 2:
            valid = False
        if valid:
            kept.append(block)
    new = "".join(direction_block(i, lang) for i in new_ids)
    new_sec = prefix + new + "".join(kept)
    return text[:s] + new_sec + text[e:]

for path, lang in (("README.md", "zh"), ("README.en.md", "en")):
    text = (ROOT / path).read_text(encoding="utf-8")
    text = filter_period(text, lang, "last-7-days", "last-30-days", date(2026,8,26), date(2026,9,1), ("2608.27912","2608.28062","2608.28476"))
    text = filter_period(text, lang, "last-30-days", "field-map", date(2026,8,3), date(2026,9,1), ("2608.27912","2608.28062","2608.28476"))
    write(path, text)

# Reading paths: surface the new placement chain without changing Field Map.
text = (ROOT / "README.en.md").read_text(encoding="utf-8")
text = replace_once(text,
    "[SIRA](papers/2605.06647.md) → [ReFind](papers/2608.12888.md) → [LENS](papers/2608.16185.md) → [ASCP](papers/2608.23252.md)",
    "[SIRA](papers/2605.06647.md) → [ITER](papers/2608.27912.md) → [WeAgent-MMSearch](papers/2608.28062.md) → [ContextPilot](papers/2608.28476.md)", "reading path en")
text = replace_once(text,
    "Move from pre-query compilation through result-conditioned access and query-time localization to fresh evidence allocation across rounds; ask where the work moved each time.",
    "Move from pre-query compilation to trajectory-conditioned ranking, cross-turn multimodal evidence persistence, and learned context retention/offloading; ask which state each layer can actually observe.", "reading path en prose")
write("README.en.md", text)

text = (ROOT / "README.md").read_text(encoding="utf-8")
text = replace_once(text,
    "[SIRA](papers/2605.06647.md) → [ReFind](papers/2608.12888.zh.md) → [LENS](papers/2608.16185.zh.md) → [ASCP](papers/2608.23252.zh.md)",
    "[SIRA](papers/2605.06647.md) → [ITER](papers/2608.27912.zh.md) → [WeAgent-MMSearch](papers/2608.28062.zh.md) → [ContextPilot](papers/2608.28476.zh.md)", "reading path zh")
# prose wording is allowed to differ naturally; locate row by path and replace following sentence fragment only if present.
text = text.replace("从 pre-query compilation 经过 result-conditioned access、query-time localization，再到跨轮 fresh evidence allocation；每一步都要追问工作到底被移到了哪里。", "从 pre-query compilation 到 trajectory-conditioned ranking、跨 turn multimodal evidence persistence，再到 learned context retention/offloading；每一步都追问控制层真正能看到哪一种 state。", 1)
write("README.md", text)

# Close August: membership is Radar acceptance time, so Sep-1 records are excluded despite Aug-28 source dates.
aug_native = []
for p in (ROOT / "data/papers").glob("*.json"):
    r = json.loads(p.read_text(encoding="utf-8"))
    if r.get("time_provenance") != "native_v2": continue
    t = datetime.strptime(r["radar_published_at"], "%Y-%m-%dT%H:%M:%SZ").replace(tzinfo=timezone.utc)
    if date(2026,8,1) <= t.date() <= date(2026,8,31): aug_native.append(r)
aug_native.sort(key=lambda r: r["radar_published_at"])
if len(aug_native) != 22:
    raise RuntimeError(f"expected 22 August native acceptances, found {len(aug_native)}")
monthly = r'''# Agentic RAG Monthly — 2026-08

> **Coverage:** 2026-08-01 to 2026-08-31 · **Status:** final · **Radar acceptance boundary:** 2026-08-31T23:59:59Z · **Accepted native records:** 22

## Month thesis

**August changes the measurement object more than it changes the architecture taxonomy.** Retrieval success, evidence materialization, current-valid state, later reuse, stopping, and lifecycle cost repeatedly separate under matched controls. The useful model is no longer `static RAG → more agentic rounds`; it is:

`coverage × interface × evidence lifetime/materialization × retained state × control placement × realized resources`.

This closed digest uses `radar_published_at` for monthly membership and original `published_at` only for source chronology. Papers accepted on 2026-09-01 are not backfilled into August even when their source release date is 2026-08-28.

## 1. Evidence access, evidence state, and evidence grounding split apart

LENS delays evidence-window formation until query time. Scroll retains a lossless event log and materializes selected state later. AWM supplies the sharpest post-retrieval control: with gold evidence pages fixed, final/memory-only accuracy still rises **45.4/41.2→48.0/43.5**, while `Pmmc` falls **19.1%→16.4%**. EviGraph then writes verifier-approved spans into claim-level support/conflict state, and MCite-RL shows the visual analogue where citation-region reward can improve without proving semantic support.

The research consequence is a four-stage measurement chain:

`evidence reached → evidence preserved/materialized → evidence grounded → evidence changes later behavior`.

Collapsing these into one “retrieval quality” score loses the failure boundary.

## 2. Current-valid state is a lifecycle decision, not a recall problem

StateMem and EvoWiki provide the only August direction that cleared the durable evidence gate. StateMem resolves operative facts at answer time; across six backends its matched wrapper attributes **15.0–31.7 points** on StateMemBench beyond the same transcript/chunks/call/length budget. EvoWiki resolves supersession during writes; holding extraction, coreference, entity Wiki and reader fixed, removing overwrite drops macro accuracy **60.09→51.46**.

This supports one durable statement: preserving history and deciding what is currently valid are separate operations, and supersession can be placed at read time or write time. The external ceiling remains medium because StateMem is strongest on a synthetic stale-state benchmark and EvoWiki exposes large complete-state contexts.

## 3. “Adaptive search” now has to beat strong simpler controls

ASCP shows that fresh evidence rotation, not feedback-scheduler complexity, is the load-bearing result: at `k=2,T=12`, fresh rotation reaches **0.397** PR versus **0.257** for fixed reuse, while full ASCP is statistically tied with deep rotation (**0.309 vs 0.303, q=0.343**). Crase supplies a structurally bounded alternative: fixed citation-neighborhood exploration can report much lower calls/tokens/cost than open-ended deep-search baselines, although that comparison changes output contract, models, corpus access and substrate.

The standard therefore becomes: before crediting adaptivity, compare it with **fresh allocation, bounded exploration, and stronger interface design under one evidence surface and resource budget**.

## 4. Interface resolution is part of the causal treatment

VisDocAgentBench and CTIFoundry jointly reinforce explicit evidence-path operations. ReFind shows that chat-native session/time/local-context controls plus iterative access can outperform generic multi-round BM25 without proving that structured memory is obsolete. ToolScout demonstrates an even earlier failure: a capability absent from the candidate set cannot be repaired by downstream planning. Risk-Aware Reranking makes shortlist exposure measurable but stops before tool execution.

The causal path is:

`candidate/evidence coverage → surfaced interface → inspection/materialization → controller decision → execution/answer`.

A leaderboard that changes more than one edge is system evidence first.

## 5. Retained state must be priced against reacquisition

Context Compression Cost shows that similar task completion can hide repeated retrieval after state loss. EARM retains judged retrieval experience to amortize reranking, but evidence comes from one fixed LoCoMo store/query order and lacks complete token/latency accounting. Compaction Cliff protects typed constraints under severe compression but receives metadata unavailable to type-blind controls. RAAC and LoongReflect expose progress and rollback state while paying extra controller/teacher work.

“Smaller context,” “fewer calls,” and “persistent memory” are not cost claims by themselves. Construction/update, stored state, model tokens, tool calls, verifier/controller compute, latency, and later reacquisition belong in one ledger.

## 6. Learning targets are multiplying faster than causal evidence

GTA-RAG supervises complete evidence chains; CAFE learns when to request corrective feedback; CAS adapts evidence-set width; SSE-Bio routes between sources; SkillAlchemy learns what procedure to admit. Their common weakness is attribution: graph construction, tool/source inventory, feedback calls, acquisition budget, curriculum, and reward often move together.

The most informative negative controls are therefore as important as the positive results: ASCP's scheduler tie, CAS's calibration/correctness gap, MCite-RL's terminal-crop proxy, and CAFE's schedule sensitivity all bound what a headline gain can support.

## Durable map decision

August closes with **two reinforced map directions already represented in the Field Map**: explicit evidence-path operation surfaces and supersession-aware state assembly. No other direction has enough independent, lifecycle-matched support to justify a durable edit. The monthly synthesis therefore does not add a new axis.

## Evidence standard carried into September

A strong Agentic RAG experiment should freeze the base model, corpus/source snapshot, output contract, interface/harness, judge/verifier and total resource budget, then change one control boundary at a time. Report evidence coverage, evidence lifetime/materialization, state retained versus reacquired, stopping/verification behavior, and complete token/tool/latency accounting.

The key question is no longer whether an agentic package wins. It is **which state transition or control policy causes the win, compared with the strongest simpler policy that sees the same evidence and spends the same resources**.

## Reading path

**Placement:** SIRA → ReFind → LENS → ASCP.

**State:** StateMem → EvoWiki → AWM → EviGraph.

**Causal controls:** Training Protocols → Context Compression Cost → VisDocAgentBench → Crase.
'''
write("digests/monthly/2026-08.md", monthly)

idx = (ROOT / "digests/README.md").read_text(encoding="utf-8")
idx = idx.replace("[2026-W34 — Evidence-path operations, breadth/depth routing, and capability coverage](weekly/2026-W34.md)", "[2026-W35 — State validity, evidence materialization, and stronger controls](weekly/2026-W35.md)", 1)
idx = idx.replace("**[2026-W34 · Evidence-path operations, breadth/depth routing, and capability coverage](weekly/2026-W34.md)**\nExplicit evidence-path operations gain cross-task support, while breadth/depth and source-conditioned routing remain bounded single-paper signals.\n\n", "**[2026-W35 · State validity, evidence materialization, and stronger controls](weekly/2026-W35.md)**\nSupersession-aware state clears one durable gate while fresh allocation and bounded-search controls raise the attribution bar for adaptive search.\n\n**[2026-W34 · Evidence-path operations, breadth/depth routing, and capability coverage](weekly/2026-W34.md)**\nExplicit evidence-path operations gain cross-task support, while breadth/depth and source-conditioned routing remain bounded single-paper signals.\n\n", 1)
idx = idx.replace("**[2026-08 · Rolling research map](monthly/2026-08.md)**  \nAugust separates evidence/capability coverage, materialization, operation surfaces, retained state, and lifecycle resources.", "**[2026-08 · Finalized research map](monthly/2026-08.md)**  \nAugust closes by separating evidence access, materialization, current-valid state, control placement, and lifecycle resources; only two directions clear durable support.", 1)
write("digests/README.md", idx)

# Advance projection contracts and their tests.
val = (ROOT / "scripts/validate_reading.py").read_text(encoding="utf-8")
val = val.replace('SYNTHESIS_TIMESTAMP = "2026-08-28T01:56:45Z"', f'SYNTHESIS_TIMESTAMP = "{SYNTH}"')
val = val.replace('"last-7-days": (date(2026, 8, 22), date(2026, 8, 28))', '"last-7-days": (date(2026, 8, 26), date(2026, 9, 1))')
val = val.replace('"last-30-days": (date(2026, 7, 30), date(2026, 8, 28))', '"last-30-days": (date(2026, 8, 3), date(2026, 9, 1))')
write("scripts/validate_reading.py", val)

t = (ROOT / "tests/test_validate_reading.py").read_text(encoding="utf-8")
t = t.replace('"2026-08-28T01:56:46Z"', '"2026-09-01T01:24:02Z"')
t = t.replace('"accepted after direction synthesized=2026-08-28T01:56:45Z"', '"accepted after direction synthesized=2026-09-01T01:24:01Z"')
t = t.replace('"falls outside 2026-07-30—2026-08-28"', '"falls outside 2026-08-03—2026-09-01"')
t = t.replace('en.replace("Last updated: **2026-08-28**", "Last updated: **2026-08-26**", 1)', 'en.replace("Last updated: **2026-09-01**", "Last updated: **2026-08-31**", 1)')
short_marker = '    SHORT_LABELS = {\n'
short_add = '    SHORT_LABELS = {\n        "2608.27912": "ITER",\n        "2608.28062": "WeAgent-MMSearch",\n        "2608.28476": "ContextPilot",\n'
t = replace_once(t, short_marker, short_add, "short labels")
# Repository-count assertions, if present in this revision.
t = t.replace("periods.count('state=\"reinforced\"'), 3", "periods.count('state=\"reinforced\"'), 2")
t = t.replace("periods.count('state=\"new_signal\"'), 34", "periods.count('state=\"new_signal\"'), 33")
write("tests/test_validate_reading.py", t)

print("Applied 2026-09-01 Agentic RAG Radar transaction")
