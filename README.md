# Agentic RAG Radar

**中文** | [English](README.en.md)

*追踪 Agent 如何主动获取、检查、控制和保存外部信息。*

这个 Radar 主要回答：**retrieval intelligence 应该放在哪里？Evidence 什么时候 materialize？哪些 state 值得保留？Adaptivity 到底换来了什么？**

**Radar Family：** [Agent Benchmark Radar](https://github.com/H20Zhang/Agent-Benchmark-Radar) · [Agent Memory](https://github.com/H20Zhang/Agent-Memory-Radar) · **Agentic RAG** · [Data Agent](https://github.com/H20Zhang/Data-Agent-Radar)

[30 秒：最新工作](#latest) · [5 分钟：领域地图](#field-map) · [15 分钟：阅读路径](#reading-paths) · [浏览全部](#library)

> **先建立一个简单模型：** `need information → search/access evidence → inspect → decide where/if to search again → answer or act`
>
> **当前判断：** “retriever 还是 agent”“一次 search 还是多次 search”都太粗。更稳定的设计轴是：**adaptivity 放在哪、evidence 何时 materialize、哪些 state 跨 action 保留、offline + online 到底花了多少资源。**

最后更新：**2026-08-20**

<a id="latest"></a>
## 最新论文

### [LENS: In-Context Search via Latent Evidence Exploration over Dynamic Raw Documents](papers/2608.16185.md)
`Retrieval & Tool Use` · `documents` `iterative search` `budget allocation` · **4/5** · 2026-08-17

**Research delta.** LENS 把 **evidence materialization 本身**推迟到 query time：raw document region 在真正看到 query 之前不必先固定成 chunk。

[Paper](https://arxiv.org/abs/2608.16185) · [英文研究笔记](papers/2608.16185.md)

<details><summary><strong>约 60 秒理解 LENS</strong></summary>

固定 chunk/index 会在 query 之前就决定 evidence boundary，而且 raw file 更新后可能变 stale。LENS 从多个廉价 cue 提议 raw-document regions，用 relevance oracle 检查，更新 per-fact belief 和 proposal weights，并在预算内停止。

最有信息量的结果是 evidence localization，而不是 answer EM。D500 controlled setting 上，LENS 为 **62.4% EM / 84.8% evidence recall**，ReAct-style search 为 **65.2% / 50.4%**；fixed fullwiki 上 EM 基本打平，但 grounded answer 更偏向 LENS。代价是更多 online token 与 latency。真正决定它是不是更好的 systems point，需要把 fresh-index maintenance cost 与 query-time localization cost 放在同一 lifecycle budget 下比较。

</details>

### [What Does Context Compression Cost an Agent? Interaction Costs Unrevealed by Task-Completion Metrics](papers/2608.16370.md)
`Evaluation & Analysis` · `memory` `iterative search` · **4/5** · 2026-08-17

**Research delta.** Context 变短不一定更便宜：被压掉的 state 可能在之后通过大量 **reacquisition retrieval** 重新买回来，而 task completion 看起来几乎没变。

[Paper](https://arxiv.org/abs/2608.16370) · [英文研究笔记](papers/2608.16370.md)

<details><summary><strong>约 60 秒理解这个结果</strong></summary>

论文把 tool calls 分成真正执行任务的 calls 与“因为 context 丢失而重新获取 state”的 calls。在固定 24-turn horizon 下，sliding compression 越激进，retrieval 越多；oracle 把被丢掉且可查询的 state 恢复后，大部分额外交互消失。

一个代表 cell 中 retrieval calls 从 **21.0 增到 63.9**，completion 却没有显著变化。负面边界同样重要：ALFWorld 没出现同样的 surge。因此“省了多少 context token”本身不是 cost metric，应该比较保留 state 的成本与以后通过 tool/retrieval 重取它的 latency/money。

</details>

### [When Deep Research Agents Stagnate: Enhancing Reasoning with Retrieval-Aware Agent Control](papers/2608.15191.md)
`Iterative Reasoning & Verification` · `adaptive stopping` `query rewrite` · **4/5** · 2026-08-15

**Research delta.** RAAC 把 **search progress** 显式化，用 coverage、novelty、query diversity 与 drift 共同决定 continue / redirect / stop。

[Paper](https://arxiv.org/abs/2608.15191) · [英文研究笔记](papers/2608.15191.md)

<details><summary><strong>约 60 秒理解 RAAC</strong></summary>

Deep-research agent 常见的问题不是不会继续搜，而是 evidence 已经饱和后还在搜。RAAC 在原 agent 外面加 progress signals，并根据它们继续 search、停止，或调用 critical re-thinker 生成真正不同的新 query。

BrowseComp-Plus 上，论文报告平均减少约 **14 次 search calls**，同时平均准确率提升约 **3 points**。但 controller 和 re-thinker 自己也要额外 LLM calls，所以“search 次数更少”还不能等价成 total cost 更低。下一步应该匹配 controller + retrieval 的 token、latency 和 monetary cost。

</details>

### [When Your Agent Opens the Chat App: Agent-Controlled Search over Raw Chat Logs Rivals Structured Memory](papers/2608.12888.md)
`Retrieval & Tool Use` · `memory` `iterative search` · **4/5** · 2026-08-13

**Research delta.** 当 raw archive 暴露 session/time/local-context controls，并允许 agent 根据结果继续搜索时，question-time access 可以替代一部分预先构建的 semantic memory structure。

[Paper](https://arxiv.org/abs/2608.12888) · [英文研究笔记](papers/2608.12888.md)

<details><summary><strong>约 60 秒理解 ReFind</strong></summary>

ReFind 保留原始 timestamped turns，并提供 lexical search、neighboring context、session fusion、temporal filters 和 seen-session state。它因此是一个比 one-shot BM25 更强的 control，用来判断 semantic memory structure 是否真的必要。

六个任务上，论文报告 **58.2 mean accuracy**，HippoRAG 2 为 **53.2**，BM25-RAG 为 **48.8**。LongMemEval-S/M 上，完整 interface 为 **93.2/89.3**，也高于 matched generic multi-round BM25 与 one-search control。尚未解决的是 lifecycle-matched cost，尤其在 semantic 与 acting-agent workload 上。

</details>

### [LoongReflect: Boosting Long-Horizon Reflection in Search Agents via Global Perspective Distillation](papers/2608.11967.md)
`Learning & Optimization` · `backtracking` `RL` · **4/5** · 2026-08-12

**Research delta.** LoongReflect 让 active search state **可回滚**：发现被污染的 branch 后回到可信 prefix，保留 corrective lesson，再继续执行。

[Paper](https://arxiv.org/abs/2608.11967) · [英文研究笔记](papers/2608.11967.md)

<details><summary><strong>约 60 秒理解 LoongReflect</strong></summary>

一个错误 entity association 或错误 evidence 可能污染后续很多 search action。LoongReflect 训练 agent 做 reflect、backtrack 到可信 state、保留 corrective lesson，再从那里继续，而不是把错误 suffix 一直带下去。

Qwen2.5-3B 上，论文报告七个 RAG benchmark 平均 **46.15 F1**，AgenticRAG-R1 为 **33.55**。但 teacher 拥有 privileged global trajectory information，因此当前实验更支持“recovery-learning package”，还不能把全部增益归给 rollback semantics 本身。

</details>

### [VAKRA: Evaluating Multi-Hop Reasoning Across APIs and Retrieval Under Tool-Use Policies](papers/2608.12282.md)
`Evaluation & Analysis` · `APIs` `documents` `cross-source grounding` · **4/5** · 2026-08-12

**Research delta.** VAKRA 不再单独测 API use 或 document QA，而是测它们和 multi-hop reasoning、policy constraint 是否能在**同一条 executable trajectory**里保持一致。

[Paper](https://arxiv.org/abs/2608.12282) · [Code](https://github.com/IBM/vakra) · [英文研究笔记](papers/2608.12282.md)

<details><summary><strong>约 60 秒理解 VAKRA</strong></summary>

一个 agent 可以分别在 API benchmark 和 document QA 上表现很好，却在真正跨 source 时因为 identity resolution、grounding 或 policy constraint 失败。VAKRA 在固定 harness 中重新执行预测 tool calls，评估完整 trajectory，而不只是 final answer。

最佳模型在 single-hop endpoint-style tasks 上达到 **70.4%**，但 compositional APIs 只有约 **50–51%**；一些 policy-constrained unanswerable setting 低到 **2.4%**。这是 evaluation result，不是对某个 controller 的 component evidence。下一步应该固定 model/tools/budget，再隔离究竟哪种 control change 能修复 cross-source grounding。

</details>

<a id="changes"></a>
## 最近真正发生了什么变化

| 变化 | 新证据 | 对研究设计的含义 |
|---|---|---|
| **Evidence materialization 变成一等设计变量。** | Indexed RAG 预先 materialize chunk；DCI 保留 raw files；LENS 把 query-conditioned evidence localization 推到线上。 | 比较 freshness、evidence fidelity 与 offline+online cost，而不是只看 answer score。 |
| **Progress 与 retained state 开始变成显式 control state。** | RAAC 暴露 search progress；LoongReflect 让 reasoning state 可回滚；context-compression work 给 dropped state 的 re-query tax 定价。 | State policy 应进入 retrieval-cost attribution，而不是当作 runtime plumbing。 |
| **强 retrieval baseline 必须包含 interface 与 harness。** | ReFind、Pi-Serini 与 harness 分析都说明 search primitive、surfaced depth、interaction protocol 能显著改变结论。 | 在归因给“agentic retrieval policy”之前，先匹配 interface/harness。 |

时间视角：[weekly](digests/README.md) · [monthly](digests/monthly/2026-08.md) · [yearly](digests/yearly/2026.md)

<a id="field-map"></a>
## 领域地图

`information need → query/planning → retrieval interface → evidence materialization → inspection/reasoning → continue/redirect/stop → persistent state → answer/action`

| Axis | 核心问题 | 当前张力 |
|---|---|---|
| **Adaptivity placement** | 哪些行为可以在 evidence 到来前 compile，哪些必须 result-conditioned？ | `pre-query compilation ↔ query-time adaptation` |
| **Evidence materialization** | chunk/region/workspace 什么时候才应该变成 concrete object？ | `pre-materialized index ↔ raw/query-conditioned evidence` |
| **Interface resolution** | agent 到底能观察和控制哪些 retrieval operation / source state？ | `opaque top-k ↔ explicit search/read/filter/navigation` |
| **State persistence** | 哪些 evidence、progress、reasoning state 值得跨 action 保留？ | `stateless loop ↔ persistent/recoverable state` |
| **Resource accounting** | 什么方案真的更便宜？ | `local retrieval metric ↔ lifecycle cost + task outcome` |

[进入完整 research-question map →](categories/README.md) · [看这个方向如何被评价 →](https://github.com/H20Zhang/Agent-Benchmark-Radar#rag-agentic-retrieval)

<a id="reading-paths"></a>
## 阅读路径

| 你想回答的问题 | 建议顺序 | 应该学到什么 |
|---|---|---|
| **Retrieval control 和 materialization 应放在哪里？** | [SIRA](papers/2605.06647.md) → [DCI](papers/2605.05242.md) → [ReFind](papers/2608.12888.md) → [LENS](papers/2608.16185.md) | 有些 intelligence 能在 retrieval 前 compile；有些信息只有读到 evidence 后才可见；连 evidence granularity 本身都可能推迟到 query time。 |
| **哪些 state 值得保留？** | [SGR-Bench](papers/2605.22219.md) → [RAAC](papers/2608.15191.md) → [LoongReflect](papers/2608.11967.md) → [Context Compression Cost](papers/2608.16370.md) | Environment state、progress state、reversible reasoning state、retained context 的 failure cost 不同。 |
| **怎样让 retrieval claim 更 causal？** | [Training Protocols](papers/2605.27881.md) → [Pi-Serini](papers/2605.10848.md) → [Is Grep All You Need?](papers/2605.15184.md) → [VAKRA](papers/2608.12282.md) | Backend、interface、harness、model、budget、cross-source execution 要分开，才能谈 retrieval policy 的贡献。 |

<a id="library"></a>
## Research Library

历史工作应该按问题和 design tension 找，而不是只按周找。

- **[按 problem / research line / year 浏览](library/README.md)**
- **[Research-question map](categories/README.md)**
- **[Chronological paper index](papers/README.md)**
- **[时间维度 synthesis](digests/README.md)**

## 怎么用这个 Radar

**先扫**一句 Research delta；**再展开**重要论文的 60–90 秒 causal explanation；真正要判断 claim，再进入 paper note 检查 mechanism、closest comparison、negative result、cost 与 attribution。只有问题、没有 paper 名时，从 Field Map 或 Library 进入。

## Scope

纳入的工作需要让 Agent 对**是否、检索什么、去哪里检索、如何检索、检索多少**拥有实质控制，或者改变支持这种控制的 persistent information state。普通 fixed RAG 如果没有真正的 control/interface/state contribution，通常不纳入。

## About / Contributing

这是一个研究判断地图，不是 exhaust feed。证据标准是：**改了什么？相比什么？实际 hold fixed 了什么？还有什么 confounded？**

[Contributing](CONTRIBUTING.md) · [Curation](CURATION.md) · [Daily workflow](docs/DAILY_WORKFLOW.md)
