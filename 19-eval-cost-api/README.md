# 19 — Eval, Cost, Security, and API

**Status:** Planned

## What this project teaches

- Evaluate in **two layers**: retrieval (hit rate, MRR, precision@k) and generation (faithfulness, relevance, LLM-as-judge)
- **Cost engineering**: prompt caching, semantic cache, model routing, fallbacks
- Tracing (LangSmith / Langfuse / Phoenix)
- Expose `/ask` with FastAPI, SSE streaming, limits, and HITL for risky tools
