"""Compara o mesmo prompt em provedores OpenAI-compatible (API e/ou Ollama)."""

from __future__ import annotations

import os
import time
from dataclasses import dataclass

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

PROMPT = "Em 3 bullets, explique o que é RAG para um desenvolvedor sênior."


@dataclass
class RunResult:
    name: str
    model: str
    text: str
    latency_s: float
    prompt_tokens: int | None
    completion_tokens: int | None
    error: str | None = None


def make_client(api_key: str, base_url: str) -> OpenAI:
    return OpenAI(api_key=api_key or "ollama", base_url=base_url)


def run_once(name: str, client: OpenAI, model: str, prompt: str) -> RunResult:
    started = time.perf_counter()
    try:
        response = client.chat.completions.create(
            model=model,
            messages=[{"role": "user", "content": prompt}],
            temperature=0,
        )
        latency = time.perf_counter() - started
        usage = response.usage
        return RunResult(
            name=name,
            model=model,
            text=(response.choices[0].message.content or "").strip(),
            latency_s=latency,
            prompt_tokens=getattr(usage, "prompt_tokens", None) if usage else None,
            completion_tokens=getattr(usage, "completion_tokens", None) if usage else None,
        )
    except Exception as exc:  # noqa: BLE001 — script didático
        return RunResult(
            name=name,
            model=model,
            text="",
            latency_s=time.perf_counter() - started,
            prompt_tokens=None,
            completion_tokens=None,
            error=str(exc),
        )


def print_result(result: RunResult) -> None:
    print("=" * 60)
    print(f"{result.name} | model={result.model}")
    print(f"latency={result.latency_s:.2f}s | "
          f"prompt_tokens={result.prompt_tokens} | "
          f"completion_tokens={result.completion_tokens}")
    if result.error:
        print(f"ERROR: {result.error}")
    else:
        print(result.text)
    print()


def main() -> None:
    targets: list[tuple[str, OpenAI, str]] = []

    openai_key = os.getenv("OPENAI_API_KEY", "").strip()
    if openai_key:
        targets.append(
            (
                "cloud",
                make_client(openai_key, os.getenv("OPENAI_BASE_URL", "https://api.openai.com/v1")),
                os.getenv("OPENAI_MODEL", "gpt-4o-mini"),
            )
        )

    ollama_model = os.getenv("OLLAMA_MODEL", "").strip()
    if ollama_model:
        targets.append(
            (
                "ollama",
                make_client("ollama", os.getenv("OLLAMA_BASE_URL", "http://localhost:11434/v1")),
                ollama_model,
            )
        )

    if not targets:
        raise SystemExit(
            "Configure OPENAI_API_KEY e/ou OLLAMA_MODEL no .env (veja .env.example)."
        )

    print(f"Prompt:\n{PROMPT}\n")
    for name, client, model in targets:
        print_result(run_once(name, client, model, PROMPT))


if __name__ == "__main__":
    main()
