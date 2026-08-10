# AIStudies

> **Repositório de estudos.** Projetos didáticos e comparativos sobre RAG, agentes, workflows e o stack de IA usado no mercado (2026).  
> Não é um produto comercial — é um portfólio de aprendizado hands-on.

**Autor:** [Cod3G00d](https://github.com/Cod3G00d)  
**Repo:** https://github.com/Cod3G00d/AIStudies

---

## Objetivo

Aprender, na prática, como a indústria monta sistemas com LLMs:

- RAG clássico, hybrid search, rerank e GraphRAG  
- Agentes (ReAct), LangGraph, multiagente e MCP/A2A  
- Memória, context engineering, avaliação e segurança  
- Comparar stacks lado a lado (quando usar cada um)

Cada pasta é um **projeto independente**, com README próprio, setup e o que aquele exercício ensina.

---

## Como navegar (para recrutadores)

| Status | Significado |
|--------|-------------|
| Done | Código funcional + notas do que aprendi |
| In progress | Em construção |
| Planned | Roadmap — README descreve o que será ensinado |

Comece pelos projetos marcados **Done** / **In progress**. Os Planned mostram o currículo completo.

---

## Roadmap de projetos

| # | Pasta | Tema | O que você aprende | Status |
|---|--------|------|--------------------|--------|
| 01 | [`01-compare-models`](./01-compare-models) | Fundamentos de LLM | Chamar modelos, medir latência/tokens/custo, cloud vs local (Ollama) | In progress |
| 02 | [`02-semantic-faq`](./02-semantic-faq) | Embeddings | Similaridade semântica, limiar de confiança, chunking — **sem** framework | Planned |
| 03 | [`03-rag-agent-hello`](./03-rag-agent-hello) | RAG + agente | Chunking, Chroma, retrieval como tool, ReAct com LangGraph/Ollama | Done |
| 04 | [`04-rag-llamaindex-vs-langchain`](./04-rag-llamaindex-vs-langchain) | Comparação RAG | Mesmo corpus em LlamaIndex e LangChain; trade-offs de API e clareza | Planned |
| 05 | [`05-hybrid-rerank`](./05-hybrid-rerank) | RAG de produção | BM25 + vector, rerank, citações; cria o **gold set** de avaliação | Planned |
| 06 | [`06-agentic-rag`](./06-agentic-rag) | Agentic RAG | Agente decide *se/quando* recuperar; vs pipeline RAG fixo | Planned |
| 07 | [`07-memory-layers`](./07-memory-layers) | Memória | Working / episódica / estruturada — memória ≠ só vector DB | Planned |
| 08 | [`08-agent-native`](./08-agent-native) | Agente mínimo | Loop ReAct ~80 linhas com tool calling nativo (sem LangChain) | Planned |
| 09 | [`09-agent-langgraph`](./09-agent-langgraph) | LangGraph | StateGraph, ciclos agent↔tools, checkpoints, debug de estado | Planned |
| 10 | [`10-mcp-tool`](./10-mcp-tool) | MCP | Model Context Protocol: tools como servidor; higiene vs tool poisoning | Planned |
| 11 | [`11-workflow-rpi`](./11-workflow-rpi) | Workflows | Research → Plan → Implement + HITL; context engineering em prática | Planned |
| 12 | [`12-multiagent-sdk`](./12-multiagent-sdk) | Multiagente | CrewAI ou OpenAI Agents SDK vs LangGraph — velocidade vs controle | Planned |
| 13 | [`13-a2a-mini`](./13-a2a-mini) | A2A | Agent Cards e delegação agent↔agent (intro ao protocolo) | Planned |
| 14 | [`14-minigraphrag`](./14-minigraphrag) | GraphRAG caseiro | Entidades/relações + NetworkX; queries globais vs locais | Planned |
| 15 | [`15-ms-graphrag`](./15-ms-graphrag) | Microsoft GraphRAG | Indexação em comunidade; comparar custo/qualidade com vector RAG | Planned |
| 16 | [`16-hermes-study-buddy`](./16-hermes-study-buddy) | Hermes Agent | Agente persistente, skills, memória que acumula entre sessões | Planned |
| 17 | [`17-eval-security-api`](./17-eval-security-api) | Produção enxuta | RAGAS/DeepEval, tracing, FastAPI, sandbox/HITL para tools | Planned |

---

## Stack que aparece ao longo do curso

- **LLMs:** OpenAI / Anthropic / OpenRouter + **Ollama** (local)  
- **RAG:** Chroma → Qdrant/pgvector, hybrid search, rerank  
- **Frameworks:** LangChain, LlamaIndex, **LangGraph**  
- **Agentes:** tool calling nativo, CrewAI / OpenAI Agents SDK, **Hermes Agent**  
- **Protocolos:** **MCP**, intro **A2A**  
- **Qualidade:** gold set, RAGAS/DeepEval, LangSmith / Langfuse / Phoenix  

---

## Princípio de estudo

Em cada projeto: **1 conceito → 1 implementação mínima → 1 comparação**.

Critério de “aprendi”: explicar *quando* usar a abordagem e mostrar trade-off (qualidade, latência, custo, complexidade).

---

## Setup geral

- Python **3.11+** (alguns projetos sugerem 3.12)  
- Cada pasta tem seu `requirements.txt` / `.env.example`  
- **Nunca** commitar `.env` — só `.env.example`  
- Ollama opcional no início; útil para experimentos sem custo de API  

```bash
git clone https://github.com/Cod3G00d/AIStudies.git
cd AIStudies
cd 03-rag-agent-hello   # exemplo já funcional
```

---

## Aviso

Código de **estudo e demonstração**. Não use em produção sem revisão de segurança, avaliação e governança de tools/dados.
