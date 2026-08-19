# Design Anchors

These are **design points, not a ranking**. The goal is to expose the smallest set of abstractions needed to reason about the current Agentic RAG information-acquisition stack.

[Latest Papers](../README.md#-latest-papers) · [What's Changing](../README.md#-whats-changing) · [Reading Paths](../README.md#-reading-paths) · [Research Map](../categories/README.md) · [Curated Paper Index](README.md)

| Paper | Design point | Research card |
|---|---|---|
| **SIRA** | compile a corpus-aware retrieval action **before** evidence inspection | [2605.06647](2605.06647.md) |
| **A-RAG** | expose retrieval as a model-controlled hierarchy of search/read operations | [2602.03442](2602.03442.md) |
| **Direct Corpus Interaction (DCI)** | make raw-corpus interface resolution first-class instead of accepting fixed top-k evidence delivery | [2605.05242](2605.05242.md) |
| **RISE** | use retrieval to construct a bounded persistent interaction space while preserving local corpus operations | [2606.06880](2606.06880.md) |
| **RARG** | keep relevance active as an execution prior inside direct interaction rather than only as a candidate filter | [2607.24223](2607.24223.md) |
| **ReFind** | preserve raw history and move semantic work into substrate-native question-time search when later queries depend on newly revealed cues | [2608.12888](2608.12888.md) |
| **LENS** | defer **evidence materialization** itself until query time over dynamic raw documents | [2608.16185](2608.16185.md) |
| **S2G-RAG** | represent evidence sufficiency and missing information explicitly so state drives the next retrieval action | [2604.23783](2604.23783.md) |
| **RAAC** | make search progress/stagnation observable and map it to continue, redirect, or stop | [2608.15191](2608.15191.md) |
| **LoongReflect** | make active reasoning/search state reversible with explicit rollback and recovery | [2608.11967](2608.11967.md) |
| **Context Compression Cost** | make state **recoverability and reacquisition cost** part of retrieval accounting | [2608.16370](2608.16370.md) |
| **SGR-Bench** | separate finding a source from putting the external system into the correct retrieval state | [2605.22219](2605.22219.md) |
| **Training Protocols** | require answer-bearing evidence and a valid training environment before attributing reward gains to search policy learning | [2605.27881](2605.27881.md) |

## How to read the anchors

A useful progression is:

`evidence exists → corpus is observable → work is compiled/materialized or deferred → interface exposes actions → evidence changes control → progress/state is retained or repaired → displaced work is charged over the lifecycle`

This makes the central systems tension more precise than `retriever vs agent` or `one search vs many`:

**`precompute / materialize / retain ↔ defer / localize / reacquire`**.

The left side spends work before or between queries: corpus enrichment, indexes, structured memory, persistent evidence, and retained execution state. The right side preserves rawer substrates and buys information later through query-time localization, repeated retrieval, controller computation, or state reacquisition. Neither side is inherently more agentic or more efficient.

## Three boundaries that should not be collapsed

**Interface is not policy.** A-RAG, DCI, RISE, and RARG show that what an agent can express and inspect can change outcomes even before asking whether its controller is better.

**Materialization is not adaptivity.** SIRA asks what can be compiled before seeing result passages; ReFind asks when later searches need cues exposed by earlier results; LENS asks an earlier question still—whether evidence units should exist before the query at all.

**State size is not state cost.** S2G-RAG and RAAC expose useful state abstractions, LoongReflect makes active state editable, and the context-compression study shows that deleting state can simply move work into external retrieval when that state must be bought back.

SGR-Bench and Training Protocols guard the outside of this loop: the right internal controller cannot recover evidence that the environment does not contain or does not expose under the current source state.

## Evidence bar implied by the anchors

A strong new paper should identify **which variable changed** and hold the neighboring ones as fixed as possible:

`evidence coverage × corpus observability × materialization/interface × environment state × harness/delivery × agent state × policy × realized offline+online resources × base model × training protocol × historical baseline`.

The most useful future experiments are therefore not larger end-to-end leaderboards. They are matched substitutions that answer questions such as: should this work be paid offline or online; did a richer operation surface or a better controller cause the gain; and did removed context/index/search work reappear somewhere else?

## Caveat

Anchors are promoted only when they change the field map or evidence standard. They should not become an exhaustive paper list; use the [Curated Paper Index](README.md) and [Research Map](../categories/README.md) for broader coverage.
