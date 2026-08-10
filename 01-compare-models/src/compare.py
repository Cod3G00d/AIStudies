"""Compare the same prompt across OpenAI-compatible providers (DeepSeek by default, optional Ollama)."""

from __future__ import annotations

import os
import time
from dataclasses import dataclass
from pathlib import Path

from dotenv import load_dotenv
from openai import OpenAI

# Prefer project .env, then monorepo root .env
_HERE = Path(__file__).resolve().parent
load_dotenv(_HERE.parent / ".env")
load_dotenv(_HERE.parent.parent / ".env")

PROMPT = "In 3 bullets, explain what RAG is to a senior developer."


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


def run_once(
    name: str,
    client: OpenAI,
    model: str,
    prompt: str,
    *,
    disable_thinking: bool = False,
) -> RunResult:
    started = time.perf_counter()
    kwargs: dict = {
        "model": model,
        "messages": [{"role": "user", "content": prompt}],
        "temperature": 0,
    }
    # DeepSeek V4 thinking is on by default; disable for faster/cheaper study runs
    if disable_thinking:
        kwargs["extra_body"] = {"thinking": {"type": "disabled"}}

    try:
        response = client.chat.completions.create(**kwargs)
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
    except Exception as exc:  # noqa: BLE001 — study script
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
    print(
        f"latency={result.latency_s:.2f}s | "
        f"prompt_tokens={result.prompt_tokens} | "
        f"completion_tokens={result.completion_tokens}"
    )
    if result.error:
        print(f"ERROR: {result.error}")
    else:
        print(result.text)
    print()


def main() -> None:
    targets: list[tuple[str, OpenAI, str, bool]] = []

    api_key = (
        os.getenv("DEEPSEEK_API_KEY", "").strip()
        or os.getenv("OPENAI_API_KEY", "").strip()
    )
    if api_key:
        base_url = (
            os.getenv("DEEPSEEK_BASE_URL")
            or os.getenv("OPENAI_BASE_URL")
            or "https://api.deepseek.com"
        )
        model = (
            os.getenv("DEEPSEEK_MODEL")
            or os.getenv("OPENAI_MODEL")
            or "deepseek-v4-flash"
        )
        targets.append(("deepseek", make_client(api_key, base_url), model, True))

    ollama_model = os.getenv("OLLAMA_MODEL", "").strip()
    if ollama_model:
        targets.append(
            (
                "ollama",
                make_client("ollama", os.getenv("OLLAMA_BASE_URL", "http://localhost:11434/v1")),
                ollama_model,
                False,
            )
        )

    if not targets:
        raise SystemExit(
            "Set DEEPSEEK_API_KEY (or OPENAI_API_KEY) in .env — see .env.example."
        )

    print(f"Prompt:\n{PROMPT}\n")
    for name, client, model, disable_thinking in targets:
        print_result(
            run_once(name, client, model, PROMPT, disable_thinking=disable_thinking)
        )


if __name__ == "__main__":
    main()
