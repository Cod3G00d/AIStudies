# 01 — Compare Models

**Status:** In progress  
**Objetivo:** fundamentos de engenharia com LLMs antes de RAG/agentes.

## O que este projeto ensina

- Chamar um LLM via API (OpenAI-compatible) e/ou **Ollama** local  
- Medir **latência**, **tokens** (quando disponível) e **custo aproximado**  
- Comparar o **mesmo prompt** em mais de um modelo  
- Entender trade-offs cloud vs local (custo, privacidade, qualidade)

## Setup

```bash
cd 01-compare-models
py -3.12 -m venv .venv
.\.venv\Scripts\activate   # Windows
pip install -r requirements.txt
copy .env.example .env     # preencha chaves se for usar API
```

Ollama (opcional):

```bash
ollama pull llama3.2
```

## Rodar

```bash
python src/compare.py
```

## Comparação sugerida

Rode o mesmo prompt em: (1) um modelo via OpenRouter/OpenAI e (2) Ollama. Anote em `NOTES.md`: qualidade subjetiva, tempo e custo.
