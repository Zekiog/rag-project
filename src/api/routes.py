from functools import lru_cache

from fastapi import FastAPI
from pydantic import BaseModel

from src.embeddings.embedder import Embedder
from src.llm.llm_client import LLMClient
from src.prompts.prompt_templates import build_qa_prompt
from src.retrieval.retriever import Retriever
from src.utils.helpers import load_config
from src.vectordb.vector_store import VectorStore

app = FastAPI(title="rag-project")

@lru_cache
def get_pipeline():
    cfg = load_config()
    embedder = Embedder(model=cfg["embedding"]["model"])
    store = VectorStore(collection=cfg["vectordb"]["collection"])
    retriever = Retriever(embedder, store)
    llm = LLMClient(model=cfg["llm"]["model"],
                    temperature=cfg["llm"]["temperature"])
    return retriever, llm

class QueryRequest(BaseModel):
    question: str

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/query")
def query(req: QueryRequest):
    retriever, llm = get_pipeline()
    hits = retriever.retrieve(req.question)
    context = "\n\n".join(h["text"] for h in hits)
    answer = llm.complete(build_qa_prompt(context, req.question))
    return {"answer": answer,
            "sources": sorted({h["source"] for h in hits})}
