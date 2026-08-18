import sys

from src.chunking.chunker import chunk_documents
from src.embeddings.embedder import Embedder
from src.ingestion.loader import load_documents
from src.utils.helpers import load_config, setup_logging
from src.vectordb.vector_store import VectorStore

def ingest():
    logger = setup_logging()
    cfg = load_config()
    docs = load_documents()
    chunks = chunk_documents(docs,
                             cfg["chunking"]["chunk_size"],
                             cfg["chunking"]["overlap"])
    if not chunks:
        logger.warning("data/ bos — indexlenecek belge yok.")
        return
    embedder = Embedder(cfg["embedding"]["model"])
    store = VectorStore(cfg["vectordb"]["collection"])
    store.add(ids=[c["chunk_id"] for c in chunks],
              texts=[c["text"] for c in chunks],
              embeddings=embedder.embed([c["text"] for c in chunks]),
              metadatas=[{"source": c["source"]} for c in chunks])
    logger.info("%d chunk vector DB'ye eklendi.", len(chunks))

if __name__ == "__main__":
    cmd = sys.argv[1] if len(sys.argv) > 1 else "ingest"
    if cmd == "ingest":
        ingest()
