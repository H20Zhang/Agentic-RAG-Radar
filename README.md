# Agentic RAG Radar

**中文** | [English](README.en.md)

追踪 Agent 如何主动获取、检查、控制和保存外部信息。

这个 Radar 主要回答：**检索决策应放在哪里？证据何时形成？哪些状态值得保留？自适应控制到底换来了什么？**

**Radar Family：** [Agent Benchmark Radar](https://github.com/H20Zhang/Agent-Benchmark-Radar) · [Agent Memory](https://github.com/H20Zhang/Agent-Memory-Radar) · **Agentic RAG** · [Data Agent](https://github.com/H20Zhang/Data-Agent-Radar)

[30 秒：最新时间线](#timeline) · [3 分钟：7/30 天变化](#periods) · [5 分钟：领域地图](#field-map) · [15 分钟：阅读路径](#reading-paths) · [浏览全部](#library)

**状态：** 最后更新：**2026-08-24** · 最后合成：**2026-08-24T01:33:36Z（UTC）**

<a id="timeline"></a><a id="latest"></a><a id="latest-papers"></a>
## 最新时间线

> **迁移说明：** 这六条 legacy 记录没有保存历史 Radar 接纳时间，因此按论文公开日期排序，不把它们冒充为“最近被 Radar 接纳”。v2 切换后新增记录按 `radar_published_at` 排序，同时保留原始 `published_at`。

<a id="entry-2608.19652"></a>
<details><summary>2026-08-24 · StateMem · State persistence → supersession-aware state <!-- timefirst:area=supersession-aware-state --> — 把“取回历史”和“判断哪些事实及依赖仍然有效”拆成两个问题。 <!-- timefirst:delta=supersession-aware-state-assembly --></summary>

**问题。** 当检索历史同时包含已作废和仍有效的事实时，agent 能否组装出当前状态？ <!-- timefirst:question=evolving-state-assembly -->

**证据。** StateMem value chain structure：六个 backend 上，StateMemWrapper 在相同 full transcript、chunks、call 与长度预算之外贡献 15.0–31.7 个点。 <!-- timefirst:evidence=statemem-control~statemem-value-chain-structure -->

**限制。** Synthetic benchmark upper bound：benchmark 针对的正是方法所编码的 lazy-reader failure family；完整 StateMem 约用 165–600 次 ingest LLM calls，dependency propagation 有时有害，DeepSeek/LongMemEval 的结构增量仅 −5 到 +5 个点。 <!-- timefirst:caveat=statemem-boundary~synthetic-benchmark-upper-bound -->

**地图。** `early_signal`：为 State persistence 加入 supersession-aware state assembly；单个 benchmark/method package 不构成 durable direction。

**链接。** [Can Agent Memory Systems Track Evolving State?](https://arxiv.org/abs/2608.19652) · [英文深读](papers/2608.19652.md) · [中文深读](papers/2608.19652.zh.md)

</details>

<a id="entry-2608.18613"></a>
<details><summary>2026-08-21 · CTIFoundry · Interface resolution → agent-native corpus scaffold <!-- timefirst:area=agent-native-corpus-scaffold --> — 在同一底层 agent 上，把平面语料改造成具名实体、关系与 typed operations 的证据路径。 <!-- timefirst:delta=typed-evidence-path-operations --></summary>

**问题。** 语料 scaffold 与可操作接口，而非更换 agent，能否改善跨文档证据导航？ <!-- timefirst:question=corpus-scaffold-operation-surface -->

**证据。** four-model panel 全部提升 0.190–0.275 F1；GPT-5.4 从 flat base 0.610 提升到 tools+skills full 0.829，且 tools-only 0.746 高于 skills-only 0.672。 <!-- timefirst:evidence=ctifoundry-package~four-model-panel -->

**限制。** tools skills bundled：完整处理同时改变图/实体索引、七种 typed tools、工具输出与描述、system prompt 及用户轮次 skills；没有对齐每个分支的 online 成本和更新生命周期。 <!-- timefirst:caveat=ctifoundry-attribution~tools-skills-bundled -->

**地图。** `reinforces`：与 VisDocAgentBench 共同加强“在共享输出契约下显式暴露证据路径操作”这一接口轴，不把整套增益归给检索或规划。

**链接。** [CTIFoundry: An Agent-Native Corpus Scaffold for Cyber Threat Intelligence](https://arxiv.org/abs/2608.18613) · [英文深读](papers/2608.18613.md) · [中文深读](papers/2608.18613.zh.md)

</details>

<a id="entry-2608.17889"></a>
<details><summary>2026-08-21 · VisDocAgentBench · Interface resolution → ranked visual retrieval <!-- timefirst:area=ranked-visual-retrieval --> — 用统一 top-10 opaque page 输出测试静态与 iterative visual target discovery。 <!-- timefirst:delta=bridge-path-acquisition-benchmark --></summary>

**问题。** 在页面级视觉检索中，iterative visual target discovery 能否弥补静态检索从直接目标到复杂目标的崩塌？ <!-- timefirst:question=iterative-visual-target-discovery -->

**证据。** iterative search ablation 中，GPT-5.6-sol 视觉路径 R@1 从无迭代的 53.33 提升到 61.67，OCR 路径从 27.50 提升到 36.67；但最强静态 Nemotron 在 L3 仅 2.5%。 <!-- timefirst:evidence=visdoc-iteration~iterative-search-ablation -->

**限制。** input token history 未匹配：完整视觉 agent 约 177K input tokens，对照约 101K；agent 后端是 Qwen single-vector，而最强静态对照是 Nemotron late-interaction。 <!-- timefirst:caveat=visdoc-attribution~input-token-history -->

**地图。** `reinforces`：与 CTIFoundry 一起强化显式证据路径操作，但当前证据不能分离 policy、retriever 与累积历史。

**链接。** [VisDocAgentBench: Benchmarking Agents for Visually Rich Document Retrieval](https://arxiv.org/abs/2608.17889) · [项目](https://hulx2002.github.io/VisDocAgentBench/) · [代码](https://github.com/hulx2002/VisDocAgentBench) · [英文深读](papers/2608.17889.md) · [中文深读](papers/2608.17889.zh.md)

</details>

<a id="entry-2608.16502"></a>
<details><summary>2026-08-21 · ToolScout · Interface resolution → capability retrieval <!-- timefirst:area=capability-retrieval --> — 揭示工具检索器可能把来源风格误当成能力匹配信号。 <!-- timefirst:delta=source-style-capability-routing --></summary>

**问题。** capability retrieval transfer 到混合工具源时，失败来自 agent planning，还是上游候选工具没有被召回？ <!-- timefirst:question=capability-retrieval-transfer -->

**证据。** source-style collapse：专用检索器在匹配来源 depth-20 coverage 为 91.8%，混合来源仅 22.3%；路由到来源聚合器后为 86.1%。 <!-- timefirst:evidence=toolscout-transfer~source-style-collapse -->

**限制。** end-to-end execution missing：工作测量候选覆盖与 proxy generation，并未执行工具完成任务；“来源风格”还混合 query–tool pairing 与目标侧分布。 <!-- timefirst:caveat=toolscout-scope~end-to-end-execution-missing -->

**地图。** `early_signal`：把 capability coverage audit 放到 agent planning 之前；单篇迁移诊断不足以建立稳定方向。

**链接。** [When Tool-Backed Skill Retrieval Fails: Source-Style Collapse in Executable Capability Retrieval](https://arxiv.org/abs/2608.16502) · [英文深读](papers/2608.16502.md) · [中文深读](papers/2608.16502.zh.md)

</details>

<a id="entry-2608.16417"></a>
<details><summary>2026-08-21 · D2-ScaleAgent · Adaptivity placement → evidence-sufficiency routing <!-- timefirst:area=evidence-sufficiency-routing --> — 让 verifier 根据 Evidence Bank 在继续找新页与深入已找到页面之间路由。 <!-- timefirst:delta=breadth-depth-evidence-routing --></summary>

**问题。** breadth versus depth allocation 是否能由当前证据充分性显式控制，而不是固定增加检索轮数？ <!-- timefirst:question=breadth-versus-depth-allocation -->

**证据。** verifier loop ablation：GPT-4o 在 MMLongBench 上完整系统为 52.0，移除 verifier 为 44.1，移除 retrieval scale 为 46.8；oracle 为 54.9。 <!-- timefirst:evidence=d2-verifier~verifier-loop-ablation -->

**限制。** unmatched adaptive compute：完整系统自身为 21.4K tokens、16.22 秒与 5.02 次 routing-agent calls，但未给关键对照的匹配成本；Gemini direct VQA 在两项主 benchmark 上更强。 <!-- timefirst:caveat=d2-attribution~unmatched-adaptive-compute -->

**地图。** `early_signal`：为 evidence-sufficiency routing 增加一个受控信号，不把整套视觉文档 agent 的收益单独归给 verifier。

**链接。** [D2-ScaleAgent: Dual-Dimensional Scaling for Long Document Understanding](https://arxiv.org/abs/2608.16417) · [英文深读](papers/2608.16417.md) · [中文深读](papers/2608.16417.zh.md)

</details>

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
### 过去 7 天 · 2026-08-18—2026-08-24

- **`reinforced` · Evidence path operation surfaces · 显式证据路径操作获得跨任务证据。** <!-- timefirst:direction key="evidence-path-operation-surfaces" state="reinforced" supports="2608.17889,2608.18613" confidence="medium" implication="make-evidence-path-operations-explicit" timing="radar_published_at" synthesized="2026-08-24T01:33:36Z" prior="field-map" -->
  支撑：[VisDocAgentBench](#entry-2608.17889) · [CTIFoundry](#entry-2608.18613)；置信度：**medium**；时间依据：`radar_published_at`；精确合成时间：`2026-08-24T01:33:36Z`（UTC）；研究设计含义（make evidence path operations explicit）：在共享输出契约下显式暴露 search / resolve / traverse / inspect / read，并以匹配后端、harness 与预算的静态对照检验；先验地图证据：[Interface resolution](#field-map)。

- **`new_signal` · Evidence sufficiency routing · 证据充分性可路由广度与深度。** <!-- timefirst:direction key="evidence-sufficiency-routing" state="new_signal" supports="2608.16417" confidence="medium" implication="separate-page-coverage-from-reading-depth" timing="radar_published_at" synthesized="2026-08-24T01:33:36Z" prior="none" -->
  支撑：[D2-ScaleAgent](#entry-2608.16417)；置信度：**medium**；时间依据：`radar_published_at`；精确合成时间：`2026-08-24T01:33:36Z`（UTC）；研究设计含义（separate page coverage from reading depth）：分别测量新页面覆盖和已命中页面的深读，并对齐 verifier 的 token、调用与延迟；先验地图证据：`none`。

- **`new_signal` · Source conditioned capability routing · 工具能力召回受来源分布制约。** <!-- timefirst:direction key="source-conditioned-capability-routing" state="new_signal" supports="2608.16502" confidence="medium" implication="audit-capability-coverage-before-agent-planning" timing="radar_published_at" synthesized="2026-08-24T01:33:36Z" prior="none" -->
  支撑：[ToolScout](#entry-2608.16502)；置信度：**medium**；时间依据：`radar_published_at`；精确合成时间：`2026-08-24T01:33:36Z`（UTC）；研究设计含义（audit capability coverage before agent planning）：先核验候选工具覆盖与跨来源迁移，再把最终失败归因给 agent planning；先验地图证据：`none`。

- **`new_signal` · Supersession aware state assembly · 历史召回与当前有效状态组装可以分开。** <!-- timefirst:direction key="supersession-aware-state-assembly" state="new_signal" supports="2608.19652" confidence="medium" implication="separate-recall-from-state-validity" timing="radar_published_at" synthesized="2026-08-24T01:33:36Z" prior="none" -->
  支撑：[StateMem](#entry-2608.19652)；置信度：**medium**；时间依据：`radar_published_at`；精确合成时间：`2026-08-24T01:33:36Z`（UTC）；研究设计含义（separate recall from state validity）：匹配 transcript access 与 answer cost，并独立改变 supersession、dependency propagation 与 recomputation；先验地图证据：`none`。

<a id="last-30-days"></a>
### 过去 30 天 · 2026-07-26—2026-08-24

- **`reinforced` · Evidence path operation surfaces · 显式证据路径操作获得跨任务证据。** <!-- timefirst:direction key="evidence-path-operation-surfaces" state="reinforced" supports="2608.17889,2608.18613" confidence="medium" implication="make-evidence-path-operations-explicit" timing="radar_published_at" synthesized="2026-08-24T01:33:36Z" prior="field-map" -->
  支撑：[VisDocAgentBench](#entry-2608.17889) · [CTIFoundry](#entry-2608.18613)；置信度：**medium**；时间依据：`radar_published_at`；精确合成时间：`2026-08-24T01:33:36Z`（UTC）；研究设计含义（make evidence path operations explicit）：在共享输出契约下显式暴露 search / resolve / traverse / inspect / read，并以匹配后端、harness 与预算的静态对照检验；先验地图证据：[Interface resolution](#field-map)。

- **`new_signal` · Evidence sufficiency routing · 证据充分性可路由广度与深度。** <!-- timefirst:direction key="evidence-sufficiency-routing" state="new_signal" supports="2608.16417" confidence="medium" implication="separate-page-coverage-from-reading-depth" timing="radar_published_at" synthesized="2026-08-24T01:33:36Z" prior="none" -->
  支撑：[D2-ScaleAgent](#entry-2608.16417)；置信度：**medium**；时间依据：`radar_published_at`；精确合成时间：`2026-08-24T01:33:36Z`（UTC）；研究设计含义（separate page coverage from reading depth）：分别测量新页面覆盖和已命中页面的深读，并对齐 verifier 的 token、调用与延迟；先验地图证据：`none`。

- **`new_signal` · Source conditioned capability routing · 工具能力召回受来源分布制约。** <!-- timefirst:direction key="source-conditioned-capability-routing" state="new_signal" supports="2608.16502" confidence="medium" implication="audit-capability-coverage-before-agent-planning" timing="radar_published_at" synthesized="2026-08-24T01:33:36Z" prior="none" -->
  支撑：[ToolScout](#entry-2608.16502)；置信度：**medium**；时间依据：`radar_published_at`；精确合成时间：`2026-08-24T01:33:36Z`（UTC）；研究设计含义（audit capability coverage before agent planning）：先核验候选工具覆盖与跨来源迁移，再把最终失败归因给 agent planning；先验地图证据：`none`。

- **`new_signal` · Supersession aware state assembly · 历史召回与当前有效状态组装可以分开。** <!-- timefirst:direction key="supersession-aware-state-assembly" state="new_signal" supports="2608.19652" confidence="medium" implication="separate-recall-from-state-validity" timing="radar_published_at" synthesized="2026-08-24T01:33:36Z" prior="none" -->
  支撑：[StateMem](#entry-2608.19652)；置信度：**medium**；时间依据：`radar_published_at`；精确合成时间：`2026-08-24T01:33:36Z`（UTC）；研究设计含义（separate recall from state validity）：匹配 transcript access 与 answer cost，并独立改变 supersession、dependency propagation 与 recomputation；先验地图证据：`none`。

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
| **Interface resolution** | Agent 能观察和控制哪些检索操作与来源状态？ | `opaque top-k ↔ explicit search/resolve/traverse/inspect/read under shared output contract` |
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
