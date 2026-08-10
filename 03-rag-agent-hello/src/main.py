"""
01 — Hello World: Agente + RAG (Ollama local)

Pipeline:
  documentos → chunking → embeddings → vector store → retrieve → LLM

Stack local (sem API paga):
  - Chat: llama3.2
  - Embeddings: nomic-embed-text
  - Vector store: Chroma
"""

from pathlib import Path

from dotenv import load_dotenv
from langchain.agents import create_agent  # agente ReAct (decide → tool → responde)
from langchain_chroma import Chroma  # vector store local (persiste embutidos em disco)
from langchain_core.documents import Document
# Document ≈ DTO: page_content (texto) + metadata (dict com source, etc.)
from langchain_core.messages import HumanMessage
from langchain_core.tools import tool
from langchain_ollama import ChatOllama, OllamaEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter

load_dotenv()

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data"
# Pasta separada da época OpenAI — dimensões de embedding são diferentes
DB_DIR = ROOT / "chroma_db_ollama"

LLM_MODEL = "llama3.2"
EMBED_MODEL = "nomic-embed-text"


def build_vectorstore() -> Chroma:
    """Lê .txt em data/, faz chunking e indexa no Chroma com embeddings Ollama."""
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

    # OllamaEmbeddings fala com o servidor local (http://localhost:11434)
    return Chroma.from_documents(
        documents=chunks,
        embedding=OllamaEmbeddings(model=EMBED_MODEL),
        persist_directory=str(DB_DIR),
    )


def make_agent(vectorstore: Chroma):
    """LLM local + tool de busca (RAG)."""
    # as_retriever: interface de busca; k=3 = top-3 chunks
    retriever = vectorstore.as_retriever(search_kwargs={"k": 3})

    @tool
    def buscar_documentos(pergunta: str) -> str:
        """Busca trechos relevantes na base de conhecimento da empresa."""
        hits = retriever.invoke(pergunta)
        if not hits:
            return "Nenhum trecho encontrado."
        return "\n\n".join(
            f"[{d.metadata.get('source', '?')}]\n{d.page_content}" for d in hits
        )

    # ChatOllama = ChatOpenAI, mas contra o Ollama local (sem API key)
    llm = ChatOllama(model=LLM_MODEL, temperature=0)

    return create_agent(
        llm,
        tools=[buscar_documentos],
        system_prompt=(
            "Você é um assistente da Acme Tech. "
            "Use a tool buscar_documentos antes de responder fatos sobre a empresa. "
            "Se a base não tiver a informação, diga que não sabe. "
            "Responda de forma curta e objetiva."
        ),
    )


def main() -> None:
    print(f"Indexando com Ollama ({EMBED_MODEL})...")
    vs = build_vectorstore()
    agent = make_agent(vs)
    print(f"Agente pronto ({LLM_MODEL}).\n")

    perguntas = [
        "Quanto custa o plano Pro?",
        "O que é RAG segundo a documentação?",
        "Qual o telefone do CEO?",
    ]

    for q in perguntas:
        print(f"\n{'=' * 60}\nPergunta: {q}\n{'=' * 60}")
        result = agent.invoke({"messages": [HumanMessage(content=q)]})
        print(result["messages"][-1].content)


if __name__ == "__main__":
    main()
