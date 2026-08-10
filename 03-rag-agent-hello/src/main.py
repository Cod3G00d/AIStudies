"""
03 — Hello World: Agent + RAG (local Ollama)

Pipeline:
  documents → chunking → embeddings → vector store → retrieve → LLM

Local stack (no paid API):
  - Chat: llama3.2
  - Embeddings: nomic-embed-text
  - Vector store: Chroma
"""

from pathlib import Path

from dotenv import load_dotenv
from langchain.agents import create_agent  # ReAct agent (decide → tool → answer)
from langchain_chroma import Chroma  # local vector store (persists embeddings on disk)
from langchain_core.documents import Document
# Document ≈ DTO: page_content (text) + metadata (dict with source, etc.)
from langchain_core.messages import HumanMessage
from langchain_core.tools import tool
from langchain_ollama import ChatOllama, OllamaEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter

load_dotenv()

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data"
# Separate folder from an earlier OpenAI attempt — embedding dims differ
DB_DIR = ROOT / "chroma_db_ollama"

LLM_MODEL = "llama3.2"
EMBED_MODEL = "nomic-embed-text"


def build_vectorstore() -> Chroma:
    """Read .txt files under data/, chunk them, and index into Chroma with Ollama embeddings."""
    docs: list[Document] = []
    for path in DATA.glob("*.txt"):
        docs.append(
            Document(
                page_content=path.read_text(encoding="utf-8"),
                metadata={"source": path.name},
            )
        )

    splitter = RecursiveCharacterTextSplitter(chunk_size=300, chunk_overlap=50)
    chunks = splitter.split_documents(docs)

    # OllamaEmbeddings talks to the local server (http://localhost:11434)
    return Chroma.from_documents(
        documents=chunks,
        embedding=OllamaEmbeddings(model=EMBED_MODEL),
        persist_directory=str(DB_DIR),
    )


def make_agent(vectorstore: Chroma):
    """Local LLM + search tool (RAG)."""
    # as_retriever: search interface; k=3 = top-3 chunks
    retriever = vectorstore.as_retriever(search_kwargs={"k": 3})

    @tool
    def search_documents(query: str) -> str:
        """Search relevant snippets in the company knowledge base."""
        hits = retriever.invoke(query)
        if not hits:
            return "No snippets found."
        return "\n\n".join(
            f"[{d.metadata.get('source', '?')}]\n{d.page_content}" for d in hits
        )

    # ChatOllama ≈ ChatOpenAI, but against local Ollama (no API key)
    llm = ChatOllama(model=LLM_MODEL, temperature=0)

    return create_agent(
        llm,
        tools=[search_documents],
        system_prompt=(
            "You are an assistant for Acme Tech. "
            "Use the search_documents tool before answering factual questions about the company. "
            "If the knowledge base does not contain the information, say you do not know. "
            "Keep answers short and direct."
        ),
    )


def main() -> None:
    print(f"Indexing with Ollama ({EMBED_MODEL})...")
    vs = build_vectorstore()
    agent = make_agent(vs)
    print(f"Agent ready ({LLM_MODEL}).\n")

    questions = [
        "How much does the Pro plan cost?",
        "What is RAG according to the documentation?",
        "What is the CEO's phone number?",
    ]

    for q in questions:
        print(f"\n{'=' * 60}\nQuestion: {q}\n{'=' * 60}")
        result = agent.invoke({"messages": [HumanMessage(content=q)]})
        print(result["messages"][-1].content)


if __name__ == "__main__":
    main()
