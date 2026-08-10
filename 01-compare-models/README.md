# 01 — Compare Models

**Status:** In progress  
**Goal:** LLM engineering basics before RAG/agents.

## What this project teaches

- Call an LLM via an OpenAI-compatible API (**DeepSeek-V4-Flash** by default) and/or **Ollama**  
- Measure **latency**, **tokens** (when available), and **approximate cost**  
- Compare the **same prompt** across more than one model  
- Understand cloud vs local trade-offs (cost, privacy, quality)

## Setup

```bash
cd 01-compare-models
py -3.12 -m venv .venv
.\.venv\Scripts\activate   # Windows
pip install -r requirements.txt
copy .env.example .env     # or use the monorepo root .env
```

Default provider: **DeepSeek** (`deepseek-v4-flash`, `https://api.deepseek.com`).

Ollama (optional):

```bash
ollama pull llama3.2
```

## Run

```bash
python src/compare.py
```

## Suggested comparison

Run the same prompt on DeepSeek-V4-Flash and (optional) Ollama. Record in `NOTES.md`: quality, time, and cost.
