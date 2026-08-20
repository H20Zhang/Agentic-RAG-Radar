# Agentic RAG Radar

**中文** | [English](README.en.md)

追踪 Agent 如何主动获取、检查、控制和保存外部信息。

这个 Radar 主要回答：**检索决策应放在哪里？证据何时形成？哪些状态值得保留？自适应控制到底换来了什么？**

**Radar Family：** [Agent Benchmark Radar](https://github.com/H20Zhang/Agent-Benchmark-Radar) · [Agent Memory](https://github.com/H20Zhang/Agent-Memory-Radar) · **Agentic RAG** · [Data Agent](https://github.com/H20Zhang/Data-Agent-Radar)

[30 秒：最新时间线](#timeline) · [3 分钟：7/30 天变化](#periods) · [5 分钟：领域地图](#field-map) · [15 分钟：阅读路径](#reading-paths) · [浏览全部](#library)

**状态：** 最后更新：**2026-08-20** · 最后合成：**2026-08-20T00:00:00Z（UTC）**

<a id="timeline"></a><a id="latest"></a><a id="latest-papers"></a>
## 最新时间线

> **迁移说明：** 这六条 legacy 记录没有保存历史 Radar 接纳时间，因此按论文公开日期排序，不把它们冒充为“最近被 Radar 接纳”。v2 切换后新增记录按 `radar_published_at` 排序，同时保留原始 `published_at`。

<a id="entry-2608.16185"></a>
<details><summary>2026-08-17 · LENS · Evidence materialization <!-- timefirst:area=evidence-materialization --> — 把证据边界从索引时预先固定，改为查询时在原始文档上按预算定位。 <!-- timefirst:delta=query-time-raw-region-localization --></summary>

**问题。** 在动态语料中，固定 chunk/index 与查询时原始文档定位，谁能以可归因的成本取得更完整证据？ <!-- timefirst:question=dynamic-evidence-localization -->

**证据。** D500 上 LENS 为 62.4% EM / 84.8% evidence localization recall，ReAct-style search 为 65.2% / 50.4%；核心增益是证据定位与 grounding，而不是答案 EM。 <!-- timefirst:evidence=lens-grounding~evidence-localization-recall -->

**限制。** 在线 proposal 与 relevance oracle 会增加 online token latency；当前仍缺少与最新索引维护成本对齐的完整生命周期比较。 <!-- timefirst:caveat=lens-cost~online-token-latency -->

**地图。** `early_signal`：进入 Evidence materialization 轴，不凭单篇改写稳定地图。

**链接。** [LENS: In-Context Search via Latent Evidence Exploration over Dynamic Raw Documents](https://arxiv.org/abs/2608.16185) · [英文深读](papers/2608.16185.md) · [中文深读](papers/2608.16185.zh.md)

</details>

<a id="entry-2608.16370"></a>
<details><summary>2026-08-17 · Context Compression Cost · Resource accounting → context reacquisition <!-- timefirst:area=state-persistence-cost --> — 揭示上下文压缩可能把 token 成本转移为后续重新获取式检索。 <!-- timefirst:delta=compression-reacquisition-tax --></summary>

**问题。** 任务完成情况不变时，上下文压缩是否会因丢失可查询状态而产生新的检索成本？ <!-- timefirst:question=compression-reacquisition-cost -->

**证据。** 固定 24-turn protocol 的代表性实验中，retrieval calls surge 从 21.0 增至 63.9，任务完成情况却没有显著变化；oracle 恢复被丢弃但仍可查询的状态后，多数额外交互消失。 <!-- timefirst:evidence=compression-cost~retrieval-calls-surge -->

**限制。** ALFWorld negative boundary 没有同样的激增；检索调用数也不等于完整的耗时或金钱成本。 <!-- timefirst:caveat=environment-boundary~alfworld-negative-boundary -->

**地图。** `early_signal`：把 retained state 与 reacquisition cost 放进同一资源核算，但不由单项结果创建趋势。

**链接。** [What Does Context Compression Cost an Agent? Interaction Costs Unrevealed by Task-Completion Metrics](https://arxiv.org/abs/2608.16370) · [英文深读](papers/2608.16370.md) · [中文深读](papers/2608.16370.zh.md)

</details>

<a id="entry-2608.15191"></a>
<details><summary>2026-08-15 · RAAC · State persistence → progress control <!-- timefirst:area=progress-control --> — 根据 coverage、novelty、query diversity 与 drift 显式决定继续、转向或停止。 <!-- timefirst:delta=observable-search-progress --></summary>

**问题。** 同一个 deep-research agent 能否观察搜索进展，在证据饱和时停下、停滞时改变方向？ <!-- timefirst:question=stagnation-control -->

**证据。** BrowseComp-Plus search calls 平均约减少 14 次，同时平均准确率提高约 3 个百分点；对照是同一底层 agent 加或不加 RAAC overlay。 <!-- timefirst:evidence=raac-overlay~browsecomp-plus-search-calls -->

**限制。** Controller rethinker cost 包含额外 LLM 调用，因此搜索次数减少不能直接解释为总计算成本更低；不同 agent / dataset 的结果也不完全一致。 <!-- timefirst:caveat=raac-cost~controller-rethinker-cost -->

**地图。** `early_signal`：强化 progress state 作为控制面；结论仍需资源匹配与干预拆分。

**链接。** [When Deep Research Agents Stagnate: Enhancing Reasoning with Retrieval-Aware Agent Control](https://arxiv.org/abs/2608.15191) · [英文深读](papers/2608.15191.md) · [中文深读](papers/2608.15191.zh.md)

</details>

<a id="entry-2608.12888"></a>
<details><summary>2026-08-13 · ReFind · Interface resolution → raw-chat retrieval <!-- timefirst:area=retrieval-interface --> — 说明带会话、时间和局部上下文控制的多轮访问，可让原始归档替代一部分预构建语义记忆。 <!-- timefirst:delta=raw-chat-runtime-access --></summary>

**问题。** 在运行时控制条件对齐后，收益来自预构建语义结构，还是来自 agent 可操作的会话、时间和局部上下文接口？ <!-- timefirst:question=structure-versus-interface -->

**证据。** LongMemEval interface ablation 中，完整 interface 为 93.2/89.3，高于 generic multi-round BM25 的 78.7/82.2 与 one-search 的 84.7/68.9；六任务 mean accuracy 为 58.2。 <!-- timefirst:evidence=refind-interface~longmemeval-interface-ablation -->

**限制。** Lifecycle cost unmatched：实验主要面向文本对话，回答时平均仍需约 2.5–2.6 次搜索与 5 次 LLM 调用，不能据此推断结构化记忆普遍无用。 <!-- timefirst:caveat=refind-scope~lifecycle-cost-unmatched -->

**地图。** `early_signal`：进入 Interface resolution 轴；证据支持强 runtime control，不是淘汰 semantic structure。

**链接。** [When Your Agent Opens the Chat App: Agent-Controlled Search over Raw Chat Logs Rivals Structured Memory](https://arxiv.org/abs/2608.12888) · [英文深读](papers/2608.12888.md) · [中文深读](papers/2608.12888.zh.md)

</details>

<a id="entry-2608.11967"></a>
<details><summary>2026-08-12 · LoongReflect · State persistence → reversible search state <!-- timefirst:area=reversible-search-state --> — 让 agent 回滚受污染的分支，保留纠错经验后继续检索。 <!-- timefirst:delta=trajectory-rollback-control --></summary>

**问题。** 长程搜索中，agent 能否删除不可靠的轨迹后缀，避免错误证据继续污染后续动作？ <!-- timefirst:question=reversible-trajectory-recovery -->

**证据。** Qwen2.5-3B 的 seven benchmark F1 平均为 46.15，AgenticRAG-R1 为 33.55；固定 retrieval environment/tool budget 的组件消融支持 reflection/backtracking 与两条训练通道的组合。 <!-- timefirst:evidence=loongreflect-package~seven-benchmark-f1 -->

**限制。** 教师在训练时可查看全局轨迹（privileged teacher information）；当前证据不能把全部增益归因于回滚语义本身。 <!-- timefirst:caveat=loongreflect-attribution~privileged-teacher-information -->

**地图。** `early_signal`：把 reversible state 纳入控制面；单项 recovery-learning package 不构成稳定趋势。

**链接。** [LoongReflect: Boosting Long-Horizon Reflection in Search Agents via Global Perspective Distillation](https://arxiv.org/abs/2608.11967) · [英文深读](papers/2608.11967.md) · [中文深读](papers/2608.11967.zh.md)

</details>

<a id="entry-2608.12282"></a>
<details><summary>2026-08-12 · VAKRA · Interface resolution → cross-source evaluation <!-- timefirst:area=cross-source-evaluation --> — 把 API、文档检索、策略约束与多跳推理放进同一条可重放轨迹。 <!-- timefirst:delta=executable-cross-source-trajectory --></summary>

**问题。** 模型能否在固定评测框架中跨 API 与文档获取证据，同时保持实体 grounding、策略合规与多跳组合？ <!-- timefirst:question=cross-source-grounding -->

**证据。** 最佳模型 single-hop 为 70.4%，compositional API accuracy 约 50–51%，部分 policy-constrained unanswerable setting 低至 2.4%；tool calls 会被重新执行。 <!-- timefirst:evidence=vakra-depth~compositional-api-accuracy -->

**限制。** Fixed ReAct harness 只能隔离模型能力，不能说明哪种 planner、memory 或 retrieval controller 能修复失败；聚合轨迹仍混合多种原因。 <!-- timefirst:caveat=vakra-attribution~fixed-react-harness -->

**地图。** `early_signal`：为跨源执行增加 evaluation coordinate，不把 benchmark 难度直接当作某种 controller 的证据。

**链接。** [VAKRA: Evaluating Multi-Hop Reasoning Across APIs and Retrieval Under Tool-Use Policies](https://arxiv.org/abs/2608.12282) · [代码](https://github.com/IBM/vakra) · [英文深读](papers/2608.12282.md) · [中文深读](papers/2608.12282.zh.md)

</details>

<a id="periods"></a><a id="changes"></a><a id="whats-changing"></a>
## 7 天 / 30 天变化

方向条目只按 Radar 接纳时间判断；legacy 论文仍可提供领域背景，但不能冒充滚动窗口支撑。

<a id="last-7-days"></a>
### 过去 7 天 · 2026-08-14—2026-08-20

- **`no_material_change` · RAG Radar acceptance time 暂无可报告变化。** <!-- timefirst:direction key="rag-radar-acceptance-time" state="no_material_change" supports="none" confidence="high" implication="require-native-v2-times-for-period-claims" timing="radar_published_at" synthesized="2026-08-20T00:00:00Z" prior="none" -->
  支撑：**none**；置信度：**high**；时间依据：`radar_published_at`；精确合成时间：`2026-08-20T00:00:00Z`（UTC）；研究设计含义（require native v2 times for period claims）：只有带原生 Radar 接纳时间的记录才能支持窗口判断；先验地图证据：`none`。

<a id="last-30-days"></a>
### 过去 30 天 · 2026-07-22—2026-08-20

- **`no_material_change` · RAG Radar acceptance time 暂无可报告变化。** <!-- timefirst:direction key="rag-radar-acceptance-time" state="no_material_change" supports="none" confidence="high" implication="require-native-v2-times-for-period-claims" timing="radar_published_at" synthesized="2026-08-20T00:00:00Z" prior="none" -->
  支撑：**none**；置信度：**high**；时间依据：`radar_published_at`；精确合成时间：`2026-08-20T00:00:00Z`（UTC）；研究设计含义（require native v2 times for period claims）：只有带原生 Radar 接纳时间的记录才能支持窗口判断；先验地图证据：`none`。

封闭周期与长期压缩：[weekly](digests/README.md) · [monthly](digests/monthly/2026-08.md) · [yearly](digests/yearly/2026.md)

<a id="field-map"></a><a id="research-map"></a>
## 领域地图

![Agentic RAG 领域设计轴](assets/editorial/field-overview.svg)

> **先建立一个简单模型：** `need information → search/access evidence → inspect → decide where/if to search again → answer or act`
>
> **当前判断：** “retriever 还是 agent”“一次 search 还是多次 search”都太粗。更稳定的设计轴是：**adaptivity 放在哪、evidence 何时 materialize、哪些 state 跨 action 保留、offline + online 到底花了多少资源。**

`information need → query/planning → retrieval interface → evidence materialization → inspection/reasoning → continue/redirect/stop → persistent state → answer/action`

| Axis | 核心问题 | 当前张力 |
|---|---|---|
| **Adaptivity placement** | 哪些操作可以在看到证据前预先编排，哪些必须根据返回结果调整？ | `pre-query compilation ↔ query-time adaptation` |
| **Evidence materialization** | 何时应把文本块、区域或工作区固化为可操作对象？ | `pre-materialized index ↔ raw/query-conditioned evidence` |
| **Interface resolution** | Agent 能观察和控制哪些检索操作与来源状态？ | `opaque top-k ↔ explicit search/read/filter/navigation` |
| **State persistence** | 哪些证据、进度和推理状态应跨动作保留？ | `stateless loop ↔ persistent/recoverable state` |
| **Resource accounting** | 哪种方案的生命周期总成本更低？ | `local retrieval metric ↔ lifecycle cost + task outcome` |

[进入完整 research-question map →](categories/README.md) · [Research-question visual](assets/editorial/research-question-map.svg) · [看这个方向如何被评价 →](https://github.com/H20Zhang/Agent-Benchmark-Radar#benchmark-rag)

<a id="reading-paths"></a>
## 阅读路径

| 你想回答的问题 | 建议顺序 | 应该学到什么 |
|---|---|---|
| **检索控制和证据形成应放在哪个环节？** | [SIRA](papers/2605.06647.md) → [DCI](papers/2605.05242.md) → [ReFind](papers/2608.12888.md) → [LENS](papers/2608.16185.md) | 有些检索决策可以预先编排；有些信息只有读到证据后才可见；连证据粒度也可以推迟到查询时再决定。 |
| **哪些状态值得保留？** | [SGR-Bench](papers/2605.22219.md) → [RAAC](papers/2608.15191.md) → [LoongReflect](papers/2608.11967.md) → [Context Compression Cost](papers/2608.16370.md) | 环境状态、进度状态、可回滚推理状态和保留上下文的失败成本各不相同。 |
| **怎样对检索结论做因果归因？** | [Training Protocols](papers/2605.27881.md) → [Pi-Serini](papers/2605.10848.md) → [Is Grep All You Need?](papers/2605.15184.md) → [VAKRA](papers/2608.12282.md) | 只有把后端、接口、评测框架、模型、预算和跨来源执行分开，才能判断检索策略的贡献。 |

<a id="library"></a>
## 研究资料库

历史工作可按问题与设计张力浏览，也可按论文或时间查找。

[按问题、研究路线与年份浏览](library/README.md) · [研究问题地图](categories/README.md) · [论文时间索引](papers/README.md) · [时间维度综述](digests/README.md)

## 怎么用这个 Radar

**先扫**时间线折叠行；**再展开**问题、证据、限制与地图影响；需要核验结论时进入深读。只有问题、没有论文名时，从领域地图或资料库进入。

## 收录范围

纳入的工作需要让 Agent 对**是否、检索什么、去哪里检索、如何检索、检索多少**拥有实质控制，或者改变支持这种控制的持久信息状态。普通固定式 RAG 如果没有真正的控制、接口或状态贡献，通常不纳入。

## 维护

这是研究判断地图，而不是穷举式信息流。证据标准是：**改了什么？与什么比较？实际固定了什么？还有哪些混杂因素？**

[Contributing](CONTRIBUTING.md) · [Curation](CURATION.md) · [Daily workflow](docs/DAILY_WORKFLOW.md)
