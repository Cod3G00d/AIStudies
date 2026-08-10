# AIStudies

> **Study repository.** Hands-on, comparative projects on RAG, agents, workflows, and the AI stack used in industry (2026).  
> This is **not** a commercial product — it is a learning / portfolio monorepo.

**Author:** [Cod3G00d](https://github.com/Cod3G00d)  
**Repo:** https://github.com/Cod3G00d/AIStudies

---

## Goal

Learn, by building, how industry teams ship LLM systems:

- Classic RAG, hybrid search, reranking, and GraphRAG  
- Agents (ReAct), LangGraph, multi-agent workflows, MCP / A2A  
- Memory, context engineering, evaluation, and agent security  
- Compare stacks side by side (when to use each)

Each folder is an **independent project** with its own README, setup, and learning outcomes.

---

## How to navigate (for recruiters)

| Status | Meaning |
|--------|---------|
| Done | Working code + notes on what was learned |
| In progress | Currently being built |
| Planned | Roadmap — README describes what it will teach |

Start with **Done** / **In progress**. Planned folders show the full curriculum.

---

## Project roadmap

| # | Folder | Topic | What you learn | Status |
|---|--------|-------|----------------|--------|
| 01 | [`01-compare-models`](./01-compare-models) | LLM basics | Call models, measure latency/tokens/cost, cloud vs local (Ollama) | In progress |
| 02 | [`02-semantic-faq`](./02-semantic-faq) | Embeddings | Semantic similarity, confidence threshold, chunking — **no** framework | Planned |
| 03 | [`03-rag-agent-hello`](./03-rag-agent-hello) | RAG + agent | Chunking, Chroma, retrieval as a tool, ReAct with LangGraph/Ollama | Done |
| 04 | [`04-rag-llamaindex-vs-langchain`](./04-rag-llamaindex-vs-langchain) | RAG comparison | Same corpus in LlamaIndex and LangChain; API/DX trade-offs | Planned |
| 05 | [`05-hybrid-rerank`](./05-hybrid-rerank) | Production RAG | BM25 + vector, rerank, citations; create the shared **gold set** | Planned |
| 06 | [`06-agentic-rag`](./06-agentic-rag) | Agentic RAG | Agent decides *whether/when* to retrieve; vs fixed RAG pipeline | Planned |
| 07 | [`07-memory-layers`](./07-memory-layers) | Memory | Working / episodic / structured — memory ≠ vector DB only | Planned |
| 08 | [`08-agent-native`](./08-agent-native) | Minimal agent | ReAct loop ~80 lines with native tool calling (no LangChain) | Planned |
| 09 | [`09-agent-langgraph`](./09-agent-langgraph) | LangGraph | StateGraph, agent↔tools cycles, checkpoints, state debugging | Planned |
| 10 | [`10-mcp-tool`](./10-mcp-tool) | MCP | Model Context Protocol: tools as a server; tool-poisoning hygiene | Planned |
| 11 | [`11-workflow-rpi`](./11-workflow-rpi) | Workflows | Research → Plan → Implement + HITL; context engineering in practice | Planned |
| 12 | [`12-multiagent-sdk`](./12-multiagent-sdk) | Multi-agent | CrewAI or OpenAI Agents SDK vs LangGraph — speed vs control | Planned |
| 13 | [`13-a2a-mini`](./13-a2a-mini) | A2A | Agent Cards and agent↔agent delegation (protocol intro) | Planned |
| 14 | [`14-minigraphrag`](./14-minigraphrag) | Homemade GraphRAG | Entity/relation extraction + NetworkX; global vs local queries | Planned |
| 15 | [`15-ms-graphrag`](./15-ms-graphrag) | Microsoft GraphRAG | Community indexing; cost/quality vs vector RAG | Planned |
| 16 | [`16-hermes-study-buddy`](./16-hermes-study-buddy) | Hermes Agent | Persistent agent, skills, memory that compounds across sessions | Planned |
| 17 | [`17-eval-security-api`](./17-eval-security-api) | Lean production | RAGAS/DeepEval, tracing, FastAPI, sandbox/HITL for risky tools | Planned |

---

## Stack covered across the course

- **LLMs:** OpenAI / Anthropic / OpenRouter + **Ollama** (local)  
- **RAG:** Chroma → Qdrant/pgvector, hybrid search, rerank  
- **Frameworks:** LangChain, LlamaIndex, **LangGraph**  
- **Agents:** native tool calling, CrewAI / OpenAI Agents SDK, **Hermes Agent**  
- **Protocols:** **MCP**, intro to **A2A**  
- **Quality:** gold set, RAGAS/DeepEval, LangSmith / Langfuse / Phoenix  

---

## Study principle

For every project: **1 concept → 1 minimal implementation → 1 comparison**.

“I’ve learned it” means you can explain *when* to use the approach and show a measured trade-off (quality, latency, cost, complexity).

---

## General setup

- Python **3.11+** (some projects suggest 3.12)  
- Each folder has its own `requirements.txt` / `.env.example`  
- **Never** commit `.env` — only `.env.example`  
- Ollama is optional early on; useful for zero-API-cost experiments  

```bash
git clone https://github.com/Cod3G00d/AIStudies.git
cd AIStudies
cd 03-rag-agent-hello   # first fully working example
```

---

## Disclaimer

**Study and demo code only.** Do not use in production without security review, evaluation, and governance for tools/data.
