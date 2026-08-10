# 03 — RAG + Agent (Hello World)

**Status:** Done  
**Stack:** LangChain · LangGraph · Chroma · Ollama

## What this project teaches

1. Load documents and apply **chunking** (`RecursiveCharacterTextSplitter`)  
2. **Embeddings** + persistence in **Chroma**  
3. Expose retrieval as an agent **tool**  
4. **ReAct** loop (LangGraph / `create_agent`): decide → tool → answer  
5. Run everything **locally** with Ollama (no paid API)

> Use **Python 3.12**. Ollama must be running (`ollama list`).

## Setup

```bash
cd 03-rag-agent-hello
py -3.12 -m venv .venv
.\.venv\Scripts\activate
pip install -r requirements.txt
# ollama pull llama3.2
# ollama pull nomic-embed-text
```

## Run

```bash
python src/main.py
```

## Why this project sits here

First **end-to-end** contact with RAG + an agent. Later projects isolate and deepen each piece (hybrid search, eval, memory, MCP, etc.).
