# 03 — RAG + Agente (Hello World)

**Status:** Done  
**Stack:** LangChain · LangGraph · Chroma · Ollama

## O que este projeto ensina

1. Carregar documentos e fazer **chunking** (`RecursiveCharacterTextSplitter`)  
2. **Embeddings** + persistência no **Chroma**  
3. Retrieval exposto como **tool** do agente  
4. Loop **ReAct** (LangGraph / `create_agent`): decide → tool → responde  
5. Rodar tudo **local** com Ollama (sem API paga)

> Use **Python 3.12**. Ollama precisa estar rodando (`ollama list`).

## Setup

```bash
cd 03-rag-agent-hello
py -3.12 -m venv .venv
.\.venv\Scripts\activate
pip install -r requirements.txt
# ollama pull llama3.2
# ollama pull nomic-embed-text
```

## Rodar

```bash
python src/main.py
```

## Por que este projeto existe no currículo

É o primeiro contato **end-to-end** com RAG + agente. Os projetos seguintes isolam e aprofundam cada peça (hybrid search, eval, memória, MCP, etc.).
